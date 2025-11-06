import psutil
import time
import os
import matplotlib.pyplot as plt

def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def show_system_info():
    print("="*40)
    print("SYSTEM INFORMATION")
    print("="*40)
    print(f"CPU Cores: {psutil.cpu_count(logical=False)} Physical, {psutil.cpu_count(logical=True)} Logical")
    print(f"CPU Usage: {psutil.cpu_percent(interval=1)}%")
    memory = psutil.virtual_memory()
    print(f"Memory Usage: {memory.percent}% ({get_size(memory.used)} / {get_size(memory.total)})")
    disk = psutil.disk_usage('/')
    print(f"Disk Usage: {disk.percent}% ({get_size(disk.used)} / {get_size(disk.total)})")
    net = psutil.net_io_counters()
    print(f"Network: Sent={get_size(net.bytes_sent)} | Received={get_size(net.bytes_recv)}")

def live_monitor():
    try:
        while True:
            os.system("clear")
            print("="*30, "Real-Time System Monitor", "="*30)
            print(f"CPU Usage: {psutil.cpu_percent(interval=1)}%")
            memory = psutil.virtual_memory()
            print(f"Memory Usage: {memory.percent}%")
            disk = psutil.disk_usage('/')
            print(f"Disk Usage: {disk.percent}%")
            net = psutil.net_io_counters()
            print(f"Network Sent: {get_size(net.bytes_sent)} | Received: {get_size(net.bytes_recv)}")
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")

def plot_cpu_usage(duration=20):
    cpu_data = []
    timestamps = []
    for i in range(duration):
        cpu = psutil.cpu_percent(interval=1)
        cpu_data.append(cpu)
        timestamps.append(i+1)
    plt.plot(timestamps, cpu_data, label="CPU Usage (%)")
    plt.xlabel("Time (s)")
    plt.ylabel("CPU Usage %")
    plt.title("CPU Usage Over Time")
    plt.legend()
    plt.show()

def main():
    while True:
        print("\n===== SYSTEM MONITOR TOOL =====")
        print("1. Show System Info")
        print("2. Start Live Monitor")
        print("3. Plot CPU Usage Graph")
        print("4. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            show_system_info()
        elif choice == '2':
            live_monitor()
        elif choice == '3':
            plot_cpu_usage()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid option. Try again!")

if __name__ == "__main__":
    main()
