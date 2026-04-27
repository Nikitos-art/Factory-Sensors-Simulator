# Factory (Modbus Experiment)

## Overview

This is a small experimental project where I explored working with **Modbus**, basic data collection, and simple orchestration of components in Python.

The idea was to simulate a factory-like environment with sensors (e.g. temperature, humidity), read their values via Modbus, log the data, and display it in a basic dashboard.

**Status:** Experimental / learning project (not production-ready)

---

## What this project does

* Simulates industrial sensors using Modbus
* Reads register data (temperature, humidity)
* Logs data to CSV
* Displays data in a simple Tkinter dashboard
* Uses a YAML config for device definitions

---

## Project Structure

```
factory/
│
├── main/
│   ├── main.py            # Orchestrates everything
│   ├── modbus_client.py  # Reads registers from devices
│   ├── modbus_server.py  # Simulated Modbus server
│   ├── datalogger.py     # Logs data to CSV
│   ├── dashboard.py      # Tkinter UI
│   ├── config.yaml       # Device configuration
│   ├── alerts.py         # (currently unused)
│   ├── utils.py          # (currently unused)
│
├── data.csv              # Example logged data
├── requirements.txt
├── README.md
```

---

## Configuration

Devices are defined in `config.yaml`:

```yaml
devices:
  - name: temperature_sensor_1
    ip: 127.0.0.1
    port: 1502
    unit_id: 1
    registers:
      temperature: 0
      humidity: 1
    threshold:
      temperature: 50
      humidity: 80
```

---

## Tech Stack

* Python
* pymodbus (Modbus communication)
* asyncio
* pandas / numpy (data handling)
* Tkinter (basic UI)

---

## How it works (high level)

1. Load device configuration from YAML
2. Connect to devices via Modbus
3. Read register values (temperature, humidity)
4. Log data to CSV
5. Update dashboard UI

---

## Running the project

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the system:

```bash
python main/main.py
```

(Optional) Run Modbus server:

```bash
python main/modbus_server.py
```

---

## Notes / Limitations

* This was an experiment to understand Modbus and system orchestration
* Code is not fully cleaned or optimized
* Some modules are incomplete (`alerts.py`, `utils.py`)
* No error handling or robustness guarantees

---

## Why I built this

To explore:

* Industrial protocols (Modbus)
* Data collection pipelines
* Structuring a multi-component Python system
* Basic monitoring/dashboard concepts

---

## Future ideas (if revisited)

* Add alerting system (threshold-based)
* Improve UI / replace Tkinter
* Add proper error handling and retries
* Dockerize services
* Expand to multiple devices / scaling

---
