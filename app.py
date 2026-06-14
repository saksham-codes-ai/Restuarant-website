from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    restaurant = {
        'name': 'Royal Spice',
        'tagline': 'Experience Authentic Flavors',
        'phone': '+91 98765 43210',
        'email': 'info@royalspice.com',
        'address': 'Main Market Road, Mohali, Punjab',
        'hours': '10:00 AM - 11:00 PM',
        'stats': [
            {'number': '5000+', 'label': 'Happy Customers'},
            {'number': '50+', 'label': 'Menu Items'},
            {'number': '10+', 'label': 'Years Experience'},
            {'number': '98%', 'label': 'Positive Reviews'}
        ]
    }
    return render_template('home.html', restaurant=restaurant)

# Menu page
@app.route('/menu')
def menu():
    categories = ['All', 'Main Course', 'Rice', 'Chinese', 'Fast Food', 'Drink', 'Healthy']
    menu_items = [
        {'id': 1, 'name': 'Butter Chicken', 'price': 280, 'category': 'Main Course', 
         'description': 'Tender chicken in creamy tomato sauce', 'image': '🍗', 'popular': True},
        {'id': 2, 'name': 'Paneer Tikka', 'price': 220, 'category': 'Main Course', 
         'description': 'Cottage cheese grilled with spices', 'image': '🧀', 'popular': True},
        {'id': 3, 'name': 'Chicken Biryani', 'price': 180, 'category': 'Rice', 
         'description': 'Aromatic rice with spiced chicken', 'image': '🍚', 'popular': False},
        {'id': 4, 'name': 'Veg Fried Rice', 'price': 150, 'category': 'Rice', 
         'description': 'Fresh rice with vegetables', 'image': '🍳', 'popular': False},
        {'id': 5, 'name': 'Hakka Noodles', 'price': 130, 'category': 'Chinese', 
         'description': 'Stir-fried noodles with veggies', 'image': '🍜', 'popular': True},
        {'id': 6, 'name': 'Cheese Burger', 'price': 120, 'category': 'Fast Food', 
         'description': 'Grilled veg burger with cheese', 'image': '🍔', 'popular': False},
        {'id': 7, 'name': 'Veg Pizza', 'price': 200, 'category': 'Fast Food', 
         'description': 'Fresh vegetables on crispy base', 'image': '🍕', 'popular': True},
        {'id': 8, 'name': 'Iced Coffee', 'price': 60, 'category': 'Drink', 
         'description': 'Cold coffee with ice cream', 'image': '☕', 'popular': False},
        {'id': 9, 'name': 'Mango Lassi', 'price': 70, 'category': 'Drink', 
         'description': 'Sweet mango yogurt drink', 'image': '🥤', 'popular': True},
        {'id': 10, 'name': 'Green Salad', 'price': 80, 'category': 'Healthy', 
         'description': 'Fresh seasonal vegetables', 'image': '🥗', 'popular': False}
    ]
    return render_template('menu.html', categories=categories, menu_items=menu_items)

# About page
@app.route('/about')
def about():
    return render_template('about.html')

# Contact page
@app.route('/contact')
def contact():
    restaurant = {
        'phone': '+91 98765 43210',
        'email': 'info@royalspice.com',
        'address': 'Main Market Road, Mohali, Punjab',
        'hours': '10:00 AM - 11:00 PM'
    }
    return render_template('contact.html', restaurant=restaurant)

# Order API
@app.route('/api/order', methods=['POST'])
def submit_order():
    data = request.json
    order = {
        'id': datetime.now().strftime('%Y%m%d%H%M%S'),
        'name': data['name'],
        'phone': data['phone'],
        'items': data['items'],
        'total': data['total'],
        'time': datetime.now().strftime('%H:%M %d/%m/%Y'),
        'status': 'Received'
    }
    return jsonify({'success': True, 'order_id': order['id'], 'message': 'Order received! We will call you soon.'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
