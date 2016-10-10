#!/usr/bin/env python

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
#  bgp_codec.py Sample program illustrating use of codec service for
#  ydk.models.bgp.bgp.py which in turn is derived from the
#  open-config bgp yang module.
#

from __future__ import print_function
from ydk.providers import CodecServiceProvider
from ydk.services import CodecService

from _config_builder import _get_bgp_config, _get_routing_cfg, _get_bgp_routing_multiple_object


def bgp_run(codec_service, provider):
    bgp_cfg = _get_bgp_config()
    bgp_payload = codec_service.encode(provider, bgp_cfg)
    bgp_entity = codec_service.decode(provider, bgp_payload)
    assert bgp_payload == codec_service.encode(provider, bgp_entity)


def run_routing(codec_service, provider):
    routing_policy = _get_routing_cfg()
    routing_payload = codec_service.encode(provider, routing_policy)
    print(routing_payload)
    routing_entity = codec_service.decode(provider, routing_payload)
    assert routing_payload == codec_service.encode(provider, routing_entity)


def run_multiple_routing_bgp(codec_service, provider):
    multi_cfg = _get_bgp_routing_multiple_object()
    multi_payload = codec_service.encode(provider, multi_cfg)
    multi_entity = codec_service.decode(provider, multi_payload)
    assert multi_payload == codec_service.encode(provider, multi_entity)


def init_logging():
    import logging
    logger = logging.getLogger("ydk")
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    formatter = logging.Formatter(("%(asctime)s - %(name)s - "
                                  "%(levelname)s - %(message)s"))
    handler.setFormatter(formatter)
    logger.addHandler(handler)


if __name__ == "__main__":
    init_logging()
    provider = CodecServiceProvider(type='xml')
    codec_service = CodecService()
    bgp_run(codec_service, provider)
    run_routing(codec_service, provider)
    run_multiple_routing_bgp(codec_service, provider)
    exit()
