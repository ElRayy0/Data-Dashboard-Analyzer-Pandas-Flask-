from flask import Flask, render_template_string
import pandas as pd
import sqlite3

app = Flask(__name__)

@app.route('/')
def dashboard():
    df = pd.read_csv('sales.csv')  # Sample data
    summary = df.describe().to_html()
    return f"<h1>Sales Dashboard</h1>{summary}"

if __name__ == '__main__':
    app.run()