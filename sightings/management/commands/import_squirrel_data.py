#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import csv
import datetime
from django.core.management.base import BaseCommand #neccessary
from sightings.models import Squirrel

INTERPRETER = "/usr/bin/python"

def import_(path):
    with open(path) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        data = []
        for row in readCSV:
            data.append(row)
    data = data[1:]
    for things in data:
        try:
            squirrel = Squirrel()
            squirrel.longitude = float(things[0])
            squirrel.latitude = float(things[1])
            squirrel.unique_squirrel_id = things[2]
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
        except:
            pass

class Command(BaseCommand):
    help = 'import data from csv'
    def add_arguments(self, parser):
        parser.add_argument('path', nargs='+', type=str)
    def handle(self, *args, **options):
        for path in options['path']:
            import_(path)
#enable arguments
