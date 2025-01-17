import pytest
from pid_manager import PIDManager
import json
import os

@pytest.fixture
def pid_manager():
    return PIDManager()

@pytest.fixture
def sample_pids():
    return {
        "010C": {
            "name": "Engine RPM",
            "description": "Engine speed",
            "units": "rpm"
        }
    }

def test_pid_manager_initialization(pid_manager):
    assert pid_manager.available_pids == {}
    assert isinstance(pid_manager.selected_pids, list)

def test_pid_selection(pid_manager, sample_pids):
    pid_manager.available_pids = sample_pids
    pid_manager.select_pids(["010C"])
    assert "010C" in pid_manager.selected_pids

def test_data_logging(pid_manager, tmp_path):
    pid_manager.log_file = str(tmp_path / "test_log.csv")
    test_data = {"010C": 2500}
    pid_manager.log_data(test_data)
    assert os.path.exists(pid_manager.log_file)
