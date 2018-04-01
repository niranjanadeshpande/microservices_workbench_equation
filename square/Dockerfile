FROM ubuntu

RUN \
    apt-get update && apt-get install -y python python-dev python-pip python-virtualenv && rm -rf /var/lib/apt/lists/*

ADD square.py /root/square.py

CMD python -u /root/square.py $SEND_HOST $SEND_PORT
