Py3alive
========

A client-server script set including Py3status plugin capabilities to keep track of the status (online or offline) of remote machines.

USEAGE
=====

1: Clone the repo onto both your remote machine, and your local machine.

2: On the remote - Edit alive_server.conf so it looks like this:

[Public IPv4 address of remote machine or domain name or private IPv4]
[Port]

The IP/domain name needs to be on the first line, the port on the second.
You will need to forward the port to the remote machine.

3: Run the server on the remote machine. It is advised that you fork the process from the terminal with an &:

    $ python alive_server.py &

4: Open alive_client.conf on your local machine. Enter the same IP/domain name and port as you did on the server. You do not need to port forward the client.

5: Copy both alive_client.py and alive_client.conf into whatever directory your install of Py3Status looks for plugins.

6: Restart Py3Status.
