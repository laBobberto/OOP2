import csv
import xml.etree.ElementTree as ET


class FileProcessor:
    def processFile(self, filePath):
        raise NotImplementedError("This method should be overridden in a subclass")

class CSVProcessor(FileProcessor):
    def processFile(self, filePath):
        parsedData = []
        with open(filePath, encoding="utf-8") as csvFile:
            csvReader = csv.reader(csvFile, delimiter=';')
            next(csvReader)
            for row in csvReader:
                parsedData.append({
                    "city": row[0],
                    "street": row[1],
                    "house": int(row[2]),
                    "floor": int(row[3])
                })
        return parsedData

class XMLProcessor(FileProcessor):
    def processFile(self, filePath):
        parsedData = []
        xmlTree = ET.parse(filePath)
        rootElement = xmlTree.getroot()
        for itemElement in rootElement.findall("item"):
            parsedData.append({
                "city": itemElement.attrib["city"],
                "street": itemElement.attrib["street"],
                "house": int(itemElement.attrib["house"]),
                "floor": int(itemElement.attrib["floor"])
            })
        return parsedData
