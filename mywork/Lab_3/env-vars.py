#!/usr/bin/python3

import os

favorite_color = input("What is your favorite color? ")
hometown = input("What is your hometown? ")
dream_job = input("What is your dream job? ")

os.environ["FAVORITE_COLOR"] = favorite_color
os.environ["HOMETOWN"] = hometown
os.environ["DREAM_JOB"] = dream_job

print("\nStored Environment Variables:")
print("Favorite Color:", os.getenv("FAVORITE_COLOR"))
print("Hometown:", os.getenv("HOMETOWN"))
print("Dream Job:", os.getenv("DREAM_JOB"))
