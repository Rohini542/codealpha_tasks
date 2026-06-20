from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw

def process_packet(packet):
    print("\n" + "=" * 60)

    # Check if packet contains IP layer
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

        print(f"Source IP      : {src_ip}")
        print(f"Destination IP : {dst_ip}")

        # Identify protocol
        if packet.haslayer(TCP):
            protocol = "TCP"
        elif packet.haslayer(UDP):
            protocol = "UDP"
        elif packet.haslayer(ICMP):
            protocol = "ICMP"
        else:
            protocol = str(packet[IP].proto)

        print(f"Protocol       : {protocol}")

        # Ports for TCP/UDP
        if packet.haslayer(TCP):
            print(f"Source Port    : {packet[TCP].sport}")
            print(f"Destination Port: {packet[TCP].dport}")

        elif packet.haslayer(UDP):
            print(f"Source Port    : {packet[UDP].sport}")
            print(f"Destination Port: {packet[UDP].dport}")

        # Payload data
        if packet.haslayer(Raw):
            payload = packet[Raw].load
            print("Payload:")
            try:
                print(payload.decode('utf-8', errors='ignore'))
            except:
                print(payload)

    print("=" * 60)

print("Starting Packet Sniffer...")
print("Press Ctrl + C to stop.\n")

# Capture packets continuously
sniff(prn=process_packet, store=False)