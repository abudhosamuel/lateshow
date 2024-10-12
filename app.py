from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.orm import validates

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///episodes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Models
class Episode(db.Model):
    __tablename__ = 'episodes'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String, nullable=False)
    number = db.Column(db.Integer, nullable=False)
    appearances = db.relationship('Appearance', backref='episode', cascade="all, delete-orphan")

class Guest(db.Model):
    __tablename__ = 'guests'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    occupation = db.Column(db.String, nullable=False)
    appearances = db.relationship('Appearance', backref='guest', cascade="all, delete-orphan")

class Appearance(db.Model):
    __tablename__ = 'appearances'
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id'), nullable=False)
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'), nullable=False)

    @validates('rating')
    def validate_rating(self, key, rating):
        if rating < 1 or rating > 5:
            raise ValueError("Rating must be between 1 and 5.")
        return rating

# Routes

# GET /episodes
@app.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([{'id': e.id, 'date': e.date, 'number': e.number} for e in episodes])

# GET /episodes/<id>
@app.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    print(f"Fetching Episode with ID: {id}")  # Debugging line
    episode = Episode.query.get(id)
    if episode:
        print(f"Found Episode: {episode}")  # Debugging line
        appearances = [
            {
                'id': a.id,
                'episode_id': a.episode_id,
                'guest_id': a.guest_id,
                'rating': a.rating,
                'guest': {
                    'id': a.guest.id,
                    'name': a.guest.name,
                    'occupation': a.guest.occupation
                }
            }
            for a in episode.appearances
        ]
        return jsonify({
            'id': episode.id,
            'date': episode.date,
            'number': episode.number,
            'appearances': appearances
        })
    print("Episode not found.")  # Debugging line
    return jsonify({'error': 'Episode not found'}), 404

# GET /guests
@app.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    return jsonify([{'id': g.id, 'name': g.name, 'occupation': g.occupation} for g in guests])

# POST /appearances
@app.route('/appearances', methods=['POST'])
def create_appearance():
    data = request.get_json()
    try:
        rating = data['rating']
        episode_id = data['episode_id']
        guest_id = data['guest_id']
        
        print(f"Creating Appearance with rating: {rating}, episode_id: {episode_id}, guest_id: {guest_id}")  # Debugging line
        
        episode = Episode.query.get(episode_id)
        guest = Guest.query.get(guest_id)
        
        if not episode or not guest:
            print("Invalid episode_id or guest_id.")  # Debugging line
            return jsonify({'error': 'Invalid episode_id or guest_id'}), 404

        appearance = Appearance(rating=rating, episode_id=episode_id, guest_id=guest_id)
        db.session.add(appearance)
        db.session.commit()
        
        return jsonify({
            'id': appearance.id,
            'rating': appearance.rating,
            'guest_id': appearance.guest_id,
            'episode_id': appearance.episode_id,
            'episode': {
                'id': episode.id,
                'date': episode.date,
                'number': episode.number
            },
            'guest': {
                'id': guest.id,
                'name': guest.name,
                'occupation': guest.occupation
            }
        })
    except ValueError as e:
        print(f"Validation error: {e}")  # Debugging line
        return jsonify({'errors': [str(e)]}), 400
    except Exception as e:
        print(f"Unexpected error: {e}")  # Debugging line
        return jsonify({'errors': ['An unexpected error occurred']}), 500

if __name__ == '__main__':
    app.run(debug=True)
