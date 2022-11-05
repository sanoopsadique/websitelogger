FROM sanoopsadique/al-py:latest
RUN apk add curl
EXPOSE 80
COPY ./code /weblogger
ARG website
ARG interval
ENTRYPOINT [ "python3","/weblogger/logger.py",website,interval ]