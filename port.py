import socket

target = input("Enter target IP (e.g., 127.0.0.1): ")

ports = [21, 22, 80, 135, 443] 

print(f"\nScanning {target}...")

for port in ports:
    s = socket.socket() 
    s.settimeout(0.5)
    
    result = s.connect_ex((target, port))
    
    if result == 0:
        print(f"[+] Port {port} is OPEN")
    else:
        
        print(f"[-] Port {port} is closed") 
        
    s.close()