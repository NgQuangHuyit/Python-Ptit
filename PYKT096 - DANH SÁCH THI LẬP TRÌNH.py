class Team:
    ID = 1

    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.id = "Team{:0>2}".format(Team.ID)
        Team.ID += 1

    def __str__(self):
        return self.name


class Contestant:
    ID = 1

    def __init__(self, name, team):
        self.name = name
        self.team = team
        self.id = "C{0:0>3}".format(Contestant.ID)
        Contestant.ID += 1

    def __str__(self):
        return f"{self.id} {self.name} {self.team} {self.team.school}"


teamList = {}
for i in range(int(input())):
    team = Team(input(), input())
    teamList[team.id] = team

contestantList = []
for i in range(int(input())):
    contestantList.append(Contestant(input(), teamList[input()]))

contestantList.sort(key= lambda cont: cont.name)
print(*contestantList, sep='\n')
'''
2
BAV_MIS
Banking Academy of Vietnam
FTU Knights1
Foreign Trade University
6
Le Trung Toan
Team01
Nguyen Trinh Quoc Long
Team01
Giang Minh Tung
Team01
Nguyen Hang Giang
Team02
Nguyen Thanh Nhan
Team02
Nguyen Viet Duc
Team02
'''