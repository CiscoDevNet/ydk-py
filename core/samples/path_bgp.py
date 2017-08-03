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

from ydk.providers import RestconfServiceProvider
from ydk.path import Codec, Repository
from ydk.types import EncodingFormat


def execute_path(provider, codec):
    schema = provider.get_root_schema()
    bgp = schema.create_datanode("openconfig-bgp:bgp")
    bgp.create_datanode("global/config/as", "65321")

    runner = schema.create_datanode('ydktest-sanity:runner')
    runner.create_datanode('ytypes/built-in-t/number8', '12')
    xml = codec.encode(runner, EncodingFormat.JSON, True)
    print(xml)
    create_rpc = schema.create_rpc("ydk:create")
    create_rpc.get_input_node().create_datanode("entity", xml)
    create_rpc(provider)


if __name__ == "__main__":
    repo = Repository("/usr/local/share/ydktest@0.1.0")
    provider = RestconfServiceProvider(repo, '127.0.0.1', 'admin', 'admin', 12306, EncodingFormat.JSON)
    codec = Codec()
    execute_path(provider, codec)
