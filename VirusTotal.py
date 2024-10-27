import requests

def scan_ip_address(ip_address, api_key):
    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip_address}"
    headers = {
        "x-apikey": api_key
    }

    # Send GET request to VirusTotal
    response = requests.get(url, headers=headers)

    # Check the response
    if response.status_code == 200:
        data = response.json()
        
        # Print basic information
        print(f"IP Address: {ip_address}")
        print("Malicious Detections:", data['data']['attributes']['last_analysis_stats']['malicious'])
        print("Suspicious Detections:", data['data']['attributes']['last_analysis_stats']['suspicious'])
        print("Undetected Detections:", data['data']['attributes']['last_analysis_stats']['undetected'])

        # Optional: Print detailed information
        for engine, result in data['data']['attributes']['last_analysis_results'].items():
            if result['category'] == 'malicious' or result['category'] == 'suspicious':
                print(f"{engine}: {result['category']} - {result['result']}")

    else:
        print(f"Failed to retrieve data: {response.status_code}")

# Example usage
api_key = "f9a1a4ad8c1363a520d7e1bd9b0858751cf1e735d74c149dea13b03378a8dd59"  # Replace with your actual VirusTotal API key
ip_address = "127.0.0.1"     # Replace with the IP address you want to scan
scan_ip_address(ip_address, api_key)