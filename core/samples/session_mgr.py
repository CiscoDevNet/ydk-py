from __future__ import print_function
#  ----------------------------------------------------------------
# Copyright 2016 Cisco Systems
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ------------------------------------------------------------------


#  ----------------------------------------------------------------
# Utility functions to create and return a Session

from optparse import OptionParser, IndentedHelpFormatter
from ydk.providers import NetconfServiceProvider
import logging

class HelpFormatterWithLineBreaks(IndentedHelpFormatter):
    def format_description(self, description):
        result = ""
        if description is not None:
            description_paragraphs = description.split("\n")
            for paragraph in description_paragraphs:
                result += self._format_text(paragraph) + "\n"
            return result

def init_logging():
    """ Initialize the logging infra and add a handler """
    logger = logging.getLogger('ydk')
    logger.setLevel(logging.DEBUG)
    # create file handler
    fh = logging.FileHandler('bgp.log')
    fh.setLevel(logging.DEBUG)
    # create a console logger too
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    # add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)

def establish_session():

    usage = """%prog [-h | --help] [options] """

    parser = OptionParser(usage, formatter=HelpFormatterWithLineBreaks())
    parser.add_option("-v", "--version", dest="version",
                      help="force NETCONF version 1.0 or 1.1")
    parser.add_option("-u", "--user", dest="username", default="admin")
    parser.add_option("-p", "--password", dest="password", default="admin",
                      help="password")
    parser.add_option("--proto", dest="proto", default="ssh",
                      help="Which transport protocol to use, one of ssh or tcp")
    parser.add_option("--host", dest="host", default="localhost",
                      help="NETCONF agent hostname")
    parser.add_option("--port", dest="port", default=830, type="int",
                      help="NETCONF agent SSH port")


    (o, args) = parser.parse_args()

    print('Establishing connection with device %s:%d using %s :'%(o.host, o.port, o.proto))

    ne = NetconfServiceProvider(address=o.host,
                                port=o.port,
                                username = o.username,
                                password = o.password,
                                protocol = o.proto)

    print('connection established...')
    return ne