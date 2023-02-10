import random

feet_in_mile = 5280
meter_in_kms = 1000
beatles = ["Jhon Lennon", "Paul McCartney", "George Harrinson", "Ringo Star"]

def get_file_ext(filename):
    return filename[filename.index(".") + 1:]

def roll_dice(num):
    return random.randint(1, num)