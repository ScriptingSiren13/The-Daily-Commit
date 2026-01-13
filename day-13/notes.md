# Day 13 — Identity Service: Security Fundamentals (High-Level)

Today I continued studying the Identity Service, specifically focusing on the **security layer** inside the auth flow. Instead of just onboarding and RBAC, the focus shifted to how tokens are actually created, secured, and validated inside the system.

---

##  Security Components Observed Today

I looked into how an identity service must handle certain cryptographic and security details, including:

- **Signature validation**  
- **Hashing algorithm selection**
- **Access token expiration**
- **JWT payload composition**

These are critical because an identity service not only verifies *who* someone is, but also ensures the token cannot be forged, tampered with, or used indefinitely.

---

##  Access Token Creation

I studied the helper responsible for generating the access token. Key details noted:

### **Payload Contents**
The token payload typically includes:

- `sub` (subject)
- `email`
- `role`
- `tenant_id`
- `exp` (expiration timestamp)

### **Expiration Handling**
I learned how expiration is added to the payload (usually as a Unix timestamp) and why it matters:

- prevents indefinite token reuse
- forces periodic re-authentication
- reduces surface for stolen token misuse

### **Signing & Hashing**
During token creation:

- a **secret key** is used to sign the token
- a **hashing algorithm** (e.g., HS256) is selected
- the resulting token ensures **integrity** — if modified, validation fails

I will document the token creation flow in more detail tomorrow after breaking down the helper and verifying how libraries expect the data to be passed.

---

##  Token Safety Observations

The Identity Service must ensure:

- correct secret key usage
- correct hashing algorithm usage
- safe expiration strategy
- secure claim handling

These are often overlooked but are foundational for secure multi-tenant systems.

---

## Additional Work Done Today

Aside from Identity Service exploration:

- I created a dedicated repo to store the LLM Engineering materials
- I pushed the structured output section into that repo
- I shared the project update publicly on LinkedIn

This lets my identity work stay clean in the Daily Commit repo, and keeps deeper technical work organized in its own repository.

---

##  Tomorrow's Plan

Tomorrow I will continue with the Identity Service focusing on:

- Access token helper implementation details
- How expiration and signing are configured in code
- How tokens are verified on inbound requests
- Where hashing fits into credential verification
- How secrets/algorithms are abstracted or configured

This will complete the foundation for the security portion of the identity subsystem.
