import os
basedir = os.path.abspath(os.path.dirname(__file__))


#class Config(object):
     #SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
     #SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
     #SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
    #SQLALCHEMY_TRACK_MODIFICATIONS = False
DIALECT = "mysql"
DRIVER = "mysqldb"
USERNAME = "root"
PASSWD = "yangxp"
HOST = "127.0.0.1"
PORT = "3306"
DATABSE = "my_blog"



SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT,DRIVER,USERNAME,PASSWD,HOST,PORT,DATABSE)
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')