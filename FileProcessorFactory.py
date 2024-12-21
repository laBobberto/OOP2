from FileProcessor import CSVProcessor, XMLProcessor


class FileProcessorFactory:
    @staticmethod
    def getProcessor(filePath):
        if filePath.endswith(".csv"):
            return CSVProcessor()
        elif filePath.endswith(".xml"):
            return XMLProcessor()
        else:
            raise ValueError("Unsupported file format")