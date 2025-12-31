# Overview

This project is a baseline docker configuration for creating a django website with the following features:

* HTTPS support.
* MySQL. Could be adapted to postgres as well if you like.
* Support for phpmyadmin. Very nice way to inspect and work with a MySQL database.
* Based on docker compose pipeline: download, install docker and docker compose, run `docker compose up`.
* Batteries included. Self signed certs and key material provided so you can play with this without
  dealing with that. Obviously, I am not using these for production (sorry hackers), and you shouldn't either. 
  Your site should use certs obtained from a legit source, e.g., digicert.

# Architecture

* The project is the standard, django-generated hello world project. Obviously, you will want to use
  your own django project.
* Uses nginx reverse proxies, and gunicorn (because using the dev server provided by django is not
  the right answer as documented by the django project). If your current project is supporting
  django via apache2, gunicorn is a far better way to go.
* Separate docker containers for phpmyadmin, mysql, and django. Both phpmyadmin and django are
  supported by their own nginx reverse proxies, which themselves are in two separate containers.

# How to Use

* clone this repo
* install docker server and docker compose (search the web for instructions)
* Run `docker compose up`
* Open a web browser to https://localhost to get the django hello world.
* Run `docker exec -it <docker container id> python manage.py createsuperuser` and follow the instructions
  to create a django admin account, then visit https://localhost/admin to log in. Use `docker container list`
  to get the container ID (a hex number).
* Open a web browser to https://localhost:8443 to poke around the db with phpmyadmin. User: django_user
  and password: django_password to get in.

# Packet sniffing

* The docker compose file defines a service which sniffs the internal network created by docker and
  captures packets to a pcap file suitable for debugging the net configuration via `tcpdump` and 
  `wireshark`. Packet capture will be saved to a local file on your host in the directory `./tcpdump_data`
  I used this to inspect packet headers when debugging my CSRF config in django and nginx. What's cool
  about this is the local network traffic between the reverse proxy and gunicorn is HTTP so capturing 
  the local network allows you to inspect the packets after they are decrypted. 

