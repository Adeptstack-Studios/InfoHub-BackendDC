# InfoHub-BackendDC for sensors
#### for Raspberry Pi.
DC => Door/Window Contact

## Installation
Clone the GitHub repository in `/home/pi/`:
```
git clone https://github.com/Adeptstack-Studios/InfoHub-BackendDC
```

If git is not installed, you can install it this way:
```
sudo apt-get update
sudo apt-get install git
```

Once this is done, navigate to the cloned repository:
```
cd /home/pi/InfoHub-BackendDC
```

The repository contains the installation script, which installs all the necessary applications and libraries when you run it.
```
bash installation.sh
```

However, before the server is started, you create a new screen in which the server then runs. This is done so that the server continues to run even after the ssh session has ended.
```
screen -SO InfoHub
```

Once this has been done and all sensors have been connected correctly, you can put the sensor module into operation. You will find the `start.sh` script file in the repository that you need to execute to start it.
```
bash start.sh
```
And now everything should work :)

## Documentation
*following soon*

## Libraries
The following libraries are used:
```
- from flask import Flask, jsonify, request
- from json import dumps
- import requests
- import threading
- import time
- import os
- gunicorn (server)
```
