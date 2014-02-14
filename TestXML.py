#!/usr/bin/env python3

#----------
# imports
#----------

import io
import unittest
from XML import xml_read, xml_findPattern, StoreGlob1, StoreGlob2

#----------
# xml_test
#----------

class TestXML(unittest.TestCase) :
    #-------------
    #
    #-------------
    def test1_read(self):
       # r = io.stringIO"<xml></xml>")
        xml_read()

    def test2_read(self):
        r = xml_read()

    def test3_read(self):
        r = xml_read()

    def test1_findPattern(self):
        xmltree = xml_read(ElementTree.xml)
        globals1 = StoreGlob1(xmltree)
        xml_findPattern(globals1,xmltree[-1])
        p = xml_findPattern()

    def test2_findPattern(self):
        p = xml_findPattern()

    def test3_findPattern(self):
        p = xml_findPattern()

    def test1_traverse(self):
        # r =

    def test2_traverse(self):
        # r =

    def test3_traverse(self):
        # r =

    def test1_print(self):
        # r =

    def test2_print(self):
        # r =

    def test3_print(self):
        # r =

    def test1_solve(self):
        # r =

    def test2_solve(self):
        # r =

    def test3_solve(self):
        # r =
