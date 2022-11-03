FROM sanoopsadique/al-py:latest
RUN apk add curl
EXPOSE 80
COPY ./code /weblogger
COPY settings.txt /weblogger/settings
ENTRYPOINT [ "./weblogger/run.sh" ]