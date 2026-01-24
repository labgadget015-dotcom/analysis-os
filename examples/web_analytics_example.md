# Web Analytics Optimization Example

This example demonstrates how to use the Analysis OS framework to optimize conversion funnels for an e-commerce platform.

---

## Stage 1: Data Preparation

### Checklist Used
Refer to `checklists/master_analysis_checklist.md` -> Data Preparation section

### Actions Taken
- [x] Exported Google Analytics 4 (GA4) event data (Add to Cart, Checkout, Purchase)
- [x] Cleaned session IDs and removed bot traffic (IP filtering)
- [x] Merged traffic source data with conversion events
- [x] Calculated baseline conversion rates per channel

### Dataset Profile
- **Events**: 142,500
- **Users**: 28,000
- **Date Range**: Oct 2025 - Dec 2025
- **Channels**: Organic, Paid Search, Social, Referral

---

## Stage 2: Core Analysis

### Key Business Questions Answered
1. **Funnel Bottleneck**: Where do we lose the most users?
   - *Answer*: 65% drop-off between "Initiate Checkout" and "Shipping Info".
2. **Channel Performance**: Which channel has the highest ROI?
   - *Answer*: Organic Search has the highest LTV/CAC ratio (4.2x).
3. **Device Impact**: Does mobile performance lag behind desktop?
   - *Answer*: Mobile conversion is 40% lower despite representing 70% of traffic.

---

## Stage 3: Drill-down Analysis

### Investigated Segments
- **Mobile Users on iOS vs Android**: Found iOS users have 2x higher cart abandonment.
- **Returning vs New Users**: Returning users convert at 3x the rate of new users.
- **Page Load Speed vs Conversion**: Pages loading in >3s see a 50% drop in conversion.

---

## Stage 4: Actionization (Recommendations)

| Action | Cost | Impact | Priority | Metric |
| :--- | :--- | :--- | :--- | :--- |
| **Optimize Checkout Form** | $5k | High | **CRITICAL** | Form Completion % |
| **Speed Up Product Pages** | $8k | High | **HIGH** | Conv. Rate |
| **Mobile UX Redesign** | $15k | Very High | **HIGH** | Mobile Conv. % |
| **Personalized Retargeting**| $10k | Medium | **MEDIUM** | ROAS |

---

## Stage 5: Iteration & Success Tracking

### Designed Experiment
- **A/B Test**: Single-page checkout vs Multi-step checkout.
- **Success Metric**: Checkout completion rate.
- **Target**: 15% improvement in conversion.

### Tracking Cadence
- **Weekly**: Monitor funnel drop-off rates.
- **Monthly**: Review channel-level ROAS and update `config.yaml`.
