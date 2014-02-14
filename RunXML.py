#!/usr/bin/env python3

"""
To run the program
    % python RunXML.py < RunXML.in > RunXML.out
    % chmod ugo+x RunXML.py
    % RunXML.py < RunXML.in > RunXML.out
"""

#----------
# imports
#----------

from XML import xml_solve
from xml.etree.ElementTree import Element, fromstring
import sys

#----------
# Main Run
#----------

xml_solve(sys.stdin)
