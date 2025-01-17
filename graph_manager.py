import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class GraphManager:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.x_data, self.y_data = [], []

    def update_graph(self, frame, pid_data):
        self.x_data.append(frame)
        self.y_data.append(pid_data['value'])
        self.ax.clear()
        self.ax.plot(self.x_data, self.y_data)
        self.ax.set_title("Real-Time PID Data")
        self.ax.set_xlabel("Time (s)")
        self.ax.set_ylabel("Value")

    def start_graph(self, data_stream):
        animation = FuncAnimation(self.fig, self.update_graph,
                                fargs=(data_stream,), interval=1000)
        plt.show()
