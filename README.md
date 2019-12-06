Link to Website:
https://tools-for-analytics-e4501.appspot.com/sightings

What is it?

This application keeps track of all the known squirrels found in Central Park. The application can import the data and allow the users to add, update, and delete squirrel data.

Main Features

Our application have the following features:

- Management commands:
	Import: A command that can be used to import the data from a file (in CSV format). The file path should be specified at the command line after the name of the management command.
	e.g. $ python manage.py import_squirrel_data /path/to/file.csv
	Export: A command that can be used to export the data in CSV format. The file path should be specified at the command line after the name of the management command. 
	e.g. $ python manage.py export_squirrel_data /path/to/file.csv
- Views:
	- A view that shows a map that displays the location of the squirrel sightings on an
OpenStreets map​.
		- Located at: ​/map
		- User can specify the number of sighting spots in before showing maps.
	- A view that lists all squirrel sightings with links to edit and add sightings 
		- Located at: ​/sightings
	- A view to update a particular sighting
		- Located at: ​/sightings/<unique-squirrel-id>
	- A view to create a new sighting
		- Located at: ​/sightings/add
	- A view to delete a sighting
		- Located at: ​/sightings/<unique-squirrel-id>
	- A view with general stats about the sightings
		- Located at: ​/sightings/stats


Dependencies
Run below command in order to get all of the required packages for running the site properly.
pip install -r requirements.txt

Contributors
Project Group 15 in Section 1 (16:10 - 18:40)
UNIs: [si2353,ys3250]