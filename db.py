import sqlite3
from datetime import datetime

def init_db():
    """Initialize the database with tables if not exist."""
    conn = sqlite3.connect('network.db')
    c = conn.cursor()
    # Table for scan logs
    c.execute('''CREATE TABLE IF NOT EXISTS scans
                 (id INTEGER PRIMARY KEY, ip TEXT, status TEXT, rtt REAL, timestamp TEXT, ipinfo TEXT)''')
    # Table for device names
    c.execute('''CREATE TABLE IF NOT EXISTS devices
                 (ip TEXT PRIMARY KEY, name TEXT)''')
    conn.commit()
    conn.close()

def insert_scan(ip, status, rtt, ipinfo):
    """Insert a scan result into the DB."""
    conn = sqlite3.connect('network.db')
    c = conn.cursor()
    timestamp = datetime.now().isoformat()
    c.execute("INSERT INTO scans (ip, status, rtt, timestamp, ipinfo) VALUES (?, ?, ?, ?, ?)",
              (ip, status, rtt, timestamp, ipinfo))
    conn.commit()
    conn.close()

def get_latest_scans():
    """Get the latest scan for each IP."""
    conn = sqlite3.connect('network.db')
    c = conn.cursor()
    c.execute('''SELECT s.ip, s.status, s.rtt, s.timestamp, s.ipinfo, d.name
                 FROM scans s
                 LEFT JOIN devices d ON s.ip = d.ip
                 WHERE s.timestamp = (SELECT MAX(timestamp) FROM scans WHERE ip = s.ip)''')
    results = c.fetchall()
    conn.close()
    return results

def get_history(ip):
    """Get historical RTT for a device."""
    conn = sqlite3.connect('network.db')
    c = conn.cursor()
    c.execute("SELECT timestamp, rtt FROM scans WHERE ip = ? AND status = 'online' ORDER BY timestamp", (ip,))
    results = c.fetchall()
    conn.close()
    return results

def set_device_name(ip, name):
    """Set or update device name."""
    conn = sqlite3.connect('network.db')
    c = conn.cursor()
    c.execute("INSERT OR REPLACE INTO devices (ip, name) VALUES (?, ?)", (ip, name))
    conn.commit()
    conn.close()

def get_previous_status(ip):
    """Get previous status for alert check."""
    conn = sqlite3.connect('network.db')
    c = conn.cursor()
    c.execute("SELECT status FROM scans WHERE ip = ? ORDER BY timestamp DESC LIMIT 1,1", (ip,))
    result = c.fetchone()
    conn.close()
    return result[0] if result else None
