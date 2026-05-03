# Advanced OOP E-Commerce CLI System

## Overview

This project is a **CLI-based e-commerce management system** built in Python to explore **advanced object-oriented design patterns and backend architectural principles** beyond basic CRUD applications.

The system supports:

* Authentication and user management
* Product management
* Order and order-item handling
* Extensible pricing/discount strategies

The primary goal was not just feature implementation, but designing the application using **production-oriented backend architecture patterns** commonly used in scalable systems.

**Why this architecture:**

* Separate business logic from data access using the **Service + Repository pattern**
* Use interfaces and abstractions to reduce coupling
* Encapsulate business rules using strategy-based design
* Improve maintainability and extensibility through modular OOP design

This project focuses on  **system design discipline inside a small application** , which is often where junior projects fail.

---

# Architecture

```text
CLI (main.py)
      │
      ▼
 Services Layer
      │
      ▼
Repositories Layer
      │
      ▼
Entities / Models
```

## Architectural Decisions

### Service Layer

Business rules are isolated inside services instead of being embedded in CLI logic.

Example:

* Authentication validation
* Order creation rules
* Product stock checks

**Why:**
Keeps orchestration logic centralized and reusable.

---

### Repository Layer

Repositories abstract data access operations from business logic.

Example:

* `ProductRepository`
* `OrderRepository`

**Why:**
Allows future replacement of storage implementation without changing services.

Current implementation uses in-memory structures, but the architecture supports migration to:

* PostgreSQL
* MySQL
* Redis
* External APIs

---

### Strategy Pattern

Discount calculation logic is isolated into interchangeable strategies.

Example:

* `VIPDiscountStrategy`

**Why:**
Avoids deeply nested conditional logic and enables runtime behavior extension.

---

### Interfaces / Abstractions

Interfaces define contracts for repositories and services.

**Why:**
Promotes loose coupling and improves testability.

---

## Scalability & Trade-offs

### Current Design Strengths

* Highly modular
* Easy to extend
* Clear separation of concerns
* Test-friendly architecture

### Trade-offs

* More abstraction increases complexity for small projects
* Additional layers introduce more files/classes
* Slightly slower development initially, but improves long-term maintainability

---

# ⚙️ Tech Stack

## Backend

* Python 3.12
* Abstract Base Classes (ABC)

## Architecture & Design

* Repository Pattern
* Service Layer Pattern
* Strategy Pattern
* Dependency Injection
* Interface-based Design

---

# 📦 Services / Components

## Entities

Represents core business objects:

* User
* Product
* Order
* OrderItem

Uses Python `dataclasses` for lightweight domain modeling.

---

## Repositories

Responsible for data persistence abstraction.

Examples:

* Create product
* Fetch order
* Update stock

Repositories isolate storage logic from business rules.

---

## Services

Contains orchestration and business logic.

Responsibilities:

* Authentication handling
* Product management
* Order processing
* Validation logic

---

## Strategies

Encapsulates replaceable business behaviors.

Example:

* VIP discount logic

Enables adding:

* Seasonal discounts
* Coupon-based pricing
* Membership tiers

without modifying existing order logic.

---

## Exceptions

Custom exceptions improve domain-level error handling.

Example:

* Product not found
* Invalid order
* Authentication failure

**Why:**
Production systems require meaningful error boundaries instead of generic runtime failures.

---

# 🔄 Request Flow

```text
CLI Input
   ↓
Service Layer
   ↓
Validation / Business Rules
   ↓
Repository Layer
   ↓
Entity Operations
   ↓
Response to User
```

Example order flow:

1. User authenticates
2. Product is fetched from repository
3. Stock validation occurs
4. Discount strategy is applied
5. Order is created
6. Stock is updated

---

# 🛠️ Setup & Installation

## Clone Repository

```bash
git clone https://github.com/Swapno963/E-Commerce-Order-Processing-System.git
cd E-Commerce-Order-Processing-System
```

## Run Application

```bash
python main.py
```

---

# 🧪 Advanced OOP Concepts Demonstrated

## Repository Pattern

Decouples storage from business logic.

---

## Service Layer

Centralizes business orchestration.

---

## Strategy Pattern

Supports interchangeable pricing logic.

---

## Dependency Injection

Services depend on abstractions instead of concrete implementations.

---

## Interface-based Design

Improves extensibility and testability.

---

## Custom Exceptions

Provides domain-aware error handling.

---

## Dataclasses

Reduces boilerplate while modeling entities cleanly.

---

# Authentication

Current authentication is simplified for CLI usage.

Production improvements:

* JWT authentication
* Password hashing
* RBAC

---

## Validation

Business validation exists at service layer.

Production systems should additionally include:

* Input sanitization
* Request schema validation
* Audit logging

---

## Observability

CLI applications lack centralized observability.

Future production adaptation could include:

* Structured logging
* Metrics
* Distributed tracing

---

## Understanding Real OOP Design

The project demonstrated that:

* OOP is not about classes alone
* Good architecture is about:
  * separation of concerns
  * replaceability
  * maintainability
  * extensibility

---

## Strategy Pattern Learnings

Initially, discount logic was implemented using conditional statements.

This became difficult to scale.

Refactoring to strategy-based design improved:

* readability
* extensibility
* testing

---

# Future Improvements

* Replace in-memory repositories with PostgreSQL
* Add unit and integration tests
* Introduce async order processing
* Add event-driven architecture
* Implement JWT authentication
* Add REST API layer using FastAPI
* Containerize application using Docker

---

# Project Structure

```text
project/
│
├── entities/       # Domain models
├── repositories/   # Data access layer
├── services/       # Business logic
├── strategies/     # Replaceable business rules
├── interfaces/     # Contracts / abstractions
├── exceptions/     # Domain exceptions
└── main.py         # CLI entry point
```

---

# 💡 Key Takeaway

This project focuses on  **backend engineering discipline** , not just functionality.

It demonstrates:

* clean architecture thinking
* modular system design
* maintainable OOP practices
* extensible business logic design

The system intentionally mirrors architectural patterns used in production backend services, even within a CLI-based environment.
