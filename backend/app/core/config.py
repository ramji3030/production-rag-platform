"""Application configuration settings."""

from typing import List
from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    """Application settings from environment variables."""

    # API Configuration
    API_V1_STR: str = "/api/v1"
    API_VERSION: str = "0.1.0"
    PROJECT_NAME: str = "Production RAG Platform"
    DESCRIPTION: str = "Enterprise-grade RAG platform with multi-tenant support"

    # Server Configuration
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    DEBUG: bool = False
    ENVIRONMENT: str = "development"  # development, staging, production
    LOG_LEVEL: str = "INFO"

    # CORS Configuration
    CORS_ORIGINS: List[str] = ["*"]
    CORS_ALLOW_CREDENTIALS: bool = True
    CORS_ALLOW_METHODS: List[str] = ["*"]
    CORS_ALLOW_HEADERS: List[str] = ["*"]

    # Database Configuration
    DATABASE_URL: str = "postgresql://user:password@localhost:5432/rag_platform"
    DATABASE_ECHO: bool = False
    DATABASE_POOL_SIZE: int = 20
    DATABASE_MAX_OVERFLOW: int = 10
    DATABASE_POOL_PRE_PING: bool = True

    # Redis Configuration
    REDIS_URL: str = "redis://localhost:6379/0"
    REDIS_CACHE_TTL: int = 3600  # 1 hour

    # LLM Configuration
    OPENAI_API_KEY: str = ""
    OPENAI_MODEL: str = "gpt-4-turbo-preview"
    LLM_TEMPERATURE: float = 0.7
    LLM_MAX_TOKENS: int = 2048

    # RAG Configuration
    VECTOR_STORE_TYPE: str = "faiss"  # faiss, pinecone, weaviate, chroma
    EMBEDDING_MODEL: str = "text-embedding-3-small"
    EMBEDDING_DIMENSION: int = 1536
    CHUNK_SIZE: int = 1024
    CHUNK_OVERLAP: int = 256

    # Security Configuration
    SECRET_KEY: str = "your-secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    # Multi-tenant Configuration
    MULTI_TENANT_ENABLED: bool = True
    TENANT_ISOLATION_LEVEL: str = "SCHEMA"  # DATABASE, SCHEMA, ROW

    # Monitoring Configuration
    SENTRY_DSN: str = ""
    ENABLE_PROMETHEUS_METRICS: bool = True

    # Feature Flags
    ENABLE_RAG: bool = True
    ENABLE_AGENTS: bool = True
    ENABLE_EVALUATION: bool = True
    ENABLE_STREAMING: bool = True

    class Config:
        """Pydantic config."""
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()


settings = get_settings()
