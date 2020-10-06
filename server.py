from flask import Flask, json, request, redirect, url_for, render_template

app = Flask(__name__)


# numbers_to_add = list(range(10000001))


@app.route('/')
def home():
    try:
        return render_template("index.html")
    except Exception as e:
        return str(e)


@app.route('/total', methods=['POST'])
def total():
    req_data = request.get_json()
    nums = req_data['numbers']
    return json.dumps({'total': sum(nums)})


if __name__ == '__main__':
    app.run(debug=True)
