# Stage 1: Data Preparation Prompt

## 🎯 Purpose
Clean, understand, and document your dataset before analysis. This stage prevents 80% of common analysis errors.

---

## 📝 Full Prompt Template

```
You are an experienced data scientist preparing a dataset for analysis.

**ROLE & CONTEXT**
I have a dataset about [DOMAIN: e.g., "SaaS customer behavior", "e-commerce transactions"].
The data includes [NUMBER] rows and [NUMBER] columns covering [TIME PERIOD].

Key columns:
- [Column 1]: [Brief description]
- [Column 2]: [Brief description]
- [Column 3]: [Brief description]

**YOUR TASK**
1. **Data Profile**: Summarize the dataset structure, size, and time coverage
2. **Quality Check**: Identify missing values, duplicates, outliers, and formatting issues
3. **Data Dictionary**: Create a clear description of each column (name, type, meaning, example values)
4. **Segment Identification**: What natural segments exist? (e.g., user types, product categories, time periods)
5. **Red Flags**: Call out any data quality issues that could invalidate analysis

**CONSTRAINTS**
- Focus only on data from [DATE RANGE]
- Flag any columns with >20% missing values
- Highlight any suspicious patterns (e.g., sudden spikes, zeros where there shouldn't be)

**OUTPUT FORMAT**
```
## Data Profile
- Rows: [X]
- Columns: [Y]
- Time Period: [Start] to [End]
- File Size: [Z MB]

## Data Quality Summary
| Issue Type | Count | Severity | Action Needed |
|------------|-------|----------|---------------|
| Missing values | [X] | High/Medium/Low | [What to do] |
| Duplicates | [Y] | High/Medium/Low | [What to do] |
| Outliers | [Z] | High/Medium/Low | [What to do] |

## Data Dictionary
| Column Name | Data Type | Description | Example Values | Missing % |
|-------------|-----------|-------------|----------------|------------|
| customer_id | String | Unique customer identifier | "C001", "C002" | 0% |
| signup_date | Date | When customer signed up | 2024-01-15 | 2% |

## Natural Segments
1. [Segment 1]: [Description]
2. [Segment 2]: [Description]

## Red Flags ⚠️
- [Issue 1 and why it matters]
- [Issue 2 and why it matters]
```

**ADDITIONAL INSTRUCTIONS**
- Use chain-of-thought: Show your reasoning for each quality assessment
- Be specific: Don't say "some missing values" - say "347 missing values (12% of total)"
- Prioritize: Mark issues as High/Medium/Low severity
```

---

## 🛠️ Customization Examples

### For Small Datasets (<100MB)
```
**TOOL PREFERENCE**: Use Python with pandas for this analysis.
Provide code snippets for data profiling.
```

### For Large Datasets (>100MB)
```
**TOOL PREFERENCE**: Use SQL for initial profiling.
Focus on sampling strategies to avoid memory issues.
```

### For Time-Series Data
```
**ADDITIONAL CHECKS**:
- Verify timestamps are in correct format
- Check for gaps in time series
- Identify seasonality patterns
```

---

## ✅ Success Criteria

You've completed this stage when you have:

1. ✅ Clear data dictionary with all columns documented
2. ✅ Quantified data quality issues (not just "there are some problems")
3. ✅ Identified 2-5 natural segments to analyze separately
4. ✅ Flagged any showstopper issues that must be fixed first
5. ✅ Created a "clean dataset" ready for Stage 2 analysis

---

## 🔄 Common Follow-ups

After the AI responds, ask:

1. **"What's the recommended fix for [specific data quality issue]?"**
2. **"Should we exclude [segment/time period] from analysis? Why or why not?"**
3. **"Which columns are most relevant for answering [business question]?"**
4. **"Create a cleaned version of the dataset with [fixes applied]"**

---

## 🚨 Common Pitfalls to Avoid

| Pitfall | Why It's Bad | How to Avoid |
|---------|--------------|---------------|
| Ignoring missing data | Leads to biased analysis | Explicitly decide: impute, exclude, or model |
| Not checking date ranges | Mixes incomparable time periods | Always filter to relevant dates first |
| Assuming column meanings | Misinterpret data | Verify every column with stakeholders |
| Skipping outlier review | Outliers often reveal insights | Investigate top/bottom 1% of values |

---

## 📊 Example Output

See how a good Stage 1 response looks:

```
## Data Profile
- Rows: 45,231 customers
- Columns: 18 features
- Time Period: 2024-01-01 to 2024-12-31
- File Size: 8.3 MB

## Data Quality Summary
| Issue Type | Count | Severity | Action Needed |
|------------|-------|----------|---------------|
| Missing `last_login` | 3,847 (8.5%) | Medium | Likely churned users - keep for analysis |
| Duplicate `email` | 127 (0.3%) | High | Remove duplicates, keep most recent record |
| Negative `mrr` values | 5 (0.01%) | High | Data entry error - flag and exclude |

## Data Dictionary
| Column | Type | Description | Example | Missing % |
|--------|------|-------------|---------|------------|
| customer_id | String | Unique ID | "C12345" | 0% |
| signup_date | Date | Account creation date | 2024-03-15 | 0% |
| plan_tier | String | Subscription level | "Pro", "Enterprise" | 1.2% |
| mrr | Float | Monthly recurring revenue | 49.99 | 0% |
| last_login | Datetime | Most recent login | 2024-12-20 | 8.5% |

## Natural Segments
1. **By Plan Tier**: Free (12%), Pro (67%), Enterprise (21%)
2. **By Tenure**: New <3mo (22%), Mid 3-12mo (45%), Veteran >12mo (33%)
3. **By Engagement**: Active (last login <30d), At-Risk (30-90d), Dormant (>90d)

## Red Flags ⚠️
- 5 customers have negative MRR (data entry errors) - EXCLUDE from revenue analysis
- 18% of "Enterprise" customers missing `company_size` field - impacts segmentation
- Sudden spike in signups in Nov 2024 (3x normal) - verify if legitimate or data issue
```

---

## Next Step

Once data prep is complete → **Go to Stage 2: Core Analysis** (`/prompts/core/core_analysis.md`)
