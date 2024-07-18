from app import db


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80), nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	preferences = db.Column(db.Text, nullable=True)

	def __repr__(self):
		return f'<User {self.name}>'
