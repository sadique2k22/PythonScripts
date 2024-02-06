import platform
import time

# Get system properties
system_info = platform.uname()

# Get system architecture
architecture = platform.architecture()[0]

# Print system architecture
print("System Architecture:", architecture)

# Print system properties
print("System Information:")
print(f"System: {system_info.system}")
print(f"Node Name: {system_info.node}")
print(f"Release: {system_info.release}")
print(f"Version: {system_info.version}")
print(f"Machine: {system_info.machine}")
print(f"Processor: {system_info.processor}")
print()
print("-------------")
import psutil #first run "pip install psutil" in terminal

# Get CPU information
cpu_info = {
    "Physical cores": psutil.cpu_count(logical=False),
    "Total cores": psutil.cpu_count(logical=True),
    "Max Frequency": f"{psutil.cpu_freq().max}Mhz",
    "Min Frequency": f"{psutil.cpu_freq().min}Mhz",
    "Current Frequency": f"{psutil.cpu_freq().current}Mhz",
    "CPU Usage Per Core": psutil.cpu_percent(percpu=True)
}

# Get Memory information
mem_info = {
    "Total Memory": f"{psutil.virtual_memory().total / (1024 ** 3):.2f} GB",
    "Available Memory": f"{psutil.virtual_memory().available / (1024 ** 3):.2f} GB",
    "Used Memory": f"{psutil.virtual_memory().used / (1024 ** 3):.2f} GB",
    "Memory Percentage": f"{psutil.virtual_memory().percent}%"
}

# Print CPU and Memory information
print("CPU Information:")
for key, value in cpu_info.items():
    print(f"{key}: {value}")

print("\nMemory Information:")
for key, value in mem_info.items():
    print(f"{key}: {value}")


time.sleep(500)