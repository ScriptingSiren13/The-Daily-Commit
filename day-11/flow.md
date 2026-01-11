# Identity Service Flow — Multi-Tenant Overview

##  Onboarding Flow

1. **Create Tenant**
   - System establishes a tenant and issues tenant identifier.

2. **Bootstrap Admin**
   - A privileged user is assigned to the tenant.
   - Gains ability to register additional users.

3. **User Registration**
   - Admin provisions users under the same tenant.

4. **User Login**
   - User authenticates via credentials and receives JWT token.

5. **Token Propagation**
   - Token contains tenant and role claims for access decisions.

---

##  Claims Propagation Model

Tokens typically propagate context:

| Claim | Description |
|---|---|
| `sub` | Subject identifier |
| `email` | User email |
| `role` | Assigned RBAC role |
| `tenant_id` | Tenant ownership context |

This allows downstream services to authorize requests without shared state.

---

##  Authorization Model

Authorization decisions rely on:

- Role → what the user can do
- Tenant → where the user can operate

This supports clean separation within a shared platform.
