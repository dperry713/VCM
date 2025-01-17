import json
from datetime import datetime

class PIDManager:
    def __init__(self):
        self.available_pids = {}
        self.selected_pids = []
        self.log_file = f"logs/data_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

    def load_pids(self, pids_json):
        with open(pids_json, 'r') as file:
            self.available_pids = json.load(file)

    def select_pids(self, pid_list):
        self.selected_pids = [pid for pid in pid_list if pid in self.available_pids]

    def log_data(self, data):
        with open(self.log_file, 'a') as file:
            if file.tell() == 0:
                file.write(','.join(data.keys()) + '\n')
            file.write(','.join(map(str, data.values())) + '\n')
