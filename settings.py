import os


SECRET_KEY = 'NOTHING FOR NOW'
DEBUG = True
DB_USERNAME = 'root'
DB_PASSWORD = '1234'
BLOG_DB_NAME = 'blog'
DB_HOST = 'sabbib-MS-7693'
# DB_URI = 'jdbc:mysql://localhost:3306'
# DB_URI = os.environ.get('DEV_DATABASE_URL')
DB_URI = 'mysql+pymysql://%s:%s@%s/%s' % (DB_USERNAME, DB_PASSWORD, DB_HOST, BLOG_DB_NAME)
# DB_URI = 'mysql+pymysql://root@localhost:1234@localhost/blog'

print(DB_URI)

SQLALCHEMY_DB_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True
