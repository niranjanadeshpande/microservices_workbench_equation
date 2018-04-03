FROM ubuntu

RUN \
    apt-get update && apt-get install -y python python-dev python-pip python-virtualenv && rm -rf /var/lib/apt/lists/*

ADD integral.py /root/integral.py

CMD python -u /root/integral.py $LISTEN_HOST $LISTEN_PORT $SEND_HOST $SEND_PORT
