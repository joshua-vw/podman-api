from flask import Flask, jsonify, request
import os
import psycopg

app = Flask(__name__)

def get_db_conn():
    return psycopg.connect(
        host=os.environ.get("DB_HOST", "db"),
        port=os.environ.get("DB_PORT", "5432"),
        dbname=os.environ.get("DB_NAME","appdb"),
        user=os.environ.get("DB_USER", "appuser"),
        password=os.environ.get("DB_PASSWORD", "apppass"),
    )

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/db-health")
def db_health():
    try:
        with get_db_conn() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT 1;")
                result = cur.fetchone()
        return {"db": "ok", "result": result[0]}
    except Exception as e:
        return {"db": "error", "error": str(e)}, 500


@app.get("/hello")
def hello():
    name = request.args.get("name", "world")
    return {"message": f"hello, {name}"}

@app.post("/echo")
def echo():
    data = request.get_json(silent=True) or {}
    return jsonify(received=data)
