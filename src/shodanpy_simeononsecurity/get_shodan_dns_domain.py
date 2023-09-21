import os
import requests
import json
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

def get_shodan_dns_domain(domain):
    """
    Get all the subdomains and other DNS entries for the given domain.

    :param domain: Domain for which to retrieve DNS entries.
    :type domain: str
    :return: DNS entries as a dictionary or an error message.
    :rtype: dict or str
    """
    api_key = os.getenv("SHODAN_API_KEY")
    if not api_key:
        return "Please set the 'SHODAN_API_KEY' environment variable with your Shodan API key."

    if not domain:
        return "Please specify a domain address with '-domain [string]'."

    api_endpoint = f"https://api.shodan.io/dns/domain/{domain}?key={api_key}"

    try:
        response = requests.get(api_endpoint)
        response.raise_for_status()  # Raise an exception for non-200 status codes
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

if __name__ == "__main__":
    # Replace 'google.com' with the domain you want to query
    domain_to_query = "google.com"
    result = get_shodan_dns_domain(domain_to_query)
    if isinstance(result, dict):
        print(json.dumps(result, indent=4))
    else:
        print(result)