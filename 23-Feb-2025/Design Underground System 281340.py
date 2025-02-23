# Problem: Design Underground System - https://leetcode.com/problems/design-underground-system/

class UndergroundSystem:
    def __init__(self):
        self.check_ins = {}
        self.travel_times = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_ins[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.check_ins.pop(id)
        travel_key = (start_station, stationName)
        travel_time = t - start_time

        if travel_key in self.travel_times:
            total_time, count = self.travel_times[travel_key]
            self.travel_times[travel_key] = (total_time + travel_time, count + 1)
        else:
            self.travel_times[travel_key] = (travel_time, 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_time, count = self.travel_times[(startStation, endStation)]
        return total_time / count
