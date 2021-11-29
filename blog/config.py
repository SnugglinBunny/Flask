from decouple import config


class Config:
    SQLALCHEMY_DATABASE_URI = config("DB_URI")
    SECRET_KEY = config("SECRET_KEY")
    MAIL_SERVER = "smtp.googlemail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = config("EMAIL_USER")
    MAIL_PASSWORD = config("EMAIL_PASS")
