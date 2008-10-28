"""
freshbooks.py - Python interface to the FreshBooks API (http://developers.freshbooks.com)

Library Maintainer:  Matt Culbreth, mattculbreth@gmail.com, http://mattculbreth.com

#####################################################################

This work is distributed under an MIT License: 
http://www.opensource.org/licenses/mit-license.php

The MIT License

Copyright (c) 2008 Matt Culbreth (http://mattculbreth.com)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

#####################################################################

Hello, this is an open source Python library that serves as an interface to FreshBooks.
"""

import sys
import os
import urllib
import xml.dom.minidom as xml_lib


