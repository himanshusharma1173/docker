#use latest ubuntu image as the base image
FROM ubuntu:latest

#set working directory inside the container to /app
WORKDIR /app

#copy all the files from the current directory on the host to the /app directory inside the container
COPY . /app

#update package list and install python3 and pip
RUN apt-get update && apt-get install -y python3 python3-pip

#set an environment variable called NAME with value Himanshu
ENV NAME Himanshu

#command to run when the container starts
CMD ["python3", "app.py"]
