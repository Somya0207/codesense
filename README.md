# CodeSense — AI-Powered Python Code Analyzer

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Tests](https://img.shields.io/badge/Tests-12%20passing-brightgreen)
![FastAPI](https://img.shields.io/badge/FastAPI-0.136-green)

CodeSense is a command-line tool and REST API that analyzes Python files,
scores the complexity of every function, and tracks analysis history in a
database. Built from scratch to demonstrate real-world Python engineering.

## Features

- Analyzes any Python file using Python's built-in `ast` module
- Scores every function using cyclomatic complexity (the same metric used by Google and Microsoft)
- Color-coded terminal output — green, yellow, red
- Saves every analysis to a SQLite database automatically
- View full history of past analyses
- REST API built with FastAPI — test it in your browser
- 12 automated tests covering all core modules

## Installation

```bash
# Clone the repository
git clone https://github.com/Somya0207/codesense
cd codesense

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate       # Windows
source venv/bin/activate    # Mac/Linux

# Install dependencies
pip install -r requirements.txt
```

## Usage

### Analyze a Python file
```bash
python main.py analyze yourfile.py
```

### View analysis history
```bash
python main.py history
```

### Run the REST API
```bash
uvicorn api.server:app --reload
# Open http://127.0.0.1:8000/docs in your browser
```

### Run all tests
```bash
pytest tests/ -v
```

## Example Output

```
╭──────────────────────────────╮
│ CodeSense v0.1.0             │
│ AI Code Reviewer             │
╰──────────────────────────────╯

Analyzing test_sample.py...

Results for test_sample.py
┌─────────────────┬──────┬───────┬─────────┐
│ Function        │ Line │ Score │ Health  │
├─────────────────┼──────┼───────┼─────────┤
│ simple()        │ 1    │ 1     │ good    │
│ medium()        │ 5    │ 4     │ good    │
│ complex_func()  │ 17   │ 7     │ good    │
└─────────────────┴──────┴───────┴─────────┘
✓ Saved to history — 3 functions, 0 warnings
```

## Project Structure

```
codesense/
├── core/
│   ├── models.py       # Data shapes — Issue and FunctionReport dataclasses
│   ├── analyzer.py     # AST-based function finder
│   └── complexity.py   # Cyclomatic complexity scorer
├── cli/
│   └── scanner.py      # Glue connecting analyzer and complexity
├── api/
│   └── server.py       # FastAPI REST API
├── storage/
│   └── database.py     # SQLAlchemy ORM — SQLite database
├── tests/
│   ├── test_models.py      # 5 tests
│   ├── test_complexity.py  # 3 tests
│   └── test_scanner.py     # 4 tests
├── main.py             # Entry point and CLI
├── config.py           # Central settings
└── conftest.py         # pytest configuration
```

## Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.12 | Core language |
| ast module | Parse Python code into syntax trees |
| SQLAlchemy | ORM for SQLite database |
| FastAPI | REST API framework |
| Rich | Beautiful terminal output |
| pytest | Automated testing |

## Concepts Demonstrated

- Abstract Syntax Tree (AST) parsing
- Object-Oriented Programming and inheritance
- Dataclasses and type hints
- SQLAlchemy ORM with SQLite
- REST API design with FastAPI and Pydantic
- Automated testing with pytest
- CLI design with sys.argv
- Environment configuration with python-dotenv