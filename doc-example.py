from scapy.all import *

# Crée un paquet IP avec l'adresse de destination 8.8.8.8
packet = IP(dst="8.8.8.8")  # type: ignore 
#packet.show()  # Affiche le contenu du paquet

# Segment TCP encapsulé dans paquet IP ( / ) avec un drapeau SYN sur le port 80
tcp_packet = IP(dst="8.8.8.8") / TCP(dport=80, flags="S")  # type: ignore 
#tcp_packet.show()


#### Sniffing
#fonction appelé à chaque sniff
def packet_callback(packet):
    print(packet.summary()) #methode summary (résumé comme visu Wireshark != show (details))

# Capture 10 paquets sur l'interface réseau par défaut
#sniff(count=1, prn=packet_callback)


#capture sur une carte réseau specified
sniff(iface="lo", count=5, prn=lambda x: x.summary())
