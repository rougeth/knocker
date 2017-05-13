# knock... knock...

![](https://media.giphy.com/media/4WONcbcxCOYRa/giphy.gif)

Yet another port knock client.


#### Installing

`$ pip install knocker`


#### Running

`$ knocker your.server.domain 8001 8002 8003`

#### Example server

The `knock_server_example.py` is just a socket server that listen 3 different  
ports and print a message after a ping on it.

```
$ python knock_server_example.py
Listening ports: 49485 38749 42846
```
