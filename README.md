# Google Sheet API

This repository contains a Python project for interacting with the Google Sheets API.

## Contents

- `Google.py` — main Python script for Google Sheets operations
- `lead_generation_notebook.ipynb` — Jupyter notebook for lead generation workflow containing all the command usage for Data manipulation.
- `.gitignore` — ignores credentials and runtime artifacts

## Notes

Do not commit or push the following files because they contain sensitive credentials:

- `client_secret.json`
- `token.json`
- `token_sheets_v4.pickle`

## Git push steps

1. Create a GitHub repository.
2. Add the remote:
   ```bash
   git remote add origin https://github.com/USERNAME/REPO.git
   ```
3. Push the local branch:
   ```bash
   git push -u origin master
   ```
