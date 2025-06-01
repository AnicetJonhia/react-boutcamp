#!/usr/bin/env python3
"""
Port Scanner basique en Python

Ce script se connecte en TCP aux ports d'une machine cible pour déterminer
si chaque port est ouvert ou fermé. 

Usage :
    python3 port_scanner.py <adresse_IP> <port_début> <port_fin>

Exemple :
    python3 port_scanner.py 192.168.1.10 1 1024
"""

import socket
import sys
from datetime import datetime

def scan_port(host: str, port: int, timeout: float = 0.5) -> bool:
    """
    Tente de se connecter en TCP à (host, port).
    Si la connexion réussit, on considère que le port est ouvert.
    Sinon, il est fermé ou filtré.
    """
    try:
        # Création d'un socket TCP
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # On définit un délai d'attente (timeout) pour ne pas bloquer trop longtemps
        sock.settimeout(timeout)
        # Tentative de connexion
        result = sock.connect_ex((host, port))
        sock.close()
        # connect_ex renvoie 0 si la connexion réussit
        return result == 0
    except Exception:
        return False

def main():
    # Vérification des arguments
    if len(sys.argv) != 4:
        print(f"Usage : {sys.argv[0]} <adresse_IP> <port_début> <port_fin>")
        sys.exit(1)

    target = sys.argv[1]
    try:
        port_start = int(sys.argv[2])
        port_end   = int(sys.argv[3])
    except ValueError:
        print("Les ports doivent être des entiers.")
        sys.exit(1)

    # Affichage d'un en-tête
    print("-" * 60)
    print(f"Scan des ports de {target} de {port_start} à {port_end}")
    print(f"Démarré à : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 60)

    # Pour chaque port dans l’intervalle, on teste si le port est ouvert
    for port in range(port_start, port_end + 1):
        ouvert = scan_port(target, port)
        if ouvert:
            print(f"[+] Port {port:5d} : ouvert")
        # Pour ne pas surcharger l’affichage, on n’affiche pas les ports fermés
        # else:
        #     print(f"[-] Port {port:5d} : fermé")

    print("-" * 60)
    print(f"Scan terminé à : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 60)

if __name__ == "__main__":
    main()
