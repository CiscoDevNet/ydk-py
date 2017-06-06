""" MPLS_LDP_GENERIC_STD_MIB 

Copyright (C) The Internet Society (year). The
initial version of this MIB module was published
in RFC 3815. For full legal notices see the RFC
itself or see\:
http\://www.ietf.org/copyrights/ianamib.html

This MIB contains managed object definitions for
configuring and monitoring the Multiprotocol Label
Switching (MPLS), Label Distribution Protocol (LDP),
utilizing ethernet as the Layer 2 media.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class MplsLdpGenericStdMib(object):
    """
    
    
    .. attribute:: mplsldpentitygenericlrtable
    
    	The MPLS LDP Entity Generic Label Range (LR) Table.  The purpose of this table is to provide a mechanism for configurating a contiguous range of generic labels, or a 'label range' for LDP Entities.  LDP Entities which use Generic Labels must have at least one entry in this table.  In other words, this table 'extends' the mpldLdpEntityTable for Generic Labels
    	**type**\:   :py:class:`Mplsldpentitygenericlrtable <ydk.models.cisco_ios_xe.MPLS_LDP_GENERIC_STD_MIB.MplsLdpGenericStdMib.Mplsldpentitygenericlrtable>`
    
    

    """

    _prefix = 'MPLS-LDP-GENERIC-STD-MIB'
    _revision = '2004-06-03'

    def __init__(self):
        self.mplsldpentitygenericlrtable = MplsLdpGenericStdMib.Mplsldpentitygenericlrtable()
        self.mplsldpentitygenericlrtable.parent = self


    class Mplsldpentitygenericlrtable(object):
        """
        The MPLS LDP Entity Generic Label Range (LR)
        Table.
        
        The purpose of this table is to provide a mechanism
        for configurating a contiguous range of generic labels,
        or a 'label range' for LDP Entities.
        
        LDP Entities which use Generic Labels must have at least
        one entry in this table.  In other words, this table
        'extends' the mpldLdpEntityTable for Generic Labels.
        
        .. attribute:: mplsldpentitygenericlrentry
        
        	A row in the LDP Entity Generic Label Range (LR) Table.  One entry in this table contains information on a single range of labels represented by the configured Upper and Lower Bounds pairs.  NOTE\: there is NO corresponding LDP message which relates to the information in this table, however, this table does provide a way for a user to 'reserve' a generic label range.  NOTE\:  The ranges for a specific LDP Entity are UNIQUE and non\-overlapping.  A row will not be created unless a unique and non\-overlapping range is specified
        	**type**\: list of    :py:class:`Mplsldpentitygenericlrentry <ydk.models.cisco_ios_xe.MPLS_LDP_GENERIC_STD_MIB.MplsLdpGenericStdMib.Mplsldpentitygenericlrtable.Mplsldpentitygenericlrentry>`
        
        

        """

        _prefix = 'MPLS-LDP-GENERIC-STD-MIB'
        _revision = '2004-06-03'

        def __init__(self):
            self.parent = None
            self.mplsldpentitygenericlrentry = YList()
            self.mplsldpentitygenericlrentry.parent = self
            self.mplsldpentitygenericlrentry.name = 'mplsldpentitygenericlrentry'


        class Mplsldpentitygenericlrentry(object):
            """
            A row in the LDP Entity Generic Label
            Range (LR) Table.  One entry in this table contains
            information on a single range of labels
            represented by the configured Upper and Lower
            Bounds pairs.  NOTE\: there is NO corresponding
            LDP message which relates to the information
            in this table, however, this table does provide
            a way for a user to 'reserve' a generic label
            range.
            
            NOTE\:  The ranges for a specific LDP Entity
            are UNIQUE and non\-overlapping.
            
            A row will not be created unless a unique and
            non\-overlapping range is specified.
            
            .. attribute:: mplsldpentityldpid  <key>
            
            	
            	**type**\:  str
            
            	**refers to**\:  :py:class:`mplsldpentityldpid <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MplsLdpStdMib.Mplsldpentitytable.Mplsldpentityentry>`
            
            .. attribute:: mplsldpentityindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`mplsldpentityindex <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MplsLdpStdMib.Mplsldpentitytable.Mplsldpentityentry>`
            
            .. attribute:: mplsldpentitygenericlrmin  <key>
            
            	The minimum label configured for this range
            	**type**\:  int
            
            	**range:** 0..1048575
            
            .. attribute:: mplsldpentitygenericlrmax  <key>
            
            	The maximum label configured for this range
            	**type**\:  int
            
            	**range:** 0..1048575
            
            .. attribute:: mplsldpentitygenericifindexorzero
            
            	This value represents either the InterfaceIndex of the 'ifLayer' where these Generic Label would be created,   or 0 (zero).  The value of zero means that the InterfaceIndex is not known.  However, if the InterfaceIndex is known, then it must be represented by this value.  If an InterfaceIndex becomes known, then the network management entity (e.g., SNMP agent) responsible for this object MUST change the value from 0 (zero) to the value of the InterfaceIndex
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: mplsldpentitygenericlabelspace
            
            	This value of this object is perPlatform(1), then this means that the label space type is per platform.  If this object is perInterface(2), then this means that the label space type is per Interface
            	**type**\:   :py:class:`MplsldpentitygenericlabelspaceEnum <ydk.models.cisco_ios_xe.MPLS_LDP_GENERIC_STD_MIB.MplsLdpGenericStdMib.Mplsldpentitygenericlrtable.Mplsldpentitygenericlrentry.MplsldpentitygenericlabelspaceEnum>`
            
            .. attribute:: mplsldpentitygenericlrrowstatus
            
            	The status of this conceptual row.  All writable objects in this row may be modified at any time, however, as described in  detail in the section entitled, 'Changing Values After Session Establishment', and again described in the DESCRIPTION clause of the mplsLdpEntityAdminStatus object, if a session has been initiated with a Peer, changing objects in this table will wreak havoc with the session and interrupt traffic. To repeat again\:  the recommended procedure is to set the mplsLdpEntityAdminStatus to down, thereby explicitly causing a session to be torn down. Then, change objects in this entry, then set the mplsLdpEntityAdminStatus to enable which enables a new session to be initiated.  There must exist at least one entry in this table for every LDP Entity that has a generic label configured
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: mplsldpentitygenericlrstoragetype
            
            	The storage type for this conceptual row. Conceptual rows having the value 'permanent(4)' need not allow write\-access to any columnar objects in the row
            	**type**\:   :py:class:`StoragetypeEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.StoragetypeEnum>`
            
            

            """

            _prefix = 'MPLS-LDP-GENERIC-STD-MIB'
            _revision = '2004-06-03'

            def __init__(self):
                self.parent = None
                self.mplsldpentityldpid = None
                self.mplsldpentityindex = None
                self.mplsldpentitygenericlrmin = None
                self.mplsldpentitygenericlrmax = None
                self.mplsldpentitygenericifindexorzero = None
                self.mplsldpentitygenericlabelspace = None
                self.mplsldpentitygenericlrrowstatus = None
                self.mplsldpentitygenericlrstoragetype = None

            class MplsldpentitygenericlabelspaceEnum(Enum):
                """
                MplsldpentitygenericlabelspaceEnum

                This value of this object is perPlatform(1), then

                this means that the label space type is

                per platform.

                If this object is perInterface(2), then this

                means that the label space type is per Interface.

                .. data:: perPlatform = 1

                .. data:: perInterface = 2

                """

                perPlatform = 1

                perInterface = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _MPLS_LDP_GENERIC_STD_MIB as meta
                    return meta._meta_table['MplsLdpGenericStdMib.Mplsldpentitygenericlrtable.Mplsldpentitygenericlrentry.MplsldpentitygenericlabelspaceEnum']


            @property
            def _common_path(self):
                if self.mplsldpentityldpid is None:
                    raise YPYModelError('Key property mplsldpentityldpid is None')
                if self.mplsldpentityindex is None:
                    raise YPYModelError('Key property mplsldpentityindex is None')
                if self.mplsldpentitygenericlrmin is None:
                    raise YPYModelError('Key property mplsldpentitygenericlrmin is None')
                if self.mplsldpentitygenericlrmax is None:
                    raise YPYModelError('Key property mplsldpentitygenericlrmax is None')

                return '/MPLS-LDP-GENERIC-STD-MIB:MPLS-LDP-GENERIC-STD-MIB/MPLS-LDP-GENERIC-STD-MIB:mplsLdpEntityGenericLRTable/MPLS-LDP-GENERIC-STD-MIB:mplsLdpEntityGenericLREntry[MPLS-LDP-GENERIC-STD-MIB:mplsLdpEntityLdpId = ' + str(self.mplsldpentityldpid) + '][MPLS-LDP-GENERIC-STD-MIB:mplsLdpEntityIndex = ' + str(self.mplsldpentityindex) + '][MPLS-LDP-GENERIC-STD-MIB:mplsLdpEntityGenericLRMin = ' + str(self.mplsldpentitygenericlrmin) + '][MPLS-LDP-GENERIC-STD-MIB:mplsLdpEntityGenericLRMax = ' + str(self.mplsldpentitygenericlrmax) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.mplsldpentityldpid is not None:
                    return True

                if self.mplsldpentityindex is not None:
                    return True

                if self.mplsldpentitygenericlrmin is not None:
                    return True

                if self.mplsldpentitygenericlrmax is not None:
                    return True

                if self.mplsldpentitygenericifindexorzero is not None:
                    return True

                if self.mplsldpentitygenericlabelspace is not None:
                    return True

                if self.mplsldpentitygenericlrrowstatus is not None:
                    return True

                if self.mplsldpentitygenericlrstoragetype is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _MPLS_LDP_GENERIC_STD_MIB as meta
                return meta._meta_table['MplsLdpGenericStdMib.Mplsldpentitygenericlrtable.Mplsldpentitygenericlrentry']['meta_info']

        @property
        def _common_path(self):

            return '/MPLS-LDP-GENERIC-STD-MIB:MPLS-LDP-GENERIC-STD-MIB/MPLS-LDP-GENERIC-STD-MIB:mplsLdpEntityGenericLRTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.mplsldpentitygenericlrentry is not None:
                for child_ref in self.mplsldpentitygenericlrentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _MPLS_LDP_GENERIC_STD_MIB as meta
            return meta._meta_table['MplsLdpGenericStdMib.Mplsldpentitygenericlrtable']['meta_info']

    @property
    def _common_path(self):

        return '/MPLS-LDP-GENERIC-STD-MIB:MPLS-LDP-GENERIC-STD-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.mplsldpentitygenericlrtable is not None and self.mplsldpentitygenericlrtable._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _MPLS_LDP_GENERIC_STD_MIB as meta
        return meta._meta_table['MplsLdpGenericStdMib']['meta_info']


