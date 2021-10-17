# Star Wars Fan App

Simple app for experimenting with technologies and architecture patterns

## Getting Started

1. Install dependencies
   ```bash
   poetry install
   ```
1. Create .env from .env.example, set proper config values
1. Up required services
   ```bash
   docker-compose up -d
   ```
1. Run app
   ```bash
   poetry run uvicorn src.main:app --reload
   ```
1. Open app http://127.0.0.1:8000/

## TODO
- [x] Add settings
- [x] Add cache
- [ ] Add command
- [ ] Fix mypy errors
- [ ] Add flake8 and plugins