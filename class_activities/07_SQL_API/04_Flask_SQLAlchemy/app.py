from flask import Flask, render_template, request, jsonify
import json
from flask_sqlalchemy import SQLAlchemy
import psycopg2
import psycopg2.extras
import dotenv
import os
from flask_migrate import Migrate
import pandas as pd

dotenv.load_dotenv()

app = Flask(__name__)

cf = {
    'host': os.environ.get('DB_HOST'),
    'port': os.environ.get('DB_PORT'),
    'user': os.environ.get('DB_USER'),
    'password': os.environ.get('DB_PASSWORD'),
    'dbname': os.environ.get('DB_NAME')
}
conn = psycopg2.connect(**cf)
cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

@app.route('/')
def index():
    print(cf)
    cursor.execute('SELECT * from lungcancer')
    lc = cursor.fetchall()
    df = pd.DataFrame(lc)
    print (df.dtypes)
    for col in df.columns:
        print(df[col].dtype)
        if df[col].dtype!='object':
            df[col] = df[col].apply(lambda x: x-1)
    json_df = df.to_json(orient='records')
    json_df = json.loads(json_df)
    out = {
        'metadata': {
            'dataset': 'Lung Cancer Survey',
            'version': 1.0,
            'models_applied': 'Data cleaning'
        },
        'data': json_df
    }
    return jsonify(out)

@app.route('/query/<table>')
def query(table):
    base_query = f"SELECT * from {table}"
    filters = []
    limit = ""
    params  = request.args
    #get columns
    cursor.execute(f'SELECT * FROM {table} LIMIT 1')
    
    valid_cols = [col.name for col in cursor.description]
    for param in params:
        if param in valid_cols:
            filters.append(f"{param}={params[param]}")
        if param in ['limit','max_result']:
            limit = f"LIMIT {params[param]}" 

    if len(filters) > 1:
        filters = f'WHERE {" AND ".join(filters)}'
    elif len(filters) == 1:
        filters = f'WHERE {filters[0]}'
    else:
        filters = ""

    query = f'{base_query} {filters} {limit}'
    query = query.strip()
    print(query)
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Exception as e:
        print(e)
        cursor.execute("ROLLBACK")
        return {'error':400, 'message':'Invalid query'}



if __name__=='__main__':
    app.run(debug=True)