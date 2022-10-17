import requests
import json
from collections import Counter


def get_response(url):
    return json.loads(requests.get(url).text)["results"]

def main():
    character_counter = Counter()
    all_films = get_response("https://swapi.dev/api/films/")
    for film in all_films:
        # all_character = all_character.union(set(film["characters"]))
        character_counter += Counter(film["characters"])
    characters_with_more_apperances = character_counter.most_common(10)



if __name__ == '__main__':
    main()