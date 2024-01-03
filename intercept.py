from scapy.all import sniff, IP

# Function to process intercepted packets
def packet_handler(packet):
    if IP in packet:
        # Extract the destination IP address from the packet
        dest_ip = packet[IP].dst

        # Define criteria for good and bad traffic (replace with your criteria)
        good_ips = ['192.168.0.1', '192.168.0.2']  # Example good IPs
        bad_ips = ['10.0.0.1', '10.0.0.2']  # Example bad IPs

        # Check if the destination IP is in good or bad IPs
        if dest_ip in good_ips:
            print(f"Good Traffic - Destination IP: {dest_ip}")
            # Perform actions for good traffic (e.g., allow, log, etc.)
        elif dest_ip in bad_ips:
            print(f"Bad Traffic - Destination IP: {dest_ip}")
            # Perform actions for bad traffic (e.g., block, alert, etc.)
        else:
            print(f"Unknown Traffic - Destination IP: {dest_ip}")
            # Handle other traffic types

# Start sniffing traffic on the network interface (adjust interface as needed)
# Sniff indefinitely and pass intercepted packets to the packet_handler function
sniff(iface="eth0", prn=packet_handler, store=0)  # Change 'eth0' to your interface name
