import netifaces
import nmap
import socket
import struct

def mask2cidr(mask):
    """Convert netmask from Dotted address to CIDR."""
    return bin(struct.unpack('!L', socket.inet_pton(socket.AF_INET, mask))[0])[2:].index('0')

for iface in netifaces.interfaces():
    conf = netifaces.ifaddresses(iface)
    if 2 in conf:
        adr = str(conf[2][0]['addr'])
        if adr == '127.0.0.1' or '169.254' in adr:
            continue
        search = adr + '/' + str(mask2cidr(conf[2][0]['netmask']))
        print(search)
        nm = nmap.PortScanner()
        output = nm.scan(hosts=search, arguments='-sn')
        dic = output['scan']
        for key in dic:
            ip = dic[key]['addresses']['ipv4']
            if 'mac' in dic[key]['addresses']:
                m = dic[key]['addresses']['mac']
            else:
                m = ''
            print(' IP address: %s\tMac address: %s' % (ip, m))
