# MCP-OKTA-PROXY

## Overview

**MCP-OKTA-PROXY** is an API layer that acts as a Model Context Proxy (MCP) for [Okta](https://okta.com/).  
It exposes a simple, secure set of endpoints for downstream apps to consume user profile information and user schema, abstracting away Okta’s native API structure, and lets you filter, map, or enrich identity data as needed.

- **Hides Okta-specific complexity**
- **Exposes only user profile attributes**
- **Easily customizable for per-tenant or per-use-case contexts**
- **Centralizes identity filtering, masking, and enforcement**

---

## Features

- **REST API** with endpoints for:
  - Listing all user profiles (`/users`)
  - Fetching a single user profile (`/users/{user_id}`)
  - Describing the user profile schema (`/model-context/describe?resource=User`)
- **Flexible data shaping:** Return only the `profile` portion of Okta users, hiding technical and sensitive fields
- **Built on FastAPI** (Python) for fast, interactive docs and easy extension
- **Central point to add auth, masking, enrichment, or custom logic**

---

## Quick Start

### Prerequisites

- Python 3.8+
- Okta Account & API Token ([How to create an Okta token](https://developer.okta.com/docs/guides/create-an-api-token/overview/))

### Installation

1. **Clone the repository**
   git clone https://github.com/YOUR-ORG/MCP-OKTA-PROXY.git
   cd MCP-OKTA-PROXY
2. **Install dependecies**
    pip install -r requirements.txt

3. **Configure environment variables**
    OKTA_ORG_URL=https://your-domain.okta.com
    OKTA_API_TOKEN=your-okta-api-token
4. **Run the API server**
   uvicorn main:app --reload


GET http://localhost:8000/users
GET http://localhost:8000/users/{user_id}
GET http://localhost:8000/model-context/describe?resource=User
