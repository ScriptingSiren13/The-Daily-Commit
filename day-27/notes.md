# Day 27 — Frontend Architecture + Login Flow

Today I studied the frontend `src` directory structure and understood how the authentication + role routing system works.

Key points:
• `frontend/src` holds all core UI logic
• `app/` implements routing + layouts
• `context/` manages shared auth state
• `components/` contains reusable UI widgets
• `lib/` contains API helpers and utilities

Login page flow:
1. User enters email + password
2. Sends POST /auth/login to backend
3. Token stored client-side (localStorage)
4. Calls /auth/me to fetch user role
5. Redirects user based on role:
   - Admin → /app/admin/overview
   - Manager → /app/manager/overview
   - Employee → /app/employee/overview
6. Handles invalid login + loading states

This login page acts as the entry to the entire app’s dashboards.
