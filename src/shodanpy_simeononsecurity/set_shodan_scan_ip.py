import os
import requests
import json
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

def set_shodan_scan_ip(ips):
    """
    Use this function to request Shodan to crawl a network.

    :param ips: IP address(es) to scan in CIDR notation (e.g., "8.8.8.8/32").
    :type ips: str

    :return: Scan request response or an error message.
    :rtype: dict or str
    """
    api_key = os.getenv("SHODAN_API_KEY")
    if not api_key:
        return "Please set the 'SHODAN_API_KEY' environment variable with your Shodan API key."

    api_endpoint = f"https://api.shodan.io/shodan/scan?key={api_key}&ips={ips}"

    try:
        response = requests.post(api_endpoint)
        response.raise_for_status()  # Raise an exception for non-2xx status codes
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

if __name__ == "__main__":
    ips_to_scan = "8.8.8.8/32"  # Specify the IP(s) you want to scan in CIDR notation
    result = set_shodan_scan_ip(ips_to_scan)
    print(result)
