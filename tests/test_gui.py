import pytest
from PyQt5.QtWidgets import QApplication
from gui import VCMApp

@pytest.fixture
def app(qtbot):
    test_app = VCMApp()
    qtbot.addWidget(test_app)
    return test_app

def test_gui_initialization(app):
    assert app.status_label.text() == "Status: Disconnected"

def test_connect_button(app, qtbot):
    connect_button = app.findChild(QPushButton, "connect_button")
    qtbot.mouseClick(connect_button, Qt.LeftButton)
    assert app.status_label.text() == "Status: Connected"

def test_disconnect_button(app, qtbot):
    disconnect_button = app.findChild(QPushButton, "disconnect_button")
    qtbot.mouseClick(disconnect_button, Qt.LeftButton)
    assert app.status_label.text() == "Status: Disconnected"
