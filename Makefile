
deploy:
	rsync . django:mysite/. --exclude='.git/' -avzPh

# Run the webserver on the EC2 instance
# Needs to be run as sudo
runserver:
	/usr/bin/python3 ./manage.py runserver 0.0.0.0:80
