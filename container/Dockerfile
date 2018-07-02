FROM node:latest

RUN npm install -g @angular/cli
#WORKDIR /app
ADD startapp.sh /startapp.sh
RUN chmod 700 /startapp.sh

EXPOSE 4200

CMD /startapp.sh
