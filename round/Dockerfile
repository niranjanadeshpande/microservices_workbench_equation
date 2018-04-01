FROM ubuntu

RUN \
    apt-get update && apt-get install -y python python-dev python-pip python-virtualenv && rm -rf /var/lib/apt/lists/*

ADD round.py /root/round.py

CMD python -u /root/round.py $LISTEN_HOST $LISTEN_PORT
