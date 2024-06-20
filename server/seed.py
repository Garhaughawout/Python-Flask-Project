from config import app, db
from models import User, Property, Visit, FavoriteProperty, Review
from datetime import datetime
from faker import Faker

faker = Faker()

with app.app_context():
    
    User.query.delete()
    Property.query.delete()
    Visit.query.delete()
    FavoriteProperty.query.delete()
    Review.query.delete()
    
    db.create_all()

    # Create users
    users = []
    for i in range(5):
        user = User(
            username=faker.user_name(),
            email=faker.email()
        )
        user.set_password('password123')
        db.session.add(user)
        users.append(user)
        print(f"User {i+1}: {user.username} created")

    db.session.commit()

    # Create properties
    properties = []
    for user in users:
        for i in range(2):
            property = Property(
                title=faker.sentence(nb_words=3),
                description=faker.text(),
                price=faker.random_number(digits=5),
                address=faker.address(),
                owner_id=user.id
            )
            db.session.add(property)
            properties.append(property)
            print(f"Property {property.title} for user {user.username} created")

    db.session.commit()

    # Create visits
    for i in range(10):
        visit = Visit(
            user_id=faker.random_element(users).id,
            property_id=faker.random_element(properties).id,
            scheduled_date=faker.future_datetime(end_date='+30d'),
            status='pending'
        )
        db.session.add(visit)
        print(f"Visit {i+1} scheduled for property {visit.property_id}")

    db.session.commit()

    # Create favorite properties
    for user in users:
        for i in range(3):
            favorite_property = FavoriteProperty(
                user_id=user.id,
                property_id=faker.random_element(properties).id,
                added_at=datetime.now()
            )
            db.session.add(favorite_property)
            print(f"Favorite property {favorite_property.property_id} added for user {user.username}")

    db.session.commit()

    # Create reviews
    for property in properties:
        for i in range(3):
            review = Review(
                content=faker.text(),
                rating=faker.random_int(min=1, max=5),
                user_id=faker.random_element(users).id,
                property_id=property.id,
                created_at=datetime.now()
            )
            db.session.add(review)
            print(f"Review {i+1} for property {property.title} by user {review.user_id} created")

    db.session.commit()

    print("Database seeded successfully.")
