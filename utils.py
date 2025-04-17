# utils.py
import os
import pandas as pd
import snowflake.connector
from config import SNOWFLAKE_CONFIG


def load_sql(file_path):
    with open(file_path, 'r') as f:
        return f.read()


def run_query(sql):
    ctx = snowflake.connector.connect(**SNOWFLAKE_CONFIG)
    try:
        cs = ctx.cursor()
        cs.execute(sql)
        df = pd.DataFrame(cs.fetchall(), columns=[col[0] for col in cs.description])
        return df
    finally:
        cs.close()
        ctx.close()


def df_to_html(df, highlight_long_running=False):
    if df.empty:
        return '<p>No results.</p>'
    if highlight_long_running and 'QUERY_EXECUTION_TIME' in df.columns:
        def highlight_row(row):
            if row['QUERY_EXECUTION_TIME'] > 900000:
                return ['background-color: #f8d7da'] * len(row)
            return [''] * len(row)
        styled = df.style.apply(highlight_row, axis=1)
        return styled.to_html(escape=False, index=False)
    return df.to_html(escape=False, index=False)
