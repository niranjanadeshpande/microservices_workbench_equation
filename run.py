import os
from subprocess import call

#call(,)

call('docker network create --driver bridge sample-sendr-rcv-test',shell="True")

#build 'em all
call('docker build -t result /home/niranjana/microservices/Equation_Microservices/microservices_workbench_equation/result/',shell="True")
call('docker build -t square /home/niranjana/microservices/Equation_Microservices/microservices_workbench_equation/square/',shell="True")
call('docker build -t round /home/niranjana/microservices/Equation_Microservices/microservices_workbench_equation/round/',shell="True")
call('docker build -t integral /home/niranjana/microservices/Equation_Microservices/microservices_workbench_equation/integral/',shell="True")

#run result first

call('docker run --name="result" --env LISTEN_HOST="0.0.0.0" --env LISTEN_PORT_ONE="7071" --env LISTEN_PORT_TWO="8080" --network=sample-sendr-rcv-test -d result',shell="True")

#run square next

call('docker run --name="square" --env SEND_HOST="result" --env SEND_PORT="8080" --network=sample-sendr-rcv-test -d square',shell="True")


#run round next
call('docker run --name="round" --env LISTEN_HOST="0.0.0.0" --env LISTEN_PORT="7070" --env SEND_HOST="result" --env SEND_PORT="7071" --network=sample-sendr-rcv-test -d round',shell="True")

#run integral next
call('docker run --name="integral" --env SEND_HOST="round" --env SEND_PORT="7070" --network=sample-sendr-rcv-test -d integral',shell="True")






