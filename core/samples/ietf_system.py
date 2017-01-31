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
from __future__ import print_function
from ydk.providers import NetconfServiceProvider
from ydk.services import CRUDService


def _get_obj_system():
    from ydk.models.ietf import ietf_system

    obj_system=ietf_system.System()
    obj_system.contact = 'support@example.com'
    obj_system.hostname = '1.2.3.4'

    obj_clock = ietf_system.System.Clock()
    obj_clock.timezone_name = 'Argentina'
    obj_system.clock = obj_clock

    obj_ntp = ietf_system.System.Ntp()

    obj_server = ietf_system.System.Ntp.Server()
    obj_server.name = 'xyz'

    obj_udp = ietf_system.System.Ntp.Server.Udp()
    obj_udp.address = '1.2.3.4'
    obj_udp.port = 22
    obj_server.udp = obj_udp
    obj_server.association_type = ietf_system.System.Ntp.Server.AssociationTypeEnum.peer
    obj_ntp.server.append(obj_server)
    obj_system.ntp = obj_ntp

    obj_dns_resolver = ietf_system.System.DnsResolver()
    obj_dns_resolver.search.append('abc.com')
    obj_dns_resolver.search.append('fff.com')

    obj_server = ietf_system.System.DnsResolver.Server()
    obj_server.name = 'abc'

    obj_udp_and_tcp = ietf_system.System.DnsResolver.Server.UdpAndTcp()
    obj_udp_and_tcp.address = '1.2.3.4'
    obj_udp_and_tcp.port = 830
    obj_server.udp_and_tcp = obj_udp_and_tcp
    obj_dns_resolver.server.append(obj_server)
    obj_system.dns_resolver = obj_dns_resolver

    obj_authentication = ietf_system.System.Authentication()

    obj_user = ietf_system.System.Authentication.User()
    obj_user.name = 'guest'
    obj_user.password = 'guest'
    obj_authentication.user.append(obj_user)

    obj_user = ietf_system.System.Authentication.User()
    obj_user.name = 'admin'
    obj_user.password = 'admin'
    obj_authentication.user.append(obj_user)
    obj_system.authentication = obj_authentication

    return obj_system


def _get_decoded_entity():
    from ydk.providers import CodecServiceProvider
    from ydk.services import CodecService

    payload = '''
    <system xmlns="urn:ietf:params:xml:ns:yang:ietf-system">
        <contact>support@example.com</contact>
        <hostname>1.2.3.4</hostname>
        <clock>
          <timezone-name>Argentina</timezone-name>
        </clock>
        <ntp>
          <server>
            <name>xyz</name>
            <udp>
              <address>1.2.3.4</address>
              <port>22</port>
            </udp>
            <association-type>peer</association-type>
          </server>
        </ntp>
        <dns-resolver>
          <search>abc.com</search>
          <search>fff.com</search>
          <server>
            <name>abc</name>
            <udp-and-tcp>
              <address>1.2.3.4</address>
              <port>830</port>
            </udp-and-tcp>
          </server>
        </dns-resolver>
        <authentication>
          <user>
            <name>guest</name>
            <password>guest</password>
          </user>
          <user>
            <name>admin</name>
            <password>admin</password>
          </user>
        </authentication>
      </system>
    '''
    codec = CodecService()
    provider = CodecServiceProvider(type='xml')
    return codec.decode(provider, payload)


def _init_logging():
    import logging
    log = logging.getLogger('ydk')
    log.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    log.addHandler(ch)


def ietf_run(crud_service, provider):
    print('==============\nCRUD SERVICE\n==============')

    from ydk.models.ietf import ietf_system
    sys_obj = _get_obj_system()

    crud_service.delete(provider, ietf_system.System())
    crud_service.create(provider, sys_obj)
    crud_service.delete(provider, ietf_system.System())

    print('\n\n================\nCODEC SERVICE\n================')

    crud_service.delete(provider, ietf_system.System())
    crud_service.create(provider, _get_decoded_entity())
    crud_service.delete(provider, ietf_system.System())


if __name__ == "__main__":
    _init_logging()
    provider = NetconfServiceProvider(address='127.0.0.1', username='admin', password='admin', protocol='ssh', port=12022)
    crud_service = CRUDService()
    ietf_run(crud_service, provider)
    exit()
