# CLAUDE.md

## Project

Backend API built with Django and Django REST Framework.

## Stack

- Python
- Django
- Django REST Framework
- PostgreSQL
- pytest
- drf-spectacular

## Project Structure

- `core/` - shared/domain models
- `stock/` - stock API
- `stock/serializers.py` - API serializers
- `stock/views.py` - API views/viewsets
- `stock/services.py` - business logic
- `tests/` - tests

## Commands

Run tests:

    pytest

Run a specific test:

    pytest path/to/test.py -q

Run Django checks:

    python manage.py check

## Architecture

- Keep ViewSets thin.
- Keep business logic out of serializers and views when it is reusable or complex.
- Prefer service classes for business operations.
- Serializers are responsible for validation and representation.
- Views/ViewSets coordinate HTTP/API behavior.
- Models should contain domain behavior directly related to the model.
- Do not create unnecessary abstraction.

## API

- Use DRF serializers for input validation.
- Use `drf-spectacular` for OpenAPI documentation.
- Keep API responses consistent with existing endpoints.
- Follow existing authentication and permission patterns.

## Testing

- Add or update tests when changing behavior.
- Do not modify a test simply to make it pass.
- Test business logic independently when it lives in a service.
- Prefer focused tests over large integration tests when appropriate.

## Database

- Never modify existing migrations that may already have been applied.
- Create a new migration for schema changes.
- Check existing models and migrations before changing the database.

## Code Style

- Follow the existing project style.
- Prefer simple, readable Python.
- Do not introduce dependencies unless necessary.
- Do not refactor unrelated code while fixing a specific issue.

## Workflow

Before changing code:

1. Inspect the relevant files.
2. Understand existing patterns.
3. Identify the smallest appropriate change.
4. Implement the change.
5. Run the relevant tests.
6. Review the final diff.

## Important

Do not claim a task is complete unless the relevant tests/checks have actually been run.

If something is unclear, inspect the repository before making assumptions.
