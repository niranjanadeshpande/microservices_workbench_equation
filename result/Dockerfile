FROM ubuntu

RUN \
    apt-get update && apt-get install -y python python-dev python-pip python-virtualenv && rm -rf /var/lib/apt/lists/*

ADD result.py /root/result.py

CMD python -u /root/result.py $LISTEN_HOST $LISTEN_PORT
