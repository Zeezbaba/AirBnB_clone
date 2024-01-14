#!/usr/bin/python3
'''test cases for the console'''
from unittest import main
from unittest import TestCase
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestHelpCommand(TestCase):
    def test_help_quit(self):
        string = "Exit the console\nUsage: quit"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(string, output.getvalue().strip())

    def test_help_all(self):
        string = ("Print all string representation of all instances\n"
                  "Usage: all [BaseModel]")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help all"))
            self.assertEqual(string, output.getvalue().strip())

    def test_help_update(self):
        string = ("update an instance\nUsage: update "
                  "<class name><id> <attribute name> <attribute value>")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help update"))
            self.assertEqual(string, output.getvalue().strip())

    def test_help_show(self):
        string = ("Prints representation of an instance\n"
                  "Usage: show BaseModel 1234-1234-1234")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help show"))
            self.assertEqual(string, output.getvalue().strip())

    def test_help_destroy(self):
        string = ("Delete an instance based on the class name\n"
                  "Usage: destroy BaseModel 1234-1234-1234")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help destroy"))
            self.assertEqual(string, output.getvalue().strip())

    def test_help_create(self):
        string = "create a model instance\nUsage: create BaseModel"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertEqual(string, output.getvalue().strip())

    def test_help_EOF(self):
        string = "Quit the shell"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(string, output.getvalue().strip())


class TestPrompt(TestCase):
    def test_prompt(self):
        self.assertEqual("(hbnb) ", HBNBCommand().prompt)


class TestCreateCommand(TestCase):
    def test_class_name_missing(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual("** class name missing **",
                             output.getvalue().strip())

    def test_class_name_does_not_exist(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create MyModel"))
            self.assertEqual("** class doesn't exist **",
                             output.getvalue().strip())

    def test_model_created(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertLess(0, len(output.getvalue().strip()))


class TestEmptyLine(TestCase):
    def test_eof(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())


class TestShow(TestCase):
    def test_class_name_missing(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show"))
            self.assertEqual("** class name missing **",
                             output.getvalue().strip())

    def test_class_name_does_not_exist(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show MyModel"))
            self.assertEqual("** class doesn't exist **",
                             output.getvalue().strip())

    def test_id_missing(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel"))
            self.assertEqual("** instance id missing **",
                             output.getvalue().strip())

    def test_class_model_instance_does_not_exist(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel 123123"))
            self.assertEqual("** no instance found **",
                             output.getvalue().strip())

    def test_model_instance_exists(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel <uuid>"))
            self.assertLess(0, len(output.getvalue().strip()))


class TestDestroy(TestCase):
    def test_class_name_missing(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy"))
            self.assertEqual("** class name missing **",
                             output.getvalue().strip())

    def test_class_name_does_not_exist(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy MyModel"))
            self.assertEqual("** class doesn't exist **",
                             output.getvalue().strip())

    def test_id_missing(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel"))
            self.assertEqual("** instance id missing **",
                             output.getvalue().strip())

    def test_class_model_instance_does_not_exist(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel 123123"))
            self.assertEqual("** no instance found **",
                             output.getvalue().strip())

    def test_model_instance_exists(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel <uuid>"))
            self.assertLess(0, len(output.getvalue().strip()))


class TestAll(TestCase):
    def test_all_no_args(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all"))
            self.assertLess(0, len(output.getvalue().strip()))

    def test_class_name_does_not_exist(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all MyModel"))
            self.assertEqual("** class doesn't exist **",
                             output.getvalue().strip())

    def test_model_exists(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all BaseModel <uuid>"))
            self.assertLess(0, len(output.getvalue().strip()))


class TestUpdate(TestCase):
    def test_class_name_missing(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update"))
            self.assertEqual("** class name missing **",
                             output.getvalue().strip())

    def test_class_name_does_not_exist(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update MyModel"))
            self.assertEqual("** class doesn't exist **",
                             output.getvalue().strip())

    def test_id_missing(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update BaseModel"))
            self.assertEqual("** instance id missing **",
                             output.getvalue().strip())

    def test_class_model_instance_does_not_exist(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update BaseModel 123123"))
            self.assertEqual("** no instance found **",
                             output.getvalue().strip())


if __name__ == "__main__":
    main()
