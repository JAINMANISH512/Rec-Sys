# all the imports
from flask import g
from flask.ext.login import  current_user
from app import app, db, lm, models
from .models import User,Document,Department,Company


def search(searchterm):
	document = models.Document.query.all()
	result = []
	for doc in document:
		if searchterm in doc.keywords:
			result.append(doc)

	return result