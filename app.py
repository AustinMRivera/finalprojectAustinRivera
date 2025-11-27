from flask import Flask, render_template, request, redirect, url_for
import os
from db import init_db, get_latest_scans, get_history, set_device_name
from scanner import scan_network

app = Flask(__name__)

# Init DB on start
init_db()

@app.route('/')
def dashboard():
    """Main dashboard showing latest scans."""
    scans = get_latest_scans()
    # Simple sort by IP, or filter if query param
    filter_status = request.args.get('filter', '')
    if filter_status:
        scans = [s for s in scans if s[1] == filter_status]
    scans.sort(key=lambda x: x[0])  # Sort by IP
    return render_template('index.html', scans=scans)

@app.route('/scan', methods=['POST'])
def scan():
    """Trigger a scan."""
    try:
        scan_network()
        return redirect(url_for('dashboard'))
    except Exception as e:
        return f"Scan failed: {e}", 500

@app.route('/device/<ip>')
def device_detail(ip):
    """Detail page with history chart."""
    history = get_history(ip)
    timestamps = [h[0] for h in history]
    rtts = [h[1] for h in history]
    return render_template('device_detail.html', ip=ip, timestamps=timestamps, rtts=rtts)

@app.route('/admin/name', methods=['POST'])
def admin_name():
    """Set device name via form."""
    ip = request.form.get('ip')
    name = request.form.get('name')
    if ip and name:
        set_device_name(ip, name)
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True)
