# Objective

This project is a simplified airline booking system developed using Django and Django Rest Framework (DRF). It provides a RESTful API for managing flights and passengers, allowing CRUD operations and additional features like filtering and pagination.

# Features

- Manage Flights:

Create, Read, Update, and Delete (CRUD) operations for flights.

- Manage Passengers:

CRUD operations for passengers, with each passenger linked to a flight.

- Relationships:

A flight can have multiple passengers.

A passenger is associated with exactly one flight.

Filtering passengers by flight.

Paginated list endpoints for flights and passengers.

# Setup Instructions

#   1. Clone the Repository

git clone <repository_url>
cd Simplified-Airline-Booking-System

#   2. Create and Activate a Virtual Environment

python3 -m venv airline_booking_env
source airline_booking_env/bin/activate

#   3. Install Dependencies

pip install -r requirements.txt

#   4. Apply Migrations

python manage.py makemigrations
python manage.py migrate

#   5. Run the Development Server
python manage.py runserver

Access the API at: http://127.0.0.1:8000/api/

# API Endpoints

#   Flights

- List all flights:

URL: /api/flights/

Method: GET

- Retrieve a flight by ID:

URL: /api/flights/<id>/

Method: GET

- Create a flight:

URL: /api/flights/

Method: POST

Body: { "flight_number": "AB123", "departure": "2024-12-25T10:00:00Z", "arrival": "2024-12-25T14:00:00Z", "origin": "New York", "destination": "London", "capacity": 200 }

- Update a flight:

URL: /api/flights/<id>/

Method: PUT

- Delete a flight:

URL: /api/flights/<id>/

Method: DELETE

# Passengers

- List all passengers:

URL: /api/passengers/

Method: GET

- Retrieve a passenger by ID:

URL: /api/passengers/<id>/

Method: GET

- Create a passenger:

URL: /api/passengers/

Method: POST

Body: { "first_name": "Jane", "last_name": "Doe", "email": "jane.doe@example.com", "phone_number": "1234567890", "flight": 1 }

- Update a passenger:

URL: /api/passengers/<id>/

Method: PUT

- Delete a passenger:

URL: /api/passengers/<id>/

Method: DELETE

- Filter passengers by flight number:

URL: /api/passengers/?search=<flight_number>

Method: GET

#  Design Details

# Models

Flight:

Represents a flight in the airline system with attributes like flight_number, departure, arrival, origin, destination, and capacity.

Passenger:

Represents a passenger with attributes like first_name, last_name, email, phone_number, and a foreign key flight to associate it with a specific flight.

#  Serializers

Used to convert Django models into JSON for the API and vice versa.

FlightSerializer: Handles serialization for Flight.

PassengerSerializer: Handles serialization for Passenger and includes details of the associated flight.

#  ViewSets

FlightViewSet: Provides CRUD operations for Flight.

PassengerViewSet: Provides CRUD operations for Passenger and supports filtering by flight.

#  Pagination

Enabled globally using Django Rest Framework's pagination settings, with a default page size of 10.

#  Filtering

Passengers can be filtered by flight_number using the search query parameter.

#  Deployment Instructions
1.pip install gunicorn

2.Install gunicorn for production:

3.pip install gunicorn

4.Configure a web server like Nginx to serve the application.

5.Collect static files:

python manage.py collectstatic

6.Run the application with Gunicorn:

gunicorn airline_system.wsgi:application

