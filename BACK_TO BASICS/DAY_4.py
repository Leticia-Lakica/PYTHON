# NESTED LOOOPS
# This is basically a loop within a loop

# OBJECTED ORIENTED PROGRAMMIN
# Object, a bundle of related characteristics and methods
from abc import ABC, abstractmethod

class Movie:
    def __init__(self,title,year,duration,genre, is_available):
        self.title = title
        self.year = year
        self.duration = duration
        self.genre = genre
        self.is_available = is_available

    def play(self):
        print(f"You are watching {self.title}")


    def pause(self):
        print(f"Press Enter to continue watching {self.title}")

    def search(self):
        if self.is_available == True:
            print(f"{self.title} found. Tap play to watch")
        else:
            print(f"{self.tile} not found")

M1 = Movie("Lost", 2012, "1:54:00", "Adventure", True)

print(M1.title)

M1.play()
M1.pause()
M1.search()

# # INHERITANCE
# # The ability of a class to inherite the traites of another

class Media(ABC):
    def __init__(self,title,year,genre, is_available):
        self.title = title
        self.year = year
        self.genre = genre
        self.is_available = is_available

    @abstractmethod
    def play(self):
        pass


    def pause(self):
        print(f"Press Enter to continue watching {self.title}")

    def search(self):
        if self.is_available == True:
            print(f"{self.title} found. Tap play to watch")
        else:
            print(f"{self.tile} not found")

class Movie(Media):
    def __init__(self, title, year, genre, is_available,runtime):
        super().__init__(title, year, genre, is_available)
        self.runtime = runtime

    def play(self):
        return f"Play {self.title}"




class Series(Media):
    def __init__(self, title, year, genre, is_available,seasons, episodes):
        super().__init__(title, year, genre, is_available)
        self.seasons = seasons
        self.episodes = episodes

    def play(self):
        return "Select Season and episode"

S1 = Series("Supernatural", 2009, "Thriller", True, "14", "22")

S1.play()
print(S1.seasons)

M1 = Movie("Lost", 2012, "1:54:00", "Adventure", True)
M1.play()

