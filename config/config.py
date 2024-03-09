from config.constant import Constants

class Config:
    SQLALCHEMY_DATABASE_URI = f"postgresql://{Constants.DATABASE_USERNAME}:{Constants.DATABASE_PASSWORD}@localhost/{Constants.DATABASE_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False