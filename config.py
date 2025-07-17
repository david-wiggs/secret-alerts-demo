#!/usr/bin/env python3
"""
Application configuration with various secrets
This file contains intentional test secrets for demonstration purposes
"""

import os

# Cloud provider credentials
AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

AZURE_CLIENT_SECRET = "1234567890abcdefghijklmnopqrstuvwxyz~ABCDE"
AZURE_TENANT_ID = "12345678-1234-1234-1234-123456789012"

GCP_SERVICE_ACCOUNT_KEY = """{
  "type": "service_account",
  "project_id": "my-test-project",
  "private_key_id": "1234567890abcdefghijklmnopqrstuvwxyz123456",
  "private_key": "-----BEGIN PRIVATE KEY-----\\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC+1234567890ab\\ncdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890ab\\n-----END PRIVATE KEY-----\\n",
  "client_email": "test@my-test-project.iam.gserviceaccount.com",
  "client_id": "123456789012345678901",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token"
}"""

# SSH Keys (fake)
SSH_PRIVATE_KEY = """-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAFwAAAAdzc2gtcn
NhAAAAAwEAAQAAAQEA1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP
QRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWX
YZ1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456
7890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcd
efghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
-----END OPENSSH PRIVATE KEY-----"""

# Database connections
DATABASE_CONNECTIONS = {
    'postgres': 'postgresql://superuser:ultra_secret_db_password_2023@pg.example.com:5432/maindb',
    'mysql': 'mysql://root:mysql_root_password_secret_2023@mysql.example.com:3306/app',
    'mongodb': 'mongodb://admin:mongo_admin_secret_pass_2023@mongo.example.com:27017/app'
}

# API Keys and tokens
API_CREDENTIALS = {
    'openai_api_key': 'sk-1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
    'anthropic_api_key': 'ant-api01-1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-ABCDEFGHIJKLMNOPQRSTUVWXYZ123456',
    'cohere_api_key': 'co-1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
    'huggingface_token': 'hf_1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
}

# Webhook secrets
WEBHOOK_SECRETS = {
    'github_webhook_secret': 'github_webhook_secret_key_1234567890abcdefghijklmnop',
    'stripe_webhook_secret': 'whsec_1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP',
    'paypal_webhook_id': 'WH-1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
}

# Encryption keys
ENCRYPTION_KEYS = {
    'aes_key': '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456',
    'rsa_private_key': """-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP
QRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWX
YZ1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456
7890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
-----END RSA PRIVATE KEY-----"""
}

def get_database_url():
    return DATABASE_CONNECTIONS['postgres']

def get_api_key(service):
    return API_CREDENTIALS.get(service)

if __name__ == "__main__":
    print("Configuration loaded with secrets")
    print(f"Database URL: {get_database_url()}")
    print(f"OpenAI API Key: {get_api_key('openai_api_key')}")
