# Data Returner
This is a data returner. You can use config.json to config the server.

## Return data

This server can return a json.

- ip: The client's IP address.
- port: The client's request port.

Example:

`{'ip':127.0.0.1,"port":58341}`

##Config

> config.json

`{"port":22024,"max",5}`

You can change the port and max client count. Config the server and run the script.

## Run

> Windows

Run `server.exe`.

> Linux

Run `python3 ./server.py`.

> Mac OS

Run `python3 ./server.py`

---
_Author:Kangbo Hua_
