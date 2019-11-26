
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
    columns = cur.execute("SELECT * FROM sightings_squirrel;").description
    column_name = []
    for things in columns:
        column_name.append(things[0])
    # available_table=(mycur.fetchall())
    squirrel_data = cur.execute("SELECT * FROM sightings_squirrel;").fetchall()
    data = [column_name]
    for thing in squirrel_data:
        data.append(list(thing))
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
