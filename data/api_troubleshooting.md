# API Troubleshooting Guide

## 401 Unauthorized Error

Cause:
The API token is invalid, expired, or missing.

Resolution:
1. Verify the API token is correct.
2. Ensure the Authorization header is present.
3. Generate a new API token if the current token has expired.

Example Header:

Authorization: Bearer YOUR_API_TOKEN

## 403 Forbidden Error

Cause:
The user does not have permission to access the resource.

Resolution:
1. Verify user roles.
2. Check API permissions.
3. Contact system administrator.