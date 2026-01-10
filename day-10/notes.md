# Day 10 — Topics Studied in Identity Service (FastAPI)

Today I focused on understanding some of the components that typically belong inside an identity/authentication service when implemented with FastAPI. The goal was to understand how authentication and user identification are handled in backend systems.

---

## Topics Studied Today

###  1. Router Initialization

Identity services generally group authentication-related endpoints under a router with a common prefix (e.g., `/auth`). This helps keep login, registration, token refresh, etc. organized and isolated.

---

###  2. Security-Related Setup

I studied two major security aspects commonly used in such services:

1. **Password Hashing**  
   - Use of hashing mechanisms via `CryptContext`
   - Handling deprecated hashing schemes
   - Ensures passwords are never stored in plain text

2. **OAuth2 Bearer Tokens**  
   - Tokens are passed using the pattern:  
     `Authorization: Bearer <token>`
   - Token issuer/URL is configured in the backend for dependency injection

---

###  3. Request Schemas

Identity services typically define schemas for:

- User registration
- User login

These use Pydantic models to declare the required fields and their types. This ensures that incoming data is structured and validated.

---

###  4. Determining Who is Calling the API

A very important part of identity services is knowing **who is hitting the API**. This requires extracting the identity from the token so that roles, permissions, or tenant context can be applied.

I studied how this is typically done:

- A helper function receives a token (via dependency injection)
- The token contains user claims inside the payload
- These claims determine **role**, **tenant**, **user ID**, etc.

This is foundational for RBAC (Role-Based Access Control).

---

###  5. Token Decoding & Payload Extraction (JWT-Based)

I studied how the JWT token’s payload can be decoded to retrieve user information. This involves:

- verifying the signature (using a secret key)
- validating the hashing algorithm
- extracting the payload claims

Payload is where the identity information actually resides.

---

###  6. Error Handling

Identity services must handle invalid token scenarios, such as:

- malformed tokens
- signature mismatch
- expired tokens
- unsupported algorithms

In such cases, the backend returns an authentication/authorization error.

---

##  Summary of Understanding

Identity services typically handle:

- authentication
- user identity extraction
- token validation
- password hashing
- role/tenant context for RBAC
- request validation

There are many additional components (e.g., permissions, refresh tokens, session handling, MFA, etc.) that I have not yet covered. For now, I studied the above subset.


