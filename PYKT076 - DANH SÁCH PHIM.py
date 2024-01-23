class MovieType:
    ID = 1

    def __init__(self, name):
        self.name = name
        if MovieType.ID < 10:
            self.id = 'TL00' + str(MovieType.ID)
            MovieType.ID += 1
        elif MovieType.ID <100:
            self.id = 'TL0' + str(MovieType.ID)
            MovieType.ID += 1
        else:
            self.id = 'TL' + str(MovieType.ID)
            MovieType.ID += 1


class Movie:
    ID = 1

    def __init__(self, movieTypeID, date, movieName, ep):
        self.typeID = movieTypeID
        self.date = date
        self.name = movieName
        self.ep = ep
        self.day, self.month, self.year = map(int, self.date.split(sep="/"))
        if Movie.ID < 10:
            self.id = 'P00' + str(Movie.ID)
            Movie.ID += 1
        elif Movie.ID <100:
            self.id = 'P0' + str(Movie.ID)
            Movie.ID += 1
        else:
            self.id = 'P' + str(Movie.ID)
            Movie.ID += 1

    def __str__(self):
        return f"{self.id} {type[self.typeID]} {self.date} {self.name} {self.ep}"


n, m = map(int, input().split())
type = {}
for i in range(n):
    theLoai = MovieType(input())
    type[theLoai.id] = theLoai.name

movieList = []
for i in range(m):
    movieList.append(Movie(input(), input(), input(), int(input())))
movieList.sort(key=lambda movie: (movie.year, movie.month, movie.day, movie.name, -movie.ep))
print(*movieList, sep='\n')
