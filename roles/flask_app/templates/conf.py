SECRET_KEY = '{{ flask_app_secretKey }}'
FLASK_ADMIN_SWATCH = 'cerulean'
SQLALCHEMY_DATABASE_URI = 'postgres://app:{{ flask_app_dbPassword }}@db.lukepafford.com:5432/flask_app'
DEBUG_TB_INTERCEPT_REDIRECTS = False
