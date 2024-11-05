import os
import shodan
from dotenv import load_dotenv
import json

load_dotenv('data.env')


SHODAN_API_KEY = os.getenv("SHODAN_API_KEY")
shodan_client = shodan.Shodan(SHODAN_API_KEY)


def get_host_info(ip_address):   
    try:
        host_info = shodan_client.host(ip_address)
        result = json.dumps(host_info, indent=2)
        return result
    except shodan.APIError as e:
        return {'error': str(e)}


def get_open_ports(ip_address):
    host_info = shodan_client.host(ip_address)
    open_ports = [service['port'] for service in host_info['data']]
    return open_ports

if __name__ == "__main__":
    print(get_host_info("8.8.8.8"))
    print(get_open_ports("8.8.8.8"))