# Churn Analysis Example

## Overview

This example demonstrates how to use the Analysis OS framework to conduct a complete churn analysis for a SaaS subscription service. Follow this walkthrough to understand the 5-stage pipeline in action.

---

## Stage 1: Data Preparation

### Checklist Used
Refer to `checklists/master_analysis_checklist.md` → Data Preparation section

### Actions Taken
- ✅ Collected customer data from CRM and billing systems
- ✅ Verified data completeness (95% complete, acceptable threshold)
- ✅ Cleaned duplicates and standardized date formats
- ✅ Created churn flag (1 = churned, 0 = active)

### Dataset Profile
```
Rows: 15,432 customers
Date Range: Jan 2023 - Dec 2024
Key Features: 
- Customer tenure (months)
- Monthly recurring revenue (MRR)
- Support tickets count
- Product usage score (0-100)
- Last login date
- Subscription tier (Basic/Pro/Enterprise)
```

---

## Stage 2: Core Analysis

### Prompt Used
`prompts/use_cases/churn/PROMPT.md` → Data Profile + Core Analysis sections

### AI Instruction
```
You are an experienced data scientist analyzing customer churn for a B2B SaaS company.

Dataset: 15,432 customers, 2 years historical data
Objective: Identify top 3 churn drivers and quantify impact
Constraints: Focus on actionable features (exclude non-controllable factors)
```

### Key Findings
1. **Low Product Engagement**
   - Customers with usage score <30 have 68% churn rate
   - Active users (score >70) only 12% churn rate
   - 2,340 customers currently in danger zone

2. **Support Ticket Volume**
   - 5+ tickets in 30 days → 45% churn risk
   - 0-2 tickets → 8% baseline churn
   - Unresolved tickets increase risk by 3.2x

3. **Tenure Cliff**
   - 41% of churn happens in months 3-6
   - After 12 months, churn drops to 5% annually
   - Onboarding quality is critical

---

## Stage 3: Drill-Down

### Iteration Prompt
Used `prompts/core/drill_down.md`:
```
Break down churn by subscription tier and usage patterns.
Which segment shows highest ROI for retention efforts?
```

### Drill-Down Results

#### By Tier
| Tier | Customers | Churn Rate | Avg MRR | Total At-Risk MRR |
|------|-----------|------------|---------|-------------------|
| Basic | 8,200 | 32% | $29 | $75,968 |
| Pro | 5,800 | 18% | $99 | $103,284 |
| Enterprise | 1,432 | 9% | $599 | $77,229 |

**Insight**: Pro tier has highest at-risk revenue despite lower churn rate.

#### By Usage Pattern
- **Power Users** (>80 score): 420 customers, 3% churn, $249k MRR
- **Regular Users** (40-80): 7,100 customers, 15% churn, $531k MRR  
- **Light Users** (<40): 5,200 customers, 42% churn, $187k MRR
- **Ghost Users** (0 usage): 2,712 customers, 89% churn, $79k MRR

---

## Stage 4: Actionization

### Prompt Used
`prompts/core/actionize.md` + `templates/recommendation_table.md`

### Recommendations Generated

| Recommendation | Development | Marketing | Other | Total | Expected Return | ROI |
|----------------|-------------|-----------|-------|-------|-----------------|-----|
| **Rec 1**: Launch automated onboarding program for Basic/Pro tiers (weeks 1-8) | $12k | $3k | $2k | $17k | $180k/year | [B]x |
| **Rec 2**: Implement usage alerts + CSM intervention for customers with score drop >20pts | $8k | $1k | $5k (CS hiring) | $14k | $124k/year | [A]x |
| **Rec 3**: Create "ghost user" win-back campaign with simplified onboarding | $5k | $8k | - | $13k | $47k/year | [C]x |
| **Total** | $25k | $12k | $7k | **$44k** | **$351k/year** | **[A]x** |

**Assumptions**:
- 40% of at-risk Pro customers saved = $41k MRR preserved
- 25% Basic tier improvement = $19k MRR
- Ghost user 15% reactivation = $12k MRR
- Annual value = 12x monthly recurring revenue

---

## Stage 5: Iteration & Validation

### Success Metrics (from `templates/recommendation_table.md`)

#### 30-Day Metrics
- [ ] Onboarding program launched for 100 test customers
- [ ] Usage alert system deployed
- [ ] Baseline churn rate measured: 24.3%

#### 90-Day Metrics
- [ ] Test cohort churn rate vs control
- [ ] Pro tier at-risk MRR reduced by 15%
- [ ] Support ticket resolution time <48hrs

#### 180-Day Metrics
- [ ] Overall churn reduced to <20%
- [ ] Ghost user reactivation rate >10%
- [ ] ROI validation: $351k revenue impact achieved

### Next Steps
1. [ ] Get stakeholder buy-in on recommendations (Priority 1 & 2 first)
2. [ ] Allocate $44k budget across Q1
3. [ ] Set up tracking dashboard with weekly KPIs
4. [ ] Launch Rec 1 pilot with 500 Basic tier customers
5. [ ] Schedule monthly review cadence

---

## Files Used in This Example

```
/checklists/master_analysis_checklist.md  → Data prep validation
/prompts/core/data_prep.md                → Stage 1 guidance
/prompts/core/core_analysis.md            → Stage 2 framework
/prompts/core/drill_down.md               → Stage 3 deep-dive
/prompts/core/actionize.md                → Stage 4 recommendations
/prompts/use_cases/churn/PROMPT.md        → Domain-specific template
/templates/output_template.md             → Structured output format
/templates/recommendation_table.md        → Financial modeling
/config.yaml                              → Quality gates & thresholds
```

---

## Key Takeaways

1. **Systematic Approach Works**: Following the 5-stage pipeline prevented analysis paralysis and ensured completeness
2. **Prompts Save Time**: Pre-configured templates reduced setup from 2 hours to 15 minutes
3. **Validation is Critical**: Config.yaml quality gates caught 3 data issues early
4. **Actionable > Accurate**: Focus shifted from perfect models to implementable solutions
5. **Documentation Enables Iteration**: This example can be replicated for other cohorts/time periods

---

## How to Adapt This Example

### For Different Industries
- **E-commerce**: Replace "churn" with "repeat purchase rate"
- **Healthcare**: Adapt for "patient retention" or "appointment no-shows"
- **SaaS**: Use as-is or customize for freemium conversion

### For Different Questions
- Swap `prompts/use_cases/churn/` with `web_analytics/` or `market_research/`
- Keep same 5-stage structure
- Adjust `config.yaml` thresholds for your domain

### For Different Tools
- Replace AI prompts with SQL queries if using BI tools
- Keep checklist/template structure intact
- Document tool-specific setup in config.yaml

---

**End of Example** | [Back to Main README](../README.md)
