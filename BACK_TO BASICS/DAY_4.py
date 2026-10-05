# NESTED LOOOPS
# This is basically a loop within a loop

# OBJECTED ORIENTED PROGRAMMIN
# Object, a bundle of related characteristics and methods

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