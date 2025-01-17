# Vehicle Communication Module (VCM)

Real-time vehicle diagnostic monitoring system with GM protocol support.

## Features

- Real-time OBD-II data monitoring
- Support for GM-specific protocols (J1850 VPW, CAN, GMLAN)
- Live data visualization and graphing
- Comprehensive data logging
- Interactive GUI dashboard
- PID management system

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/vcm.git
cd vcm
pip install -r src/requirements.txt
src/
├── obd_dashboard.py    # Main application entry point
├── gui.py             # GUI implementation
├── obd_connection.py  # OBD communication handler
├── pid_manager.py     # PID management system
├── graph_manager.py   # Real-time data visualization
├── logger.py          # Logging system
└── config/
    ├── config.json    # Application configuration
    └── pids.json      # PID definitions
cd src
python obd_dashboard.py
Connect to your vehicle's OBD-II port
Monitor real-time data through the interactive dashboard
Supported Protocols
J1850 VPW (10.4 kbps)
CAN (ISO 15765-4, 500 kbps)
GMLAN (33.3 kbps)
Configuration
Edit config.json to customize:

Connection settings
Logging preferences
GUI parameters
Graph refresh rates
Contributing
Fork the repository
Create a feature branch
Submit a pull request
