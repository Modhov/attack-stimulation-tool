import nmap

def scan_network(ip_range):
    # Initialize the PortScanner
    nm = nmap.PortScanner()

    # Perform a scan on the specified IP range for common ports
    print(f"Scanning network range: {ip_range}")
    nm.scan(hosts=ip_range, arguments='-sP')  # -sP for ping scan

    # Display the scan results
    hosts_list = [(host, nm[host].state()) for host in nm.all_hosts()]
    for host, status in hosts_list:
        print(f"Host: {host}, Status: {status}")
        nm.scan(host, arguments='-p "1-1024" -sV')  # Scanning ports 1-1024 and detecting service versions
        for proto in nm[host].all_protocols():
            lport = nm[host][proto].keys()
            for port in sorted(lport):
                port_info = nm[host][proto][port]
                print(f"Port: {port}\tState: {port_info['state']}\tService: {port_info.get('name', 'Unknown')}\tVersion: {port_info.get('version', 'N/A')}")
    return hosts_list
# Example usage
if __name__ == "__main__":
    ip_range = "127.0.0.1"  # Replace with the desired IP range
    scan_results = scan_network(ip_range)