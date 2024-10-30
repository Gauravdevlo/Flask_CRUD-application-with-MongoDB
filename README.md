# Flask_CRUD-application-with-MongoDB
This project is a Flask application that performs CRUD (Create, Read, Update, Delete) operations on a MongoDB database for a User resource using a REST API.

## Features
- Create, read, update, and delete user records.
- Data validation for user input.
- Uses MongoDB as the database.
- Provides a RESTful API for user management.

## Technologies Used
- Flask: A micro web framework for Python.
- Flask-PyMongo: A Flask extension for working with MongoDB.
- MongoDB Atlas: A cloud-based MongoDB database.
- Docker: For containerization.

## Setup Instructions

### Prerequisites
- Python 3.9 or higher
- Docker
- An active MongoDB Atlas account and a database created

### Clone the Repository
`git clone https://github.com/Gauravdevlo/your-repository.git
cd your-repository `

### Create a Virtual Environment

`python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate`

###Install Dependencies
Make sure you have requirements.txt in the root directory. Install the dependencies:
`pip install -r requirements.txt`

###Set Up Environment Variables
Create a .env file in the root directory of your project and add the following:
`MONGO_URI="mongodb+srv://<username>:<password>@cluster0.l8zlb.mongodb.net/flask_mongo_crud?retryWrites=true&w=majority"`

###Docker Setup 
If you prefer to run the application using Docker, make sure you have Docker installed and run:
`docker build -t flask-mongo-crud 
docker run -p 5000:5000 flask-mongo-crud`

###Running the Application
To run the application locally, execute:
`python run.py`

## API Endpoints

### Users API

#### Create User
- **Endpoint:** `POST /api/users`
- This endpoint is used to create a new user. The request must include the user's name, email, and password.

#### Get All Users
- **Endpoint:** `GET /api/users`
- This endpoint retrieves a list of all users in the database.

#### Get User by ID
- **Endpoint:** `GET /api/users/<id>`
- This endpoint retrieves the details of a specific user based on the provided user ID.

#### Update User
- **Endpoint:** `PUT /api/users/<id>`
- This endpoint updates the information of a specific user identified by their ID. The request must include the updated user details.

#### Delete User
- **Endpoint:** `DELETE /api/users/<id>`
- This endpoint deletes a specific user from the database based on the provided user ID.

## Testing with Postman
1. Open Postman and set the request method (GET, POST, PUT, DELETE) according to the endpoint you want to test.
2. Set the URL to http://127.0.0.1:5000/api/users.
3. For POST and PUT requests, add the appropriate JSON body in the Body tab and set the content type to application/json.
4. Send the request and observe the responses.


