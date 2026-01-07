from datetime import date

def evaluate_rules(claim):
    risk_score = 0.0
    fraud_score = 0.0
    factors = []

    policy_age_days = (claim.submission_date - claim.policy.policy_start_date).days

    # Rule 1: New policy + high claim amount
    if policy_age_days < 60 and claim.claim_amount > 5000:
        risk_score += 0.3
        fraud_score += 0.2
        factors.append("New policy with high claim amount")

    # Rule 2: Multiple prior claims
    if claim.claimant.prior_claims_count >= 3:
        risk_score += 0.2
        factors.append("Multiple prior claims")

    # Rule 3: Weak evidence
    if claim.attachments.photos_count < 2:
        fraud_score += 0.2
        factors.append("Low number of supporting photos")

    return risk_score, fraud_score, factors