# analysis-os

![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)
![Shell](https://img.shields.io/badge/shell-100%25-green.svg)
![Version](https://img.shields.io/badge/version-1.0.0-brightgreen.svg)
![Status](https://img.shields.io/badge/status-production--ready-success.svg)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)

**Analysis & AI Consulting OS** - The operating system for analytics consultants and technical founders who want to turn messy data exports into executive-ready recommendations in hours, not weeks.

> **For consultants**: Run this monthly as a standardized churn review, SMB AI audit, or funnel optimization—each analysis becomes a repeatable, high-margin engagement.

---

## 🎯 What This Does

Reduces **subscription churn by 10–20%** in 8 weeks for SaaS and e-commerce companies.

Transforms AI readiness assessments for SMBs into a **systematic, repeatable audit** with clear ROI projections.

Turns ad-hoc data analysis into a **5-stage pipeline** that works the same way every time:

```
Data Prep → Core Analysis → Drill-down → Actionization → Iteration
```

Each stage includes:
- ✅ **Reusable prompt templates** (copy-paste into ChatGPT, Claude, or your AI tool)
- ✅ **Pre-configured checklists** to catch blind spots
- ✅ **Output templates** for standardized deliverables
- ✅ **KPI tracking framework** to measure results

---

## 🚀 Two-Minute Demo

**Scenario**: You need to reduce churn for a B2B SaaS client with 2,000 customers.

### Step 1: Configure (30 seconds)

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

### Step 2: Run the Pipeline (1–2 hours)

```bash
bash scripts/run_analysis.sh --use-case churn --config config.yaml
```

The script will walk you through:
1. **Data Prep** → Clean dataset, identify segments
2. **Core Analysis** → Answer key churn questions  
3. **Drill-down** → Explore high-risk cohorts
4. **Actionization** → Generate prioritized recommendations
5. **Iteration** → Validate findings, design A/B tests

### Step 3: Deliver (outputs auto-generated)

- **`outputs/recommendations.md`** → Executive summary
- **`outputs/recommendation_table.md`** → Action | Evidence | Impact | Effort | Metric
- **`outputs/kpi_tracking.yaml`** → Baseline, targets, review cadence

See **[examples/churn_analysis_example.md](examples/churn_analysis_example.md)** for a complete worked example.

---

## 🏆 Flagship Use Cases

### 1. SaaS/E-commerce Churn Analysis

**Promise**: Reduce 6-month logo churn by 10–20% through targeted retention interventions.

**Who it's for**: SaaS companies with 500+ subscribers, e-commerce with subscription boxes, B2B platforms.

**Deliverables**:
- Churn risk segmentation (plan, tenure, engagement)
- 3–5 high-impact retention strategies (winback campaigns, onboarding fixes, retention offers)
- A/B test designs + KPI dashboard spec

**Time to value**: 8 weeks from data intake to measurable churn reduction.

**Consulting package**: Run this as a $15k–$25k engagement or monthly retainer.

📄 **[Complete prompt + example →](prompts/use_cases/churn/PROMPT.md)**  
📊 **[Worked case study →](examples/churn_analysis_example.md)**

---

### 2. SMB AI Readiness Audit

**Promise**: Deliver a 2-week AI readiness assessment for small B2B/SaaS companies with clear quick-win automations and 12-month roadmap.

**Who it's for**: SMBs (10–100 employees) wanting to adopt AI but unsure where to start.

**Deliverables**:
- Current tech stack summary
- 3–5 quick-win automations (e.g., AI-powered support triage, sales email drafting)
- 12-month AI roadmap with estimated ROI ranges
- Tool recommendations + implementation effort

**Time to value**: 2-week engagement.

**Consulting package**: Run this as a $5k–$10k fixed-scope audit.

📄 **[Complete prompt + example →](prompts/use_cases/smb_ai_audit/PROMPT.md)**  
📊 **[Worked case study →](examples/smb_ai_audit_example.md)**

---

## 📁 File Structure

```
analysis-os/
├── README.md                    # This file
├── config.yaml                  # Analysis configuration
├── scripts/
│   └── run_analysis.sh          # One-command pipeline orchestration
├── checklists/
│   └── master_analysis_checklist.md  # Complete validation checklist
├── prompts/
│   ├── core/
│   │   ├── data_prep.md         # Stage 1: Data preparation
│   │   ├── core_analysis.md     # Stage 2: Core analysis
│   │   ├── drilldown.md         # Stage 3: Deep dives
│   │   ├── actionization.md     # Stage 4: Recommendations
│   │   └── iteration.md         # Stage 5: Validation
│   └── use_cases/
│       ├── churn/PROMPT.md      # Complete churn analysis prompt
│       ├── smb_ai_audit/PROMPT.md  # SMB AI readiness audit
│       ├── web_analytics/PROMPT.md
│       ├── market_research/PROMPT.md
│       └── [6 more modules...]
├── templates/
│   ├── recommendation_table.md  # Standard action table
│   └── output_template.md       # Executive summary format
├── examples/
│   ├── churn_analysis_example.md     # Full worked churn example
│   └── smb_ai_audit_example.md       # Full worked SMB AI audit
└── docs/
    ├── TUTORIAL.md              # Complete walkthrough + 2-week engagement template
    ├── KPI_TRACKING_FRAMEWORK.md
    ├── ARCHITECTURE.md          # Technical design
    ├── ROADMAP.md               # Future modules
    └── ENGAGEMENT_TEMPLATES.md  # Consulting package templates
```

---

## 🔧 The 5-Stage Pipeline

| Stage | Checklist | Prompt Template | Output |
|-------|-----------|-----------------|--------|
| **1. Data Prep** | `/checklists/` | `/prompts/core/data_prep.md` | Clean dataset, metadata |
| **2. Core Analysis** | `/checklists/` | `/prompts/core/core_analysis.md` | Key findings, answers |
| **3. Drill-down** | `/checklists/` | `/prompts/core/drilldown.md` | Segment insights |
| **4. Actionization** | `/checklists/` | `/prompts/core/actionization.md` | Prioritized recommendations |
| **5. Iteration** | `/checklists/` | `/prompts/core/iteration.md` | Validation, experiments |

### Run It All at Once

```bash
bash scripts/run_analysis.sh --use-case churn --config config.yaml
```

This will:
1. Validate your `config.yaml`
2. Print which stage is running
3. Write outputs to `/outputs/run-YYYYMMDD/`
4. Generate ready-to-use markdown skeletons for your AI tool

**See [QUICKSTART.md](QUICKSTART.md) for full instructions.**

---

## 🎓 All Use Cases

### Flagship Modules (Production-Ready)

1. **[Churn Analysis](prompts/use_cases/churn/)** - Reduce SaaS/subscription churn by 10–20%
2. **[SMB AI Audit](prompts/use_cases/smb_ai_audit/)** - AI readiness assessment for small businesses

### Additional Modules

3. **[Web Analytics](prompts/use_cases/web_analytics/)** - Optimize traffic, conversions, engagement
4. **[Market Research](prompts/use_cases/market_research/)** - Competitive intelligence, positioning
5. **[Marketing Attribution](prompts/use_cases/marketing_attribution/)** - Optimize spend, understand customer journey
6. **[Pricing Optimization](prompts/use_cases/pricing_optimization/)** - Maximize revenue through strategic pricing
7. **[Customer Segmentation](prompts/use_cases/customer_segmentation/)** - RFM, behavioral, demographic profiling
8. **[A/B Test Analysis](prompts/use_cases/ab_test_analysis/)** - Rigorous experiment analysis

**All modules** follow the same 5-stage pipeline and output standardized recommendation tables.

---

## 🏗️ Who This Is For

### ✅ Perfect For

- **Analytics consultants** who want to productize their process and run repeatable engagements
- **Technical founders** who need to turn data into action without hiring a full analytics team
- **Fractional CPOs/data leads** managing multiple SMB clients
- **AI-powered auditors** who want to systematize SMB assessments

### ❌ Not For

- Large enterprises with dedicated BI teams (this is for small, fast-moving teams)
- Pure data science research (this focuses on business action, not academic rigor)
- Real-time dashboarding (this is for strategic reviews, not live monitoring)

---

## 💼 Commercial Usage

### How Consultants Use This OS

**Month 1: Client Intake**
- Configure `config.yaml` with client's domain, questions, constraints
- Run `scripts/run_analysis.sh`
- Deliver recommendations deck + KPI tracking framework

**Ongoing: Monthly Reviews**
- Re-run analysis with updated data
- Track KPIs against baseline
- Iterate on experiments

**Pricing Models**:
- **One-time audit**: $5k–$25k (depending on complexity)
- **Monthly retainer**: $3k–$8k/month (includes data refresh, KPI review, experiment design)
- **Success fee**: Base fee + % of churn reduction or revenue lift

**See [docs/ENGAGEMENT_TEMPLATES.md](docs/ENGAGEMENT_TEMPLATES.md) for complete engagement templates.**

---

## 🔒 Best Practices

1. **Always start with data prep** - 80% of errors come from bad data
2. **Use checklists religiously** - They prevent blind spots
3. **Request evidence** - Ask AI to cite data for every claim
4. **Iterate with "why" prompts** - Drill down on surprising findings
5. **Design experiments** - Recommendations without tests are just hypotheses
6. **Track KPIs from day 1** - Use the KPI framework to measure impact

---

## 📖 Documentation

- **[QUICKSTART.md](QUICKSTART.md)** - Get running in 5 minutes
- **[docs/TUTORIAL.md](docs/TUTORIAL.md)** - Complete walkthrough + 2-week churn engagement template
- **[docs/KPI_TRACKING_FRAMEWORK.md](docs/KPI_TRACKING_FRAMEWORK.md)** - How to measure and track outcomes
- **[docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)** - Technical design and customization
- **[docs/ROADMAP.md](docs/ROADMAP.md)** - Planned modules and features
- **[docs/ENGAGEMENT_TEMPLATES.md](docs/ENGAGEMENT_TEMPLATES.md)** - Consulting package templates

---

## 🔗 Links

- **Repository**: https://github.com/labgadget015-dotcom/analysis-os
- **Issues**: https://github.com/labgadget015-dotcom/analysis-os/issues
- **Discussions**: https://github.com/labgadget015-dotcom/analysis-os/discussions

---

## 📄 License

MIT License - Feel free to use and adapt for your own consulting work.

**Status**: v1.0 - Production-ready for churn analysis and SMB AI audits.
