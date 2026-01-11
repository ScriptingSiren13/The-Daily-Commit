# Identity Service Architecture — Multi-Tenant Context

##  Overview
An identity service in a multi-tenant system enables secure onboarding, authentication, and authorization of users across tenant boundaries. Its primary role is to establish identity and propagate role and tenant information through token-based communication.

---

##  Core Components

### **1. Password Hashing**
Ensures credentials are stored securely and prevents storing raw passwords.

### **2. OAuth2 Bearer Tokens**
Defines how tokens are transmitted from client to server via headers.

### **3. JWT Token Issuance**
Encodes claims such as:
- `email`
- `role`
- `tenant_id`
- `sub`

### **4. Input Validation Schemas**
Used to validate payloads for:
- tenant creation
- user provisioning
- login

### **5. RBAC (Role-Based Access Control)**
Maps which actions are allowed for:
- admins
- managers
- employees
- system accounts

### **6. Tenant Boundary Logic**
Prevents cross-tenant data leakage and enforces isolation.

---

##  Essential Endpoints

| Endpoint | Purpose |
|---|---|
| `POST /tenant` | Creates a new tenant |
| `POST /tenant/bootstrap-admin` | Creates first admin for a tenant |
| `POST /register` | Registers additional users under the tenant |
| `POST /login` | Authenticates and returns JWT tokens |
| `GET /me` | Returns current identity extracted from token |

---

##  User Onboarding Sequence

Correct order of operations:

**Tenant → Bootstrap Admin → Register Users → Login**


This ensures administrators can perform provisioning without elevated platform-wide privileges.

---

##  Multi-Tenant Constraints

A multi-tenant identity service must ensure:

- **Tenant isolation**
- **Scoped permissions**
- **Scoped user storage**
- **Consistent token claims**
- **Enforcement via RBAC**

These form the foundation for secure and scalable tenant-aware systems.
