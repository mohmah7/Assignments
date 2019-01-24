FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get upgrade -y

RUN apt-get install git  -y

#RUN git clone http://github.com/mohmah7/Assignments

#FROM ubuntu:16.04
#CMD apt-get -y update
#CMD apt-get -y install nodejs
#CMD git clone https://github.com/mawalie/zawya_management.git
CMD cd zawya_management 
CMD npm install
ENTRYPOINT ["nodemon","start"]
