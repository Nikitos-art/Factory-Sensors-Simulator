from pymodbus.client import ModbusTcpClient

class ModbusHandler:
    def __init__(self, devices):
        self.devices = devices

    def read_registers(self, device):
        client = ModbusTcpClient(
            device["ip"],
            port=device["port"],
            timeout=2
        )

        if not client.connect():
            print(f"[ERROR] Cannot connect to {device['ip']}:{device['port']}")
            return None, "DISCONNECTED"

        temp_addr = device["registers"]["temperature"]
        hum_addr = device["registers"]["humidity"]

        rr_temp = client.read_holding_registers(address=temp_addr, count=1)
        rr_hum = client.read_holding_registers(address=hum_addr, count=1)

        client.close()

        if rr_temp.isError() or rr_hum.isError():
            print(f"[ERROR] Modbus read failed: temp={rr_temp}, hum={rr_hum}")
            return None, "READ ERROR"

        data = {
            "temperature": rr_temp.registers[0],
            "humidity": rr_hum.registers[0],
        }

        return data, "CONNECTED"

    # def read_registers(self, device):
    #     client = ModbusTcpClient(
    #         device["ip"],
    #         port=device["port"],
    #         timeout=2
    #     )

    #     if not client.connect():
    #         print(f"[ERROR] Cannot connect to {device['ip']}:{device['port']}")
    #         return None, "DISCONNECTED"

    #     rr = client.read_holding_registers(
    #         address=device["registers"]["temperature"],
    #         count=2
    #     )

    #     client.close()

    #     if rr is None or rr.isError():
    #         print(f"[ERROR] Modbus read failed: {rr}")
    #         return None, "READ ERROR"

    #     # Map registers explicitly
    #     data = {
    #         "temperature": rr.registers[0],
    #         "humidity": rr.registers[1],
    #     }

    #     return data, "CONNECTED"
