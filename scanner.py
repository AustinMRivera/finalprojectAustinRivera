import socket
import subprocess
import re
import time
from db import insert_scan, get_previous_status
from api_handler import get_ip_info
from config import EMAIL_SENDER, EMAIL_PASSWORD, EMAIL_RECEIVER
import smtplib
from email.mime.text import MIMEText

def get_local_network():
    """Get local network prefix (assumes /24)."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return '.'.join(local_ip.split('.')[:3]) + '.'
    except:
        return '192.168.1.'  # Fallback

def ping_ip(ip):
    """Ping an IP and get status and RTT."""
    try:
        start = time.time()
        output = subprocess.check_output(['ping', '-c', '1', '-W', '1', ip])
        duration = time.time() - start
        # Gather round trip time
        match = re.search(r'time=(\d+\.?\d*) ms', output.decode())
        rtt = float(match.group(1)) if match else duration * 1000  # Approx ms
        return 'online', rtt
    except subprocess.CalledProcessError:
        return 'offline', 0.0
    except Exception:
        return 'error', 0.0

def scan_network():
    """Scan the network and log results."""
    network = get_local_network()
    results = []
    for i in range(1, 255):
        ip = network + str(i)
        status, rtt = ping_ip(ip)
        if status != 'error':  # Skip errors
            ipinfo = get_ip_info(ip)
            insert_scan(ip, status, rtt, ipinfo)
            # Check for alert
            prev = get_previous_status(ip)
            if prev == 'online' and status == 'offline':
                send_alert(ip)
            results.append((ip, status, rtt))
    return results

def send_alert(ip):
    """Send email alert for offline device."""
    try:
        msg = MIMEText(f"Device {ip} went offline!")
        msg['Subject'] = 'Network Alert'
        msg['From'] = EMAIL_SENDER
        msg['To'] = EMAIL_RECEIVER

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
        server.quit()
    except Exception as e:
        print(f"Alert failed: {e}")  # Log to preventt crashing
