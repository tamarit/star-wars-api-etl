import requests
import json
from collections import Counter

CSV_FILE = "star_wars.csv"
CSV_SIZE = 10

def get_response(url):
    return json.loads(requests.get(url).text)

def get_most_common_characters(size=None):
    character_counter = Counter()
    all_films = get_response("https://swapi.dev/api/films/")["results"]
    for film in all_films:
        character_counter += Counter(film["characters"])
    # characters_with_more_apperances = map(
    #         lambda tuple: tuple[0], 
    #         character_counter.most_common(size)
    #     )
    return character_counter.most_common(size)


# CURRENT TIME USED: ~ 1:30 hours
# TODO
# *docker
# * instructions

def main():

    # 1. Find the ten characters who appear in the most Star Wars films
    characters_data = []
    for character_url, appearances in get_most_common_characters(size=CSV_SIZE):
        character_data = get_response(character_url)
        species_urls = character_data['species']
        species_list = []
        for specie_url in species_urls:
            specie_data = get_response(specie_url)
            species_list.append(specie_data["name"])
        species_str = "-".join(species_list)
        assert appearances == len(character_data['films'])
        characters_data.append((
                character_data['name'], 
                species_str, 
                character_data['height'], 
                appearances
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
    with open(CSV_FILE, 'w') as handle:
        handle.write(csv_content)

    # 4. Send the CSV to httpbin.org
    with open(CSV_FILE, 'rb') as handle:
        response = requests.post('http://httpbin.org/post', files={CSV_FILE: handle})
    return json.loads(response.text)

if __name__ == '__main__':
    main()