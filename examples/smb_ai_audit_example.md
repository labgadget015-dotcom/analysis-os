# SMB AI Readiness Audit Example

> **Client**: CloudBooks - B2B SaaS accounting software (42 employees, $3.2M ARR)  
> **Engagement**: 2-week AI readiness assessment  
> **Investment**: $8k fixed scope  
> **Expected Value**: $180k/year in cost savings + productivity gains  
> **ROI**: 22x over 12 months  

---

## 🎯 Executive Summary

### The Problem

CloudBooks, a 42-person B2B SaaS accounting platform, wanted to adopt AI but didn't know where to start. Their team was overwhelmed by AI hype, unsure which tools provided real ROI, and lacked a systematic framework for evaluating opportunities.

**Pain points**:
- Customer support team spending 60% of time on repetitive tier-1 questions
- Sales reps manually drafting proposals and follow-up emails
- No AI governance or security policies in place
- Engineering team exploring LLMs but no clear roadmap

### The Approach

We ran a systematic 2-week AI readiness audit using the Analysis OS framework:

**Week 1: Discovery & Analysis**
1. **Data Prep** - Interviewed 12 stakeholders, mapped current tech stack
2. **Core Analysis** - Identified 8 AI opportunity areas across support, sales, product, and ops
3. **Drill-down** - Scored each opportunity on impact, effort, and risk

**Week 2: Recommendations & Roadmap**
4. **Actionization** - Prioritized top 5 quick wins + 12-month roadmap
5. **Iteration** - Built ROI models, implementation plans, and governance framework

**Total time**: 2 weeks from kickoff to final deliverable.

### The Results

**Immediate Quick Wins** (0–3 months):  
1. AI-powered support triage - Save 15 hours/week, $42k/year
2. Sales email drafting assistant - Save 8 hours/week, $28k/year
3. Automated meeting summaries - Save 10 hours/week across team, $35k/year

**6-Month Initiatives**:  
4. AI-enhanced code review - Reduce bug density 25%, $45k/year value
5. Customer onboarding automation - Improve activation rate 12%, $30k/year

**12-Month Strategic Bets**:  
6. AI-powered insights in product - New premium feature, $120k/year ARR potential

**Total projected value**: $180k/year cost savings + $120k new revenue = $300k/year

---

## Stage 1: Discovery & Data Preparation

### Stakeholder Interviews

**Completed**: 12 interviews across 4 departments  
- Support (3): Manager + 2 agents  
- Sales (3): VP Sales + 2 AEs  
- Product/Eng (4): CTO + 3 engineers  
- Operations (2): CEO + Operations Manager  

### Current Tech Stack Audit

**SaaS Tools** (23 total):  
- Customer Support: Intercom, Zendesk  
- Sales: HubSpot CRM, Calendly  
- Product: GitHub, Linear, Figma  
- Data: PostgreSQL, Segment, Mixpanel  
- Communication: Slack, Zoom, Notion  

**AI/ML Capabilities** (current):  
- Intercom chatbot (basic intent detection)  
- HubSpot email scoring (black box)  
- No custom AI/ML models  
- No AI governance or security policies  

### Pain Point Analysis

| Department | Top Pain Point | Hours/Week Wasted | Annual Cost |
|------------|----------------|-------------------|-------------|
| Support | Tier-1 question triage | 15 hrs | $42k |
| Sales | Manual email drafting | 8 hrs | $28k |
| Product | Code review delays | 12 hrs | $45k |
| Operations | Meeting notes + follow-up | 10 hrs | $35k |
| **Total** | **Multi-department waste** | **45 hrs/week** | **$150k/year** |

---

## Stage 2: Core Analysis - AI Opportunity Scoring

### Framework Used

We scored 8 identified AI opportunities across 4 dimensions:

1. **Impact** (1–10): Revenue lift or cost savings  
2. **Effort** (1–10): Implementation complexity (lower = easier)  
3. **Risk** (1–10): Data, security, accuracy concerns (lower = safer)  
4. **Time to Value** (weeks): How quickly ROI is realized  

### Opportunity Matrix

| Opportunity | Impact | Effort | Risk | Time to Value | Priority Score |
|-------------|--------|--------|------|---------------|----------------|
| **1. Support triage AI** | 8 | 3 | 2 | 4 weeks | **High** |
| **2. Sales email assistant** | 7 | 2 | 1 | 2 weeks | **High** |
| **3. Meeting summarization** | 7 | 2 | 1 | 1 week | **High** |
| **4. Code review AI** | 8 | 6 | 4 | 12 weeks | **Medium** |
| **5. Onboarding automation** | 7 | 5 | 3 | 8 weeks | **Medium** |
| 6. Automated release notes | 4 | 3 | 2 | 6 weeks | Low |
| 7. Customer health scoring | 6 | 7 | 5 | 16 weeks | Low |
| 8. AI product feature (insights) | 9 | 9 | 6 | 24 weeks | Strategic |

**Quick Wins** (High priority): Initiatives 1–3  
**6-Month Bets** (Medium priority): Initiatives 4–5  
**12-Month Strategic**: Initiative 8  

---

## Stage 3: Drill-Down - Tool Selection & ROI Modeling

### Quick Win #1: AI Support Triage

**Problem**: Support team spends 60% of time routing tier-1 questions that could be auto-answered.

**Solution**: Implement AI-powered triage using existing Intercom + GPT-4 integration.

**Implementation**:  
- Week 1: Configure Intercom AI workflows  
- Week 2: Train on 500 historical support tickets  
- Week 3: Pilot with 20% of incoming tickets  
- Week 4: Full rollout + monitoring  

**ROI Model**:  
- Current: 15 hours/week @ $35/hr fully loaded = $27,300/year  
- Tool cost: Intercom AI add-on $200/month = $2,400/year  
- **Net savings**: $24,900/year  
- **Payback**: <1 month  

---

### Quick Win #2: Sales Email Assistant

**Problem**: Sales reps spend 2 hours/day drafting personalized follow-up emails.

**Solution**: Deploy HubSpot AI Email Writer + custom prompt library.

**Implementation**:  
- Week 1: Enable HubSpot AI, build 10 email templates  
- Week 2: Train sales team, collect feedback, iterate  

**ROI Model**:  
- Current: 2 hrs/day/rep × 2 reps × 5 days = 20 hrs/week @ $40/hr = $41,600/year  
- Reduce by 40% = 8 hours saved/week = $16,640/year  
- Tool cost: Included in existing HubSpot plan = $0  
- **Net savings**: $16,640/year  
- **Payback**: Immediate  

---

### Quick Win #3: Meeting Summarization

**Problem**: Team spends 10 hours/week taking notes and writing follow-up emails post-meeting.

**Solution**: Deploy Fireflies.ai or Otter.ai for all internal + customer meetings.

**Implementation**:  
- Week 1: Purchase licenses, integrate with Zoom/Calendar  
- Week 2: Train team on reviewing summaries + action items  

**ROI Model**:  
- Current: 10 hrs/week across team @ $50/hr avg = $26,000/year  
- Reduce by 60% = 6 hours saved/week = $15,600/year  
- Tool cost: Fireflies Business plan $120/month = $1,440/year  
- **Net savings**: $14,160/year  
- **Payback**: 1 month  

---

## Stage 4: Actionization - Prioritized Recommendations

### 12-Month AI Roadmap

#### Phase 1: Quick Wins (0–3 months) - $8k investment

| Initiative | Tool | Investment | Annual Savings | Payback |
|------------|------|------------|----------------|----------|
| Support triage AI | Intercom AI | $2.4k/year | $24.9k | <1 month |
| Sales email assistant | HubSpot AI | $0 (included) | $16.6k | Immediate |
| Meeting summaries | Fireflies.ai | $1.4k/year | $14.2k | 1 month |
| AI governance policy | Internal doc | 8 hours work | Risk mitigation | N/A |
| **Total Phase 1** | **Multiple** | **~$4k** | **$55.7k/year** | **<2 months** |

#### Phase 2: Medium Bets (3–6 months) - $18k investment

| Initiative | Tool | Investment | Annual Value | Payback |
|------------|------|------------|--------------|----------|
| AI code review | GitHub Copilot Enterprise | $8k setup + $5k/year | $45k (bug reduction) | 3 months |
| Onboarding automation | Custom GPT-4 workflow | $10k dev | $30k (activation lift) | 4 months |
| **Total Phase 2** | **Multiple** | **$18k** | **$75k/year** | **3–4 months** |

#### Phase 3: Strategic (6–12 months) - $65k investment

| Initiative | Description | Investment | Annual Revenue Potential |
|------------|-------------|------------|-------------------------|
| AI Insights Premium Feature | Add GPT-powered financial insights to product | $65k dev (3 eng-months) | $120k ARR (10 enterprise customers @ $1k/month upgrade) |

### Total Investment & ROI

**Total 12-month investment**: $8k + $18k + $65k = **$91k**  
**Year 1 value**:  
- Cost savings: $55.7k + $75k = $130.7k  
- New revenue (pro-rated 6 months): $60k  
- **Total Year 1**: $190.7k  

**ROI**: ($190.7k - $91k) / $91k = **110% first-year ROI**  
**Payback period**: ~6 months  

---

## Stage 5: Implementation & Governance

### AI Governance Framework

We delivered a 12-page AI governance policy covering:

1. **Data Privacy**: What customer data can be sent to AI APIs  
2. **Security**: Approved vendors (OpenAI, Anthropic, Google only)  
3. **Accuracy Standards**: When human review is required (customer-facing content)  
4. **Vendor Evaluation**: 5-point checklist for new AI tools  
5. **Incident Response**: What to do if AI produces harmful output  

### Success Metrics (KPIs to Track)

**30-Day Metrics**:
- [ ] 3 quick-win tools deployed  
- [ ] AI governance policy approved by leadership  
- [ ] 80% of team trained on new AI tools  

**90-Day Metrics**:
- [ ] Support resolution time reduced by 25%  
- [ ] Sales email response rate increased 15%  
- [ ] Meeting follow-up time reduced 50%  

**6-Month Metrics**:
- [ ] Code review cycle time reduced 20%  
- [ ] Customer activation rate increased 12%  
- [ ] Phase 2 initiatives delivering projected ROI  

**12-Month Metrics**:
- [ ] AI Insights feature launched with 10+ paying customers  
- [ ] Total realized savings ≥ $130k  
- [ ] Team AI literacy score >8/10  

---

## Key Takeaways

1. **Start Small, Think Big**: Quick wins (Phase 1) funded bigger bets (Phase 3)
2. **Governance First**: AI policy prevented security incidents and built trust
3. **ROI-Driven**: Every recommendation had a clear financial model
4. **Tool Pragmatism**: Used off-the-shelf SaaS AI vs. building custom models
5. **Change Management**: 80% of value came from adoption, not technology

---

## Files Used in This Engagement

```
/prompts/use_cases/smb_ai_audit/PROMPT.md  → AI audit template
/templates/recommendation_table.md         → Prioritization framework
/docs/KPI_TRACKING_FRAMEWORK.md            → Success metrics
/config.yaml                                → Engagement parameters
```

---

## How to Replicate This Audit

### For Different Company Sizes

- **10–25 employees**: Focus only on Phase 1 quick wins ($3k–$5k engagement)  
- **25–75 employees**: Full 3-phase roadmap (this example, $8k–$10k)  
- **75–150 employees**: Add departmental AI champions, $15k–$20k engagement  

### For Different Industries

- **E-commerce**: Focus on inventory forecasting, customer service AI, personalization  
- **Professional Services**: Emphasize proposal automation, client research, billing AI  
- **Healthcare**: Prioritize compliance, HIPAA-safe AI vendors, clinical documentation  

---

**End of Example** | [Back to Main README](../../README.md)
