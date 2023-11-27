import platform
import psutil
import json
import socket
import netifaces
import getmac
import time

def get_ip_address():
    interfaces = netifaces.interfaces()
    for interface in interfaces:
        if interface != "lo":
            addresses = netifaces.ifaddresses(interface)
            if netifaces.AF_INET in addresses:
                return addresses[netifaces.AF_INET][0]['addr']

    return "Não foi possível obter o endereço IP."

def get_system_info():
    boot_time = psutil.boot_time()
    current_time = time.time()
    uptime_seconds = current_time - boot_time

    system_info = {
        'platform': platform.system(),
        'platform_version': platform.version(),
        'architecture': platform.architecture(),
        'cpu': platform.processor(),
        'hostname': socket.gethostname(),
        'ip_address': get_ip_address(),
        'mac_address': getmac.get_mac_address(),
        'memory': {
            'total': round(psutil.virtual_memory().total / (1024 ** 3), 2),
            'available': round(psutil.virtual_memory().available / (1024 ** 3), 2),
            'used': round(psutil.virtual_memory().used / (1024 ** 3), 2)
        },
        'uptime': round(uptime_seconds / 3600, 2)
    }
    return system_info

def save_to_json(data, filename='system_info.json'):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == "__main__":
    system_info = get_system_info()
    save_to_json(system_info)
    print("Informações da máquina salvas com sucesso no arquivo 'system_info.json'.")
