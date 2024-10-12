
## Badges

Add badges from somewhere like: [shields.io](https://shields.io/)

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)Python Application

# Late Show API


This API allows interaction with a database of episodes, guests, and appearances. It provides functionality for retrieving information about episodes and guests, adding new appearances for guests in episodes, and deleting episodes.
## Features


Features
The Late Show API provides the following features:

Manage Episodes:

Retrieve a list of all episodes.
View details of individual episodes, including the date, episode number, and guest appearances.
Delete an episode by its unique ID.
Manage Guests:

Retrieve a list of all guests, including their names and occupations.
View details of individual guests in each episode through the appearance records.
Create Guest Appearances:

Add a guest's appearance in an episode, specifying the rating for their appearance.
Associate guest appearances with specific episodes and guests, creating many-to-many relationships between episodes and guests.
Data Validation:

Enforce a rating system between 1 and 5 for each appearance to ensure valid data.
Ensure relationships between episodes and guests are properly maintained through the Appearance model.
Postman Collection for Easy Testing:

The API comes with a Postman collection that allows for easy testing and verification of all endpoints. This collection can be imported into Postman for quick testing of features like listing episodes, guests, and creating appearances.
Database Seeding:

A provided seed script allows for easy population of the database with initial data for testing the API, including episodes and guests.
## Installation
1. Clone the Repository

git clone <https://github.com/abudhosamuel/lateshow>
cd <lateshow>
2. Set Up Virtual Environment and Install Dependencies
Ensure you have python3 and pip installed. Then, set up a virtual environment and install the dependencies:

pipenv install
pipenv shell


pip install -r requirements.txt

3. Configure Database
In app.py, you’ll find the configuration for the SQLite database. The database file will be automatically created when running migrations.

Database Setup
1. Initialize Database
You will need to set up the database and apply migrations:

flask db init
flask db migrate
flask db upgrade

This will create the necessary tables for the episodes, guests, and appearances models.

Seeding the Database
After setting up the database, you can seed it with some initial data (episodes and guests) using the seed.py script:

python seed.py
This will populate the database with initial episodes and guests for testing purposes.
## Running Tests


Run the Flask application using the following command:

flask run
By default, the application will run on http://127.0.0.1:5000/.

API Endpoints

GET /episodes
Description: Fetches a list of all episodes.
Method: GET
URL: /episodes
Response Example:

[
  {
    "id": 1,
    "date": "1/11/99",
    "number": 1
  },
  {
    "id": 2,
    "date": "1/12/99",
    "number": 2
  }
]
GET /episodes/
Description: Fetches details of a specific episode by its ID.
Method: GET
URL: /episodes/:id
Response Example:

{
  "id": 1,
  "date": "1/11/99",
  "number": 1,
  "appearances": [
    {
      "episode_id": 1,
      "guest": {
        "id": 1,
        "name": "Michael J. Fox",
        "occupation": "actor"
      },
      "guest_id": 1,
      "id": 1,
      "rating": 5
    }
  ]
}
GET /guests
Description: Fetches a list of all guests.
Method: GET
URL: /guests
Response Example:

[
  {
    "id": 1,
    "name": "Michael J. Fox",
    "occupation": "actor"
  },
  {
    "id": 2,
    "name": "Sandra Bernhard",
    "occupation": "Comedian"
  }
]
POST /appearances
Description: Creates a new appearance of a guest in an episode.
Method: POST
URL: /appearances
Request Body:

{
  "rating": 5,
  "episode_id": 2,
  "guest_id": 3
}
Response Example:

{
  "id": 1,
  "rating": 5,
  "guest_id": 3,
  "episode_id": 2,
  "episode": {
    "id": 2,
    "date": "1/12/99",
    "number": 2
  },
  "guest": {
    "id": 3,
    "name": "Tracey Ullman",
    "occupation": "television actress"
  }
}
DELETE /episodes/
Description: Deletes an episode by its ID.
Method: DELETE
URL: /episodes/:id
Response Example:

{
  "message": "Episode deleted successfully"
}
Testing the API
You can test the API using tools like Postman or cURL. Here’s how you can use cURL to test the POST /appearances endpoint:


Using Postman
Open Postman.
Import the provided Postman collection (challenge-4-lateshow.postman_collection.json).
Test the available endpoints.


## Authors

- [@abudhosamuel](https://www.github.com/abudhosamuel)




## License

[MIT](https://choosealicense.com/licenses/mit/)


## Acknowledgements

Acknowledgements

Font Awesome
Feel free to contribute to the project by submitting a pull request or opening an issue.

