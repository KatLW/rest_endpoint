from flask import Flask, json, request, render_template
import json

app = Flask(__name__)


@app.route('/')
def home():
    try:
        return render_template("index.html")
    except Exception as e:
        return str(e)


@app.route('/total', methods=['POST', 'GET'])
def total():
    if request.method == 'POST':
        req_data = request.get_json()
        nums = req_data['numbers']
        return json.dumps({'total': sum(nums)})
    else:
        return render_template('total.html')


if __name__ == '__main__':
    app.run(host='localhost', debug=True)
