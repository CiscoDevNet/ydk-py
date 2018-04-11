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

import os
import logging
import importlib

from ydk.entity_utils import get_data_node_from_entity as _get_data_node_from_entity
from ydk.entity_utils import get_entity_from_data_node as _get_entity_from_data_node
from ydk.entity_utils import XmlSubtreeCodec
from ydk.entity_utils import _payload_to_top_entity, _get_bundle_name

from ydk.path import Codec as _Codec
from ydk.errors import YServiceProviderError as _YServiceProviderError
from ydk.errors import YServiceError as _YServiceError
from ydk.errors.error_handler import handle_runtime_error as _handle_error
from ydk.errors.error_handler import check_argument as _check_argument
from ydk.types import EncodingFormat


_TRACE_LEVEL_NUM = 5
_PAYLOAD_ERROR_MSG = "Codec service only supports one entity per payload, please split payload"


class CodecService(object):
    """CodecService wrapper.

    Attributes:
        logger (logging.Logger): CodecService logger.
    """

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    @_check_argument
    def encode(self, provider, entity_holder, pretty=True, subtree=False):
        """Encode entities from entity_holder to string payload(s).

        Args:
            provider: An instance of ydk.provider.CodecServiceProvider class.
            entity_holder: an instance or collection of ydk.types.Entity class instances. 
                           Expected collection types - dict(str, ydk.types.Entity) or list(ydk.types.Entity).
            pretty: Pretty formatting of payload string, default - True.
            subtree: Bool flag, which specifies encode to XML subtree; default= False

        Returns:
            Payload in XML or JSON format based on configuration of Codec Provider.
            The type of return corresponds to the type of the 'entity_holder'.

        Raises:
            Instance of YError, if encoding fails.
        """
        if isinstance(entity_holder, dict):
            payload_map = {}
            for key in entity_holder:
                payload_map[key] = self._encode(provider, entity_holder[key], pretty, subtree)
            return payload_map
        elif isinstance(entity_holder, list):
            payload_list = []
            for entity in entity_holder:
                payload = self.encode(provider, entity, pretty, subtree)
                payload_list.append(payload)
            return payload_list
        else:
            return self._encode(provider, entity_holder, pretty, subtree)

    def _encode(self, provider, entity, pretty, subtree):
        """Encode a YDK entity to string payload.

        Args:
            provider (ydk.providers.CodecServiceProvider): Codec provider.
            entity (ydk.types.Entity) : Encoding target.
            pretty (bool): Pretty formatting if True.
            subtree: (bool) flag, which directs encode to XML subtree; default= False

        Returns:
            Encoded payload if success.

        Raises:
            Instance of YError is encoding fails.
        """
        bundle_name = _get_bundle_name(entity)
        provider.initialize(bundle_name, _get_yang_path(entity))
        root_schema = provider.get_root_schema(bundle_name)

        if subtree:
            if provider.encoding != EncodingFormat.XML:
                raise _YServiceError('Subtree option can only be used with XML encoding')
            xml_codec = XmlSubtreeCodec()
            return xml_codec.encode(entity, root_schema)

        with _handle_error():
            data_node = _get_data_node_from_entity(entity, root_schema)
            codec_service = _Codec()
            result = codec_service.encode(data_node, provider.encoding, pretty)
            self.logger.debug("Performing encode operation, resulting in {}".format(result))
            return result

    @_check_argument
    def decode(self, provider, payload_holder, subtree=False):
        """Decode payload in XML or JSON format to YDK entities.

        Args:
            provider: (ydk.providers.CodecServiceProvider): Codec provider.
            payload_holder: (str or dict(str, str) or list(str)), which represents payload in XML or JSON format.
            subtree: (bool) flag, which directs encode to XML subtree; default - False.

        Returns:
            An instance of ydk.types.Entity class or a dict(str, Entity) or list(Entity).

        Raises:
            YServiceProviderError, see documentation for `_decode`.
        """
        if isinstance(payload_holder, dict):
            entities = {}
            for key in payload_holder:
                entity = self.decode(provider, payload_holder[key], subtree)
                entities[key] = entity
            return entities
        elif isinstance(payload_holder, list):
            entities = []
            for payload in payload_holder:
                entity = self.decode(provider, payload, subtree)
                entities.append(entity)
            return entities
        else:
            return self._decode(provider, payload_holder, subtree)

    def _decode(self, provider, payload, subtree):
        """Decode payload to a YDK entity instance.

        Args:
            provider (ydk.providers.CodecServiceProvider): Codec provider.
            payload (str): Incoming payload, formatted in XML or JSON.

        Returns:
            A YDK entity (ydk.types.Entity) instance with children populated.

        Raises:
            - YServiceProviderError with _PAYLOAD_ERROR_MSG if payload
              contains more than one top level containers.
            - YServiceProviderError with _ENTITY_ERROR_MSG if no such entity
              could be found in locally installed YDK model packages.
        """
        entity = _payload_to_top_entity(payload, provider.encoding)

        if subtree:
            if provider.encoding != EncodingFormat.XML:
                raise _YServiceError('Subtree option can only be used with XML encoding')
            xml_codec = XmlSubtreeCodec()
            return xml_codec.decode(payload, entity)

        bundle_name = _get_bundle_name(entity)
        provider.initialize(bundle_name, _get_yang_path(entity))

        root_schema = provider.get_root_schema(bundle_name)

        self.logger.debug("Performing decode operation on payload:\n{}".format(payload))

        codec_service = _Codec()
        root_data_node = codec_service.decode(root_schema, payload, provider.encoding)
        data_nodes = root_data_node.get_children();
        if data_nodes is None or len(data_nodes) == 0:
            self.logger.debug(_PAYLOAD_ERROR_MSG)
            raise _YServiceProviderError(_PAYLOAD_ERROR_MSG)
        else:
            data_node = data_nodes[0]
            _get_entity_from_data_node(data_node, entity)
            return entity

    def _log_error_and_raise_exception(self, msg, exception_class):
        self.logger.error(msg)
        raise exception_class(msg)

def _get_yang_path(entity):
    """Return YANG models install location for entity.

    Args:
        entity (ydk.types.Entity): YDK entity instance.

    Returns:
        Path for installed YANG models location (str).
    """
    m = '.'.join(entity.__module__.rsplit('.')[0:3])
    m = importlib.import_module(m)
    return os.path.join(m.__path__[0], '_yang')
