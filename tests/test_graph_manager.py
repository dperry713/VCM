import pytest
from graph_manager import GraphManager
import matplotlib.pyplot as plt

@pytest.fixture
def graph_manager():
    return GraphManager()

def test_graph_initialization(graph_manager):
    assert isinstance(graph_manager.fig, plt.Figure)
    assert len(graph_manager.x_data) == 0
    assert len(graph_manager.y_data) == 0

def test_graph_update(graph_manager):
    test_data = {'value': 100}
    graph_manager.update_graph(1, test_data)
    assert len(graph_manager.x_data) == 1
    assert len(graph_manager.y_data) == 1
    assert graph_manager.y_data[0] == 100
