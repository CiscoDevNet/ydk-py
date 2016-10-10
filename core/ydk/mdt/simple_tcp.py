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
# Simple TCP receiver
#
import threading
import socket
import zlib
from .receiver import get_message
from .receiver import TCPMsgType


def tcp_loop (*args):
    """Simple event loop. Wait for TCP messages and pretty-print them.
    """
    (tcp_sock, cb) = args
    while True:
        conn, addr = tcp_sock.accept()
        deco = zlib.decompressobj()
        try:
            while True:
                deco, msg_type, data = get_message(conn, deco)
                if cb:
                    cb(msg_type, data)
                else:
                    print("  Message Type: {}\n  Length: {}".format(
                        TCPMsgType.to_string(msg_type), len(data)))
        except Exception as e:
            print("ERROR: Failed to get TCP message: {}".format(e))

    
def listen(callback=None, ip=None, port=None):
    """Start listening for telemetry using the loop in
    telem_tcp_loop. This is a simple loop that can only accept a
    single connection at a time.
    """
    tcp_sock = socket.socket()
    tcp_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcp_sock.bind((ip, port))
    tcp_sock.listen(1)
    tcp_thread = threading.Thread(target=tcp_loop, args=[tcp_sock, callback])
    tcp_thread.daemon = True
    tcp_thread.start()
