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
#  oc-interfaces.py Sample program illustrating use of generated api
#  ydk.models.openconfig_interfaces.py which inturn is derived from the
#  open-config-interfaces yang module.
#



from __future__ import print_function
from ydk.types import Empty, DELETE, Decimal64
from ydk.services import CRUDService
import logging

from session_mgr import establish_session, init_logging
from ydk.models.openconfig.openconfig_interfaces import Interfaces
from ydk.errors import YError



def print_interface(interface):
    print('*' * 28)
    print('Interface %s'%interface.name)

    if interface.config is not None:
        print ('  config')
        print('     name:-%s'% interface.config.name)
        if interface.config.type is not None:
            print('     type:-%s'%interface.config.type.__class__)
        print('    enabled:-%s'%interface.config.enabled)

    if interface.state is not None:
        print ('  state')
        print('     name:-%s'% interface.state.name)
        if interface.state.type is not None:
            print('     type:-%s'%interface.state.type.__class__)
        print('     enabled:-%s'%interface.state.enabled)
        if interface.state.admin_status is not None:
            enum_str = 'DOWN'
            if interface.state.admin_status == interface.state.AdminStatusEnum.UP:
                enum_str = 'UP'
            print('     admin_status:-%s'%enum_str)
        if interface.state.oper_status is not None:
            oper_status_map = { interface.state.OperStatusEnum.UP : 'UP',
                                interface.state.OperStatusEnum.DOWN : 'DOWN',
                                interface.state.OperStatusEnum.TESTING : 'TESTING',
                                interface.state.OperStatusEnum.UNKNOWN: 'UNKNOWN',
                                interface.state.OperStatusEnum.DORMANT : 'DORMANT',
                                interface.state.OperStatusEnum.NOT_PRESENT : 'NOT_PRESENT',
                                }
            print('     oper_status:-%s'%oper_status_map[interface.state.oper_status])

        if interface.state.mtu is not None:
            print('      mtu:-%s'%interface.state.mtu)
        if interface.state.last_change is not None:
            print('      last_change:-%s'%interface.state.last_change)

        if interface.state.counters is not None:
            print('     counters')
            print('        in_unicast_pkts:-%s'%interface.state.counters.in_unicast_pkts)
            print('        in_octets:-%s'%interface.state.counters.in_octets)
            print('        out_unicast_pkts:-%s'%interface.state.counters.out_unicast_pkts)
            print('        out_octets:-%s'%interface.state.counters.out_octets)
            print('        in_multicast_pkts:-%s'%interface.state.counters.in_multicast_pkts)
            print('        in_broadcast_pkts:-%s'%interface.state.counters.in_broadcast_pkts)
            print('        out_multicast_pkts:-%s'%interface.state.counters.out_multicast_pkts)
            print('        out_broadcast_pkts:-%s'%interface.state.counters.out_broadcast_pkts)
            print('        out_discards:-%s'%interface.state.counters.out_discards)
            print('        in_discards:-%s'%interface.state.counters.in_discards)
            print('        in_unknown_protos:-%s'%interface.state.counters.in_unknown_protos)
            print('        in_errors:-%s'%interface.state.counters.in_errors)
            print('        out_errors:-%s'%interface.state.counters.out_errors)
            print('        last_clear:-%s'%interface.state.counters.last_clear)

        if interface.state.ifindex is not None:
            print('     ifindex:-%s'%interface.state.ifindex)

    print('*' * 28)

def read_interfaces(crud_service, provider):

    interfaces_filter = Interfaces()

    try:
        interfaces = crud_service.read(provider, interfaces_filter)
        for interface in interfaces.interface:
            print_interface(interface)
    except YError:
        print('An error occurred reading interfaces.')


def create_interfaces_config(crud_service, provider):

    interface = Interfaces.Interface()
    interface.config.name = 'LoopbackYDK'
    interface.name = interface.config.name

    try:
        crud_service.create(provider, interface)
    except YError:
        print('An error occurred creating the interface.')



if __name__ == "__main__":
    init_logging()
    provider = establish_session()
    crud_service = CRUDService()
    read_interfaces(crud_service, provider)


    provider.close()
    exit()
