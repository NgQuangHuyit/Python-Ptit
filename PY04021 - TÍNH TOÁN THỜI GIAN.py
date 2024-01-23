class Gamer:
    def __init__(self, id, name, inTime, outTime):
        self.timeDelta = 0
        self.id = id
        self.name = name
        self.inTime = inTime
        self.outTime = outTime

    def calTime(self):
        timedelta = -(int(self.inTime[:2]) * 60 + int(self.inTime[3:])) + (int(self.outTime[:2]) * 60 + int(self.outTime[3:]))
        self.timeDelta = timedelta

    def __str__(self):
        return f"{self.id} {self.name} {self.timeDelta // 60} gio {self.timeDelta % 60} phut"


gamerList = []
for t in range(int(input())):
    gamerList.append(Gamer(input(), input(), input(), input()))
    gamerList[t].calTime()
gamerList.sort(key=lambda gamer: -gamer.timeDelta)
print(*gamerList, sep='\n')
