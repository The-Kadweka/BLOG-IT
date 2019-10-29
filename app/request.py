import urllib.request
import json
from .models import Quotes


def get_quote():
   '''
   Function to get random quote
   '''
   quote_url = 'http://quotes.stormconsultancy.co.uk/random.json'
   with urllib.request.urlopen(quote_url) as url:
       quote_data = url.read()
       quote_response = json.loads(quote_data)
       quote_result = None
       if quote_response:
           author = quote_response.get('author')
           quote = quote_response.get('quote')
           permalink = quote_response.get('permalink')
           quote_result = Quotes(author, quote, permalink)
       return quote_result