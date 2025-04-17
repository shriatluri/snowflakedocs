# Snowflake Query Monitor Report

This Python project automates daily monitoring of Snowflake query activity and emails a summary report as HTML.

## Features
- Connects to Snowflake and runs your `.sql` scripts
- Loads results into Pandas DataFrames
- Converts results to HTML tables (long-running queries highlighted in red)
- Composes a daily HTML email with all sections
- Sends via Gmail SMTP (app password required)

## Setup
1. Clone this repo and add your `.sql` files to the `sql/` directory.
2. Fill in your Snowflake and email credentials in `config.py`.
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
