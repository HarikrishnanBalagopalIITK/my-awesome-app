#!/usr/bin/env python


from utils import greeting


def main():
    """main is the entry point of the app"""
    name = input("What is your name?\n")
    print(greeting(name))


main()
