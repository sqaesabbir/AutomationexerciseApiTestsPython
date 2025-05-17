# API Testing Framework with Python, Pytest and Playwright

This project contains automated API tests for the Automation Exercise API endpoints using Python, Pytest and Playwright.

## Setup

1. Clone the repository
2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running Tests

To run all tests:
```bash
pytest
```

To run tests with HTML report:
```bash
pytest --html=report.html
```

## Project Structure

- `tests/` - Contains all test files
- `config/` - Configuration files and constants
- `utils/` - Utility functions and helper classes
- `requirements.txt` - Project dependencies 