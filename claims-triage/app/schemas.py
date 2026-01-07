from pydantic import BaseModel
from typing import List
from datetime import date

class Policy(BaseModel):
    policy_id: str
    policy_start_date: date

class Claimant(BaseModel):
    prior_claims_count: int

class Attachments(BaseModel):
    photos_count: int = 0
    documents_count: int = 0

class ClaimRequest(BaseModel):
    claim_id: str
    claim_type: str
    claim_amount: float
    currency: str
    incident_date: date
    submission_date: date
    policy: Policy
    claimant: Claimant
    attachments: Attachments

class ClaimResponse(BaseModel):
    claim_id: str
    risk_score: float
    fraud_score: float
    complexity: str
    recommended_path: str
    sla_priority: str
    decision_factors: List[str]
    rules_version: str

