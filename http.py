from scapy.all import sniff

# Function to handle intercepted HTTP packets
def http_packet_handler(packet):
    if packet.haslayer('TCP') and packet.haslayer('Raw'):
        # Check if it's an HTTP request (simplified for demonstration)
        raw = packet['Raw'].load.decode('utf-8', errors='ignore')
        if 'HTTP' in raw:
            # Extract the HTTP method and URI
            http_lines = raw.split('\r\n')
            first_line = http_lines[0]
            http_method, uri, _ = first_line.split()

            # Define criteria for good and potentially malicious traffic
            # For instance, consider legitimate requests as 'GET' methods and specific URIs
            if http_method == 'GET' and uri.startswith('/api'):
                print(f"Regular Traffic - {http_method} {uri}")
                # Perform actions for regular traffic (e.g., log, allow, etc.)
            else:
                print(f"Potentially Malicious Traffic - {http_method} {uri}")
                # Perform actions for potentially malicious traffic (e.g., alert, block, etc.)

# Start sniffing HTTP traffic on the network interface
# Sniff indefinitely and pass intercepted packets to the http_packet_handler function
sniff(iface="eth0", filter="tcp port 80", prn=http_packet_handler, store=0)  # Change 'eth0' to your interface name
