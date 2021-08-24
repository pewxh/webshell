# Webshell

## Your ON THE GO solution to access shell remotely !!!

<p align="center">
<h3>    
  <img src="demo/sample.gif" alt="screenshot">
  This setup allows you to access the shell of your system via web. <br>
  Any sytem command can be executed using this webapp (or API).
</h3>
</p>
<p align="center"><a href="#" target="_blank"><img src="https://forthebadge.com/images/badges/uses-html.svg" alt="html" /></a>&nbsp;&nbsp;<a href="# target="_blank"><img src="https://forthebadge.com/images/badges/made-with-python.svg" alt="python" /></a>&nbsp;
<a href="# target="_blank"><img src="https://forthebadge.com/images/badges/no-ragrets.svg" alt="no ragrets" /></a>&nbsp;</a>&nbsp;
<a href="# target="_blank"><img src="https://forthebadge.com/images/badges/fo-sho.svg" alt="foso" /></a>&nbsp;
</p>

## ⚡️ Quick start

<hr>

First of all, [download](https://www.python.org/downloads/) and install **Python**. <br>
Install Flask module using pip/pip3.

```pip
pip3 install flask
```

Next, run the file (called `app.py`) using python/python3 to start your **Flask Server**. <br>
Use **localhost:5000** to visit the app.

```bash
python3 ./app.py
```

### 🐳 Docker

You can use docker container to launch the app.
Feel free to use this [Docker image](https://hub.docker.com/repository/docker/pewxh/webshell) and run CLI from isolated container:

```bash
docker run -d -p 5000:5000 pewxh/webshell
```

<i><b>- p</b> is used to publish the port number 5000 of the container to that of the hostmachine.</i>
