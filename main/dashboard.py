import tkinter as tk

class Dashboard:
    def __init__(self, devices):
        self.root = tk.Tk()
        self.root.title("Factory Monitor")

        self.labels = {}

        for i, device in enumerate(devices):
            name = device["name"]

            tk.Label(self.root, text=name, width=20).grid(row=i, column=0)

            status = tk.Label(self.root, text="INIT", width=15)
            status.grid(row=i, column=1)

            values = tk.Label(self.root, text="---", width=20)
            values.grid(row=i, column=2)

            self.labels[name] = {
                "status": status,
                "values": values,
            }

    def update(self, device_name, data, status):
        if data is None:
            self.labels[device_name]["status"].config(text=status)
            self.labels[device_name]["values"].config(text="---")
        else:
            text = f"T={data['temperature']} H={data['humidity']}"
            self.labels[device_name]["status"].config(text=status)
            self.labels[device_name]["values"].config(text=text)

        self.root.update_idletasks()

    def run(self):
        self.root.mainloop()
