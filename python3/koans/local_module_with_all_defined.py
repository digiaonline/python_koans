#!/usr/bin/env python

__all__ = (
    'Goat',
    '_Velociraptor'
)

class Goat:
    @property
    def name(self):
        return "George"

class _Velociraptor:
    @property
    def name(self):
        return "Cuddles"

class SecretDuck:
    @property
    def name(self):
        return "None of your business"
