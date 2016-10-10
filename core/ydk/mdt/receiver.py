from __future__ import print_function
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
#
# Sample telemetry receiver
#
import time
import struct
import zlib
from enum import Enum


class TCPMsgType(Enum):
    RESET_COMPRESSOR = 1
    JSON = 2
    GPB_COMPACT = 3
    GPB_KEY_VALUE = 4

    @classmethod
    def to_string (self, value):
        if value == 1:
            return "RESET_COMPRESSOR (1)"
        elif value == 2:
            return "JSON (2)"
        elif value == 3:
            return "GPB_COMPACT (3)"
        elif value == 4:
            return "GPB_KEY_VALUE (4)"
        else:
            raise ValueError("{} is not a valid TCP message type".format(value))


TCP_FLAG_ZLIB_COMPRESSION = 0x1


def tcp_flags_to_string (flags):
    strings = []
    if flags & TCP_FLAG_ZLIB_COMPRESSION != 0:
        strings.append("ZLIB compression")
    if len(strings) == 0:
        return "None"
    else:
        return "|".join(strings)


def unpack_int(raw_data):
    return struct.unpack_from(">I", raw_data, 0)[0]


def flush(length, conn):
    """Flush data of a specific length fron the socket. Used to flush out
    unsupported message types.
    """
    data = b""
    while len(data) < length:
        data += c.recv(length - len(data))
    return data


def get_message(conn, deco):
    """
    Handle a received TCP message, synchronously reading it to completion.
    Argument: conn
      TCP connection
    Argument: deco
      ZLIB decompression object
    Return: updated decompression object in the case where compression was
            reset
    """
    # v1 message header (from XR6.0) consists of just a 4-byte length
    # v2 message header (from XR6.1 onwards) consists of 3 4-byte fields:
    #     Type,Flags,Length
    # If the first 4 bytes read is <=4 then it is too small to be a 
    # valid length. Assume it is v2 instead
    # 
    t = conn.recv(4)
    msg_type = unpack_int(t)
    if msg_type > 4:
        # V1 message - compressed JSON
        flags = TCP_FLAG_ZLIB_COMPRESSION
        msg_type_str = "JSONv1 (COMPRESSED)"
        length = msg_type
        msg_type = TCPMsgType.JSON
        data = flush(length, conn)
        return (deco, msg_type, data)
    else:
        # V2 message
        t = conn.recv(4)
        flags = unpack_int(t)
        t = conn.recv(4)
        length = unpack_int(t)
   
    # Read all the bytes of the message according to the length in the header 
    data = b""
    while len(data) < length:
        data += conn.recv(length - len(data))

    # Decompress the message if necessary. Otherwise use as-is
    if flags & TCP_FLAG_ZLIB_COMPRESSION != 0:
        try:
            # print("Decompressing message")
            msg = deco.decompress(data)
        except Exception as e:
            print("ERROR: failed to decompress message: {}".format(e))
            msg = None
    else:
        msg = data

    if msg_type == TCPMsgType.RESET_COMPRESSOR:
        deco = zlib.decompressobj()

    return (deco, msg_type, msg)
