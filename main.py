import requests
import os
from colorama import Fore, Style, init

# Inicializa colorama
init(autoreset=True)

# Função para limpar tela
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Banner principal
BANNER = f"""{Fore.GREEN}
╔══════════════════════════════════════════════════════╗
║                                                      ║
║   ████████╗██████╗  █████╗  ██████╗██╗  ██╗          ║
║   ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝          ║
║      ██║   ██████╔╝███████║██║     █████╔╝           ║
║      ██║   ██╔═══╝ ██╔══██║██║     ██╔═██╗           ║
║      ██║   ██║     ██║  ██║╚██████╗██║  ██╗          ║
║      ╚═╝   ╚═╝     ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝          ║
║                                                      ║
║      Created By HTR-TECH ( TAHMID RAYAT )            ║
╚══════════════════════════════════════════════════════╝
{Style.RESET_ALL}
"""

def track_ip(ip):
    url = f"https://ipinfo.io/{ip}/json"
    response = requests.get(url)
    data = response.json()

    # Alguns campos podem não existir, então usamos .get()
    ip_addr = data.get("ip", "N/A")
    city = data.get("city", "N/A")
    region = data.get("region", "N/A")
    country = data.get("country", "N/A")
    loc = data.get("loc", "N/A")
    org = data.get("org", "N/A")
    timezone = data.get("timezone", "N/A")
    postal = data.get("postal", "N/A")

    latitude, longitude = ("N/A", "N/A")
    if loc != "N/A":
        try:
            latitude, longitude = loc.split(",")
        except:
            pass

    print(Fore.GREEN + "╔══════════════════════════════════════════════════════╗")
    print(Fore.GREEN + "║" + Fore.YELLOW + f" Ip Address : {Fore.CYAN}{ip_addr}".ljust(54) + Fore.GREEN + "║")
    print(Fore.GREEN + "║" + Fore.YELLOW + f" City       : {Fore.CYAN}{city}".ljust(54) + Fore.GREEN + "║")
    print(Fore.GREEN + "║" + Fore.YELLOW + f" Region     : {Fore.CYAN}{region}".ljust(54) + Fore.GREEN + "║")
    print(Fore.GREEN + "║" + Fore.YELLOW + f" Country    : {Fore.CYAN}{country}".ljust(54) + Fore.GREEN + "║")
    print(Fore.GREEN + "║" + Fore.YELLOW + f" Latitude   : {Fore.CYAN}{latitude}".ljust(54) + Fore.GREEN + "║")
    print(Fore.GREEN + "║" + Fore.YELLOW + f" Longitude  : {Fore.CYAN}{longitude}".ljust(54) + Fore.GREEN + "║")
    print(Fore.GREEN + "║" + Fore.YELLOW + f" Time Zone  : {Fore.CYAN}{timezone}".ljust(54) + Fore.GREEN + "║")
    print(Fore.GREEN + "║" + Fore.YELLOW + f" Postal Code: {Fore.CYAN}{postal}".ljust(54) + Fore.GREEN + "║")
    print(Fore.GREEN + "║" + Fore.YELLOW + f" Org/ISP    : {Fore.CYAN}{org}".ljust(54) + Fore.GREEN + "║")
    print(Fore.GREEN + "╚══════════════════════════════════════════════════════╝")

    if latitude != "N/A" and longitude != "N/A":
        print(Fore.YELLOW + f"\n GOOGLE Maps: {Fore.CYAN}https://maps.google.com/?q={latitude},{longitude}\n")

def menu():
    while True:
        clear()
        print(BANNER)
        print(Fore.GREEN + "[01] Track IP")
        print("[02] Exit\n")

        choice = input(Fore.CYAN + ">> ")

        if choice in ["1", "01"]:
            ip = input(Fore.CYAN + "\n[+] Insira o IP (IPv4 ou IPv6): ")
            clear()
            print(BANNER)
            track_ip(ip)
            print(Fore.GREEN + "\n[01] Return To Main Menu")
            print("[02] Exit")
            sub = input(Fore.CYAN + "\n>> ")
            if sub in ["2", "02"]:
                print(Fore.RED + "\nSaindo...")
                break
        elif choice in ["2", "02"]:
            print(Fore.RED + "\nSaindo...")
            break
        else:
            print(Fore.RED + "\n[!] Opção inválida!")
            input("\nPressione ENTER para continuar...")

if __name__ == "__main__":
    menu()