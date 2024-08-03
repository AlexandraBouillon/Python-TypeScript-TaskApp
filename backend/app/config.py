python
import os

class Settings:
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")

settings = Settings()