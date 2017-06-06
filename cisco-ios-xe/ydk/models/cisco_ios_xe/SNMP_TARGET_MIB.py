""" SNMP_TARGET_MIB 

This MIB module defines MIB objects which provide
mechanisms to remotely configure the parameters used
by an SNMP entity for the generation of SNMP messages.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class SnmpTargetMib(object):
    """
    
    
    .. attribute:: snmptargetaddrtable
    
    	A table of transport addresses to be used in the generation of SNMP messages
    	**type**\:   :py:class:`Snmptargetaddrtable <ydk.models.cisco_ios_xe.SNMP_TARGET_MIB.SnmpTargetMib.Snmptargetaddrtable>`
    
    .. attribute:: snmptargetobjects
    
    	
    	**type**\:   :py:class:`Snmptargetobjects <ydk.models.cisco_ios_xe.SNMP_TARGET_MIB.SnmpTargetMib.Snmptargetobjects>`
    
    .. attribute:: snmptargetparamstable
    
    	A table of SNMP target information to be used in the generation of SNMP messages
    	**type**\:   :py:class:`Snmptargetparamstable <ydk.models.cisco_ios_xe.SNMP_TARGET_MIB.SnmpTargetMib.Snmptargetparamstable>`
    
    

    """

    _prefix = 'SNMP-TARGET-MIB'
    _revision = '1998-08-04'

    def __init__(self):
        self.snmptargetaddrtable = SnmpTargetMib.Snmptargetaddrtable()
        self.snmptargetaddrtable.parent = self
        self.snmptargetobjects = SnmpTargetMib.Snmptargetobjects()
        self.snmptargetobjects.parent = self
        self.snmptargetparamstable = SnmpTargetMib.Snmptargetparamstable()
        self.snmptargetparamstable.parent = self


    class Snmptargetobjects(object):
        """
        
        
        .. attribute:: snmptargetspinlock
        
        	This object is used to facilitate modification of table entries in the SNMP\-TARGET\-MIB module by multiple      managers.  In particular, it is useful when modifying the value of the snmpTargetAddrTagList object.  The procedure for modifying the snmpTargetAddrTagList object is as follows\:      1.  Retrieve the value of snmpTargetSpinLock and         of snmpTargetAddrTagList.      2.  Generate a new value for snmpTargetAddrTagList.      3.  Set the value of snmpTargetSpinLock to the         retrieved value, and the value of         snmpTargetAddrTagList to the new value.  If         the set fails for the snmpTargetSpinLock         object, go back to step 1
        	**type**\:  int
        
        	**range:** 0..2147483647
        
        .. attribute:: snmpunavailablecontexts
        
        	The total number of packets received by the SNMP engine which were dropped because the context contained in the message was unavailable
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpunknowncontexts
        
        	The total number of packets received by the SNMP engine which were dropped because the context contained in the message was unknown
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'SNMP-TARGET-MIB'
        _revision = '1998-08-04'

        def __init__(self):
            self.parent = None
            self.snmptargetspinlock = None
            self.snmpunavailablecontexts = None
            self.snmpunknowncontexts = None

        @property
        def _common_path(self):

            return '/SNMP-TARGET-MIB:SNMP-TARGET-MIB/SNMP-TARGET-MIB:snmpTargetObjects'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.snmptargetspinlock is not None:
                return True

            if self.snmpunavailablecontexts is not None:
                return True

            if self.snmpunknowncontexts is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _SNMP_TARGET_MIB as meta
            return meta._meta_table['SnmpTargetMib.Snmptargetobjects']['meta_info']


    class Snmptargetaddrtable(object):
        """
        A table of transport addresses to be used in the generation
        of SNMP messages.
        
        .. attribute:: snmptargetaddrentry
        
        	A transport address to be used in the generation of SNMP operations.  Entries in the snmpTargetAddrTable are created and deleted using the snmpTargetAddrRowStatus object
        	**type**\: list of    :py:class:`Snmptargetaddrentry <ydk.models.cisco_ios_xe.SNMP_TARGET_MIB.SnmpTargetMib.Snmptargetaddrtable.Snmptargetaddrentry>`
        
        

        """

        _prefix = 'SNMP-TARGET-MIB'
        _revision = '1998-08-04'

        def __init__(self):
            self.parent = None
            self.snmptargetaddrentry = YList()
            self.snmptargetaddrentry.parent = self
            self.snmptargetaddrentry.name = 'snmptargetaddrentry'


        class Snmptargetaddrentry(object):
            """
            A transport address to be used in the generation
            of SNMP operations.
            
            Entries in the snmpTargetAddrTable are created and
            deleted using the snmpTargetAddrRowStatus object.
            
            .. attribute:: snmptargetaddrname  <key>
            
            	The locally arbitrary, but unique identifier associated with this snmpTargetAddrEntry
            	**type**\:  str
            
            	**length:** 1..32
            
            .. attribute:: snmptargetaddrparams
            
            	The value of this object identifies an entry in the snmpTargetParamsTable.  The identified entry contains SNMP parameters to be used when generating messages to be sent to this transport address
            	**type**\:  str
            
            	**length:** 1..32
            
            .. attribute:: snmptargetaddrretrycount
            
            	This object specifies a default number of retries to be attempted when a response is not received for a generated message.  An application may provide its own retry count, in which case the value of this object is ignored
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: snmptargetaddrrowstatus
            
            	The status of this conceptual row.  To create a row in this table, a manager must set this object to either createAndGo(4) or createAndWait(5).  Until instances of all corresponding columns are appropriately configured, the value of the corresponding instance of the snmpTargetAddrRowStatus column is 'notReady'.  In particular, a newly created row cannot be made active until the corresponding instances of snmpTargetAddrTDomain, snmpTargetAddrTAddress, and snmpTargetAddrParams have all been set.  The following objects may not be modified while the value of this object is active(1)\:     \- snmpTargetAddrTDomain     \- snmpTargetAddrTAddress An attempt to set these objects while the value of snmpTargetAddrRowStatus is active(1) will result in an inconsistentValue error
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: snmptargetaddrstoragetype
            
            	The storage type for this conceptual row
            	**type**\:   :py:class:`StoragetypeEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.StoragetypeEnum>`
            
            .. attribute:: snmptargetaddrtaddress
            
            	This object contains a transport address.  The format of this address depends on the value of the snmpTargetAddrTDomain object
            	**type**\:  str
            
            	**length:** 1..255
            
            .. attribute:: snmptargetaddrtaglist
            
            	This object contains a list of tag values which are used to select target addresses for a particular operation
            	**type**\:  str
            
            .. attribute:: snmptargetaddrtdomain
            
            	This object indicates the transport type of the address contained in the snmpTargetAddrTAddress object
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: snmptargetaddrtimeout
            
            	This object should reflect the expected maximum round trip time for communicating with the transport address defined by this row.  When a message is sent to this address, and a response (if one is expected) is not received within this time period, an implementation may assume that the response will not be delivered.  Note that the time interval that an application waits for a response may actually be derived from the value of this object.  The method for deriving the actual time interval is implementation dependent.  One such method      is to derive the expected round trip time based on a particular retransmission algorithm and on the number of timeouts which have occurred.  The type of message may also be considered when deriving expected round trip times for retransmissions.  For example, if a message is being sent with a securityLevel that indicates both authentication and privacy, the derived value may be increased to compensate for extra processing time spent during authentication and encryption processing
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            

            """

            _prefix = 'SNMP-TARGET-MIB'
            _revision = '1998-08-04'

            def __init__(self):
                self.parent = None
                self.snmptargetaddrname = None
                self.snmptargetaddrparams = None
                self.snmptargetaddrretrycount = None
                self.snmptargetaddrrowstatus = None
                self.snmptargetaddrstoragetype = None
                self.snmptargetaddrtaddress = None
                self.snmptargetaddrtaglist = None
                self.snmptargetaddrtdomain = None
                self.snmptargetaddrtimeout = None

            @property
            def _common_path(self):
                if self.snmptargetaddrname is None:
                    raise YPYModelError('Key property snmptargetaddrname is None')

                return '/SNMP-TARGET-MIB:SNMP-TARGET-MIB/SNMP-TARGET-MIB:snmpTargetAddrTable/SNMP-TARGET-MIB:snmpTargetAddrEntry[SNMP-TARGET-MIB:snmpTargetAddrName = ' + str(self.snmptargetaddrname) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.snmptargetaddrname is not None:
                    return True

                if self.snmptargetaddrparams is not None:
                    return True

                if self.snmptargetaddrretrycount is not None:
                    return True

                if self.snmptargetaddrrowstatus is not None:
                    return True

                if self.snmptargetaddrstoragetype is not None:
                    return True

                if self.snmptargetaddrtaddress is not None:
                    return True

                if self.snmptargetaddrtaglist is not None:
                    return True

                if self.snmptargetaddrtdomain is not None:
                    return True

                if self.snmptargetaddrtimeout is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _SNMP_TARGET_MIB as meta
                return meta._meta_table['SnmpTargetMib.Snmptargetaddrtable.Snmptargetaddrentry']['meta_info']

        @property
        def _common_path(self):

            return '/SNMP-TARGET-MIB:SNMP-TARGET-MIB/SNMP-TARGET-MIB:snmpTargetAddrTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.snmptargetaddrentry is not None:
                for child_ref in self.snmptargetaddrentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _SNMP_TARGET_MIB as meta
            return meta._meta_table['SnmpTargetMib.Snmptargetaddrtable']['meta_info']


    class Snmptargetparamstable(object):
        """
        A table of SNMP target information to be used
        in the generation of SNMP messages.
        
        .. attribute:: snmptargetparamsentry
        
        	A set of SNMP target information.  Entries in the snmpTargetParamsTable are created and deleted using the snmpTargetParamsRowStatus object
        	**type**\: list of    :py:class:`Snmptargetparamsentry <ydk.models.cisco_ios_xe.SNMP_TARGET_MIB.SnmpTargetMib.Snmptargetparamstable.Snmptargetparamsentry>`
        
        

        """

        _prefix = 'SNMP-TARGET-MIB'
        _revision = '1998-08-04'

        def __init__(self):
            self.parent = None
            self.snmptargetparamsentry = YList()
            self.snmptargetparamsentry.parent = self
            self.snmptargetparamsentry.name = 'snmptargetparamsentry'


        class Snmptargetparamsentry(object):
            """
            A set of SNMP target information.
            
            Entries in the snmpTargetParamsTable are created and
            deleted using the snmpTargetParamsRowStatus object.
            
            .. attribute:: snmptargetparamsname  <key>
            
            	The locally arbitrary, but unique identifier associated with this snmpTargetParamsEntry
            	**type**\:  str
            
            	**length:** 1..32
            
            .. attribute:: snmptargetparamsmpmodel
            
            	The Message Processing Model to be used when generating SNMP messages using this entry
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: snmptargetparamsrowstatus
            
            	The status of this conceptual row.  To create a row in this table, a manager must set this object to either createAndGo(4) or createAndWait(5).  Until instances of all corresponding columns are appropriately configured, the value of the corresponding instance of the snmpTargetParamsRowStatus column is 'notReady'.  In particular, a newly created row cannot be made      active until the corresponding snmpTargetParamsMPModel, snmpTargetParamsSecurityModel, snmpTargetParamsSecurityName, and snmpTargetParamsSecurityLevel have all been set. The following objects may not be modified while the value of this object is active(1)\:     \- snmpTargetParamsMPModel     \- snmpTargetParamsSecurityModel     \- snmpTargetParamsSecurityName     \- snmpTargetParamsSecurityLevel An attempt to set these objects while the value of snmpTargetParamsRowStatus is active(1) will result in an inconsistentValue error
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: snmptargetparamssecuritylevel
            
            	The Level of Security to be used when generating SNMP messages using this entry
            	**type**\:   :py:class:`SnmpsecuritylevelEnum <ydk.models.cisco_ios_xe.SNMP_FRAMEWORK_MIB.SnmpsecuritylevelEnum>`
            
            .. attribute:: snmptargetparamssecuritymodel
            
            	The Security Model to be used when generating SNMP messages using this entry.  An implementation may choose to return an inconsistentValue error if an attempt is made to set this variable to a value for a security model which the implementation does      not support
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: snmptargetparamssecurityname
            
            	The securityName which identifies the Principal on whose behalf SNMP messages will be generated using this entry
            	**type**\:  str
            
            .. attribute:: snmptargetparamsstoragetype
            
            	The storage type for this conceptual row
            	**type**\:   :py:class:`StoragetypeEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.StoragetypeEnum>`
            
            

            """

            _prefix = 'SNMP-TARGET-MIB'
            _revision = '1998-08-04'

            def __init__(self):
                self.parent = None
                self.snmptargetparamsname = None
                self.snmptargetparamsmpmodel = None
                self.snmptargetparamsrowstatus = None
                self.snmptargetparamssecuritylevel = None
                self.snmptargetparamssecuritymodel = None
                self.snmptargetparamssecurityname = None
                self.snmptargetparamsstoragetype = None

            @property
            def _common_path(self):
                if self.snmptargetparamsname is None:
                    raise YPYModelError('Key property snmptargetparamsname is None')

                return '/SNMP-TARGET-MIB:SNMP-TARGET-MIB/SNMP-TARGET-MIB:snmpTargetParamsTable/SNMP-TARGET-MIB:snmpTargetParamsEntry[SNMP-TARGET-MIB:snmpTargetParamsName = ' + str(self.snmptargetparamsname) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.snmptargetparamsname is not None:
                    return True

                if self.snmptargetparamsmpmodel is not None:
                    return True

                if self.snmptargetparamsrowstatus is not None:
                    return True

                if self.snmptargetparamssecuritylevel is not None:
                    return True

                if self.snmptargetparamssecuritymodel is not None:
                    return True

                if self.snmptargetparamssecurityname is not None:
                    return True

                if self.snmptargetparamsstoragetype is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _SNMP_TARGET_MIB as meta
                return meta._meta_table['SnmpTargetMib.Snmptargetparamstable.Snmptargetparamsentry']['meta_info']

        @property
        def _common_path(self):

            return '/SNMP-TARGET-MIB:SNMP-TARGET-MIB/SNMP-TARGET-MIB:snmpTargetParamsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.snmptargetparamsentry is not None:
                for child_ref in self.snmptargetparamsentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _SNMP_TARGET_MIB as meta
            return meta._meta_table['SnmpTargetMib.Snmptargetparamstable']['meta_info']

    @property
    def _common_path(self):

        return '/SNMP-TARGET-MIB:SNMP-TARGET-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.snmptargetaddrtable is not None and self.snmptargetaddrtable._has_data():
            return True

        if self.snmptargetobjects is not None and self.snmptargetobjects._has_data():
            return True

        if self.snmptargetparamstable is not None and self.snmptargetparamstable._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _SNMP_TARGET_MIB as meta
        return meta._meta_table['SnmpTargetMib']['meta_info']


