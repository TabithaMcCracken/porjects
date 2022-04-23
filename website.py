# make venv, install requests
# imiport the tools for web requests
import requests
from pathlib import Path

# get image and quote

# an image API http://shibe.online/api/shibes
# inspect the API
img_url = "http://shibe.online/api/shibes?count=1"
img = requests.get(img_url).json()[0]
print(img)

# a quotes API http://quotes.stormconsultancy.co.uk/random.json
# inspect the API
quote_url = "http://quotes.stormconsultancy.co.uk/random.json"
quote = requests.get(quote_url).json()["quote"]

# create html structure
html = f"<p>{quote}</p><img src='{img}'>"
print(html)
# create a new file
f = Path().home().joinpath("Documents").joinpath("codingnomads").joinpath("projects").joinpath("index.html")
# write to the file
f.write_text(html)
print(html)


