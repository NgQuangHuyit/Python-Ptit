from datetime import datetime


def calculate_minutes_difference(time_str1, time_str2):
    time_format = "%H:%M"

    try:
        # Chuyển đổi chuỗi thời gian thành đối tượng datetime
        time1 = datetime.strptime(time_str1, time_format)
        time2 = datetime.strptime(time_str2, time_format)

        # Tính toán khoảng thời gian giữa hai thời điểm
        time_difference = abs(time2 - time1)

        # Tính số phút từ khoảng thời gian
        total_minutes = time_difference.seconds // 60

        return total_minutes

    except ValueError:
        return None


class TramDo:
    ID = 1

    def __init__(self, name):
        self.name = name
        self.time = 0
        self.amount = 0
        self.avg = 0
        if TramDo.ID < 10:
            self.id = 'T' + '0' + str(TramDo.ID)
            TramDo.ID += 1
        else:
            self.id = 'T' + str(TramDo.ID)
            TramDo.ID += 1

    def update(self, start, finish, amount):
        self.amount += amount
        self.time += calculate_minutes_difference(start, finish)
        self.avg = self.amount / self.time * 60

    def __str__(self):
        return f"{self.id} {self.name} {self.avg:.2f}"


dic = {}
for t in range(int(input())):
    name = input()
    start = input()
    end = input()
    mes = int(input())
    if name not in dic:
        dic[name] = TramDo(name)
    dic[name].update(start, end, mes)
ls = list(dic.values())
ls.sort(key=lambda x: x.id)
print(*ls, sep='\n')
