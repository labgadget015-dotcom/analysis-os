# Tutorial: Your First Analysis with Analysis OS

This step-by-step tutorial will guide you through your first complete analysis using the Analysis & AI Consulting OS framework.

## Prerequisites

- An AI assistant (ChatGPT, Claude, or similar)
- A dataset to analyze (CSV, JSON, or similar format)
- 30-60 minutes of time

## Tutorial Overview

We'll walk through a **customer churn analysis** using the complete 5-stage pipeline.

---

## Step 1: Setup (5 minutes)

### 1.1 Clone or Download the Repository

```bash
git clone https://github.com/labgadget015-dotcom/analysis-os.git
cd analysis-os
```

### 1.2 Choose Your Use Case

For this tutorial, we'll use **Churn Analysis**. The available use cases are:

- `churn_analysis` - Predict and prevent customer attrition
- `web_analytics` - Analyze website behavior and conversions  
- `market_research` - Survey analysis and market insights
- `marketing_attribution` - Multi-touch attribution modeling
- `pricing_optimization` - Strategic pricing decisions
- `customer_segmentation` - RFM and behavioral segmentation
- `ab_test_analysis` - Rigorous experiment analysis

### 1.3 Prepare Your Dataset

For churn analysis, you'll need customer data with:
- Customer ID
- Sign-up date
- Activity metrics (logins, purchases, engagement)
- Churn status (active/churned)
- Optional: demographics, plan type, support tickets

**Don't have data?** Use our example structure from `examples/churn_analysis_example.md`

---

## Step 2: Configure Your Analysis (2 minutes)

### 2.1 Edit config.yaml

Open `config.yaml` and customize for your domain:

```yaml
analysis:
  domain: "SaaS subscription service"
  questions:
    - "What factors drive churn?"
    - "Which customers are at highest risk?"
    - "What interventions could reduce churn?"
  constraints:
    - "Focus on B2B customers"
    - "Must be actionable within 30 days"
```

### 2.2 (Optional) Use the Automation Script

```bash
chmod +x scripts/run_analysis.sh
./scripts/run_analysis.sh -u churn_analysis -d data/customers.csv
```

This will:
- Generate all prompts for the 5 stages
- Load the use case-specific instructions
- Copy the quality checklist
- Create an output directory with everything ready

---

## Step 3: Run the 5-Stage Pipeline (30-45 minutes)

### Stage 1: Data Preparation (5-8 minutes)

**What you'll do:**
1. Open `prompts/core/data_prep.md` OR `output/stage_1_data_prep.txt`
2. Copy the entire prompt
3. Paste into ChatGPT/Claude
4. When prompted, paste your dataset (first 50-100 rows)

**What the AI will do:**
- Check data quality and identify issues
- Summarize key statistics
- Suggest data transformations
- Flag missing values or anomalies

**Expected output:**
```
Data Quality Report:
- 10,000 customers, 15 features
- Missing values: last_login (5%), support_tickets (2%)
- Churn rate: 23%
- Recommendation: Impute missing values, create tenure_days feature
```

**Action:** Fix any critical data issues before proceeding.

---

### Stage 2: Core Analysis (10-12 minutes)

**What you'll do:**
1. Open `prompts/core/core_analysis.md`
2. Copy and paste into your AI conversation (same thread)
3. The AI already has your data context

**What the AI will do:**
- Answer your key business questions
- Identify primary churn drivers
- Discover patterns and correlations
- Generate initial insights

**Expected output:**
```
Key Findings:
1. Customers with <2 logins/month have 3x higher churn
2. Support ticket count correlates with retention
3. Annual plans have 60% lower churn than monthly
4. Churn peaks at 3-4 month tenure
```

**Action:** Note surprising findings for deeper investigation in Stage 3.

---

### Stage 3: Drill-Down (8-10 minutes)

**What you'll do:**
1. Open `prompts/core/drilldown.md`
2. Copy and paste into the same conversation
3. Ask follow-up questions about specific segments

**What the AI will do:**
- Deep-dive into specific customer segments
- Compare cohorts (e.g., annual vs monthly plans)
- Analyze time-based patterns
- Test hypotheses from Stage 2

**Expected output:**
```
Segment Analysis:
- Enterprise customers (>$1k MRR): 8% churn
- SMB customers (<$100 MRR): 35% churn
- Product usage gap: Churned users used 60% fewer features
- Onboarding impact: Week 1 engagement predicts 6-month retention
```

**Action:** Identify 2-3 high-impact intervention opportunities.

---

### Stage 4: Actionization (5-8 minutes)

**What you'll do:**
1. Open `prompts/core/actionization.md`
2. Copy and paste into the conversation
3. Request specific, prioritized recommendations

**What the AI will do:**
- Generate actionable recommendations
- Prioritize by impact and feasibility
- Estimate effort and expected outcomes
- Create implementation roadmap

**Expected output:**
```
Top 3 Recommendations:

1. [HIGH IMPACT] Proactive outreach for <2 login/month users
   - Target: 1,500 at-risk customers
   - Action: Automated email + CSM call
   - Expected: 15% churn reduction
   - Effort: 2 weeks

2. [MEDIUM IMPACT] Enhanced onboarding for SMB segment  
   - Target: All new SMB customers
   - Action: Interactive tutorial + milestone rewards
   - Expected: 10% churn reduction
   - Effort: 4 weeks

3. [QUICK WIN] Annual plan incentive
   - Target: Monthly subscribers at 6-month tenure
   - Action: 20% discount offer
   - Expected: 5% churn reduction
   - Effort: 1 week
```

**Action:** Select 1-2 recommendations to test.

---

### Stage 5: Iteration (5-7 minutes)

**What you'll do:**
1. Open `prompts/core/iteration.md`
2. Copy and paste into the conversation
3. Design experiments to validate your recommendations

**What the AI will do:**
- Design A/B tests
- Define success metrics
- Calculate sample sizes
- Create monitoring plan

**Expected output:**
```
Experiment Design: Proactive Outreach

Hypothesis: Outreach to low-engagement users reduces churn by >10%

Test Setup:
- Control: 750 at-risk users (no outreach)
- Treatment: 750 at-risk users (email + call)
- Duration: 30 days
- Success metric: Churn rate difference
- Required effect: >5% absolute reduction

Monitoring:
- Week 1: Track outreach completion rate
- Week 2: Monitor engagement uplift
- Week 4: Measure churn rate
```

**Action:** Launch your experiment!

---

## Step 4: Quality Check (5 minutes)

### 4.1 Use the Checklist

Open `checklists/master_analysis_checklist.md` and verify:

✅ Data quality validated  
✅ Key questions answered with evidence  
✅ Segments analyzed  
✅ Recommendations are specific and actionable  
✅ Experiments designed with clear metrics  
✅ Assumptions documented  

### 4.2 Review Use Case Checklist

Open `checklists/churn_analysis_checklist.md` for domain-specific validation.

---

## Step 5: Document & Share (5 minutes)

### 5.1 Export Your Analysis

Save the full conversation with your AI assistant:
- ChatGPT: Click "..." → Export
- Claude: Copy conversation to a document

### 5.2 Create Summary Report

Use `templates/recommendation_table.md` as a starting point:

```markdown
# Churn Analysis Summary
**Date:** 2026-01-23  
**Analyst:** Your Name

## Key Findings
1. Low engagement (<2 logins/month) drives churn
2. SMB segment has highest churn risk
3. Week 1 onboarding predicts retention

## Recommendations
| Priority | Action | Target | Expected Impact |
|----------|--------|--------|----------------|
| HIGH | Proactive outreach | Low-engagement users | 15% churn reduction |
| MEDIUM | Enhanced onboarding | SMB customers | 10% churn reduction |
| QUICK WIN | Annual incentive | 6-month monthly subs | 5% churn reduction |
```

---

## Troubleshooting

### "My AI doesn't understand the prompt"

- **Solution**: Make sure you're using the full prompt from the `.md` file
- Try breaking it into smaller chunks
- Ensure your dataset is included after the prompt

### "The analysis is too generic"

- **Solution**: Edit `config.yaml` with more specific domain details
- Add constraints to guide the analysis
- Use the use case-specific prompt (e.g., `prompts/use_cases/churn_analysis/PROMPT.md`)

### "I don't have technical skills"

- **Solution**: You don't need them! Just copy/paste prompts and your data
- Skip the automation script—manual process works fine
- Focus on Stages 2-4 (Core Analysis, Drill-down, Actionization)

### "My dataset is too large"

- **Solution**: Use a representative sample (first 1000 rows)
- Provide summary statistics instead of raw data
- Use ChatGPT Advanced Data Analysis for large files

---

## Tips for Success

1. **Keep it conversational**: The 5 stages work best in a single AI conversation thread
2. **Ask follow-ups**: Don't hesitate to ask "why" or "show me an example"
3. **Use the checklist**: Quality checks prevent blind spots
4. **Start small**: Your first analysis doesn't need to be perfect
5. **Iterate**: Come back to Stage 5 after implementing recommendations

---

## Next Steps

### After Your First Analysis

1. **Try another use case**: Explore `web_analytics` or `customer_segmentation`
2. **Customize prompts**: Adapt templates for your specific industry
3. **Automate recurring analyses**: Use the shell script for monthly reports
4. **Share your results**: Contribute examples to the community

### Advanced Usage

- **API Integration**: Connect prompts to your data warehouse (BigQuery, Snowflake)
- **Scheduled Analysis**: Run monthly automated reports
- **Custom Use Cases**: Create your own prompt templates
- **Team Collaboration**: Share config files across your organization

---

## Example Timeline

| Time | Activity |
|------|----------|
| 0:00 | Setup: Clone repo, prepare data |
| 0:05 | Configure: Edit config.yaml |
| 0:07 | Stage 1: Data Prep prompt |
| 0:15 | Stage 2: Core Analysis |
| 0:27 | Stage 3: Drill-down |
| 0:37 | Stage 4: Actionization |
| 0:45 | Stage 5: Iteration & experiment design |
| 0:52 | Quality check with checklists |
| 0:57 | Export and document |
| **1:00** | **Complete!** |

---

## Real-World Example

See `examples/churn_analysis_example.md` for a complete walkthrough with:
- Sample dataset structure
- Full AI conversation transcript
- Generated insights
- Recommended actions
- Experiment design

---

## Community & Support

- **Issues**: Report bugs or request features on GitHub
- **Discussions**: Share your analyses and ask questions
- **Contributing**: Help improve prompts and add use cases

---

## You're Ready!

You now have everything you need to run your first analysis. The framework will guide you through each step.

**Pro tip**: Bookmark this tutorial and refer back as you go through the stages.

Happy analyzing! 🚀

---

**Version**: 1.0  
**Last Updated**: January 2026  
**Feedback**: Open an issue or discussion on GitHub
