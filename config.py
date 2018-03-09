import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or "\xb6\x8d\x05`\xce\xc0Y\xef\xdf\xfd\xc9}\xe8\xbf\xbeO\x98\xd2\xf0\xb5:M\xe9,m\x9e\xa2;^\x13S\xd7"
	
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///'+os.path.join(basedir, 'app.db')
	SQLALCHEMY_TRACK_MODIFICATIONS= False