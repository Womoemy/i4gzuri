class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = str(name)
        self.age = int(age)
        self.tracks = tracks
        self.score = float(score)
    
    def change_name(self, change_name):
        self.change_name = change_name
        # print("My old name is", self.name)
        print(f"My new name is {self.change_name}.")
    
    def change_age(self, change_age):
        self.change_age = change_age
        # print("My old age is ", self.age)
        print(f"My new age is {self.change_age} years old.")
    
    def add_track(self, change_tracks):
        self.tracks.append(change_tracks)
        # print(f"My old tracks are {self.tracks[0]} and {self.tracks[1]}")
        print(f"My new track is {self.tracks[-1]}.")

    def get_score(self):
        print(f"My score is {self.score}.")

Bob = Student(name = "Bob", age = 26, tracks = ["FE","BE"], score = 20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
