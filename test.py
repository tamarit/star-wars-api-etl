from io import StringIO
import csv

import main

############################################################
# COMMON DATA
############################################################

csv_content = list(csv.reader(StringIO(main.main()["files"][main.CSV_FILE])))

############################################################
# TEST CASES
############################################################

def test_csv_size():
    assert len(csv_content) == main.CSV_SIZE + 1

def test_csv_content():
    reader_local = []
    with open(main.CSV_FILE) as csvfile:
        reader_local += csv.reader(csvfile)
    assert csv_content == list(reader_local)

def test_csv_order():
    sorted_result = sorted(
            csv_content[1:], 
            key=lambda tuple: int(tuple[2]), 
            reverse=True
        )
    assert csv_content[1:] == sorted_result

def test_csv_most_common_in():
    print(list(main.get_most_common_characters(size=main.CSV_SIZE)))
    expected_appearecenes = list(map(
            lambda tuple: tuple[1],
            main.get_most_common_characters(size=main.CSV_SIZE)
        ))
    print(expected_appearecenes)
    print(csv_content)
    for row in csv_content[1:]:
        if int(row[3]) in expected_appearecenes:
            expected_appearecenes.remove(int(row[3]))
    assert expected_appearecenes == []
