# AWS Configuration Example
# This file has been cleaned of secrets

# AWS configuration (use environment variables or IAM roles instead)
export AWS_DEFAULT_REGION=us-east-1
export AWS_PROFILE=development

# Database connection (moved to environment variables)
# DATABASE_URL should be set via environment

echo "AWS configuration loaded from environment"
