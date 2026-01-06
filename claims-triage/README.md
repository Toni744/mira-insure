# Claims Triage & Fraud Scoring API

A rules-based, explainable claims triage service for insurance platforms.  
This API evaluates incoming claims and classifies them by risk, fraud likelihood, and recommended handling path, with full auditability and idempotency.

This project intentionally does not use AI or ML. The system is deterministic, explainable, and production-ready. AI can be layered on later without re-architecture.

## Why This Exists

Insurance claims teams face:

- High claim volumes
- Expensive manual reviews
- Late-stage fraud detection
- Slow customer payouts

This service addresses those problems by:

- Automatically triaging claims at ingestion
- Flagging risk and fraud signals early
- Routing claims to the correct workflow
- Providing human-readable decision explanations

## Key Features

- Idempotent API (safe retries)  
- Rules-based scoring (no black boxes)  
- Explainable decisions (audit-friendly)  
- Clear routing outcomes  
- AWS-ready architecture  
- Designed for B2B and multi-tenant use  

## High-Level Architecture

Client / Insurer System  
→ API Gateway  
→ FastAPI Service  
→ Rules Engine  
→ Decision Engine  
→ DynamoDB (results and audit)

## API Overview

- `POST /v1/claims/triage` — Runs triage on a claim and returns a routing decision.  
- `GET /health` — Health check endpoint.

### Example Request

```json
{
  "claim_id": "claim_123",
  "claim_type": "auto",
  "claim_amount": 4500,
  "currency": "CAD",
  "incident_date": "2026-01-01",
  "submission_date": "2026-01-02",
  "policy": {
    "policy_id": "policy_abc",
    "policy_start_date": "2025-11-15"
  },
  "claimant": {
    "prior_claims_count": 3
  },
  "attachments": {
    "photos_count": 6,
    "documents_count": 2
  }
}
```

### Example Response

```json
{
  "claim_id": "claim_123",
  "risk_score": 0.65,
  "fraud_score": 0.3,
  "complexity": "medium",
  "recommended_path": "human_adjuster",
  "sla_priority": "standard",
  "decision_factors": [
    "New policy with high claim amount",
    "Multiple prior claims"
  ],
  "rules_version": "v1.0"
}
```

## Decision Outputs Explained

| Field            | Meaning                                  |
|------------------|------------------------------------------|
| risk_score       | Overall claim risk (0–1)                 |
| fraud_score      | Fraud likelihood indicator               |
| complexity       | low / medium / high                      |
| recommended_path | Workflow routing                         |
| sla_priority     | Processing urgency                       |
| decision_factors | Human-readable explanations              |

## Recommended Claim Paths

| Path           | Description                         |
|----------------|-------------------------------------|
| auto_approve   | Low risk, minimal review            |
| fast_track     | Simple claim, quick handling        |
| human_adjuster | Standard manual review              |
| fraud_review   | SIU or fraud investigation          |

## Project Structure

```
claims-triage/
├── app/
│   ├── main.py        # API entry point
│   ├── config.py      # Configuration
│   ├── schemas.py     # Request and response models
│   ├── rules.py       # Deterministic rules engine
│   ├── decision.py    # Routing logic
│   ├── service.py     # Orchestration layer
│   └── storage.py     # Persistence and idempotency
├── requirements.txt
└── README.md
```

## Running Locally

### Requirements

- Python 3.10+
- AWS credentials (for DynamoDB access)

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the API

```bash
uvicorn app.main:app --reload
```

Open Swagger UI: http://localhost:8000/docs

## Data Storage

This project assumes AWS DynamoDB for:

- Idempotency
- Audit logs
- Decision replay

Minimum table schema:

- `claim_id` (partition key)  
- Decision output  
- Timestamp  
- Rules version

## Security Considerations

- Stateless API design  
- Designed for API key or JWT authentication  
- No image or document storage  
- Minimal PII exposure  
- Explainability-first decision logic

## What This Project Does Not Include

- Machine learning or AI  
- Claims payment or settlement logic  
- Pricing or underwriting  
- Frontend UI  
- Regulatory-specific workflows

These are intentionally excluded to keep the system safe, explainable, and extensible.

## Roadmap

- Rules-as-code (DSL)  
- Tenant-level rule customization  
- Async webhooks  
- Photo-based evidence analysis  
- ML-assisted fraud scoring  
- Policy versioning and rollback  
- Full Terraform deployment

## Intended Users

- Insurtech startups  
- Regional insurers  
- Managing General Agents (MGAs)  
- Platform, SRE, and DevOps engineers  
- Claims operations teams

## License

This project is licensed under the GNU General Public License v3.0 (GPL-3.0). See the LICENSE file for details.