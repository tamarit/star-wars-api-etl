from matplotlib.pyplot import title
import requests
import json
from collections import Counter


def get_response(url):
    return json.loads(requests.get(url).text)

def main():

    # 1. Find the ten characters who appear in the most Star Wars films
    character_counter = Counter()
    all_films = get_response("https://swapi.dev/api/films/")["results"]
    for film in all_films:
        character_counter += Counter(film["characters"])
    characters_with_more_apperances = map(
            lambda tuple: tuple[0], 
            character_counter.most_common(10)
        )
    characters_data = []
    for character_url in characters_with_more_apperances:
        character_data = get_response(character_url)
        species_urls = character_data['species']
        species_list = []
        for specie_url in species_urls:
            specie_data = get_response(specie_url)
            species_list.append(specie_data["name"])
        species_str = "-".join(species_list)
        characters_data.append((
                character_data['name'], 
                species_str, 
                character_data['height'], 
                len(character_data['films'])
            ))

    # 2. Sort those ten characters by height in descending order (i.e., tallest first)
    characters_data.sort(
            key=lambda tuple:int(tuple[2]), 
            reverse=True
        )
    # print(characters_data)

    # 3. Produce a CSV with the following columns: name, species, height, appearances
    csv_title = "name,species,height,appearances"
    csv_rows = "\n".join(map(
            lambda tuple: ",".join(map(str, tuple)), 
            characters_data
        ))
    csv_content = f"{csv_title}\n{csv_rows}"
    print(csv_content)

if __name__ == '__main__':
    main()