#!/usr/bin/env python


def greeting(name):
    """greeting returns a nice message"""
    return f"Hello {name}!"


def main():
    """main is the entry point of the app"""
    name = input("What is your name?\n")
    print(greeting(name))


main()
