#!/usr/bin/env python3
"""
A module that contains the entry point of the command interpreter.
"""

import cmd
import models
BaseModel = models.base_model.BaseModel


class HBNBCommand(cmd.Cmd):
    """ Defines the command hooks. """

    prompt = '(hbnb) '

    def do_all(self, line):
        """Prints all string representation of all instances
        based or not on the class name.\n"""
        arguments = line.split()
        if len(arguments) == 0:
            objects = models.storage.all()
            object_array = []
            if not len(objects) == 0:
                for key, value in objects.items():
                    instance = '%s' % value
                    object_array.append(instance)
                print(object_array)
            else:
                pass
        elif arguments[0] == 'BaseModel':
            objects = models.storage.all()
            class_name = arguments[0]
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
        """Creates an instance of BaseModel and save to JSON file.\n"""
        arguments = line.split()
        if len(arguments) > 0:
            class_name = arguments[0]
        else:
            class_name = line

        if not class_name:
            print("** class name missing **")
        elif class_name == "BaseModel":
            instance = BaseModel()
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
            if class_name == 'BaseModel':
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
        on call name and id\n"""
        arguments = line.split()
        if not line:
            print("** class name missing **")
        elif len(arguments) == 1:
            print("** instance id missing **")
        elif arguments[0] == "BaseModel":
            inst_id = arguments[0] + "." + arguments[1]
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
        elif args[0] == 'BaseModel':
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
        """Prevent execution of empty line\n"""
        pass

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def help_quit(self):
        print('Quit command to exit the program\n')

    def do_EOF(self, line):
        """Quit command to exit the program\n"""
        return True

    def help_EOF(self):
        print('Quit command to exit the program\n')


if __name__ == '__main__':
    """Make the program executable except when imported."""
    HBNBCommand().cmdloop()
