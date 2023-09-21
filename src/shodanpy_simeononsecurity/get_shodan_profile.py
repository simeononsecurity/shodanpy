import os
import requests
import json
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

def get_shodan_profile():
    """
    Returns information about the Shodan account linked to this API key.

    :return: Shodan account information or an error message.
    :rtype: dict or str
    """
    api_key = os.getenv("SHODAN_API_KEY")
    if not api_key:
        return "Please set the 'SHODAN_API_KEY' environment variable with your Shodan API key."

    api_endpoint = f"https://api.shodan.io/account/profile?key={api_key}"

    try:
        response = requests.get(api_endpoint)
        response.raise_for_status()  # Raise an exception for non-200 status codes
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

if __name__ == "__main__":
    result = get_shodan_profile()
    if isinstance(result, dict):
        print(json.dumps(result, indent=4))
    else:
        print(result)
