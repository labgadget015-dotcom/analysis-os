# Stage 3: Drill-down Analysis Prompt

## 🎯 Purpose
Explore surprising patterns, outliers, and segments identified in Stage 2.

---

## 📝 Full Prompt Template

```
You are an experienced data analyst conducting deep-dive investigations.

**CONTEXT FROM STAGE 2**
We completed core analysis and found these key insights:
- [Insight 1 from Stage 2]
- [Insight 2 from Stage 2]
- [Surprise finding / outlier from Stage 2]

**YOUR TASK**
Drill down into [SPECIFIC FINDING] by investigating:

1. **Segment Breakdown**: How does [metric] vary by [dimension]?  
   (e.g., by customer tier, region, product category, cohort)

2. **Time Patterns**: Are there temporal trends?  
   (e.g., seasonality, day-of-week effects, before/after events)

3. **Outlier Investigation**: What explains the [top/bottom X%]?  
   (e.g., Why do these customers have 10x higher churn?)

4. **Correlation Analysis**: What factors correlate with [target metric]?
   (e.g., Which behaviors predict high churn risk?)

**DRILL-DOWN QUESTIONS**
Answer these to understand WHY the pattern exists:

- "Why" questions: Why does [segment] behave differently?
- "What if" questions: What if we exclude [outlier group]?
- "How much" questions: How much does [factor] contribute to [outcome]?

**OUTPUT FORMAT**
For each drill-down:
```
### Drill-down: [Specific investigation]

**Hypothesis:** [What you expected to find]

**Method:** [How you analyzed it]

**Findings:**
- [Specific finding with numbers]
- [Specific finding with numbers]
- [Specific finding with numbers]

**Surprising Insight:**  
[What was unexpected and why it matters]

**Business Implication:**  
[So what? Why should stakeholders care?]
```
```

---

## ✅ Success Criteria

1. ✅ Investigated at least 3 different segment breakdowns
2. ✅ Identified which factors drive differences (not just that differences exist)
3. ✅ Quantified the size of segment differences
4. ✅ Found actionable insights (not just "interesting" patterns)
5. ✅ Uncovered root causes (answered "why" not just "what")

---

## 🔄 Common Follow-Up Prompts

**Go deeper:**
- "What explains the difference between [segment A] and [segment B]?"
- "Can you break down [segment] further by [another dimension]?"
- "What's driving the outliers in [metric]?"

**Validate:**
- "Is this pattern consistent over time?"
- "Does this hold true for all [segments]?"
- "Could this be due to [confounder]?"

**Actionize:**
- "Which segment should we prioritize based on [criteria]?"
- "What's the potential impact of targeting [segment]?"

---

## Next Step

Identified actionable segments and patterns? → **Go to Stage 4: Actionization** (`/prompts/core/actionization.md`)
