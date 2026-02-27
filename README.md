# production-rag-platform

> Enterprise-grade RAG (Retrieval Augmented Generation) platform with multi-tenant support, pluggable retrievers, LangGraph-based agents, advanced evaluation, and production observability.

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/fastapi-0.104+-green.svg)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Vision

Build sophisticated AI assistants by combining:
- **Your Data**: Documents, APIs, databases with secure onboarding
- **Smart Retrieval**: Pluggable retrievers (FAISS, BM25, HyDE, GraphRAG, hybrid)
- **Agentic Workflows**: LangGraph-based agents with tools, planning, and reasoning
- **Quality Assurance**: RAG evaluation suite measuring coverage, hallucination, faithfulness
- **Production Ready**: Multi-tenancy, observability, cost tracking, audit logs

## Key Features

### 🏗️ Multi-Tenant Architecture
- Organization and user management with granular access control
- Isolated vector stores and knowledge bases per tenant
- Billing and usage tracking per org/workspace
- API key management and rotation

### 🔍 Pluggable Retrievers
- **Dense**: FAISS, Qdrant, Pinecone embeddings
- **Sparse**: BM25, TF-IDF for keyword matching
- **Smart**: HyDE (Hypothetical Document Embeddings)
- **Advanced**: GraphRAG for structured knowledge graphs
- **Hybrid**: Dense + sparse fusion with configurable weights

### 🤖 LangGraph-Based Agents
- Workflow engine with persistent state and retry logic
- Built-in agents: Researcher, Planner, Executor, Refiner
- Custom tool integration: web search, database queries, APIs
- Multi-turn conversation with memory management

### 📊 RAG Evaluation Suite
- **Metrics**: Coverage, hallucination rate, answer faithfulness, latency, cost
- **Datasets**: Create benchmark datasets per knowledge base
- **Runs**: Compare retriever/LLM combinations
- **Dashboards**: Real-time performance tracking

### 👁️ Production Observability
- Trace every request: retrieval, reasoning, LLM calls
- Cost breakdown per request (tokens × model pricing)
- Conversation replay and annotation
- Structured logging and error taxonomy

## Quick Start

### Prerequisites
- Python 3.9+
- PostgreSQL 14+
- Redis (optional, for caching)
- OpenAI API key or local LLM

### Local Development

```bash
# Clone and setup
git clone https://github.com/ramji3030/production-rag-platform
cd production-rag-platform

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows

# Install dependencies
pip install -r backend/requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your API keys and database URL

# Run migrations
cd backend
alembic upgrade head

# Start backend
uvicorn main:app --reload --port 8000

# In another terminal, start frontend
cd frontend
npm install
npm start  # runs on http://localhost:3000
```

### Docker Compose (Recommended)

```bash
docker-compose up -d
# Backend: http://localhost:8000
# Frontend: http://localhost:3000
# API docs: http://localhost:8000/docs
```

## Project Structure

```
production-rag-platform/
├── backend/                    # FastAPI application
│   ├── app/
│   │   ├── core/              # Config, security, auth
│   │   ├── models/            # SQLAlchemy ORM models
│   │   ├── api/               # API routes
│   │   ├── services/          # Business logic
│   │   │   ├── retriever.py   # Pluggable retrievers
│   │   │   ├── agent.py       # Agent orchestration
│   │   │   └── evaluator.py   # RAG evaluation
│   │   └── schemas/           # Pydantic schemas
│   ├── tests/
│   ├── migrations/            # Alembic migrations
│   ├── requirements.txt
│   └── main.py
├── frontend/                   # React + TypeScript
│   ├── src/
│   │   ├── components/        # Reusable components
│   │   ├── pages/             # Page components
│   │   ├── hooks/             # Custom React hooks
│   │   ├── services/          # API client
│   │   └── store/             # State management
│   └── package.json
├── sdk/                        # Python SDK
│   ├── production_rag/
│   │   ├── client.py          # Main client
│   │   ├── trace.py           # Tracing utilities
│   │   └── models.py          # Type hints
│   └── pyproject.toml
├── docker-compose.yml
├── Dockerfile.backend
└── Dockerfile.frontend
```

## API Overview

### Authentication
```bash
# Create API key
curl -X POST http://localhost:8000/api/v1/keys \
  -H "Authorization: Bearer <session-token>" \
  -d '{"name": "my-key"}'

# Use API key
curl http://localhost:8000/api/v1/data \
  -H "X-API-Key: <api-key>"
```

### Data Onboarding
```bash
# Upload documents
curl -X POST http://localhost:8000/api/v1/kb/upload \
  -F "file=@document.pdf" \
  -F "source=documentation" \
  -H "X-API-Key: <api-key>"

# Index data
curl -X POST http://localhost:8000/api/v1/kb/index \
  -H "Content-Type: application/json" \
  -d '{"kb_id": "kb-123", "retriever": "hybrid"}' \
  -H "X-API-Key: <api-key>"
```

### Query with Agent
```bash
curl -X POST http://localhost:8000/api/v1/query \
  -H "Content-Type: application/json" \
  -d '{
    "kb_id": "kb-123",
    "query": "What are the latest company policies?",
    "agent_type": "researcher",
    "tools": ["search", "summarize"]
  }' \
  -H "X-API-Key: <api-key>"
```

## Evaluation Workflow

1. **Create Benchmark Dataset**
   - Upload ground-truth Q&A pairs
   - Define expected retrieval sources

2. **Run Evaluation**
   - Test against multiple retrievers (FAISS, BM25, hybrid)
   - Compare different LLM models
   - Measure coverage, hallucination, faithfulness

3. **Analyze Results**
   - View metrics per retriever/LLM combo
   - Identify failure modes
   - Export reports

## Tech Stack

### Backend
- **Framework**: FastAPI 0.104+
- **ORM**: SQLAlchemy 2.0 with async support
- **VectorDB**: Qdrant (self-hosted) / Pinecone / Weaviate
- **Search**: elasticsearch or opensearch for BM25
- **Agents**: LangGraph + LangChain
- **LLM**: OpenAI API, local Ollama, Anthropic Claude
- **Task Queue**: Celery + Redis
- **Tracing**: OpenTelemetry, Datadog/Jaeger

### Frontend
- **Framework**: React 18 + TypeScript
- **UI**: Tailwind CSS + shadcn/ui
- **State**: TanStack Query + Zustand
- **Charting**: Recharts
- **Code Editor**: Monaco Editor

### Infrastructure
- **Containerization**: Docker + Docker Compose
- **DB**: PostgreSQL 14+ (Timescale for metrics)
- **Cache**: Redis
- **Auth**: JWT + OAuth2
- **Deployment**: Kubernetes-ready (Helm charts included)

## Configuration

See `.env.example` for all environment variables:

```bash
# LLM Configuration
OPENAI_API_KEY=sk-...
LLM_MODEL=gpt-4
LOCAL_LLM_URL=http://ollama:11434  # optional

# Vector Database
VECTOR_DB=qdrant
QDRANT_URL=http://qdrant:6333

# Search Engine  
SEARCH_ENGINE=elasticsearch
ELASTICSEARCH_URL=http://elasticsearch:9200

# Database
DATABASE_URL=postgresql://user:pass@localhost:5432/rag_db
REDIS_URL=redis://localhost:6379

# Multi-tenancy
MAX_ORGS_FREE_TIER=3
MAX_KB_PER_ORG=10
MAX_DOCS_PER_KB=1000

# Billing
BILLING_ENABLED=true
STRIPE_SECRET_KEY=sk-...
```

## Common Use Cases

### 1. Enterprise Documentation Assistant
- Onboard internal wikis, policies, runbooks
- Query with agents for multi-hop reasoning
- Track usage per department

### 2. Customer Support Automation  
- Index support tickets and KB articles
- Route queries to correct agent
- Log interactions for training

### 3. Research & Analysis
- Index academic papers or market data
- Complex queries spanning multiple documents
- Compare retriever quality on domain-specific questions

### 4. Code & Technical Documentation
- Index API docs, code repositories
- Answer architectural questions
- Generate code examples from docs

## Production Deployment

### AWS ECS + RDS
See `infra/aws/` for Terraform modules:
```bash
cd infra/aws
terraform init
terraform plan -var="env=production"
terraform apply
```

### Kubernetes
See `k8s/` for Helm charts:
```bash
helm repo add production-rag-platform https://charts.example.com
helm install rag production-rag-platform/rag-platform \
  --namespace production \
  -f values-prod.yaml
```

## Testing

```bash
# Unit tests
pytest backend/tests/unit

# Integration tests
pytest backend/tests/integration

# RAG evaluation tests
pytest backend/tests/evaluation

# Frontend tests
cd frontend && npm test
```

## Contributing

1. Fork and create feature branch: `git checkout -b feature/amazing-feature`
2. Make changes and test thoroughly
3. Commit with conventional commits: `git commit -m 'feat: add amazing feature'`
4. Push and open PR

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## Roadmap

- [ ] GraphRAG for knowledge graph construction
- [ ] Fine-tuned retriever models
- [ ] Multi-modal (images, tables, charts)
- [ ] Real-time streaming responses
- [ ] Advanced caching strategies
- [ ] Cost optimization recommendations
- [ ] A/B testing framework for agents
- [ ] Enterprise audit logging

## License

MIT License - see [LICENSE](LICENSE)

## Support

- 📚 [Documentation](https://docs.example.com)
- 💬 [Discord Community](https://discord.gg/example)
- 📧 support@example.com
- 🐛 [GitHub Issues](https://github.com/ramji3030/production-rag-platform/issues)
