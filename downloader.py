import os
import requests
from datetime import datetime
import time

def download_inputs():
    day_of_month = datetime.today().day
    current_year = datetime.today().year
    home = os.environ.get("HOME")
    # Download all inputs
    for year in range(2015, current_year+1):
        year_dir = os.path.join(home, "advent-of-code", str(year))
        if not os.path.exists(year_dir):
            os.mkdir(year_dir)
        for day in range(1, 26):
            if year == current_year and day > day_of_month:
                return True
            day_str = str(day).zfill(2)
            day_dir = os.path.join(year_dir, day_str)
            if not os.path.exists(day_dir):
                os.mkdir(day_dir)
            filepath = os.path.join(day_dir, f"{day_str}.txt")
            if not os.path.exists(filepath):
                download_day(year, day, filepath)

def download_day(year, day, filepath):
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    data = requests.get(url)
    open(filepath, "wb").write(data.content)
    print(f"downloading from {url} to {filepath}")
    time.sleep(1)

download_inputs()
