from app import db, models
import datetime
import bcrypt

#empty the database
company = models.Company.query.all()
for c in company:
     db.session.delete(c)
department = models.Department.query.all()
for d in department:
     db.session.delete(d)
document = models.Document.query.all()
for doc in document:
     db.session.delete(doc)
users = models.User.query.all()
for u in users:
     db.session.delete(u)
db.session.commit()



#populate the database

# 2 companies
c = models.Company(name='companya', about='abc')
db.session.add(c)
db.session.commit()

c = models.Company(name='companyb', about='xyz')
db.session.add(c)
db.session.commit()

# 3 departments
d = models.Department(name='depa', about='abc')
db.session.add(d)
db.session.commit()

d = models.Department(name='depb', about='fgh')
db.session.add(d)
db.session.commit()

d = models.Department(name='depc', about='xyz')
db.session.add(d)
db.session.commit()


# 4 users

u = models.User(username='john', password=bcrypt.hashpw('123', bcrypt.gensalt()),department='1',company='1') 
db.session.add(u)
db.session.commit()

u = models.User(username='susan', password=bcrypt.hashpw('456', bcrypt.gensalt()),department='2',company='1')
db.session.add(u)
db.session.commit()

u = models.User(username='manju', password=bcrypt.hashpw('jain', bcrypt.gensalt()),department='3',company='2')
db.session.add(u)
db.session.commit()

u = models.User(username='amnu', password=bcrypt.hashpw('noob', bcrypt.gensalt()),department='1',company='2') 
db.session.add(u)
db.session.commit()

# 4 documents

doc = models.Document(title='A',description='abc',keywords='akey',body='bodya',uploader_id='1',department='1',company='1',_global=True)
db.session.add(doc)
db.session.commit()

doc = models.Document(title='B',description='bcd',keywords='bkey',body='bodyb',uploader_id='3',department='2',company='1')
db.session.add(doc)
db.session.commit()

doc = models.Document(title='C',description='cde',keywords='ckey',body='bodyc',uploader_id='3',department='3',company='2',_public=True)
db.session.add(doc)
db.session.commit()

doc = models.Document(title='D',description='def',keywords='dkey',body='bodyd',uploader_id='4',department='1',company='2')
db.session.add(doc)
db.session.commit()


#sample queries
company = models.Company.query.all()
print company
department = models.Department.query.all()
print department
document = models.Document.query.all()
print document
users = models.User.query.all()
print users



#empty the database
# company = models.Company.query.all()
# for c in company:
#      db.session.delete(c)
# department = models.Department.query.all()
# for d in deparmtent:
#      db.session.delete(d)
# document = models.Document.query.all()
# for doc in document:
#      db.session.delete(doc)
# users = models.User.query.all()
# for u in users:
#      db.session.delete(u)
# db.session.commit()