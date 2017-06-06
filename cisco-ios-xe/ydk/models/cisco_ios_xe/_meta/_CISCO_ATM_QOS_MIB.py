


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'VcparamconfiglocationEnum' : _MetaInfoEnum('VcparamconfiglocationEnum', 'ydk.models.cisco_ios_xe.CISCO_ATM_QOS_MIB',
        {
            'configDefault':'configDefault',
            'configVcDirect':'configVcDirect',
            'configVcClass':'configVcClass',
            'configVcClassSubInterface':'configVcClassSubInterface',
            'configVcClassInterface':'configVcClassInterface',
        }, 'CISCO-ATM-QOS-MIB', _yang_ns._namespaces['CISCO-ATM-QOS-MIB']),
    'VpstateEnum' : _MetaInfoEnum('VpstateEnum', 'ydk.models.cisco_ios_xe.CISCO_ATM_QOS_MIB',
        {
            'vpStateInactive':'vpStateInactive',
            'vpStateActive':'vpStateActive',
        }, 'CISCO-ATM-QOS-MIB', _yang_ns._namespaces['CISCO-ATM-QOS-MIB']),
    'CiscoAtmQosMib.Caqvccparamstable.Caqvccparamsentry' : {
        'meta_info' : _MetaInfoClass('CiscoAtmQosMib.Caqvccparamstable.Caqvccparamsentry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'CISCO-ATM-QOS-MIB', True),
            _MetaInfoClassMember('atmVclVpi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4095')], [], 
                '''                ''',
                'atmvclvpi',
                'CISCO-ATM-QOS-MIB', True),
            _MetaInfoClassMember('atmVclVci', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                ''',
                'atmvclvci',
                'CISCO-ATM-QOS-MIB', True),
            _MetaInfoClassMember('caqVccParamsAdtf', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Allowed cell rate decrease time factor.
                ''',
                'caqvccparamsadtf',
                'CISCO-ATM-QOS-MIB', False),
            _MetaInfoClassMember('caqVccParamsBcsIn0', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Input Burst Cell Size (BCS) for connection
                with VBR type of QoS and
                Cell Loss Priority bit set to 0 (clp0).
                ''',
                'caqvccparamsbcsin0',
                'CISCO-ATM-QOS-MIB', False),
            _MetaInfoClassMember('caqVccParamsBcsIn01', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Input Burst Cell Size (BCS) for connection
                with VBR type of QoS and
                Cell Loss Priority bit set to 1 (clp01).
                ''',
                'caqvccparamsbcsin01',
                'CISCO-ATM-QOS-MIB', False),
            _MetaInfoClassMember('caqVccParamsBcsOut0', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Output Burst Cell Size (BCS) for connection
                with VBR type of QoS and 
                Cell Loss Priority bit set to 0 (clp0).
                ''',
                'caqvccparamsbcsout0',
                'CISCO-ATM-QOS-MIB', False),
            _MetaInfoClassMember('caqVccParamsBcsOut01', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Output Burst Cell Size (BCS) for connection
                with VBR type of QoS and
                Cell Loss Priority bit set to 1 (clp01).
                ''',
                'caqvccparamsbcsout01',
                'CISCO-ATM-QOS-MIB', False),
            _MetaInfoClassMember('caqVccParamsCdv', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Cell delay variation.
                ''',
                'caqvccparamscdv',
                'CISCO-ATM-QOS-MIB', False),
            _MetaInfoClassMember('caqVccParamsCdvt', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Cell delay variation tolerance.
                ''',
                'caqvccparamscdvt',
                'CISCO-ATM-QOS-MIB', False),
            _MetaInfoClassMember('caqVccParamsFrtt', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Fixed round-trip time.
                ''',
                'caqvccparamsfrtt',
                'CISCO-ATM-QOS-MIB', False),
            _MetaInfoClassMember('caqVccParamsIcr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Initial cell rate.
                ''',
                'caqvccparamsicr',
                'CISCO-ATM-QOS-MIB', False),
            _MetaInfoClassMember('caqVccParamsInheritLevel', REFERENCE_ENUM_CLASS, 'VcparamconfiglocationEnum' , 'ydk.models.cisco_ios_xe.CISCO_ATM_QOS_MIB', 'VcparamconfiglocationEnum', 
                [], [], 
                '''                The source of configuration for peak cell rate.
                ''',
                'caqvccparamsinheritlevel',
                'CISCO-ATM-QOS-MIB', False),
            _MetaInfoClassMember('caqVccParamsInvCdf', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Inverse of cutoff decrease factor.
                ''',
                'caqvccparamsinvcdf',
                'CISCO-ATM-QOS-MIB', False),
            _MetaInfoClassMember('caqVccParamsInvRdf', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Inverse of rate decrease factor.
                ''',
                'caqvccparamsinvrdf',
                'CISCO-ATM-QOS-MIB', False),
            _MetaInfoClassMember('caqVccParamsInvRif', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Inverse of rate increase factor.
                ''',
                'caqvccparamsinvrif',
                'CISCO-ATM-QOS-MIB', False),
            _MetaInfoClassMember('caqVccParamsInvTrm', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum time between forward rm cells.
                ''',
                'caqvccparamsinvtrm',
                'CISCO-ATM-QOS-MIB', False),
            _MetaInfoClassMember('caqVccParamsMcrIn', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Input Minimum Cell Rate (MCR) in kbps for
                connection with VBR-nrt or ABR type of QoS.
                ''',
                'caqvccparamsmcrin',
                'CISCO-ATM-QOS-MIB', False),
            _MetaInfoClassMember('caqVccParamsMcrOut', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Output Minimum Cell Rate (MCR) in kbps for
                connection with VBR-nrt or ABR type of QoS.
                ''',
                'caqvccparamsmcrout',
                'CISCO-ATM-QOS-MIB', False),
            _MetaInfoClassMember('caqVccParamsNrm', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of tx cells for each forward rm cell.
                ''',
                'caqvccparamsnrm',
                'CISCO-ATM-QOS-MIB', False),
            _MetaInfoClassMember('caqVccParamsPcrIn0', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Input Peak Cell Rate (PCR) in kbps with 
                Cell Loss Priority bit set to 0 (clp0).
                ''',
                'caqvccparamspcrin0',
                'CISCO-ATM-QOS-MIB', False),
            _MetaInfoClassMember('caqVccParamsPcrIn01', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of OAM F5 end to end loopback cells sent through
                the VCC.
                ''',
                'caqvccparamspcrin01',
                'CISCO-ATM-QOS-MIB', False),
            _MetaInfoClassMember('caqVccParamsPcrOut0', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Output Peak Cell Rate (PCR) in kbps with
                Cell Loss Priority bit set to 0 (clp0).
                ''',
                'caqvccparamspcrout0',
                'CISCO-ATM-QOS-MIB', False),
            _MetaInfoClassMember('caqVccParamsPcrOut01', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Output Peak Cell Rate (PCR) in kbps with
                Cell Loss Priority bit set to 1 (clp01).
                ''',
                'caqvccparamspcrout01',
                'CISCO-ATM-QOS-MIB', False),
            _MetaInfoClassMember('caqVccParamsRfl', REFERENCE_ENUM_CLASS, 'VcparamconfiglocationEnum' , 'ydk.models.cisco_ios_xe.CISCO_ATM_QOS_MIB', 'VcparamconfiglocationEnum', 
                [], [], 
                '''                The source of configuration for rate factor.
                ''',
                'caqvccparamsrfl',
                'CISCO-ATM-QOS-MIB', False),
            _MetaInfoClassMember('caqVccParamsScrIn0', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Input Sustained Cell Rate (SCR) in kbps
                for connection with VBR type of QoS and
                Cell Loss Priority bit set to 0 (clp0).
                ''',
                'caqvccparamsscrin0',
                'CISCO-ATM-QOS-MIB', False),
            _MetaInfoClassMember('caqVccParamsScrIn01', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Input Sustained Cell Rate (SCR) in kbps
                for connection with VBR type of QoS and
                Cell Loss Priority bit set to 1 (clp01).
                ''',
                'caqvccparamsscrin01',
                'CISCO-ATM-QOS-MIB', False),
            _MetaInfoClassMember('caqVccParamsScrOut0', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Output Sustained Cell Rate (SCR) in kbps
                for connection with VBR type of QoS and
                Cell Loss Priority bit set to 0 (clp0).
                ''',
                'caqvccparamsscrout0',
                'CISCO-ATM-QOS-MIB', False),
            _MetaInfoClassMember('caqVccParamsScrOut01', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Output Sustained Cell Rate (SCR) in kbps
                for connection with VBR type of QoS and
                Cell Loss Priority bit set to 1 (clp01).
                ''',
                'caqvccparamsscrout01',
                'CISCO-ATM-QOS-MIB', False),
            _MetaInfoClassMember('caqVccParamsTbe', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Transient buffer exposure.
                ''',
                'caqvccparamstbe',
                'CISCO-ATM-QOS-MIB', False),
            _MetaInfoClassMember('caqVccParamsType', REFERENCE_ENUM_CLASS, 'AtmservicecategoryEnum' , 'ydk.models.cisco_ios_xe.ATM_FORUM_TC_MIB', 'AtmservicecategoryEnum', 
                [], [], 
                '''                The service category of this virtual circuit connection.
                ''',
                'caqvccparamstype',
                'CISCO-ATM-QOS-MIB', False),
            ],
            'CISCO-ATM-QOS-MIB',
            'caqVccParamsEntry',
            _yang_ns._namespaces['CISCO-ATM-QOS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ATM_QOS_MIB'
        ),
    },
    'CiscoAtmQosMib.Caqvccparamstable' : {
        'meta_info' : _MetaInfoClass('CiscoAtmQosMib.Caqvccparamstable',
            False, 
            [
            _MetaInfoClassMember('caqVccParamsEntry', REFERENCE_LIST, 'Caqvccparamsentry' , 'ydk.models.cisco_ios_xe.CISCO_ATM_QOS_MIB', 'CiscoAtmQosMib.Caqvccparamstable.Caqvccparamsentry', 
                [], [], 
                '''                This list contains the ATM QoS parameters provided by
                ciscoAtmQosVccEntry.
                ''',
                'caqvccparamsentry',
                'CISCO-ATM-QOS-MIB', False),
            ],
            'CISCO-ATM-QOS-MIB',
            'caqVccParamsTable',
            _yang_ns._namespaces['CISCO-ATM-QOS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ATM_QOS_MIB'
        ),
    },
    'CiscoAtmQosMib.Caqvpcparamstable.Caqvpcparamsentry' : {
        'meta_info' : _MetaInfoClass('CiscoAtmQosMib.Caqvpcparamstable.Caqvpcparamsentry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'CISCO-ATM-QOS-MIB', True),
            _MetaInfoClassMember('atmVplVpi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4095')], [], 
                '''                ''',
                'atmvplvpi',
                'CISCO-ATM-QOS-MIB', True),
            _MetaInfoClassMember('caqVpcParamsAvailBw', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Bandwidth in Kbps currently currently available
                on this PVP.
                ''',
                'caqvpcparamsavailbw',
                'CISCO-ATM-QOS-MIB', False),
            _MetaInfoClassMember('caqVpcParamsCesRate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum rate in kbps at which CES VCs can transmit
                data with the associated permanent virtual path.
                ''',
                'caqvpcparamscesrate',
                'CISCO-ATM-QOS-MIB', False),
            _MetaInfoClassMember('caqVpcParamsCesVcCount', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Number of CES VCs currently associated with
                the permanent virtual path.
                ''',
                'caqvpcparamscesvccount',
                'CISCO-ATM-QOS-MIB', False),
            _MetaInfoClassMember('caqVpcParamsDataVcCount', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Number of data VCs currently associated with
                the permanent virtual path.
                ''',
                'caqvpcparamsdatavccount',
                'CISCO-ATM-QOS-MIB', False),
            _MetaInfoClassMember('caqVpcParamsMbs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum burst size associated with the PVP.
                ''',
                'caqvpcparamsmbs',
                'CISCO-ATM-QOS-MIB', False),
            _MetaInfoClassMember('caqVpcParamsPeakRate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum rate in kbps at which the associated
                permanent virtual path can transmit data.
                ''',
                'caqvpcparamspeakrate',
                'CISCO-ATM-QOS-MIB', False),
            _MetaInfoClassMember('caqVpcParamsScr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sustained cell rate associated with the PVP.
                ''',
                'caqvpcparamsscr',
                'CISCO-ATM-QOS-MIB', False),
            _MetaInfoClassMember('caqVpcParamsVcdF4Ete', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Vcd for F4 OAM end to end processing.
                ''',
                'caqvpcparamsvcdf4ete',
                'CISCO-ATM-QOS-MIB', False),
            _MetaInfoClassMember('caqVpcParamsVcdF4Seg', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Vcd for F4 OAM segment processing.
                ''',
                'caqvpcparamsvcdf4seg',
                'CISCO-ATM-QOS-MIB', False),
            _MetaInfoClassMember('caqVpcParamsVpState', REFERENCE_ENUM_CLASS, 'VpstateEnum' , 'ydk.models.cisco_ios_xe.CISCO_ATM_QOS_MIB', 'VpstateEnum', 
                [], [], 
                '''                VP state of the current permanent virtual path.
                ''',
                'caqvpcparamsvpstate',
                'CISCO-ATM-QOS-MIB', False),
            ],
            'CISCO-ATM-QOS-MIB',
            'caqVpcParamsEntry',
            _yang_ns._namespaces['CISCO-ATM-QOS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ATM_QOS_MIB'
        ),
    },
    'CiscoAtmQosMib.Caqvpcparamstable' : {
        'meta_info' : _MetaInfoClass('CiscoAtmQosMib.Caqvpcparamstable',
            False, 
            [
            _MetaInfoClassMember('caqVpcParamsEntry', REFERENCE_LIST, 'Caqvpcparamsentry' , 'ydk.models.cisco_ios_xe.CISCO_ATM_QOS_MIB', 'CiscoAtmQosMib.Caqvpcparamstable.Caqvpcparamsentry', 
                [], [], 
                '''                This list contains the ATM QoS parameters provided by
                ciscoAtmQosVpcEntry.
                ''',
                'caqvpcparamsentry',
                'CISCO-ATM-QOS-MIB', False),
            ],
            'CISCO-ATM-QOS-MIB',
            'caqVpcParamsTable',
            _yang_ns._namespaces['CISCO-ATM-QOS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ATM_QOS_MIB'
        ),
    },
    'CiscoAtmQosMib.Caqqueuingparamstable.Caqqueuingparamsentry' : {
        'meta_info' : _MetaInfoClass('CiscoAtmQosMib.Caqqueuingparamstable.Caqqueuingparamsentry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'CISCO-ATM-QOS-MIB', True),
            _MetaInfoClassMember('atmVclVpi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4095')], [], 
                '''                ''',
                'atmvclvpi',
                'CISCO-ATM-QOS-MIB', True),
            _MetaInfoClassMember('atmVclVci', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                ''',
                'atmvclvci',
                'CISCO-ATM-QOS-MIB', True),
            _MetaInfoClassMember('caqQueuingParamsMeanQDepth', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Mean Queue Depth associated with the vc.  This value
                is calculated based on the actual queue depth on the
                interface and the exponential weighting constant.
                ''',
                'caqqueuingparamsmeanqdepth',
                'CISCO-ATM-QOS-MIB', False),
            ],
            'CISCO-ATM-QOS-MIB',
            'caqQueuingParamsEntry',
            _yang_ns._namespaces['CISCO-ATM-QOS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ATM_QOS_MIB'
        ),
    },
    'CiscoAtmQosMib.Caqqueuingparamstable' : {
        'meta_info' : _MetaInfoClass('CiscoAtmQosMib.Caqqueuingparamstable',
            False, 
            [
            _MetaInfoClassMember('caqQueuingParamsEntry', REFERENCE_LIST, 'Caqqueuingparamsentry' , 'ydk.models.cisco_ios_xe.CISCO_ATM_QOS_MIB', 'CiscoAtmQosMib.Caqqueuingparamstable.Caqqueuingparamsentry', 
                [], [], 
                '''                This is defined as an entry in caqQueuingParamsTable.
                ''',
                'caqqueuingparamsentry',
                'CISCO-ATM-QOS-MIB', False),
            ],
            'CISCO-ATM-QOS-MIB',
            'caqQueuingParamsTable',
            _yang_ns._namespaces['CISCO-ATM-QOS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ATM_QOS_MIB'
        ),
    },
    'CiscoAtmQosMib.Caqqueuingparamsclasstable.Caqqueuingparamsclassentry' : {
        'meta_info' : _MetaInfoClass('CiscoAtmQosMib.Caqqueuingparamsclasstable.Caqqueuingparamsclassentry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'CISCO-ATM-QOS-MIB', True),
            _MetaInfoClassMember('atmVclVpi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4095')], [], 
                '''                ''',
                'atmvclvpi',
                'CISCO-ATM-QOS-MIB', True),
            _MetaInfoClassMember('atmVclVci', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                ''',
                'atmvclvci',
                'CISCO-ATM-QOS-MIB', True),
            _MetaInfoClassMember('caqQueuingParamsClassIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '8')], [], 
                '''                A class index, which associates with an IP precedence
                (0 to 8), is defined to reference individual
                caqQueuingParamsClassEntry.
                ''',
                'caqqueuingparamsclassindex',
                'CISCO-ATM-QOS-MIB', True),
            _MetaInfoClassMember('caqQueuingParamsClassMaxThre', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum Threshold value in kbps.
                ''',
                'caqqueuingparamsclassmaxthre',
                'CISCO-ATM-QOS-MIB', False),
            _MetaInfoClassMember('caqQueuingParamsClassMinThre', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Minimum Threshold value in kbps.
                ''',
                'caqqueuingparamsclassminthre',
                'CISCO-ATM-QOS-MIB', False),
            _MetaInfoClassMember('caqQueuingParamsClassMrkProb', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Mark probability denominator.  This is the value used
                in the calculation of a packet being dropped when
                the average queue size is between the minimum
                threshold and the maximum threshold.
                ''',
                'caqqueuingparamsclassmrkprob',
                'CISCO-ATM-QOS-MIB', False),
            _MetaInfoClassMember('caqQueuingParamsClassRandDrp', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of packets dropped when Mean Queue
                Length is between Minimum Threshold and
                Maximum Threshold range.
                ''',
                'caqqueuingparamsclassranddrp',
                'CISCO-ATM-QOS-MIB', False),
            _MetaInfoClassMember('caqQueuingParamsClassTailDrp', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of packets dropped because the Mean
                Queue Depth exceeds the Maximum Threshold value.
                ''',
                'caqqueuingparamsclasstaildrp',
                'CISCO-ATM-QOS-MIB', False),
            ],
            'CISCO-ATM-QOS-MIB',
            'caqQueuingParamsClassEntry',
            _yang_ns._namespaces['CISCO-ATM-QOS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ATM_QOS_MIB'
        ),
    },
    'CiscoAtmQosMib.Caqqueuingparamsclasstable' : {
        'meta_info' : _MetaInfoClass('CiscoAtmQosMib.Caqqueuingparamsclasstable',
            False, 
            [
            _MetaInfoClassMember('caqQueuingParamsClassEntry', REFERENCE_LIST, 'Caqqueuingparamsclassentry' , 'ydk.models.cisco_ios_xe.CISCO_ATM_QOS_MIB', 'CiscoAtmQosMib.Caqqueuingparamsclasstable.Caqqueuingparamsclassentry', 
                [], [], 
                '''                This is defined as an entry in ciscoAtmQosVcQueuingClassTable
                to provide queuing information of a specific class.
                ''',
                'caqqueuingparamsclassentry',
                'CISCO-ATM-QOS-MIB', False),
            ],
            'CISCO-ATM-QOS-MIB',
            'caqQueuingParamsClassTable',
            _yang_ns._namespaces['CISCO-ATM-QOS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ATM_QOS_MIB'
        ),
    },
    'CiscoAtmQosMib' : {
        'meta_info' : _MetaInfoClass('CiscoAtmQosMib',
            False, 
            [
            _MetaInfoClassMember('caqQueuingParamsClassTable', REFERENCE_CLASS, 'Caqqueuingparamsclasstable' , 'ydk.models.cisco_ios_xe.CISCO_ATM_QOS_MIB', 'CiscoAtmQosMib.Caqqueuingparamsclasstable', 
                [], [], 
                '''                This table provides queuing information for all 
                queuing classes associating with a VC.
                ''',
                'caqqueuingparamsclasstable',
                'CISCO-ATM-QOS-MIB', False),
            _MetaInfoClassMember('caqQueuingParamsTable', REFERENCE_CLASS, 'Caqqueuingparamstable' , 'ydk.models.cisco_ios_xe.CISCO_ATM_QOS_MIB', 'CiscoAtmQosMib.Caqqueuingparamstable', 
                [], [], 
                '''                This table provides queuing related information
                for a VC existing on an ATM interface.
                ''',
                'caqqueuingparamstable',
                'CISCO-ATM-QOS-MIB', False),
            _MetaInfoClassMember('caqVccParamsTable', REFERENCE_CLASS, 'Caqvccparamstable' , 'ydk.models.cisco_ios_xe.CISCO_ATM_QOS_MIB', 'CiscoAtmQosMib.Caqvccparamstable', 
                [], [], 
                '''                This table is defined to provide QoS information for
                each active ATM VC existing on the interface.
                ''',
                'caqvccparamstable',
                'CISCO-ATM-QOS-MIB', False),
            _MetaInfoClassMember('caqVpcParamsTable', REFERENCE_CLASS, 'Caqvpcparamstable' , 'ydk.models.cisco_ios_xe.CISCO_ATM_QOS_MIB', 'CiscoAtmQosMib.Caqvpcparamstable', 
                [], [], 
                '''                This table is defined to provide QoS information for
                each active ATM VP existing on the interface.
                ''',
                'caqvpcparamstable',
                'CISCO-ATM-QOS-MIB', False),
            ],
            'CISCO-ATM-QOS-MIB',
            'CISCO-ATM-QOS-MIB',
            _yang_ns._namespaces['CISCO-ATM-QOS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ATM_QOS_MIB'
        ),
    },
}
_meta_table['CiscoAtmQosMib.Caqvccparamstable.Caqvccparamsentry']['meta_info'].parent =_meta_table['CiscoAtmQosMib.Caqvccparamstable']['meta_info']
_meta_table['CiscoAtmQosMib.Caqvpcparamstable.Caqvpcparamsentry']['meta_info'].parent =_meta_table['CiscoAtmQosMib.Caqvpcparamstable']['meta_info']
_meta_table['CiscoAtmQosMib.Caqqueuingparamstable.Caqqueuingparamsentry']['meta_info'].parent =_meta_table['CiscoAtmQosMib.Caqqueuingparamstable']['meta_info']
_meta_table['CiscoAtmQosMib.Caqqueuingparamsclasstable.Caqqueuingparamsclassentry']['meta_info'].parent =_meta_table['CiscoAtmQosMib.Caqqueuingparamsclasstable']['meta_info']
_meta_table['CiscoAtmQosMib.Caqvccparamstable']['meta_info'].parent =_meta_table['CiscoAtmQosMib']['meta_info']
_meta_table['CiscoAtmQosMib.Caqvpcparamstable']['meta_info'].parent =_meta_table['CiscoAtmQosMib']['meta_info']
_meta_table['CiscoAtmQosMib.Caqqueuingparamstable']['meta_info'].parent =_meta_table['CiscoAtmQosMib']['meta_info']
_meta_table['CiscoAtmQosMib.Caqqueuingparamsclasstable']['meta_info'].parent =_meta_table['CiscoAtmQosMib']['meta_info']
