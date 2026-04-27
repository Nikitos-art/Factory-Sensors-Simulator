# modbus_server.py
from pymodbus.server import StartTcpServer
from pymodbus.datastore import (
    ModbusSequentialDataBlock,
    ModbusDeviceContext,
    ModbusServerContext,
)

print("Starting Modbus TCP server...")

store = ModbusDeviceContext(
    hr=ModbusSequentialDataBlock(0, [25, 60])
)

context = ModbusServerContext(devices=store, single=True)

print("Listening on port 1502")
StartTcpServer(context, address=("0.0.0.0", 1502))

try:
    StartTcpServer(context, address=("0.0.0.0", 1502))
except Exception as e:
    print("SERVER CRASHED:", e)
finally:
    print("Modbus server stopped")
