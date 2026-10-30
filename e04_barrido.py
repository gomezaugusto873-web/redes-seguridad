import ipaddress
import platform
import subprocess
import time

from concurrent.futures import ThreadPoolExecutor


def hacer_ping(host):
    host = str(host)
    if platform.system().lower() == "windows":
        comando = ["ping", "-n", "1", "-w", "1000", host]
    else:
        comando = ["ping", "-c", "1", "-W", "1", host]
    try:
        r = subprocess.run(
            comando, 
            stdout=subprocess.DEVNULL, 
            stderr=subprocess.DEVNULL, 
            timeout=5
        )
        return r.returncode == 0
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return False

entrada = input("Red a barrer (ej. 192.168.10.0/24): ")

red = ipaddress.ip_network(entrada, strict=False)


if red.num_addresses > 1024:
    print("Red demasiado grande para esta práctica (máximo /22)")
    raise SystemExit(1)


hosts = list(red.hosts())


inicio = time.time()


with ThreadPoolExecutor(max_workers=50) as ejecutor:
    resultados = list(ejecutor.map(hacer_ping, hosts))

fin = time.time()


vivos = [h for h, ok in zip(hosts, resultados) if ok]


print(f"Hosts activos: {len(vivos)} de {len(hosts)}")
for h in vivos:
    print(" ", h)

print(f"\nTiempo transcurrido: {fin - inicio:.2f} segundos")
