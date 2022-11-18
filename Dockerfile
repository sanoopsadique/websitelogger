FROM sanoopsadique/al-py:latest
RUN apk add curl
RUN mkdir /logger
EXPOSE 80
COPY ./code / 
VOLUME [ "/logger" ]
ENV website=www.example.com
ENV interval=30
ENTRYPOINT [ "/log" ]