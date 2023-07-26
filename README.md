# Task Manager

Django project for managing tasks and workers in Task Manager

## Check it out!

[Task Manager Deployed to Render](https://task-manager-wgxq.onrender.com)

User for testing:

```shell
username: user
password: pass123word
```

## Installation

Python3 must already be installed!

```shell
git clone https://github.com/vitalii-babiienko/task-manager
cd task-manager
python3 -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)
pip install -r requirements.txt
python3 manage.py runserver
```

## Run the tests

```shell
python3 manage.py test
```

## Features

* Authentication functionality for Worker/User
* Managing tasks, task types, workers, and positions directly from the website
* Powerful admin panel for advanced management
