"""
Selenium Training - Demo Test Application
A Flask web application with various features for Selenium practice.
"""
import os
import time

from flask import (
    Flask, render_template, request, redirect, url_for,
    session, jsonify, flash
)
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'selenium-training-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL', 'postgresql://admin:admin123@postgres:5432/db_learning'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = '/tmp/uploads'

db = SQLAlchemy(app)


# ── Models ──────────────────────────────────────────────────────────────────

class User(db.Model):
    __tablename__ = 'app_users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    full_name = db.Column(db.String(120))


class Product(db.Model):
    __tablename__ = 'app_products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50))
    description = db.Column(db.Text)
    stock = db.Column(db.Integer, default=0)


class Employee(db.Model):
    __tablename__ = 'app_employees'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    department = db.Column(db.String(50))
    salary = db.Column(db.Float)
    email = db.Column(db.String(120))
    phone = db.Column(db.String(20))


# ── Seed Data ───────────────────────────────────────────────────────────────

def seed_data():
    if Product.query.count() == 0:
        products = [
            Product(name='Laptop Pro', price=999.99, category='Electronics',
                    description='High-performance laptop for professionals', stock=50),
            Product(name='Wireless Mouse', price=29.99, category='Electronics',
                    description='Ergonomic wireless mouse with USB receiver', stock=200),
            Product(name='Python Book', price=49.99, category='Books',
                    description='Comprehensive guide to Python programming', stock=100),
            Product(name='Selenium Guide', price=39.99, category='Books',
                    description='Master Selenium WebDriver testing', stock=75),
            Product(name='USB-C Hub', price=59.99, category='Electronics',
                    description='7-in-1 USB-C hub with HDMI output', stock=150),
            Product(name='Desk Lamp', price=34.99, category='Home',
                    description='Adjustable LED desk lamp', stock=80),
            Product(name='Notebook Set', price=12.99, category='Stationery',
                    description='Pack of 5 ruled notebooks', stock=300),
            Product(name='Backpack', price=79.99, category='Accessories',
                    description='Water-resistant laptop backpack', stock=60),
            Product(name='Monitor Stand', price=44.99, category='Home',
                    description='Adjustable aluminum monitor stand', stock=90),
            Product(name='Mechanical Keyboard', price=89.99, category='Electronics',
                    description='RGB mechanical keyboard with Cherry MX switches', stock=120),
        ]
        db.session.add_all(products)

    if Employee.query.count() == 0:
        employees = [
            Employee(name='Alice Johnson', department='Engineering', salary=95000,
                     email='alice@company.com', phone='555-0101'),
            Employee(name='Bob Smith', department='Marketing', salary=72000,
                     email='bob@company.com', phone='555-0102'),
            Employee(name='Carol Williams', department='Engineering', salary=105000,
                     email='carol@company.com', phone='555-0103'),
            Employee(name='David Brown', department='Sales', salary=68000,
                     email='david@company.com', phone='555-0104'),
            Employee(name='Eva Martinez', department='HR', salary=78000,
                     email='eva@company.com', phone='555-0105'),
            Employee(name='Frank Lee', department='Engineering', salary=110000,
                     email='frank@company.com', phone='555-0106'),
            Employee(name='Grace Kim', department='Marketing', salary=75000,
                     email='grace@company.com', phone='555-0107'),
            Employee(name='Henry Wilson', department='Sales', salary=71000,
                     email='henry@company.com', phone='555-0108'),
            Employee(name='Iris Chen', department='Engineering', salary=98000,
                     email='iris@company.com', phone='555-0109'),
            Employee(name='Jack Taylor', department='HR', salary=82000,
                     email='jack@company.com', phone='555-0110'),
        ]
        db.session.add_all(employees)

    if User.query.count() == 0:
        demo_user = User(
            username='testuser',
            email='test@example.com',
            password=generate_password_hash('password123'),
            full_name='Test User'
        )
        db.session.add(demo_user)

    db.session.commit()


# ── Routes ──────────────────────────────────────────────────────────────────

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['username'] = user.username
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            error = 'Invalid username or password'
    return render_template('login.html', error=error)


@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    success = None
    if request.method == 'POST':
        username = request.form.get('username', '')
        email = request.form.get('email', '')
        password = request.form.get('password', '')
        confirm_password = request.form.get('confirm_password', '')
        full_name = request.form.get('full_name', '')

        if password != confirm_password:
            error = 'Passwords do not match'
        elif User.query.filter_by(username=username).first():
            error = 'Username already exists'
        elif User.query.filter_by(email=email).first():
            error = 'Email already registered'
        else:
            new_user = User(
                username=username,
                email=email,
                password=generate_password_hash(password),
                full_name=full_name
            )
            db.session.add(new_user)
            db.session.commit()
            success = 'Registration successful! You can now login.'
    return render_template('register.html', error=error, success=success)


@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user = db.session.get(User, session['user_id'])
    return render_template('dashboard.html', user=user)


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


@app.route('/products')
def products():
    category = request.args.get('category', '')
    search = request.args.get('search', '')
    query = Product.query
    if category:
        query = query.filter_by(category=category)
    if search:
        query = query.filter(Product.name.ilike(f'%{search}%'))
    all_products = query.all()
    categories = db.session.query(Product.category).distinct().all()
    return render_template(
        'products.html', products=all_products,
        categories=[c[0] for c in categories],
        selected_category=category, search=search
    )


@app.route('/add-to-cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    cart = session.get('cart', {})
    pid = str(product_id)
    cart[pid] = cart.get(pid, 0) + 1
    session['cart'] = cart
    flash(f'Item added to cart!', 'success')
    return redirect(url_for('products'))


@app.route('/cart')
def cart():
    cart_data = session.get('cart', {})
    items = []
    total = 0
    for pid, qty in cart_data.items():
        product = db.session.get(Product, int(pid))
        if product:
            item_total = product.price * qty
            items.append({'product': product, 'quantity': qty, 'total': item_total})
            total += item_total
    return render_template('cart.html', items=items, total=total)


@app.route('/update-cart/<int:product_id>', methods=['POST'])
def update_cart(product_id):
    cart = session.get('cart', {})
    action = request.form.get('action')
    pid = str(product_id)
    if action == 'increase':
        cart[pid] = cart.get(pid, 0) + 1
    elif action == 'decrease':
        if cart.get(pid, 0) > 1:
            cart[pid] -= 1
        else:
            cart.pop(pid, None)
    elif action == 'remove':
        cart.pop(pid, None)
    session['cart'] = cart
    return redirect(url_for('cart'))


@app.route('/checkout', methods=['POST'])
def checkout():
    session.pop('cart', None)
    flash('Order placed successfully! Thank you for your purchase.', 'success')
    return redirect(url_for('products'))


@app.route('/practice-forms')
def practice_forms():
    return render_template('practice_forms.html')


@app.route('/submit-form', methods=['POST'])
def submit_form():
    data = {
        'first_name': request.form.get('first_name'),
        'last_name': request.form.get('last_name'),
        'email': request.form.get('email'),
        'gender': request.form.get('gender'),
        'hobbies': request.form.getlist('hobbies'),
        'country': request.form.get('country'),
        'message': request.form.get('message'),
        'experience': request.form.get('experience'),
        'agree_terms': 'Yes' if request.form.get('agree_terms') else 'No',
        'dob': request.form.get('dob'),
        'color': request.form.get('color'),
    }
    return render_template('form_result.html', data=data)


@app.route('/tables')
def tables():
    employees = Employee.query.all()
    return render_template('tables.html', employees=employees)


@app.route('/dynamic')
def dynamic():
    return render_template('dynamic.html')


@app.route('/api/load-content')
def api_load_content():
    time.sleep(2)
    return jsonify({
        'message': 'This content was loaded dynamically after a 2-second delay!',
        'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
        'items': ['Dynamic Item 1', 'Dynamic Item 2', 'Dynamic Item 3']
    })


@app.route('/api/search-employees')
def api_search_employees():
    query = request.args.get('q', '')
    employees = Employee.query.filter(
        Employee.name.ilike(f'%{query}%')
    ).all()
    return jsonify([{
        'name': e.name, 'department': e.department, 'email': e.email
    } for e in employees])


@app.route('/api/notifications')
def api_notifications():
    time.sleep(1)
    return jsonify([
        {'text': 'New order received', 'time': '2 min ago'},
        {'text': 'User registered', 'time': '5 min ago'},
        {'text': 'Server backup completed', 'time': '1 hour ago'},
    ])


@app.route('/interactions')
def interactions():
    return render_template('interactions.html')


@app.route('/frames')
def frames():
    return render_template('frames.html')


@app.route('/frame-content')
def frame_content():
    return render_template('frame_content.html')


@app.route('/nested-frame')
def nested_frame():
    return render_template('nested_frame.html')


@app.route('/new-window')
def new_window():
    return render_template('new_window.html')


@app.route('/file-upload', methods=['GET', 'POST'])
def file_upload():
    message = None
    if request.method == 'POST':
        uploaded = request.files.get('file')
        if uploaded and uploaded.filename:
            os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
            safe_name = uploaded.filename.replace('..', '').replace('/', '')
            uploaded.save(os.path.join(app.config['UPLOAD_FOLDER'], safe_name))
            message = f'File "{safe_name}" uploaded successfully!'
        else:
            message = 'No file selected'
    return render_template('file_upload.html', message=message)


@app.route('/slow-page')
def slow_page():
    delay = request.args.get('delay', 3, type=int)
    time.sleep(min(delay, 10))
    return render_template('slow_page.html', delay=delay)


# ── App Startup ─────────────────────────────────────────────────────────────

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        seed_data()
    app.run(host='0.0.0.0', port=5000, debug=True)
