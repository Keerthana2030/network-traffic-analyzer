!pip install pcapy
import pcapy
from scapy.all import *
import matplotlib.pyplot as plt
from scapy.layers.l2 import Ether


# Network interface to capture packets from
interface = "en0"

# Capture duration in seconds
capture_duration = 2

# Function to process captured packets
def process_packet(header, data):
    try:
        packet_scapy = Ether(data)
        protocol = packet_scapy.getlayer(2).name
        protocol_counts[protocol] += 1
        total_bytes[protocol] += len(data)
    except Exception as e:
        print(f"Error processing packet: {e}")  # Print any errors encountered

# Initialize dictionaries to store protocol counts and total bytes
protocol_counts = defaultdict(int)
total_bytes = defaultdict(int)

# Capture packets
print(f"Capturing packets on interface {interface} for {capture_duration} seconds...")
cap = pcapy.open_live(interface, 65536, 1, 0)
cap.loop(capture_duration, process_packet)

# Visualize results
protocols = list(protocol_counts.keys())
counts = list(protocol_counts.values())
bytes_transferred = list(total_bytes.values())

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.bar(protocols, counts)
plt.title("Packets per Protocol")
plt.xlabel("Protocol")
plt.ylabel("Number of Packets")

plt.subplot(1, 2, 2)
plt.bar(protocols, bytes_transferred)
plt.title("Total Bytes Transferred per Protocol")
plt.xlabel("Protocol")
plt.ylabel("Total Bytes")

plt.tight_layout()
plt.show()


!pip install scapy
from scapy.all import *
import matplotlib.pyplot as plt
from scapy.layers.l2 import Ether
from collections import defaultdict


# Network interface to capture packets from
interface = "eth0" # Change en0 to eth0 or your interface

# Capture duration in seconds
capture_duration = 2

# Function to process captured packets
def process_packet(packet):
    try:
        # Get protocol from layer 2
        protocol = packet.getlayer(2).name
        protocol_counts[protocol] += 1
        total_bytes[protocol] += len(packet)  # Get total bytes
    except Exception as e:
        print(f"Error processing packet: {e}")  # Print any errors encountered

# Initialize dictionaries to store protocol counts and total bytes
protocol_counts = defaultdict(int)
total_bytes = defaultdict(int)

# Capture packets
print(f"Capturing packets on interface {interface} for {capture_duration} seconds...")
packets = sniff(iface=interface, timeout=capture_duration, prn=process_packet)

# Visualize results
protocols = list(protocol_counts.keys())
counts = list(protocol_counts.values())
bytes_transferred = list(total_bytes.values())

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.bar(protocols, counts)
plt.title("Packets per Protocol")
plt.xlabel("Protocol")
plt.ylabel("Number of Packets")

plt.subplot(1, 2, 2)
plt.bar(protocols, bytes_transferred)
plt.title("Total Bytes Transferred per Protocol")
plt.xlabel("Protocol")
plt.ylabel("Total Bytes")

plt.tight_layout()
plt.show()

!pip install scapy
!apt-get update
!apt-get install libpcap-dev -y
from scapy.all import *

def packet_callback(packet):

    print(f"Source: {packet[IP].src}, Destination: {packet[IP].dst}, Protocol: {packet[IP].proto}")

# Start sniffing packets on a specific interface (e.g., 'eth0')
sniff(iface="eth0", prn=packet_callback, filter="ip", store=0)
