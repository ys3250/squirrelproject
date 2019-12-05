
import os
import sys
import csv
import datetime
from django.core.management.base import BaseCommand
import sqlite3

INTERPRETER = "/usr/bin/python"
def export_(path):
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    #enable sql command
    # columns = cur.execute("SELECT * FROM sightings_squirrel;").description
    column_name = ['Unique Squirrel ID','Shift','Date','Age','Y','X','Primary Fur Color','Location','Specific_Location',
    'Running','Chasing','Climbing','Eating','Foraging','Other Activities','Kuks', 'Quaas', 'Moans', 'Tail flags', 'Tail twitches',
    'Approaches', 'Indifferent', 'Runs from']
    # for things in columns:
    #     column_name.append(things[0])
    # #get the column name
    squirrel_data = cur.execute("SELECT * FROM sightings_squirrel;").fetchall()
    #get the squirrel data
    data = [column_name]
    for thing in squirrel_data:
        row = list(thing)
        row[2] = datetime.datetime.strptime(row[2],'%Y-%m-%d %H:%M:%S').strftime('%m%d%Y')
        data.append(row)
    with open(path,'w',newline='') as fp:
        a= csv.writer(fp,delimiter=',')
        a.writerows(data)

class Command(BaseCommand):
    help = 'export data to csv'
    def add_arguments(self, parser):
        parser.add_argument('path', nargs='+', type=str)
    def handle(self, *args, **options):
        for path in options['path']:
            export_(path)
# enable arguments afterwards
