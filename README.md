# Star Wars Fan App

Simple app for experimenting with technologies and architecture patterns

## Getting Started

1. Install dependencies
    ```bash
    poetry install
    ```
2. Create .env from .env.example, set proper config values
3. Up required services
    ```bash
    docker-compose up -d
    ```
4. Run app
    ```bash
    poetry run uvicorn src.main:app --reload
    ```
6. Open app http://127.0.0.1:8000/

## TODO
- [x] Add settings
- [x] Add cache
- [ ] Add command
- [x] Fix mypy errors
- [ ] Add flake8 and plugins