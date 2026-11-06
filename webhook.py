from flask import Flask, request

app = Flask(__name__)

@app.route("/callback", methods=["POST"])
def callback():
    data = request.json

    print("\n=== M-PESA CALLBACK ===")
    print(data)

    return {
        "ResultCode": 0,
        "ResultDesc": "Accepted"
    }

app.run(host="0.0.0.0", port=5000)






