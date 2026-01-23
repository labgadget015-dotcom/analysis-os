# Stage 5: Iteration & Validation Prompt

## 🎯 Purpose
Validate findings, check blind spots, and design experiments to test recommendations.

---

## 📝 Full Prompt Template

```
You are a rigorous data scientist validating analysis before implementation.

**CONTEXT FROM STAGES 1-4**
We've completed analysis and generated recommendations:
- Key finding 1: [Summary]
- Key finding 2: [Summary]
- Top recommendation: [Summary]

**YOUR TASK**
Before implementing, validate our analysis by:

1. **Re-run with Different Assumptions**
   - What if we used [different time period]?
   - What if we excluded [edge case]?
   - What if [assumption] were different?

2. **Check for Bias & Blind Spots**
   - Survivorship bias: Are we only seeing successful cases?
   - Selection bias: Is our data sample representative?
   - Confounding factors: What else could explain this pattern?
   - Recency bias: Are we over-weighting recent data?

3. **Design Experiments**
   For top recommendation, design:
   - A/B test structure
   - Sample size requirements
   - Success metrics
   - Duration and stopping criteria

**OUTPUT FORMAT**

### Validation Checks
```
#### Assumption Sensitivity
| Assumption | Original | Alternative | Impact on Conclusion |
|------------|----------|-------------|----------------------|
| [Assumption 1] | [Value] | [Alt value] | [Does conclusion hold?] |

#### Bias Check
| Bias Type | Risk Level (H/M/L) | Evidence | Mitigation |
|-----------|--------------------|-----------|-----------|
| Survivorship | [H/M/L] | [What we found] | [How to address] |
| Selection | [H/M/L] | [What we found] | [How to address] |
| Confounders | [H/M/L] | [What we found] | [How to address] |
```

### Experiment Design
```
**Recommendation to Test:** [Top recommendation from Stage 4]

**Hypothesis:**
H0 (Null): [No effect statement]
H1 (Alternative): [Expected effect with magnitude]

**Experiment Design:**
- Type: A/B test / Multivariate / Before-after
- Duration: [X weeks]
- Sample size: [Y users/transactions per variant]
- Variants: 
  - Control: [Current state]
  - Treatment: [Recommended change]

**Success Metrics:**
- Primary: [Metric] improves by [X%] (p < 0.05)
- Secondary: [Metric 2] doesn't degrade by more than [Y%]
- Guardrail: [Metric 3] stays within [bounds]

**Power Analysis:**
- Minimum detectable effect: [X%]
- Statistical power: 80%
- Significance level: α = 0.05
- Required sample size: [N per group]

**Implementation:**
- Randomization: [How to assign users/units]
- Measurement: [How/when to collect data]
- Duration: [Start date] to [End date]

**Decision Criteria:**
- Ship if: [Primary metric improves AND no guardrail violations]
- Iterate if: [Mixed results - specify what to do]
- Kill if: [No improvement OR significant downside]
```
```

---

## ✅ Success Criteria

1. ✅ Tested key assumptions with sensitivity analysis
2. ✅ Identified and addressed potential biases
3. ✅ Designed statistically valid experiments
4. ✅ Calculated required sample sizes
5. ✅ Defined clear decision criteria for experiment results

---

## 🔄 Common Follow-Up Prompts

**Validation:**
- "What's the weakest assumption in our analysis?"
- "What could we be missing?"
- "How would a skeptic attack this conclusion?"

**Experiment Design:**
- "Calculate the sample size needed for [X%] minimum detectable effect"
- "Design an A/B test for [specific recommendation]"
- "What guardrail metrics should we monitor?"

**Risk Management:**
- "What's the downside if this recommendation fails?"
- "How can we test this with minimal risk?"
- "What's the rollback plan if results are negative?"

---

## Final Deliverable

Congratulations! You've completed the 5-stage Analysis OS pipeline:

✅ Stage 1: Data Prep - Clean, documented dataset  
✅ Stage 2: Core Analysis - Answered business questions  
✅ Stage 3: Drill-down - Understood patterns and segments  
✅ Stage 4: Actionization - Generated prioritized recommendations  
✅ Stage 5: Iteration - Validated findings and designed experiments  

**Next: Implement experiments and monitor results!**
