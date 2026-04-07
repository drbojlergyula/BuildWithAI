# Project Spec

This document defines **what** you are building and **why**. It covers product requirements and engineering decisions.
For the technical breakdown of how it is built (file structure, data flow, components), see [Architecture](docs/architecture.md).

---

# Part 1: Product Requirements

<!-- Describe your product clearly enough that someone unfamiliar with it would understand what it does, who it's for, and why it exists. Be specific — vague requirements lead to the wrong product being built. -->

## What Is This Product?

<!-- One paragraph. What does it do, and what problem does it solve?
     Example: -->

A small business owner needs a simple way to collect customer orders via a web form and see them in one place. This tool provides a public order form and a private dashboard where the owner can view, filter, and mark orders as handled — without needing a spreadsheet or a complicated system.

## Who Is It For?

<!-- Who are your users? What do they want to do?
     Example: -->

- **Customers** — people who want to place an order quickly without creating an account
- **The business owner** — needs to see incoming orders at a glance and mark them as done

## Features & User Stories

<!-- List the key features. Write each one as: "A [user] can [do something] so that [goal]."
     Be specific. Bad: "Users can submit orders."
     Good: "A customer can fill in their name, contact details, and order description and submit it in under a minute, so they don't need to call or email." -->

### Order Form
- A customer can fill in their name, contact details, and order description and submit the form, so the business owner receives the request immediately.
- A customer sees a confirmation message after submitting, so they know it was received.

### Owner Dashboard
- The owner can see all incoming orders in a list sorted by date, so nothing gets missed.
- The owner can mark an order as handled, so the list stays manageable.
- The owner can filter orders by status (new / handled), so they can focus on what needs attention.

### General
- The form works on mobile and desktop.
- The owner logs in with a password to access the dashboard.

---

# Part 2: Engineering Requirements

<!-- This section captures the technical decisions for your project. If you are not sure, leave a section blank and ask Claude to help you decide. -->

## Tech Stack

<!-- Replace with your chosen technologies.
     Example: -->

| Layer | Technology | Notes |
|---|---|---|
| Frontend | HTML, CSS, JavaScript | Simple and fast — no framework needed |
| Backend | Node.js + Express | Handles form submissions and serves the dashboard |
| Database | SQLite | Lightweight, no separate server needed for small scale |
| Auth | HTTP Basic Auth or simple session | Password-protect the owner dashboard |
| Hosting | Railway or Render | Free tier supports small Node.js apps |

## System Design Preferences

<!-- Decisions that keep the codebase consistent. Agree on these upfront.
     Example: -->

- **API style:** REST — simple POST and GET endpoints, no GraphQL needed
- **File structure:** Layer-based (`/public`, `/routes`, `/views`) — straightforward for a small app
- **Naming convention:** kebab-case for files, camelCase for JavaScript variables

## API Design

<!-- Document any backend endpoints your project needs.
     Only include this section if your project has a backend API. Delete it if not.
     Example: -->

### POST /api/orders

Receives a new order submission from the public form.

**Request:**
```json
{
  "name": "string",
  "email": "string",
  "phone": "string (optional)",
  "details": "string"
}
```

**Response (success):**
```json
{
  "success": true,
  "message": "Your order was received. We will be in touch shortly."
}
```

**Response (error):**
```json
{
  "success": false,
  "error": "VALIDATION_ERROR | SERVER_ERROR",
  "message": "Human-readable error message"
}
```

## Project Structure

<!-- Show the folder and file layout. See [Architecture](docs/architecture.md) for a detailed description of each file's role.
     Example: -->

```
my-project/
├── public/
│   ├── index.html          # Public order form
│   └── css/styles.css      # Shared styles
├── views/
│   └── dashboard.html      # Owner dashboard (password protected)
├── routes/
│   ├── orders.js           # POST /api/orders — receive submissions
│   └── dashboard.js        # GET /dashboard — serve owner view
├── data/
│   └── orders.db           # SQLite database file
├── server.js               # App entry point
└── .env.example            # Required environment variables
```
