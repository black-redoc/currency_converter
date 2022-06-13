import requests

from_ = "USD"
to = "EUR"
value = 34523

data = {
    "from": from_,
    "to": to,
    "value": value
}

res = requests.post(
    "http://localhost:8000",
    json=data
)
if res.status_code == 200:
    res = res.json()
    result = res[f"in {to}"]

    with open("data.csv", "a") as file:
        file.writelines([f"{from_},{to},{value},{result}","\n"])
