# email_report.py
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import EMAIL_CONFIG
from utils import load_sql, run_query, df_to_html

SQL_DIR = os.path.join(os.path.dirname(__file__), 'sql')
SQL_FILES = [
    'long_running_queries.sql',
    'user_query_count.sql',
    'top_users_bytes_scanned.sql',
    'query_target_tables.sql',
    'heavy_queries_bytes_scanned.sql',
    'user_filter_dropdown.sql',
    'query_execution_trends.sql',
    'query_metadata_warehouse_role.sql',
    'query_summary_last_7_days.sql',
]

SECTION_TITLES = {
    'long_running_queries.sql': 'Long-Running Queries (>15 min)',
    'user_query_count.sql': 'User Query Count (Last 7 Days)',
    'top_users_bytes_scanned.sql': 'Top 5 Users by Bytes Scanned',
    'query_target_tables.sql': 'Most Queried Tables',
    'heavy_queries_bytes_scanned.sql': 'Queries Scanning Over 1GB',
    'user_filter_dropdown.sql': 'User Filter Dropdown',
    'query_execution_trends.sql': 'Query Execution Time Trends',
    'query_metadata_warehouse_role.sql': 'Warehouse & Role Usage',
    'query_summary_last_7_days.sql': 'Last 7 Days Query Summary',
}


def build_report():
    html = ['<h2>Snowflake Query Monitor Report</h2>']
    for sql_file in SQL_FILES:
        path = os.path.join(SQL_DIR, sql_file)
        if not os.path.exists(path):
            continue
        sql = load_sql(path)
        df = run_query(sql)
        highlight = sql_file == 'long_running_queries.sql'
        html.append(f'<h3>{SECTION_TITLES.get(sql_file, sql_file)}</h3>')
        html.append(df_to_html(df, highlight_long_running=highlight))
    return '\n'.join(html)


def send_email(subject, html_content):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = EMAIL_CONFIG['email']
    msg['To'] = EMAIL_CONFIG['recipient']
    part = MIMEText(html_content, 'html')
    msg.attach(part)
    with smtplib.SMTP(EMAIL_CONFIG['smtp_server'], EMAIL_CONFIG['smtp_port']) as server:
        server.starttls()
        server.login(EMAIL_CONFIG['email'], EMAIL_CONFIG['app_password'])
        server.sendmail(msg['From'], [msg['To']], msg.as_string())


def main():
    html_report = build_report()
    send_email('Daily Snowflake Query Monitor Report', html_report)

if __name__ == '__main__':
    main()
