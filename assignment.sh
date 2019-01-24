#!/bin/bash

sudo apt-get update -y
sudo apt-get upgrade -y

sudo amazon-linux-extras install docker
sudo service docker start
sudo usermod -a -G docker ec2-user

#cd  assignments/Assignments

#sudo git pull

#sudo cp index.html /var/www/html

#sudo cp styleA.css /var/www/html
