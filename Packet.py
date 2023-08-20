from scapy.all import *
ports = [25,80,53,443,445,8080,8443]

def synscan(host):
    answer,unanswer = sr(IP(dst=host)/TCP(sport=5555,dport=ports,flags='S'),timeout=2,verbose=0)
    print('open ports at %s:'%host)
    for (s,r,) in answer:
        if s[TCP].dport == r[TCP].sport:
            print(s[TCP].dport)

def dnsscan(host):
    answer,unanswer = sr(IP(dst=host)/UDP(sport=5555,dport=53)/DNS(rd=1, qd=DNSQR(qname="google.com")),timeout=2,verbose=0)
    if answer:
        print("DNS Server at %s"%host)

host = "8.8.8.8"
synscan(host)
dnsscan(host)
