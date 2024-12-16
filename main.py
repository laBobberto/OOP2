import time
from FileProcessor import FileProcessorFactory
from StatisticsGenerator import StatisticsGenerator


def main():
    statisticsGenerator = StatisticsGenerator()

    while True:
        print("Enter the path to the file or 'exit' to quit:")
        userInput = input().strip()

        if userInput.lower() == "exit":
            print("Exiting the program.")
            break

        try:
            fileProcessor = FileProcessorFactory.getProcessor(userInput)
            startTime = time.time()
            parsedData = fileProcessor.processFile(userInput)
            duplicateRecords = statisticsGenerator.processData(parsedData)
            processingTime = time.time() - startTime

            statisticsGenerator.displayStatistics(duplicateRecords)
            print(f"\nFile processing time: {processingTime:.2f} seconds")

        except Exception as error:
            print(f"Error: {error}")

if __name__ == "__main__":
    main()
