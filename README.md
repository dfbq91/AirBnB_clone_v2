# HBNB

![HBNB Logo](hbnb-logo.png)

## What is this project about
This is the console /command interpreter for the Holberton Airbnb clone project. The console can be used to store objects in and retrieve objects from a JSON.
Airbnb is an online marketplace that connects people who want to rent out their homes with people who are looking for accommodations in that locale. ... For hosts, participating in Airbnb is a way to earn some income from their property, but with the risk that the guest might do damage to it.

## Going deeper into the project
### Supported classes:
* BaseModel
* User
* State
* City
* Amenity
* Place
* Review

### Commands:
* create - create an object
* show - show an object (based on id)
* destroy - destroy an object
* all - show all objects, of one type or all types
* quit/EOF - quit the console
* help - see descriptions of commands

To start, navigate to the project folder and enter `./console.py` in the shell.

#### Create
`create <class name>`
Ex:
`create BaseModel`

#### Show
`show <class name> <object id>`
Ex:
`show User my_id`

#### Destroy
`destroy <class name> <object id>`
Ex:
`destroy Place my_place_id`

#### All
`all` or `all <class name>`
Ex:
`all` or `all State`

#### Quit
`quit` or `EOF`

#### Help
`help` or `help <command>`
Ex:
`help` or `help quit`

Additionally, the console supports `<class name>.<command>(<parameters>)` syntax.
Ex:
`City.show(my_city_id)`

## Authors
We are students of Holberton School, passionate for computer science.
* Diego Betancourt | [GitHub](https://github.com/dfbq91) | [LinkedIn](https://www.linkedin.com/in/diegofernandobetancourtquintero/)
* Jose Luis Saldarriaga | [GitHub](https://github.com/asoka904) | [LinkedIn](https://www.linkedin.com/in/jose-saldarriaga/)