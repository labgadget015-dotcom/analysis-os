# Stage 2: Core Analysis Prompt

## 🎯 Purpose  
Answer your primary business questions using clean data from Stage 1.

---

## 📝 Full Prompt Template

```
You are an experienced data scientist and business strategist analyzing a dataset about [DOMAIN].

**ROLE & CONTEXT**
I've completed data preparation (Stage 1) and now have a clean dataset with:
- [X] rows and [Y] columns
- Time period: [START DATE] to [END DATE]
- Key segments: [List segments from Stage 1]

Relevant data dictionary:
[Paste key columns from Stage 1 data dictionary]

**YOUR OBJECTIVE**
Answer these specific business questions:

1. [QUESTION 1: e.g., "Which customer segments have the highest churn risk?"]
2. [QUESTION 2: e.g., "What behaviors predict churn in the next 30 days?"]
3. [QUESTION 3: e.g., "What is the estimated revenue impact of 10% churn reduction?"]

**CONSTRAINTS**
- Only analyze data from [DATE RANGE]
- Focus on [SPECIFIC SEGMENT] if applicable
- Budget constraint: $[X]
- Timeline: [Y weeks]
- [Any other business constraints]

**OUTPUT FORMAT**
For each question, provide:
```
### Question [N]: [Restate question]

**Chain-of-Thought Analysis:**
[Show your step-by-step reasoning]

**Answer:**
[Clear, specific answer with numbers]

**Supporting Evidence:**
- Data point 1: [Specific metric with value]
- Data point 2: [Specific metric with value]
- Data point 3: [Specific metric with value]

**Confidence Level:** High / Medium / Low  
**Why:** [Explain what could make this more/less certain]
```

**CRITICAL REQUIREMENTS**
1. **Use chain-of-thought**: Show your reasoning before each answer
2. **Cite evidence**: Every claim must reference specific data
3. **Quantify everything**: Use numbers, not vague terms like "many" or "some"
4. **State assumptions**: Make implicit assumptions explicit
5. **Flag uncertainties**: Call out what data is missing or ambiguous
```

---

## ✅ Success Criteria

You've completed Stage 2 when you have:

1. ✅ Specific numeric answers to each business question
2. ✅ Evidence citations for every major claim  
3. ✅ Confidence levels stated for each finding
4. ✅ Key assumptions documented
5. ✅ Identified 2-3 surprising insights that warrant deeper investigation (→ Stage 3)

---

## 🔄 Common Follow-Up Prompts

**Clarification:**
- "Can you break down [metric] by [segment]?"
- "What timeframe does [finding] apply to?"
- "How did you calculate [specific number]?"

**Validation:**
- "What assumptions did you make for [analysis]?"
- "How would the answer change if [assumption] were different?"
- "What's the margin of error on [estimate]?"

**Preparation for Stage 3:**
- "Which segment shows the most unusual pattern?"
- "What's the biggest outlier in [metric]?"
- "Which finding is most surprising and why?"

---

## Next Step

Identified surprising patterns or outliers? → **Go to Stage 3: Drill-down** (`/prompts/core/drilldown.md`)
