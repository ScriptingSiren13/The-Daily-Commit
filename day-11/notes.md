# Day 11 — Understanding Identity Service in Multi-Tenant Architecture

##  Context from Day 10
Yesterday, I studied the foundations of authentication in an identity service, focusing on:
- JWT structure (header, payload, signature)
- Role-based access control (RBAC)
- Token validation
- Password hashing
- OAuth2 bearer token usage
- Helper function for extracting claims from tokens

Today builds directly on that understanding.

---

##  Today's Focus
Today I moved from isolated auth concepts to understanding **how an identity service must work as a subsystem** in a multi-tenant application. Instead of looking at code directly, I mapped out the **core responsibilities and flow** required for such a system to work correctly.

---

## Identity Service Responsibilities

A multi-tenant identity service must handle:

- Creating tenants
- Provisioning users into tenants
- Bootstrapping an admin for the tenant
- Authenticating users (login)
- Issuing access tokens (JWT)
- Enforcing RBAC rules
- Validating tokens and extracting claims

These responsibilities enable **separation between tenants**, **permission enforcement**, and **secure session management**.

---

##  Bootstrap Admin Model

A key concept in multi-tenant identity is the **bootstrap admin**.

I initially assumed user registration might precede tenant creation, but later realized that the correct onboarding sequence is:

1. **Tenant is created**
2. **Bootstrap admin is provisioned for that tenant**
3. **Bootstrap admin registers additional users**
4. **Users authenticate via login**
5. **Token contains tenant + role claims**

This sequencing ensures:
- users belong to a tenant
- admins do not cross tenant boundaries
- RBAC can be enforced correctly

---

##  Token Claims & RBAC

Tokens issued by the login endpoint typically include claims such as:

- `sub` (subject)
- `email`
- `role`
- `tenant_id`

These fields allow downstream services to determine:

- **who is calling**
- **what role they have**
- **which tenant they belong to**
- **which resources they may access**

This aligns with the RBAC model studied on Day 10.

---

##  Endpoint Categories Identified

The identity service logically needs at least these endpoints:

### 1. Tenant Creation
Creates a tenant and returns its tenant identifier.

### 2. Bootstrap Admin Creation
Associates a privileged user with that tenant so that provisioning can begin.

### 3. User Registration
Admin registers additional users under the same tenant.

### 4. Login
Authenticates a user and issues JWT tokens containing claims.

### 5. `/me`
Debug endpoint for inspecting current identity via token claims.

Understanding these endpoints clarified how authentication, authorization, and onboarding fit together.

---

##  Key Takeaways

- Multi-tenant identity requires **tenant boundaries** and **role boundaries**
- Bootstrapping is necessary because someone must exist with rights to provision users
- Tokens are not only for login, they carry **context**
- RBAC enforcement depends heavily on token claims
- Payloads and tokens propagate tenant and role information across services


