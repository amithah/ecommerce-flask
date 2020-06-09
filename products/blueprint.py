import os
from flask import Blueprint,flash
from models import User, Brand ,Category, AddProduct


from flask import render_template ,url_for,redirect,request
from products.forms import BrandForm, CategoryForm, AddProductForm
from app import app,db

from werkzeug.utils import secure_filename
from flask_login import login_required,current_user

products = Blueprint('products', __name__, template_folder='templates')
# products index page routing
@products.route('/')
@login_required
def index():
    products =  AddProduct.query.all()
    return render_template('products/index.html',products = products)
#brands page routing
@products.route('/brands')
def brands():
    brands= Brand.query.all()
    return render_template('products/brands.html',brands = brands)
    #brands page routing
@products.route('/categories')
def categories():
    categories= Category.query.all()
    return render_template('products/categories.html',categories=categories)
#----------------------------------------------------------
@products.route('/addbrand' ,methods=['GET', 'POST'])
@login_required
def addbrand():
    if request.method == 'POST':
        form = BrandForm(request.form)
        if form.validate():
            brand = Brand(name=form.name.data)
            db.session.add(brand)
            db.session.commit()
            flash('Brand "%s" created successfully.' % brand.name,'success')
            return redirect(url_for('products.index', slug=brand.slug))
    else:
        form = BrandForm()
    return render_template('products/addbrand.html',form =form)
#----------------------------------------------------------
@products.route('/addcategory' ,methods=['GET', 'POST'])
@login_required
def addcategory():
    if request.method == 'POST':
        form = CategoryForm(request.form)
        if form.validate():
            category = Category(name=form.name.data)
            db.session.add(category)
            db.session.commit()
            flash('Category"%s" created successfully.' % category.name,'success')
            return redirect(url_for('products.index', slug=category.slug))
    else:
        form = CategoryForm()
    return render_template('products/addcategory.html',form =form)
#------------------------------------------------------------------------

@products.route('/addproduct', methods=['GET','POST'])
@login_required
def addproduct():
    
    form = AddProductForm(request.form)
    brands = Brand.query.all()
    print(brands)
    categories = Category.query.all()
    if request.method=="POST"and 'image_1' in request.files:
        name = form.name.data
        price = form.price.data
        discount = form.discount.data
        stock = form.stock.data
        colors = form.colors.data
        desc = form.discription.data
        brand = request.form.get('brand')
        
        category = request.form.get('category')

        im_1 = request.files.get('image_1')
        filename_1= os.path.join(app.config['IMAGES_DIR'],secure_filename(im_1.filename))
        image_1 = im_1.save(filename_1)
        os.rename(app.config['IMAGES_DIR']+'/'+im_1.filename,app.config['IMAGES_DIR']+'/image_1.jpg')
        

        im_2 = request.files.get('image_2')
        filename_2 = os.path.join(app.config['IMAGES_DIR'],secure_filename(im_2.filename))
        image_2 = im_2.save(filename_2)

        im_3 = request.files.get('image_3')
        filename_3 = os.path.join(app.config['IMAGES_DIR'],secure_filename(im_3.filename))
        image_3 = im_3.save(filename_3)

        AddProduct1 = AddProduct(name=name,price=price,discount=discount,stock=stock,colors=colors,desc=desc,category_id=category,brand_id=brand,image_1=image_1,image_2=image_2,image_3=image_3)
        db.session.add(AddProduct1)
        flash(f'The product {name} was added in database','success')
        db.session.commit()
    
    return render_template('products/addproduct.html', form=form,brands=brands,categories=categories)

#------------------------------------------------------------------------
@products.route('/logout',  methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

#-------------------------------------------------------------------------
#----------------------------------------------------------------------------
@products.route('/updatebrand/<int:id>',methods=['GET','POST'])
def updatebrand(id):
    if 'email' not in session:
        flash('Login first please','danger')
        return redirect(url_for('login'))
    updatebrand = Brand.query.get_or_404(id)
    brand = request.form.get('brand')
    if request.method =="POST":
        updatebrand.name = brand
        flash(f'The brand {updatebrand.name} was changed to {brand}','success')
        db.session.commit()
        return redirect(url_for('brands'))
    brand = updatebrand.name
    return render_template('products/addbrand.html', title='Update brand',brands='brands',updatebrand=updatebrand)


@products.route('/deletebrand/<int:id>', methods=['GET','POST'])
def deletebrand(id):
    brand = Brand.query.get_or_404(id)
    if request.method=="POST":
        db.session.delete(brand)
        flash(f"The brand {brand.name} was deleted from your database","success")
        db.session.commit()
        return redirect(url_for('index'))
    flash(f"The brand {brand.name} can't be  deleted from your database","warning")
    return redirect(url_for('index'))


@products.route('/updatecat/<int:id>',methods=['GET','POST'])
def updatecat(id):
    if 'email' not in session:
        flash('Login first please','danger')
        return redirect(url_for('login'))
    updatecat = Category.query.get_or_404(id)
    category = request.form.get('category')  
    if request.method =="POST":
        updatecat.name = category
        flash(f'The category {updatecat.name} was changed to {category}','success')
        db.session.commit()
        return redirect(url_for('categories'))
    category = updatecat.name
    return render_template('products/addbrand.html', title='Update cat',updatecat=updatecat)



@products.route('/deletecat/<int:id>', methods=['GET','POST'])
def deletecat(id):
    category = Category.query.get_or_404(id)
    if request.method=="POST":
        db.session.delete(category)
        flash(f"The brand {category.name} was deleted from your database","success")
        db.session.commit()
        return redirect(url_for('index'))
    flash(f"The brand {category.name} can't be  deleted from your database","warning")
    return redirect(url_for('index'))

