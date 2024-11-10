FROM node:14.18.1

WORKDIR /app

COPY . .

RUN npm install 

RUN npm run build

EXPOSE 8080

CMD ["npm", "start" ]