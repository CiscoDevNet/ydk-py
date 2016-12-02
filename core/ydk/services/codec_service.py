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
""" codec_service.py

   The Encoder/Decoder Service class.

"""
from __future__ import absolute_import
from .service import Service
from .meta_service import MetaService
import logging

from ydk.errors import YPYServiceError


class CodecService(Service):
    """Codec Service to encode and decode
    XML, JSON and other protocol payloads """
    def __init__(self):
        self.service_logger = logging.getLogger(__name__)

    def encode(self, encoder, entity):
        if None in (encoder, entity):
            msg = "'encoder' and 'entity' cannot be None"
            raise YPYServiceError(error_msg=msg)
        self.service_logger.info('Encoding operation initiated')
        payload = self.operate_on_object_or_dictionary(entity, CodecService._encode_entity, [encoder])
        self.service_logger.info('Encoding operation completed')
        return payload

    def decode(self, decoder, payload):
        if None in (decoder, payload):
            msg = "'decoder' and 'payload' cannot be None"
            raise YPYServiceError(error_msg=msg)
        self.service_logger.info('Decoding operation initiated')
        entity = self.operate_on_object_or_dictionary(payload, CodecService._decode_payload, [decoder])
        self.service_logger.info('Decoding operation completed')
        return entity

    @staticmethod
    def _decode_payload(payload, decoder):
        entity = decoder._decode(payload)
        return entity

    @staticmethod
    def _encode_entity(entity, encoder):
        MetaService.normalize_meta([], entity)
        payload = encoder._encode(entity)
        return payload
