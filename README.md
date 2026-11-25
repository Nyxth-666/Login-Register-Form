# Login-Register-Form

A simple authentication website built with **Django**, **SQLite**, and **Tailwind CSS**. It has three pages: Login, Register, and a Login Success page that confirms the user is signed in.

## Features

- Register with first name, last name, email, and password
- Login with email and password (email is used as the username)
- Password rules: at least 8 characters, with a number and a symbol
- Duplicate email check and password confirmation
- Success page, protected so only logged-in users can see it
- Logout
- Show/hide password toggle
- Responsive split-screen design (artwork on the left, form on the right)
- "Log in with Google" button (design only, no functionality yet)

## Tech Stack

| Tool | Purpose |
| --- | --- |
| Django | Backend, auth, forms, templates |
| SQLite | Database (Django default) |
| Tailwind CSS (via `pytailwindcss`) | Styling, no Node.js needed |
| python-decouple | Loads settings from `.env` |

## Project Structure

```
Login-Register-Form/
├── config/               # Project settings and root URLs
├── accounts/             # Auth app (views, forms, urls)
├── templates/
│   ├── base.html
│   └── accounts/
│       ├── _tabs.html
│       ├── _field.html
│       ├── _google_button.html
│       ├── login.html
│       ├── register.html
│       └── success.html
├── static/
│   ├── images/auth-bg.png
│   └── src/input.css     # Tailwind input file
├── .env                  # Local settings (not committed)
├── requirements.txt
└── manage.py
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Nyxth-666/Login-Register-Form.git
cd Login-Register-Form
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create the `.env` file

Create a `.env` file next to `manage.py`:

```dotenv
SECRET_KEY='your-secret-key-here'
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

Generate a secret key with:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 5. Set up the database

```bash
python manage.py migrate
```

### 6. Build Tailwind CSS

In a separate terminal, leave this running while you develop:

```bash
tailwindcss -i static/src/input.css -o static/css/output.css --watch
```

### 7. Run the server

```bash
python manage.py runserver
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Pages

| URL | Page |
| --- | --- |
| `/` | Login |
| `/register/` | Register |
| `/success/` | Login success (requires login) |
| `/logout/` | Logout (POST) |

## Environment Variables

| Variable | Description |
| --- | --- |
| `SECRET_KEY` | Django secret key (required) |
| `DEBUG` | `True` for development, `False` for production |
| `ALLOWED_HOSTS` | Comma-separated hosts, e.g. `yourdomain.com,www.yourdomain.com` |

## Notes

- Never commit `.env` or `db.sqlite3`. Both are in `.gitignore`.
- For production, set `DEBUG=False`, set `ALLOWED_HOSTS`, and use a new secret key.
- The Google button is a visual placeholder. Google sign-in is not implemented.

## Author

**Joshua** ([@Nyxth-666](https://github.com/Nyxth-666))