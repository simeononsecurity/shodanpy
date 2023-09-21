import os
import requests
import json
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

def get_shodan_dns_reverse(ips):
    """
    Look up the hostnames that have been defined for the given list of IP addresses.

    :param ips: List of IP addresses separated by commas.
    :type ips: str
    :return: Dictionary mapping IP addresses to hostnames or an error message.
    :rtype: dict or str
    """
    api_key = os.getenv("SHODAN_API_KEY")
    if not api_key:
        return "Please set the 'SHODAN_API_KEY' environment variable with your Shodan API key."

    if not ips:
        return "Please specify IP addresses with '-ips [string]'."

    api_endpoint = f"https://api.shodan.io/dns/reverse?ips={ips}&key={api_key}"

    try:
        response = requests.get(api_endpoint)
        response.raise_for_status()  # Raise an exception for non-200 status codes
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

if __name__ == "__main__":
    # Replace '8.8.8.8,8.8.4.4' with the list of IP addresses you want to reverse lookup
    ips_to_reverse = "8.8.8.8,8.8.4.4"
    result = get_shodan_dns_reverse(ips_to_reverse)
    if isinstance(result, dict):
        print(json.dumps(result, indent=4))
    else:
        print(result)
