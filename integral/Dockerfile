FROM ubuntu

RUN \
    apt-get update && apt-get install -y python python-dev python-pip python-virtualenv && rm -rf /var/lib/apt/lists/*

ADD integral.py /root/integral.py

CMD python -u /root/integral.py $SEND_HOST $SEND_PORT
