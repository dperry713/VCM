from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import QTimer


class VCMApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.connection = None
        self.pid_manager = None
        self.graph_manager = None
        self.logger = None

        layout = QVBoxLayout()
        self.status_label = QLabel("Status: Disconnected")
        connect_button = QPushButton("Connect")
        disconnect_button = QPushButton("Disconnect")
        layout.addWidget(self.status_label)
        layout.addWidget(connect_button)
        layout.addWidget(disconnect_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        connect_button.clicked.connect(self.connect_obd)
        disconnect_button.clicked.connect(self.disconnect_obd)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_data)
        self.timer.start(1000)

    def connect_obd(self):
        try:
            self.connection.connect()
            self.status_label.setText("Status: Connected")
            self.logger.info("OBD Connection established")
        except Exception as e:
            self.logger.error(f"Connection failed: {str(e)}")
            self.status_label.setText("Status: Connection Failed")

    def disconnect_obd(self):
        try:
            self.connection.disconnect()
            self.status_label.setText("Status: Disconnected")
            self.logger.info("OBD Connection closed")
        except Exception as e:
            self.logger.error(f"Disconnection error: {str(e)}")

    def update_data(self):
        if self.connection and self.pid_manager.selected_pids:
            for pid in self.pid_manager.selected_pids:
                try:
                    data = self.connection.query_pid(pid)
                    self.pid_manager.log_data({pid: data})
                    self.graph_manager.update_graph(len(self.graph_manager.x_data), {'value': data})
                except Exception as e:
                    self.logger.error(f"Data update error: {str(e)}")
