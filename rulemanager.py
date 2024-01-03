from scapy.all import sniff

# Simulated Rule Manager
class RuleManager:
    def __init__(self):
        self.rules = []

    def add_rule(self, rule):
        self.rules.append(rule)

    def get_rules(self):
        return self.rules

# Simulated Detection Engine
def detection_engine(packet, rule_manager):
    # Simulated detection logic (checking for TCP packets)
    if packet.haslayer('TCP'):
        src_ip = packet['IP'].src
        dst_ip = packet['IP'].dst
        src_port = packet['TCP'].sport
        dst_port = packet['TCP'].dport
        
        # Simulated rule: Detecting traffic to port 80
        for rule in rule_manager.get_rules():
            if dst_port == 80:
                print(f"Alert: Traffic to port 80 detected from {src_ip}:{src_port} to {dst_ip}:{dst_port}. Rule triggered: {rule}")

# Function to start packet capture and detection
def start_packet_sniffer(rule_manager):
    def packet_handler(packet):
        detection_engine(packet, rule_manager)

    # Sniff packets on the network interface
    sniff(iface="eth0", prn=packet_handler, store=0)  # Change 'eth0' to your interface name

# Main function to demonstrate the IDS
if __name__ == "__main__":
    rule_manager = RuleManager()

    # Add predefined rules (simplified representation)
    predefined_rules = [
        'Detects HTTP traffic to port 80',
        'Detects traffic from known malicious IPs',
        # Add more rules as needed
    ]

    for rule in predefined_rules:
        rule_manager.add_rule(rule)

    # Start the packet sniffer and detection engine
    start_packet_sniffer(rule_manager)
