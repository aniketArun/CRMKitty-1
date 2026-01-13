from typing import Any, Optional

class Settings():
    APP_NAME:str = "CRMKitty Backend"
    APP_VERSION:str = "V.0.0.1"
    SQLALCHEMY_DATABASE_URL:str = "sqlite:///./test.db"
    APP_DESCRIPTION:str = '''
                            This is CRMKitty API backend, Running with FastAPIs and uvicorn, Sqlite
                            '''
    class Config:
        env_file:str = ".env"

    SET_MAIN_OPTION:str = "sqlalchemy.url"
settings = Settings()
