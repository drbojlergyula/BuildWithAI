# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

<!-- Add a new dated section each time you make significant changes.
     Use ### Added, ### Changed, ### Fixed, ### Removed as needed.
     Example entry below — delete it when you add your first real entry. -->

---

## YYYY-MM-DD *(replace with today's date)*

### Added
- **Order form** — Public form collecting name, email, and order details
- **Owner dashboard** — Password-protected view listing all submitted orders
- **Mark as handled** — Button on each order to update its status

### Changed
- Layout updated to work correctly on mobile screens below 400px

### Fixed
- Form submission not showing confirmation message in Safari — resolved by replacing `fetch` response handling
