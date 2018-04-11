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

import sys
import json
import pkgutil
import importlib
import logging
import xml.etree.ElementTree as _ET

from ydk.ext.entity_utils import get_entity_from_data_node
from ydk.ext.services import Datastore

from ydk.types import Config, EncodingFormat

from ydk.errors import YModelError, YServiceError

_ENTITY_ERROR_MSG = "No YDK bundle installed for node path '{}'"

def _read_entities(provider, get_config=True, source=Datastore.running):
    session = provider.get_session()
    root_schema = session.get_root_schema()

    if get_config:
        read_rpc = root_schema.create_rpc("ietf-netconf:get-config")
        source_str = "running"
        if source == Datastore.candidate:
            source_str = "candidate"
        elif source == Datastore.startup:
            source_str = "startup"
        elif source != Datastore.running:
            raise YServiceError("Wrong datastore source value '{}'".format(source))
        read_rpc.get_input_node().create_datanode("source/"+source_str);
    else:
        read_rpc = root_schema.create_rpc("ietf-netconf:get")

    data_nodes = read_rpc(session)

    config = Config()
    for node in data_nodes.get_children():
        try:
            config.append(_datanode_to_entity(node))
        except YModelError as err:
            log = logging.getLogger('ydk')
            log.error(err.message)
    return config

def _datanode_to_entity(data_node):
    node_path = data_node.get_path()
    module, container = tuple(node_path[1:].split(':', 1))
    ydk_models = importlib.import_module('ydk.models')
    for (_, name, ispkg) in pkgutil.iter_modules(ydk_models.__path__):
        if ispkg:
            yang_ns = importlib.import_module('ydk.models.{}._yang_ns'.format(name))
            entity_lookup = yang_ns.__dict__['ENTITY_LOOKUP']
            if (module, container) in entity_lookup:
                mod, entity_str = entity_lookup[(module, container)].split('.', 1)
                mod = importlib.import_module('ydk.models.{}.{}'.format(name, mod))
                entity = getattr(mod, entity_str)()
                top_entity = entity.clone_ptr()
                get_entity_from_data_node(data_node, top_entity);
                return top_entity

    raise YModelError(_ENTITY_ERROR_MSG.format(node_path))


def _payload_to_top_entity(payload, encoding):
    """Return top level entity from payload.

    Namespace and entity name are extracted from payload. Then we use this
    tuple of namespace and entity name as a key and search for local
    installed YDK model packages, and return top level entity instance if
    such key matches entry in the `ENTITY_LOOKUP` for local installed YDK
    model packages.

    Args:
        payload (str): Incoming payload.
        encoding (ydk.types.EncodingFormat): Payload encoding format.

    Returns:
        A YDK entity instance (ydk.types.Entity) if the key for namespace
        and top level entity name extracted from payload exists in local
        installed YDK model packages.

    Raises:
        YServiceProviderError if search fails.
    """
    ns_ename = _get_ns_ename(payload, encoding)
    if None in ns_ename:
        raise YModelError("Could not retrieve namespace and container name")
    ydk_models = importlib.import_module('ydk.models')
    for (_, name, ispkg) in pkgutil.iter_modules(ydk_models.__path__):
        if ispkg:
            yang_ns = importlib.import_module('ydk.models.{}._yang_ns'.format(name))
            entity_lookup = yang_ns.__dict__['ENTITY_LOOKUP']
            if ns_ename in entity_lookup:
                entity_mod = entity_lookup[ns_ename]
                mod = '.'.join(entity_mod.split('.')[:-1])
                entity = entity_mod.split('.')[-1]
                mod = importlib.import_module('ydk.models.{}.{}'.format(name, mod))
                entity = getattr(mod, entity)()
                return entity.clone_ptr()

    raise YModelError(_ENTITY_ERROR_MSG.format(ns_ename[0]+':'+ns_ename[1]))


def _get_ns_ename(payload, encoding):
    """Return namespace and entity name from incoming payload.

    Args:
        payload (str): Incoming payload.
        encoding (ydk.types.EncodingFormat): Payload encoding format.

    Returns:
        A tuple of namespace and entity name (tuple(str, str)).
    """
    ns, ename = None, None
    if encoding == EncodingFormat.XML:
        log = logging.getLogger('ydk')
        try:
            payload_root = _ET.fromstring(payload)
            if '{' in payload_root.tag and '}' in payload_root.tag:
                ns, ename = payload_root.tag.rsplit('}')
                ns = ns.strip('{')
            else:
                log.error("Top tag does not have namespace attribute\n{}".format(payload))
        except _ET.ParseError as err:
            log.error("xml.etree.ElementTree.ParseError: {}\n{}".format(err, payload))
    else:
        keys = json.loads(payload).keys()
        # for Python 3
        keys = list(keys)
        ns, ename = keys[0].split(':')
        ns = _to_utf8(ns)
        ename = _to_utf8(ename)

    return (ns, ename)


def _to_utf8(string):
    """Convert unicode to str if running under Python 2 environment."""
    if sys.version_info < (3, 0):
        return string.encode('utf-8')
    return string


def _get_bundle_name(entity):
    """Return bundle name for entity.

    Args:
        entity (ydk.types.Entity): YDK entity instance.

    Returns:
        bundle name.
    """
    m = '.'.join(entity.__module__.rsplit('.')[0:3])
    m = importlib.import_module('.'.join([m, '_yang_ns']))
    return m.__dict__['BUNDLE_NAME']
