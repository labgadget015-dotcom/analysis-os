# Churn Analysis - Complete Prompt

## 🎯 Use Case
Reduce customer churn in SaaS/subscription businesses by identifying at-risk customers and actionable retention strategies.

---

## 📝 Complete All-in-One Prompt

```
You are an experienced data scientist and retention strategist analyzing customer churn.

**ROLE & CONTEXT**
I have a SaaS customer dataset with [X] customers covering [TIME PERIOD].

Key data available:
- Customer demographics: [plan tier, company size, industry]
- Behavioral data: [login frequency, feature usage, support tickets]
- Financial data: [MRR, payment history, upgrades/downgrades]
- Outcome: [churned yes/no, churn date]

**YOUR OBJECTIVE**
Answer these business questions:

1. **Which customer segments have the highest churn risk?**
   (Break down by plan tier, tenure, company size, engagement level)

2. **What behaviors predict churn in the next 30/60/90 days?**
   (Identify early warning signals)

3. **What actions can reduce churn by 10%+?**
   (Generate 3-5 specific, actionable recommendations)

4. **What's the estimated revenue impact?**
   (Quantify the financial benefit of churn reduction)

**CONSTRAINTS**
- Focus on data from [DATE RANGE]
- Budget for retention initiatives: $[X]
- Implementation timeline: [Y weeks]
- Must work within current product/team capabilities

**ANALYSIS PIPELINE**
Follow the 5-stage process:

### Stage 1: Data Prep
- Profile the dataset (rows, columns, time coverage)
- Check data quality (missing values, outliers)
- Create data dictionary
- Identify natural segments

### Stage 2: Core Analysis
Answer each business question with:
- Chain-of-thought reasoning
- Specific numeric answers
- Supporting evidence
- Confidence levels

### Stage 3: Drill-down
For surprising findings:
- Segment breakdown analysis
- Time pattern investigation
- Outlier deep-dive
- Correlation analysis

### Stage 4: Actionization
Generate recommendations table:

| Recommendation | Evidence | Expected Impact | Effort | Timeline | Metric to Monitor | Priority |
|----------------|----------|-----------------|--------|----------|-------------------|----------|
| [Action 1] | [Data] | [Quantified] | [L/M/H] | [Weeks] | [KPI] | [1-5] |

### Stage 5: Iteration
- Test key assumptions
- Check for biases (survivorship, selection, confounders)
- Design A/B test for top recommendation
- Calculate required sample sizes

**OUTPUT FORMAT**
Deliver a complete analysis with:

```
## Executive Summary
- [3-5 key findings in bullets]
- [Top recommendation]
- [Estimated impact: $X revenue saved, Y% churn reduction]

## Data Profile
- Rows: [X]
- Columns: [Y]
- Time Period: [Dates]
- Churn Rate: [Z%]

## Key Findings

### Q1: Highest Churn Risk Segments
[Answer with specific numbers and segments]

### Q2: Churn Prediction Signals
[List top 5-7 behavioral signals with evidence]

### Q3: Churn Reduction Actions
[Table of 3-5 recommendations]

### Q4: Revenue Impact
[Financial quantification]

## Drill-down Insights
[2-3 surprising findings with explanations]

## Recommendations
[Detailed breakdown of top 3 recommendations]

## Experiment Design
[A/B test structure for top recommendation]

## Appendix
- Assumptions made
- Data quality issues
- Limitations
```
```

---

## 📊 Example Output Snippets

### Example Finding
```
**Q1: Highest Churn Risk Segments**

Top 3 at-risk segments:

1. **Free-to-Paid Converters (< 3 months tenure)**: 45% churn rate
   - 2,341 customers in segment
   - 3.2x higher than average (13%)
   - Evidence: 847 of 1,880 churned within 90 days

2. **Low-Engagement Enterprise**: 38% churn rate
   - Defined as: <5 logins/month, >$500 MRR
   - 412 customers, contributing $285K MRR at risk
   - Red flag: 73% have open support tickets >30 days old

3. **Downgraders**: 52% churn within 6 months of downgrade
   - 156 customers downgraded Q4 2024
   - 81 have since churned ($47K MRR lost)
```

### Example Recommendation
```
**Recommendation 1: Onboarding Campaign for New Paid Users**

**What to Do:**
- Trigger automated email sequence for customers 0-30 days after first payment
- Include: product tutorial videos, best practice guide, 1:1 onboarding call offer
- Success milestone: Complete 3 key actions within first 30 days

**Why It Works:**
- New paid users (<3mo) have 45% churn vs. 13% average
- Customers who complete 3+ key actions in month 1 have 8% churn rate
- Evidence from 2,341 customers over 12 months

**Expected Impact:**
- Reduce new user churn from 45% to 25% (44% improvement)
- Save ~470 customers/year × $89 avg MRR = $42K MRR saved/year = $504K annual impact

**Implementation:**
- Week 1-2: Build email sequence (Marketing)
- Week 3-4: QA and test (Product)
- Week 5: Launch to 20% of new users (A/B test)
- Week 8: Analyze results, iterate or scale

**Success Metrics:**
- Primary: 30-day churn rate < 25%
- Secondary: 60% complete ≥3 key actions
- Guardrail: Email open rate > 40%

**Priority: 1** (Highest ROI, low effort)
```

---

## ✅ Checklist

Before finalizing:
- ✅ All 4 business questions answered with numbers
- ✅ Churn rate broken down by 3+ segments
- ✅ At least 5 behavioral predictors identified
- ✅ 3-5 actionable recommendations with ROI estimates
- ✅ Top recommendation has A/B test design
- ✅ Financial impact quantified ($X revenue/year)

---

## Next Steps

1. Copy this prompt to your AI tool (ChatGPT, Claude, etc.)
2. Replace [PLACEHOLDERS] with your specific data details
3. Attach or describe your dataset
4. Review the output and iterate with follow-up questions
5. Use `/prompts/core/` stages for deeper dives as needed
