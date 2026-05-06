import yaml
from modbus_client import ModbusHandler
from data_logger import Logger
from dashboard import Dashboard

# Load config
with open("config.yaml") as f:
    config = yaml.safe_load(f)

devices = config["devices"]

# Initialize components
modbus = ModbusHandler(devices)
logger = Logger("sensor_data.csv")
dashboard = Dashboard(devices)


def poll():
    for device in devices:
        data, status = modbus.read_registers(device)
        # data = {"temperature": 25, "humidity": 60}
        # status = "OK"
        
        logger.log(device["name"], data)
        dashboard.update(device["name"], data, status)

    # schedule next run (every 5 seconds)
    dashboard.root.after(5000, poll)


if __name__ == "__main__":
    poll()              # start polling loop
    dashboard.run()     # start Tkinter mainloop