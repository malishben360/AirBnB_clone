#!/usr/bin/env python3
"""
A module that contains the entry point of the command interpreter.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """ Defines the command hooks. """

    prompt = '(hbnb) '

    def emptyline(self):
        """Prevent execution of empty line"""
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
