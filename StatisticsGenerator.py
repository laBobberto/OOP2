from collections import Counter, defaultdict


class StatisticsGenerator:
    def __init__(self):
        self.cityFloorStatistics = defaultdict(Counter)

    def processData(self, parsedData):
        duplicateEntriesCounter = Counter(
            (entry['city'], entry['street'], entry['house'], entry['floor']) for entry in parsedData
        )

        duplicateRecords = {record: count for record, count in duplicateEntriesCounter.items() if count > 1}

        self.cityFloorStatistics = defaultdict(lambda: defaultdict(int))

        for entry in parsedData:
            self.cityFloorStatistics[entry["city"]][entry["floor"]] += 1

        return duplicateRecords

    def displayStatistics(self, duplicateRecords):
        print("\nDuplicate Entries:")
        for record, count in duplicateRecords.items():
            print(f"{record}: {count} times")

        print("\nNumber of Buildings by Floor Count in Each City:")
        for cityName, floorStatistics in self.cityFloorStatistics.items():
            print(f"{cityName}: {dict(floorStatistics)}")