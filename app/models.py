from app import db
from datetime import datetime 

class User(db.Model):
	__tablename__="users"
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), unique=True, index=True)
	email = db.Column(db.String(120), unique=True, index=True)
	password_hash=db.Column(db.String(128))
	posts = db.relationship('Post', backref='author', lazy='dynamic')

	def __repr__(self):
		return "<user : {}>.".format(self.username)

class Post(db.Model):
	__tablename__='posts'
	id=db.Column(db.Integer, primary_key=True)
	body=db.Column(db.String(140))
	timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

	def __repr__(self):
		return "<post {}>".format(self.body)