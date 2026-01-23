# Stage 4: Actionization Prompt

## 🎯 Purpose
Convert insights from Stages 1-3 into prioritized, actionable recommendations.

---

## 📝 Full Prompt Template

```
You are a business strategist translating data insights into actionable recommendations.

**CONTEXT FROM PREVIOUS STAGES**
Key findings:
- [Finding 1 from Stages 2-3]
- [Finding 2 from Stages 2-3]
- [Finding 3 from Stages 2-3]

**YOUR OBJECTIVE**
Generate 3-5 prioritized, actionable recommendations that:
1. Address the most important business questions
2. Are specific enough to implement
3. Have measurable success metrics
4. Fit within budget and timeline constraints

**CONSTRAINTS**
- Budget: $[X]
- Timeline: [Y weeks/months]
- Resources: [Team size, technical capabilities]
- Risk tolerance: [Low/Medium/High]

**OUTPUT FORMAT**
For each recommendation, provide:

| Recommendation | Evidence | Expected Impact | Implementation Effort | Timeline | Metric to Monitor | Priority |
|----------------|----------|-----------------|----------------------|----------|-------------------|----------|
| [Specific action] | [Data supporting this] | [Quantified benefit] | [Low/Med/High] | [X weeks] | [KPI to track] | [1-5] |

**DETAILED BREAKDOWN**
For top 3 recommendations:
```
### Recommendation [N]: [Title]

**What to Do:**
[Specific, actionable steps]

**Why It Works:**
[Evidence from your analysis]

**Expected Impact:**
- Metric 1: [Current] → [Target] (X% improvement)
- Metric 2: [Current] → [Target] (Y% improvement)
- Revenue/Cost Impact: $[Z]

**Implementation Plan:**
1. [Step 1] - [Owner] - [Week 1-2]
2. [Step 2] - [Owner] - [Week 3-4]
3. [Step 3] - [Owner] - [Week 5-6]

**Success Metrics:**
- Primary: [KPI] reaches [target] by [date]
- Secondary: [KPI 2] improves by [X%]

**Risks & Mitigations:**
- Risk: [What could go wrong]
  Mitigation: [How to prevent/handle it]

**Quick Wins vs. Long-term:**
[Quick win (if applicable) or note this is long-term]
```
```

---

## ✅ Success Criteria

1. ✅ Each recommendation is specific (not "improve retention" but "launch email campaign to at-risk users")
2. ✅ Expected impact is quantified ("reduce churn by 15%" not "reduce churn")
3. ✅ Implementation effort is realistically estimated
4. ✅ Success metrics are clearly defined
5. ✅ Recommendations are prioritized by impact/effort ratio

---

## 🔄 Common Follow-Up Prompts

**Prioritization:**
- "Which recommendation has highest ROI?"
- "What are the quick wins (< 2 weeks)?"
- "Which actions should we do first/second/third?"

**Refinement:**
- "Break down [recommendation] into specific implementation steps"
- "What resources do we need for [recommendation]?"
- "How would we measure success for [recommendation]?"

**Risk Assessment:**
- "What could go wrong with [recommendation]?"
- "What's the downside risk if [recommendation] fails?"
- "What dependencies exist for [recommendation]?"

---

## Next Step

Ready to validate and design experiments? → **Go to Stage 5: Iteration** (`/prompts/core/iteration.md`)
