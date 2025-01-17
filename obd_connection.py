import serial
from logger import Logger


class OBDConnection:
    def __init__(self, mode="serial", port=None, baudrate=9600, protocol="CAN"):
        self.mode = mode
        self.port = port
        self.baudrate = baudrate
        self.protocol = protocol
        self.connection = None

        # GM Protocol configurations
        self.PROTOCOLS = {
            "J1850_VPW": {
                "id": 1,
                "baudrate": 10400,
                "header": "6A"
            },
            "CAN": {
                "id": 6,
                "baudrate": 500000,
                "header": "7E0"
            },
            "GMLAN": {
                "id": 7,
                "baudrate": 33300,
                "header": "7E1"
            }
        }

    def connect(self):
        try:
            self.connection = serial.Serial(self.port, self.baudrate, timeout=2)
            # Set protocol
            protocol_config = self.PROTOCOLS[self.protocol]
            self.connection.write(f"ATSP{protocol_config['id']}\r".encode())
            self.connection.write(f"ATSH{protocol_config['header']}\r".encode())
            return True
        except Exception as e:
            raise ConnectionError(f"Failed to connect: {e}")

    def query_pid(self, pid):
        try:
            # Format message according to GM protocol
            protocol_config = self.PROTOCOLS[self.protocol]
            message = f"{protocol_config['header']} {pid}\r"
            self.connection.write(message.encode())
            response = self.connection.readline().decode().strip()
            return response
        except Exception as e:
            raise RuntimeError(f"Error querying PID {pid}: {e}")

    def disconnect(self):
        if self.connection:
            self.connection.close()
