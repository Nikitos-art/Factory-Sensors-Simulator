import random
import time
import threading

from pymodbus.server import StartTcpServer
from pymodbus.datastore import ModbusSequentialDataBlock, ModbusDeviceContext, ModbusServerContext

# keep a reference to the data block
data_block = ModbusSequentialDataBlock(0, [
    25, 60,   # sensor 1
    26, 65,   # sensor 2
    24, 55    # warehouse
])
store = ModbusDeviceContext(hr=data_block)
context = ModbusServerContext(devices=store, single=True)

def update_values():
    while True:
        for i in range(0, 6, 2):  # 0,2,4
            temp = data_block.getValues(i, 1)[0]
            hum = data_block.getValues(i + 1, 1)[0]

            temp += random.randint(-1, 1)
            hum += random.randint(-2, 2)

            temp = max(15, min(40, temp))
            hum = max(20, min(90, hum))

            data_block.setValues(i, [temp])
            data_block.setValues(i + 1, [hum])

        #print(f"[SERVER] T={temp}, H={hum}")
        time.sleep(2)


if __name__ == "__main__":
    try:
        print("Modbus server starting on port 1502...")
        threading.Thread(target=update_values, daemon=True).start()
        StartTcpServer(context, address=("0.0.0.0", 1502))
    except Exception as e:
        print("SERVER CRASHED:", e)
    finally:
        print("Modbus server stopped")
