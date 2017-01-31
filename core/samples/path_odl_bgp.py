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

from ydk_.providers import OpenDaylightServiceProvider
from ydk_.path import Repository, CodecService
from ydk_.types import EncodingFormat


def run(codec, provider):
    schema = provider.get_root_schema()
    bgp = schema.create("openconfig-bgp:bgp")
    bgp.create("global/config/as", "65321")

    xml = codec.encode(bgp, EncodingFormat.XML, True)
    create_rpc = schema.rpc("ydk:create")
    create_rpc.input().create("entity", xml)
    create_rpc(provider)


if __name__ == "__main__":
    repo = Repository("/Users/abhirame/Cisco/odl/distribution-karaf-0.5.2-Boron-SR2/cache/schema")
    o = OpenDaylightServiceProvider(repo,'127.0.0.1', 'admin','admin', 8181, EncodingFormat.XML)
    provider = o.get_node_provider('xr')
    codec = CodecService()
    run(codec, provider)

