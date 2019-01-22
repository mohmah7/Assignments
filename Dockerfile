FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get upgrade -y

RUN apt-get install apache2 -y
RUN apt-get install git -y

RUN git clone http://github.com/mohmah7/Assignments 

RUN cp Assignments/index.html /var/www/html/
RUN cp Assignments/12AEDCF4-8EB5-4E78-80CC-69B80297EA3B.jpeg /var/www/html/

##CMD ["/etc/init.d/apache2 start"]
