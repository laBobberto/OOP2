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
                    "cityName": row[0],
                    "buildingFloors": int(row[3])
                })
        return parsedData

class XMLProcessor(FileProcessor):
    def processFile(self, filePath):
        parsedData = []
        xmlTree = ET.parse(filePath)
        rootElement = xmlTree.getroot()
        for itemElement in rootElement.findall("item"):
            parsedData.append({
                "cityName": itemElement.attrib["city"],
                "buildingFloors": int(itemElement.attrib["floor"])
            })
        return parsedData

class FileProcessorFactory:
    @staticmethod
    def getProcessor(filePath):
        if filePath.endswith(".csv"):
            return CSVProcessor()
        elif filePath.endswith(".xml"):
            return XMLProcessor()
        else:
            raise ValueError("Unsupported file format")