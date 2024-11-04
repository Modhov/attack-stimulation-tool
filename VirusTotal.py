import requests
import json
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv('data.env')

# Replace 'your_api_key' with your actual VirusTotal API key
API_KEY = os.getenv("VIRUS_TOTAL_API_KEY")
BASE_URL = 'https://www.virustotal.com/api/v3'

def get_ip_report(ip_address):
    endpoint = f"{BASE_URL}/ip_addresses/{ip_address}"
    headers = {
        'x-apikey': API_KEY
    }
    response = requests.get(endpoint, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Error: {response.status_code} - {response.text}"}

def format_timestamp(timestamp):
    """Convert Unix timestamp to a readable format."""
    return datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S') if timestamp else "N/A"

def format_report(report):
    if 'error' in report:
        return report['error']
    
    # Extract main data
    ip_data = report.get('data', {}).get('attributes', {})
    
    # Basic IP Information
    ip_info = {
        "IP Address": report.get('data', {}).get('id', 'N/A'),
        "Reputation": ip_data.get('reputation', 'N/A'),
        "Country": ip_data.get('country', 'N/A'),
        "Regional Internet Registry": ip_data.get('regional_internet_registry', 'N/A'),
        "ASN": ip_data.get('asn', 'N/A'),
        "ASN Owner": ip_data.get('as_owner', 'N/A'),
        "Last Analysis Date": format_timestamp(ip_data.get('last_analysis_date'))
    }
    
    # Categories
    categories = ip_data.get('categories', 'N/A')
    
    # Last Analysis Stats
    analysis_stats = ip_data.get('last_analysis_stats', {})
    
    # Last Analysis Results (Engines and their findings)
    analysis_results = ip_data.get('last_analysis_results', {})
    detailed_results = [
        f"{engine}: {result['category']}, {result['result']}" 
        for engine, result in analysis_results.items()
    ]

    # Threat Names and Tags
    tags = ip_data.get('tags', [])
    total_votes = ip_data.get('total_votes', {})

    # Format the structured report
    formatted_report = "\n".join([
        "=== IP Report ===",
        f"IP Address: {ip_info['IP Address']}",
        f"Reputation: {ip_info['Reputation']}",
        f"Country: {ip_info['Country']}",
        f"Regional Internet Registry: {ip_info['Regional Internet Registry']}",
        f"ASN: {ip_info['ASN']}",
        f"ASN Owner: {ip_info['ASN Owner']}",
        f"Last Analysis Date: {ip_info['Last Analysis Date']}",
        
        "\n--- Categories ---",
        json.dumps(categories, indent=4),
        
        "\n--- Last Analysis Stats ---",
        json.dumps(analysis_stats, indent=4),
        
        "\n--- Last Analysis Results ---",
        "\n".join(detailed_results) if detailed_results else "No results available.",
        
        "\n--- Threat Tags ---",
        ", ".join(tags) if tags else "No tags available.",
        
        "\n--- Community Votes ---",
        f"Harmless: {total_votes.get('harmless', 0)}",
        f"Malicious: {total_votes.get('malicious', 0)}"
    ])
    
    return formatted_report

if __name__ == "__main__":
    # Example IP address to scan (replace with the IP address you want to check)
    ip_address = "127.0.0.1"
    report = get_ip_report(ip_address)

    # Format and print the structured report
    formatted_report = format_report(report)
    print(formatted_report)
