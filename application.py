from flask import Flask
from flask import render_template
from flask import request
import ppolom

import json
app = Flask(__name__)
app.debug = True

@app.route('/')
def hello_world():
    with open('products.json', 'r') as input_file:
        products = json.load(input_file)

    return render_template('index.html', data=products)


@app.route('/results/', methods=['POST'])
def evolve():
    item = request.form['product']
    ppolom.item = item
    results = ppolom.run()
    print results
    return render_template('results.html', data=results)

if __name__ == '__main__':
    app.run()
