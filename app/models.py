"""Database models for the rec-sys application."""

import datetime

from app import db

class User(db.Model):
    """user capable of viewing 

    :param str username: username of user
    :param str password: encrypted password for the user

    """
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)
    authenticated = db.Column(db.Boolean, default=False)
    #documents = db.relationship('document', backref='uploaded', lazy='dynamic')
    department = db.Column(db.String, db.ForeignKey('department.id'))
    company = db.Column(db.String, db.ForeignKey('company.id'))
        
    def __repr__(self):
        return '<User %r>' % self.username

    def is_active(self):
         """True, as all users are active."""
         return True

    def get_id(self):
         """Return the username to satify Flask-Login's requirements."""
         try:
            return unicode(self.id)  # python 2
         except NameError:
            return str(self.id)  # python 3

    def is_authenticated(self):
         """Return True if the user is authenticated."""
         return self.authenticated

    def is_anonymous(self):
         """False, as anonymous users aren't supported."""
         return False

    
class Document(db.Model):
    """
    documents uploaded to the database 

    """
    __tablename__ = 'document'

    id = db.Column(db.Integer, primary_key = True)
    timestamp = db.Column(db.DateTime)
    title = db.Column(db.String)
    description = db.Column(db.String)
    keywords = db.Column(db.String)
    body = db.Column(db.String) #to be replaced with real doc
    uploader_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    department = db.Column(db.String, db.ForeignKey('department.id'))
    company = db.Column(db.String, db.ForeignKey('company.id'))
    _global = db.Column(db.Boolean, default=False) #true for local
    _public = db.Column(db.Boolean, default=False) #true for private
    
    
    def __repr__(self):
        return '<Document %r>' % (self.title)


class Department(db.Model):
    """departments for users 

    :param str name: name of the department
    :param str about: deatils of the department

    """
    __tablename__ = 'department'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    about = db.Column(db.String)

    def __repr__(self):
        return '<Department %r>' % (self.name)

class Company(db.Model):
    """company for users 

    :param str name: name of the company
    :param str about: deatils of the company

    """
    __tablename__ = 'company'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    about = db.Column(db.String)

    def __repr__(self):
        return '<Company %r>' % (self.name)

