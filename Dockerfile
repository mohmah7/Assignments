FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get upgrade -y

RUN apt-get install git  -y

#RUN git clone http://github.com/mohmah7/Assignments

#FROM ubuntu:16.04
#CMD apt-get -y update
RUN apt-get -y install nodejs npm
RUN git clone https://github.com/mawalie/zawya_management.git &&  cd zawya_management  && npm install -g nodemon && npm install
#ENTRYPOINT ["tail","/dev/null"]
