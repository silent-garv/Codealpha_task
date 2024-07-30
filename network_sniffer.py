from scapy.all import sniff, IP , Ether ,TCP ,UDP 

def packet_callback(packet):
    if Ether in packet:
        eth_layer = packet[Ether]
        print(f"MAC:{eth_layer.src} -> {eth_layer.dst}")

    if IP in packet:
        ip_layer = packet[IP]
        print(f"IP:{ip_layer.src} -> {ip_layer.dst}")

    if TCP in packet:
        tcp_layer = packet[TCP]
        print(f"TCP Port:{tcp_layer.sport} -> {tcp_layer.dport}")

    elif UDP in packet:
       udp_layer = packet[UDP]
       print(f"UDP Port:{udp_layer.sport} -> {udp_layer.dport}")


print("Starting packet capturing.........")

sniff(prn=packet_callback, store=0)



