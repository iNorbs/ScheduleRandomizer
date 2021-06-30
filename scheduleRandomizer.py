"""
Author: Yours Truly
Title: Schedule Randomizer
Purpose: No human bias should go into scheduling
"""

Monday = ["4:45-9:00", "9:00-1:15", "3:45-7:00", "7:00-10:00"]

#Make a Lifeguard object
class Lifeguard:
    def __init__(self, name="John Doe", rank="LG"):
        self.name = name
        self.rank = rank
        self.hours = 0

    def __str__(self):
        return f"Name: {self.name}, Rank: {self.rank}, Hours: {self.hours}"

    def scheduling(self):
        #Monday
        pass

Norbert = Lifeguard("Norbert")
print(Norbert)
#Start scheduling people at FV first then CC cause 3 people minimum
