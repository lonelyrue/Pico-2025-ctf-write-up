from scapy.all import *
import base64

pkts = rdpcap('myNetworkTraffic.pcap')
data = [(float(p.time), bytes(p[Raw].load)) for p in pkts if p.haslayer(Raw)]
data.sort()

flag = b''
for t, raw in data:
    dec = base64.b64decode(raw)
    if all(32 <= c < 127 for c in dec):   # оставляем только printable-ASCII куски
        flag += dec

print(flag.decode())