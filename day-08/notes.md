# Day 08 — Understanding Frontend RBAC Flow

Today I spent time understanding how RBAC (Role-Based Access Control)
functions on the frontend side of a web application. I did not write code
for this yet, but focused on how the flow works conceptually.

---

## What I Learned

RBAC on the frontend is not about enforcing security (that happens on the backend),
but about controlling the user interface and available actions based on roles
and permissions. The goal is to avoid exposing UI elements or actions that
the user cannot perform.

---

## Frontend RBAC Flow (High-Level)

The typical RBAC flow I studied works as follows:

1. **Authentication**
   - User logs in and receives an identity token (usually JWT)

2. **Role / Permission Fetching**
   - After login, the frontend retrieves the user's assigned roles
     and/or permissions from an API endpoint

3. **State Storage**
   - The roles/permissions are stored in client state
   - e.g., React context, Redux store, or memory cache

4. **UI Rendering**
   - Components check roles/permissions before rendering UI elements
   - Examples: hiding buttons, disabling actions, or redirecting routes

5. **Route Protection**
   - Certain routes are only accessible if the user has required roles
   - Otherwise, the user is redirected or shown an error page

6. **API Calls**
   - Frontend still sends requests, but backend ultimately enforces RBAC

---

## Important Insight

Frontend RBAC is mainly about:
- **UX correctness**
- **Consistency**
- **Reducing confusion**

but it is **not a security boundary**. The backend still performs
authorization enforcement.

---

## Current Status

I did not dive into the exact frontend implementation or code yet,
but now have a mental model of how the RBAC flow works end-to-end.

