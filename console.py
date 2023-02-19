#!/usr/bin/env python3
"""
A module that contains the entry point of the command interpreter.
"""

import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
classes = {'BaseModel': BaseModel, 'User': User,
           'State': State, 'City': City, 'Place': Place,
           'Amenity': Amenity, 'Review': Review
           }


class HBNBCommand(cmd.Cmd):
    """ Defines the command hooks. """

    prompt = '(hbnb) '

    def do_all(self, line):
        """Prints all string representation of all instances
        based or not on the class name.\n"""
        args = line.split()
        if len(args) == 0:
            objects = models.storage.all()
            object_array = []
            if not len(objects) == 0:
                for key, value in objects.items():
                    instance = '%s' % value
                    object_array.append(instance)
                print(object_array)
            else:
                pass
        elif args[0] in classes:
            objects = models.storage.all()
            class_name = args[0]
            object_array = []
            if not len(objects) == 0:
                for key in objects.keys():
                    if key.startswith(class_name):
                        instance = '%s' % objects[key]
                        object_array.append(instance)
                    else:
                        continue
                print(object_array)
            else:
                pass
        else:
            print("** class doesn't exist **")

    def do_create(self, line):
        """Creates an instance of a class and save to JSON file.\n"""
        args = line.split()
        class_name = ""
        if len(args) > 0:
            class_name = args[0]
        else:
            class_name = line

        if not class_name:
            print("** class name missing **")
        elif class_name in classes:
            instance = classes[class_name]()
            models.storage.save()
            print("%s" % instance.id)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instance based on the class name and id by
        adding or updating attribute and save to JSON file.\n"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            class_name = args[0]
            inst_id = args[1]
            attribute = args[2]
            value = ''
            if args[3].startswith("'"):
                value = args[3].replace("'", "")
            elif args[3].startswith('"'):
                value = args[3].replace('"', "")
            else:
                value = args[3]

            objects = models.storage.all()
            if class_name in classes:
                inst_id = class_name + '.' + inst_id
                if inst_id in objects:
                    setattr(objects[inst_id], attribute, value)
                    models.FileStorage._FileStorage__objects = objects
                    models.storage.save()
                else:
                    print("** no instance found **")

            else:
                print("** class doesn't exist **")

    def do_show(self, line):
        """Prints the string representation of an instance based
        on class name and id.\n"""
        args = line.split()
        if not line:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[0] in classes:
            inst_id = args[0] + "." + args[1]
            objects = models.storage.all()
            if inst_id in objects:
                print('%s' % objects[inst_id])
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)\n"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[0] in classes:
            inst_id = args[0] + '.' + args[1]
            objects = models.storage.all()
            if inst_id in objects:
                del objects[inst_id]
                models.FileStorage._FileStorage__objects = objects
                models.storage.save()
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def emptyline(self):
        """Prevent execution of empty line.\n"""
        pass

    def do_quit(self, line):
        """Quit command to exit the program.\n"""
        return True

    def help_quit(self):
        print('Quit command to exit the program.\n')

    def do_EOF(self, line):
        """Quit command to exit the program.\n"""
        return True

    def help_EOF(self):
        """Handles the ^C command to exit the program.\n"""
        return True

    def default(self, line):
        """Retrieves all instances of a class by class name.\n"""
        args = line.split()
        if len(args) > 0:
            class_cmd = args[0].split('.')
            if len(class_cmd) > 1:
                class_name = class_cmd[0]
                cmd = class_cmd[1]
                if class_name in classes:
                    if cmd == "all()":
                        self.do_all(class_name)
                    elif cmd == "count()":
                        count = 0
                        objects = models.storage.all()
                        for key, value in objects.items():
                            if key.startswith(class_name):
                                count += 1
                        print(count)
                    elif cmd.startswith('show("') and cmd.endswith('")'):
                        instance_id = cmd[6:-2]
                        self.do_show(class_name + ' ' + instance_id)
                    elif cmd.startswith('destroy("') and cmd.endswith('")'):
                        instance_id = cmd[9:-2]
                        self.do_destroy(class_name + ' ' + instance_id)
                    else:
                        print('*** Unknown syntax: %s' % line)
                else:
                    print("*** class doesn't exist ***")
            else:
                print('*** Unknown syntax: %s' % line)
        else:
            print('*** Unknown syntax: %s' % line)

if __name__ == '__main__':
    """Make the program executable except when imported."""
    HBNBCommand().cmdloop()
