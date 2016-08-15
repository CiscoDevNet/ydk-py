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
""" _importer.py

    Merge _yang_ns for subpackage to a single _yang_ns at runtime.
"""
import importlib
import pkgutil
from ydk import models


class YangNs(object):
    def __init__(self, d):
        self.__dict__ = d

_yang_ns_dict = {}
exempt_keys = set(['__builtins__', '__doc__', '__file__',
                   '__name__', '__package__'])

try:
    _yang_ns = importlib.import_module('ydk.models._yang_ns')
except ImportError:
    for (importer, name, ispkg) in pkgutil.iter_modules(models.__path__):
        if ispkg:
            try:
                mod_yang_ns = importlib.import_module('ydk.models.%s._yang_ns' % name)
            except ImportError:
                continue
            keys = set(mod_yang_ns.__dict__) - exempt_keys
            for key in keys:
                if key not in _yang_ns_dict:
                    _yang_ns_dict[key] = mod_yang_ns.__dict__[key]
                else:
                    if isinstance(_yang_ns_dict[key], dict):
                        _yang_ns_dict[key].update(mod_yang_ns.__dict__[key])
                    else:
                        # shadow old value
                        _yang_ns_dict[key] = mod_yang_ns.__dict__[key]

    _yang_ns = YangNs(_yang_ns_dict)
