import socket

target = input("Enter target IP/domain: ")
ports = [22, 80, 443]
print(f"Scanning {target}...")

for port in ports:
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysocket.settimeout(0.5)
    result = mysocket.connect_ex((target, port))
    if result == 0:
        print(f"[+] Port {port} is open")
    else:
        print(f"[-] Port {port} is closed/filtered")
    mysocket.close()