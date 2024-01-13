#!/usr/bin/python3
'''Command interpreter'''
import cmd
from models import storage
from models.base_model import BaseModel
import json
import re


class HBNBCommand(cmd.Cmd):
    '''Command interpreter entry point'''

    prompt = '(hbnb) '

    def get_model_classes(self):
        '''Gets all available models in the filestorage'''
        model_classes = []
        for key in storage.classes(self).keys():
            model_classes.append(key)
        return model_classes

    def get_model(self, arg):
        '''Gets model Based on command argument given'''
        model = storage.classes(self).get(arg)
        return model

    def get_model_attrs(self, arg):
        '''Returns the model attributes of model arg'''
        attributes = storage.attributes.get(arg)
        return attributes

    def do_quit(self, line):
        '''Function to handle program exit'''
        return True

    def help_quit(self):
        '''Help for the quit command'''
        print('\n'.join([
            'Exit the console',
            'Usage: quit'
        ]))

    def do_create(self, line):
        """Creates a new model instance.
        """
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            model = storage.classes()[line]()
            model.save()
            print(model.id)

    def help_create(self):
        '''Help for the create command'''
        print('\n'.join([
            'create a model instance',
            'Usage: create BaseModel'
        ]))

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the model class and id
        """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def help_show(self):
        '''Help for the show command'''
        print('\n'.join([
            'Prints representation of an instance',
            'Usage: show BaseModel 1234-1234-1234'
            ]))

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id.
        """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def help_destroy(self):
        '''Help for the destroy command'''
        print('\n'.join([
            'Delete an instance based on the class name',
            'Usage: destroy BaseModel 1234-1234-1234'
        ]))

    def do_all(self, line):
        """Prints all string representation of all instances.
        """
        if line != "":
            scrpts = line.split(' ')
            if scrpts[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                inst = [str(obj) for key, obj in storage.all().items()
                        if type(obj).__name__ == scrpts[0]]
                print(inst)
        else:
            new_list = [str(obj) for key, obj in storage.all().items()]
            print(new_list)

    def help_all(self):
        '''Help for the all command'''
        print('\n'.join([
            'Print all string representation of all instances',
            'Usage: all [BaseModel]'
        ]))

    def do_update(self, line):
        """Updates an instance based on class name and
        id by adding or updating attribute.
        """
        if line == "" or line is None:
            print("** class name missing **")
            return

        regx = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(regx, line)
        classname = match.group(1)
        uid = match.group(2)
        attribute = match.group(3)
        value = match.group(4)
        if not match:
            print("** class name missing **")
        elif classname not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
            elif not attribute:
                print("** attribute name missing **")
            elif not value:
                print("** value missing **")
            else:
                disp = None
                if not re.search('^".*"$', value):
                    if '.' in value:
                        disp = float
                    else:
                        disp = int
                else:
                    value = value.replace('"', '')
                attributes = storage.attributes()[classname]
                if attribute in attributes:
                    value = attributes[attribute](value)
                elif disp:
                    try:
                        value = disp(value)
                    except ValueError:
                        pass
                setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()

    def help_update(self):
        '''Help for the update command'''
        print('\n'.join([
            'update an instance',
            'Usage: update <class name>\
                    <id> <attribute name> <attribute value>'
        ]))

    def do_EOF(self, line):
        '''EOF command, exits the shell'''
        return True

    def help_EOF(self):
        '''help for the EOF command'''
        print('\n'.join([
            'Quit the shell',
        ]))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
