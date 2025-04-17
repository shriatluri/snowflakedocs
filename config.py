# config.py
# Fill in your Snowflake and email credentials below.

SNOWFLAKE_CONFIG = {
    'user': 'YOUR_SNOWFLAKE_USER',
    'password': 'YOUR_SNOWFLAKE_PASSWORD',
    'account': 'YOUR_SNOWFLAKE_ACCOUNT',
    'warehouse': 'YOUR_WAREHOUSE',
    'database': 'YOUR_DATABASE',
    'schema': 'YOUR_SCHEMA',
}

EMAIL_CONFIG = {
    'smtp_server': 'smtp.gmail.com',
    # default port for email
    'smtp_port': 587,
    'email': 'your_email@gmail.com',
    'app_password': 'your_app_password',  # Use an app password, not your main password
    'recipient': 'manager_email@company.com',
}
