### INF601 - Advanced Programming in Python
### Austin
### Final Project

# Network Monitoring App
A simple tool to monitor devices on a local network, detect connectivity issues, and provide alerts.

## Description
This project is a Python-based network monitoring application designed for small-scale networks, such as home or office setups. It scans the local network for connected devices using ping, tracks response times, enriches data with IP details from an external API, stores historical data in a SQLite database, and displays results via a web dashboard built with Flask. Additional features include email alerts for device status changes, device naming for better identification, and basic charts for viewing ping history. The purpose is to help users quickly identify and troubleshoot network problems, aligning with computer networking concepts by demonstrating device discovery, data persistence, and user-friendly reporting. It's built to be robust for a graduate-level course, incorporating modular code, error handling, and multiple features based on instructor feedback.

## Getting Started
### Dependencies
* Python 3.8 or higher (tested on Windows 10 and macOS).
* No specific OS requirements beyond Python compatibility.
* Install required libraries: `pip install flask requests`

### Installing
* Clone or download the repository from GitHub.
* No modifications needed to files/folders, but update config.py with your ipinfo.io token and email credentials.

### Executing program
* Navigate to the project directory.
* Run the application.
python app.py
text* Open a web browser and visit http://localhost:5000/
* Click "Run Scan" on the dashboard to start monitoring.

## Help
For common issues like scan failures, check if your network firewall blocks pings or if the API token is invalid—error messages will appear in the console. Email alerts may fail due to SMTP settings; use a Gmail app password to avoid blocks.
python app.py --debug  # Run in debug mode for more logs if needed
text## Authors
Austin  
Contact: [Your email or link if desired]

## Version History
* 0.2
    * Added error handling and dashboard improvements.
    * See commit changes on GitHub.
* 0.1
    * Initial Release

## License
This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgments
Inspiration, code snippets, etc.
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* [dbader](https://github.com/dbader/readme-template)
* [zenorocha](https://gist.github.com/zenorocha/4526327)
* [fvcproductions](https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46)
* Flask documentation for web framework guidance.
* ipinfo.io API for IP data enrichment.
