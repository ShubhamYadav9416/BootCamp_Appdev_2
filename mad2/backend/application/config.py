SECRET_KEY = '1234'
SQLALCHEMY_DATABASE_URI = "sqlite:///../db_directory/flaskgrocery.db"
SQLALCHEMY_TRACK_MODIFICATIONS = False



CACHE_TYPE = 'RedisCache'
CACHE_REDIS_URL = "redis://localhost:6379/0"
CACHE_DEFAULT_TIMEOUT = 300

