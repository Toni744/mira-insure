import os

AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
CLAIMS_TABLE = os.getenv("CLAIMS_TABLE", "claims-triage-table")
RULES_VERSION = "v1.0.0"