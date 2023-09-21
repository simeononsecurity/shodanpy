import os
import requests
import json
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

def get_shodan_host_count(query, facet=None, minify=False):
    """
    This method behaves identically to "/shodan/host/search" with the only difference that it does not return any
    host results. It only returns the total number of results that matched the query and any facet information that
    was requested. As a result, this method does not consume query credits.

    :param query: The search query.
    :type query: str
    :param facet: Optional facet parameter.
    :type facet: str
    :param minify: Whether to return a minified response.
    :type minify: bool
    :return: Dictionary with host count and facet information or an error message.
    :rtype: dict or str
    """
    api_key = os.getenv("SHODAN_API_KEY")
    if not api_key:
        return "Please set the 'SHODAN_API_KEY' environment variable with your Shodan API key."

    if not query:
        return "Please specify your query with '-Query [string]'."

    api_endpoint = f"https://api.shodan.io/shodan/host/count?key={api_key}&query={query}"

    if facet:
        api_endpoint += f"&facets={facet}"

    if minify:
        api_endpoint += "&minify=true"
    else:
        api_endpoint += "&minify=false"

    try:
        response = requests.get(api_endpoint)
        response.raise_for_status()  # Raise an exception for non-200 status codes
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

if __name__ == "__main__":
    # Replace '[string]' with your query and, if needed, specify the '-Facet [string]' and '-Minify $true'
    query_to_search = "[string]"
    facet_to_include = "[string]"  # Optional
    minify_response = True  # Set to True for minified response, False for full output
    result = get_shodan_host_count(query_to_search, facet_to_include, minify_response)
    if isinstance(result, dict):
        print(json.dumps(result, indent=4))
    else:
        print(result)
