from flask import Flask, jsonify, request

app = Flask(__name__)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/hello")
def hello():
    name = request.args.get("name", "world")
    return {"message": f"hello, {name}"}

@app.post("/echo")
def echo():
    data = request.get_json(silent=True) or {}
    return jsonify(received=data)
