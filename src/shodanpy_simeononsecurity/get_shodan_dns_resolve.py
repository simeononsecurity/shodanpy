import os
import requests
import json
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

def get_shodan_dns_resolve(domains):
    """
    Look up the IP address for the provided list of hostnames.

    :param domains: List of domain names separated by commas.
    :type domains: str
    :return: Dictionary mapping hostnames to IP addresses or an error message.
    :rtype: dict or str
    """
    api_key = os.getenv("SHODAN_API_KEY")
    if not api_key:
        return "Please set the 'SHODAN_API_KEY' environment variable with your Shodan API key."

    if not domains:
        return "Please specify one or more domain addresses with '-domains [string]'."

    api_endpoint = f"https://api.shodan.io/dns/resolve?hostnames={domains}&key={api_key}"

    try:
        response = requests.get(api_endpoint)
        response.raise_for_status()  # Raise an exception for non-200 status codes
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

if __name__ == "__main__":
    # Replace 'google.com,bing.com' with the list of domains you want to resolve
    domains_to_resolve = "google.com,bing.com"
    result = get_shodan_dns_resolve(domains_to_resolve)
    if isinstance(result, dict):
        print(json.dumps(result, indent=4))
    else:
        print(result)
