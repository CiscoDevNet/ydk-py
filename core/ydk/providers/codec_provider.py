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

""" providers.py

   Service Providers module. Current implementation supports the NetconfServiceProvider which
   uses ncclient (a Netconf client library) to provide CRUD services.

"""
from ydk.errors import YPYServiceProviderError
from .provider import ServiceProvider
from ._encoder import XmlEncoder
from ._decoder import XmlDecoder

import logging


class CodecServiceProvider(ServiceProvider):
    """ Codec ServiceProvider to encode to and decode from desired payload format

        Initialization parameters of CodecServiceProvider

        kwargs:
            - type : desired type of codec (xml, json etc)
    """

    def __init__(self, **kwargs):
        if(len(kwargs) == 0):
            raise YPYServiceProviderError(error_msg='Codec type is required')

        codec_type = ''
        for key, val in kwargs.items():
            if key == 'type':
                codec_type = val

        if codec_type == 'xml':
            self.encoder = XmlEncoder()
            self.decoder = XmlDecoder()
        else:
            raise YPYServiceProviderError(error_msg='Codec type "{0}" not yet supported'.format(codec_type))
        self.logger = logging.getLogger(__name__)

    def _encode(self, entity):
        """ Encodes the entity into the desired encoding format """
        payload = self.encoder.encode(entity)
        self.logger.info('Result of encoding: \n{0}'.format(payload))
        return payload

    def _decode(self, payload):
        """ Decodes the payload from the desired decoding format """
        self.logger.info('Decoding payload: {0}'.format(payload))
        entity = self.decoder.decode(payload)
        self.logger.info('Result of decoding: {0}'.format(entity))
        return entity

