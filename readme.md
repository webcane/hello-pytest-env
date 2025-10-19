# hello-pytest-env

## Overview
This project demonstrates a minimal Python application structure with configuration management and role-based logic, along with a robust pytest-based test suite. It is intended as a template or example for:
- Demonstrating a singleton pattern for application settings, ensuring configuration is loaded only once and reused throughout the app
- Using Pydantic for settings management via environment variables
- Writing and running isolated, environment-dependent tests with pytest

## Prerequisite
- Python 3.11 or newer

## Install
1. Copy the provided `default.env` to `.env` in the project root:
2. Edit `.env` to set your actual environment values. Example variables:
   ```env
   APP_NAME=your_app_name
   SECURITY__USERS_GROUP_ID=your_user_group_id
   SECURITY__MANAGERS_GROUP_ID=your_manager_group_id
   SECURITY__ADMINS_GROUP_ID=your_admin_group_id
   ```
3. Activate your virtual environment.
4. Install dependencies:
   ```sh
   pip install -e '.[dev]'
   ```

## Run
Make sure your `.env` file is present and configured. Run the main application (example):
```sh
python -m app.main
```
or, if you have an entry point script, run it directly.

## Test
1. Install development dependencies:
   ```sh
   pip install -e '.[dev]'
   ```
2. Run the test suite with pytest:
   ```sh
   pytest
   ```
   or for more verbose output:
   ```sh
   pytest -v
   ```

### Notes
- The test suite uses fixtures to set environment variables and reset configuration caches, ensuring each test is isolated and reproducible.
- The `.env` file is ignored by git for security.
- You can extend the roles, settings, and tests as needed for your own use case.
