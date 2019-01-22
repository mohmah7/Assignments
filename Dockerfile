FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get upgrade -y

RUN apt-get install apache2 -y
RUN apt-get install git -y

RUN git clone http://github.com/mohmah7/Assignments 

CMD ["/etc/init.d/apache2 start"]
