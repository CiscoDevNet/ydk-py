


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'CISCOVLANIFTABLERELATIONSHIPMIB.CviVlanInterfaceIndexTable.CviVlanInterfaceIndexEntry' : {
        'meta_info' : _MetaInfoClass('CISCOVLANIFTABLERELATIONSHIPMIB.CviVlanInterfaceIndexTable.CviVlanInterfaceIndexEntry',
            False, 
            [
            _MetaInfoClassMember('cviPhysicalIfIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 2147483647)], [], 
                '''                For subinterfaces, this object is the ifIndex of the
                physical interface for the subinterface.
                
                For Switch Virtual Interfaces (SVIs), this object is zero.
                ''',
                'cviphysicalifindex',
                'CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB', True),
            _MetaInfoClassMember('cviVlanId', ATTRIBUTE, 'int' , None, None, 
                [(0, 4095)], [], 
                '''                The VLAN-id number of the routed VLAN interface.
                ''',
                'cvivlanid',
                'CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB', True),
            _MetaInfoClassMember('cviRoutedVlanIfIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                The index for the ifTable entry associated with
                this routed VLAN interface.
                ''',
                'cviroutedvlanifindex',
                'CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB', False),
            ],
            'CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB',
            'cviVlanInterfaceIndexEntry',
            _yang_ns._namespaces['CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB'],
        'ydk.models.vlan.CISCO_VLAN_IFTABLE_RELATIONSHIP_MIB'
        ),
    },
    'CISCOVLANIFTABLERELATIONSHIPMIB.CviVlanInterfaceIndexTable' : {
        'meta_info' : _MetaInfoClass('CISCOVLANIFTABLERELATIONSHIPMIB.CviVlanInterfaceIndexTable',
            False, 
            [
            _MetaInfoClassMember('cviVlanInterfaceIndexEntry', REFERENCE_LIST, 'CviVlanInterfaceIndexEntry' , 'ydk.models.vlan.CISCO_VLAN_IFTABLE_RELATIONSHIP_MIB', 'CISCOVLANIFTABLERELATIONSHIPMIB.CviVlanInterfaceIndexTable.CviVlanInterfaceIndexEntry', 
                [], [], 
                '''                Each entry represents a routed VLAN interface, its
                corresponding physical port if any, and the ifTable entry
                for the routed VLAN interface.
                
                Entries are created by the agent when the routed VLAN interface
                is created.  Operational status of routing does not affect
                the entries listed here.  For routing configuration please refer
                to ipRouteTable.
                
                Entries are deleted by the agent when the routed VLAN interface
                is removed from the system configuration.
                ''',
                'cvivlaninterfaceindexentry',
                'CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB', False),
            ],
            'CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB',
            'cviVlanInterfaceIndexTable',
            _yang_ns._namespaces['CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB'],
        'ydk.models.vlan.CISCO_VLAN_IFTABLE_RELATIONSHIP_MIB'
        ),
    },
    'CISCOVLANIFTABLERELATIONSHIPMIB' : {
        'meta_info' : _MetaInfoClass('CISCOVLANIFTABLERELATIONSHIPMIB',
            False, 
            [
            _MetaInfoClassMember('cviVlanInterfaceIndexTable', REFERENCE_CLASS, 'CviVlanInterfaceIndexTable' , 'ydk.models.vlan.CISCO_VLAN_IFTABLE_RELATIONSHIP_MIB', 'CISCOVLANIFTABLERELATIONSHIPMIB.CviVlanInterfaceIndexTable', 
                [], [], 
                '''                The cviVlanInterfaceIndexTable provides a way to
                translate a VLAN-id in to an ifIndex, so that 
                the routed VLAN interface's routing configuration 
                can be obtained from interface entry in ipRouteTable.
                
                Note that some routers can have interfaces to multiple
                VLAN management domains, and therefore can have multiple 
                routed VLAN interfaces which connect to different VLANs 
                having the same VLAN-id.  Thus, it is possible to have 
                multiple rows in this table for the same VLAN-id.
                
                The cviVlanInterfaceIndexTable also provides a way
                to find the VLAN-id from an ifTable VLAN's ifIndex.
                ''',
                'cvivlaninterfaceindextable',
                'CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB', False),
            ],
            'CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB',
            'CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB',
            _yang_ns._namespaces['CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB'],
        'ydk.models.vlan.CISCO_VLAN_IFTABLE_RELATIONSHIP_MIB'
        ),
    },
}
_meta_table['CISCOVLANIFTABLERELATIONSHIPMIB.CviVlanInterfaceIndexTable.CviVlanInterfaceIndexEntry']['meta_info'].parent =_meta_table['CISCOVLANIFTABLERELATIONSHIPMIB.CviVlanInterfaceIndexTable']['meta_info']
_meta_table['CISCOVLANIFTABLERELATIONSHIPMIB.CviVlanInterfaceIndexTable']['meta_info'].parent =_meta_table['CISCOVLANIFTABLERELATIONSHIPMIB']['meta_info']
