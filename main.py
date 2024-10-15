#!/usr/bin/env python3
from scapy.all import *
import time
import pandas as pd

nb_packet = 0
df = pd.DataFrame(columns=['Time', 'Protocol'])

def packet_callback(packet):
    global nb_packet
    nb_packet += 1
    elapsed_time = time.time() - start_time

    # Identifier le protocole du paquet
    if packet.haslayer("UDP"):
        protocol = "UDP"
    elif packet.haslayer("TCP"):
        protocol = "TCP"
    else:
        protocol = "OTHER"

    # Ajouter une nouvelle ligne au DataFrame
    global df
    df = pd.concat([df, pd.DataFrame([[round(elapsed_time), protocol]], columns=['Time', 'Protocol'])], ignore_index=True)
    print(f"Temps : {round(elapsed_time)}s, Protocole : {protocol}")

start_time = time.time()
sniff(iface = "wlo1", prn=packet_callback)

try : 
    df.to_csv('network_capture.csv', index=False)
    print("Les données ont été enregistrées dans 'network_capture.csv'")
except :
    print("ERROR :  Les données n'ont pas pu être enregistré dans le CSV ")