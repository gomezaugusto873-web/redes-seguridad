
import socket
import time

nombre = input("Dominio a resolver: ").strip()


inicio = time.perf_counter()
try:
    
    canonico, alias, ips = socket.gethostbyname_ex(nombre)

except socket.gaierror:
    print("No se pudo resolver", nombre)
    raise SystemExit(1)


ms = (time.perf_counter() - inicio) * 1000

print(f"Nombre canónico: {canonico}")
print(f"IP: {ips[0]}")
print(f"Tiempo de resolución: {ms:.1f} ms")


try:
    inverso, _, _ = socket.gethostbyaddr(ips[0])
    print(f"Resolución inversa: {inverso}")
except socket.herror:
    print("Resolución inversa: No disponible")