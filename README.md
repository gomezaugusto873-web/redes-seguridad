# redes-seguridad
e01_mi_equipo.py

Obtiene e imprime el nombre del equipo local junto con su dirección IP activa utilizando sockets UDP, resolviéndola mediante conexión de prueba sin necesidad de enviarla realmente.

e02_subred.py

Calcula y procesa parámetros de redes IPv4 en formato CIDR utilizando el módulo ipaddress, mostrando la dirección de red, máscara, prefijo, broadcast, cantidad de hosts útiles, primer host y último host.

e03_ping.py

Realiza una prueba básica de conectividad ICMP (ping) hacia un host o dirección IP específica adaptando los parámetros del sistema operativo (Windows o Linux), indicando si responde o no.

e04_barrido.py

Ejecuta un escaneo masivo (barrido de ping) sobre una subred completa utilizando múltiples hilos concurrentes (ThreadPoolExecutor) para descubrir equipos activos de forma eficiente y medir el tiempo transcurrido.

e05_puertos.py

Funciona como un escáner de puertos TCP de capa de transporte, evaluando un listado de puertos conocidos y servicios (incluyendo puertos personalizados como SMB, PostgreSQL y HTTP-Alt) para detectar cuáles se encuentran abiertos en un host.

e06_dns.py

Realiza la resolución de nombres de dominio (DNS) obteniendo el nombre canónico, la dirección IP asociada y el tiempo exacto que tarda la consulta en milisegundos, incluyendo además resolución inversa.

e07_latencia_tcp.py

Mide la latencia de conectividad a nivel de capa de transporte mediante múltiples intentos de conexión TCP sobre un puerto específico, calculando estadísticas de tiempos mínimos, máximos, promedios y porcentaje de pérdida.

e08_https_certificado.py

Verifica el estado de una aplicación web mediante HTTPS midiendo su tiempo de respuesta, código de estado HTTP y analizando de forma segura la validez y los días restantes hasta el vencimiento del certificado TLS/SSL del servidor.

Requisitos python 3.14
