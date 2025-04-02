import psutil

CPU_LIMIT = 20
RAM_LIMIT = 50
DISK_LIMIT = 20

# Get current PC data
def get_system_data():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    return cpu, ram, disk

def verify_limits(cpu, ram, disk):
    if cpu > CPU_LIMIT:
        print("Excessive CPU usage")

    if ram > RAM_LIMIT:
        print("Excessive RAM usage")

    if disk > DISK_LIMIT:
        print("Excessive DISK usage")

cpu, ram, disk = get_system_data()
verify_limits(cpu, ram, disk)
