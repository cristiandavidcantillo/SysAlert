import psutil
import time
from plyer import notification

CPU_LIMIT = 20
RAM_LIMIT = 50
DISK_LIMIT = 20



def get_system_data():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    return cpu, ram, disk



def verify_limits(cpu, ram, disk):
    if cpu > CPU_LIMIT:
        notification.notify(
            title="⚠ ¡Uso alto de CPU!",
            message=f"El uso del procesador es del {cpu}%. Cierra programas innecesarios o revisa los procesos en segundo plano.",
            timeout=5,
        )

    if ram > RAM_LIMIT:
        notification.notify(
            title="⚠ ¡Memoria RAM casi llena!",
            message=f"El uso de RAM es del {ram}%. Cierra aplicaciones que no uses.",
            timeout=5,
        )

    if disk > DISK_LIMIT:
        notification.notify(
            title="⚠ ¡Poco espacio en disco!",
            message=f"El almacenamiento está al {disk}%. Borra archivos innecesarios.",
            timeout=5,
        )


def procesos():
    process = []
    
    for i in psutil.process_iter(["name", "cpu_percent"]):
        name = i.info["name"]
        cpu = i.info["cpu_percent"]
        
        if name and cpu > 0.0: 
            process.append((name, cpu))
    
    procesos_ordenados = sorted(process, key=lambda x: x[1], reverse=True)
    
    procesos_altos = procesos_ordenados[:3]
    
    print(procesos_altos)

procesos()



while True:
    cpu, ram, disk = get_system_data()
    verify_limits(cpu, ram, disk)
    procesos()
    time.sleep(2)
