


                                     
                                        GitHub repository: holbertonschool-web_back_end
                                              Directory: Session_authentication


Session Authentication Project

This repository contains the Session Authentication version of the API originally built in the 0x06 Basic Authentication project. It extends the Basic Authentication system by adding a convenient endpoint to retrieve the currently authenticated user.

📂 Repository Structure

Session_authentication/
├── api/
│   └── v1/
│       ├── app.py
│       └── views/
│           └── users.py
├── models/
│   └── user.py  (copied from 0x06 Basic Authentication)
└── requirements.txt

models/: contains the User model and storage logic.

api/v1/app.py: Flask application setup, request hooks, and error handlers.

api/v1/views/users.py: RESTful user routes, including the new /users/me endpoint.

requirements.txt: Python dependencies.

🔐 Authentication Flow

All /api/v1/users* routes are protected by Basic Authentication:

Client sends HTTP header:

Authorization: Basic <base64(email:password)>

The BasicAuth class in app.py validates credentials:

Missing header → 401 Unauthorized

Invalid credentials → 403 Forbidden

Success → request.current_user is set to the corresponding User instance

📖 API Endpoints

Health Check

GET /api/v1/status

Response: 200 OK with { "status": "OK" }

List All Users

GET /api/v1/users

Auth: Basic

Response: 200 OK with JSON array of all users

Create a New User

POST /api/v1/users
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "Secretpwd",
  "first_name": "John",
  "last_name": "Doe"
}

Auth: Basic

Response: 201 Created with the new user object

Get User by ID

GET /api/v1/users/<user_id>

Auth: Basic

Response: 200 OK with the user object, or 404 Not found

Update an Existing User

PUT /api/v1/users/<user_id>
Content-Type: application/json

{
  "first_name": "NewName",
  "last_name": "NewLast"
}

Auth: Basic

Response: 200 OK with the updated user object, or 404 Not found

Delete a User

DELETE /api/v1/users/<user_id>

Auth: Basic

Response: 200 OK with empty body, or 404 Not found

Get Authenticated User (“me”)

GET /api/v1/users/me

Auth: Basic

Response:

200 OK with the JSON of the authenticated user

404 Not found if no valid user is attached

🚀 Installation & Running

Clone the repo

git clone https://github.com/YOUR_USERNAME/holbertonschool-web_back_end.git
cd holbertonschool-web_back_end/Session_authentication

Create a virtual environment (recommended)

python3 -m venv venv
source venv/bin/activate

Install dependencies

pip install -r requirements.txt

Set environment variables

export API_HOST=0.0.0.0
export API_PORT=5000
export AUTH_TYPE=basic_auth

Start the server

python3 -m api.v1.app

The API will be available at http://$API_HOST:$API_PORT.

📋 Testing the /users/me Endpoint

Create a test user (example script provided in main_0.py)

Retrieve the Base64 credential

Call the new endpoint

curl "http://0.0.0.0:5000/api/v1/users/me" \
  -H "Authorization: Basic <BASE64_CREDENTIALS>"

You should receive the JSON representation of the authenticated user.
