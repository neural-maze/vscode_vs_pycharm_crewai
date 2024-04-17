import os
from exa_py import Exa
from crewai_tools import tool
from dotenv import load_dotenv

load_dotenv()

EXA = Exa(api_key=os.environ["EXA_API_KEY"])


@tool
def search(query: str):
	"""Search for a webpage based on the provided query"""
	return EXA.search(f"{query}", use_autoprompt=True, num_results=3)


@tool
def find_similar(url: str):
	"""Search for webpages similar to a given URL.
	The url passed in should be a URL returned from `search`.
	"""
	return EXA.find_similar(url, num_results=10)


@tool
def get_contents(ids: list):
	"""Get the contents of a webpage.
	The ids must be passed in as a list, a list of ids returned from `search`.
	"""
	contents = str(EXA.get_contents(ids))
	contents = contents.split("URL:")
	contents = [content[:1000] for content in contents]
	return "\n\n".join(contents)


TOOLS = [search, find_similar, get_contents]
