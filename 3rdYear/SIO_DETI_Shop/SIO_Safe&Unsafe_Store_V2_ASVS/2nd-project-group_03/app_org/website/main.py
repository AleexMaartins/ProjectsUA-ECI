import random
import time
from flask import Flask, render_template, request, redirect, request, flash, session
import sqlite3
import os
from flask import send_file
from cryptography.hazmat.primitives import hashes #pip install cryptography

############################# AUXILIARY FUNCTIONS #############################
#engine = create_engine(sqlite:///nome.bd,echo= true)
def init_db():
    connection = sqlite3.connect('data.db', check_same_thread=False)
    cursor = connection.cursor()

    #################### users table ####################

    cursor.execute("""DROP TABLE IF EXISTS users""") 
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    email TEXT NOT NULL,
    name TEXT NOT NULL,
    password TEXT NOT NULL
    );""")
    cursor.execute("""INSERT OR IGNORE INTO users VALUES (NULL,'admin@gmail.com', 'admin', 'admin')""")
    cursor.execute("""INSERT OR IGNORE INTO users VALUES (NULL,'alex@gmail.com', 'Alex', '1' )""")
    cursor.execute("""INSERT OR IGNORE INTO users VALUES (NULL,'eve@gmail.com', 'Eve', '1' )""")
    
    #################### checkout ####################
    cursor.execute("""DROP TABLE IF EXISTS checkout""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS checkout (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    credit_card INTEGER NOT NULL,
    expiration_date INTEGER NOT NULL,
    cvv INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id)
    );""")
    #################### catalog table ####################
    cursor.execute("""DROP TABLE IF EXISTS products""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    stock INTEGER NOT NULL, 
    description TEXT NULL,
    category TEXT NULL,
    image TEXT NULL
    );""")

    cursor.execute("INSERT OR IGNORE INTO products (name, price, stock, description, category, image) VALUES (?, ?, ?, ?, ?, ?)",
                   ('Steel Mug', 5.0, 44, 'This 1L stainless steel travel mug will keep your drinks refreshed for hours.', 'mugs', 'detiShopM1.png'))
    
    cursor.execute("INSERT OR IGNORE INTO products (name, price, stock, description, category, image) VALUES (?, ?, ?, ?, ?, ?)",
                   ('Shopping Bag', 7.0, 28, 'Shop smart and sustainably with our eco-friendly shopping bag.','bags', 'detiShopB.png' ))
    
    cursor.execute("INSERT OR IGNORE INTO products (name, price, stock, description, category, image) VALUES (?, ?, ?, ?, ?, ?)",
                   ('Mug', 3.0, 0, 'Start your day with a smile and your favorite beverage in our charming mugs.','mugs', 'detiShopM2.png'))
    
    cursor.execute("INSERT OR IGNORE INTO products (name, price, stock, description, category, image) VALUES (?, ?, ?, ?, ?, ?)",
                   ('Phone Case', 40.0, 8, 'Protect your smartphone with style using our new and improved sleek phone cases.','cases', 'detiShopP.png'))
    
    cursor.execute("INSERT OR IGNORE INTO products (name, price, stock, description, category, image) VALUES (?, ?, ?, ?, ?, ?)",
                   ('T-shirt', 25.0, 5,'Crafted with premium fabric, elevate your style with new improved T-shirt collection!','clothes', 'deti-shirtpng.png'))
   
    
    #################### cart table ####################
    cursor.execute("""DROP TABLE IF EXISTS cart""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS cart (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id),
    FOREIGN KEY (product_id) REFERENCES products (id)
    );""")
    
    cursor.execute("INSERT INTO cart (user_id, product_id, quantity) VALUES (?, ?, ?)",
        (2, 1, 1))  
    cursor.execute("INSERT INTO cart (user_id, product_id, quantity) VALUES (?, ?, ?)",
        (3, 4, 10))  

    ################## wishlist table #################
    cursor.execute("""DROP TABLE IF EXISTS wishlist""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS wishlist (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id),
    FOREIGN KEY (product_id) REFERENCES products (id)
    );""")

    cursor.execute("INSERT INTO wishlist (user_id, product_id, quantity) VALUES (?, ?, ?)",
            (2, 5, 1)) 
    cursor.execute("INSERT INTO wishlist (user_id, product_id, quantity) VALUES (?, ?, ?)",
            (2, 2, 2)) 
    
    ################## orders table #################
    cursor.execute("""DROP TABLE IF EXISTS orders""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY,
        order_id INTEGER NOT NULL,
        user_id INTEGER NOT NULL,
        product_id INTEGER NOT NULL,
        quantity INTEGER NOT NULL,
        order_date DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users (id),
        FOREIGN KEY (product_id) REFERENCES products (id)
        );""")
    cursor.execute("INSERT INTO orders (order_id, user_id, product_id, quantity,order_date) VALUES (?, ?, ?, ?, ?)",
        ('ORD_TEST_ORDER', 2, 1, 100,'2002-10-31 00:00:00' ))  

    ################## social table #################
    cursor.execute("""DROP TABLE IF EXISTS social""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS social (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    name TEXT NOT NULL,
    comment TEXT,
    rating INTEGER,  
    product_id INTEGER NOT NULL,
    FOREIGN KEY (product_id) REFERENCES products (id)
    );""")
    

    
    cursor.execute("INSERT INTO social (name, comment, rating, product_id) VALUES (?, ?, ?, ?)",
            ('Alex', "Pretty nice.", 4, 1)) 
    cursor.execute("INSERT INTO social (name, comment, rating, product_id) VALUES (?, ?, ?, ?)",
            ('Eve', "mid", 3, 1)) 
    cursor.execute("INSERT INTO social (name, comment, rating, product_id) VALUES (?, ?, ?, ?)",
            ('Alex', "It was perfect... perfect to the last detail :)", 5, 2))     
    
    ####### credit card info table #######
    cursor.execute("""DROP TABLE IF EXISTS credit_card_info""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS credit_card_info (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    cc_number INTEGER NOT NULL,
    exp_month INTEGER NOT NULL,
    exp_year INTEGER NOT NULL,
    cvv INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id)
    );""")
    cursor.execute("INSERT INTO credit_card_info (user_id, name, cc_number, exp_month, exp_year, cvv) VALUES (?, ?, ?, ?, ?, ?)",
               (2, 'Alex', 4444555566667777, 2, 2222, 123))




    connection.commit()

    # no fim dar close


def sign_up(name, password, password2, email):
    if password != password2:
        return False, "passwords don't match"
   
    password = hash(password)

    connection = sqlite3.connect('data.db', check_same_thread=False)
    cursor = connection.cursor()
    # check if there already exists a user with that name
    query = "SELECT EXISTS(SELECT 1 FROM users WHERE email ='" + \
        email + "');"
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        if results[0][0] == 1:
            return False, "email already exists"
    except:
        return False, "There was an error validating your input, please check your data and try again."
    # if we've reached this point, we can add the user to the database
    try:
        cursor.execute("INSERT INTO users VALUES (?, ?, ?)",
                       (email,name, password))
        connection.commit()
        return True, 'Account created successfully. Click <a href="/login">here</a> to login'
    except:
        return False, "There was an error validating your input, please check your data and try again."


def authenticate_user(email, password):
    if '/' in email:
        return False, "email can't contain character '/'"
    connection = sqlite3.connect('data.db', check_same_thread=False)
    cursor = connection.cursor()
    
    try:
        cursor.execute( "SELECT email, password, name FROM users WHERE email= ? AND password = ?", (email, password))
        results = cursor.fetchall()
        if len(results) == 0:
            return False, "Incorrect email or password", None, None, None
        
        return True, "", results[0][0], results[0][1], results[0][2]
    
    except Exception as e:
        print(e)
        return False, "There was an error validating your input, please check your data and try again.", None, None, None


############################# END OF AUXILIARY FUNCTIONS #############################

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
init_db()



@app.route('/', methods=['POST', 'GET'])
def home():
    if not session.get('user_email'):
        return redirect('/login')
    connection = sqlite3.connect('data.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    connection.close()
    
    return render_template('home.html', products=products)

# get current user 
def get_current_user_id():
    user_email = session.get('user_email')  
    if user_email:
        try:
            connection = sqlite3.connect('data.db', check_same_thread=False)
            cursor = connection.cursor()
            cursor.execute("SELECT id FROM users WHERE email = ?", (user_email,))
            user_id = cursor.fetchone()
            if user_id:
                user_id = user_id[0]
            
            return user_id
        except Exception as e:
            print("Database error:", str(e))
            return None


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        if password != 'admin' and password != '1':
            password = hash(password)

        
        result, msg, email, password, user_name = authenticate_user(email, password)
        
        if not result:
            flash(msg, category='error')
            return render_template('login.html')
        
        else:
            flash(msg, category='success')
            session['user_email'] = email # Set the user_id in the session
            session['user_password'] = password # Set the user_password in the session
            session['user_name'] = user_name # Set the user_name in the session
            return redirect('/')
    else:
        return render_template('login.html')



@app.route('/logout')
def logout():
    session.pop('user_name', None)  # Remove user_name from the session
    session.pop('user_email', None)  # Remove user_email from the session
    session.pop('user_password', None)  # Remove user_password from the session
    return redirect('/login')

@app.route('/sign-up', methods=['POST', 'GET'])
def sign_up():
    if request.method == 'POST':
        email = request.form['email']
        name = request.form['name']
        password = request.form['password']
        password2 = request.form['password2']
        
        
        result, msg = insert_user(email, name, password, password2)
        if not result:
            flash(msg, category='error')
        else:
            flash(msg, category='success')
        return render_template('sign_up.html')
    else:
        return render_template('sign_up.html')


def insert_user(email, name, password, password2):
    if password != password2:
        return False, "Passwords don't match"
    if len(password ) < 7:
        return False, "Password must be at least 7 characters long"
        
    password = hash(password)

    connection = sqlite3.connect('data.db', check_same_thread=False)
    cursor = connection.cursor()
    # check if there already exists a user with that email
    query = "SELECT EXISTS(SELECT 1 FROM users WHERE email = ?);"
    try:
        cursor.execute(query, (email,))
        results = cursor.fetchall()
        if results[0][0] == 1:
            return False, "email already exists"
    except:
        return False, "1There was an error validating your input, please check your data and try again."
    # if we've reached this point, we can add the user to the database
    try:
        cursor.execute("INSERT INTO users VALUES (NULL,?, ?, ?)",
                       (email, name, password))
        connection.commit()
        
        return True, 'Account created successfully. You can now login'
    except:
        return False, "There was an error validating your input, please check your data and try again."

def hash(input):
    input=bytes(input, 'utf-8')
    digest = hashes.Hash(hashes.SHA256())
    digest.update(input)
    return  digest.finalize()



#------------------------ Tomás trabalho hihihihi -----------------------------------------

#------------------------ Perfil do usuário -----------------------------------------------


@app.route('/profile', methods=['GET','POST'])

def change_password():
    if not session.get('user_email'):
        return redirect('/login')
    
    if request.method == 'POST':
        old_password = request.form['old_password']
        password = request.form['new_password']
        confirm_password = request.form['confirm_password']

        current_password = session.get('user_password')

        if hash(old_password) != current_password:
            flash("Old password is incorrect. Please try again.", category='error')
            return redirect('/profile')

        if password != confirm_password:
            flash("New passwords do not match. Please try again.", category='error')
            return redirect('/profile')

        if len(password) < 7:
            flash("New password must be at least 7 characters long. Please try again.", category='error')
            return redirect('/profile')

        result, msg = passworder_changer(password)
        if not result:
            flash(msg, category='error')
        else:
            flash(msg, category='success')
        return render_template('profile.html')
    else:
        return render_template('profile.html')


def passworder_changer(password):
    
    user_email = session.get('user_email')
    connection = sqlite3.connect('data.db', check_same_thread=False)
    cursor = connection.cursor()
    password = hash(password)
    session['user_password'] = password # Set the user_password in the session
    try:
        cursor.execute("UPDATE users SET password = ? WHERE email = ?",
                       (password, user_email))
        connection.commit()
        
        return True, 'Password changed'
    except:
        return False, "There was an error validating your input, please check your data and try again."
    
#------------------------ USER MANAGER -----------------------------------

@app.route('/usermanager', methods=['GET','POST'])
def edit_user():
    if not session.get('user_email'):
        return redirect('/login')
    connection = sqlite3.connect('data.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    users_data = cursor.fetchall()
    if session['user_name'] == "admin":
        if request.method == 'POST':
            id = request.form['user_id']
            name = request.form['new_name']
            password = request.form['new_password']   
            password2 = request.form['new_password2']   
            if password != password2:
                flash("Passwords do not match. Please try again.", category='error') 
                return redirect('/usermanager')
            if len(password ) < 7:
                flash("Password must be at least 7 characters long. Please try again.", category='error') 
                return redirect('/usermanager')
            result, msg = user_editor(id, name, password)

            if not result:
                flash(msg, category='error')
            else:
                flash(msg, category='success')

            cursor.execute("SELECT * FROM users")
            users_data = cursor.fetchall()    
            return render_template('usermanager.html', users_data=users_data)
        else:
            return render_template('usermanager.html', users_data=users_data)
    else:
        return 'Acesso negado'

def user_editor(id, name, password):
    
    connection = sqlite3.connect('data.db', check_same_thread=False)
    cursor = connection.cursor()

    try:
        password = hash(password)
        cursor.execute("UPDATE users SET password = ?, name = ? WHERE id = ?",
                       (password, name, id))
        connection.commit()
        
        return True, 'Profile changed'
    except:
        return False, "There was an error validating your input, please check your data and try again."



#------------------------------------------------------------------------------
#---------------------- BRANCO TEST CODE --------------------------------------
#------------------------------------------------------------------------------


# ---- DOWNLOAD ORDER--- 
@app.route('/download', methods=['POST'])
def download():
    if not session.get('user_email'):
        return redirect('/login')
    # Retrieve order_id from the form data
    order_id = request.form.get('order_id')

    connection = sqlite3.connect('data.db', check_same_thread=False)
    cursor = connection.cursor()

    # Get order data
    cursor.execute("""SELECT products.name, orders.quantity, products.price
                     FROM orders
                     JOIN products ON products.id = orders.product_id
                     WHERE orders.order_id = ?""", (order_id,))
    order_data = cursor.fetchall()

    # Get order date
    cursor.execute("SELECT order_date FROM orders WHERE order_id = ?", (order_id,))
    order_date = cursor.fetchone()

    # Calculate the total price
    total_price = sum(item[1] * item[2] for item in order_data)

    # Prepare the data as a string
    data = f"Order ID: {order_id}\nOrder Date: {order_date[0]}\n\n"
    for item in order_data:
        name, quantity, price = item
        data += f"Product: {name}\nQuantity: {quantity}\nPrice: ${price}\n\n"

    data += f"Total Price: ${total_price}\n"

    # Get the user's desktop directory
    desktop_dir = os.path.join(os.path.expanduser("~"), "Desktop")

    # Create a path to save the file on the desktop
    file_path = os.path.join(desktop_dir, f"temp_order_{order_id}.txt")
    
    with open(file_path, 'w') as file:
        file.write(data)

    # Create a Flask response for the file download
    response = send_file(file_path, as_attachment=True)
    response.headers["Content-Disposition"] = f"attachment; filename={os.path.basename(file_path)}"

    # Do not remove the temporary file since it's saved to the desktop

    return response


    
#------------------------------------------------------------------------------
#---------- SOCIAL/REVIEWS ----------------
#------------------------------------------------------------------------------

@app.route("/social")
def social():
    if not session.get('user_email'):
        return redirect('/login')
    # Remove the argument from the route
    review = request.args.get('review')  # Retrieve 'review' from the URL query parameter
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM products WHERE id = ?", (review,))
    products = cursor.fetchall()
    user_id = get_current_user_id()


    if products:
        product_id = products[0][0]  # Extract the product ID from the selected product
        # Retrieve reviews from the "social" table for the selected product
        cursor.execute("SELECT * FROM social WHERE product_id = ?", (product_id,))

        reviews = cursor.fetchall()

    connection.close()
    return render_template('social.html', products=products, reviews=reviews, product_id=product_id)

#------------------------ ADD REVIEW -------------------------------------------
@app.route("/add_review", methods=['POST'])
def add_review():
    if not session.get('user_email'):
        return redirect('/login')
    if request.method == 'POST':
        user_id = get_current_user_id()
        name = session['user_name']
        product_id = request.form.get('product_id')
        comment = request.form.get('comment')
        rating = request.form.get('rating')

        # Insert the review into the database
        update_review_ADD(user_id, name, product_id, comment, rating)

        # Redirect back to the social page with the selected product_id
        return redirect(f'/social?review={product_id}')
    else:
        return redirect('/social')
#-----update review---
def update_review_ADD(user_id, name, product_id, comment, rating):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO social (user_id, name, product_id, comment, rating) VALUES (?, ?, ?, ?, ?)", (user_id, name, product_id, comment, rating))
    connection.commit()
    return



#-------------------------------- SAVE CHECKOUT DATA --------------------------------- 

@app.route('/checkout', methods=['GET'])
def checkout():
    if not session.get('user_email'):
        return redirect('/login')
    user_id = get_current_user_id()
    connection = sqlite3.connect('data.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM credit_card_info WHERE user_id = ?", (user_id,))
    cc_info = cursor.fetchall()

    return render_template('checkout.html', cc_info=cc_info)


#-------- ADD CART DATA TO ORDERS HISTORY ------------ 
@app.route('/move_to_orders', methods=['POST'])
def move_to_orders():
    if not session.get('user_email'):
        return redirect('/login')
    user_id = get_current_user_id()
    update_orders_ADD(user_id)

    # Check if the "Save credit card information" box is checked
    save_cc_info = request.form.get('sameadr') == "on"

    name = request.form.get('name')
    cc_number = request.form.get('cc_number')
    exp_month = request.form.get('exp_month')
    exp_year = request.form.get('exp_year')
    cvv = request.form.get('cvv')

    # Check if any of the info is missing or empty
    if not name or not cc_number or not exp_month or not exp_year or not cvv:
        flash("Please fill in all the required fields.", category='error')
        return redirect('/checkout')  # Redirect if there is an error

    connection = sqlite3.connect('data.db', check_same_thread=False)
    cursor = connection.cursor()

    if save_cc_info:
        # If the box is checked, delete the existing credit card info and insert the new one
        cursor.execute("DELETE FROM credit_card_info WHERE user_id = ?", (user_id,))
        cursor.execute("INSERT INTO credit_card_info (user_id, name, cc_number, exp_month, exp_year, cvv) VALUES (?, ?, ?, ?, ?, ?)",
                       (user_id, name, cc_number, exp_month, exp_year, cvv))

        connection.commit()
    else:
        # If the box is not checked, only insert the order data without updating credit card info
        pass

    return redirect('/orders')
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------



#------------------------ TEST CODE TO BURN LATER - Alex ---------------------

# WORKS FINE ------------------- VIEW USER DATA IN DATABASE ---------------------------------------
@app.route('/view_users', methods=['GET']) 
def view_users():
    if not session.get('user_email'):
        return redirect('/login')
    connection = sqlite3.connect('data.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    users_data = cursor.fetchall()
    
    cursor.execute("SELECT * FROM cart")
    cart = cursor.fetchall()
    

    return render_template('view_usersTEST.html', users_data=users_data, cart=cart)
# ------------------------------------------------------------------------------------------------------
@app.route('/products', methods=['GET'])
def products():
    connection = sqlite3.connect('data.db', check_same_thread=False)
    cursor = connection.cursor()

    # Fetch products from the database
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    

    return render_template('home.html', products=products)
# ------------------------------------------------------------------------------------------------------

# WORKS FINE ------------------- ADD TO CART -------------------------------------------------
@app.route('/move_to_cart', methods=['POST'])
def move_to_cart():
    if not session.get('user_email'):
        return redirect('/login')
    if request.method == 'POST':
        user_id = get_current_user_id()
        product_id = request.form.get('product_id')
        review = request.form.get('review') # devolve o ID do produto que poderá receber a review

        if review:
            return redirect(f'/social?review={review}')


        if product_id:
            update_cart_ADD(user_id, product_id)
            # Check if the current page is the cart and redirect accordingly
            current_page = request.form.get('current_page')
            if current_page == "cart":
                return redirect('/cart')
            else:
                return redirect('/#products')
    else:
        return redirect('/#products')

def update_cart_ADD(user_id, product_id):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute("SELECT stock FROM products WHERE products.id = ?", (product_id))
    existing_stock = cursor.fetchone()
    if existing_stock[0] == 0:
        flash("OUT OF STOCK")
        return False
    cursor.execute("UPDATE products SET stock = ? WHERE products.id = ?", (existing_stock[0]-1,product_id))

    try:
        cursor.execute("SELECT quantity FROM cart WHERE cart.user_id = ? AND cart.product_id = ?", (user_id,product_id))
        existing_quantity = cursor.fetchone()
        new_quantity = existing_quantity[0]+1
        cursor.execute("UPDATE cart SET quantity = ? WHERE cart.user_id = ? AND cart.product_id = ?", (new_quantity,user_id,product_id))
        connection.commit()
        return True 

    except :
        cursor.execute("INSERT INTO cart (user_id, product_id, quantity) VALUES (?, ?, ?)", (user_id, product_id, 1))
        connection.commit()
        return False
    

# WORKS FINE ------------------- SHOW CART ---------------------------------------
# Define a function to fetch the user's cart data from the database.
@app.route('/cart', methods=['POST', 'GET'])
def cartANDwishlist():
    if not session.get('user_email'):
        return redirect('/login')
    # Get the current user's ID (you need to implement this).
    user_id = get_current_user_id()

    # Fetch the user's cart data.
    cart_data = cart(user_id)
    wishlist_data= wishlist(user_id)

    return render_template('cart.html', cart_data=cart_data, wishlist_data=wishlist_data)

def cart(user_id):

    # Fetch the user's cart data.
    cart_data = get_cart_data(user_id)
    
    return cart_data

def get_cart_data(user_id):
    connection = sqlite3.connect('data.db', check_same_thread=False)
    cursor = connection.cursor()

    # Fetch the user's cart data from the database.
    cursor.execute("""SELECT * FROM cart WHERE cart.user_id = ?""", (user_id,))
    cursor.execute("""SELECT cart.id, cart.quantity, products.id, products.name, products.price
                      FROM cart
                      JOIN products ON products.id = cart.product_id
                      WHERE cart.user_id = ?""", (user_id,))
    cart_data = cursor.fetchall()
    if not cart_data:
        return None

    #list for product and quantity
    products = {"total_price": 0, "products": []}
    
    for cart_item in cart_data:
        price = cart_item[1] * cart_item[-1]
        products["products"].append({"id" : cart_item[2] ,"name" : cart_item[3], "quantity": cart_item[1], "price": price})
        products["total_price"] += price
    
    return products
# WORKS FINE ------------------- SHOW WISHLIST ---------------------------------------
def wishlist(user_id):
    # Fetch the user's cart data.
    wishlist_data = get_wishlist_data(user_id)
    
    return wishlist_data

def get_wishlist_data(user_id):
    connection = sqlite3.connect('data.db', check_same_thread=False)
    cursor = connection.cursor()
    # Fetch the user's cart data from the database.
    cursor.execute("""SELECT * FROM wishlist WHERE wishlist.user_id = ?""", (user_id,))
    cursor.execute("""SELECT wishlist.id, wishlist.quantity, products.id, products.name, products.price
                      FROM wishlist
                      JOIN products ON products.id = wishlist.product_id
                      WHERE wishlist.user_id = ?""", (user_id,))
    wishlist_data = cursor.fetchall()
    if not wishlist_data:
        return None

    #list for product and quantity
    products = {"total_price": 0, "products": []}
    
    for wishlist_item in wishlist_data:
        price = wishlist_item[1] * wishlist_item[-1]
        products["products"].append({"id" : wishlist_item[2] ,"name" : wishlist_item[3], "quantity": wishlist_item[1], "price": price})
        products["total_price"] += price
    
    return products

# WORKS FINE ------------------- REMOVE FROM CART ---------------------------------------
@app.route('/remove_from_cart', methods=['POST'])
def remove_from_cart():
    if not session.get('user_email'):
        return redirect('/login')
    if request.method == 'POST':
        user_id = get_current_user_id()
        product_id = request.form.get('product_id')

        update_cart_REMOVE(user_id, product_id)
        return redirect('/cart')
    else:
        return redirect('/cart')

def update_cart_REMOVE(user_id, product_id):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute("SELECT stock FROM products WHERE products.id = ?", (product_id))
    existing_stock = cursor.fetchone()
    cursor.execute("UPDATE products SET stock = ? WHERE products.id = ?", (existing_stock[0]+1,product_id))

    cursor.execute("SELECT quantity FROM cart WHERE cart.user_id = ? AND cart.product_id = ?", (user_id,product_id))
    existing_quantity = cursor.fetchone()
    if existing_quantity[0]>1:
        cursor.execute("UPDATE cart SET quantity = ? WHERE cart.user_id = ? AND cart.product_id = ?", (existing_quantity[0]-1,user_id,product_id))
    else:
        cursor.execute("DELETE FROM cart WHERE cart.user_id = ? AND cart.product_id = ?", (user_id,product_id))

    connection.commit()
        
    return  
# WORKS FINE ------------------- ADD TO WISHLIST -----------------------------------------
@app.route('/move_to_wishlist', methods=['POST'])
def move_to_wishlist():
    if not session.get('user_email'):
        return redirect('/login')
    user_id = get_current_user_id()
    product_id = request.form.get('product_id')

    update_wishlist_ADD(user_id, product_id)
    
    return redirect('/cart')

def update_wishlist_ADD(user_id, product_id):
    try:
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        cursor.execute("SELECT quantity FROM wishlist WHERE wishlist.user_id = ? AND wishlist.product_id = ?", (user_id,product_id))
        existing_quantity = cursor.fetchone() 
        new_quantity = existing_quantity[0]+1
        cursor.execute("UPDATE wishlist SET quantity = ? WHERE wishlist.user_id = ? AND wishlist.product_id = ?", (new_quantity,user_id,product_id))
        connection.commit()
        return True 

    except :
        cursor.execute("INSERT INTO wishlist (user_id, product_id, quantity) VALUES (?, ?, ?)", (user_id, product_id, 1))
        connection.commit()
        return False


# WORKS FINE ------------------- REMOVE FROM WISHLIST ---------------------------------------
@app.route('/remove_from_wishlist', methods=['POST'])
def remove_from_wishlist():
    if not session.get('user_email'):
        return redirect('/login')
    if request.method == 'POST':
        user_id = get_current_user_id()
        product_id = request.form.get('product_id')

        update_wishlist_REMOVE(user_id, product_id)
        return redirect('/cart')
    else:
        return redirect('/cart')

def update_wishlist_REMOVE(user_id, product_id):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute("SELECT quantity FROM wishlist WHERE wishlist.user_id = ? AND wishlist.product_id = ?", (user_id,product_id))
    existing_quantity = cursor.fetchone()
    if existing_quantity[0]>1:
        cursor.execute("UPDATE wishlist SET quantity = ? WHERE wishlist.user_id = ? AND wishlist.product_id = ?", (existing_quantity[0]-1,user_id,product_id))
    else:
        cursor.execute("DELETE FROM wishlist WHERE wishlist.user_id = ? AND wishlist.product_id = ?", (user_id,product_id))

    connection.commit()
        
    return  
 
def update_orders_ADD(user_id):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    
    # Fetch cart id
    cursor.execute("SELECT * FROM cart WHERE cart.user_id = ?", (user_id,))
    cart = cursor.fetchall()
   
    counter = 0

    order_id = get_new_order_id()  # A function to generate a new unique order ID

    for item in cart:
        cart_id = item[0]
        user_id = item[1]
        product_id = item[2]
        quantity = item[3]
        counter += 1
        #appends all items in cart and adds them to orders in one fell swoop
        cursor.execute("INSERT INTO orders (order_id,user_id, product_id, quantity) VALUES (?, ?, ?, ?)",
            (order_id, user_id, product_id, quantity))
        cursor.execute("DELETE FROM cart WHERE id = ?", (cart_id,)) #THIS IS COMMENTED FOR TESTING PURPOSES

    
    connection.commit()
    cursor.execute("SELECT * FROM cart where user_id = ?", (user_id,))
    orders = cursor.fetchall()

    cursor.execute("SELECT * FROM orders")
    orders = cursor.fetchall()


def get_new_order_id():
    # Get current time (in seconds) since the epoch
    current_time = int(time.time() ) 
    # Generate a random number between 0 and 9999
    random_number = random.randint(0, 9999)

    # Combine the timestamp and random number to form the order ID

    order_id = f"ORD_{current_time}_{random_number}"  # Example format: ORD_1635634132_5678

    return order_id

# WORKS FINE ------------- SHOW PREVIOUS ORDERS ---------------------------------

@app.route('/orders', methods=['GET'])
def orders():
    if not session.get('user_email'):
        return redirect('/login')
    user_id = get_current_user_id()
    # Fetch the user's orders data with associated items.
    orders_data = get_orders_data(user_id)
    
    return render_template("orders.html", orders_data=orders_data)

def get_orders_data(user_id):
    connection = sqlite3.connect ('data.db', check_same_thread=False)
    cursor = connection.cursor()
    
    # Fetch orders for the user
    cursor.execute("SELECT * FROM orders WHERE user_id = ?", (user_id,))
    cursor.execute("""SELECT orders.order_id, orders.quantity, orders.order_date, products.id, products.name, products.price
                      FROM orders
                      JOIN products ON products.id = orders.product_id
                      WHERE orders.user_id = ?""", (user_id,))
    orders_data = cursor.fetchall()
    
    if not orders_data:
        return None

    products = {}  # Dictionary to store order_id as keys

        
    for orders_item in orders_data:
        order_id = orders_item[0]

        # If order_id is not already in products, initialize it
        if order_id not in products:
            products[order_id] = {"total_price": 0, "products": [], "order_date": orders_item[2]}

        price = orders_item[1] * orders_item[-1]
        products[order_id]["products"].append({"id" : orders_item[3] ,"name" : orders_item[4], "quantity": orders_item[1], "price": price})
        products[order_id]["total_price"] += price
    
    return products


# WORKS FINE  ------------- REORDER ---------------------------------
@app.route('/reorder', methods=['POST'])
def reorder():
    if not session.get('user_email'):
        return redirect('/login')
    order_id = request.form.get('order_id')
    user_id = get_current_user_id()
    
    connection = sqlite3.connect ('data.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM orders WHERE order_id = ?", (order_id,))
    previous_orders = cursor.fetchall()
    for item in previous_orders:
        update_cart_REORDER(user_id, item[3], item[4])

    return redirect('/cart')

def update_cart_REORDER(user_id, product_id, quantity):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute("SELECT quantity FROM cart WHERE cart.user_id = ? AND cart.product_id = ?", (user_id,product_id))
    existing_quantity = cursor.fetchone()
    if existing_quantity:
        new_quantity = existing_quantity[0] + quantity
        cursor.execute("UPDATE cart SET quantity = ? WHERE cart.user_id = ? AND cart.product_id = ?", (new_quantity,user_id,product_id))
        connection.commit()
        return True 

    else :
        cursor.execute("INSERT INTO cart (user_id, product_id, quantity) VALUES (?, ?, ?)", (user_id, product_id, quantity))
        connection.commit()
        return False

if __name__ == "__main__":
    app.run(debug=False,port=2000) 





