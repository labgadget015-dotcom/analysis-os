# API Integration Guide

Complete guide for integrating Analysis & AI Consulting OS with client systems via REST API. Covers authentication, endpoints, webhooks, and common integration patterns.

## Table of Contents
1. [Authentication](#authentication)
2. [Base Endpoints](#base-endpoints)
3. [Core API Operations](#core-api-operations)
4. [Webhooks](#webhooks)
5. [Integration Patterns](#integration-patterns)
6. [Error Handling](#error-handling)
7. [Rate Limiting](#rate-limiting)
8. [Troubleshooting](#troubleshooting)

---

## Authentication

### API Key Authentication

All API requests require an `X-API-Key` header with your authentication token.

```bash
curl -H "X-API-Key: your_api_key_here" \
     https://api.analysis-os.io/v1/analyses
```

### Obtaining API Keys

1. Log in to your Analysis & AI Consulting OS dashboard
2. Navigate to Settings → API Keys
3. Click "Create New Key"
4. Give your key a descriptive name (e.g., "CRM Integration", "Data Pipeline")
5. Select the required scopes (read, write, admin)
6. Copy the key and store securely

**Security Best Practices:**
- Rotate keys every 90 days
- Use different keys for different applications
- Never commit keys to version control
- Use environment variables for key storage
- Monitor key usage in the Activity Log

---

## Base Endpoints

### API Base URL

```
https://api.analysis-os.io/v1
```

### Health Check

**GET** `/health`

```bash
curl -H "X-API-Key: your_api_key" \
     https://api.analysis-os.io/v1/health
```

Response:
```json
{
  "status": "healthy",
  "version": "1.2.0",
  "timestamp": "2024-01-15T10:30:00Z"
}
```

---

## Core API Operations

### Data Uploads

**POST** `/data/upload`

Upload transaction or customer data for analysis.

```bash
curl -X POST \
     -H "X-API-Key: your_api_key" \
     -H "Content-Type: application/json" \
     https://api.analysis-os.io/v1/data/upload \
     -d '{
       "source_name": "crm_monthly_export",
       "data_type": "transactions",
       "period": "2024-01",
       "records": 1500,
       "file_url": "s3://your-bucket/data.csv"
     }'
```

### Analysis Requests

**POST** `/analyses/create`

Trigger a new analysis on uploaded data.

```bash
curl -X POST \
     -H "X-API-Key: your_api_key" \
     https://api.analysis-os.io/v1/analyses/create \
     -d '{
       "type": "churn",
       "lookback_days": 90,
       "client_id": "client_12345",
       "priority": "standard"
     }'
```

Response:
```json
{
  "analysis_id": "analysis_xyz789",
  "type": "churn",
  "status": "processing",
  "created_at": "2024-01-15T10:35:00Z",
  "estimated_completion": "2024-01-15T11:35:00Z"
}
```

### Retrieve Results

**GET** `/analyses/{analysis_id}/results`

Get results of a completed analysis.

```bash
curl -H "X-API-Key: your_api_key" \
     https://api.analysis-os.io/v1/analyses/analysis_xyz789/results
```

Response:
```json
{
  "analysis_id": "analysis_xyz789",
  "status": "completed",
  "summary": {
    "total_customers": 5000,
    "churn_rate": 8.5,
    "at_risk_customers": 425
  },
  "insights": [
    {
      "segment": "high_value",
      "churn_risk": "high",
      "estimated_impact": 125000
    }
  ],
  "recommendations": [
    "Focus retention efforts on high_value segment",
    "Implement win-back campaign for 45+ day inactive customers"
  ]
}
```

### Get Status

**GET** `/analyses/{analysis_id}/status`

Check analysis processing status.

```bash
curl -H "X-API-Key: your_api_key" \
     https://api.analysis-os.io/v1/analyses/analysis_xyz789/status
```

---

## Webhooks

### Webhook Configuration

Configure webhooks to receive real-time notifications when analyses complete.

**POST** `/webhooks/create`

```bash
curl -X POST \
     -H "X-API-Key: your_api_key" \
     https://api.analysis-os.io/v1/webhooks/create \
     -d '{
       "url": "https://your-system.com/webhooks/analysis-complete",
       "events": ["analysis.completed", "analysis.failed"],
       "active": true,
       "retry_policy": "exponential"
     }'
```

### Webhook Payload Example

```json
{
  "event_type": "analysis.completed",
  "analysis_id": "analysis_xyz789",
  "timestamp": "2024-01-15T11:35:00Z",
  "status": "completed",
  "results_url": "https://api.analysis-os.io/v1/analyses/analysis_xyz789/results",
  "summary": {
    "duration_seconds": 3600,
    "records_processed": 50000,
    "findings_count": 12
  }
}
```

### Webhook Security

All webhook payloads include an `X-Signature` header for verification:

```python
import hmac
import hashlib

def verify_webhook(payload, signature, webhook_secret):
    expected_signature = hmac.new(
        webhook_secret.encode(),
        payload.encode(),
        hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(signature, expected_signature)
```

---

## Integration Patterns

### Pattern 1: Real-Time Analysis Pipeline

```
[CRM System] 
    ↓ (Daily export)
[Your System] 
    ↓ (POST /data/upload)
[Analysis OS] 
    ↓ (Webhook notification)
[Your Dashboard] (Display results)
```

### Pattern 2: Scheduled Batch Analysis

```python
import schedule
import requests
import os

def run_analysis():
    api_key = os.getenv('ANALYSIS_OS_API_KEY')
    
    # Upload latest data
    response = requests.post(
        'https://api.analysis-os.io/v1/data/upload',
        headers={'X-API-Key': api_key},
        json={
            'source_name': 'daily_export',
            'data_type': 'transactions',
            'file_url': 's3://bucket/latest.csv'
        }
    )
    
    # Trigger analysis
    requests.post(
        'https://api.analysis-os.io/v1/analyses/create',
        headers={'X-API-Key': api_key},
        json={'type': 'churn', 'lookback_days': 90}
    )

schedule.every().day.at("02:00").do(run_analysis)
```

### Pattern 3: Streaming Updates

For high-frequency data, stream updates incrementally:

```bash
curl -X POST \
     -H "X-API-Key: your_api_key" \
     https://api.analysis-os.io/v1/data/stream \
     -d '{"stream_id": "stream_123", "data": [...]}'
```

---

## Error Handling

### HTTP Status Codes

| Code | Meaning | Action |
|------|---------|--------|
| 200 | Success | Process response |
| 400 | Bad Request | Check request format |
| 401 | Unauthorized | Verify API key |
| 403 | Forbidden | Check key permissions |
| 429 | Rate Limited | Implement backoff |
| 500 | Server Error | Retry with exponential backoff |

### Error Response Format

```json
{
  "error": "invalid_data_format",
  "message": "CSV file must contain customer_id and timestamp columns",
  "code": 400,
  "request_id": "req_abc123"
}
```

---

## Rate Limiting

### Limits by Plan

| Plan | Requests/Hour | Concurrent | Max File Size |
|------|---------------|-----------|---------------|
| Starter | 100 | 2 | 10MB |
| Professional | 1000 | 10 | 100MB |
| Enterprise | Unlimited | Unlimited | 1GB |

### Rate Limit Headers

Every response includes:

```
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 987
X-RateLimit-Reset: 1705324800
```

---

## Troubleshooting

### Common Issues

**Problem:** Authentication fails
- Verify API key is correct
- Check key hasn't expired
- Ensure X-API-Key header is present

**Problem:** Analysis takes too long
- Check data size (> 1GB may take hours)
- Verify no rate limiting
- Contact support if > 24 hours

**Problem:** Missing data in results
- Confirm all required columns in upload
- Check data quality score in upload response
- Run data validation report

**Problem:** Webhook not receiving notifications
- Verify webhook URL is publicly accessible
- Check webhook is active
- Review webhook delivery logs
- Ensure firewall allows inbound traffic

---

## Support

For API issues:
- Email: api-support@analysis-os.io
- Docs: https://docs.analysis-os.io
- Status: https://status.analysis-os.io
