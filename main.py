import ipaddress
import os 
import pyfiglet
from colorama import Fore, init
import colorama

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')
print(colorama.Fore.RED)
pyfiglet.print_figlet("Asylum")
print(colorama.Fore.RESET)
def generate_ip_port_list(ip, start_port, end_port):
    try:
        ip_obj = ipaddress.ip_address(ip)
        
        ip_port_list = [f"{ip}:{port}" for port in range(start_port, end_port + 1)]
        
        with open('ip_port_list.txt', 'w') as f:
            for item in ip_port_list:
                f.write(f"{item}\n")
        print(colorama.Fore.GREEN)
        print(f"IP and port list has been saved to 'ip_port_list.txt'.")
        print(colorama.Fore.RESET)
    except ValueError:
        print("Invalid IP address.")


ip = input("Please enter the IP address==> ")
start_port = int(input("Please enter the starting port==> "))
end_port = int(input("Please enter the ending port==> "))

generate_ip_port_list(ip, start_port, end_port)