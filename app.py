from flask import Flask, render_template, jsonify
import psutil

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/stats')
def stats():
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory()
    disk = psutil.disk_usage("C:\\" if psutil.WINDOWS else "/")

    return jsonify({
        "cpu": cpu,
        "memory": mem.percent,
        "disk": disk.percent,
        "mem_used": round(mem.used / (1024**3), 1),
        "mem_total": round(mem.total / (1024**3), 1),
        "disk_used": round(disk.used / (1024**3), 1),
        "disk_total": round(disk.total / (1024**3), 1),
    })

if __name__ == '__main__':
    app.run(debug=True)
