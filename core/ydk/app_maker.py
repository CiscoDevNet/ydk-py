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
""" ydk_app_maker.py

   YDK app maker

"""
import logging
from ydk.providers._encoder import XmlEncoder
from ydk.providers._decoder import XmlDecoder
from ydk.services.meta_service import MetaService
from ydk.errors import YPYServiceProviderError


class YdkAppMaker(object):
    def __init__(self, **kwargs):
        if(len(kwargs) == 0):
            raise YPYServiceProviderError('Codec type is required')

        codec_type = ''
        for key, val in kwargs.items():
            if key == 'type':
                codec_type = val

        if codec_type != 'xml':
            raise YPYServiceProviderError('Codec type "{0}" not yet supported'.format(codec_type))

        self.logger = logging.getLogger(__name__)

    def payload2python(self, payload):
        self.logger.debug('Converting payload to python app: {}'.format(payload))
        decoder = XmlDecoder()
        decoded_entity = decoder.decode(payload)
        MetaService.normalize_meta([], decoded_entity)
        encoder = XmlEncoder()
        xml = encoder.encode(decoded_entity)
        self.logger.debug('Resulting python app: {}'.format(encoder.app))
        return encoder.app
