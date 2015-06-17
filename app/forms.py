"""Forms for the rec-sys application."""
from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, SubmitField
from wtforms.validators import DataRequired

 
class LoginForm(Form):
  """Form class for user login."""
  username = TextField("Username", validators=[DataRequired("Please enter your Username")])   
  password = PasswordField("Password", validators=[DataRequired("Please enter your Password")])
  submit = SubmitField("Send")

class SearchForm(Form):
  """Form class for database searching."""
  searchterm = TextField("Search Term", validators=[DataRequired("Please enter Search Term")])
  submit = SubmitField("Search")
