# AI-Driven QA Requirements Analyzer

A complete, production-grade QA automation framework delivered as 5 standalone HTML files. Open any file directly in your browser — no server, build step, npm, or external dependencies required.

## Quick Start

1. Open `index.html` in your browser for the navigation hub, or open any widget directly.
2. Enter your Anthropic API key when prompted (stored in browser memory only).
3. Start with **Widget 1** — paste or upload requirements and click **Analyze**.

## Files

| File | Description |
|------|-------------|
| `index.html` | Navigation hub — links to all widgets |
| `widget1-core-analyzer.html` | Ingestion, NLP extraction, quality scoring, Gherkin gen, RTM, ambiguity detection, exports |
| `widget2-advanced-analysis.html` | Req drilldown, change impact, domain KB, compliance (GDPR/OWASP/HIPAA/PCI/WCAG/SOC2), risk heatmap, AI enhance |
| `widget3-generation-operations.html` | Test case gen, test data gen, script gen (Playwright/Selenium/Cypress), defect predictor, analytics, executive report |
| `widget4-workspace.html` | State machine visualizer, API contract tester, dependency mapper, sprint board, effort estimator, version history, global search |
| `widget5-ai-tools.html` | Prompt library, LLM playground, model comparison, test runner console, benchmark, webhook logs, onboarding |

## API Key

Each widget prompts for your Anthropic API key on first use. The key is:
- Stored in browser memory (`let AKEY = ''`)
- Sent exclusively to `https://api.anthropic.com/v1/messages`
- Never logged, persisted, or sent anywhere else
- Cleared when you close or refresh the tab

Get a key at [console.anthropic.com](https://console.anthropic.com).

## Features by Widget

### Widget 1 — Core Analyzer
- **Ingestion**: File upload (txt, yaml, feature) or paste
- **NLP extraction**: Actors, preconditions, postconditions, acceptance criteria, business rules
- **Quality scoring**: INVEST/SMART evaluation per requirement (0–100%)
- **Gherkin generation**: Happy path, negative, boundary, edge case scenarios
- **RTM builder**: Bidirectional traceability with coverage analysis
- **Ambiguity detection**: Flags vague terms, detects conflicting requirements
- **Exports**: JSON catalog, .feature file, CSV RTM, HTML report

### Widget 2 — Advanced Analysis
- **Req drilldown**: Deep AI analysis of a single requirement
- **Change impact**: Word-level diff + AI impact report for version changes
- **Domain KB**: Extracts terms, business rules, entities, integration points
- **Compliance checker**: GDPR, HIPAA, PCI-DSS, OWASP, WCAG 2.1, SOC 2
- **OWASP mapping**: Top 10 reference + requirement-specific security test gen
- **Risk heatmap**: Interactive 4×4 impact vs probability matrix
- **AI enhance**: Rewrites weak requirements with full AC, edge cases, NFRs

### Widget 3 — Generation & Operations
- **Test case gen**: Happy/negative/boundary/edge in step-by-step, Gherkin, or table format
- **Test data gen**: Valid, invalid, boundary, null/empty, SQL injection, XSS payloads
- **Script gen**: Playwright (Python/JS), Selenium, Cypress, Pytest — POM or BDD
- **Defect predictor**: AI hotspot analysis with probability bars and recommendations
- **Analytics**: Coverage by type, risk distribution metrics
- **Executive report**: AI-generated report for executives, QA team, or auditors

### Widget 4 — Workspace & Visualization
- **State machine**: Generate and visualize workflow state diagrams
- **API contract**: Analyze OpenAPI/Swagger specs for test requirements
- **Dependency map**: Layer-by-layer dependency visualization with critical path
- **Sprint board**: Drag-and-drop kanban with AI prioritization
- **Effort estimator**: Test case count, automation %, hours, sprints
- **Version history**: Audit trail with timestamps and authors
- **Global search**: Keyword search + AI semantic question answering
- **Collaboration**: Team members, review queue, inline comments

### Widget 5 — AI Tools & System
- **Prompt library**: CRUD editor for all LLM prompts with 6 built-in templates
- **LLM playground**: System/user prompt editor with streaming and run history
- **Model comparison**: Side-by-side output with latency, length, and AI verdict
- **Test runner**: Animated console with 4 built-in test suites
- **Benchmark**: p50/p95/p99 latency measurement with bar visualization
- **Webhook logs**: Event history + test payload generator
- **Onboarding**: 8-step interactive setup checklist with CLI commands
- **Feature tour**: Clickable map of all 40+ panels

## Backend Architecture (Production)

For production deployment, pair these widgets with a FastAPI backend:

```
requirements-analyzer/
├── backend/
│   ├── api/          # FastAPI routes
│   ├── core/         # Business logic
│   ├── parsers/      # PDF, DOCX, XLSX parsers
│   ├── ai/           # LLM prompt chains
│   ├── analyzers/    # Quality, risk, conflict analyzers
│   ├── generators/   # Gherkin, RTM, report generators
│   ├── integrations/ # Jira, ADO, Confluence connectors
│   └── models/       # Pydantic data models
├── docker-compose.yml
├── requirements.txt
└── README.md
```

**Stack**: FastAPI · PostgreSQL · Redis · ChromaDB · Celery · Anthropic SDK

## Tech Stack (Frontend)

- Vanilla HTML/CSS/JS — zero dependencies, zero build step
- Anthropic Messages API with streaming (`anthropic-dangerous-direct-browser-access: true`)
- CSS custom properties for full dark mode support
- Drag-and-drop via HTML5 Drag and Drop API
- File export via Blob + URL.createObjectURL

## License

MIT — use freely for commercial and non-commercial projects.
