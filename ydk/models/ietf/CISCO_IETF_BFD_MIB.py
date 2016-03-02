""" CISCO_IETF_BFD_MIB 

This document contains the Management information base for
Bidirectional Forwarding Detection(BFD) Protocol as defined
in draft\-ietf\-bfd\-base\-06.txt.

BFD is a protocol intended to detect faults in the
bidirectional path between two forwarding engines, including
interfaces, data link(s), and to the extent possible the forwarding
engines themselves, with potentially very low latency.  It operates
independently of media, data protocols, and routing protocols.

This MIB module is based on the Internet Draft
draft\-ietf\-bfd\-mib\-03.txt and draft\-ietf\-bfd\-mib\-04.txt

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.inet.INET_ADDRESS_MIB import InetAddressType_Enum
from ydk.models.snmpv2.SNMPv2_TC import RowStatus_Enum
from ydk.models.snmpv2.SNMPv2_TC import StorageType_Enum

class CiscoBfdDiag_Enum(Enum):
    """
    CiscoBfdDiag_Enum

    A common BFD diagnostic code.

    """

    NODIAGNOSTIC = 0

    CONTROLDETECTIONTIMEEXPIRED = 1

    ECHOFUNCTIONFAILED = 2

    NEIGHBORSIGNALEDSESSIONDOWN = 3

    FORWARDINGPLANERESET = 4

    PATHDOWN = 5

    CONCATENATEDPATHDOWN = 6

    ADMINISTRATIVELYDOWN = 7

    REVERSECONCATENATEDPATHDOWN = 8


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _CISCO_IETF_BFD_MIB as meta
        return meta._meta_table['CiscoBfdDiag_Enum']



class CISCOIETFBFDMIB(object):
    """
    
    
    .. attribute:: ciscobfdscalarobjects
    
    	
    	**type**\: :py:class:`CiscoBfdScalarObjects <ydk.models.ietf.CISCO_IETF_BFD_MIB.CISCOIETFBFDMIB.CiscoBfdScalarObjects>`
    
    .. attribute:: ciscobfdsessdiscmaptable
    
    	The BFD Session Discriminator Mapping Table maps a local discriminator value to associated BFD sessions' CiscoBfdSessIndexTC used in the ciscoBfdSessTable
    	**type**\: :py:class:`CiscoBfdSessDiscMapTable <ydk.models.ietf.CISCO_IETF_BFD_MIB.CISCOIETFBFDMIB.CiscoBfdSessDiscMapTable>`
    
    .. attribute:: ciscobfdsessipmaptable
    
    	The BFD Session IP Mapping Table maps given ciscoBfdSessInterface, ciscoBfdSessAddrType, and ciscoBbfdSessAddr to an associated BFD sessions' CiscoBfdSessIndexTC used in the ciscoBfdSessTable. This table SHOULD contains those BFD sessions are of IP type\: singleHop(1) and multiHop(2)
    	**type**\: :py:class:`CiscoBfdSessIpMapTable <ydk.models.ietf.CISCO_IETF_BFD_MIB.CISCOIETFBFDMIB.CiscoBfdSessIpMapTable>`
    
    .. attribute:: ciscobfdsessmaptable
    
    	The BFD Session Mapping Table maps the complex indexing of the BFD sessions to the flat  CiscoBfdSessIndexTC used in the ciscoBfdSessTable
    	**type**\: :py:class:`CiscoBfdSessMapTable <ydk.models.ietf.CISCO_IETF_BFD_MIB.CISCOIETFBFDMIB.CiscoBfdSessMapTable>`
    
    .. attribute:: ciscobfdsesstable
    
    	The BFD Session Table describes the BFD sessions
    	**type**\: :py:class:`CiscoBfdSessTable <ydk.models.ietf.CISCO_IETF_BFD_MIB.CISCOIETFBFDMIB.CiscoBfdSessTable>`
    
    

    """

    _prefix = 'cisco-ietf'
    _revision = '2011-04-16'

    def __init__(self):
        self.ciscobfdscalarobjects = CISCOIETFBFDMIB.CiscoBfdScalarObjects()
        self.ciscobfdscalarobjects.parent = self
        self.ciscobfdsessdiscmaptable = CISCOIETFBFDMIB.CiscoBfdSessDiscMapTable()
        self.ciscobfdsessdiscmaptable.parent = self
        self.ciscobfdsessipmaptable = CISCOIETFBFDMIB.CiscoBfdSessIpMapTable()
        self.ciscobfdsessipmaptable.parent = self
        self.ciscobfdsessmaptable = CISCOIETFBFDMIB.CiscoBfdSessMapTable()
        self.ciscobfdsessmaptable.parent = self
        self.ciscobfdsesstable = CISCOIETFBFDMIB.CiscoBfdSessTable()
        self.ciscobfdsesstable.parent = self


    class CiscoBfdScalarObjects(object):
        """
        
        
        .. attribute:: ciscobfdadminstatus
        
        	The global administrative status of BFD in this router. The value 'enabled' denotes that the BFD Process is  active on at least one interface; 'disabled' disables   it on all interfaces
        	**type**\: :py:class:`CiscoBfdAdminStatus_Enum <ydk.models.ietf.CISCO_IETF_BFD_MIB.CISCOIETFBFDMIB.CiscoBfdScalarObjects.CiscoBfdAdminStatus_Enum>`
        
        .. attribute:: ciscobfdsessnotificationsenable
        
        	If this object is set to true(1), then it enables the emission of ciscoBfdSessUp and ciscoBfdSessDown  notifications; otherwise these notifications are not  emitted
        	**type**\: bool
        
        .. attribute:: ciscobfdversionnumber
        
        	The current version number of the BFD protocol
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'cisco-ietf'
        _revision = '2011-04-16'

        def __init__(self):
            self.parent = None
            self.ciscobfdadminstatus = None
            self.ciscobfdsessnotificationsenable = None
            self.ciscobfdversionnumber = None

        class CiscoBfdAdminStatus_Enum(Enum):
            """
            CiscoBfdAdminStatus_Enum

            The global administrative status of BFD in this router.
            The value 'enabled' denotes that the BFD Process is 
            active on at least one interface; 'disabled' disables  
            it on all interfaces.

            """

            ENABLED = 1

            DISABLED = 2


            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _CISCO_IETF_BFD_MIB as meta
                return meta._meta_table['CISCOIETFBFDMIB.CiscoBfdScalarObjects.CiscoBfdAdminStatus_Enum']


        @property
        def _common_path(self):

            return '/CISCO-IETF-BFD-MIB:CISCO-IETF-BFD-MIB/CISCO-IETF-BFD-MIB:ciscoBfdScalarObjects'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ciscobfdadminstatus is not None:
                return True

            if self.ciscobfdsessnotificationsenable is not None:
                return True

            if self.ciscobfdversionnumber is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _CISCO_IETF_BFD_MIB as meta
            return meta._meta_table['CISCOIETFBFDMIB.CiscoBfdScalarObjects']['meta_info']


    class CiscoBfdSessDiscMapTable(object):
        """
        The BFD Session Discriminator Mapping Table maps a
        local discriminator value to associated BFD sessions'
        CiscoBfdSessIndexTC used in the ciscoBfdSessTable.
        
        .. attribute:: ciscobfdsessdiscmapentry
        
        	Each row contains a mapping between a local discriminator value to an entry in ciscoBfdSessTable
        	**type**\: list of :py:class:`CiscoBfdSessDiscMapEntry <ydk.models.ietf.CISCO_IETF_BFD_MIB.CISCOIETFBFDMIB.CiscoBfdSessDiscMapTable.CiscoBfdSessDiscMapEntry>`
        
        

        """

        _prefix = 'cisco-ietf'
        _revision = '2011-04-16'

        def __init__(self):
            self.parent = None
            self.ciscobfdsessdiscmapentry = YList()
            self.ciscobfdsessdiscmapentry.parent = self
            self.ciscobfdsessdiscmapentry.name = 'ciscobfdsessdiscmapentry'


        class CiscoBfdSessDiscMapEntry(object):
            """
            Each row contains a mapping between a local discriminator
            value to an entry in ciscoBfdSessTable.
            
            .. attribute:: ciscobfdsessdiscriminator
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: ciscobfdsessdiscmapindex
            
            	This object indicates the CiscoBfdSessIndexTC referred to by the index of this row. In essence, a mapping is  provided between this index and the ciscoBfdSessTable
            	**type**\: int
            
            	**range:** 1..4294967295
            
            

            """

            _prefix = 'cisco-ietf'
            _revision = '2011-04-16'

            def __init__(self):
                self.parent = None
                self.ciscobfdsessdiscriminator = None
                self.ciscobfdsessdiscmapindex = None

            @property
            def _common_path(self):
                if self.ciscobfdsessdiscriminator is None:
                    raise YPYDataValidationError('Key property ciscobfdsessdiscriminator is None')

                return '/CISCO-IETF-BFD-MIB:CISCO-IETF-BFD-MIB/CISCO-IETF-BFD-MIB:ciscoBfdSessDiscMapTable/CISCO-IETF-BFD-MIB:ciscoBfdSessDiscMapEntry[CISCO-IETF-BFD-MIB:ciscoBfdSessDiscriminator = ' + str(self.ciscobfdsessdiscriminator) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ciscobfdsessdiscriminator is not None:
                    return True

                if self.ciscobfdsessdiscmapindex is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _CISCO_IETF_BFD_MIB as meta
                return meta._meta_table['CISCOIETFBFDMIB.CiscoBfdSessDiscMapTable.CiscoBfdSessDiscMapEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IETF-BFD-MIB:CISCO-IETF-BFD-MIB/CISCO-IETF-BFD-MIB:ciscoBfdSessDiscMapTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ciscobfdsessdiscmapentry is not None:
                for child_ref in self.ciscobfdsessdiscmapentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _CISCO_IETF_BFD_MIB as meta
            return meta._meta_table['CISCOIETFBFDMIB.CiscoBfdSessDiscMapTable']['meta_info']


    class CiscoBfdSessIpMapTable(object):
        """
        The BFD Session IP Mapping Table maps given
        ciscoBfdSessInterface, ciscoBfdSessAddrType, and
        ciscoBbfdSessAddr to an associated BFD sessions'
        CiscoBfdSessIndexTC used in the ciscoBfdSessTable.
        This table SHOULD contains those BFD sessions are
        of IP type\: singleHop(1) and multiHop(2).
        
        .. attribute:: ciscobfdsessipmapentry
        
        	Each row contains a mapping between ciscoBfdSessInterface, ciscoBfdSessAddrType and ciscoBfdSessAddr values to an  entry in ciscoBfdSessTable
        	**type**\: list of :py:class:`CiscoBfdSessIpMapEntry <ydk.models.ietf.CISCO_IETF_BFD_MIB.CISCOIETFBFDMIB.CiscoBfdSessIpMapTable.CiscoBfdSessIpMapEntry>`
        
        

        """

        _prefix = 'cisco-ietf'
        _revision = '2011-04-16'

        def __init__(self):
            self.parent = None
            self.ciscobfdsessipmapentry = YList()
            self.ciscobfdsessipmapentry.parent = self
            self.ciscobfdsessipmapentry.name = 'ciscobfdsessipmapentry'


        class CiscoBfdSessIpMapEntry(object):
            """
            Each row contains a mapping between ciscoBfdSessInterface,
            ciscoBfdSessAddrType and ciscoBfdSessAddr values to an 
            entry in ciscoBfdSessTable.
            
            .. attribute:: ciscobfdsessaddr
            
            	
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: ciscobfdsessaddrtype
            
            	
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: ciscobfdsessinterface
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: ciscobfdsessipmapindex
            
            	This object indicates the CiscoBfdSessIndexTC referred to by the indices of this row. In essence, a mapping is  provided between these indices and an entry in ciscoBfdSessTable
            	**type**\: int
            
            	**range:** 1..4294967295
            
            

            """

            _prefix = 'cisco-ietf'
            _revision = '2011-04-16'

            def __init__(self):
                self.parent = None
                self.ciscobfdsessaddr = None
                self.ciscobfdsessaddrtype = None
                self.ciscobfdsessinterface = None
                self.ciscobfdsessipmapindex = None

            @property
            def _common_path(self):
                if self.ciscobfdsessaddr is None:
                    raise YPYDataValidationError('Key property ciscobfdsessaddr is None')
                if self.ciscobfdsessaddrtype is None:
                    raise YPYDataValidationError('Key property ciscobfdsessaddrtype is None')
                if self.ciscobfdsessinterface is None:
                    raise YPYDataValidationError('Key property ciscobfdsessinterface is None')

                return '/CISCO-IETF-BFD-MIB:CISCO-IETF-BFD-MIB/CISCO-IETF-BFD-MIB:ciscoBfdSessIpMapTable/CISCO-IETF-BFD-MIB:ciscoBfdSessIpMapEntry[CISCO-IETF-BFD-MIB:ciscoBfdSessAddr = ' + str(self.ciscobfdsessaddr) + '][CISCO-IETF-BFD-MIB:ciscoBfdSessAddrType = ' + str(self.ciscobfdsessaddrtype) + '][CISCO-IETF-BFD-MIB:ciscoBfdSessInterface = ' + str(self.ciscobfdsessinterface) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ciscobfdsessaddr is not None:
                    return True

                if self.ciscobfdsessaddrtype is not None:
                    return True

                if self.ciscobfdsessinterface is not None:
                    return True

                if self.ciscobfdsessipmapindex is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _CISCO_IETF_BFD_MIB as meta
                return meta._meta_table['CISCOIETFBFDMIB.CiscoBfdSessIpMapTable.CiscoBfdSessIpMapEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IETF-BFD-MIB:CISCO-IETF-BFD-MIB/CISCO-IETF-BFD-MIB:ciscoBfdSessIpMapTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ciscobfdsessipmapentry is not None:
                for child_ref in self.ciscobfdsessipmapentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _CISCO_IETF_BFD_MIB as meta
            return meta._meta_table['CISCOIETFBFDMIB.CiscoBfdSessIpMapTable']['meta_info']


    class CiscoBfdSessMapTable(object):
        """
        The BFD Session Mapping Table maps the complex
        indexing of the BFD sessions to the flat 
        CiscoBfdSessIndexTC used in the ciscoBfdSessTable.
        
        .. attribute:: ciscobfdsessmapentry
        
        	The BFD Session Entry describes BFD session that is mapped to this index
        	**type**\: list of :py:class:`CiscoBfdSessMapEntry <ydk.models.ietf.CISCO_IETF_BFD_MIB.CISCOIETFBFDMIB.CiscoBfdSessMapTable.CiscoBfdSessMapEntry>`
        
        

        """

        _prefix = 'cisco-ietf'
        _revision = '2011-04-16'

        def __init__(self):
            self.parent = None
            self.ciscobfdsessmapentry = YList()
            self.ciscobfdsessmapentry.parent = self
            self.ciscobfdsessmapentry.name = 'ciscobfdsessmapentry'


        class CiscoBfdSessMapEntry(object):
            """
            The BFD Session Entry describes BFD session
            that is mapped to this index.
            
            .. attribute:: ciscobfdsessaddr
            
            	
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: ciscobfdsessaddrtype
            
            	
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: ciscobfdsessapplicationid
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscobfdsessdiscriminator
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: ciscobfdsessmapbfdindex
            
            	This object indicates the CiscoBfdSessIndexTC referred to by the indices of this row. In essence, a mapping is  provided between these indices and the ciscoBfdSessTable
            	**type**\: int
            
            	**range:** 1..4294967295
            
            

            """

            _prefix = 'cisco-ietf'
            _revision = '2011-04-16'

            def __init__(self):
                self.parent = None
                self.ciscobfdsessaddr = None
                self.ciscobfdsessaddrtype = None
                self.ciscobfdsessapplicationid = None
                self.ciscobfdsessdiscriminator = None
                self.ciscobfdsessmapbfdindex = None

            @property
            def _common_path(self):
                if self.ciscobfdsessaddr is None:
                    raise YPYDataValidationError('Key property ciscobfdsessaddr is None')
                if self.ciscobfdsessaddrtype is None:
                    raise YPYDataValidationError('Key property ciscobfdsessaddrtype is None')
                if self.ciscobfdsessapplicationid is None:
                    raise YPYDataValidationError('Key property ciscobfdsessapplicationid is None')
                if self.ciscobfdsessdiscriminator is None:
                    raise YPYDataValidationError('Key property ciscobfdsessdiscriminator is None')

                return '/CISCO-IETF-BFD-MIB:CISCO-IETF-BFD-MIB/CISCO-IETF-BFD-MIB:ciscoBfdSessMapTable/CISCO-IETF-BFD-MIB:ciscoBfdSessMapEntry[CISCO-IETF-BFD-MIB:ciscoBfdSessAddr = ' + str(self.ciscobfdsessaddr) + '][CISCO-IETF-BFD-MIB:ciscoBfdSessAddrType = ' + str(self.ciscobfdsessaddrtype) + '][CISCO-IETF-BFD-MIB:ciscoBfdSessApplicationId = ' + str(self.ciscobfdsessapplicationid) + '][CISCO-IETF-BFD-MIB:ciscoBfdSessDiscriminator = ' + str(self.ciscobfdsessdiscriminator) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ciscobfdsessaddr is not None:
                    return True

                if self.ciscobfdsessaddrtype is not None:
                    return True

                if self.ciscobfdsessapplicationid is not None:
                    return True

                if self.ciscobfdsessdiscriminator is not None:
                    return True

                if self.ciscobfdsessmapbfdindex is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _CISCO_IETF_BFD_MIB as meta
                return meta._meta_table['CISCOIETFBFDMIB.CiscoBfdSessMapTable.CiscoBfdSessMapEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IETF-BFD-MIB:CISCO-IETF-BFD-MIB/CISCO-IETF-BFD-MIB:ciscoBfdSessMapTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ciscobfdsessmapentry is not None:
                for child_ref in self.ciscobfdsessmapentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _CISCO_IETF_BFD_MIB as meta
            return meta._meta_table['CISCOIETFBFDMIB.CiscoBfdSessMapTable']['meta_info']


    class CiscoBfdSessTable(object):
        """
        The BFD Session Table describes the BFD sessions.
        
        .. attribute:: ciscobfdsessentry
        
        	The BFD Session Entry describes BFD session
        	**type**\: list of :py:class:`CiscoBfdSessEntry <ydk.models.ietf.CISCO_IETF_BFD_MIB.CISCOIETFBFDMIB.CiscoBfdSessTable.CiscoBfdSessEntry>`
        
        

        """

        _prefix = 'cisco-ietf'
        _revision = '2011-04-16'

        def __init__(self):
            self.parent = None
            self.ciscobfdsessentry = YList()
            self.ciscobfdsessentry.parent = self
            self.ciscobfdsessentry.name = 'ciscobfdsessentry'


        class CiscoBfdSessEntry(object):
            """
            The BFD Session Entry describes BFD session.
            
            .. attribute:: ciscobfdsessindex
            
            	This object contains an index used to represent a unique BFD session on this device
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: ciscobfdsessaddr
            
            	This object specifies the neighboring IP address which is being monitored with this BFD session. It can also be used to enabled BFD on a specific   interface. The value is set to zero when BFD session is not   associated with a specific interface
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: ciscobfdsessaddrtype
            
            	This object specifies IP address type of the neighboring IP address which is being monitored with this BFD session.  Only values unknown(0), ipv4(1) or ipv6(2)  have to be supported.    A value of unknown(0) is allowed only when   the outgoing interface is of type point\-to\-point, or  when the BFD session is not associated with a specific   interface.   If any other unsupported values are attempted in a set  operation, the agent MUST return an inconsistentValue   error
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: ciscobfdsessapplicationid
            
            	This object contains an index used to indicate a local application which owns or maintains this  BFD session. For instance, the MPLS VPN process may  maintain a subset of the total number of BFD  sessions.  This application ID provides a convenient  way to segregate sessions by the applications which  maintain them
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscobfdsessauthenticationtype
            
            	The Authentication Type used for this BFD session. This field is valid only when the Authentication Present bit is set
            	**type**\: :py:class:`CiscoBfdSessAuthenticationType_Enum <ydk.models.ietf.CISCO_IETF_BFD_MIB.CISCOIETFBFDMIB.CiscoBfdSessTable.CiscoBfdSessEntry.CiscoBfdSessAuthenticationType_Enum>`
            
            .. attribute:: ciscobfdsessauthpresflag
            
            	This object indicates that the local system's desire to use Authentication. Specifically, it is set   to true(1) if the local system wishes the session   to be authenticated or false(0) if not
            	**type**\: bool
            
            .. attribute:: ciscobfdsesscontrolplanindepflag
            
            	This object indicates that the local system's ability to continue to function through a disruption of   the control plane. Specifically, it is set   to true(1) if the local system BFD implementation is  independent of the control plane. Otherwise, the   value is set to false(0)
            	**type**\: bool
            
            .. attribute:: ciscobfdsessdemandmodedesiredflag
            
            	This object indicates that the local system's desire to use Demand mode. Specifically, it is set   to true(1) if the local system wishes to use   Demand mode or false(0) if not
            	**type**\: bool
            
            .. attribute:: ciscobfdsessdesiredmintxinterval
            
            	This object specifies the minimum interval, in microseconds, that the local system would like to use when       transmitting BFD Control packets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscobfdsessdetectmult
            
            	This object specifies the Detect time multiplier
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscobfdsessdiag
            
            	A diagnostic code specifying the local system's reason for the last transition of the session from up(1)   to some other state
            	**type**\: :py:class:`CiscoBfdDiag_Enum <ydk.models.ietf.CISCO_IETF_BFD_MIB.CiscoBfdDiag_Enum>`
            
            .. attribute:: ciscobfdsessdiscriminator
            
            	This object specifies the local discriminator for this BFD session, used to uniquely identify it
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: ciscobfdsessechofuncmodedesiredflag
            
            	This object indicates that the local system's desire to use Echo mode. Specifically, it is set   to true(1) if the local system wishes to use   Echo mode or false(0) if not
            	**type**\: bool
            
            .. attribute:: ciscobfdsessinterface
            
            	This object contains an interface index used to indicate the interface which this BFD session is running on
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: ciscobfdsessopermode
            
            	This object specifies current operating mode that BFD session is operating in
            	**type**\: :py:class:`CiscoBfdSessOperMode_Enum <ydk.models.ietf.CISCO_IETF_BFD_MIB.CISCOIETFBFDMIB.CiscoBfdSessTable.CiscoBfdSessEntry.CiscoBfdSessOperMode_Enum>`
            
            .. attribute:: ciscobfdsessperfdisctime
            
            	The value of sysUpTime on the most recent occasion at which any one or more of the session counters suffered  a discontinuity.    The relevant counters are the specific instances associated   with this BFD session of any Counter32 object contained in  the ciscoBfdSessPerfTable. If no such discontinuities have occurred   since the last re\-initialization of the local management  subsystem, then this object contains a zero value
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscobfdsessperflastcommlostdiag
            
            	The BFD diag code for the last time communication was lost with the neighbor. If no such down event exists this object   contains a zero value
            	**type**\: :py:class:`CiscoBfdDiag_Enum <ydk.models.ietf.CISCO_IETF_BFD_MIB.CiscoBfdDiag_Enum>`
            
            .. attribute:: ciscobfdsessperflastsessdowntime
            
            	The value of sysUpTime on the most recent occasion at which the last time communication was lost with the neighbor. If   no such down event exist this object contains a zero value
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscobfdsessperfpktin
            
            	The total number of BFD messages received for this BFD session
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscobfdsessperfpktinhc
            
            	This value represents the total number of BFD messages received for this BFD session. It MUST be equal to the  least significant 32 bits of ciscoBfdSessPerfPktIn  if ciscoBfdSessPerfPktInHC is supported according to  the rules spelled out in RFC2863
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ciscobfdsessperfpktout
            
            	The total number of BFD messages sent for this BFD session
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscobfdsessperfpktouthc
            
            	This value represents the total number of total number of BFD messages transmitted for this   BFD session. It MUST be equal to the  least significant 32 bits of ciscoBfdSessPerfPktIn  if ciscoBfdSessPerfPktOutHC is supported according to  the rules spelled out in RFC2863
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ciscobfdsessperfsessupcount
            
            	The number of times this session has gone into the Up state since the router last rebooted
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscobfdsessremotediscr
            
            	This object specifies the session discriminator chosen by the remote system for this BFD session
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscobfdsessremoteheardflag
            
            	This object specifies status of BFD packet reception from the remote system. Specifically, it is set to true(1) if  the local system is actively receiving BFD packets from the   remote system, and is set to false(0) if the local system   has not received BFD packets recently (within the detection   time) or if the local system is attempting to tear down  the BFD session
            	**type**\: bool
            
            .. attribute:: ciscobfdsessreqminechorxinterval
            
            	This object specifies the minimum interval, in microseconds, between received BFD Echo packets that this  system is capable of supporting
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscobfdsessreqminrxinterval
            
            	This object specifies the minimum interval, in microseconds, between received  BFD Control packets the   local system is capable of supporting
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscobfdsessrowstatus
            
            	This variable is used to create, modify, and/or delete a row in this table. When a row in this  table has a row in the active(1) state, no   objects in this row can be modified except the  ciscoBfdSessRowStatus and ciscoBfdSessStorageType
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: ciscobfdsessstate
            
            	The perceived state of the BFD session
            	**type**\: :py:class:`CiscoBfdSessState_Enum <ydk.models.ietf.CISCO_IETF_BFD_MIB.CISCOIETFBFDMIB.CiscoBfdSessTable.CiscoBfdSessEntry.CiscoBfdSessState_Enum>`
            
            .. attribute:: ciscobfdsessstortype
            
            	This variable indicates the storage type for this object. Conceptual rows having the value   'permanent' need not allow write\-access to any   columnar objects in the row
            	**type**\: :py:class:`StorageType_Enum <ydk.models.snmpv2.SNMPv2_TC.StorageType_Enum>`
            
            .. attribute:: ciscobfdsesstype
            
            	The type of this BFD session
            	**type**\: :py:class:`CiscoBfdSessType_Enum <ydk.models.ietf.CISCO_IETF_BFD_MIB.CISCOIETFBFDMIB.CiscoBfdSessTable.CiscoBfdSessEntry.CiscoBfdSessType_Enum>`
            
            .. attribute:: ciscobfdsessudpport
            
            	The destination UDP Port for BFD. The default value is the well\-known value for this port. BFD State failing(5) is only applicable if this BFD session is running version 0
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: ciscobfdsessuptime
            
            	The value of sysUpTime on the most recent occasion at which the session came up. If no such up event exists this object  contains a zero value
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscobfdsessversionnumber
            
            	The version number of the BFD protocol that this session is running in
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-ietf'
            _revision = '2011-04-16'

            def __init__(self):
                self.parent = None
                self.ciscobfdsessindex = None
                self.ciscobfdsessaddr = None
                self.ciscobfdsessaddrtype = None
                self.ciscobfdsessapplicationid = None
                self.ciscobfdsessauthenticationtype = None
                self.ciscobfdsessauthpresflag = None
                self.ciscobfdsesscontrolplanindepflag = None
                self.ciscobfdsessdemandmodedesiredflag = None
                self.ciscobfdsessdesiredmintxinterval = None
                self.ciscobfdsessdetectmult = None
                self.ciscobfdsessdiag = None
                self.ciscobfdsessdiscriminator = None
                self.ciscobfdsessechofuncmodedesiredflag = None
                self.ciscobfdsessinterface = None
                self.ciscobfdsessopermode = None
                self.ciscobfdsessperfdisctime = None
                self.ciscobfdsessperflastcommlostdiag = None
                self.ciscobfdsessperflastsessdowntime = None
                self.ciscobfdsessperfpktin = None
                self.ciscobfdsessperfpktinhc = None
                self.ciscobfdsessperfpktout = None
                self.ciscobfdsessperfpktouthc = None
                self.ciscobfdsessperfsessupcount = None
                self.ciscobfdsessremotediscr = None
                self.ciscobfdsessremoteheardflag = None
                self.ciscobfdsessreqminechorxinterval = None
                self.ciscobfdsessreqminrxinterval = None
                self.ciscobfdsessrowstatus = None
                self.ciscobfdsessstate = None
                self.ciscobfdsessstortype = None
                self.ciscobfdsesstype = None
                self.ciscobfdsessudpport = None
                self.ciscobfdsessuptime = None
                self.ciscobfdsessversionnumber = None

            class CiscoBfdSessAuthenticationType_Enum(Enum):
                """
                CiscoBfdSessAuthenticationType_Enum

                The Authentication Type used for this BFD session. This
                field is valid only when the Authentication Present bit is set

                """

                SIMPLEPASSWORD = 1

                KEYEDMD5 = 2

                METICULOUSKEYEDMD5 = 3

                KEYEDSHA1 = 4

                METICULOUSKEYEDSHA1 = 5


                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _CISCO_IETF_BFD_MIB as meta
                    return meta._meta_table['CISCOIETFBFDMIB.CiscoBfdSessTable.CiscoBfdSessEntry.CiscoBfdSessAuthenticationType_Enum']


            class CiscoBfdSessOperMode_Enum(Enum):
                """
                CiscoBfdSessOperMode_Enum

                This object specifies current operating mode that BFD
                session is operating in.

                """

                ASYNCMODEWECHOFUN = 1

                ASYNCHMODEWOECHOFUN = 2

                DEMANDMODEWECHOFUNCTION = 3

                DEMANDMODEWOECHOFUNCTION = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _CISCO_IETF_BFD_MIB as meta
                    return meta._meta_table['CISCOIETFBFDMIB.CiscoBfdSessTable.CiscoBfdSessEntry.CiscoBfdSessOperMode_Enum']


            class CiscoBfdSessState_Enum(Enum):
                """
                CiscoBfdSessState_Enum

                The perceived state of the BFD session.

                """

                ADMINDOWN = 1

                DOWN = 2

                INIT = 3

                UP = 4

                FAILING = 5


                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _CISCO_IETF_BFD_MIB as meta
                    return meta._meta_table['CISCOIETFBFDMIB.CiscoBfdSessTable.CiscoBfdSessEntry.CiscoBfdSessState_Enum']


            class CiscoBfdSessType_Enum(Enum):
                """
                CiscoBfdSessType_Enum

                The type of this BFD session.

                """

                SINGLEHOP = 1

                MULTIHOP = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _CISCO_IETF_BFD_MIB as meta
                    return meta._meta_table['CISCOIETFBFDMIB.CiscoBfdSessTable.CiscoBfdSessEntry.CiscoBfdSessType_Enum']


            @property
            def _common_path(self):
                if self.ciscobfdsessindex is None:
                    raise YPYDataValidationError('Key property ciscobfdsessindex is None')

                return '/CISCO-IETF-BFD-MIB:CISCO-IETF-BFD-MIB/CISCO-IETF-BFD-MIB:ciscoBfdSessTable/CISCO-IETF-BFD-MIB:ciscoBfdSessEntry[CISCO-IETF-BFD-MIB:ciscoBfdSessIndex = ' + str(self.ciscobfdsessindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ciscobfdsessindex is not None:
                    return True

                if self.ciscobfdsessaddr is not None:
                    return True

                if self.ciscobfdsessaddrtype is not None:
                    return True

                if self.ciscobfdsessapplicationid is not None:
                    return True

                if self.ciscobfdsessauthenticationtype is not None:
                    return True

                if self.ciscobfdsessauthpresflag is not None:
                    return True

                if self.ciscobfdsesscontrolplanindepflag is not None:
                    return True

                if self.ciscobfdsessdemandmodedesiredflag is not None:
                    return True

                if self.ciscobfdsessdesiredmintxinterval is not None:
                    return True

                if self.ciscobfdsessdetectmult is not None:
                    return True

                if self.ciscobfdsessdiag is not None:
                    return True

                if self.ciscobfdsessdiscriminator is not None:
                    return True

                if self.ciscobfdsessechofuncmodedesiredflag is not None:
                    return True

                if self.ciscobfdsessinterface is not None:
                    return True

                if self.ciscobfdsessopermode is not None:
                    return True

                if self.ciscobfdsessperfdisctime is not None:
                    return True

                if self.ciscobfdsessperflastcommlostdiag is not None:
                    return True

                if self.ciscobfdsessperflastsessdowntime is not None:
                    return True

                if self.ciscobfdsessperfpktin is not None:
                    return True

                if self.ciscobfdsessperfpktinhc is not None:
                    return True

                if self.ciscobfdsessperfpktout is not None:
                    return True

                if self.ciscobfdsessperfpktouthc is not None:
                    return True

                if self.ciscobfdsessperfsessupcount is not None:
                    return True

                if self.ciscobfdsessremotediscr is not None:
                    return True

                if self.ciscobfdsessremoteheardflag is not None:
                    return True

                if self.ciscobfdsessreqminechorxinterval is not None:
                    return True

                if self.ciscobfdsessreqminrxinterval is not None:
                    return True

                if self.ciscobfdsessrowstatus is not None:
                    return True

                if self.ciscobfdsessstate is not None:
                    return True

                if self.ciscobfdsessstortype is not None:
                    return True

                if self.ciscobfdsesstype is not None:
                    return True

                if self.ciscobfdsessudpport is not None:
                    return True

                if self.ciscobfdsessuptime is not None:
                    return True

                if self.ciscobfdsessversionnumber is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _CISCO_IETF_BFD_MIB as meta
                return meta._meta_table['CISCOIETFBFDMIB.CiscoBfdSessTable.CiscoBfdSessEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IETF-BFD-MIB:CISCO-IETF-BFD-MIB/CISCO-IETF-BFD-MIB:ciscoBfdSessTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ciscobfdsessentry is not None:
                for child_ref in self.ciscobfdsessentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _CISCO_IETF_BFD_MIB as meta
            return meta._meta_table['CISCOIETFBFDMIB.CiscoBfdSessTable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-IETF-BFD-MIB:CISCO-IETF-BFD-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.ciscobfdscalarobjects is not None and self.ciscobfdscalarobjects._has_data():
            return True

        if self.ciscobfdscalarobjects is not None and self.ciscobfdscalarobjects.is_presence():
            return True

        if self.ciscobfdsessdiscmaptable is not None and self.ciscobfdsessdiscmaptable._has_data():
            return True

        if self.ciscobfdsessdiscmaptable is not None and self.ciscobfdsessdiscmaptable.is_presence():
            return True

        if self.ciscobfdsessipmaptable is not None and self.ciscobfdsessipmaptable._has_data():
            return True

        if self.ciscobfdsessipmaptable is not None and self.ciscobfdsessipmaptable.is_presence():
            return True

        if self.ciscobfdsessmaptable is not None and self.ciscobfdsessmaptable._has_data():
            return True

        if self.ciscobfdsessmaptable is not None and self.ciscobfdsessmaptable.is_presence():
            return True

        if self.ciscobfdsesstable is not None and self.ciscobfdsesstable._has_data():
            return True

        if self.ciscobfdsesstable is not None and self.ciscobfdsesstable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _CISCO_IETF_BFD_MIB as meta
        return meta._meta_table['CISCOIETFBFDMIB']['meta_info']


