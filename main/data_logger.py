import csv
from datetime import datetime

class Logger:
    def __init__(self, filename):
        self.filename = filename
        with open(self.filename, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['timestamp', 'device', 'temperature', 'humidity'])

    def log(self, device_name, readings):
        if readings is None:
            print(f"[WARN] No data for {device_name}")
            return

        with open(self.filename, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), device_name, *readings])

    # def log(self, device_name, readings):
    #     with open(self.filename, 'a', newline='') as f:
    #         writer = csv.writer(f)
    #         writer.writerow([datetime.now(), device_name, *readings])
