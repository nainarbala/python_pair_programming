# Python Pair Programming

A simple Flask API for calculating simple interest, organized with separate business logic, validation, and Swagger documentation.

## Project structure

- `app.py` — Flask application entrypoint and HTTP routes
- `simple_interest/` — package containing calculator logic, input validation, and OpenAPI documentation generation
  - `calculator.py`
  - `validation.py`
  - `swagger.py`
- `requirements.txt` — runtime and test dependencies
- `test_app.py` — Flask endpoint tests
- `test_simple_interest.py` — package unit tests for calculation and validation

## API endpoints

- `POST /simple-interest`
  - Accepts JSON `{ "principal": number, "rate": number, "time": number }`
  - Returns calculated `simple_interest`
- `GET /openapi.json`
  - Returns the OpenAPI spec for the API
- `GET /docs`
  - Serves a minimal Swagger UI for the API

## Run the application

Activate the virtual environment and start the app:

```bash
source .venv/bin/activate
python app.py
```

Open the docs in the browser:

- `http://127.0.0.1:5000/docs`
- `http://127.0.0.1:5000/openapi.json`

## Example request

```bash
curl -X POST http://127.0.0.1:5000/simple-interest \
  -H "Content-Type: application/json" \
  -d '{"principal": 1000, "rate": 5, "time": 2}'
```

Expected response:

```json
{
  "principal": 1000.0,
  "rate": 5.0,
  "time": 2.0,
  "simple_interest": 100.0
}
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Run tests

```bash
pytest
```
