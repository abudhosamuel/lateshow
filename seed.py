# seed.py
from app import db, Guest, Episode, app  # Import the necessary models and the app

def seed_data():
    # Push the application context to allow interaction with the database
    with app.app_context():
        # Seed Episodes
        episodes_data = [
            {'id': 1, 'date': '1/11/99', 'number': 1},
            {'id': 2, 'date': '1/12/99', 'number': 2},
        ]

        for ep in episodes_data:
            episode = Episode(id=ep['id'], date=ep['date'], number=ep['number'])
            db.session.add(episode)

        # Seed Guests
        guests_data = [
            {'id': 1, 'name': 'Michael J. Fox', 'occupation': 'actor'},
            {'id': 2, 'name': 'Sandra Bernhard', 'occupation': 'Comedian'},
            {'id': 3, 'name': 'Tracey Ullman', 'occupation': 'television actress'},
        ]

        for g in guests_data:
            guest = Guest(id=g['id'], name=g['name'], occupation=g['occupation'])
            db.session.add(guest)

        # Commit the changes to the database
        db.session.commit()
        print("Database seeded successfully.")

if __name__ == '__main__':
    seed_data()
