#!/usr/bin/env python3
import re
from flask import request, jsonify
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from config import app, db
from models import User, Property, Visit, FavoriteProperty, Review
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

@app.route('/')
def index():
    return '<h1>Project Server</h1>'

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    # Validate username
    if not re.match(r'^\w+$', username):
        return jsonify({"error": "Username must contain only letters, numbers, and underscores."}), 400

    # Validate email
    if not re.match(r'^[^@]+@[^@]+\.[^@]+$', email):
        return jsonify({"error": "Invalid email address."}), 400

    # Validate password
    if len(password) < 8:
        return jsonify({"error": "Password must be at least 8 characters long."}), 400

    # Check if the username or email already exists
    if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
        return jsonify({"error": "Username or email already exists."}), 400

    new_user = User(username=username, email=email)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully!"}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if user is None or not user.check_password(password):
        return jsonify({"error": "Invalid username or password."}), 401

    access_token = create_access_token(identity={'id': user.id, 'username': user.username})
    return jsonify(access_token=access_token), 200

@app.route('/properties', methods=['POST', 'GET'])
##@jwt_required()
def manage_properties():
    if request.method == 'POST':
        data = request.get_json()
        new_property = Property(
            title=data['title'],
            description=data['description'],
            price=data['price'],
            address=data['address'],
            ##owner_id=get_jwt_identity()['id']
        )
        db.session.add(new_property)
        db.session.commit()
        return jsonify({"message": "Property created successfully!"}), 201
    else:
        properties = Property.query.all()
        return jsonify([property.to_dict() for property in properties]), 200

@app.route('/properties/<int:property_id>', methods=['GET', 'PUT', 'DELETE'])
##@jwt_required()
def manage_property(property_id):
    property = Property.query.get_or_404(property_id)
    if request.method == 'GET':
        return jsonify(property.to_dict()), 200
    elif request.method == 'PUT':
        data = request.get_json()
        property.title = data.get('title', property.title)
        property.description = data.get('description', property.description)
        property.price = data.get('price', property.price)
        property.address = data.get('address', property.address)
        db.session.commit()
        return jsonify({"message": "Property updated successfully!"}), 200
    elif request.method == 'DELETE':
        db.session.delete(property)
        db.session.commit()
        return jsonify({"message": "Property deleted successfully!"}), 200

@app.route('/visits', methods=['POST', 'GET'])
##@jwt_required()
def manage_visits():
    if request.method == 'POST':
        data = request.get_json()
        new_visit = Visit(
            user_id=get_jwt_identity()['id'],
            property_id=data['property_id'],
            scheduled_date=data['scheduled_date'],
            status='pending'
        )
        db.session.add(new_visit)
        db.session.commit()
        return jsonify({"message": "Visit scheduled successfully!"}), 201
    else:
        ##user_id = get_jwt_identity()['id']
        visits = Visit.query.filter_by(user_id=user_id).all()
        return jsonify([visit.to_dict() for visit in visits]), 200

@app.route('/favorites', methods=['POST', 'GET'])
##@jwt_required()
def manage_favorites():
    if request.method == 'POST':
        data = request.get_json()
        new_favorite = FavoriteProperty(user_id=get_jwt_identity()['id'], property_id=data['property_id'])
        db.session.add(new_favorite)
        db.session.commit()
        return jsonify({"message": "Property added to favorites"}), 201
    else:
        ##user_id = get_jwt_identity()['id']
        favorites = FavoriteProperty.query.filter_by(user_id=user_id).all()
        return jsonify([favorite.to_dict() for favorite in favorites]), 200

@app.route('/favorites/<int:favorite_id>', methods=['DELETE'])
##@jwt_required()
def delete_favorite(favorite_id):
    favorite = FavoriteProperty.query.get_or_404(favorite_id)
    db.session.delete(favorite)
    db.session.commit()
    return jsonify({"message": "Favorite removed successfully"}), 200

@app.route('/reviews', methods=['POST', 'GET'])
##@jwt_required()
def manage_reviews():
    if request.method == 'POST':
        data = request.get_json()
        new_review = Review(
            content=data['content'],
            rating=data['rating'],
            user_id=get_jwt_identity()['id'],
            property_id=data['property_id']
        )
        db.session.add(new_review)
        db.session.commit()
        return jsonify({"message": "Review added successfully"}), 201
    else:
        property_id = request.args.get('property_id')
        reviews = Review.query.filter_by(property_id=property_id).all()
        return jsonify([review.to_dict() for review in reviews]), 200

@app.route('/reviews/<int:review_id>', methods=['PUT', 'DELETE'])
##@jwt_required()
def manage_review(review_id):
    review = Review.query.get_or_404(review_id)
    if request.method == 'PUT':
        data = request.get_json()
        review.content = data.get('content', review.content)
        review.rating = data.get('rating', review.rating)
        db.session.commit()
        return jsonify({"message": "Review updated successfully"}), 200
    elif request.method == 'DELETE':
        db.session.delete(review)
        db.session.commit()
        return jsonify({"message": "Review deleted successfully"}), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(port=5555, debug=True)