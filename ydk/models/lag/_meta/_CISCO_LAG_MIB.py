


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'ClagPortAdminStatus_Enum' : _MetaInfoEnum('ClagPortAdminStatus_Enum', 'ydk.models.lag.CISCO_LAG_MIB',
        {
            'off':'OFF',
            'on':'ON',
            'active':'ACTIVE',
            'passive':'PASSIVE',
        }, 'CISCO-LAG-MIB', _yang_ns._namespaces['CISCO-LAG-MIB']),
    'ClagAggregationProtocol_Enum' : _MetaInfoEnum('ClagAggregationProtocol_Enum', 'ydk.models.lag.CISCO_LAG_MIB',
        {
            'lacp':'LACP',
            'pagp':'PAGP',
        }, 'CISCO-LAG-MIB', _yang_ns._namespaces['CISCO-LAG-MIB']),
    'ClagDistributionProtocol_Enum' : _MetaInfoEnum('ClagDistributionProtocol_Enum', 'ydk.models.lag.CISCO_LAG_MIB',
        {
            'ip':'IP',
            'mac':'MAC',
            'port':'PORT',
            'vlanIpPort':'VLANIPPORT',
            'vlanIp':'VLANIP',
            'ipPort':'IPPORT',
        }, 'CISCO-LAG-MIB', _yang_ns._namespaces['CISCO-LAG-MIB']),
    'ClagDistributionAddressMode_Enum' : _MetaInfoEnum('ClagDistributionAddressMode_Enum', 'ydk.models.lag.CISCO_LAG_MIB',
        {
            'source':'SOURCE',
            'destination':'DESTINATION',
            'both':'BOTH',
        }, 'CISCO-LAG-MIB', _yang_ns._namespaces['CISCO-LAG-MIB']),
    'ClagDistributionMplsProtocol_Enum' : _MetaInfoEnum('ClagDistributionMplsProtocol_Enum', 'ydk.models.lag.CISCO_LAG_MIB',
        {
            'label':'LABEL',
            'labelIp':'LABELIP',
        }, 'CISCO-LAG-MIB', _yang_ns._namespaces['CISCO-LAG-MIB']),
    'CISCOLAGMIB.ClagAggChannelIfTable.ClagAggChannelIfEntry.ClagAggChannelIfHashDistAdminMethod_Enum' : _MetaInfoEnum('ClagAggChannelIfHashDistAdminMethod_Enum', 'ydk.models.lag.CISCO_LAG_MIB',
        {
            'none':'NONE',
            'adaptive':'ADAPTIVE',
            'fixed':'FIXED',
        }, 'CISCO-LAG-MIB', _yang_ns._namespaces['CISCO-LAG-MIB']),
    'CISCOLAGMIB.ClagAggChannelIfTable.ClagAggChannelIfEntry.ClagAggChannelIfHashDistOperMethod_Enum' : _MetaInfoEnum('ClagAggChannelIfHashDistOperMethod_Enum', 'ydk.models.lag.CISCO_LAG_MIB',
        {
            'other':'OTHER',
            'adaptive':'ADAPTIVE',
            'fixed':'FIXED',
        }, 'CISCO-LAG-MIB', _yang_ns._namespaces['CISCO-LAG-MIB']),
    'CISCOLAGMIB.ClagAggChannelIfTable.ClagAggChannelIfEntry' : {
        'meta_info' : _MetaInfoClass('CISCOLAGMIB.ClagAggChannelIfTable.ClagAggChannelIfEntry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'ifindex',
                'CISCO-LAG-MIB', True),
            _MetaInfoClassMember('clagAggChannelIfFastSwitchOver', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Specifies whether LACP protocol fast switchover
                mode is enabled on this port channel interface
                or not.
                ''',
                'clagaggchanneliffastswitchover',
                'CISCO-LAG-MIB', False),
            _MetaInfoClassMember('clagAggChannelIfHashDistAdminMethod', REFERENCE_ENUM_CLASS, 'ClagAggChannelIfHashDistAdminMethod_Enum' , 'ydk.models.lag.CISCO_LAG_MIB', 'CISCOLAGMIB.ClagAggChannelIfTable.ClagAggChannelIfEntry.ClagAggChannelIfHashDistAdminMethod_Enum', 
                [], [], 
                '''                Specifies the hash distribution method that is administratively
                configured on this port channel interface upon its channel 
                membership transition event. 
                
                none(1)      :  Hash distribution algorithm on this 
                                port channel interface is not specifically 
                                configured and global configuration of 
                                clagAggHashDistMethodGlobalConfig will
                                be applied on this port channel interface.
                adaptive(2)  :  Adaptive hash distribution for this port 
                                channel interface among its channel members.
                fixed(3)     :  Fixed hash distribution for this port channel
                                interface among its channel members.
                ''',
                'clagaggchannelifhashdistadminmethod',
                'CISCO-LAG-MIB', False),
            _MetaInfoClassMember('clagAggChannelIfHashDistOperMethod', REFERENCE_ENUM_CLASS, 'ClagAggChannelIfHashDistOperMethod_Enum' , 'ydk.models.lag.CISCO_LAG_MIB', 'CISCOLAGMIB.ClagAggChannelIfTable.ClagAggChannelIfEntry.ClagAggChannelIfHashDistOperMethod_Enum', 
                [], [], 
                '''                Specifies the operational hash distribution method
                for this port channel interface among the port channel members.
                
                other(1)        : None of the following. 
                adaptive(2)     : Adaptive hash distribution for the 
                                  port channel interface among its 
                                  channel members.
                fixed(3)        : Fixed hash distribution for the port
                                  channel among channel members.
                ''',
                'clagaggchannelifhashdistopermethod',
                'CISCO-LAG-MIB', False),
            _MetaInfoClassMember('clagAggChannelIfMaxBundle', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                Specifies the maximum number of member
                ports that can be bundled on this port
                channel interface for LACP protocol.
                ''',
                'clagaggchannelifmaxbundle',
                'CISCO-LAG-MIB', False),
            _MetaInfoClassMember('clagAggChannelIfMinLink', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Specifies the minimum number of bundled member ports that are
                needed in order for this port channel interface to be
                operational.
                A value of zero for this object indicates that no minimum
                number of bundled member ports are required for this port
                channel interface to be operational.
                ''',
                'clagaggchannelifminlink',
                'CISCO-LAG-MIB', False),
            ],
            'CISCO-LAG-MIB',
            'clagAggChannelIfEntry',
            _yang_ns._namespaces['CISCO-LAG-MIB'],
        'ydk.models.lag.CISCO_LAG_MIB'
        ),
    },
    'CISCOLAGMIB.ClagAggChannelIfTable' : {
        'meta_info' : _MetaInfoClass('CISCOLAGMIB.ClagAggChannelIfTable',
            False, 
            [
            _MetaInfoClassMember('clagAggChannelIfEntry', REFERENCE_LIST, 'ClagAggChannelIfEntry' , 'ydk.models.lag.CISCO_LAG_MIB', 'CISCOLAGMIB.ClagAggChannelIfTable.ClagAggChannelIfEntry', 
                [], [], 
                '''                An entry containing port channel
                configuration information for port 
                channel interfaces.
                ''',
                'clagaggchannelifentry',
                'CISCO-LAG-MIB', False),
            ],
            'CISCO-LAG-MIB',
            'clagAggChannelIfTable',
            _yang_ns._namespaces['CISCO-LAG-MIB'],
        'ydk.models.lag.CISCO_LAG_MIB'
        ),
    },
    'CISCOLAGMIB.ClagAggProtocolTable.ClagAggProtocolEntry' : {
        'meta_info' : _MetaInfoClass('CISCOLAGMIB.ClagAggProtocolTable.ClagAggProtocolEntry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'ifindex',
                'CISCO-LAG-MIB', True),
            _MetaInfoClassMember('clagAggProtocolType', REFERENCE_ENUM_CLASS, 'ClagAggregationProtocol_Enum' , 'ydk.models.lag.CISCO_LAG_MIB', 'ClagAggregationProtocol_Enum', 
                [], [], 
                '''                The aggregation protocol type for the interface.
                
                On some platforms, aggregation protocol may be assigned per
                group.  The group can be a collection of the ports which belong
                to a module or system.  If the aggregation protocol is assigned
                to any of the ports in such group then the aggregation protocol
                will apply to all ports in the same group.
                
                On some platforms, aggregation protocol type  can be assigned
                per aggregator.  If multiple ports belong to a aggregator,
                the aggregation protocol assigned to any of the ports in such
                aggregator will apply to all ports in the same.
                ''',
                'clagaggprotocoltype',
                'CISCO-LAG-MIB', False),
            ],
            'CISCO-LAG-MIB',
            'clagAggProtocolEntry',
            _yang_ns._namespaces['CISCO-LAG-MIB'],
        'ydk.models.lag.CISCO_LAG_MIB'
        ),
    },
    'CISCOLAGMIB.ClagAggProtocolTable' : {
        'meta_info' : _MetaInfoClass('CISCOLAGMIB.ClagAggProtocolTable',
            False, 
            [
            _MetaInfoClassMember('clagAggProtocolEntry', REFERENCE_LIST, 'ClagAggProtocolEntry' , 'ydk.models.lag.CISCO_LAG_MIB', 'CISCOLAGMIB.ClagAggProtocolTable.ClagAggProtocolEntry', 
                [], [], 
                '''                Entry containing aggregation protocol type for a
                particular interface.  An entry is created in this
                table when its associated ifEntry is created and that 
                interface supports link aggregation.  The entry of this
                table is deleted when the associated ifEntry is removed.
                ''',
                'clagaggprotocolentry',
                'CISCO-LAG-MIB', False),
            ],
            'CISCO-LAG-MIB',
            'clagAggProtocolTable',
            _yang_ns._namespaces['CISCO-LAG-MIB'],
        'ydk.models.lag.CISCO_LAG_MIB'
        ),
    },
    'CISCOLAGMIB.ClagGlobalConfigObjects.ClagAggHashDistMethodGlobalConfig_Enum' : _MetaInfoEnum('ClagAggHashDistMethodGlobalConfig_Enum', 'ydk.models.lag.CISCO_LAG_MIB',
        {
            'adaptive':'ADAPTIVE',
            'fixed':'FIXED',
        }, 'CISCO-LAG-MIB', _yang_ns._namespaces['CISCO-LAG-MIB']),
    'CISCOLAGMIB.ClagGlobalConfigObjects' : {
        'meta_info' : _MetaInfoClass('CISCOLAGMIB.ClagGlobalConfigObjects',
            False, 
            [
            _MetaInfoClassMember('clagAggDistributionAddressMode', REFERENCE_ENUM_CLASS, 'ClagDistributionAddressMode_Enum' , 'ydk.models.lag.CISCO_LAG_MIB', 'ClagDistributionAddressMode_Enum', 
                [], [], 
                '''                The load balancing address mode for the device.
                ''',
                'clagaggdistributionaddressmode',
                'CISCO-LAG-MIB', False),
            _MetaInfoClassMember('clagAggDistributionMplsProtocol', REFERENCE_ENUM_CLASS, 'ClagDistributionMplsProtocol_Enum' , 'ydk.models.lag.CISCO_LAG_MIB', 'ClagDistributionMplsProtocol_Enum', 
                [], [], 
                '''                This object controls the load balancing algorithms
                used on this port channel interface to distribute 
                outgoing MPLS data frames among its component interfaces.
                
                This object is only instantiated on platforms which 
                support aggregation load balancing for MPLS packets.
                ''',
                'clagaggdistributionmplsprotocol',
                'CISCO-LAG-MIB', False),
            _MetaInfoClassMember('clagAggDistributionProtocol', REFERENCE_ENUM_CLASS, 'ClagDistributionProtocol_Enum' , 'ydk.models.lag.CISCO_LAG_MIB', 'ClagDistributionProtocol_Enum', 
                [], [], 
                '''                This object controls the load balancing algorithms
                used on this port channel interface to distribute outgoing 
                data frames among its component interfaces.
                ''',
                'clagaggdistributionprotocol',
                'CISCO-LAG-MIB', False),
            _MetaInfoClassMember('clagAggHashDistMethodGlobalConfig', REFERENCE_ENUM_CLASS, 'ClagAggHashDistMethodGlobalConfig_Enum' , 'ydk.models.lag.CISCO_LAG_MIB', 'CISCOLAGMIB.ClagGlobalConfigObjects.ClagAggHashDistMethodGlobalConfig_Enum', 
                [], [], 
                '''                Specifies the global configuration for hash
                distribution method applied on a port channel 
                interface among its channel members.
                
                adaptive(1)  :  Adaptive hash distribution for the bundle
                                among port channel members.
                fixed(2)     :  Fixed hash distribution for the bundle
                                among port channel members.
                ''',
                'clagagghashdistmethodglobalconfig',
                'CISCO-LAG-MIB', False),
            _MetaInfoClassMember('clagAggMaxAggregators', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object indicates the maximum number of aggregators
                supported by the device.
                ''',
                'clagaggmaxaggregators',
                'CISCO-LAG-MIB', False),
            ],
            'CISCO-LAG-MIB',
            'clagGlobalConfigObjects',
            _yang_ns._namespaces['CISCO-LAG-MIB'],
        'ydk.models.lag.CISCO_LAG_MIB'
        ),
    },
    'CISCOLAGMIB' : {
        'meta_info' : _MetaInfoClass('CISCOLAGMIB',
            False, 
            [
            _MetaInfoClassMember('clagAggChannelIfTable', REFERENCE_CLASS, 'ClagAggChannelIfTable' , 'ydk.models.lag.CISCO_LAG_MIB', 'CISCOLAGMIB.ClagAggChannelIfTable', 
                [], [], 
                '''                A table providing port channel
                configuration information for port channel
                interfaces identified by ifIndex.
                ''',
                'clagaggchanneliftable',
                'CISCO-LAG-MIB', False),
            _MetaInfoClassMember('clagAggProtocolTable', REFERENCE_CLASS, 'ClagAggProtocolTable' , 'ydk.models.lag.CISCO_LAG_MIB', 'CISCOLAGMIB.ClagAggProtocolTable', 
                [], [], 
                '''                A table that contains protocol information about every
                interface which supports link aggregation.
                ''',
                'clagaggprotocoltable',
                'CISCO-LAG-MIB', False),
            _MetaInfoClassMember('clagGlobalConfigObjects', REFERENCE_CLASS, 'ClagGlobalConfigObjects' , 'ydk.models.lag.CISCO_LAG_MIB', 'CISCOLAGMIB.ClagGlobalConfigObjects', 
                [], [], 
                '''                ''',
                'clagglobalconfigobjects',
                'CISCO-LAG-MIB', False),
            ],
            'CISCO-LAG-MIB',
            'CISCO-LAG-MIB',
            _yang_ns._namespaces['CISCO-LAG-MIB'],
        'ydk.models.lag.CISCO_LAG_MIB'
        ),
    },
}
_meta_table['CISCOLAGMIB.ClagAggChannelIfTable.ClagAggChannelIfEntry']['meta_info'].parent =_meta_table['CISCOLAGMIB.ClagAggChannelIfTable']['meta_info']
_meta_table['CISCOLAGMIB.ClagAggProtocolTable.ClagAggProtocolEntry']['meta_info'].parent =_meta_table['CISCOLAGMIB.ClagAggProtocolTable']['meta_info']
_meta_table['CISCOLAGMIB.ClagAggChannelIfTable']['meta_info'].parent =_meta_table['CISCOLAGMIB']['meta_info']
_meta_table['CISCOLAGMIB.ClagAggProtocolTable']['meta_info'].parent =_meta_table['CISCOLAGMIB']['meta_info']
_meta_table['CISCOLAGMIB.ClagGlobalConfigObjects']['meta_info'].parent =_meta_table['CISCOLAGMIB']['meta_info']
