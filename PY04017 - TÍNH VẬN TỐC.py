class Rider:
    def __init__(self, name, area, finishTime):
        self.name = name
        self.area = area
        self.hour, self.minute = map(int, finishTime.split(sep=':'))
        self.ma = ''.join(([s[0] for s in self.area.split()] + [s[0] for s in self.name.split()]))
        self.speed = 0

    def Speed(self):
        time = self.hour - 6 + (self.minute / 60)
        self.speed = round(120 / time)

    def __str__(self):
        return f"{self.ma} {self.name} {self.area} {self.speed} Km/h"


def keySort(r: Rider):
    return -r.hour, -r.minute


riderList = []
for r in range(int(input())):
    riderList.append(Rider(input(), input(), input()))
    riderList[r].Speed()
riderList.sort(key=keySort, reverse=True)
print(*riderList, sep='\n')
