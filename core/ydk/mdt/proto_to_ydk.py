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
#
# Convert Telemetry KV data in GPB format to a list of YDK objects
#
import re
import logging
import keyword
import importlib

from google.protobuf.message import Message
from google.protobuf.descriptor import FieldDescriptor

logger = logging.getLogger('mdt.proto_to_ydk')


def bytes_to_string (bytes):
    """
    Convert a byte array into a string aa:bb:cc
    """
    return ":".join(["{:02x}".format(int(ord(c))) for c in bytes])


TF_DECODE_FN_MAP = {
    "bytes_value": lambda b: bytes_to_string(b),
    "string_value": str,
    "bool_value": bool,
    "uint32_value": int,
    "uint64_value": int,
    "sint32_value": int,
    "sint64_value": int,
    "double_value": float,
    "float_value": float,
}


def flexible_attr_name(s, obj):
    """Find the attr in the object that matches when doing a
    case-insensitive match on s. This will break if we happen to have
    an attribute that only differs in case, but that is very
    unlikely. It is likely that using this in a telemetry scenario
    will be slow.

    """
    for item in dir(obj):
        if item.lower() == s.lower():
            return item


def telemetryfield_to_ydk(msg, clazz, level):
    """
    Convert a KV telemetry message to a YDK object graph. The msg is
    a contained GPB 'message TelemetryField'.
    """
    result = clazz()
    logger.debug("{}> Container class {}".format('-'*level,type(result)))
    for field in msg.fields:
        if field.fields and len(field.fields)>0:
            logger.debug("{}> Need to recurse on {}".format('-'*level,field.name))
            # get the nested class
            nested_clazz = None
            try:
                nested_clazz = getattr(clazz, flexible_attr_name(field.name, clazz))
            except:
                logger.debug("{}> failed to get nested class for {}".format('-'*level,field.name))
                return None
            logger.debug("{}> Nested Class {}".format('-'*level,nested_clazz.__name__))
            setattr(
                result,
                convert_camelcase(nested_clazz.__name__),
                telemetryfield_to_ydk(field, nested_clazz, level+1))
        else:
            for f, v in field.ListFields():
                decode_fn = TF_DECODE_FN_MAP.get(f.name)
                if decode_fn:
                    setattr(result, convert_camelcase(field.name), decode_fn(v))
                    logger.debug("{}> Set Scalar {} to {}".format(
                        '-'*level,
                        convert_camelcase(field.name),
                        decode_fn(v)))
                    break
    return result


def convert_camelcase(name):
    """
    Convert a name from camel case to lower case with underscores.
    """
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def get_py_mod_name(name):
    """
    Get the python module name that contains this
    NamedElement.
    """
    t = name.split('_')
    t = [n for n in t if n.lower() not in ['cisco', 'ios', 'xr']]
    if t:
        sub = t[0].lower()
        if keyword.iskeyword(sub) or sub in ('None',):
            sub = '%s_' % sub
        sub = '.%s' % sub
    else:
        sub = ''
    py_mod_name = 'ydk.models%s.%s' % (sub, name)
    logger.debug('Mapped {} to {}'.format(name, py_mod_name))
    return py_mod_name


def get_meta_py_mod_name(name):
    """
    Get the python meta module that contains the meta model
    information about this NamedElement.
    """
    t = name.split('_')
    t = [n for n in t if n.lower() not in ['cisco', 'ios', 'xr']]
    if t:
        sub = t[0].lower()
        if keyword.iskeyword(sub) or sub in ('None',):
            sub = '%s_' % sub
        sub = '.%s' % sub
    else:
        sub = ''
    py_meta_mod_name = 'ydk.models%s._meta' % sub
    logger.debug('Mapped {} to {}'.format(name, py_meta_mod_name))
    return py_meta_mod_name


def pythonize_yang_name(name):
    """
    Convert a name like "interface-name" to "InterfaceName" or
    "interface" to "Interface
    """
    if '-' in name:
        py_name = ''
        sub_components = name.split('-')
        for s in sub_components:
            py_name += s.capitalize()
        return py_name
    else:
        return name.capitalize()

    
def get_ydk_class_from_path(mod, path):
    """
    Create a python class name from a /-separated path.
    """
    path_components = path.split('/')
    clazz = mod
    for c in path_components:
        clazz = getattr(clazz, pythonize_yang_name(c))
    return clazz


def proto_to_ydk(msg):
    """
    Convert a GPB formatted according to telemetry_kv.proto to a list
    of ydk-py objects. Note that this routine currently depends
    strongly on the base_path in the protobuf being 'correct', where
    correct means being specified down to the level of the objects in
    the protobuf messages.
    """
    # Extract the base path
    mod_name, path = msg.base_path.split(':')
    mod_name = mod_name.replace("-", "_")

    # Import the required module
    py_mod = importlib.import_module(get_py_mod_name(mod_name))

    # Create the top-level class from the path. The return will be an
    # array of these objects
    clazz = get_ydk_class_from_path(py_mod, path)

    # iterate over top level Telemetry fields and create an object for
    # each
    results = []
    for field in msg.fields:
        results.append(telemetryfield_to_ydk(field, clazz, 1))
        
    # return the array of YDK objects
    return results
