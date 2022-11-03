FROM sanoopsadique/al-py:latest
RUN apk add curl
EXPOSE 80
COPY ./code /weblogger
ENTRYPOINT [ "/weblogger/run.sh" ]