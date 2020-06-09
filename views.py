from flask import render_template ,redirect,request,url_for,flash
from app import app ,db
from models import User
from app import login_manager
from products.forms import LoginForm , RegisterForm
from flask_login import login_user
from flask_bootstrap import Bootstrap
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

@app.route('/')
def homepage():
    return render_template('homepage.html')
 

@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('products.index'))
        return '<h1>Invalid username or password</h1>'
    return render_template('login.html', form=form)

#signup
@app.route('/signup/', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('products.index'))
        flash("Successfully logged in as %s." % form.user.username,"success")
    return render_template('signup.html', form=form)

@app.route("/logout/")
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(request.args.get('next') or url_for('homepage'))
