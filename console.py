#!/usr/bin/python3
'''Command interpreter'''
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


# #TODO: print string representations of output instead of dict repr
class HBNBCommand(cmd.Cmd):
    '''Command interpreter entry point'''
    prompt = '(hbnb) '

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
        '''Creates a new BaseModel instance'''
        args = line.split()
        if len(args) < 1:
            print('** class name missing **')
        elif args[0] != 'BaseModel':
            print('** class doesn\'t exist **')
        else:
            model = BaseModel()
            model.save()

    def help_create(self):
        '''Help for the create command'''
        print('\n'.join([
            'create a model instance',
            'Usage: create BaseModel'
        ]))

    def do_show(self, line):
        '''Prints the string representation of an instance
          based on class name and id'''
        args = line.split()
        if len(args) < 1:
            print('** class name missing **')
        elif args[0] != 'BaseModel':
            print('** class doesn\'t exist **')
        elif len(args) < 2:
            print('** instance id missing **')
        else:
            key = args[0]+'.'+args[1]
            model = FileStorage.all(self).get(key)
            if model is None:
                print('** no instance found **')
                return
            print(model)

    def help_show(self):
        '''Help for the show command'''
        print('\n'.join([
            'Prints representation of an instance',
            'Usage: show BaseModel 1234-1234-1234'
            ]))

    def do_destroy(self, line):
        '''Deletes an instance based on the class name id'''
        args = line.split()
        if len(args) < 1:
            print('** class name missing **')
            return
        elif args[0] != 'BaseModel':
            print('** class doesn\'t exist **')
        elif len(args) < 2:
            print('** instance id missing **')
        else:
            key = args[0]+'.'+args[1]
            models = FileStorage.all(self)
            model = models.get(key)
            if model is None:
                print('** no instance found **')
                return
            del models[key]
            FileStorage.save(self)

    def help_destroy(self):
        '''Help for the destroy command'''
        print('\n'.join([
            'Delete an instance based on the class name',
            'Usage: destroy BaseModel 1234-1234-1234'
        ]))

    def do_all(self, line):
        '''prints all string representation of all instances
          based based/not on the class name'''
        args = line.split()
        if len(args) == 1:
            if args[0] != 'BaseModel':
                print('** class doesn\'t exist **')
            else:
                # #TODO: get models based on provided args[0]
                # print the models to STDOUT
                print('Some specific model')
        else:
            models = FileStorage.all(self)
            print(models)

    def help_all(self):
        '''Help for the all command'''
        print('\n'.join([
            'Print all string representation of all instances',
            'Usage: all [BaseModel]'
        ]))

    def do_update(self, line):
        '''updates all instances based in the calss name
          and id by adding or updating attributes'''
        args = line.split()
        # #TODO: update this to update model instances

    def help_update(self):
        '''Help for the update command'''
        print('\n'.join([
            'update an instance',
            'Usage: update BaseModel 1234-1234-1234'
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
