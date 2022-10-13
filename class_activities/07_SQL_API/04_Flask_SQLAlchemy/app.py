from flask import Flask, render_template, request, jsonify
import json
import psycopg2
import psycopg2.extras
import os
import pandas as pd



app = Flask(__name__)

# Specify credentials
cd = {
    'host':os.environ.get('DB_HOST'),
    'port':os.environ.get('DB_PORT'),
    'user':os.environ.get('DB_USER'),
    'password':os.environ.get('DB_PASSWORD'),
    'dbname':os.environ.get('DB_NAME')
}

#Establish connection
conn = psycopg2.connect(**cd)
cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query/<table>')
def query(table):
    params = request.args
    print(params)
    try:
        init_query = f"SELECT * FROM {table} LIMIT 1"
        base_query = f"SELECT * FROM {table}"
        limit = ""
        filters = []
        cursor.execute(init_query)
        columns=[col.name for col in cursor.description]
        for param in params:
            if param in columns:
                filters.append(f"{param}={params[param]}")
            if param in ['limit','max_results','total_results']:
                limit = f"LIMIT {params[param]}"
        
        if len(filters) >= 1:
            filter_str = f"WHERE {' AND '.join(filters)}"
        else:
            filter_str = ""
        
        final_query = f"{base_query} {filter_str} {limit}".strip()
        cursor.execute(final_query)
        results = cursor.fetchall()
        return results
    except:
        cursor.execute("ROLLBACK")
        output = {
            'code': 404,
            'message': f'provided table {table} does not exist'
        }
        return output

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')