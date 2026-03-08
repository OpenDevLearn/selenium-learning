# Selenium WebDriver Training — 5‑Day Program

A comprehensive 5-day hands-on training program for learning Selenium WebDriver with Python.

## Prerequisites

- Python 3.12 (Conda environment)
- Google Chrome browser
- Docker & Docker Compose

> **Note:** ChromeDriver is managed automatically — Selenium 4.6+ includes a built-in **Selenium Manager** that detects your installed Chrome version and downloads the matching ChromeDriver. No manual installation or version matching is needed. If you update Chrome, the correct driver is fetched automatically on the next run.

## Quick Start

### 1. Install Python dependencies

```bash
cd selenium
pip install -r requirements.txt
```

### 2. Start the Practice Application

From the workspace root:

```bash
docker compose up -d --build
```

This starts:

| Service | URL | Credentials |
|---------|-----|-------------|
| Practice App | http://localhost:5000 | `testuser` / `password123` |
| pgAdmin | http://localhost:5050 | `admin@admin.com` / `admin123` |
| PostgreSQL | localhost:5432 | `admin` / `admin123` |

### 3. Verify Setup

```bash
python Day01_Introduction/Session/01_first_script.py
```

### Docker Lifecycle

```bash
# Check running containers
docker ps

# Stop services
docker compose down

# Stop services and remove volumes
docker compose down -v
```

### DB Connection

- **Connection string:** `postgresql://admin:admin123@localhost:5432/db_learning`
- From pgAdmin, use the service name `postgres_db` as the host (since both run inside Docker).

#### Connect from command line

```bash
docker exec -it postgres_db /bin/bash
psql -U admin -d db_learning
```

#### Useful psql meta-commands

```
\l             -- list all databases
\c mydb        -- connect to a database
\dt            -- list tables in current database
\d tablename   -- describe table (schema, columns, constraints)
\dn            -- list schemas
\q             -- quit psql
```

## Course Structure

| Day | Topic | Folder |
|-----|-------|--------|
| 1 | Introduction, Setup, Browser Basics | `Day01_Introduction/` |
| 2 | Locators, Elements, CSS & XPath | `Day02_WebElements/` |
| 3 | Actions, Alerts, Tables, Frames, Windows | `Day03_ActionsAssertions/` |
| 4 | Waits, Screenshots, File Upload, JavaScript | `Day04_WaitingStrategies/` |
| 5 | Page Object Model, Mini Project, Test Suite | `Day05_MiniProject/` |

Each day's folder contains:
- **Session/** — Programs taught in class
- **Homework/** — Practice exercises (hands-on, fill-in-the-blank, challenges)
- **README.md** — Topics covered and homework descriptions

## Practice Application Features

The Docker-based test application includes:

- **Login / Register** — Authentication flows
- **Products & Cart** — E-commerce workflow (browse, search, filter, add to cart, checkout)
- **Practice Forms** — Every form element type (text, radio, checkbox, select, date, range, color, textarea)
- **Data Tables** — Sortable employee table with search and modals
- **Dynamic Content** — AJAX loading, countdown timer, toggle elements, live search
- **Interactions** — Alerts, hover, drag & drop, double click, right click, keyboard events
- **iFrames** — Embedded and nested iframes
- **File Upload** — File upload form
- **Multiple Windows** — New tab / popup window handling
