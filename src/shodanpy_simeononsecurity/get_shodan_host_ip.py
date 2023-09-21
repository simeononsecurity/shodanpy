import os
import requests
import json
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

def get_shodan_host_ip(ip, minify=False):
    """
    Search Shodan with an IP address.

    :param ip: The IP address to search for.
    :type ip: str
    :param minify: Whether to return a minified response.
    :type minify: bool
    :return: Dictionary with host information or an error message.
    :rtype: dict or str
    """
    api_key = os.getenv("SHODAN_API_KEY")
    if not api_key:
        return "Please set the 'SHODAN_API_KEY' environment variable with your Shodan API key."

    if not ip:
        return "Please specify an IP address with '-IP [string]'."

    api_endpoint = f"https://api.shodan.io/shodan/host/{ip}?key={api_key}"

    if minify:
        api_endpoint += "&minify=true"

    try:
        response = requests.get(api_endpoint)
        response.raise_for_status()  # Raise an exception for non-200 status codes
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

if __name__ == "__main__":
    # Replace '8.8.8.8' with the IP address you want to search for
    ip_to_search = "8.8.8.8"
    minify_response = True  # Set to True for minified response, False for full output
    result = get_shodan_host_ip(ip_to_search, minify_response)
    if isinstance(result, dict):
        print(json.dumps(result, indent=4))
    else:
        print(result)
