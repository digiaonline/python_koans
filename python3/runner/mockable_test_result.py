#!/usr/bin/env python

import unittest

# Needed to stop unittest.TestResult itself getting Mocked out of existence,
# which is a problem when testing the helper classes! (It confuses the runner)

class MockableTestResult(unittest.TestResult):
    pass