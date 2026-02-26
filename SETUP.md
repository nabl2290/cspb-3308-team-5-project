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

The app will be available at `http://127.0.0.1:5000`.

## Deactivate the virtual environment

When you're done working on the project, you can deactivate the virtual environment by running:
```bash
deactivate
```

To reactivate it later, simply run the activation command again.
