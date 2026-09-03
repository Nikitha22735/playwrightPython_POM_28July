import json


def jsonhandling(filePath):
    with open(filePath) as data:
        formattedData = json.load(data)
        return formattedData