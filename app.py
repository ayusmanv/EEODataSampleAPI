from flask import Flask, render_template
from dataRead import data_read
import pandas as pd
app = Flask(__name__)

toc = pd.read_excel('data/FY 2020 Annual Report Workforce Tables.xlsx', sheet_name='Table of Contents', skiprows=4, nrows= 17)
@app.route('/')
def index():  # put application's code here
    return render_template("index.html", data  = toc.to_html())
@app.route('/data/api/v1/<table_name>')
def data(table_name):
    eeo1_table = data_read()
    eeo2_table = eeo1_table[eeo1_table['Table'] == table_name]

    return eeo2_table.to_json(orient='records')


if __name__ == '__main__':
    app.run()
