import nmap
import netifaces

def get_network_range():
    """
    現在のネットワークインターフェースのIPv4アドレスとサブネット範囲を取得
    """
    for iface in netifaces.interfaces():
        addrs = netifaces.ifaddresses(iface)
        if netifaces.AF_INET in addrs:
            ipv4_info = addrs[netifaces.AF_INET][0]
            ip_address = ipv4_info['addr']
            netmask = ipv4_info['netmask']
            
            # サブネット範囲をCIDR表記で計算
            subnet_bits = sum([bin(int(x)).count('1') for x in netmask.split('.')])
            network_range = f"{ip_address}/{subnet_bits}"
            return network_range
    return None

def scan_network(network_range):
    """
    Nmapを使用してネットワーク内のデバイスをスキャンし、IPv4アドレスを収集
    """
    scanner = nmap.PortScanner()
    print(f"スキャン中: {network_range}")
    result = scanner.scan(hosts=network_range, arguments='-sn')  # Pingスキャン
    devices = []

    for host, info in result['scan'].items():
        ipv4 = info['addresses'].get('ipv4', None)
        if ipv4:
            devices.append(ipv4)
    
    return devices

def main():
    # 現在のネットワーク範囲を取得
    network_range = get_network_range()
    if not network_range:
        print("ネットワーク範囲が取得できませんでした")
        return

    # スキャンを実行してデバイスのIPv4アドレスを取得
    devices = scan_network(network_range)
    print("接続されているデバイスのIPv4アドレス:")
    for device in devices:
        print(f" - {device}")

if __name__ == "__main__":
    main()
