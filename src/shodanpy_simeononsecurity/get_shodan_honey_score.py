import os
import requests
import json
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

def get_shodan_honey_score(ip):
    """
    Calculates a honeypot probability score ranging from 0 (not a honeypot) to 1.0 (is a honeypot).

    :param ip: The IP address to calculate the honeypot score for.
    :type ip: str
    :return: Honeypot probability score or an error message.
    :rtype: float or str
    """
    api_key = os.getenv("SHODAN_API_KEY")
    if not api_key:
        return "Please set the 'SHODAN_API_KEY' environment variable with your Shodan API key."

    if not ip:
        return "Please specify an IP address with '-IP [string]'."

    api_endpoint = f"https://api.shodan.io/labs/honeyscore/{ip}?key={api_key}"

    try:
        response = requests.get(api_endpoint)
        response.raise_for_status()  # Raise an exception for non-200 status codes
        return float(response.text)
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

if __name__ == "__main__":
    # Replace '8.8.8.8' with the IP address you want to calculate the honeypot score for
    ip_to_check = "8.8.8.8"
    result = get_shodan_honey_score(ip_to_check)
    print(result)
