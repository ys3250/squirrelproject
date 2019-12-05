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
        reader = csv.DictReader(csvfile)
        data = list(reader)
    for things in data:
        squirrel = Squirrel()
        squirrel.unique_squirrel_id = things['Unique Squirrel ID']
        squirrel.longitude = float(things['X'])
        squirrel.latitude = float(things['Y'])
        squirrel.shift = things['Shift']
        squirrel.date = datetime.datetime.strptime(things['Date'],'%m%d%Y')
        squirrel.age = things['Age']
        squirrel.primary_fur_color = things['Primary Fur Color']
        squirrel.location = things['Location']
        squirrel.specific_location = things['Specific Location']
        squirrel.running = things['Running']
        squirrel.chasing = things['Chasing']
        squirrel.climbing = things['Climbing']
        squirrel.eating = things['Eating']
        squirrel.foraging = things['Foraging']
        squirrel.other_activities = things['Other Activities']
        squirrel.kuks = things['Kuks']
        squirrel.quaas = things['Quaas']
        squirrel.moans = things['Moans']
        squirrel.tail_flags = things['Tail flags']
        squirrel.tail_twitches = things['Tail twitches']
        squirrel.approaches = things['Approaches']
        squirrel.indifferent = things['Indifferent']
        squirrel.runs_from = things['Runs from']
        squirrel.save()

class Command(BaseCommand):
    help = 'import data from csv'
    def add_arguments(self, parser):
        parser.add_argument('path', nargs='+', type=str)
    def handle(self, *args, **options):
        for path in options['path']:
            import_(path)
#enable arguments
