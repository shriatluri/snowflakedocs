# Snowflake Query Monitor Report

This Python project automates daily monitoring of Snowflake query activity and emails a summary report as HTML.

## Features
- Connects to Snowflake and runs your `.sql` scripts
- Loads results into Pandas DataFrames
- Converts results to HTML tables (long-running queries highlighted in red)
- Composes a daily HTML email with all sections
- Sends via Gmail SMTP (app password required)

## Required Modifications Before Running
**You must make the following changes to get this project working:**

1. **Fill in your Snowflake credentials in `config.py`:**
   - `'user'`: Your Snowflake username
   - `'password'`: Your Snowflake password
   - `'account'`: Your Snowflake account identifier (e.g., `xy12345.us-east-1`)
   - `'warehouse'`: The Snowflake warehouse to use
   - `'database'`: The database to use
   - `'schema'`: The schema to use

2. **Fill in your email credentials in `config.py`:**
   - `'email'`: The Gmail address to send from
   - `'app_password'`: [App Password](https://support.google.com/accounts/answer/185833?hl=en) generated from your Google Account (not your main password)
   - `'recipient'`: The email address to send the report to
   - `'smtp_server'` and `'smtp_port'`: Leave as defaults unless using a different provider

3. **Add your `.sql` files to the `sql/` directory:**
   - Each SQL file should contain a valid Snowflake query
   - The file names should match those referenced in `email_report.py` (or update the script accordingly)

4. **(Optional but recommended) Create a `config_template.py`:**
   - Copy `config.py` to `config_template.py` and remove your real credentials
   - Share `config_template.py` instead of `config.py` to keep secrets safe

5. **Ensure `.gitignore` includes `config.py`:**
   - This prevents accidental upload of your credentials to GitHub

---

## Setup
1. Clone this repo and add your `.sql` files to the `sql/` directory.
2. Fill in your Snowflake and email credentials in `config.py` (see above).
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the report:
   ```bash
   python email_report.py
   ```

## Notes
- For Gmail, generate an [App Password](https://support.google.com/accounts/answer/185833?hl=en) and use it in `config.py`.
- Add/modify `.sql` files as needed. Each will appear as a section in the report.
- Long-running queries (>15 min) will be highlighted in red.

## Extending
- To add Slack, PDF output, or scheduling (e.g., cron), ask Cascade for help!
