# AirBnB clone - RESTful API
The RESTful API is the third segment of the AirBnB project at ALX Africa (Holberton School) that will collectively cover fundamental concepts of higher level programming. The goal of AirBnB project is to eventually deploy a server, a simple copy of the AirBnB website.

#### Functionalities of this command interpreter:
* Create a new object (example: a new User of a new Place)
* Retrieve an object from a file, a database, etc...
* Do operations on objects (count, compute stats, etc...)
* Update attributes of an object
* Destroy an object

## Table of Content
* [Environment](#environment)
* [Installation](#installation)
* [File Descriptions](#file-descriptions)
* [Usage](#usage)
* [Examples of use](#examples-of-use)
* [Bugs](#bugs)
* [Authors](#authors)
* [License](#license)

## Environment
This project is interpreted/tested on Ubuntu 20.04 LTS using python3 (version 3.8.5)

## Installation
* Clone this repository: `git clone "https://github.com/malishben360/AirBnB__clone.git"``
* Access AirBnB directory: `cd AirBnB_clone`
* Run bnb(interactively): `./console.py` and enter command
* Run bnb(non-interactively): `echo "<command>" | ./console.py`

## File Descriptions
#### `models/` - directory contains classes used for this project:
[base_model.py](/models/base_model.py) - The BaseModel class from which future classes will be derived
* `def __init__(self, *args, **kwargs)` - Initialization of the basw model* `def __str__(self)` - String representation of the BaseModel class
* `def save(self)` - Updates the attribute `updated_at` with the current datetime
* `def to_dict(self)` - Returns a dictionary containing all keys/values of the instance
