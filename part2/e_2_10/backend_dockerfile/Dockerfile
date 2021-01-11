
FROM ubuntu:16.04
WORKDIR /mydir
RUN apt-get update && apt-get install -y curl git
RUN curl -sL https://deb.nodesource.com/setup_15.x | bash -
RUN apt-get install -y nodejs
RUN git clone https://github.com/docker-hy/backend-example-docker.git
RUN mv backend-example-docker/* .
RUN npm install
EXPOSE 8000
CMD ["npm", "start"]



