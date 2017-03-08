#!/usr/bin/env python
#  ----------------------------------------------------------------
# Copyright 2016 Cisco Systems
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compayloadiance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by appayloadicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or impayloadied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ------------------------------------------------------------------
""" Sampayloade

"""
from argparse import ArgumentParser

from ydk.app_maker import YdkAppMaker


def test_yam1():
    payload = '''
    <system xmlns="urn:ietf:params:xml:ns:yang:ietf-system">
      <contact>support@exampayloade.com</contact>
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
    yam = YdkAppMaker(type='xml')
    python_app = yam.payload2python(payload)
    print('Generated python app for ietf-system')


def test_yam2():
    payload = ''' <routing-policy xmlns="http://openconfig.net/yang/routing-policy">
        <policy-definitions>
          <policy-definition>
            <name>Politicas</name>
            <statements>
              <statement>
                <name>Black Hole</name>
                <name>ww</name>
                <actions>
                  <accept-route></accept-route>
                  <bgp-actions xmlns="http://openconfig.net/yang/bgp-policy">
                    <set-next-hop>192.0.2.1</set-next-hop>
                  </bgp-actions>
                </actions>
                <conditions>
                  <bgp-conditions xmlns="http://openconfig.net/yang/bgp-policy">
                    <match-community-set>
                      <community-set>blackHoleCli</community-set>
                      <match-set-options>ANY</match-set-options>
                    </match-community-set>
                  </bgp-conditions>
                </conditions>
              </statement>
              <statement>
                <name>Prefix Set</name>
                <conditions>
                  <match-prefix-set>
                    <match-set-options>ANY</match-set-options>
                    <prefix-set>int_BH</prefix-set>
                  </match-prefix-set>
                </conditions>
              </statement>
              <statement>
                <name>reject route</name>
                <actions>
                  <reject-route></reject-route>
                </actions>
              </statement>
            </statements>
          </policy-definition>
        </policy-definitions>
      </routing-policy>
'''
    yam = YdkAppMaker(type='xml')
    python_app = yam.payload2python(payload)
    print('Generated python app for openconfig-routing-policy')


def test_yam3():
    payload = '''
     <bgp xmlns="http://openconfig.net/yang/bgp">
  <global>
    <config>
      <as>65172</as>
      <router-id>1.2.3.4</router-id>
    </config>
  </global>
  <neighbors>
    <neighbor>
      <neighbor-address>6.7.8.9</neighbor-address>
      <config>
        <local-as>65001</local-as>
        <neighbor-address>6.7.8.9</neighbor-address>
        <peer-as>65001</peer-as>
        <peer-group>IBGP</peer-group>
      </config>
    </neighbor>
  </neighbors>
  <peer-groups>
    <peer-group>
      <peer-group-name>IBGP</peer-group-name>
      <config>
        <description>test description</description>
        <local-as>65001</local-as>
        <peer-as>65001</peer-as>
        <peer-group-name>IBGP</peer-group-name>
      </config>
    </peer-group>
  </peer-groups>
</bgp>
    '''
    yam = YdkAppMaker(type='xml')
    python_app = yam.payload2python(payload)
    print('Generated python app for openconfig-bgp')


def test_yam4():
    payload = '''
      <l2vpn xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-l2vpn-cfg">
      <nsr/>
      <l2vpn-router-id>1.2.3.4</l2vpn-router-id>
      <pw-routing>
        <pw-routing-global-id>12</pw-routing-global-id>
        <pw-routing-bgp>
          <enable/>
        </pw-routing-bgp>
      </pw-routing>
      <pwoam-refresh>23</pwoam-refresh>
      <database>
        <redundancy>
          <iccp-redundancy-groups>
            <iccp-redundancy-group>
              <group-id>23</group-id>
              <multi-homing-node-id>2</multi-homing-node-id>
            </iccp-redundancy-group>
          </iccp-redundancy-groups>
          <enable/>
        </redundancy>
      </database>
    </l2vpn>
    '''
    yam = YdkAppMaker(type='xml')
    python_app = yam.payload2python(payload)
    print('Generated python app for Cisco-IOS-XR-l2vpn-cfg')


def test_yam5():
    payload = '''    <mpls-te xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-mpls-te-cfg">
      <enable-traffic-engineering/>
      <named-tunnels>
        <enable/>
        <tunnels>
          <tunnel>
            <tunnel-name>LER1-LER2-t54</tunnel-name>
            <tunnel-type>p2p</tunnel-type>
            <enable/>
            <tunnel-attributes>
              <path-setups>
                <path-setup>
                  <path-setup-name>DYNAMIC</path-setup-name>
                  <enable/>
                  <preference>10</preference>
                  <path-computation>
                    <path-computation-method>dynamic</path-computation-method>
                  </path-computation>
                </path-setup>
              </path-setups>
              <bandwidth>
                <dste-type>pre-standard-dste</dste-type>
                <class-or-pool-type>0</class-or-pool-type>
                <bandwidth>100000</bandwidth>
              </bandwidth>
              <destination>172.16.255.2</destination>
              <fast-reroute>
                <bandwidth-protection>0</bandwidth-protection>
                <node-protection>0</node-protection>
              </fast-reroute>
            </tunnel-attributes>
          </tunnel>
        </tunnels>
      </named-tunnels>
    </mpls-te>'''
    yam = YdkAppMaker(type='xml')
    python_app = yam.payload2python(payload)
    print('Generated python app for Cisco-IOS-XR-mpls-te-cfg')
    
def test_yam6():
    payload='''<isis xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-clns-isis-cfg">
      <instances>
        <instance>
          <instance-name>DEFAULT</instance-name>
          <afs>
            <af>
              <af-name>ipv4</af-name>
              <saf-name>unicast</saf-name>
              <af-data>
                <metric-styles>
                  <metric-style>
                    <level>not-set</level>
                    <style>new-metric-style</style>
                    <transition-state>disabled</transition-state>
                  </metric-style>
                </metric-styles>
                <segment-routing>
                  <mpls>ldp</mpls>
                </segment-routing>
              </af-data>
            </af>
          </afs>
          <interfaces>
            <interface>
              <interface-name>Loopback0</interface-name>
              <interface-afs>
                <interface-af>
                  <af-name>ipv4</af-name>
                  <saf-name>unicast</saf-name>
                  <interface-af-data>
                    <prefix-sid>
                      <explicit-null>disable</explicit-null>
                      <nflag-clear>disable</nflag-clear>
                      <php>enable</php>
                      <type>absolute</type>
                      <value>16041</value>
                    </prefix-sid>
                    <running></running>
                  </interface-af-data>
                </interface-af>
              </interface-afs>
              <running></running>
              <state>passive</state>
            </interface>
            <interface>
              <interface-name>GigabitEthernet0/0/0/0</interface-name>
              <interface-afs>
                <interface-af>
                  <af-name>ipv4</af-name>
                  <saf-name>unicast</saf-name>
                  <interface-af-data>
                    <running></running>
                  </interface-af-data>
                </interface-af>
              </interface-afs>
              <point-to-point></point-to-point>
              <running></running>
            </interface>
          </interfaces>
          <is-type>level2</is-type>
          <nets>
            <net>
              <net-name>49.0000.1720.1625.5001.00</net-name>
            </net>
          </nets>
          <running></running>
        </instance>
      </instances>
    </isis>
    '''
    yam = YdkAppMaker(type='xml')
    python_app = yam.payload2python(payload)
    print('Generated python app for Cisco-IOS-XR-clns-isis-cfg')


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-v", "--verbose", help="print debugging messages",
                        action="store_true")    
    args = parser.parse_args()

    # log debug messages if verbose argument specified
    if args.verbose:
        import logging
        logger = logging.getLogger("ydk")
        logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        logger.addHandler(handler)

    test_yam1()
    test_yam2()
    test_yam3()
    test_yam4()
    test_yam5()
    test_yam6()

