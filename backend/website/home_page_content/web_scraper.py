from serpapi import GoogleSearch

from website.settings import SERPAPIKEY

params = {
  "engine": "google_maps",
  "ll": "@28.615813906365094, 77.37481583619687,14z",
  "q": "PaddleLift",
  "api_key": SERPAPIKEY
}

def get_reviews():
  search = GoogleSearch(params)
  results = search.get_dict()['place_results']['user_reviews']['most_relevant']
  return results
