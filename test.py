from io import StringIO
import csv

import main


############################################################
# TEST CASES
############################################################


FINAL_RESPONSE = main.main()
reader_execution = list(csv.reader(StringIO(FINAL_RESPONSE["files"][main.CSV_FILE])))

def test_csv_size():
    assert len(list(reader_execution)) == main.CSV_SIZE + 1

def test_csv_content():
    reader_local = []
    with open(main.CSV_FILE) as csvfile:
        reader_local += csv.reader(csvfile)
    assert list(reader_execution) == list(reader_local)