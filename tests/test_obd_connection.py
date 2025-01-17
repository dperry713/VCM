import pytest
from obd_connection import OBDConnection

def test_obd_connection_initialization():
    connection = OBDConnection(mode="serial", port="COM3", baudrate=9600, protocol="CAN")
    assert connection.mode == "serial"
    assert connection.port == "COM3"
    assert connection.protocol == "CAN"

def test_protocol_configurations():
    connection = OBDConnection()
    protocols = connection.PROTOCOLS
    assert "J1850_VPW" in protocols
    assert "CAN" in protocols
    assert "GMLAN" in protocols
    assert protocols["CAN"]["baudrate"] == 500000

@pytest.mark.parametrize("protocol", ["J1850_VPW", "CAN", "GMLAN"])
def test_protocol_headers(protocol):
    connection = OBDConnection(protocol=protocol)
    assert connection.PROTOCOLS[protocol]["header"] is not None
