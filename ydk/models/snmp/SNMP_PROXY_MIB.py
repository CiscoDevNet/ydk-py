""" SNMP_PROXY_MIB 

This MIB module defines MIB objects which provide
mechanisms to remotely configure the parameters
used by a proxy forwarding application.

Copyright (C) The Internet Society (2002). This
version of this MIB module is part of RFC 3413;
see the RFC itself for full legal notices.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.snmpv2.SNMPv2_TC import RowStatus_Enum
from ydk.models.snmpv2.SNMPv2_TC import StorageType_Enum


class SNMPPROXYMIB(object):
    """
    
    
    .. attribute:: snmpproxytable
    
    	The table of translation parameters used by proxy forwarder applications for forwarding SNMP messages
    	**type**\: :py:class:`SnmpProxyTable <ydk.models.snmp.SNMP_PROXY_MIB.SNMPPROXYMIB.SnmpProxyTable>`
    
    

    """

    _prefix = 'snmp-proxy'
    _revision = '2002-10-14'

    def __init__(self):
        self.snmpproxytable = SNMPPROXYMIB.SnmpProxyTable()
        self.snmpproxytable.parent = self


    class SnmpProxyTable(object):
        """
        The table of translation parameters used by proxy forwarder
        applications for forwarding SNMP messages.
        
        .. attribute:: snmpproxyentry
        
        	A set of translation parameters used by a proxy forwarder application for forwarding SNMP messages.  Entries in the snmpProxyTable are created and deleted using the snmpProxyRowStatus object
        	**type**\: list of :py:class:`SnmpProxyEntry <ydk.models.snmp.SNMP_PROXY_MIB.SNMPPROXYMIB.SnmpProxyTable.SnmpProxyEntry>`
        
        

        """

        _prefix = 'snmp-proxy'
        _revision = '2002-10-14'

        def __init__(self):
            self.parent = None
            self.snmpproxyentry = YList()
            self.snmpproxyentry.parent = self
            self.snmpproxyentry.name = 'snmpproxyentry'


        class SnmpProxyEntry(object):
            """
            A set of translation parameters used by a proxy forwarder
            application for forwarding SNMP messages.
            
            Entries in the snmpProxyTable are created and deleted
            using the snmpProxyRowStatus object.
            
            .. attribute:: snmpproxyname
            
            	The locally arbitrary, but unique identifier associated with this snmpProxyEntry
            	**type**\: str
            
            	**range:** 1..32
            
            .. attribute:: snmpproxycontextengineid
            
            	The contextEngineID contained in messages that may be forwarded using the translation parameters defined by this entry
            	**type**\: str
            
            	**pattern:** (([0\-9a\-fA\-F]){2}(\:([0\-9a\-fA\-F]){2})\*)?
            
            .. attribute:: snmpproxycontextname
            
            	The contextName contained in messages that may be forwarded using the translation parameters defined by this entry.  This object is optional, and if not supported, the contextName contained in a message is ignored when selecting an entry in the snmpProxyTable
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: snmpproxymultipletargetout
            
            	This object selects a set of management targets defined in the snmpTargetAddrTable (in the SNMP\-TARGET\-MIB).  This object is only used when selection of multiple targets is required (i.e. when forwarding an incoming notification)
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: snmpproxyrowstatus
            
            	The status of this conceptual row.  To create a row in this table, a manager must set this object to either createAndGo(4) or createAndWait(5).  The following objects may not be modified while the value of this object is active(1)\:     \- snmpProxyType     \- snmpProxyContextEngineID     \- snmpProxyContextName     \- snmpProxyTargetParamsIn     \- snmpProxySingleTargetOut     \- snmpProxyMultipleTargetOut
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: snmpproxysingletargetout
            
            	This object selects a management target defined in the snmpTargetAddrTable (in the SNMP\-TARGET\-MIB).  The selected target is defined by an entry in the snmpTargetAddrTable whose index value (snmpTargetAddrName) is equal to this object.  This object is only used when selection of a single target is required (i.e. when forwarding an incoming read or write request)
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: snmpproxystoragetype
            
            	The storage type of this conceptual row. Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\: :py:class:`StorageType_Enum <ydk.models.snmpv2.SNMPv2_TC.StorageType_Enum>`
            
            .. attribute:: snmpproxytargetparamsin
            
            	This object selects an entry in the snmpTargetParamsTable. The selected entry is used to determine which row of the snmpProxyTable to use for forwarding received messages
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: snmpproxytype
            
            	The type of message that may be forwarded using the translation parameters defined by this entry
            	**type**\: :py:class:`SnmpProxyType_Enum <ydk.models.snmp.SNMP_PROXY_MIB.SNMPPROXYMIB.SnmpProxyTable.SnmpProxyEntry.SnmpProxyType_Enum>`
            
            

            """

            _prefix = 'snmp-proxy'
            _revision = '2002-10-14'

            def __init__(self):
                self.parent = None
                self.snmpproxyname = None
                self.snmpproxycontextengineid = None
                self.snmpproxycontextname = None
                self.snmpproxymultipletargetout = None
                self.snmpproxyrowstatus = None
                self.snmpproxysingletargetout = None
                self.snmpproxystoragetype = None
                self.snmpproxytargetparamsin = None
                self.snmpproxytype = None

            class SnmpProxyType_Enum(Enum):
                """
                SnmpProxyType_Enum

                The type of message that may be forwarded using
                the translation parameters defined by this entry.

                """

                READ = 1

                WRITE = 2

                TRAP = 3

                INFORM = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.snmp._meta import _SNMP_PROXY_MIB as meta
                    return meta._meta_table['SNMPPROXYMIB.SnmpProxyTable.SnmpProxyEntry.SnmpProxyType_Enum']


            @property
            def _common_path(self):
                if self.snmpproxyname is None:
                    raise YPYDataValidationError('Key property snmpproxyname is None')

                return '/SNMP-PROXY-MIB:SNMP-PROXY-MIB/SNMP-PROXY-MIB:snmpProxyTable/SNMP-PROXY-MIB:snmpProxyEntry[SNMP-PROXY-MIB:snmpProxyName = ' + str(self.snmpproxyname) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.snmpproxyname is not None:
                    return True

                if self.snmpproxycontextengineid is not None:
                    return True

                if self.snmpproxycontextname is not None:
                    return True

                if self.snmpproxymultipletargetout is not None:
                    return True

                if self.snmpproxyrowstatus is not None:
                    return True

                if self.snmpproxysingletargetout is not None:
                    return True

                if self.snmpproxystoragetype is not None:
                    return True

                if self.snmpproxytargetparamsin is not None:
                    return True

                if self.snmpproxytype is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.snmp._meta import _SNMP_PROXY_MIB as meta
                return meta._meta_table['SNMPPROXYMIB.SnmpProxyTable.SnmpProxyEntry']['meta_info']

        @property
        def _common_path(self):

            return '/SNMP-PROXY-MIB:SNMP-PROXY-MIB/SNMP-PROXY-MIB:snmpProxyTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.snmpproxyentry is not None:
                for child_ref in self.snmpproxyentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.snmp._meta import _SNMP_PROXY_MIB as meta
            return meta._meta_table['SNMPPROXYMIB.SnmpProxyTable']['meta_info']

    @property
    def _common_path(self):

        return '/SNMP-PROXY-MIB:SNMP-PROXY-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.snmpproxytable is not None and self.snmpproxytable._has_data():
            return True

        if self.snmpproxytable is not None and self.snmpproxytable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.snmp._meta import _SNMP_PROXY_MIB as meta
        return meta._meta_table['SNMPPROXYMIB']['meta_info']


