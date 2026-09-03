import csv
import json

import pytest

from utils.jsonhandling import jsonhandling


def test_jsonhandling():
    with open('testData\\creds.json') as data:
        formattedData = json.load(data)
        print(formattedData["positiveCreds"]["password"])


def test_jsonHandling2():
    data = jsonhandling('testData\\creds.json')
    print(data)

@pytest.mark.dh
def test_csvhandling():
    with open('testData\\credentails.csv') as data:
        formattedData =csv.DictReader(data)
        values = []
        for i in formattedData:
            values.append(i)
        print(values[1]["username"])



