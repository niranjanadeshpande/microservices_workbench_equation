FROM ubuntu

RUN \
    apt-get update && apt-get install -y python python-dev python-pip python-virtualenv && rm -rf /var/lib/apt/lists/*

ADD x.py /root/x.py

CMD python -u /root/x.py $SEND_HOST_ONE $SEND_PORT_ONE $SEND_HOST_TWO $SEND_PORT_TWO $N
