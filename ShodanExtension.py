import os
import shodan
from dotenv import load_dotenv

load_dotenv('data.env')


SHODAN_API_KEY = os.getenv("SHODAN_API_KEY")
shodan_client = shodan.Shodan(SHODAN_API_KEY)


def get_host_info(ip_address):   
    try:
        host_info = shodan_client.host(ip_address)
        return host_info
    except shodan.APIError as e:
        return {'error': str(e)}


def get_open_ports(ip_address):
    host_info = shodan_client.host(ip_address)
    open_ports = [service['port'] for service in host_info['data']]
    return open_ports

