from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    restaurant = {
        'name': 'Pizza With Spice',
        'tagline': 'Taste of Happiness - Best Pizza in Town',
        'phone': '85436xxxxx',
        'email': 'info@pizzawithspice.com',
        'address': 'Main Market Road, Mohali, Punjab',
        'hours': '9 AM - 11 PM',
        'stats': [
            {'number': '5000+', 'label': 'Happy Customers'},
            {'number': '100+', 'label': 'Menu Items'},
            {'number': '5+', 'label': 'Years Experience'},
            {'number': '98%', 'label': 'Positive Reviews'}
        ]
    }
    return render_template('home.html', restaurant=restaurant)

@app.route('/menu')
def menu():
    categories = ['All', 'Pizza', 'Burgers', 'Sandwich', 'Snacks', 'Pasta', 'Shakes', 'Coffee', 'Mojito', 'Combos']
    
    menu_items = [
        # PIZZA
        {'id': 1, 'name': 'Veg Special 1', 'price': 259, 'category': 'Pizza', 
         'description': 'Double Cheese loaded', 'image': '🍕', 'popular': True},
        {'id': 2, 'name': 'Farm House', 'price': 259, 'category': 'Pizza', 
         'description': 'Onion, capsicum, tomato, mushroom', 'image': '🍕', 'popular': True},
        {'id': 3, 'name': 'Makhani Paneer', 'price': 259, 'category': 'Pizza', 
         'description': 'Capsicum, paneer', 'image': '🍕', 'popular': False},
        {'id': 4, 'name': 'Achari Pizza', 'price': 259, 'category': 'Pizza', 
         'description': 'Onion, corn, red paprika', 'image': '🍕', 'popular': False},
        {'id': 5, 'name': 'Cheese Corn', 'price': 259, 'category': 'Pizza', 
         'description': 'Cheese + corn', 'image': '🍕', 'popular': False},
        {'id': 6, 'name': 'Cheese Mushroom', 'price': 259, 'category': 'Pizza', 
         'description': 'Cheese + mushroom', 'image': '🍕', 'popular': False},
        {'id': 7, 'name': 'Tandoori Paneer', 'price': 259, 'category': 'Pizza', 
         'description': 'Onion, capsicum, corn, paneer', 'image': '🍕', 'popular': True},
        {'id': 8, 'name': 'New Chef Choice', 'price': 259, 'category': 'Pizza', 
         'description': 'Onion, corn, paneer, cucumber, mushroom', 'image': '🍕', 'popular': True},
        {'id': 9, 'name': 'Mix Flavoured Pizza', 'price': 259, 'category': 'Pizza', 
         'description': 'Onion, capsicum, paneer, jalapeno, tomato', 'image': '🍕', 'popular': False},
        {'id': 10, 'name': 'Veg Saucy Pasta Pizza', 'price': 259, 'category': 'Pizza', 
         'description': 'Onion, corn, jalapeno, penny pasta', 'image': '🍕', 'popular': False},
        
        # BURGERS
        {'id': 11, 'name': 'Aloo Tikki Burger', 'price': 120, 'category': 'Burgers', 
         'description': 'Classic veg burger', 'image': '🍔', 'popular': False},
        {'id': 12, 'name': 'Veg Burger', 'price': 120, 'category': 'Burgers', 
         'description': 'Grilled veg burger', 'image': '🍔', 'popular': False},
        {'id': 13, 'name': 'Cheese Burger', 'price': 140, 'category': 'Burgers', 
         'description': 'With cheese', 'image': '🍔', 'popular': True},
        {'id': 14, 'name': 'Paneer Burger', 'price': 150, 'category': 'Burgers', 
         'description': 'Grilled paneer', 'image': '🍔', 'popular': True},
        {'id': 15, 'name': 'Chilli Cheese Paneer Burger', 'price': 160, 'category': 'Burgers', 
         'description': 'Spicy paneer', 'image': '🍔', 'popular': False},
        {'id': 16, 'name': 'Spicy Cheese Corn Burger', 'price': 150, 'category': 'Burgers', 
         'description': 'Cheese corn filling', 'image': '🍔', 'popular': False},
        {'id': 17, 'name': 'Maharaja Burger', 'price': 170, 'category': 'Burgers', 
         'description': 'Special burger', 'image': '🍔', 'popular': True},
        {'id': 18, 'name': 'Special Burger', 'price': 160, 'category': 'Burgers', 
         'description': 'Premium burger', 'image': '🍔', 'popular': False},
        
        # SANDWICH
        {'id': 19, 'name': 'Veg Grilled Sandwich', 'price': 130, 'category': 'Sandwich', 
         'description': 'Grilled veg', 'image': '🥪', 'popular': False},
        {'id': 20, 'name': 'Veg Cheese Sandwich', 'price': 140, 'category': 'Sandwich', 
         'description': 'With cheese', 'image': '🥪', 'popular': True},
        {'id': 21, 'name': 'Paneer Sandwich', 'price': 150, 'category': 'Sandwich', 
         'description': 'Grilled paneer', 'image': '🥪', 'popular': True},
        {'id': 22, 'name': 'Special Sandwich', 'price': 160, 'category': 'Sandwich', 
         'description': 'Premium sandwich', 'image': '🥪', 'popular': False},
        
        # SNACKS
        {'id': 23, 'name': 'Salted Fries', 'price': 80, 'category': 'Snacks', 
         'description': 'Classic fries', 'image': '🍟', 'popular': False},
        {'id': 24, 'name': 'Masala Fries', 'price': 90, 'category': 'Snacks', 
         'description': 'Spicy fries', 'image': '🍟', 'popular': True},
        {'id': 25, 'name': 'Peri Peri Fries', 'price': 100, 'category': 'Snacks', 
         'description': 'Nasi peri style', 'image': '🍟', 'popular': True},
        {'id': 26, 'name': 'Cheese Fries', 'price': 110, 'category': 'Snacks', 
         'description': 'With cheese', 'image': '🍟', 'popular': False},
        {'id': 27, 'name': 'Veggie Finger', 'price': 100, 'category': 'Snacks', 
         'description': 'Veg sticks', 'image': '🍟', 'popular': False},
        {'id': 28, 'name': 'Potato Bites', 'price': 90, 'category': 'Snacks', 
         'description': 'Mini potato bites', 'image': '🍟', 'popular': False},
        
        # PASTA
        {'id': 29, 'name': 'Red Pasta', 'price': 140, 'category': 'Pasta', 
         'description': 'Red sauce pasta', 'image': '🍝', 'popular': False},
        {'id': 30, 'name': 'White Pasta', 'price': 140, 'category': 'Pasta', 
         'description': 'White sauce pasta', 'image': '🍝', 'popular': True},
        {'id': 31, 'name': 'Paneer Makhani Pasta', 'price': 160, 'category': 'Pasta', 
         'description': 'Makhani paneer', 'image': '🍝', 'popular': True},
        {'id': 32, 'name': 'Mix Special Pasta', 'price': 170, 'category': 'Pasta', 
         'description': 'Special mix', 'image': '🍝', 'popular': False},
        {'id': 33, 'name': 'Spicy Achari Pasta', 'price': 150, 'category': 'Pasta', 
         'description': 'Achari style', 'image': '🍝', 'popular': False},
        
        # SHAKES
        {'id': 34, 'name': 'Vanilla Shake', 'price': 70, 'category': 'Shakes', 
         'description': 'Classic vanilla', 'image': '🥤', 'popular': False},
        {'id': 35, 'name': 'Strawberry Shake', 'price': 70, 'category': 'Shakes', 
         'description': 'Fresh strawberry', 'image': '🥤', 'popular': True},
        {'id': 36, 'name': 'Mango Shake', 'price': 70, 'category': 'Shakes', 
         'description': 'Sweet mango', 'image': '🥤', 'popular': True},
        {'id': 37, 'name': 'Oreo Shake', 'price': 80, 'category': 'Shakes', 
         'description': 'Oreo cookie', 'image': '🥤', 'popular': True},
        {'id': 38, 'name': 'Chocolate Shake', 'price': 70, 'category': 'Shakes', 
         'description': 'Rich chocolate', 'image': '🥤', 'popular': False},
        {'id': 39, 'name': 'Butter Scotch Shake', 'price': 80, 'category': 'Shakes', 
         'description': 'Butter scotch', 'image': '🥤', 'popular': False},
        {'id': 40, 'name': 'Special Shake', 'price': 90, 'category': 'Shakes', 
         'description': 'Premium shake', 'image': '🥤', 'popular': False},
        
        # COFFEE
        {'id': 41, 'name': 'Hot Coffee', 'price': 50, 'category': 'Coffee', 
         'description': 'Classic hot', 'image': '☕', 'popular': False},
        {'id': 42, 'name': 'Hot Chocolate Coffee', 'price': 70, 'category': 'Coffee', 
         'description': 'With chocolate', 'image': '☕', 'popular': True},
        {'id': 43, 'name': 'Cold Coffee', 'price': 80, 'category': 'Coffee', 
         'description': 'Ice cold', 'image': '☕', 'popular': True},
        
        # MOJITO
        {'id': 44, 'name': 'Mint Mojito', 'price': 80, 'category': 'Mojito', 
         'description': 'Fresh mint', 'image': '🍹', 'popular': True},
        {'id': 45, 'name': 'Green Apple Mojito', 'price': 90, 'category': 'Mojito', 
         'description': 'Green apple', 'image': '🍹', 'popular': False},
        {'id': 46, 'name': 'Blue Curacao Mojito', 'price': 100, 'category': 'Mojito', 
         'description': 'Blue curacao', 'image': '🍹', 'popular': False},
        
        # COMBOS
        {'id': 47, 'name': 'Burger Combo', 'price': 250, 'category': 'Combos', 
         'description': '2 Cheese Burger + Fries + 2 Coke', 'image': '🍔', 'popular': True},
        {'id': 48, 'name': 'Friends Veg Combo', 'price': 300, 'category': 'Combos', 
         'description': '2 Grilled Sandwich + 2 Parcel + Coke', 'image': '🥪', 'popular': True},
        {'id': 49, 'name': 'Pizza + 2 Shake Combo', 'price': 350, 'category': 'Combos', 
         'description': 'Medium Pizza + Mango + Strawberry Shake', 'image': '🍕', 'popular': True},
        {'id': 50, 'name': 'Large Pizza Mega Combo', 'price': 600, 'category': 'Combos', 
         'description': 'Large Pizza + 3 Burger + Garlic Bread + 2 Lava + 2 Coke', 'image': '🍕', 'popular': True},
    ]
    
    return render_template('menu.html', categories=categories, menu_items=menu_items)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    restaurant = {
        'phone': '85436xxxxx',
        'email': 'info@pizzawithspice.com',
        'address': 'Main Market Road, Mohali, Punjab',
        'hours': '9 AM - 11 PM'
    }
    return render_template('contact.html', restaurant=restaurant)

@app.route('/api/order', methods=['POST'])
def submit_order():
    data = request.json
    return jsonify({'success': True, 'order_id': datetime.now().strftime('%Y%m%d%H%M%S'), 'message': 'Order received! We will call you soon.'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
