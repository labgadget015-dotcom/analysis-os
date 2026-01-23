# analysis-os
Analysis &amp; AI Consulting OS - Unified framework for data-driven insights and actionable recommendations. Includes churn analysis, SMB AI audits, funnel optimization, and more.

## 🎯 Overview

This operating system transforms data analysis from ad-hoc exploration into a structured, repeatable pipeline. It includes:

- **5-stage analysis pipeline** (Data Prep → Core Analysis → Drill-down → Actionization → Iteration)
- **Reusable prompt templates** for each stage
- **Pre-configured checklists** to avoid common pitfalls
- **Use-case examples** (churn, web analytics, market research)
- **Configuration files** for tool selection and constraints

---

## 🚀 Quick Start

### 1. Define Your Analysis

Edit `config.yaml`:
```yaml
analysis:
  domain: "SaaS churn"
  questions:
    - "Which customer segments have highest churn risk?"
    - "What actions reduce churn by 10%+?"
  constraints:
    date_range: "2024-01-01 to 2024-12-31"
    budget: "$50k"
    timeline: "8 weeks"
```

### 2. Follow the 5-Stage Pipeline

| Stage | Checklist | Prompt Template | Output |
|-------|-----------|-----------------|--------|
| **1. Data Prep** | `/checklists/` | `/prompts/core/data_prep.md` | Clean dataset, metadata |
| **2. Core Analysis** | `/checklists/` | `/prompts/core/core_analysis.md` | Key findings, answers |
| **3. Drill-down** | `/checklists/` | `/prompts/core/drilldown.md` | Segment insights |
| **4. Actionization** | `/checklists/` | `/prompts/core/actionization.md` | Prioritized recommendations |
| **5. Iteration** | `/checklists/` | `/prompts/core/iteration.md` | Validation, experiments |

### 3. Run Your First Analysis

```bash
# Example: Churn analysis
cp prompts/use_cases/churn/PROMPT.md my_analysis.md
# Edit with your data details
# Copy to your AI tool (ChatGPT, Claude, etc.)
```

---

## 📁 File Structure

```
analysis-os/
├── README.md                          # This file
├── config.yaml                        # Analysis configuration
├── checklists/
│   └── master_analysis_checklist.md   # Complete validation checklist
├── prompts/
│   ├── core/
│   │   ├── data_prep.md              # Stage 1: Data preparation
│   │   ├── core_analysis.md          # Stage 2: Core analysis
│   │   ├── drilldown.md              # Stage 3: Deep dives
│   │   ├── actionization.md          # Stage 4: Recommendations
│   │   └── iteration.md              # Stage 5: Validation
│   └── use_cases/
│       ├── churn/
│       │   └── PROMPT.md             # Complete churn analysis prompt
│       ├── web_analytics/
│       │   └── PROMPT.md             # Web traffic optimization
│       └── market_research/
│           └── PROMPT.md             # Competitor/market analysis
├── templates/
│   ├── output_template.md            # Standard output format
│   └── recommendation_table.md       # Recommendation structure
└── notebooks/
    └── examples/                     # Jupyter notebook examples

```

---

## 🔧 The 5-Stage Pipeline

### Stage 1: Data Prep
**Goal**: Clean, understand, and document your dataset

**Checklist**: 
- ✅ Handle missing values
- ✅ Check data types and formats
- ✅ Document column meanings
- ✅ Identify date ranges and segments

**Prompt**: `/prompts/core/data_prep.md`

---

### Stage 2: Core Analysis
**Goal**: Answer primary business questions

**Checklist**:
- ✅ Define 3-5 key questions
- ✅ Set constraints (time, budget, scope)
- ✅ Use chain-of-thought prompting
- ✅ Request evidence for all claims

**Prompt**: `/prompts/core/core_analysis.md`

---

### Stage 3: Drill-down
**Goal**: Explore segments, cohorts, and edge cases

**Checklist**:
- ✅ Ask "why" and "what if"
- ✅ Segment by key dimensions
- ✅ Identify outliers and anomalies

**Prompt**: `/prompts/core/drilldown.md`

---

### Stage 4: Actionization
**Goal**: Generate prioritized, actionable recommendations

**Output Format**:
| Recommendation | Evidence | Impact | Effort | Metric to Monitor |
|----------------|----------|--------|--------|-------------------|
| Action 1 | Data X shows Y | High | Medium | Metric Z |

**Prompt**: `/prompts/core/actionization.md`

---

### Stage 5: Iteration
**Goal**: Validate findings, check blind spots, design experiments

**Checklist**:
- ✅ Re-run analysis with different assumptions
- ✅ Check for survivorship bias, confounders
- ✅ Design A/B tests for top recommendations

**Prompt**: `/prompts/core/iteration.md`

---

## 🎓 Use Cases

### Module A: Churn Analysis
**Target**: Reduce customer churn in SaaS/subscription businesses

**Questions**: 
- Which segments churn fastest?
- What behaviors predict churn?
- What interventions reduce churn by 10%+?

**Output**: Prioritized retention strategies

**Prompt**: `/prompts/use_cases/churn/PROMPT.md`

---

### Module B: Web Analytics
**Target**: Optimize traffic, conversions, engagement

**Questions**:
- Which pages have highest bounce rates?
- What drives conversions?
- Where should we invest in content/UX?

**Prompt**: `/prompts/use_cases/web_analytics/PROMPT.md`

---

### Module C: Market Research
**Target**: Competitive intelligence, positioning, go-to-market

**Questions**:
- How do we compare to competitors?
- What features/pricing drive market share?
- Which segments should we target?

**Prompt**: `/prompts/use_cases/market_research/PROMPT.md`

---

## ⚙️ Customization

### Module D: Marketing Attribution

**Target**: Optimize marketing spend and understand customer journey touchpoints

**Questions**:
- Which marketing channels drive highest ROI?
- What is the optimal budget allocation across channels?
- How do customers typically convert (customer journey)?

**Prompt**: `/prompts/use_cases/marketing_attribution/PROMPT.md`

### Module E: Pricing Optimization

**Target**: Maximize revenue and profit through strategic pricing

**Questions**:
- What are optimal price points for our products?
- How price-sensitive are different customer segments?
- What's the projected revenue impact of price changes?

**Prompt**: `/prompts/use_cases/pricing_optimization/PROMPT.md`

### Module F: Customer Segmentation

**Target**: Identify and profile distinct customer groups for targeted strategies

**Questions**:
- What are our key customer segments (RFM, behavioral, demographic)?
- Which segments have highest lifetime value?
- How should we tailor strategies by segment?

**Prompt**: `/prompts/use_cases/customer_segmentation/PROMPT.md`

### Module G: A/B Test Analysis

**Target**: Rigorously analyze experiments to make ship/no-ship decisions

**Questions**:
- Is the test result statistically significant?
- What's the expected business impact if we ship?
- Are there segment-specific effects we should consider?

**Prompt**: `/prompts/use_cases/ab_test_analysis/PROMPT.md`

### 1. Edit `config.yaml`
Centralize your analysis parameters:
```yaml
tools:
  small_data: "ChatGPT (Code Interpreter)"
  large_data: "BigQuery + Claude"
  visualization: "Python (matplotlib)"
```

### 2. Create Custom Prompts
Copy any template from `/prompts/core/` and modify for your domain.

### 3. Add New Use Cases
Create `/prompts/use_cases/[your_domain]/PROMPT.md` with:
- Role & context
- Objective
- Constraints
- Output format

---

## 🔒 Best Practices

1. **Always start with data prep** - 80% of errors come from bad data
2. **Use checklists religiously** - They prevent blind spots
3. **Request evidence** - Ask AI to cite data for every claim
4. **Iterate with "why" prompts** - Drill down on surprising findings
5. **Design experiments** - Recommendations without tests are just hypotheses

---

## 📊 Example Workflow

```bash
# Step 1: Configure
vim config.yaml  # Set domain, questions, constraints

# Step 2: Data Prep
# Use prompts/core/data_prep.md with your dataset

# Step 3: Core Analysis
# Use prompts/core/core_analysis.md to answer key questions

# Step 4: Drill-down
# Use prompts/core/drilldown.md for segment analysis

# Step 5: Actionization
# Use prompts/core/actionization.md to generate recommendations

# Step 6: Iteration
# Use prompts/core/iteration.md to validate and design experiments
```

---

## 🔗 Links

- **Repository**: https://github.com/labgadget015-dotcom/analysis-os
- **Issues**: https://github.com/labgadget015-dotcom/analysis-os/issues
- **Discussions**: https://github.com/labgadget015-dotcom/analysis-os/discussions
- **📖 Tutorial**: See [docs/TUTORIAL.md](docs/TUTORIAL.md) for a complete walkthrough
- **🏗️ Architecture**: Read [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for technical details
- **🤖 Automation**: Use `scripts/run_analysis.sh` to orchestrate analyses

---

## 📄 License

MIT License - Feel free to use and adapt for your own analysis work.

---

**Status**: v1.0 - Complete and ready for implementation
