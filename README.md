## License

This project is licensed under the [MIT License](LICENSE).

# Full stack web application with Flask and MariaDB

This project is a full stack web application that uses Flask on the backend with a MariaDB database and a static frontend built with HTML, CSS, and JavaScript. The backend exposes a RESTful API that is consumed by the frontend to interact with the database data.

## Description

The application was created to demonstrate how to build a backend server with Flask, connect to a MariaDB database, and integrate it with a static frontend. Communication between the frontend and backend happens through an API, which can be accessed from a browser or other client applications.

## Technologies Used

- **Backend**: Flask (Python)
- **Database**: MariaDB
- **Frontend**: HTML, CSS, JavaScript
- **Local Server**: To run the frontend locally and consume the API

## How to Run the Project Locally

### 1. Clone the Repository

```bash
git clone https://github.com/BernardoAlvesdeOliveira/app-web-full-stack.git
cd app-web-full-stack
```

### 2. Install Backend Dependencies

First, install the Python dependencies:

```bash
pip install -r backend/requirements.txt
```

### 3. Configure the MariaDB Database

1. Make sure MariaDB is installed and running.
2. Create a database and a table with the required columns for the application.
3. Import the database initialization script:

```bash
mysql -u root -p < database/init.sql
```

### 4. Run the Backend Server (Flask API)

To run the Flask server locally, execute the following command in the project root:

```bash
python backend/app.py
```

The server will start on port `5001` by default.

### 5. Run the Frontend Locally

To run the frontend locally, you can use a simple static server. An example using `http-server` (Node.js):

1. Install `http-server` globally:

```bash
npm install -g http-server
```

2. Navigate to the `frontend/` folder and start the server:

```bash
cd frontend
http-server
```

The server will start on port `8000` by default.

### 6. Test the Application

Now you can access the frontend at `http://localhost:8000` and test its integration with the backend running at `http://localhost:5001`.

## Features

- **RESTful API**: The backend provides endpoints to interact with the database.
- **Frontend**: The frontend consumes the API to display and manipulate data.
