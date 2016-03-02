


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'ATMMIB.Aal5VccTable.Aal5VccEntry' : {
        'meta_info' : _MetaInfoClass('ATMMIB.Aal5VccTable.Aal5VccEntry',
            False, 
            [
            _MetaInfoClassMember('aal5VccVci', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                The VCI value of the AAL5 VCC at the
                interface identified by the ifIndex.
                ''',
                'aal5vccvci',
                'ATM-MIB', True),
            _MetaInfoClassMember('aal5VccVpi', ATTRIBUTE, 'int' , None, None, 
                [(0, 4095)], [], 
                '''                The VPI value of the AAL5 VCC at the
                interface identified by the ifIndex.
                ''',
                'aal5vccvpi',
                'ATM-MIB', True),
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'ifindex',
                'ATM-MIB', True),
            _MetaInfoClassMember('aal5VccCrcErrors', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of AAL5 CPCS PDUs received with
                CRC-32 errors on this AAL5 VCC at the
                interface associated with an AAL5 entity.
                ''',
                'aal5vcccrcerrors',
                'ATM-MIB', False),
            _MetaInfoClassMember('aal5VccOverSizedSDUs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of AAL5 CPCS PDUs discarded
                on this AAL5 VCC at the interface
                associated with an AAL5 entity because the
                AAL5 SDUs were too large.
                ''',
                'aal5vccoversizedsdus',
                'ATM-MIB', False),
            _MetaInfoClassMember('aal5VccSarTimeOuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of partially re-assembled AAL5
                CPCS PDUs which were discarded
                on this AAL5 VCC at the interface associated
                with an AAL5 entity because they
                were not fully re-assembled within the
                required time period.  If the re-assembly
                timer is not supported, then this object
                contains a zero value.
                ''',
                'aal5vccsartimeouts',
                'ATM-MIB', False),
            _MetaInfoClassMember('cAal5VccExtCompEnabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Boolean, if compression enabled for VCC.
                ''',
                'caal5vccextcompenabled',
                'CISCO-ATM-EXT-MIB', False),
            _MetaInfoClassMember('cAal5VccExtInF5OamCells', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of OAM F5 end to end loopback cells 
                received through the VCC.
                ''',
                'caal5vccextinf5oamcells',
                'CISCO-ATM-EXT-MIB', False),
            _MetaInfoClassMember('cAal5VccExtOutF5OamCells', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of OAM F5 end to end loopback cells sent 
                through the VCC.
                ''',
                'caal5vccextoutf5oamcells',
                'CISCO-ATM-EXT-MIB', False),
            _MetaInfoClassMember('cAal5VccExtVoice', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Boolean, TRUE if VCC is used to carry voice.
                ''',
                'caal5vccextvoice',
                'CISCO-ATM-EXT-MIB', False),
            _MetaInfoClassMember('cAal5VccHCInOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                This is 64bit (High Capacity) version of cAal5VccInOctets 
                counters.
                ''',
                'caal5vcchcinoctets',
                'CISCO-AAL5-MIB', False),
            _MetaInfoClassMember('cAal5VccHCInPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                This is 64bit (High Capacity) version of cAal5VccInPkts 
                counters.
                ''',
                'caal5vcchcinpkts',
                'CISCO-AAL5-MIB', False),
            _MetaInfoClassMember('cAal5VccHCOutOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                This is 64bit (High Capacity) version of cAal5VccOutOctets 
                counters.
                ''',
                'caal5vcchcoutoctets',
                'CISCO-AAL5-MIB', False),
            _MetaInfoClassMember('cAal5VccHCOutPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                This is 64bit (High Capacity) version of cAal5VccOutPkts 
                counters.
                ''',
                'caal5vcchcoutpkts',
                'CISCO-AAL5-MIB', False),
            _MetaInfoClassMember('cAal5VccInDroppedOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of AAL5 CPCS PDU Octets dropped at the 
                receive side of this AAL5 VCC at the interface 
                associated with an AAL5 entity.
                ''',
                'caal5vccindroppedoctets',
                'CISCO-AAL5-MIB', False),
            _MetaInfoClassMember('cAal5VccInDroppedPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of AAL5 CPCS PDUs dropped at the 
                receive side of this AAL5 VCC at the interface 
                associated with an AAL5 entity.
                ''',
                'caal5vccindroppedpkts',
                'CISCO-AAL5-MIB', False),
            _MetaInfoClassMember('cAal5VccInOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of AAL5 CPCS PDU octets received on this AAL5 VCC
                at the interface associated with an AAL5 entity.
                ''',
                'caal5vccinoctets',
                'CISCO-AAL5-MIB', False),
            _MetaInfoClassMember('cAal5VccInPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of AAL5 CPCS PDUs received on this AAL5 VCC at the
                interface associated with an AAL5 entity.
                ''',
                'caal5vccinpkts',
                'CISCO-AAL5-MIB', False),
            _MetaInfoClassMember('cAal5VccOutDroppedOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of AAL5 CPCS PDU Octets dropped at the 
                transmit side of this AAL5 VCC at the interface 
                associated with an AAL5 entity.
                ''',
                'caal5vccoutdroppedoctets',
                'CISCO-AAL5-MIB', False),
            _MetaInfoClassMember('cAal5VccOutDroppedPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of AAL5 CPCS PDUs dropped at the transmit side 
                of this AAL5 VCC at the interface associated with an 
                AAL5 entity.
                ''',
                'caal5vccoutdroppedpkts',
                'CISCO-AAL5-MIB', False),
            _MetaInfoClassMember('cAal5VccOutOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of AAL5 CPCS PDU octets transmitted on this AAL5 
                VCC at the interface associated with an AAL5 entity.
                ''',
                'caal5vccoutoctets',
                'CISCO-AAL5-MIB', False),
            _MetaInfoClassMember('cAal5VccOutPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of AAL5 CPCS PDUs transmitted on this AAL5 VCC at
                the interface associated with an AAL5 entity.
                ''',
                'caal5vccoutpkts',
                'CISCO-AAL5-MIB', False),
            ],
            'ATM-MIB',
            'aal5VccEntry',
            _yang_ns._namespaces['ATM-MIB'],
        'ydk.models.atm.ATM_MIB'
        ),
    },
    'ATMMIB.Aal5VccTable' : {
        'meta_info' : _MetaInfoClass('ATMMIB.Aal5VccTable',
            False, 
            [
            _MetaInfoClassMember('aal5VccEntry', REFERENCE_LIST, 'Aal5VccEntry' , 'ydk.models.atm.ATM_MIB', 'ATMMIB.Aal5VccTable.Aal5VccEntry', 
                [], [], 
                '''                This list contains the AAL5 VCC
                performance parameters and is indexed
                by ifIndex values of AAL5 interfaces
                and the associated VPI/VCI values.
                ''',
                'aal5vccentry',
                'ATM-MIB', False),
            ],
            'ATM-MIB',
            'aal5VccTable',
            _yang_ns._namespaces['ATM-MIB'],
        'ydk.models.atm.ATM_MIB'
        ),
    },
    'ATMMIB.AtmInterfaceConfTable.AtmInterfaceConfEntry.AtmInterfaceAddressType_Enum' : _MetaInfoEnum('AtmInterfaceAddressType_Enum', 'ydk.models.atm.ATM_MIB',
        {
            'private':'PRIVATE',
            'nsapE164':'NSAPE164',
            'nativeE164':'NATIVEE164',
            'other':'OTHER',
        }, 'ATM-MIB', _yang_ns._namespaces['ATM-MIB']),
    'ATMMIB.AtmInterfaceConfTable.AtmInterfaceConfEntry' : {
        'meta_info' : _MetaInfoClass('ATMMIB.AtmInterfaceConfTable.AtmInterfaceConfEntry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'ifindex',
                'ATM-MIB', True),
            _MetaInfoClassMember('atmInterfaceAddressType', REFERENCE_ENUM_CLASS, 'AtmInterfaceAddressType_Enum' , 'ydk.models.atm.ATM_MIB', 'ATMMIB.AtmInterfaceConfTable.AtmInterfaceConfEntry.AtmInterfaceAddressType_Enum', 
                [], [], 
                '''                The type of primary ATM address configured
                for use at this ATM interface.
                ''',
                'atminterfaceaddresstype',
                'ATM-MIB', False),
            _MetaInfoClassMember('atmInterfaceAdminAddress', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The primary address assigned for administrative purposes,
                for example, an address associated with the
                service provider side of a public network UNI
                (thus, the value of this address corresponds
                with the value of ifPhysAddress at the host side).
                If this interface has no assigned administrative
                address, or when the address used for
                administrative purposes is the same as that used
                for ifPhysAddress, then this is an octet string of
                zero length.
                ''',
                'atminterfaceadminaddress',
                'ATM-MIB', False),
            _MetaInfoClassMember('atmInterfaceConfVccs', ATTRIBUTE, 'int' , None, None, 
                [(0, 65536)], [], 
                '''                The number of VCCs (PVCC, Soft PVCC and SVCC)
                currently in use at this ATM interface.  It includes
                the number of PVCCs and Soft PVCCs that are configured
                at the interface, plus the number of SVCCs
                that are currently  established at the
                interface.
                ''',
                'atminterfaceconfvccs',
                'ATM-MIB', False),
            _MetaInfoClassMember('atmInterfaceConfVpcs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4096)], [], 
                '''                The number of VPCs (PVPC, Soft PVPC and SVPC)
                currently in use at this ATM interface.  It includes
                the number of PVPCs and Soft PVPCs that are configured
                at the interface, plus the number of SVPCs
                that are currently  established at the
                interface.
                
                At the ATM UNI, the configured number of
                VPCs (PVPCs and SVPCs) can range from
                0 to 256 only.
                ''',
                'atminterfaceconfvpcs',
                'ATM-MIB', False),
            _MetaInfoClassMember('atmInterfaceCurrentMaxVciBits', ATTRIBUTE, 'int' , None, None, 
                [(0, 16)], [], 
                '''                The maximum number of VCI Bits that may
                currently be used at this ATM interface.
                The value is the minimum of
                atmInterfaceMaxActiveVciBits, and the
                atmInterfaceMaxActiveVciBits of the interface's
                UNI/NNI peer.
                
                If the interface does not negotiate with
                its peer to determine the number of VCI Bits
                that can be used on the interface, then the
                value of this object must equal
                atmInterfaceMaxActiveVciBits.
                ''',
                'atminterfacecurrentmaxvcibits',
                'ATM-MIB', False),
            _MetaInfoClassMember('atmInterfaceCurrentMaxVpiBits', ATTRIBUTE, 'int' , None, None, 
                [(0, 12)], [], 
                '''                The maximum number of VPI Bits that may
                currently be used at this ATM interface.
                The value is the minimum of
                atmInterfaceMaxActiveVpiBits, and the
                atmInterfaceMaxActiveVpiBits of the interface's
                UNI/NNI peer.
                
                If the interface does not negotiate with
                its peer to determine the number of VPI Bits
                that can be used on the interface, then the
                value of this object must equal
                atmInterfaceMaxActiveVpiBits.
                ''',
                'atminterfacecurrentmaxvpibits',
                'ATM-MIB', False),
            _MetaInfoClassMember('atmInterfaceIlmiVci', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                The VCI value of the VCC supporting
                the ILMI at this ATM interface.  If the values of
                atmInterfaceIlmiVpi and atmInterfaceIlmiVci are
                both equal to zero then the ILMI is not
                supported at this ATM interface.
                ''',
                'atminterfaceilmivci',
                'ATM-MIB', False),
            _MetaInfoClassMember('atmInterfaceIlmiVpi', ATTRIBUTE, 'int' , None, None, 
                [(0, 4095)], [], 
                '''                The VPI value of the VCC supporting
                the ILMI at this ATM interface.  If the values of
                atmInterfaceIlmiVpi and atmInterfaceIlmiVci are
                both equal to zero then the ILMI is not
                supported at this ATM interface.
                ''',
                'atminterfaceilmivpi',
                'ATM-MIB', False),
            _MetaInfoClassMember('atmInterfaceMaxActiveVciBits', ATTRIBUTE, 'int' , None, None, 
                [(0, 16)], [], 
                '''                The maximum number of active VCI bits
                configured for use at this ATM interface.
                ''',
                'atminterfacemaxactivevcibits',
                'ATM-MIB', False),
            _MetaInfoClassMember('atmInterfaceMaxActiveVpiBits', ATTRIBUTE, 'int' , None, None, 
                [(0, 12)], [], 
                '''                The  maximum number of active VPI bits
                configured for use at the ATM interface.
                At the ATM UNI, the maximum number of active
                VPI bits configured for use ranges from
                0 to 8 only.
                ''',
                'atminterfacemaxactivevpibits',
                'ATM-MIB', False),
            _MetaInfoClassMember('atmInterfaceMaxVccs', ATTRIBUTE, 'int' , None, None, 
                [(0, 65536)], [], 
                '''                The maximum number of VCCs (PVCCs and SVCCs)
                supported at this ATM interface.
                ''',
                'atminterfacemaxvccs',
                'ATM-MIB', False),
            _MetaInfoClassMember('atmInterfaceMaxVpcs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4096)], [], 
                '''                The maximum number of VPCs (PVPCs and SVPCs)
                supported at this ATM interface. At the ATM UNI,
                the maximum number of VPCs (PVPCs and SVPCs)
                ranges from 0 to 256 only.
                ''',
                'atminterfacemaxvpcs',
                'ATM-MIB', False),
            _MetaInfoClassMember('atmInterfaceMyNeighborIfName', ATTRIBUTE, 'str' , None, None, 
                [], ['\\p{IsBasicLatin}{0,255}'], 
                '''                The textual name of the interface on the neighbor
                system on the far end of this interface, and to
                which this interface connects.  If the neighbor
                system is manageable through SNMP and supports
                the object ifName, the value of this object must
                be identical with that of ifName for the ifEntry
                of the lowest level physical interface
                for this port.  If this interface does not have a
                textual name, the value of this object is a zero
                length string.  Note that the value of this object
                may be obtained in different ways, e.g., by manual
                configuration, or through ILMI interaction with
                the neighbor system.
                ''',
                'atminterfacemyneighborifname',
                'ATM-MIB', False),
            _MetaInfoClassMember('atmInterfaceMyNeighborIpAddress', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The IP address of the neighbor system connected to
                the  far end of this interface, to which a Network
                Management Station can send SNMP messages, as IP
                datagrams sent to UDP port 161, in order to access
                network management information concerning the
                operation of that system.  Note that the value
                of this object may be obtained in different ways,
                e.g., by manual configuration, or through ILMI
                interaction with the neighbor system.
                ''',
                'atminterfacemyneighboripaddress',
                'ATM-MIB', False),
            _MetaInfoClassMember('atmInterfaceSubscrAddress', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The identifier assigned by a service provider
                to the network side of a public network UNI.
                If this interface has no assigned service provider
                address, or for other interfaces this is an octet string
                of zero length.
                ''',
                'atminterfacesubscraddress',
                'ATM-MIB', False),
            _MetaInfoClassMember('atmIntfCurrentlyDownToUpPVcls', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The current number PVCLs on this interface which 
                changed state to 'up' since the last 
                atmIntPvcUpTrap was sent.
                ''',
                'atmintfcurrentlydowntouppvcls',
                'CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN', False),
            _MetaInfoClassMember('atmIntfCurrentlyFailingPVcls', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The current number of VCLs on this interface for which
                there is an active row in the atmVclTable having an
                atmVclConnKind value of `pvc' and an atmVclOperStatus
                with a value other than `up'.
                ''',
                'atmintfcurrentlyfailingpvcls',
                'CISCO-IETF-ATM2-PVCTRAP-MIB', False),
            _MetaInfoClassMember('atmIntfCurrentlyOAMFailingPVcls', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The current number of PVCLs on this interface for which the
                oam loop back has failed but the status of each PVCL remain 
                in the 'up' state in the last notification interval.
                ''',
                'atmintfcurrentlyoamfailingpvcls',
                'CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN', False),
            _MetaInfoClassMember('atmIntfOAMFailedPVcls', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of PVCLs in this interface which 
                are currently in the oam loopback failed condition but 
                the status of each PVCL remain in the 'up' state.
                ''',
                'atmintfoamfailedpvcls',
                'CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN', False),
            _MetaInfoClassMember('atmIntfPvcFailures', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of times the operational status of a PVCL
                on this interface has gone down.
                ''',
                'atmintfpvcfailures',
                'CISCO-IETF-ATM2-PVCTRAP-MIB', False),
            _MetaInfoClassMember('atmIntfPvcFailuresTrapEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Allows the generation of traps in response to PVCL
                failures on this interface.
                ''',
                'atmintfpvcfailurestrapenable',
                'CISCO-IETF-ATM2-PVCTRAP-MIB', False),
            _MetaInfoClassMember('atmIntfPvcNotificationInterval', ATTRIBUTE, 'int' , None, None, 
                [(1, 3600)], [], 
                '''                The minimum interval between the sending of
                cIntfPvcFailuresTrap notifications for this
                interface.
                ''',
                'atmintfpvcnotificationinterval',
                'CISCO-IETF-ATM2-PVCTRAP-MIB', False),
            _MetaInfoClassMember('atmPreviouslyFailedPVclInterval', ATTRIBUTE, 'int' , None, None, 
                [(0, 3600)], [], 
                '''                The interval for storing the failed
                time in atmPreviouslyFailedPVclTimeStamp
                ''',
                'atmpreviouslyfailedpvclinterval',
                'CISCO-IETF-ATM2-PVCTRAP-MIB', False),
            _MetaInfoClassMember('catmIntfAISRDIOAMFailedPVcls', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of PVCLs in this interface which 
                are currently in the AIS RDI OAM failed condition but 
                the status of each PVCL remain in the 'up' state.
                ''',
                'catmintfaisrdioamfailedpvcls',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmIntfAISRDIOAMRcovedPVcls', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of PVCLs in this interface which 
                are currently in the AIS RDI OAM recovered condition and 
                the status of each PVCL is in the 'up' state.
                ''',
                'catmintfaisrdioamrcovedpvcls',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmIntfAnyOAMFailedPVcls', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of PVCLs in this interface which 
                are currently in any type of OAM failed condition but 
                the status of each PVCL remain in the 'up' state.
                ''',
                'catmintfanyoamfailedpvcls',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmIntfAnyOAMRcovedPVcls', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of PVCLs in this interface which 
                are currently in any type of OAM recovered condition and 
                the status of each PVCL is in the 'up' state.
                ''',
                'catmintfanyoamrcovedpvcls',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmIntfCurAISRDIOAMFailingPVcls', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The current number of PVCLs on this interface for which the
                AIS RDI OAM has failed but the status of each PVCL remain 
                in the 'up' state in the last notification interval.
                ''',
                'catmintfcuraisrdioamfailingpvcls',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmIntfCurAISRDIOAMRcovingPVcls', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The current number of PVCLs on this interface for which the
                AIS RDI OAM has recovered and the status of each PVCL is 
                in the 'up' state in the last notification interval.
                ''',
                'catmintfcuraisrdioamrcovingpvcls',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmIntfCurAnyOAMFailingPVcls', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The current number of PVCLs on this interface for which 
                any of OAM has failed but the status of each PVCL remain 
                in the 'up' state in the last notification interval.
                ''',
                'catmintfcuranyoamfailingpvcls',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmIntfCurAnyOAMRcovingPVcls', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The current number of PVCLs on this interface for which 
                any of OAM has recovered and the status of each PVCL is 
                in the 'up' state in the last notification interval.
                ''',
                'catmintfcuranyoamrcovingpvcls',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmIntfCurEndCCOAMFailingPVcls', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The current number of PVCLs on this interface for which the
                End-to-End CC OAM has failed but the status of each PVCL 
                remain in the 'up' state in the last notification interval.
                ''',
                'catmintfcurendccoamfailingpvcls',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmIntfCurEndCCOAMRcovingPVcls', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The current number of PVCLs on this interface for which the
                End-to-End CC OAM has recovered and the status of each PVCL 
                is in the 'up' state in the last notification interval.
                ''',
                'catmintfcurendccoamrcovingpvcls',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmIntfCurrentlyDownToUpPVcls', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The current number PVCLs on this interface which 
                changed state to 'up' since the last 
                atmIntPvcUp2Trap was sent.
                ''',
                'catmintfcurrentlydowntouppvcls',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmIntfCurrentOAMFailingPVcls', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The current number of PVCLs on this interface for which the
                OAM loop back has failed but the status of each PVCL remain 
                in the 'up' state in the last notification interval.
                ''',
                'catmintfcurrentoamfailingpvcls',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmIntfCurrentOAMRcovingPVcls', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The current number of PVCLs on this interface for which the
                OAM loop back has recovered and the status of each PVCL is 
                in the 'up' state in the last notification interval.
                ''',
                'catmintfcurrentoamrcovingpvcls',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmIntfCurSegCCOAMFailingPVcls', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The current number of PVCLs on this interface for which the
                Segment CC OAM has failed but the status of each PVCL remain 
                in the 'up' state in the last notification interval.
                ''',
                'catmintfcursegccoamfailingpvcls',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmIntfCurSegCCOAMRcovingPVcls', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The current number of PVCLs on this interface for which the
                Segment CC OAM has recovered and the status of each PVCL is 
                in the 'up' state in the last notification interval.
                ''',
                'catmintfcursegccoamrcovingpvcls',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmIntfEndCCOAMFailedPVcls', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of PVCLs in this interface which 
                are currently in the End-to-End CC OAM failed condition 
                but the status of each PVCL remain in the 'up' state.
                ''',
                'catmintfendccoamfailedpvcls',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmIntfEndCCOAMRcovedPVcls', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of PVCLs in this interface which 
                are currently in the End-to-End CC OAM recovered condition 
                and the status of each PVCL is in the 'up' state.
                ''',
                'catmintfendccoamrcovedpvcls',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmIntfOAMFailedPVcls', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of PVCLs in this interface which 
                are currently in the OAM loopback failed condition but 
                the status of each PVCL remain in the 'up' state.
                ''',
                'catmintfoamfailedpvcls',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmIntfOAMRcovedPVcls', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of PVCLs in this interface which 
                are currently in the OAM loopback recovered condition and 
                the status of each PVCL is in the 'up' state.
                ''',
                'catmintfoamrcovedpvcls',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmIntfSegCCOAMFailedPVcls', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of PVCLs in this interface which 
                are currently in the Segment CC OAM failed condition 
                but the status of each PVCL remain in the 'up' state.
                ''',
                'catmintfsegccoamfailedpvcls',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmIntfSegCCOAMRcovedPVcls', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of PVCLs in this interface which 
                are currently in the Segment CC OAM recovered condition 
                and the status of each PVCL is in the 'up' state.
                ''',
                'catmintfsegccoamrcovedpvcls',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmIntfTypeOfOAMFailure', REFERENCE_ENUM_CLASS, 'CatmOAMFailureType_Enum' , 'ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB', 'CatmOAMFailureType_Enum', 
                [], [], 
                '''                Type of OAM failure.
                ''',
                'catmintftypeofoamfailure',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmIntfTypeOfOAMRecover', REFERENCE_ENUM_CLASS, 'CatmOAMRecoveryType_Enum' , 'ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB', 'CatmOAMRecoveryType_Enum', 
                [], [], 
                '''                Type of OAM Recovered
                ''',
                'catmintftypeofoamrecover',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            ],
            'ATM-MIB',
            'atmInterfaceConfEntry',
            _yang_ns._namespaces['ATM-MIB'],
        'ydk.models.atm.ATM_MIB'
        ),
    },
    'ATMMIB.AtmInterfaceConfTable' : {
        'meta_info' : _MetaInfoClass('ATMMIB.AtmInterfaceConfTable',
            False, 
            [
            _MetaInfoClassMember('atmInterfaceConfEntry', REFERENCE_LIST, 'AtmInterfaceConfEntry' , 'ydk.models.atm.ATM_MIB', 'ATMMIB.AtmInterfaceConfTable.AtmInterfaceConfEntry', 
                [], [], 
                '''                This list contains ATM interface configuration
                parameters and state variables and is indexed
                by ifIndex values of ATM interfaces.
                ''',
                'atminterfaceconfentry',
                'ATM-MIB', False),
            ],
            'ATM-MIB',
            'atmInterfaceConfTable',
            _yang_ns._namespaces['ATM-MIB'],
        'ydk.models.atm.ATM_MIB'
        ),
    },
    'ATMMIB.AtmInterfaceDs3PlcpTable.AtmInterfaceDs3PlcpEntry.AtmInterfaceDs3PlcpAlarmState_Enum' : _MetaInfoEnum('AtmInterfaceDs3PlcpAlarmState_Enum', 'ydk.models.atm.ATM_MIB',
        {
            'noAlarm':'NOALARM',
            'receivedFarEndAlarm':'RECEIVEDFARENDALARM',
            'incomingLOF':'INCOMINGLOF',
        }, 'ATM-MIB', _yang_ns._namespaces['ATM-MIB']),
    'ATMMIB.AtmInterfaceDs3PlcpTable.AtmInterfaceDs3PlcpEntry' : {
        'meta_info' : _MetaInfoClass('ATMMIB.AtmInterfaceDs3PlcpTable.AtmInterfaceDs3PlcpEntry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'ifindex',
                'ATM-MIB', True),
            _MetaInfoClassMember('atmInterfaceDs3PlcpAlarmState', REFERENCE_ENUM_CLASS, 'AtmInterfaceDs3PlcpAlarmState_Enum' , 'ydk.models.atm.ATM_MIB', 'ATMMIB.AtmInterfaceDs3PlcpTable.AtmInterfaceDs3PlcpEntry.AtmInterfaceDs3PlcpAlarmState_Enum', 
                [], [], 
                '''                This variable indicates if there is an
                alarm present for the DS3 PLCP.  The value
                receivedFarEndAlarm means that the DS3 PLCP
                has received an incoming Yellow
                Signal, the value incomingLOF means that
                the DS3 PLCP has declared a loss of frame (LOF)
                failure condition, and the value noAlarm
                means that there are no alarms present.
                Transition from the failure to the no alarm state
                occurs when no defects (e.g., LOF) are received
                for more than 10 seconds.
                ''',
                'atminterfaceds3plcpalarmstate',
                'ATM-MIB', False),
            _MetaInfoClassMember('atmInterfaceDs3PlcpSEFSs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of DS3 PLCP Severely Errored Framing
                Seconds (SEFS). Each SEFS represents a
                one-second interval which contains
                one or more SEF events.
                ''',
                'atminterfaceds3plcpsefss',
                'ATM-MIB', False),
            _MetaInfoClassMember('atmInterfaceDs3PlcpUASs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The counter associated with the number of
                Unavailable Seconds encountered by the PLCP.
                ''',
                'atminterfaceds3plcpuass',
                'ATM-MIB', False),
            ],
            'ATM-MIB',
            'atmInterfaceDs3PlcpEntry',
            _yang_ns._namespaces['ATM-MIB'],
        'ydk.models.atm.ATM_MIB'
        ),
    },
    'ATMMIB.AtmInterfaceDs3PlcpTable' : {
        'meta_info' : _MetaInfoClass('ATMMIB.AtmInterfaceDs3PlcpTable',
            False, 
            [
            _MetaInfoClassMember('atmInterfaceDs3PlcpEntry', REFERENCE_LIST, 'AtmInterfaceDs3PlcpEntry' , 'ydk.models.atm.ATM_MIB', 'ATMMIB.AtmInterfaceDs3PlcpTable.AtmInterfaceDs3PlcpEntry', 
                [], [], 
                '''                This list contains DS3 PLCP parameters and
                state variables at the ATM interface and is
                indexed by the ifIndex value of the ATM interface.
                ''',
                'atminterfaceds3plcpentry',
                'ATM-MIB', False),
            ],
            'ATM-MIB',
            'atmInterfaceDs3PlcpTable',
            _yang_ns._namespaces['ATM-MIB'],
        'ydk.models.atm.ATM_MIB'
        ),
    },
    'ATMMIB.AtmInterfaceTCTable.AtmInterfaceTCEntry.AtmInterfaceTCAlarmState_Enum' : _MetaInfoEnum('AtmInterfaceTCAlarmState_Enum', 'ydk.models.atm.ATM_MIB',
        {
            'noAlarm':'NOALARM',
            'lcdFailure':'LCDFAILURE',
        }, 'ATM-MIB', _yang_ns._namespaces['ATM-MIB']),
    'ATMMIB.AtmInterfaceTCTable.AtmInterfaceTCEntry' : {
        'meta_info' : _MetaInfoClass('ATMMIB.AtmInterfaceTCTable.AtmInterfaceTCEntry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'ifindex',
                'ATM-MIB', True),
            _MetaInfoClassMember('atmInterfaceOCDEvents', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of times the Out of Cell
                Delineation (OCD) events occur.  If seven
                consecutive ATM cells have Header Error
                Control (HEC) violations, an OCD event occurs.
                A high number of OCD events may indicate a
                problem with the TC Sublayer.
                ''',
                'atminterfaceocdevents',
                'ATM-MIB', False),
            _MetaInfoClassMember('atmInterfaceTCAlarmState', REFERENCE_ENUM_CLASS, 'AtmInterfaceTCAlarmState_Enum' , 'ydk.models.atm.ATM_MIB', 'ATMMIB.AtmInterfaceTCTable.AtmInterfaceTCEntry.AtmInterfaceTCAlarmState_Enum', 
                [], [], 
                '''                This variable indicates if there is an
                alarm present for the TC Sublayer.  The value
                lcdFailure(2) indicates that the TC Sublayer
                is currently in the Loss of Cell Delineation
                (LCD) defect maintenance state.  The value
                noAlarm(1) indicates that the TC Sublayer
                is currently not in the LCD defect
                maintenance state.
                ''',
                'atminterfacetcalarmstate',
                'ATM-MIB', False),
            ],
            'ATM-MIB',
            'atmInterfaceTCEntry',
            _yang_ns._namespaces['ATM-MIB'],
        'ydk.models.atm.ATM_MIB'
        ),
    },
    'ATMMIB.AtmInterfaceTCTable' : {
        'meta_info' : _MetaInfoClass('ATMMIB.AtmInterfaceTCTable',
            False, 
            [
            _MetaInfoClassMember('atmInterfaceTCEntry', REFERENCE_LIST, 'AtmInterfaceTCEntry' , 'ydk.models.atm.ATM_MIB', 'ATMMIB.AtmInterfaceTCTable.AtmInterfaceTCEntry', 
                [], [], 
                '''                This list contains TC Sublayer parameters
                and state variables at the ATM interface and is
                indexed by the ifIndex value of the ATM interface.
                ''',
                'atminterfacetcentry',
                'ATM-MIB', False),
            ],
            'ATM-MIB',
            'atmInterfaceTCTable',
            _yang_ns._namespaces['ATM-MIB'],
        'ydk.models.atm.ATM_MIB'
        ),
    },
    'ATMMIB.AtmMIBObjects' : {
        'meta_info' : _MetaInfoClass('ATMMIB.AtmMIBObjects',
            False, 
            [
            _MetaInfoClassMember('atmTrafficDescrParamIndexNext', ATTRIBUTE, 'int' , None, None, 
                [(0, 2147483647)], [], 
                '''                This object contains an appropriate value to
                be used for atmTrafficDescrParamIndex when
                creating entries in the
                atmTrafficDescrParamTable.
                The value 0 indicates that no unassigned
                entries are available. To obtain the
                atmTrafficDescrParamIndex value for a new
                entry, the manager issues a management
                protocol retrieval operation to obtain the
                current value of this object.  After each
                retrieval, the agent should modify the value
                to the next unassigned index.
                After a manager retrieves a value the agent will
                determine through its local policy when this index
                value will be made available for reuse.
                ''',
                'atmtrafficdescrparamindexnext',
                'ATM-MIB', False),
            _MetaInfoClassMember('atmVcCrossConnectIndexNext', ATTRIBUTE, 'int' , None, None, 
                [(0, 2147483647)], [], 
                '''                This object contains an appropriate value to
                be used for atmVcCrossConnectIndex when creating
                entries in the atmVcCrossConnectTable.  The value
                0 indicates that no unassigned entries are
                available. To obtain the atmVcCrossConnectIndex
                value for a new entry, the manager issues a
                management protocol retrieval operation to obtain
                the current value of this object.  After each
                retrieval, the agent should modify the value to
                the next unassigned index.
                After a manager retrieves a value the agent will
                determine through its local policy when this index
                value will be made available for reuse.
                ''',
                'atmvccrossconnectindexnext',
                'ATM-MIB', False),
            _MetaInfoClassMember('atmVpCrossConnectIndexNext', ATTRIBUTE, 'int' , None, None, 
                [(0, 2147483647)], [], 
                '''                This object contains an appropriate value to
                be used for atmVpCrossConnectIndex when creating
                entries in the atmVpCrossConnectTable.  The value
                0 indicates that no unassigned entries are
                available. To obtain the atmVpCrossConnectIndex
                value for a new entry, the manager issues a
                management protocol retrieval operation to obtain
                the current value of this object.  After each
                retrieval, the agent should modify the value to
                the next unassigned index.
                After a manager retrieves a value the agent will
                determine through its local policy when this index
                value will be made available for reuse.
                ''',
                'atmvpcrossconnectindexnext',
                'ATM-MIB', False),
            ],
            'ATM-MIB',
            'atmMIBObjects',
            _yang_ns._namespaces['ATM-MIB'],
        'ydk.models.atm.ATM_MIB'
        ),
    },
    'ATMMIB.AtmTrafficDescrParamTable.AtmTrafficDescrParamEntry' : {
        'meta_info' : _MetaInfoClass('ATMMIB.AtmTrafficDescrParamTable.AtmTrafficDescrParamEntry',
            False, 
            [
            _MetaInfoClassMember('atmTrafficDescrParamIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                This object is used by the virtual link
                table (i.e., VPL or VCL table)
                to identify the row of this table.
                When creating a new row in the table
                the value of this index may be obtained
                by retrieving the value of
                atmTrafficDescrParamIndexNext.
                ''',
                'atmtrafficdescrparamindex',
                'ATM-MIB', True),
            _MetaInfoClassMember('atmServiceCategory', REFERENCE_ENUM_CLASS, 'AtmServiceCategory_Enum' , 'ydk.models.atm.ATM_TC_MIB', 'AtmServiceCategory_Enum', 
                [], [], 
                '''                The ATM service category.
                ''',
                'atmservicecategory',
                'ATM-MIB', False),
            _MetaInfoClassMember('atmTrafficDescrParam1', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                The first parameter of the ATM traffic descriptor
                used according to the value of
                atmTrafficDescrType.
                ''',
                'atmtrafficdescrparam1',
                'ATM-MIB', False),
            _MetaInfoClassMember('atmTrafficDescrParam2', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                The second parameter of the ATM traffic descriptor
                used according to the value of
                atmTrafficDescrType.
                ''',
                'atmtrafficdescrparam2',
                'ATM-MIB', False),
            _MetaInfoClassMember('atmTrafficDescrParam3', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                The third parameter of the ATM traffic descriptor
                used according to the value of
                atmTrafficDescrType.
                ''',
                'atmtrafficdescrparam3',
                'ATM-MIB', False),
            _MetaInfoClassMember('atmTrafficDescrParam4', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                The fourth parameter of the ATM traffic descriptor
                used according to the value of
                atmTrafficDescrType.
                ''',
                'atmtrafficdescrparam4',
                'ATM-MIB', False),
            _MetaInfoClassMember('atmTrafficDescrParam5', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                The fifth parameter of the ATM traffic descriptor
                used according to the value of
                atmTrafficDescrType.
                ''',
                'atmtrafficdescrparam5',
                'ATM-MIB', False),
            _MetaInfoClassMember('atmTrafficDescrRowStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                This object is used to create
                a new row or modify or delete an
                existing row in this table.
                ''',
                'atmtrafficdescrrowstatus',
                'ATM-MIB', False),
            _MetaInfoClassMember('atmTrafficDescrType', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                The value of this object identifies the type
                of ATM traffic descriptor.
                The type may indicate no traffic descriptor or
                traffic descriptor with one or more parameters.
                These parameters are specified as a parameter
                vector, in the corresponding instances of the
                objects:
                    atmTrafficDescrParam1
                    atmTrafficDescrParam2
                    atmTrafficDescrParam3
                    atmTrafficDescrParam4
                    atmTrafficDescrParam5.
                ''',
                'atmtrafficdescrtype',
                'ATM-MIB', False),
            _MetaInfoClassMember('atmTrafficFrameDiscard', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If set to 'true', this object indicates that the network
                is requested to treat data for this connection, in the
                given direction, as frames (e.g. AAL5 CPCS_PDU's) rather
                than as individual cells.  While the precise
                implementation is network-specific, this treatment may
                for example involve discarding entire frames during
                congestion, rather than a few cells from many frames.
                ''',
                'atmtrafficframediscard',
                'ATM-MIB', False),
            _MetaInfoClassMember('atmTrafficQoSClass', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                The value of this object identifies the QoS Class.
                Four Service classes have been
                specified in the ATM Forum UNI Specification:
                Service Class A: Constant bit rate video and
                                 Circuit emulation
                Service Class B: Variable bit rate video/audio
                Service Class C: Connection-oriented data
                Service Class D: Connectionless data
                Four QoS classes numbered 1, 2, 3, and 4 have
                been specified with the aim to support service
                classes A, B, C, and D respectively.
                An unspecified QoS Class numbered `0' is used
                for best effort traffic.
                ''',
                'atmtrafficqosclass',
                'ATM-MIB', False),
            ],
            'ATM-MIB',
            'atmTrafficDescrParamEntry',
            _yang_ns._namespaces['ATM-MIB'],
        'ydk.models.atm.ATM_MIB'
        ),
    },
    'ATMMIB.AtmTrafficDescrParamTable' : {
        'meta_info' : _MetaInfoClass('ATMMIB.AtmTrafficDescrParamTable',
            False, 
            [
            _MetaInfoClassMember('atmTrafficDescrParamEntry', REFERENCE_LIST, 'AtmTrafficDescrParamEntry' , 'ydk.models.atm.ATM_MIB', 'ATMMIB.AtmTrafficDescrParamTable.AtmTrafficDescrParamEntry', 
                [], [], 
                '''                This list contains ATM traffic descriptor
                type and the associated parameters.
                ''',
                'atmtrafficdescrparamentry',
                'ATM-MIB', False),
            ],
            'ATM-MIB',
            'atmTrafficDescrParamTable',
            _yang_ns._namespaces['ATM-MIB'],
        'ydk.models.atm.ATM_MIB'
        ),
    },
    'ATMMIB.AtmVcCrossConnectTable.AtmVcCrossConnectEntry' : {
        'meta_info' : _MetaInfoClass('ATMMIB.AtmVcCrossConnectTable.AtmVcCrossConnectEntry',
            False, 
            [
            _MetaInfoClassMember('atmVcCrossConnectHighIfIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                The ifIndex value for the ATM interface for
                this VC cross-connect. The term high implies
                that this ATM interface has the numerically higher
                ifIndex value than the other ATM interface
                identified in the same atmVcCrossConnectEntry.
                ''',
                'atmvccrossconnecthighifindex',
                'ATM-MIB', True),
            _MetaInfoClassMember('atmVcCrossConnectHighVci', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                The VCI value at the ATM interface
                associated with the VC cross-connect that is
                identified by atmVcCrossConnectHighIfIndex.
                ''',
                'atmvccrossconnecthighvci',
                'ATM-MIB', True),
            _MetaInfoClassMember('atmVcCrossConnectHighVpi', ATTRIBUTE, 'int' , None, None, 
                [(0, 4095)], [], 
                '''                The VPI value at the ATM interface
                associated with the VC cross-connect that is
                identified by atmVcCrossConnectHighIfIndex.
                ''',
                'atmvccrossconnecthighvpi',
                'ATM-MIB', True),
            _MetaInfoClassMember('atmVcCrossConnectIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                A unique value to identify this VC cross-connect.
                For each VCL associated with this cross-connect,
                the agent reports this cross-connect index value
                in the atmVclCrossConnectIdentifier attribute of
                the corresponding atmVclTable entries.
                ''',
                'atmvccrossconnectindex',
                'ATM-MIB', True),
            _MetaInfoClassMember('atmVcCrossConnectLowIfIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                The ifIndex value of the ATM interface for this
                VC cross-connect. The term low implies
                that this ATM interface has the numerically lower
                ifIndex value than the other ATM interface
                identified in the same atmVcCrossConnectEntry.
                ''',
                'atmvccrossconnectlowifindex',
                'ATM-MIB', True),
            _MetaInfoClassMember('atmVcCrossConnectLowVci', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                The VCI value at the ATM interface
                associated with this VC cross-connect that is
                identified by atmVcCrossConnectLowIfIndex.
                ''',
                'atmvccrossconnectlowvci',
                'ATM-MIB', True),
            _MetaInfoClassMember('atmVcCrossConnectLowVpi', ATTRIBUTE, 'int' , None, None, 
                [(0, 4095)], [], 
                '''                The VPI value at the ATM interface
                associated with the VC cross-connect that is
                identified by atmVcCrossConnectLowIfIndex.
                ''',
                'atmvccrossconnectlowvpi',
                'ATM-MIB', True),
            _MetaInfoClassMember('atmVcCrossConnectAdminStatus', REFERENCE_ENUM_CLASS, 'AtmVorXAdminStatus_Enum' , 'ydk.models.atm.ATM_TC_MIB', 'AtmVorXAdminStatus_Enum', 
                [], [], 
                '''                The desired administrative status of this
                bi-directional VC cross-connect.
                ''',
                'atmvccrossconnectadminstatus',
                'ATM-MIB', False),
            _MetaInfoClassMember('atmVcCrossConnectH2LLastChange', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The value of sysUpTime at the time this
                VC cross-connect entered its current
                operational state in high to low direction.
                ''',
                'atmvccrossconnecth2llastchange',
                'ATM-MIB', False),
            _MetaInfoClassMember('atmVcCrossConnectH2LOperStatus', REFERENCE_ENUM_CLASS, 'AtmVorXOperStatus_Enum' , 'ydk.models.atm.ATM_TC_MIB', 'AtmVorXOperStatus_Enum', 
                [], [], 
                '''                The current operational status of the
                VC cross-connect in one direction; (i.e.,
                from the high to low direction).
                ''',
                'atmvccrossconnecth2loperstatus',
                'ATM-MIB', False),
            _MetaInfoClassMember('atmVcCrossConnectL2HLastChange', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The value of sysUpTime at the time this
                VC cross-connect entered its current
                operational state in low to high direction.
                ''',
                'atmvccrossconnectl2hlastchange',
                'ATM-MIB', False),
            _MetaInfoClassMember('atmVcCrossConnectL2HOperStatus', REFERENCE_ENUM_CLASS, 'AtmVorXOperStatus_Enum' , 'ydk.models.atm.ATM_TC_MIB', 'AtmVorXOperStatus_Enum', 
                [], [], 
                '''                The current operational status of the
                VC cross-connect in one direction; (i.e.,
                from the low to high direction).
                ''',
                'atmvccrossconnectl2hoperstatus',
                'ATM-MIB', False),
            _MetaInfoClassMember('atmVcCrossConnectRowStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                The status of this entry in the
                atmVcCrossConnectTable.  This object is used to
                create a new cross-connect for cross-connecting
                VCLs which are created using the atmVclTable
                or to change or delete existing cross-connect.
                This object must be initially set to
                `createAndWait' or 'createAndGo'.
                To turn on a VC cross-connect,
                the atmVcCrossConnectAdminStatus
                is set to `up'.
                ''',
                'atmvccrossconnectrowstatus',
                'ATM-MIB', False),
            ],
            'ATM-MIB',
            'atmVcCrossConnectEntry',
            _yang_ns._namespaces['ATM-MIB'],
        'ydk.models.atm.ATM_MIB'
        ),
    },
    'ATMMIB.AtmVcCrossConnectTable' : {
        'meta_info' : _MetaInfoClass('ATMMIB.AtmVcCrossConnectTable',
            False, 
            [
            _MetaInfoClassMember('atmVcCrossConnectEntry', REFERENCE_LIST, 'AtmVcCrossConnectEntry' , 'ydk.models.atm.ATM_MIB', 'ATMMIB.AtmVcCrossConnectTable.AtmVcCrossConnectEntry', 
                [], [], 
                '''                An entry in the ATM VC Cross Connect table.
                This entry is used to model a bi-directional ATM
                VC cross-connect cross-connecting two end points.
                
                Step-wise Procedures to set up a VC Cross-connect
                
                Once the entries in the atmVclTable are created,
                the following procedures are used
                to cross-connect the VCLs together to
                form a VCC segment.
                
                (1) The manager obtains a unique
                   atmVcCrossConnectIndex by reading the
                   atmVcCrossConnectIndexNext object.
                
                (2) Next, the manager creates a set of one
                   or more rows in the ATM VC Cross Connect
                   Table, one for each cross-connection between
                   two VCLs.  Each row is indexed by the ATM
                   interface port numbers and VPI/VCI values of
                   the two ends of that cross-connection.
                   This set of rows specifies the topology of the
                   VCC cross-connect and is identified by a single
                   value of atmVcCrossConnectIndex.
                
                Negotiated VC Cross-Connect Establishment
                
                (2a) The manager creates a row in this table by
                   setting atmVcCrossConnectRowStatus to
                   createAndWait(5).  The agent checks the
                   requested topology and the mutual sanity of
                   the ATM traffic parameters and
                   service categories, i.e., the row creation
                   fails if:
                   - the requested topology is incompatible with
                     associated values of atmVclCastType,
                   - the requested topology is not supported
                     by the agent,
                   - the traffic/service category parameter values
                     associated with the requested row are
                     incompatible with those of already existing
                     rows for this VC cross-connect.
                   [For example, for setting up
                   a point-to-point VC cross-connect, the
                   ATM traffic parameters in the receive direction
                   of a VCL at the low end of the cross-connect
                   must equal to the traffic parameters in the
                   transmit direction of the other VCL at the
                   high end of the cross-connect,
                   otherwise, the row creation fails.]
                   The agent also checks for internal errors
                   in building the cross-connect.
                
                   The atmVcCrossConnectIndex values in the
                   corresponding atmVclTable rows are filled
                   in by the agent at this point.
                
                (2b) The manager promotes the row in the
                   atmVcCrossConnectTable by setting
                   atmVcCrossConnectRowStatus to active(1).  If
                   this set is successful, the agent has reserved
                   the resources specified by the ATM traffic
                   parameter and Service category values
                   for each direction of the VC cross-connect
                   in an ATM switch or network.
                
                (3) The manager sets the
                   atmVcCrossConnectAdminStatus to up(1)
                   in all rows of this VC cross-connect to
                   turn the traffic flow on.
                
                
                One-Shot VC Cross-Connect Establishment
                
                A VC cross-connect may also be established in
                one step by a set-request with all necessary
                parameter values and atmVcCrossConnectRowStatus
                set to createAndGo(4).
                
                In contrast to the negotiated VC cross-connect
                establishment which allows for detailed error
                checking i.e., set errors are explicitly linked to
                particular resource acquisition failures), the
                one-shot VC cross-connect establishment
                performs the setup on one operation but does
                not have the advantage of step-wise error
                checking.
                
                VC Cross-Connect Retirement
                
                A VC cross-connect identified by a particular
                value of atmVcCrossConnectIndex is released by:
                
                (1) Setting atmVcCrossConnectRowStatus of all rows
                   identified by this value of
                   atmVcCrossConnectIndex to destroy(6).
                   The agent may release all
                   associated resources, and the
                   atmVcCrossConnectIndex values in the
                   corresponding atmVclTable row are removed.
                   Note that a situation when only a subset of
                   the associated rows are deleted corresponds
                   to a VC topology change.
                
                (2) After deletion of the appropriate
                   atmVcCrossConnectEntries, the manager may
                   set atmVclRowStatus to destroy(6) the
                   associated VCLs.  The agent releases
                   the resources and removes the associated
                   rows in the atmVclTable.
                
                VC Cross-Connect Reconfiguration
                
                At the discretion of the agent, a VC
                cross-connect may be reconfigured by
                adding and/or deleting leafs to/from
                the VC topology as per the VC cross-connect
                establishment/retirement procedures.
                Reconfiguration of traffic/service category parameter
                values requires release of the VC cross-connect
                before those parameter values may by changed
                for individual VCLs.
                ''',
                'atmvccrossconnectentry',
                'ATM-MIB', False),
            ],
            'ATM-MIB',
            'atmVcCrossConnectTable',
            _yang_ns._namespaces['ATM-MIB'],
        'ydk.models.atm.ATM_MIB'
        ),
    },
    'ATMMIB.AtmVclTable.AtmVclEntry.AtmVccAal5EncapsType_Enum' : _MetaInfoEnum('AtmVccAal5EncapsType_Enum', 'ydk.models.atm.ATM_MIB',
        {
            'vcMultiplexRoutedProtocol':'VCMULTIPLEXROUTEDPROTOCOL',
            'vcMultiplexBridgedProtocol8023':'VCMULTIPLEXBRIDGEDPROTOCOL8023',
            'vcMultiplexBridgedProtocol8025':'VCMULTIPLEXBRIDGEDPROTOCOL8025',
            'vcMultiplexBridgedProtocol8026':'VCMULTIPLEXBRIDGEDPROTOCOL8026',
            'vcMultiplexLANemulation8023':'VCMULTIPLEXLANEMULATION8023',
            'vcMultiplexLANemulation8025':'VCMULTIPLEXLANEMULATION8025',
            'llcEncapsulation':'LLCENCAPSULATION',
            'multiprotocolFrameRelaySscs':'MULTIPROTOCOLFRAMERELAYSSCS',
            'other':'OTHER',
            'unknown':'UNKNOWN',
        }, 'ATM-MIB', _yang_ns._namespaces['ATM-MIB']),
    'ATMMIB.AtmVclTable.AtmVclEntry.AtmVccAalType_Enum' : _MetaInfoEnum('AtmVccAalType_Enum', 'ydk.models.atm.ATM_MIB',
        {
            'aal1':'AAL1',
            'aal34':'AAL34',
            'aal5':'AAL5',
            'other':'OTHER',
            'unknown':'UNKNOWN',
            'aal2':'AAL2',
        }, 'ATM-MIB', _yang_ns._namespaces['ATM-MIB']),
    'ATMMIB.AtmVclTable.AtmVclEntry.CatmxVclOamLoopBkStatus_Enum' : _MetaInfoEnum('CatmxVclOamLoopBkStatus_Enum', 'ydk.models.atm.ATM_MIB',
        {
            'disabled':'DISABLED',
            'sent':'SENT',
            'received':'RECEIVED',
            'failed':'FAILED',
        }, 'CISCO-ATM-EXT-MIB', _yang_ns._namespaces['CISCO-ATM-EXT-MIB']),
    'ATMMIB.AtmVclTable.AtmVclEntry.CatmxVclOamVcState_Enum' : _MetaInfoEnum('CatmxVclOamVcState_Enum', 'ydk.models.atm.ATM_MIB',
        {
            'downRetry':'DOWNRETRY',
            'verified':'VERIFIED',
            'notVerified':'NOTVERIFIED',
            'upRetry':'UPRETRY',
            'aisRDI':'AISRDI',
            'aisOut':'AISOUT',
            'notManaged':'NOTMANAGED',
        }, 'CISCO-ATM-EXT-MIB', _yang_ns._namespaces['CISCO-ATM-EXT-MIB']),
    'ATMMIB.AtmVclTable.AtmVclEntry' : {
        'meta_info' : _MetaInfoClass('ATMMIB.AtmVclTable.AtmVclEntry',
            False, 
            [
            _MetaInfoClassMember('atmVclVci', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                The VCI value of the VCL.
                ''',
                'atmvclvci',
                'ATM-MIB', True),
            _MetaInfoClassMember('atmVclVpi', ATTRIBUTE, 'int' , None, None, 
                [(0, 4095)], [], 
                '''                The VPI value of the VCL.
                ''',
                'atmvclvpi',
                'ATM-MIB', True),
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'ifindex',
                'ATM-MIB', True),
            _MetaInfoClassMember('atmVccAal5CpcsReceiveSduSize', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                An instance of this object only exists when the
                local VCL end-point is also the VCC end-point,
                and AAL5 is in use.
                The maximum AAL5 CPCS SDU size in octets that is
                supported on the receive direction of this VCC.
                ''',
                'atmvccaal5cpcsreceivesdusize',
                'ATM-MIB', False),
            _MetaInfoClassMember('atmVccAal5CpcsTransmitSduSize', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                An instance of this object only exists when the
                local VCL end-point is also the VCC end-point,
                and AAL5 is in use.
                The maximum AAL5 CPCS SDU size in octets that is
                supported on the transmit direction of this VCC.
                ''',
                'atmvccaal5cpcstransmitsdusize',
                'ATM-MIB', False),
            _MetaInfoClassMember('atmVccAal5EncapsType', REFERENCE_ENUM_CLASS, 'AtmVccAal5EncapsType_Enum' , 'ydk.models.atm.ATM_MIB', 'ATMMIB.AtmVclTable.AtmVclEntry.AtmVccAal5EncapsType_Enum', 
                [], [], 
                '''                An instance of this object only exists when the
                local VCL end-point is also the VCC end-point,
                and AAL5 is in use.
                The type of data encapsulation used over
                the AAL5 SSCS layer. The definitions reference
                RFC 1483 Multiprotocol Encapsulation
                over ATM AAL5 and to the ATM Forum
                LAN Emulation specification.
                ''',
                'atmvccaal5encapstype',
                'ATM-MIB', False),
            _MetaInfoClassMember('atmVccAalType', REFERENCE_ENUM_CLASS, 'AtmVccAalType_Enum' , 'ydk.models.atm.ATM_MIB', 'ATMMIB.AtmVclTable.AtmVclEntry.AtmVccAalType_Enum', 
                [], [], 
                '''                An instance of this object only exists when the
                local VCL end-point is also the VCC end-point,
                and AAL is in use.
                The type of AAL used on this VCC.
                The AAL type includes AAL1, AAL2, AAL3/4,
                and AAL5. The other(4) may be user-defined
                AAL type.  The unknown type indicates that
                the AAL type cannot be determined.
                ''',
                'atmvccaaltype',
                'ATM-MIB', False),
            _MetaInfoClassMember('atmVclAdminStatus', REFERENCE_ENUM_CLASS, 'AtmVorXAdminStatus_Enum' , 'ydk.models.atm.ATM_TC_MIB', 'AtmVorXAdminStatus_Enum', 
                [], [], 
                '''                This object is instanciated only for a VCL which
                terminates a VCC (i.e., one which is NOT
                cross-connected to other VCLs). Its value
                specifies the desired administrative state of
                the VCL.
                ''',
                'atmvcladminstatus',
                'ATM-MIB', False),
            _MetaInfoClassMember('atmVclCastType', REFERENCE_ENUM_CLASS, 'AtmConnCastType_Enum' , 'ydk.models.atm.ATM_TC_MIB', 'AtmConnCastType_Enum', 
                [], [], 
                '''                The connection topology type.
                ''',
                'atmvclcasttype',
                'ATM-MIB', False),
            _MetaInfoClassMember('atmVclConnKind', REFERENCE_ENUM_CLASS, 'AtmConnKind_Enum' , 'ydk.models.atm.ATM_TC_MIB', 'AtmConnKind_Enum', 
                [], [], 
                '''                The use of call control.
                ''',
                'atmvclconnkind',
                'ATM-MIB', False),
            _MetaInfoClassMember('atmVclCrossConnectIdentifier', ATTRIBUTE, 'int' , None, None, 
                [(0, 2147483647)], [], 
                '''                This object is instantiated only for a VCL
                which is cross-connected to other VCLs
                that belong to the same VCC.  All such
                associated VCLs have the same value of this
                object, and all their cross-connections are
                identified either by entries that are indexed
                by the same value of atmVcCrossConnectIndex in
                the atmVcCrossConnectTable of this MIB module or by
                the same value of the cross-connect index in
                the cross-connect table for SVCs and Soft PVCs
                (defined in a separate MIB module).
                
                At no time should entries in these respective
                cross-connect tables exist simultaneously
                with the same cross-connect index value.
                The value of this object is initialized by the
                agent after the associated entries in the
                atmVcCrossConnectTable have been created.
                ''',
                'atmvclcrossconnectidentifier',
                'ATM-MIB', False),
            _MetaInfoClassMember('atmVclLastChange', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The value of sysUpTime at the time this VCL
                entered its current operational state.
                ''',
                'atmvcllastchange',
                'ATM-MIB', False),
            _MetaInfoClassMember('atmVclOperStatus', REFERENCE_ENUM_CLASS, 'AtmVorXOperStatus_Enum' , 'ydk.models.atm.ATM_TC_MIB', 'AtmVorXOperStatus_Enum', 
                [], [], 
                '''                The current operational status of the VCL.
                ''',
                'atmvcloperstatus',
                'ATM-MIB', False),
            _MetaInfoClassMember('atmVclReceiveTrafficDescrIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 2147483647)], [], 
                '''                The value of this object identifies the row
                in the ATM Traffic Descriptor Table which
                applies to the receive direction of this VCL.
                ''',
                'atmvclreceivetrafficdescrindex',
                'ATM-MIB', False),
            _MetaInfoClassMember('atmVclRowStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                This object is used to create, delete or
                modify a row in this table.  To create
                a new VCL, this object is initially set
                to 'createAndWait' or 'createAndGo'.
                This object should not be
                set to 'active' unless the following columnar
                objects have been set to their desired value
                in this row:
                atmVclReceiveTrafficDescrIndex,
                atmVclTransmitTrafficDescrIndex.
                In addition, if the local VCL end-point
                is also the VCC end-point:
                atmVccAalType.
                In addition, for AAL5 connections only:
                atmVccAal5CpcsTransmitSduSize,
                atmVccAal5CpcsReceiveSduSize, and
                atmVccAal5EncapsType. (The existence
                of these objects imply the AAL connection type.).
                The DESCRIPTION of atmVclEntry provides
                further guidance to row treatment in this table.
                ''',
                'atmvclrowstatus',
                'ATM-MIB', False),
            _MetaInfoClassMember('atmVclTransmitTrafficDescrIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 2147483647)], [], 
                '''                The value of this object identifies the row
                of the ATM Traffic Descriptor Table which applies
                to the transmit direction of this VCL.
                ''',
                'atmvcltransmittrafficdescrindex',
                'ATM-MIB', False),
            _MetaInfoClassMember('catmxVclOamCellsDropped', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Indicates the number of OAM cells dropped on 
                this VC.
                ''',
                'catmxvcloamcellsdropped',
                'CISCO-ATM-EXT-MIB', False),
            _MetaInfoClassMember('catmxVclOamCellsReceived', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Indicates the number of OAM cells received on 
                this VC.
                ''',
                'catmxvcloamcellsreceived',
                'CISCO-ATM-EXT-MIB', False),
            _MetaInfoClassMember('catmxVclOamCellsSent', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Indicates the number of OAM cells sent on 
                this VC.
                ''',
                'catmxvcloamcellssent',
                'CISCO-ATM-EXT-MIB', False),
            _MetaInfoClassMember('catmxVclOamDownRetryCount', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Specifies OAM retry count before declaring a VC 
                is down.
                ''',
                'catmxvcloamdownretrycount',
                'CISCO-ATM-EXT-MIB', False),
            _MetaInfoClassMember('catmxVclOamEndCCActCount', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Specifies OAM End-to-end Continuity check (CC) 
                Activation retry count.
                ''',
                'catmxvcloamendccactcount',
                'CISCO-ATM-EXT-MIB', False),
            _MetaInfoClassMember('catmxVclOamEndCCDeActCount', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Specifies OAM End-to-end Continuity check (CC) 
                Deactivation retry count.
                ''',
                'catmxvcloamendccdeactcount',
                'CISCO-ATM-EXT-MIB', False),
            _MetaInfoClassMember('catmxVclOamEndCCRetryFreq', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Specifies OAM End-to-end Continuity check (CC) 
                Activation/Deactivation retry frequency.
                ''',
                'catmxvcloamendccretryfreq',
                'CISCO-ATM-EXT-MIB', False),
            _MetaInfoClassMember('catmxVclOamEndCCStatus', REFERENCE_ENUM_CLASS, 'OamCCStatus_Enum' , 'ydk.models.atm.CISCO_ATM_EXT_MIB', 'OamCCStatus_Enum', 
                [], [], 
                '''                Indicates OAM End-to-end Continuity check (CC) 
                status.
                ''',
                'catmxvcloamendccstatus',
                'CISCO-ATM-EXT-MIB', False),
            _MetaInfoClassMember('catmxVclOamEndCCVcState', REFERENCE_ENUM_CLASS, 'OamCCVcState_Enum' , 'ydk.models.atm.CISCO_ATM_EXT_MIB', 'OamCCVcState_Enum', 
                [], [], 
                '''                Indicates OAM End-to-end Continuity check (CC) 
                VC state.
                ''',
                'catmxvcloamendccvcstate',
                'CISCO-ATM-EXT-MIB', False),
            _MetaInfoClassMember('catmxVclOamInF5ais', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Indicates the number of received OAM 
                F5 Alarm Indication Signal (AIS) cells from the VC.
                ''',
                'catmxvcloaminf5ais',
                'CISCO-ATM-EXT-MIB', False),
            _MetaInfoClassMember('catmxVclOamInF5rdi', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Indicates the number of received OAM 
                F5 Remote Detection Indication (RDI) cells from 
                the VC.
                ''',
                'catmxvcloaminf5rdi',
                'CISCO-ATM-EXT-MIB', False),
            _MetaInfoClassMember('catmxVclOamLoopbackFreq', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Specifies OAM loopback frequency.
                ''',
                'catmxvcloamloopbackfreq',
                'CISCO-ATM-EXT-MIB', False),
            _MetaInfoClassMember('catmxVclOamLoopBkStatus', REFERENCE_ENUM_CLASS, 'CatmxVclOamLoopBkStatus_Enum' , 'ydk.models.atm.ATM_MIB', 'ATMMIB.AtmVclTable.AtmVclEntry.CatmxVclOamLoopBkStatus_Enum', 
                [], [], 
                '''                Indicates OAM loopback status of the VC.
                disabled(1)  --   No OAMs on this VC.
                sent(2)      --   OAM sent, waiting for echo.
                received(3)  --   OAM received from target.
                failed(4)    --   Last OAM did not return.
                ''',
                'catmxvcloamloopbkstatus',
                'CISCO-ATM-EXT-MIB', False),
            _MetaInfoClassMember('catmxVclOamManage', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Specifies OAM Enable/Disable on the VC.
                true(1) indicates that OAM is enabled on the VC.
                false(2) indicates that OAM is disabled on the VC.
                ''',
                'catmxvcloammanage',
                'CISCO-ATM-EXT-MIB', False),
            _MetaInfoClassMember('catmxVclOamOutF5ais', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Indicates the number of transmitted OAM 
                F5 Alarm Indication Signal (AIS) cells to the VC.
                ''',
                'catmxvcloamoutf5ais',
                'CISCO-ATM-EXT-MIB', False),
            _MetaInfoClassMember('catmxVclOamOutF5rdi', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Indicates the number of transmitted OAM 
                F5 Remote Detection Indication (RDI) cells to the VC.
                ''',
                'catmxvcloamoutf5rdi',
                'CISCO-ATM-EXT-MIB', False),
            _MetaInfoClassMember('catmxVclOamRetryFreq', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Specifies OAM retry polling frequency.
                ''',
                'catmxvcloamretryfreq',
                'CISCO-ATM-EXT-MIB', False),
            _MetaInfoClassMember('catmxVclOamSegCCActCount', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Specifies OAM Segment Continuity check (CC) 
                Activation retry count.
                ''',
                'catmxvcloamsegccactcount',
                'CISCO-ATM-EXT-MIB', False),
            _MetaInfoClassMember('catmxVclOamSegCCDeActCount', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Specifies OAM Segment Continuity check (CC) 
                Deactivation retry count.
                ''',
                'catmxvcloamsegccdeactcount',
                'CISCO-ATM-EXT-MIB', False),
            _MetaInfoClassMember('catmxVclOamSegCCRetryFreq', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Specifies OAM Segment Continuity check (CC) 
                Activation/Deactivation retry frequency.
                ''',
                'catmxvcloamsegccretryfreq',
                'CISCO-ATM-EXT-MIB', False),
            _MetaInfoClassMember('catmxVclOamSegCCStatus', REFERENCE_ENUM_CLASS, 'OamCCStatus_Enum' , 'ydk.models.atm.CISCO_ATM_EXT_MIB', 'OamCCStatus_Enum', 
                [], [], 
                '''                Indicates OAM Segment Continuity check (CC) status.
                ''',
                'catmxvcloamsegccstatus',
                'CISCO-ATM-EXT-MIB', False),
            _MetaInfoClassMember('catmxVclOamSegCCVcState', REFERENCE_ENUM_CLASS, 'OamCCVcState_Enum' , 'ydk.models.atm.CISCO_ATM_EXT_MIB', 'OamCCVcState_Enum', 
                [], [], 
                '''                Indicates OAM Segment Continuity check (CC) VC 
                state.
                ''',
                'catmxvcloamsegccvcstate',
                'CISCO-ATM-EXT-MIB', False),
            _MetaInfoClassMember('catmxVclOamUpRetryCount', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Specifies OAM retry count before declaring a VC 
                is up.
                ''',
                'catmxvcloamupretrycount',
                'CISCO-ATM-EXT-MIB', False),
            _MetaInfoClassMember('catmxVclOamVcState', REFERENCE_ENUM_CLASS, 'CatmxVclOamVcState_Enum' , 'ydk.models.atm.ATM_MIB', 'ATMMIB.AtmVclTable.AtmVclEntry.CatmxVclOamVcState_Enum', 
                [], [], 
                '''                Indicates the state of VC OAM.
                downRetry(1)   --  Loopback failed. Retry sending 
                                   loopbacks with retry frequency. 
                                   VC is up.
                verified(2)    --  Loopback is successful.
                notVerified(3) --  Not verified by loopback, 
                                   AIS/RDI conditions are cleared.
                upRetry(4)     --  Retry successive loopbacks. 
                                   VC is down.
                aisRDI(5)      --  Received AIS/RDI. Loopback are 
                                   not sent in this state.
                aisOut(6)      --  Sending AIS. Loopback and reply are 
                                   not sent in this state.
                notManaged(7)  --  VC is not managed by OAM.
                ''',
                'catmxvcloamvcstate',
                'CISCO-ATM-EXT-MIB', False),
            _MetaInfoClassMember('cPppoeVcEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object specifies whether the PPPoE protocol
                should be enabled for this VCL. If the value of 
                this object is `false`, PPPoE protocol is 
                disabled; otherwise the PPPoE protocol is
                enabled.
                ''',
                'cpppoevcenable',
                'CISCO-PPPOE-MIB', False),
            ],
            'ATM-MIB',
            'atmVclEntry',
            _yang_ns._namespaces['ATM-MIB'],
        'ydk.models.atm.ATM_MIB'
        ),
    },
    'ATMMIB.AtmVclTable' : {
        'meta_info' : _MetaInfoClass('ATMMIB.AtmVclTable',
            False, 
            [
            _MetaInfoClassMember('atmVclEntry', REFERENCE_LIST, 'AtmVclEntry' , 'ydk.models.atm.ATM_MIB', 'ATMMIB.AtmVclTable.AtmVclEntry', 
                [], [], 
                '''                An entry in the VCL table. This entry is
                used to model a bi-directional VCL.
                To create a VCL at an ATM interface,
                either of the following procedures are used:
                
                Negotiated VCL establishment
                
                (1) The management application creates
                  a VCL entry in the atmVclTable
                  by setting atmVclRowStatus to createAndWait(5).
                  This may fail for the following reasons:
                  - The selected VPI/VCI values are unavailable,
                  - The selected VPI/VCI values are in use.
                  Otherwise, the agent creates a row and
                  reserves the VPI/VCI values on that port.
                
                (2) The manager selects an existing row(s) in the
                  atmTrafficDescrParamTable,
                  thereby, selecting a set of self-consistent
                  ATM traffic parameters and the service category
                  for receive and transmit directions of the VCL.
                
                
                (2a) If no suitable row(s) in the
                  atmTrafficDescrParamTable exists,
                  the manager must create a new row(s)
                  in that table.
                
                (2b) The manager characterizes the VCL's traffic
                  parameters through setting the
                  atmVclReceiveTrafficDescrIndex and the
                  atmVclTransmitTrafficDescrIndex values
                  in the VCL table, which point to the rows
                  containing desired ATM traffic parameter values
                  in the atmTrafficDescrParamTable.  The agent
                  will check the availability of resources and
                  may refuse the request.
                  If the transmit and receive service categories
                  are inconsistent, the agent should refuse the
                  request.
                
                (3) The manager activates the VCL by setting the
                  the atmVclRowStatus to active(1) (for
                  requirements on this activation see the
                  description of atmVclRowStatus).
                  If this set is successful, the agent has
                  reserved the resources to satisfy the requested
                  traffic parameter values and the service category
                  for that VCL.
                (4) If the VCL terminates a VCC in the ATM host
                  or switch, the manager turns on the
                  atmVclAdminStatus to up(1) to turn the VCL
                  traffic flow on.  Otherwise, the
                  atmVcCrossConnectTable  must be used
                  to cross-connect the VCL to another VCL(s)
                  in an ATM switch or network.
                
                One-Shot VCL Establishment
                
                A VCL may also be established in one step by a
                set-request with all necessary VCL parameter
                values and atmVclRowStatus set to createAndGo(4).
                
                In contrast to the negotiated VCL establishment
                which allows for detailed error checking
                (i.e., set errors are explicitly linked to
                particular resource acquisition failures),
                the one-shot VCL establishment
                performs the setup on one operation but
                does not have the advantage of step-wise
                error checking.
                
                VCL Retirement
                
                A VCL is released by setting atmVclRowStatus to
                destroy(6), and the agent may release all
                associated resources.
                ''',
                'atmvclentry',
                'ATM-MIB', False),
            ],
            'ATM-MIB',
            'atmVclTable',
            _yang_ns._namespaces['ATM-MIB'],
        'ydk.models.atm.ATM_MIB'
        ),
    },
    'ATMMIB.AtmVpCrossConnectTable.AtmVpCrossConnectEntry' : {
        'meta_info' : _MetaInfoClass('ATMMIB.AtmVpCrossConnectTable.AtmVpCrossConnectEntry',
            False, 
            [
            _MetaInfoClassMember('atmVpCrossConnectHighIfIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                The ifIndex value of the ATM interface for
                this VP cross-connect. The term high implies that
                this ATM interface has the numerically higher
                ifIndex value than the  other ATM interface
                identified in the same atmVpCrossConnectEntry.
                ''',
                'atmvpcrossconnecthighifindex',
                'ATM-MIB', True),
            _MetaInfoClassMember('atmVpCrossConnectHighVpi', ATTRIBUTE, 'int' , None, None, 
                [(0, 4095)], [], 
                '''                The VPI value at the ATM interface
                associated with the VP cross-connect that is
                identified by atmVpCrossConnectHighIfIndex.
                ''',
                'atmvpcrossconnecthighvpi',
                'ATM-MIB', True),
            _MetaInfoClassMember('atmVpCrossConnectIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                A unique value to identify this VP cross-connect.
                For each VPL associated with this cross-connect,
                the agent reports this cross-connect index value
                in the atmVplCrossConnectIdentifier attribute of
                the corresponding atmVplTable entries.
                ''',
                'atmvpcrossconnectindex',
                'ATM-MIB', True),
            _MetaInfoClassMember('atmVpCrossConnectLowIfIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                The ifIndex value of the ATM interface for
                this VP cross-connect. The term low implies
                that this ATM interface has the numerically lower
                ifIndex value than the other ATM interface
                identified in the same atmVpCrossConnectEntry.
                ''',
                'atmvpcrossconnectlowifindex',
                'ATM-MIB', True),
            _MetaInfoClassMember('atmVpCrossConnectLowVpi', ATTRIBUTE, 'int' , None, None, 
                [(0, 4095)], [], 
                '''                The VPI value at the ATM interface
                associated with the VP cross-connect that is
                identified by atmVpCrossConnectLowIfIndex.
                ''',
                'atmvpcrossconnectlowvpi',
                'ATM-MIB', True),
            _MetaInfoClassMember('atmVpCrossConnectAdminStatus', REFERENCE_ENUM_CLASS, 'AtmVorXAdminStatus_Enum' , 'ydk.models.atm.ATM_TC_MIB', 'AtmVorXAdminStatus_Enum', 
                [], [], 
                '''                The desired administrative status of this
                bi-directional VP cross-connect.
                ''',
                'atmvpcrossconnectadminstatus',
                'ATM-MIB', False),
            _MetaInfoClassMember('atmVpCrossConnectH2LLastChange', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The value of sysUpTime at the time this
                VP cross-connect entered its current operational
                in the high to low direction.
                ''',
                'atmvpcrossconnecth2llastchange',
                'ATM-MIB', False),
            _MetaInfoClassMember('atmVpCrossConnectH2LOperStatus', REFERENCE_ENUM_CLASS, 'AtmVorXOperStatus_Enum' , 'ydk.models.atm.ATM_TC_MIB', 'AtmVorXOperStatus_Enum', 
                [], [], 
                '''                The operational status of the VP cross-connect
                in one direction; (i.e., from the high to
                low direction).
                ''',
                'atmvpcrossconnecth2loperstatus',
                'ATM-MIB', False),
            _MetaInfoClassMember('atmVpCrossConnectL2HLastChange', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The value of sysUpTime at the time this
                VP cross-connect entered its current operational
                state in the low to high direction.
                ''',
                'atmvpcrossconnectl2hlastchange',
                'ATM-MIB', False),
            _MetaInfoClassMember('atmVpCrossConnectL2HOperStatus', REFERENCE_ENUM_CLASS, 'AtmVorXOperStatus_Enum' , 'ydk.models.atm.ATM_TC_MIB', 'AtmVorXOperStatus_Enum', 
                [], [], 
                '''                The operational status of the VP cross-connect
                in one direction; (i.e., from the low to
                high direction).
                ''',
                'atmvpcrossconnectl2hoperstatus',
                'ATM-MIB', False),
            _MetaInfoClassMember('atmVpCrossConnectRowStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                The status of this entry in the
                atmVpCrossConnectTable.  This object is used to
                create a cross-connect for cross-connecting
                VPLs which are created using the atmVplTable
                or to change or delete an existing cross-connect.
                This object must be initially set
                to `createAndWait' or 'createAndGo'.
                To turn on a VP cross-connect,
                the atmVpCrossConnectAdminStatus
                is set to `up'.
                ''',
                'atmvpcrossconnectrowstatus',
                'ATM-MIB', False),
            ],
            'ATM-MIB',
            'atmVpCrossConnectEntry',
            _yang_ns._namespaces['ATM-MIB'],
        'ydk.models.atm.ATM_MIB'
        ),
    },
    'ATMMIB.AtmVpCrossConnectTable' : {
        'meta_info' : _MetaInfoClass('ATMMIB.AtmVpCrossConnectTable',
            False, 
            [
            _MetaInfoClassMember('atmVpCrossConnectEntry', REFERENCE_LIST, 'AtmVpCrossConnectEntry' , 'ydk.models.atm.ATM_MIB', 'ATMMIB.AtmVpCrossConnectTable.AtmVpCrossConnectEntry', 
                [], [], 
                '''                An entry in the ATM VP Cross Connect table.
                This entry is used to model a bi-directional
                ATM VP cross-connect which cross-connects
                two VPLs.
                
                Step-wise Procedures to set up a VP Cross-connect
                
                Once the entries in the atmVplTable are created,
                the following procedures are used
                to cross-connect the VPLs together.
                
                (1) The manager obtains a unique
                   atmVpCrossConnectIndex by reading the
                   atmVpCrossConnectIndexNext object.
                
                (2) Next, the manager creates a set of one
                   or more rows in the ATM VP Cross Connect
                   Table, one for each cross-connection between
                   two VPLs.  Each row is indexed by the ATM
                   interface port numbers and VPI values of the
                   two ends of that cross-connection.
                   This set of rows specifies the topology of the
                   VPC cross-connect and is identified by a single
                   value of atmVpCrossConnectIndex.
                
                Negotiated VP Cross-Connect Establishment
                
                (2a) The manager creates a row in this table by
                   setting atmVpCrossConnectRowStatus to
                   createAndWait(5).  The agent checks the
                   requested topology and the mutual sanity of
                   the ATM traffic parameters and
                   service categories, i.e., the row creation
                   fails if:
                   - the requested topology is incompatible with
                     associated values of atmVplCastType,
                   - the requested topology is not supported
                     by the agent,
                   - the traffic/service category parameter values
                     associated with the requested row are
                     incompatible with those of already existing
                     rows for this VP cross-connect.
                   [For example, for setting up
                   a point-to-point VP cross-connect, the
                   ATM traffic parameters in the receive direction
                   of a VPL at the low end of the cross-connect
                   must equal to the traffic parameters in the
                   transmit direction of the other VPL at the
                   high end of the cross-connect,
                   otherwise, the row creation fails.]
                   The agent also checks for internal errors
                   in building the cross-connect.
                
                   The atmVpCrossConnectIndex values in the
                   corresponding atmVplTable rows are filled
                   in by the agent at this point.
                
                (2b) The manager promotes the row in the
                   atmVpCrossConnectTable by setting
                   atmVpCrossConnectRowStatus to active(1).  If
                   this set is successful, the agent has reserved
                   the resources specified by the ATM traffic
                   parameter and Service category values
                   for each direction of the VP cross-connect
                   in an ATM switch or network.
                
                (3) The manager sets the
                   atmVpCrossConnectAdminStatus to up(1) in all
                   rows of this VP cross-connect to turn the
                   traffic flow on.
                
                
                One-Shot VP Cross-Connect Establishment
                
                A VP cross-connect may also be established in
                one step by a set-request with all necessary
                parameter values and atmVpCrossConnectRowStatus
                set to createAndGo(4).
                
                In contrast to the negotiated VP cross-connect
                establishment which allows for detailed error
                checking (i.e., set errors are explicitly linked
                to particular resource acquisition failures),
                the one-shot VP cross-connect establishment
                performs the setup on one operation but does not
                have the advantage of step-wise error checking.
                
                VP Cross-Connect Retirement
                
                A VP cross-connect identified by a particular
                value of atmVpCrossConnectIndex is released by:
                
                (1) Setting atmVpCrossConnectRowStatus of all
                   rows identified by this value of
                   atmVpCrossConnectIndex to destroy(6).
                   The agent may release all
                   associated resources, and the
                   atmVpCrossConnectIndex values in the
                   corresponding atmVplTable row are removed.
                   Note that a situation when only a subset of
                   the associated rows are deleted corresponds
                   to a VP topology change.
                
                (2) After deletion of the appropriate
                   atmVpCrossConnectEntries, the manager may
                   set atmVplRowStatus to destroy(6) the
                   associated VPLs.  The agent releases
                   the resources and removes the associated
                   rows in the atmVplTable.
                
                VP Cross-connect Reconfiguration
                
                At the discretion of the agent, a VP
                cross-connect may be reconfigured by
                adding and/or deleting leafs to/from
                the VP topology as per the VP cross-connect
                establishment/retirement procedures.
                Reconfiguration of traffic/service category parameter
                values requires release of the VP cross-connect
                before those parameter values may by changed
                for individual VPLs.
                ''',
                'atmvpcrossconnectentry',
                'ATM-MIB', False),
            ],
            'ATM-MIB',
            'atmVpCrossConnectTable',
            _yang_ns._namespaces['ATM-MIB'],
        'ydk.models.atm.ATM_MIB'
        ),
    },
    'ATMMIB.AtmVplTable.AtmVplEntry' : {
        'meta_info' : _MetaInfoClass('ATMMIB.AtmVplTable.AtmVplEntry',
            False, 
            [
            _MetaInfoClassMember('atmVplVpi', ATTRIBUTE, 'int' , None, None, 
                [(0, 4095)], [], 
                '''                The VPI value of the VPL.
                ''',
                'atmvplvpi',
                'ATM-MIB', True),
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'ifindex',
                'ATM-MIB', True),
            _MetaInfoClassMember('atmVplAdminStatus', REFERENCE_ENUM_CLASS, 'AtmVorXAdminStatus_Enum' , 'ydk.models.atm.ATM_TC_MIB', 'AtmVorXAdminStatus_Enum', 
                [], [], 
                '''                This object is instanciated only for a VPL
                which terminates a VPC (i.e., one which is
                NOT cross-connected to other VPLs).
                Its value specifies the desired
                administrative state of the VPL.
                ''',
                'atmvpladminstatus',
                'ATM-MIB', False),
            _MetaInfoClassMember('atmVplCastType', REFERENCE_ENUM_CLASS, 'AtmConnCastType_Enum' , 'ydk.models.atm.ATM_TC_MIB', 'AtmConnCastType_Enum', 
                [], [], 
                '''                The connection topology type.
                ''',
                'atmvplcasttype',
                'ATM-MIB', False),
            _MetaInfoClassMember('atmVplConnKind', REFERENCE_ENUM_CLASS, 'AtmConnKind_Enum' , 'ydk.models.atm.ATM_TC_MIB', 'AtmConnKind_Enum', 
                [], [], 
                '''                The use of call control.
                ''',
                'atmvplconnkind',
                'ATM-MIB', False),
            _MetaInfoClassMember('atmVplCrossConnectIdentifier', ATTRIBUTE, 'int' , None, None, 
                [(0, 2147483647)], [], 
                '''                This object is instantiated only for a VPL
                which is cross-connected to other VPLs
                that belong to the same VPC.  All such
                associated VPLs have the same value of this
                object, and all their cross-connections are
                identified either by entries that are indexed
                by the same value of atmVpCrossConnectIndex in
                the atmVpCrossConnectTable of this MIB module or by
                the same value of the cross-connect index in
                the cross-connect table for SVCs and Soft PVCs
                (defined in a separate MIB module).
                At no time should entries in these respective
                cross-connect tables exist simultaneously
                with the same cross-connect index value.
                The value of this object is initialized by the
                agent after the associated entries in the
                atmVpCrossConnectTable have been created.
                ''',
                'atmvplcrossconnectidentifier',
                'ATM-MIB', False),
            _MetaInfoClassMember('atmVplLastChange', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The value of sysUpTime at the time this
                VPL entered its current operational state.
                ''',
                'atmvpllastchange',
                'ATM-MIB', False),
            _MetaInfoClassMember('atmVplOperStatus', REFERENCE_ENUM_CLASS, 'AtmVorXOperStatus_Enum' , 'ydk.models.atm.ATM_TC_MIB', 'AtmVorXOperStatus_Enum', 
                [], [], 
                '''                The current operational status of the VPL.
                ''',
                'atmvploperstatus',
                'ATM-MIB', False),
            _MetaInfoClassMember('atmVplReceiveTrafficDescrIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 2147483647)], [], 
                '''                The value of this object identifies the row
                in the atmTrafficDescrParamTable which
                applies to the receive direction of the VPL.
                ''',
                'atmvplreceivetrafficdescrindex',
                'ATM-MIB', False),
            _MetaInfoClassMember('atmVplRowStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                This object is used to create, delete
                or modify a row in this table.
                To create a new VCL, this object is
                initially set to 'createAndWait' or
                'createAndGo'.  This object should not be
                set to 'active' unless the following columnar
                objects have been set to their desired value
                in this row:
                atmVplReceiveTrafficDescrIndex and
                atmVplTransmitTrafficDescrIndex.
                The DESCRIPTION of atmVplEntry provides
                further guidance to row treatment in this table.
                ''',
                'atmvplrowstatus',
                'ATM-MIB', False),
            _MetaInfoClassMember('atmVplTransmitTrafficDescrIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 2147483647)], [], 
                '''                The value of this object identifies the row
                in the atmTrafficDescrParamTable which
                applies to the transmit direction of the VPL.
                ''',
                'atmvpltransmittrafficdescrindex',
                'ATM-MIB', False),
            ],
            'ATM-MIB',
            'atmVplEntry',
            _yang_ns._namespaces['ATM-MIB'],
        'ydk.models.atm.ATM_MIB'
        ),
    },
    'ATMMIB.AtmVplTable' : {
        'meta_info' : _MetaInfoClass('ATMMIB.AtmVplTable',
            False, 
            [
            _MetaInfoClassMember('atmVplEntry', REFERENCE_LIST, 'AtmVplEntry' , 'ydk.models.atm.ATM_MIB', 'ATMMIB.AtmVplTable.AtmVplEntry', 
                [], [], 
                '''                An entry in the VPL table.  This entry is
                used to model a bi-directional VPL.
                To create a VPL at an ATM interface,
                either of the following procedures are used:
                
                Negotiated VPL establishment
                
                (1) The management application creates
                  a VPL entry in the atmVplTable
                  by setting atmVplRowStatus to createAndWait(5).
                  This may fail for the following reasons:
                  - The selected VPI value is unavailable,
                  - The selected VPI value is in use.
                  Otherwise, the agent creates a row and
                  reserves the VPI value on that port.
                
                (2) The manager selects an existing row(s) in the
                  atmTrafficDescrParamTable,
                  thereby, selecting a set of self-consistent
                  ATM traffic parameters and the service category
                  for receive and transmit directions of the VPL.
                
                (2a) If no suitable row(s) in the
                  atmTrafficDescrParamTable exists,
                  the manager must create a new row(s)
                  in that table.
                
                (2b) The manager characterizes the VPL's traffic
                  parameters through setting the
                  atmVplReceiveTrafficDescrIndex and the
                  atmVplTransmitTrafficDescrIndex values
                  in the VPL table, which point to the rows
                  containing desired ATM traffic parameter values
                  in the atmTrafficDescrParamTable.  The agent
                  will check the availability of resources and
                  may refuse the request.
                  If the transmit and receive service categories
                  are inconsistent, the agent should refuse the
                  request.
                
                (3) The manager activates the VPL by setting the
                  the atmVplRowStatus to active(1).
                  If this set is successful, the agent has
                  reserved the resources to satisfy the requested
                  traffic parameter values and the service category
                  for that VPL.
                
                (4) If the VPL terminates a VPC in the ATM host
                  or switch, the manager turns on the
                  atmVplAdminStatus to up(1) to turn the VPL
                  traffic flow on.  Otherwise, the
                  atmVpCrossConnectTable  must be used
                  to cross-connect the VPL to another VPL(s)
                  in an ATM switch or network.
                
                One-Shot VPL Establishment
                
                A VPL may also be established in one step by a
                set-request with all necessary VPL parameter
                values and atmVplRowStatus set to createAndGo(4).
                
                In contrast to the negotiated VPL establishment
                which allows for detailed error checking
                (i.e., set errors are explicitly linked to
                particular resource acquisition failures),
                the one-shot VPL establishment
                performs the setup on one operation but
                does not have the advantage of step-wise
                error checking.
                
                VPL Retirement
                
                A VPL is released by setting atmVplRowStatus to
                destroy(6), and the agent may release all
                associated resources.
                ''',
                'atmvplentry',
                'ATM-MIB', False),
            ],
            'ATM-MIB',
            'atmVplTable',
            _yang_ns._namespaces['ATM-MIB'],
        'ydk.models.atm.ATM_MIB'
        ),
    },
    'ATMMIB' : {
        'meta_info' : _MetaInfoClass('ATMMIB',
            False, 
            [
            _MetaInfoClassMember('aal5VccTable', REFERENCE_CLASS, 'Aal5VccTable' , 'ydk.models.atm.ATM_MIB', 'ATMMIB.Aal5VccTable', 
                [], [], 
                '''                This table contains AAL5 VCC performance
                parameters.
                ''',
                'aal5vcctable',
                'ATM-MIB', False),
            _MetaInfoClassMember('atmInterfaceConfTable', REFERENCE_CLASS, 'AtmInterfaceConfTable' , 'ydk.models.atm.ATM_MIB', 'ATMMIB.AtmInterfaceConfTable', 
                [], [], 
                '''                This table contains ATM local interface
                configuration parameters, one entry per ATM
                interface port.
                ''',
                'atminterfaceconftable',
                'ATM-MIB', False),
            _MetaInfoClassMember('atmInterfaceDs3PlcpTable', REFERENCE_CLASS, 'AtmInterfaceDs3PlcpTable' , 'ydk.models.atm.ATM_MIB', 'ATMMIB.AtmInterfaceDs3PlcpTable', 
                [], [], 
                '''                This table contains ATM interface DS3 PLCP
                parameters and state variables, one entry per
                ATM interface port.
                ''',
                'atminterfaceds3plcptable',
                'ATM-MIB', False),
            _MetaInfoClassMember('atmInterfaceTCTable', REFERENCE_CLASS, 'AtmInterfaceTCTable' , 'ydk.models.atm.ATM_MIB', 'ATMMIB.AtmInterfaceTCTable', 
                [], [], 
                '''                This table contains ATM interface TC
                Sublayer parameters and state variables,
                one entry per ATM interface port.
                ''',
                'atminterfacetctable',
                'ATM-MIB', False),
            _MetaInfoClassMember('atmMIBObjects', REFERENCE_CLASS, 'AtmMIBObjects' , 'ydk.models.atm.ATM_MIB', 'ATMMIB.AtmMIBObjects', 
                [], [], 
                '''                ''',
                'atmmibobjects',
                'ATM-MIB', False),
            _MetaInfoClassMember('atmTrafficDescrParamTable', REFERENCE_CLASS, 'AtmTrafficDescrParamTable' , 'ydk.models.atm.ATM_MIB', 'ATMMIB.AtmTrafficDescrParamTable', 
                [], [], 
                '''                This table contains information on ATM traffic
                descriptor type and the associated parameters.
                ''',
                'atmtrafficdescrparamtable',
                'ATM-MIB', False),
            _MetaInfoClassMember('atmVcCrossConnectTable', REFERENCE_CLASS, 'AtmVcCrossConnectTable' , 'ydk.models.atm.ATM_MIB', 'ATMMIB.AtmVcCrossConnectTable', 
                [], [], 
                '''                The ATM VC Cross Connect table for PVCs.
                An entry in this table models two
                cross-connected VCLs.
                Each VCL must have its atmConnKind set
                to pvc(1).
                ''',
                'atmvccrossconnecttable',
                'ATM-MIB', False),
            _MetaInfoClassMember('atmVclTable', REFERENCE_CLASS, 'AtmVclTable' , 'ydk.models.atm.ATM_MIB', 'ATMMIB.AtmVclTable', 
                [], [], 
                '''                The Virtual Channel Link (VCL) table.  A
                bi-directional VCL is modeled as one entry
                in this table. This table can be used for
                PVCs, SVCs and Soft PVCs.
                ''',
                'atmvcltable',
                'ATM-MIB', False),
            _MetaInfoClassMember('atmVpCrossConnectTable', REFERENCE_CLASS, 'AtmVpCrossConnectTable' , 'ydk.models.atm.ATM_MIB', 'ATMMIB.AtmVpCrossConnectTable', 
                [], [], 
                '''                The ATM VP Cross Connect table for PVCs.
                An entry in this table models two
                cross-connected VPLs.
                Each VPL must have its atmConnKind set
                to pvc(1).
                ''',
                'atmvpcrossconnecttable',
                'ATM-MIB', False),
            _MetaInfoClassMember('atmVplTable', REFERENCE_CLASS, 'AtmVplTable' , 'ydk.models.atm.ATM_MIB', 'ATMMIB.AtmVplTable', 
                [], [], 
                '''                The Virtual Path Link (VPL) table.  A
                bi-directional VPL is modeled as one entry
                in this table. This table can be used for
                PVCs, SVCs and Soft PVCs.
                Entries are not present in this table for
                the VPIs used by entries in the atmVclTable.
                ''',
                'atmvpltable',
                'ATM-MIB', False),
            ],
            'ATM-MIB',
            'ATM-MIB',
            _yang_ns._namespaces['ATM-MIB'],
        'ydk.models.atm.ATM_MIB'
        ),
    },
}
_meta_table['ATMMIB.Aal5VccTable.Aal5VccEntry']['meta_info'].parent =_meta_table['ATMMIB.Aal5VccTable']['meta_info']
_meta_table['ATMMIB.AtmInterfaceConfTable.AtmInterfaceConfEntry']['meta_info'].parent =_meta_table['ATMMIB.AtmInterfaceConfTable']['meta_info']
_meta_table['ATMMIB.AtmInterfaceDs3PlcpTable.AtmInterfaceDs3PlcpEntry']['meta_info'].parent =_meta_table['ATMMIB.AtmInterfaceDs3PlcpTable']['meta_info']
_meta_table['ATMMIB.AtmInterfaceTCTable.AtmInterfaceTCEntry']['meta_info'].parent =_meta_table['ATMMIB.AtmInterfaceTCTable']['meta_info']
_meta_table['ATMMIB.AtmTrafficDescrParamTable.AtmTrafficDescrParamEntry']['meta_info'].parent =_meta_table['ATMMIB.AtmTrafficDescrParamTable']['meta_info']
_meta_table['ATMMIB.AtmVcCrossConnectTable.AtmVcCrossConnectEntry']['meta_info'].parent =_meta_table['ATMMIB.AtmVcCrossConnectTable']['meta_info']
_meta_table['ATMMIB.AtmVclTable.AtmVclEntry']['meta_info'].parent =_meta_table['ATMMIB.AtmVclTable']['meta_info']
_meta_table['ATMMIB.AtmVpCrossConnectTable.AtmVpCrossConnectEntry']['meta_info'].parent =_meta_table['ATMMIB.AtmVpCrossConnectTable']['meta_info']
_meta_table['ATMMIB.AtmVplTable.AtmVplEntry']['meta_info'].parent =_meta_table['ATMMIB.AtmVplTable']['meta_info']
_meta_table['ATMMIB.Aal5VccTable']['meta_info'].parent =_meta_table['ATMMIB']['meta_info']
_meta_table['ATMMIB.AtmInterfaceConfTable']['meta_info'].parent =_meta_table['ATMMIB']['meta_info']
_meta_table['ATMMIB.AtmInterfaceDs3PlcpTable']['meta_info'].parent =_meta_table['ATMMIB']['meta_info']
_meta_table['ATMMIB.AtmInterfaceTCTable']['meta_info'].parent =_meta_table['ATMMIB']['meta_info']
_meta_table['ATMMIB.AtmMIBObjects']['meta_info'].parent =_meta_table['ATMMIB']['meta_info']
_meta_table['ATMMIB.AtmTrafficDescrParamTable']['meta_info'].parent =_meta_table['ATMMIB']['meta_info']
_meta_table['ATMMIB.AtmVcCrossConnectTable']['meta_info'].parent =_meta_table['ATMMIB']['meta_info']
_meta_table['ATMMIB.AtmVclTable']['meta_info'].parent =_meta_table['ATMMIB']['meta_info']
_meta_table['ATMMIB.AtmVpCrossConnectTable']['meta_info'].parent =_meta_table['ATMMIB']['meta_info']
_meta_table['ATMMIB.AtmVplTable']['meta_info'].parent =_meta_table['ATMMIB']['meta_info']
