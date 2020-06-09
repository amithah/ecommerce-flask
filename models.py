import re
from datetime import datetime
from app import db

from app import login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(int(user_id))

def slugify(s):
    return re.sub('[^\w]+', '-', s).lower() #url generating function


#---------------------------------------------------------------------------   
# define User model
class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    email = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(255))
    slug = db.Column(db.String(64), unique=True)

    admin = db.Column(db.Boolean, default=False)
    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs) # Call parent constructor.
        self.generate_slug()
    def generate_slug(self):
        self.slug = ''
        if self.username:
            self.slug = slugify(self.username)
            
    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False
    def is_admin(self):
        return self.admin
#----------------------------------------------------------------------------
class Brand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    slug = db.Column(db.String(64), unique=True)
    def generate_slug(self):
        self.slug = ''
        if self.name:
            self.slug = slugify(self.name)

    def __init__(self, *args, **kwargs):
        super(Brand, self).__init__(*args, **kwargs)
        self.slug = slugify(self.name)
    def __repr__(self):
        return '<Brand %r>' % self.name
#--------------------------------------------------------------------------------
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    slug = db.Column(db.String(64), unique=True)
    def generate_slug(self):
        self.slug = ''
        if self.name:
            self.slug = slugify(self.name)

    def __init__(self, *args, **kwargs):
        super(Category, self).__init__(*args, **kwargs)
        self.slug = slugify(self.name)
    def __repr__(self):
        return '<Catgory %r>' % self.name
#--------------------------------------------------------------
class AddProduct(db.Model):
    __seachbale__ = ['name','desc']
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Numeric(10,2), nullable=False)
    discount = db.Column(db.Integer, default=0)
    stock = db.Column(db.Integer, nullable=False)
    colors = db.Column(db.Text, nullable=False)
    desc = db.Column(db.Text, nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)
    slug = db.Column(db.String(64), unique=True)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'),nullable=False)
    category = db.relationship('Category',backref=db.backref('categories', lazy=True))

    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'),nullable=False)
    brand = db.relationship('Brand',backref=db.backref('brands', lazy=True))

    image_1 = db.Column(db.String(150), nullable=False, default='image1.jpg')
    filename_1= db.Column(db.String(80),default='image1.jpg')
    image_2 = db.Column(db.String(150), nullable=False, default='image2.jpg')
    filename_2= db.Column(db.String(80), default='image2.jpg')
    image_3 = db.Column(db.String(150), nullable=False, default='image3.jpg')
    filename_3= db.Column(db.String(80), default='image3.jpg')
    def generate_slug(self):
        self.slug = ''
        if self.name:
            self.slug = slugify(self.name)
    def __repr__(self):
        return '<Post %r>' % self.name
    def __init__(self, *args, **kwargs):
        super(AddProduct, self).__init__(*args, **kwargs)
        self.slug = slugify(self.name)
