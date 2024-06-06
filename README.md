# EmpContact

## Frontend with Vite and React

1. **Create Vite React App**:
   ```sh
   $ npm create vite@latest client -- --template react
   ```

2. **Navigate to Project Directory**:
   ```sh
   $ cd client
   ```

3. **Install Dependencies**:
   ```sh
   $ npm install
   ```

4. **Run Development Server**:
   ```sh
   $ npm run dev
   ```

### Additional Notes:

- Ensure you have Node.js installed. You can download it from [Node.js official site](https://nodejs.org/).
- Vite is a build tool that provides a faster and leaner development experience for modern web projects.

## Backend with Flask

1. **Install Pipenv** (if you don't have it installed):
   ```sh
   $ pip install pipenv
   ```

2. **Create a Pipenv Environment** and Install Flask:
   ```sh
   $ pipenv install Flask
   ```

3. **Install Flask-SQLAlchemy** for Database Management:
   ```sh
   $ pipenv install Flask-SQLAlchemy
   ```

4. **Install Flask-CORS** to Handle Cross-Origin Requests:
   ```sh
   $ pipenv install flask-cors
   ```

### Project Structure

```
project-root/
│
├── client/               # Vite React frontend
│   ├── node_modules/
│   ├── public/
│   ├── src/
│   ├── .gitignore
│   ├── index.html
│   ├── package.json
│   ├── README.md
│   ├── vite.config.js
│   └── ...
│
├── server/               # Flask backend
│   ├── venv/             # Virtual environment
│   ├── app.py            # Main application file
│   ├── config.py         # Configuration file
│   ├── models.py         # Database models
│   ├── routes.py         # API routes
│   ├── .flaskenv         # Environment variables
│   ├── Pipfile           # Pipenv file
│   ├── Pipfile.lock      # Pipenv lock file
│   └── ...
│
├── README.md
└── ...
```

### Running the Backend

1. **Activate the Pipenv Shell**:
   ```sh
   $ pipenv shell
   ```

2. **Run the Flask Application**:
   ```sh
   $ flask run
   ```

### Additional Notes:

- Ensure you have Python installed. You can download it from [Python official site](https://www.python.org/).
- Flask-SQLAlchemy is an extension for Flask that adds support for SQLAlchemy, which is an ORM (Object Relational Mapper).
- Flask-CORS allows your Flask application to handle Cross-Origin Resource Sharing (CORS), which is necessary if your frontend and backend are on different domains or ports.

### Common Issues and Troubleshooting

- **CORS Errors**: If you encounter CORS errors, ensure that Flask-CORS is correctly configured in your Flask app.
- **Environment Activation**: If you have trouble activating the pipenv environment, ensure that pipenv is installed and properly set up.

### CRUD Operations Overview

- **Create**: To add a new employee contact, send a `POST` request to `/api/contacts` with the contact details.
- **Read**: To retrieve employee contacts, send a `GET` request to `/api/contacts` to get all contacts or `/api/contacts/<id>` for a specific contact.
- **Update**: To update an employee contact, send a `PUT` request to `/api/contacts/<id>` with the updated contact details.
- **Delete**: To delete an employee contact, send a `DELETE` request to `/api/contacts/<id>`.

