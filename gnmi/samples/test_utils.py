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

"""test_utils.py

Utility function for test cases.
"""
import sys
import re
import logging

from ydk.entity_utils import get_data_node_from_entity
from ydk.errors       import YCoreError

def assert_with_error(pattern, ErrorClass):
    def assert_with_pattern(func):
        def helper(self, *args, **kwargs):
            try:
                func(self)
            except ErrorClass as error:
                res = re.match(pattern, error.message.strip())
                self.assertEqual(res is not None, True)
        return helper
    return assert_with_pattern


def datanode_to_str(dn, indent = ''):
    try:
        s = dn.get_schema_node().get_statement()
        if s.keyword == "leaf" or s.keyword == "leaf-list" or s.keyword == "anyxml":
            out = indent + "<" + s.arg + ">" + dn.get_value() + "</" + s.arg + ">\n"
        else:
            out = indent + "<" + s.arg + ">\n"
            child_indent = indent + "  "
            for child in dn.get_children():
                out += datanode_to_str(child, child_indent)
            out += indent + "</" + s.arg + ">\n"
        return out
    except YCoreError as ex:
        print(ex.message)

def print_data_node(dn):
    try:
        print("\n=====>  Printing DataNode: '{}'".format(dn.get_path()))
        print(datanode_to_str(dn))
    except YPYCoreError as ex:
        print(ex.message)

def print_entity(entity, root_schema):
    dn = get_data_node_from_entity( entity, root_schema);
    print_data_node(dn)

def enable_logging(level):
    log = logging.getLogger('ydk')
    log.setLevel(level)
    handler = logging.StreamHandler()
    formatter = logging.Formatter(("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
    handler.setFormatter(formatter)
    log.addHandler(handler)

