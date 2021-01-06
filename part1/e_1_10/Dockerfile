FROM ubuntu:16.04
WORKDIR /mydir
COPY frontend-example-docker .
RUN apt-get update && apt-get install -y curl
RUN curl -sL https://deb.nodesource.com/setup_15.x | bash -
RUN apt-get install -y nodejs
RUN npm install
RUN npm install -g serve
RUN npm run build
EXPOSE 5000
ENTRYPOINT ["serve"]
CMD ["-s", "-l", "5000", "dist"]


