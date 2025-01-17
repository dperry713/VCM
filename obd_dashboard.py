import sys
import os
import json
from PyQt5.QtWidgets import QApplication
from gui import VCMApp
from obd_connection import OBDConnection
from pid_manager import PIDManager
from graph_manager import GraphManager
from logger import Logger


def load_config():
    config_path = os.path.join(os.path.dirname(__file__), 'config.json')
    with open(config_path, 'r') as f:
        return json.load(f)


def initialize_components(config):
    os.makedirs('logs', exist_ok=True)
    os.makedirs('config', exist_ok=True)

    logger = Logger(config['logging']['log_file'])
    connection = OBDConnection(
        mode=config['connection']['mode'],
        port=config['connection']['port'],
        baudrate=config['connection']['baudrate']
    )
    pid_manager = PIDManager()
    pid_manager.load_pids(config['pids']['file'])
    graph_manager = GraphManager()

    return logger, connection, pid_manager, graph_manager


def run_dashboard():
    app = QApplication(sys.argv)
    config = load_config()
    logger, connection, pid_manager, graph_manager = initialize_components(config)

    window = VCMApp()
    window.resize(*config['gui']['window_size'])
    window.setWindowTitle(config['gui']['window_title'])

    window.connection = connection
    window.pid_manager = pid_manager
    window.graph_manager = graph_manager
    window.logger = logger

    window.show()
    return app.exec_()


if __name__ == "__main__":
    sys.exit(run_dashboard())
