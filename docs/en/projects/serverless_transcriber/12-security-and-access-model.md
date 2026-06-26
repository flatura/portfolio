# Security and Access Model

## Access requirements

* Strict access control to the service.
* Complete isolation of user data.

## Authentication - Amazon Cognito (PKCE)

* **User Data Isolation:** AWS Cognito provides built-in account management, user registration, 2FA, brute-force protection, etc. The service integrates into the AWS ecosystem.
* Per-job access checks on download (`get_download_url` verifies user rights in DynamoDB before issuing a Presigned URL).

### Authentication sequence

```mermaid
sequenceDiagram
    autonumber
    
    actor U as Browser (SPA)
    participant API as API Gateway
    participant C as Amazon Cognito

    U->>API: Request to API without JWT in Header
    activate API
    API->>U: Redirect to login form
    deactivate API
    activate U
    U->>C: Navigate to login form
    deactivate U
    activate C
    C->>U: Login form 
    deactivate C
    activate U
    U->>C: Enter credentials and attempt authentication
    deactivate U
    activate C
    alt Valid credentials
        C-->>U: Credentials valid, return Auth Code
    else Invalid credentials
        C-->>U: Credentials invalid, return error
    end
    deactivate C
    activate U
    U->>C: Exchange Code for JWT (/oauth2/token)
    deactivate U
    activate C
    C-->>U: Access & ID Tokens
    deactivate C
```
