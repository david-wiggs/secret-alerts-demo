# GitHub Personal Access Token Configuration
# This file contains intentional test GitHub tokens for demonstration

# GitHub Personal Access Token (fake but follows pattern)
GITHUB_TOKEN=ghp_1234567890abcdefghijklmnopqrstuvwxyzABCD

# GitHub App Installation Token (fake)
GITHUB_APP_TOKEN=ghs_1234567890abcdefghijklmnopqrstuvwxyzEFGH

# GitHub OAuth Token (fake)
GITHUB_OAUTH_TOKEN=gho_1234567890abcdefghijklmnopqrstuvwxyzIJKL

# GitHub Refresh Token (fake)  
GITHUB_REFRESH_TOKEN=ghr_1234567890abcdefghijklmnopqrstuvwxyzMNOP

# Shell script using GitHub token
curl -H "Authorization: token $GITHUB_TOKEN" \
     -H "Accept: application/vnd.github.v3+json" \
     https://api.github.com/user

# Git configuration with token
git remote set-url origin https://$GITHUB_TOKEN@github.com/username/repo.git

echo "GitHub authentication configured"
