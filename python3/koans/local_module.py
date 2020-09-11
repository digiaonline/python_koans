#!/usr/bin/env python

class Duck:
    def __init__(self):
        self._password = 'password' # Genius!

    @property
    def name(self):
        return "Daffy"
