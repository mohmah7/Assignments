#!/bin/bash

sudo apt-get update -y
sudo apt-get upgrade -y

sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg2 \
    software-properties-common
    
    
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"


sudo apt-get install docker-ce

#sudo amazon-linux-extras install docker•udo service docker start
#sudo usermod -a -G docker ec2-user

#cd  assignments/Assignments

#sudo git pull

#sudo cp index.html /var/www/html

#sudo cp styleA.css /var/www/html
