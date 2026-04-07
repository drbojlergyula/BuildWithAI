# Architecture

This document describes the high-level system architecture, data flow, and component relationships.
For what is being built and why, see [Project Spec](docs/project_spec.md).

## System Overview

<!-- One paragraph describing the overall structure: what type of app it is, what the main layers are, and how they connect.
     Example: -->

This is a web application with a static frontend and a lightweight Node.js backend. The public-facing order form is served as a plain HTML file. The backend handles form submissions, stores orders in a local database, and serves a password-protected owner dashboard.

## Data Flow

<!-- Describe how data moves through the system from the user's action to the result.
     Example: -->

```
User fills in the form and clicks Submit
      ↓
JavaScript validates the input on the frontend
      ↓
POST /api/orders { name, email, details }
      ↓
Server validates and saves the order to the database
      ↓
Success response returned
      ↓
Confirmation message shown to the user
```

## Component Architecture

<!-- List the key files and folders, grouped by layer. Describe what each one does.
     Only include layers that exist in your project. Delete sections that don't apply.
     Example: -->

### Frontend Pages

- `public/index.html` — Public order form
- `views/dashboard.html` — Owner dashboard showing all orders

### Backend Routes

- `routes/orders.js` — Receives new order submissions, validates input, writes to database
- `routes/dashboard.js` — Serves the dashboard view, enforces login

### Data

- `data/orders.db` — SQLite database; one table: `orders` (id, name, email, phone, details, status, created_at)

### Configuration

- `server.js` — Express app setup, middleware, route registration
- `.env.example` — Documents required environment variables (admin password, port)

### API Layer

<!-- List backend endpoints if your project has a server. Delete this section if it's a static site with no backend.
     Example: -->

- `POST /api/orders` — Accepts a new order from the public form
- `GET /dashboard` — Returns the owner dashboard (requires auth)
- `POST /dashboard/orders/:id/handle` — Marks an order as handled
