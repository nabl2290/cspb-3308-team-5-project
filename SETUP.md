# Setting up the Project

## Prerequisites
- Python 3.x installed on your machine

## Setup

1. **Clone the repository**
   ```bash
   git clone git@github.com:nabl2290/cspb-3308-team-5-project.git
   cd cspb-3308-team-5-project
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment**

   macOS/Linux:
   ```bash
   source .venv/bin/activate
   ```
   Windows:
   ```bash
   .venv\Scripts\activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the app**
   ```bash
   flask run
   ```

   For development with auto-reload and seed data:
   ```bash
   FLASK_ENV=development flask run --debug
   ```

The app will be available at `http://127.0.0.1:5000`.

## Database

This app uses SQLite with the Flask SQL-Alchemy extension. The database will be created automatically on first run.

### Dev Seeds

When `FLASK_ENV=development` is set, the app will automatically load sample data on first run (users, children, and feeding events). Seeds only run if the database is empty, so they won't duplicate on restart.

To reset the database and re-run seeds, delete the database file and restart:
```bash
rm instance/database.db
FLASK_ENV=development flask run --debug
```

Or if you don't want to type `FLASK_ENV=development` every time, add a `.env` with the following content:
```
FLASK_ENV=development
```

and simply run:
```bash
flask run --debug
```

See Flask SQL-Alchemy documentation for more details on how to manage the database: https://flask-sqlalchemy.readthedocs.io/en/stable/

## Deactivate the virtual environment

When you're done working on the project, you can deactivate the virtual environment by running:
```bash
deactivate
```

To reactivate it later, simply run the activation command again.

## Adding new dependencies

If you add new dependencies to the project, make sure to update the `requirements.txt`. 

Make sure your virtual environment is activated, install dependencies using pip, and then run the following command to update `requirements.txt`:

```bash
pip freeze > requirements.txt
```

## Testing

To run tests, make sure your virtual environment is activated and run:
```bash
pytest tests/ -v  
```
