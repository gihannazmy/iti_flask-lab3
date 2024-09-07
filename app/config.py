


class Config:
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://iti:123@localhost:5432/posts'

config_options = {
    "dev":DevelopmentConfig,
    "prod":ProductionConfig,
}