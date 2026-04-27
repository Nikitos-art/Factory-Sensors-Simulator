import time
from modbus_client import ModbusHandler
from data_logger import Logger
from dashboard import Dashboard
import yaml

# Load device config
with open("config.yaml") as f:
    config = yaml.safe_load(f)

# Initialize modules
modbus = ModbusHandler(config['devices'])
logger = Logger("sensor_data.csv")
dashboard = Dashboard(config['devices'])

# Poll loop
while True:
    for device in config['devices']:
        data, status = modbus.read_registers(device)

        logger.log(device['name'], data)
        dashboard.update(device['name'], data, status)

    time.sleep(5)
