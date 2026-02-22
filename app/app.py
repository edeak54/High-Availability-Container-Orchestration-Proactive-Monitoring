from flask import Flask
import os
from datetime import datetime

app = Flask(__name__)
DATA_FILE = "/data/migration_test.log"

@app.route('/')
def index():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    
    with open(DATA_FILE, "a") as f:
        f.write(f"Access at: {now}\n")
    
    return f"<h1>Migration Demo</h1><p>Logged access at {now}. Check /data/migration_test.log</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)