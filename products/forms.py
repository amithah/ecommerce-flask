from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileRequired, FileAllowed
from wtforms import StringField, FloatField,SelectField,PasswordField,SubmitField,BooleanField,FileField,IntegerField, TextAreaField, DateField
from models import User
from wtforms.validators import InputRequired, Email, Length, DataRequired


#-------------------------------------------------------------------------------
class RegisterForm(FlaskForm):
    email = StringField('email',validators=[InputRequired(), Length(min=5, max=80)])
    username = StringField('username', validators=[InputRequired(), Length(min=5, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=5, max=80)])
    admin =BooleanField("Admin?",default=True)
    remember_me =BooleanField("Remember me?",default=True)
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=5, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=5, max=80)])
    remember_me = BooleanField('Keep me logged in',default=True)
    submit = SubmitField('Login')
#---------------------------------------------------------------------------------
class BrandForm(FlaskForm):
    name = StringField('name', validators=[InputRequired(), Length(min=5, max=15)])
    submit = SubmitField('Add brand')
class CategoryForm(FlaskForm):
    name = StringField('name', validators=[InputRequired(), Length(min=5, max=15)])
    submit = SubmitField('Add category')

#products

class AddProductForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    price = FloatField('Price', validators=[DataRequired()])
    discount = IntegerField('Discount', default=0)
    stock = IntegerField('Stock', validators=[DataRequired()])
    colors = StringField('Colors', validators= [DataRequired()])
    discription = TextAreaField('Discription',validators= [DataRequired()])

    image_1 = FileField('Image 1', validators=[FileRequired(), FileAllowed(['jpg','png','gif','jpeg'], 'Images only please')])
    image_2 = FileField('Image 2', validators=[FileRequired(), FileAllowed(['jpg','png','gif','jpeg'], 'Images only please')])
    image_3 = FileField('Image 3', validators=[FileRequired(), FileAllowed(['jpg','png','gif','jpeg'], 'Images only please')])

