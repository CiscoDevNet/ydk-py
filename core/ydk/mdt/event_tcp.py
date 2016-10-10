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
# Simple event driven protocol using Twisted
#
import zlib
from enum import Enum
from .receiver import TCPMsgType
from twisted.internet import protocol
import struct
import logging

logger = logging.getLogger('mdt.event_tcp')


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


class MDTState(Enum):
    START = 0
    TYPE_RECVD_V1 = 1
    TYPE_RECVD_V2 = 2
    FLAGS_RECVD_V2 = 3
    DATA_RECVD_V1 = 4
    DATA_RECVD_V2 = 5

    
class MDTReceiver(protocol.Protocol):
    """
    Receive GPB self-describing telemetry.
    """
    
    def connectionMade(self):
        """
        Initialize the decompression object we may need.
        """
        self.fn_vec = [
            self.handle_START,
            self.handle_TYPE_RECVD_V1,
            self.handle_TYPE_RECVD_V2,
            self.handle_FLAGS_RECVD_V2,
            self.handle_DATA_RECVD_V1,
            self.handle_DATA_RECVD_V2,
            ]
        self.deco = zlib.decompressobj()
        self.state = MDTState.START
        self.data = b""

    def connectionLost(self, reason):
        pass

    def dataReceived(self, data):
        """
        Decode and display some stats.
        """
        self.data += data
        logger.debug("data received {}/total {}".format(len(data), len(self.data)))
        self.fn_vec[self.state]()

    def handle_START(self):
        logger.debug("handle_START")
        if len(self.data) >= 4:
            self.msg_type = unpack_int(self.data)
            self.data = self.data[4:]
            if self.msg_type > 4:
                self.length = self.msg_type
                self.msg_type = TCPMsgType.JSON
                self.flags = TCP_FLAG_ZLIB_COMPRESSION
                self.handle_TYPE_RECVD_V1()
            else:
                self.handle_TYPE_RECVD_V2()

    def handle_TYPE_RECVD_V1(self):
        """
        Handle messages of type V1, which is just flushing them as we don't
        handle them.
        """
        logger.debug("handle_TYPE_RECVD_V1")
        self.state = MDTState.TYPE_RECVD_V1
        if len(self.data) >= self.length:
            self.data = self.data[self.length:]
            self.state = MDTState.START

    def handle_TYPE_RECVD_V2(self):
        """
        Handle messages of type V2. Mostly just the self-describing GPB.
        """
        logger.debug("handle_TYPE_RECVD_V2")
        self.state = MDTState.TYPE_RECVD_V2
        if len(self.data) >= 4:
            self.flags = unpack_int(self.data)
            self.data = self.data[4:]
            self.handle_FLAGS_RECVD_V2()

    def handle_FLAGS_RECVD_V2(self):
        logger.debug("handle_FLAGS_RECVD_V2")
        self.state = MDTState.FLAGS_RECVD_V2
        if len(self.data) >= 4:
            self.length = unpack_int(self.data)
            self.data = self.data[4:]
            self.handle_DATA_RECVD_V2()

    def handle_DATA_RECVD_V1(self):
        """
        This is just a skipper for now.
        """
        logger.debug("handle_DATA_RECVD_V1")
        if len(self.data) >= self.length:
            self.data = self.data[self.length:]
            self.handle_COMPLETE_V1()
    
    def handle_DATA_RECVD_V2(self):
        logger.debug("handle_DATA_RECVD_V2")
        self.state = MDTState.DATA_RECVD_V2
        if len(self.data) >= self.length:
            self.handle_COMPLETE_V2()

    def handle_COMPLETE_V1(self):
        logger.debug("handle_COMPLETE_V1")
        self.state = MDTState.START
        if len(self.data) > 0:
            self.handle_START()

    def handle_COMPLETE_V2(self):
        logger.debug("handle_COMPLETE_V2, data length = {}/{}".format(self.length, len(self.data)))
        if (self.flags & TCP_FLAG_ZLIB_COMPRESSION) != 0:
            try:
                msg = self.deco.decompress(self.data[:self.length])
            except Exception as e:
                print("ERROR: failed to decompress message: {}".format(e))
                msg = None
        else:
            msg = self.data[:self.length]
            
        # reset the state machine
        self.state = MDTState.START

        # reset the decompressor
        if self.msg_type == TCPMsgType.RESET_COMPRESSOR:
            self.deco = zlib.decompressobj()
            
        # call the final message processing
        self.process_v2(msg)

        # and finally restart the state machine
        self.data = self.data[self.length:]
        if len(self.data) > 0:
            self.handle_START()

    def process_v2(self, msg):
        pass
        
