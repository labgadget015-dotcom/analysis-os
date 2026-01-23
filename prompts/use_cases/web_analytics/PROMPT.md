# Web Analytics - Complete Prompt

## 🎯 Use Case
Optimize website traffic, conversions, and user engagement through data-driven insights.

---

## 📝 Complete All-in-One Prompt

```
You are an experienced web analytics expert and conversion rate optimization specialist.

**ROLE & CONTEXT**
I have web analytics data covering [TIME PERIOD] with [X] sessions/users.

Key data available:
- Traffic sources: [organic, paid, direct, referral, social]
- User behavior: [page views, bounce rate, time on site, pages per session]
- Conversion data: [conversion events, funnel stages, revenue]
- Content performance: [top pages, exit pages, engagement metrics]
- Technical data: [device type, browser, location]

**YOUR OBJECTIVE**
Answer these business questions:

1. **Which pages/traffic sources have highest bounce rates and why?**
   (Identify problem areas requiring optimization)

2. **What drives conversions?**
   (Analyze conversion paths, high-performing content, user segments)

3. **Where should we invest in content/UX improvements?**
   (Prioritize pages/features by impact potential)

4. **What's the estimated ROI of optimization efforts?**
   (Quantify revenue impact of improvements)

**CONSTRAINTS**
- Focus on data from [DATE RANGE]
- Optimization budget: $[X]
- Development resources: [Y sprint capacity]
- Timeline: [Z weeks to implement]

**ANALYSIS PIPELINE**

### Stage 1: Data Prep
- Profile traffic volume and trends
- Validate tracking implementation
- Segment users (new vs returning, device, source)
- Identify data quality issues

### Stage 2: Core Analysis
- Calculate key metrics: bounce rate, conversion rate, avg session value
- Identify top/bottom performing pages
- Analyze traffic source effectiveness
- Map conversion funnels

### Stage 3: Drill-down
- Investigate high-bounce pages
- Analyze conversion drop-off points
- Compare segments (mobile vs desktop, new vs returning)
- Identify content gaps

### Stage 4: Actionization
- Generate prioritized optimization recommendations
- Estimate impact of each improvement
- Create implementation roadmap

### Stage 5: Iteration
- Design A/B tests
- Set success metrics
- Plan measurement strategy

**OUTPUT FORMAT**

## Executive Summary
- Current conversion rate: [X%]
- Top opportunity: [Specific finding]
- Estimated impact: [+Y% conversion, $Z revenue]

## Traffic Overview
- Total sessions: [X]
- Unique users: [Y]
- Avg session duration: [Z min]
- Overall bounce rate: [A%]
- Conversion rate: [B%]

## Key Findings

### Q1: High Bounce Rate Pages
[Top 5 pages with analysis]

### Q2: Conversion Drivers
[What works well and why]

### Q3: Optimization Priorities
[Ranked list with ROI estimates]

### Q4: Revenue Impact
[Financial projections]

## Recommendations

| Recommendation | Current Metric | Target | Impact | Effort | Priority |
|----------------|----------------|--------|--------|--------|----------|
| [Action 1] | [X%] | [Y%] | [+$Z] | [L/M/H] | [1-5] |

## A/B Test Plan
[Design for top recommendation]
```

---

## 📊 Example Outputs

### Example Finding
```
**Q1: High Bounce Rate Pages**

Top 3 problem pages:

1. **/pricing** - 78% bounce rate (2.1x site average)
   - 15,420 sessions/month
   - Hypothesis: Page loads slowly (4.2s), lacks clear CTA
   - Evidence: Users exit within 5 seconds (89% of bounces)
   
2. **/blog/category/technical** - 71% bounce rate
   - 8,200 sessions/month from organic search
   - Issue: Content doesn't match search intent
   - Bounce users have 0% conversion vs 3% site average

3. **/signup** - 65% bounce rate on mobile only
   - Desktop: 22% bounce, Mobile: 65% bounce
   - Problem: Form not mobile-optimized (12 fields)
```

### Example Recommendation
```
**Recommendation 1: Optimize Pricing Page Load Speed**

**Current State:**
- Load time: 4.2 seconds
- Bounce rate: 78%
- 15,420 sessions/month
- Estimated lost conversions: 463/month

**Proposed Changes:**
- Compress images (reduce 2.3MB to 400KB)
- Lazy load below-fold content
- Implement CDN for static assets
- Target load time: <1.5s

**Expected Impact:**
- Bounce rate: 78% → 45% (industry benchmark for <2s load)
- Additional conversions: +230/month (from currently bouncing traffic)
- Revenue impact: 230 × $89 avg deal = +$20,470/month = $245K/year

**Implementation:**
- Week 1: Image optimization (Dev team, 8 hours)
- Week 2: CDN setup (DevOps, 4 hours)
- Week 3: Testing and monitoring
- Total effort: 12 dev hours = LOW effort

**A/B Test Design:**
- Control: Current pricing page
- Treatment: Optimized version
- Sample size: 10,000 sessions per variant
- Duration: 2 weeks
- Success metric: Bounce rate < 50%
- Guardrail: Conversion rate doesn't decrease

**Priority: 1** (Highest impact, lowest effort)
```

---

## ✅ Checklist

- ✅ Analyzed traffic from at least 3 sources
- ✅ Identified 3+ high-impact optimization opportunities
- ✅ Calculated conversion rate improvement potential
- ✅ Estimated revenue impact ($X/year)
- ✅ Prioritized recommendations by ROI
- ✅ Designed A/B test for top recommendation
- ✅ Included mobile vs desktop analysis

---

## Next Steps

1. Copy prompt to AI tool
2. Replace [PLACEHOLDERS] with your GA4/analytics data
3. Include screenshots or data exports
4. Review findings and refine
5. Implement top recommendations with A/B testing
