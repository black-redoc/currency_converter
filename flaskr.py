from flask import Flask, request

from .currencies import currency_list

app = Flask(__name__)


@app.route("/", methods=["POST"])
def home():
    data = request.get_json()
    from_ = data["from"]
    to = data["to"]
    value = float(data["value"])
    currency_vals = currency_list.get(from_)
    currency_2vals = currency_vals[to]
    if not currency_vals or not currency_2vals:
        return {"error": "currency has not exist"}, 400
    else:
        result = value * currency_2vals
        result = result * 100
        result = int(result) / 100
        return {f"{from_}": value, f"in {to}": result}


app.run(port=8000, debug=True)
