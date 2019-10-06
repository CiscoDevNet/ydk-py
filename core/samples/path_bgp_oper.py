#!/usr/bin/env python
#  ----------------------------------------------------------------
# Copyright 2019 Cisco Systems
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

from ydk.path import Codec, Repository, NetconfSession
from ydk.types import EncodingFormat

from session_mgr import init_logging


def execute_path(session):
    codec = Codec()
    schema = session.get_root_schema()
    bgp = schema.create_datanode("Cisco-IOS-XR-ipv4-bgp-oper:bgp")

    xml = codec.encode(bgp, EncodingFormat.XML, True)
    create_rpc = schema.create_rpc("ydk:read")
    create_rpc.get_input_node().create_datanode("filter", xml)
    create_rpc(session)


if __name__ == "__main__":
    init_logging()
    session = NetconfSession('172.29.2.67', 'lab', 'lab', 830)
    execute_path(session)
