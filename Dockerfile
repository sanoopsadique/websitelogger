FROM sanoopsadique/al-py:latest
RUN apk add curl
EXPOSE 80
COPY ./code / 