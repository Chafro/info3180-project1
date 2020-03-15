from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, TextAreaField
from wtforms.validators import DataRequired,InputRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])

class UserForm(FlaskForm):
	firstname = StringField('Firstname', validators=[InputRequired()])
	lastname = StringField('Lastname', validators=[InputRequired()])
	email = StringField('Email', validators=[InputRequired()])
	location = StringField('Location', validators=[InputRequired()])
	gender = SelectField('Gender', choices=[('Male','Male'), ('Female','Female')])
	bio = TextAreaField('Biograpghy')
	file = FileField('Photo', validators=[FileRequired(),FileAllowed(['jpg', 'png', 'jpeg'])])