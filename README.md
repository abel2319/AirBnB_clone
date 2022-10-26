AirBnB clone
==========================
![Logo ](url "images/logo.png")

I know you were waiting for it: it’s here!

The AirBnB clone project starts now until… the end of the first year. The goal of the project is to deploy on your server a simple copy of the AirBnB website.

You won’t implement all the features, only some of them to cover all fundamental concepts of the higher level programming track.

After 4 months, you will have a complete web application composed by:
    A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
    A website (the front-end) that shows the final product to everybody: static and dynamic
    A database or files that store data (data = objects)
    An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)


Concepts to learn

    Unittest - and please work all together on tests cases
    Python packages concept page
    Serialization/Deserialization
    *args, **kwargs
    datetime



Files and Directories

    models directory will contain all classes used for the entire project. A class, called “model” in a OOP project is the representation of an object/instance.
    tests directory will contain all unit tests.
    console.py file is the entry point of our command interpreter.
    models/base_model.py file is the base class of all our models. It contains common elements:
        attributes: id, created_at and updated_at
        methods: save() and to_json()
    models/engine directory will contain all storage classes (using the same prototype). For the moment you will have only one: file_storage.py.



The console
    create your data model
    manage (create, update, destroy, etc) objects via a console / command interpreter
    store and persist objects to a file (JSON file)

The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine


Examples of the console
Your shell should work like this in interactive mode:

	$ ./console.py
	(hbnb) help

	Documented commands (type help <topic>):
	========================================
	EOF  help  quit

	(hbnb) 
	(hbnb) 
	(hbnb) quit
	$


Data diagram

![Diagram ](url "images/diagram.jpg")

