import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or "\xb6\x8d\x05`\xce\xc0Y\xef\xdf\xfd\xc9}\xe8\xbf\xbeO\x98\xd2\xf0\xb5:M\xe9,m\x9e\xa2;^\x13S\xd7"
	
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///'+os.path.join(basedir, 'app.db')
	SQLALCHEMY_TRACK_MODIFICATIONS= False

	MAIL_SERVER = os.environ.get('MAIL_SERVER')
	MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
	MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
	MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
	MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
	ADMINS = ['dhanutester93@gmail.com']

	POSTS_PER_PAGE = 25