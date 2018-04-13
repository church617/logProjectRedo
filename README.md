# logProjectRedo

this is a resubmission of the log analysis project for Udacity

This is the third project of the Udacity Full Stack Nanodegree.

To run correctly, the followin views must be created:

create view articleViews as select articles.author, count(*) as views from articles join log on log.path like concat('%', articles.slug, '%') where log.status = '200 OK' group by articles.author;

create view dailyRequests as select count(*) as requests, date(TIME) as date from log where status = '200 OK' group by date order by requests desc;

create view dailyErrors as select date(TIME) as date, count(*) as errors from log where log.status = '404 NOT FOUND' group by date order by errors desc;

You will need to install the following: 
  Python3 Vagrant VirtualBox

Setup: 
  First install Vagrant and VirtualBox Clone repository

To properly run: 
  Launch Vagrant by running vagrant up, then login with vagrant ssh 
  Then run psql -d news -f newsdata.sql to connect to the database 
  To execute the program, run python3 logProject.py from command line
