# knock... knock...

![](https://media.giphy.com/media/4WONcbcxCOYRa/giphy.gif)

Yet another port knock client.


#### Installing

`$ pip install knocker`


#### Running

`$ knocker your.server.domain 8001 8002 8003`


##### Getting help
```
$ knocker -h           
usage: knocker [-h] [-d DELAY] host ports [ports ...]

Knock host and port using tcp connection

positional arguments:
  host                  Hostname or IP address of the host
  ports                 Ports to knock

optional arguments:
  -h, --help            show this help message and exit
  -d DELAY, --delay DELAY
                        Milliseconds between each knock

```

#### Example server

The `example_server.py` is just a socket server that listen 3 different
ports and print a message after receive a ping on it.

```
$ python example_server.py
Listening ports: 49485 38749 42846
```
