import os
import requests
import json
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

def get_shodan_client_ip():
    """
    Get your current IP address as seen from the Internet.

    :return: Current IP address or an error message.
    :rtype: str or str
    """
    api_key = os.getenv("SHODAN_API_KEY")
    if not api_key:
        return "Please set the 'SHODAN_API_KEY' environment variable with your Shodan API key."

    api_endpoint = f"https://api.shodan.io/tools/myip?key={api_key}"

    try:
        response = requests.get(api_endpoint)
        response.raise_for_status()  # Raise an exception for non-200 status codes
        return response.text
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

if __name__ == "__main__":
    result = get_shodan_client_ip()
    print(result)
