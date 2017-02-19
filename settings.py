import os


SECRET_KEY = 'NOTHING FOR NOW'
DEBUG = True
DB_USERNAME = 'root'
DB_PASSWORD = '1234'
BLOG_DB_NAME = 'blog2'
DB_HOST = os.getenv('IP', '127.0.0.1')
DB_URI = 'mysql+pymysql://root@127.0.0.1:blog'
# DB_URI = 'mysql+pymysql://%s:%s@%s/%s' % (DB_USERNAME, DB_PASSWORD, DB_HOST, BLOG_DB_NAME)

SQLALCHEMY_DB_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True
