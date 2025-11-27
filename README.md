### INF 601 - Advanced Programming in Python
### Austin Rivera
### Final Project

# Network Monitoring App
A simple tool to monitor devices on a local network, detect connectivity issues, and provide alerts.

## Description
This project is a Python-based network monitoring app that is designed for small networks, such as home or small office setups. It scans the local network for connected devices using ping, tracks response times, uses data with IP details from an external API, stores historical data in a SQLite database, and displays results via a web dashboard built with Flask. Additional features include email alerts for device status changes, device naming for better identification, and basic charts for viewing ping history. The purpose is to help users identify and troubleshoot network problems, aligning with computer networking concepts.

## Getting Started
### Dependencies
* Python 3.8 or higher (tested on Windows 11).
* Install required libraries: `pip install flask requests`

### Installing
* Clone or download the repository from GitHub.
* No modifications needed to files/folders, but update config.py with your ipinfo.io token and email credentials.

### Executing program
* Navigate to the project directory.
* Run the application.
  python app.py
* Open a web browser and visit http://localhost:5000/
* Click "Run Scan" on the dashboard to start monitoring.

## Help
If the API token is invalid—error messages will appear in the console. Email alerts may fail due to SMTP settingss.
python app.py --debug  # Run in debug mode for more logs if needed

## Authors
Austin Rivera amrivera5@mail.fhsu.edu

## License
This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgments
* Flask documentation for web framework guidance.
* ipinfo.io API for IP data.
