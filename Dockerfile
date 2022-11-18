FROM sanoopsadique/al-py:latest
RUN apk add curl
EXPOSE 80
COPY ./code / 
ENV website = www.example.com
ENV interval = 30
ENTRYPOINT [ "/log",website,interval ]