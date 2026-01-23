# Master Analysis Checklist

Use this checklist for every analysis project to ensure consistency and quality.

## A. Data Prep Checklist

- [ ] Confirm data dictionary: columns, types, meaning, grain, timeframe, primary keys
- [ ] Clean: handle missing values, duplicates, inconsistent formats (dates, currencies, categories)
- [ ] Standardize formats: CSV/Parquet/SQL tables; clear column names; consistent units/timezones
- [ ] Record metadata: data source, extract date, filters applied, known limitations

## B. Tool Selection Checklist

- [ ] **Size/complexity**: 
  - Small/medium → LLM + Python (pandas)
  - Large/wide → warehouse + pandas/Spark + specialized tabular tools
- [ ] **Structure**: 
  - Tabular → pandas/SQL + charting
  - Text → NLP-capable tools, embeddings
- [ ] **Purpose**: EDA vs forecasting vs segmentation vs recommendation engine; pick tools accordingly

## C. Prompting & Templates Checklist

- [ ] Define role: "experienced data scientist and business strategist"
- [ ] Specify objective and target metric(s)
- [ ] Add constraints: timeframe, budget, segments in scope
- [ ] Require structured reasoning (but only final reasoning surfaced)

## D. Iteration Prompts Checklist

After first pass, always ask:

- [ ] "Focus only on [segment/region/product]. What changes in the drivers and recommendations?"
- [ ] "Why might this trend have occurred from [start date] to [end date]? Give 3 explanations and how to test each."
- [ ] "What hidden correlations/interaction effects should be investigated, and how would you test them?"
- [ ] "What are the main limitations or blind spots, and what data would most improve this?"

## E. Validation & Action Checklist

- [ ] Re-run sanity checks on key metrics (rates, totals, date ranges) before finalizing
- [ ] Log decisions: assumptions, chosen drivers, rejected hypotheses, data gaps
- [ ] End with an actionization step: prioritized experiments/actions, with impact/effort and monitoring plan

---

## Default Analysis Loop

1. **Initial pass**: Data prep + data-understanding prompt; get candidate drivers, patterns, and questions
2. **Drill-down**: Run iterative prompts on key segments, time windows, and metrics
3. **Challenge assumptions**: Ask explicitly about blind spots, alternative explanations, and missing data
4. **Finalize recommendations**: Convert findings into a ranked list of actions with impact/effort/time-to-result
5. **Next experiments**: Define 30-day experiments and simple monitoring queries
