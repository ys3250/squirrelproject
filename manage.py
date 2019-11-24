#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

import os
import sys
import csv
import datetime

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'final_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

def import_squirrel_data(path):
    with open('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        type(readCSV)
    data = []
    for row in readCSV:
        data.append(row)
    data = data[1:]
    for rows in len(cvsdata):
        squirrel.longitude = things[0]
        squirrel.unique_squirrel_id = things[1]
        squirrel.shift = things[4]
        squirrel.date = datetime.datetime.strptime(things[5],'%m%d%Y')
        squirrel.age = things[7]
        squirrel.primary_fur_color = things[8]
        squirrel.location = things[12]
        squirrel.specific_location = things[14]
        squirrel.running = things[15]
        squirrel.chasing = things[16]
        squirrel.climbing = things[17]
        squirrel.eating = things[18]
        squirrel.foraging = things[19]
        squirrel.other_activities = things[20]
        squirrel.kuks = things[21]
        squirrel.quaas = things[22]
        squirrel.moans = things[23]
        squirrel.tail_flags = things[24]
        squirrel.tail_twitches = things[25]
        squirrel.approaches = things[26]
        squirrel.indifferent = things[27]
        squirrel.runs_from = things[28]
        squirrel.save()
if __name__ == '__main__':
    main()
