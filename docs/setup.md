# Setup

## Requirements
- Python 3.12+

## Local install
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Demo data
```bash
python manage.py loaddata fixtures/demo_data.json
```
