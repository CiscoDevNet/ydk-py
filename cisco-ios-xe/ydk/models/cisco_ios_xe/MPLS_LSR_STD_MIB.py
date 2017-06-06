""" MPLS_LSR_STD_MIB 

This MIB module contains managed object definitions for
the Multiprotocol Label Switching (MPLS) Router as
defined in\: Rosen, E., Viswanathan, A., and R.
Callon, Multiprotocol Label Switching Architecture,
RFC 3031, January 2001.

Copyright (C) The Internet Society (2004). The
initial version of this MIB module was published
in RFC 3812. For full legal notices see the RFC
itself or see\:
http\://www.ietf.org/copyrights/ianamib.html

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class MplsLsrStdMib(object):
    """
    
    
    .. attribute:: mplsinsegmentmaptable
    
    	This table specifies the mapping from the mplsInSegmentIndex to the corresponding mplsInSegmentInterface and mplsInSegmentLabel objects. The purpose of this table is to provide the manager with an alternative means by which to locate in\-segments
    	**type**\:   :py:class:`Mplsinsegmentmaptable <ydk.models.cisco_ios_xe.MPLS_LSR_STD_MIB.MplsLsrStdMib.Mplsinsegmentmaptable>`
    
    .. attribute:: mplsinsegmenttable
    
    	This table contains a description of the incoming MPLS segments (labels) to an LSR and their associated parameters. The index for this table is mplsInSegmentIndex. The index structure of this table is specifically designed to handle many different MPLS implementations that manage their labels both in a distributed and centralized manner. The table is also designed to handle existing MPLS labels as defined in RFC3031 as well as longer ones that may be necessary in the future.  In cases where the label cannot fit into the mplsInSegmentLabel object, the mplsInSegmentLabelPtr will indicate this by being set to the first accessible column in the appropriate extension table's row. In this case an additional table MUST be provided and MUST be indexed by at least the indexes used by this table. In all other cases when the label is represented within the mplsInSegmentLabel object, the mplsInSegmentLabelPtr MUST be set to 0.0. Due to the fact that MPLS labels may not exceed 24 bits, the mplsInSegmentLabelPtr object is only a provision for future\-proofing the MIB module. Thus, the definition of any extension tables is beyond the scope of this MIB module
    	**type**\:   :py:class:`Mplsinsegmenttable <ydk.models.cisco_ios_xe.MPLS_LSR_STD_MIB.MplsLsrStdMib.Mplsinsegmenttable>`
    
    .. attribute:: mplsinterfacetable
    
    	This table specifies per\-interface MPLS capability and associated information
    	**type**\:   :py:class:`Mplsinterfacetable <ydk.models.cisco_ios_xe.MPLS_LSR_STD_MIB.MplsLsrStdMib.Mplsinterfacetable>`
    
    .. attribute:: mplslabelstacktable
    
    	This table specifies the label stack to be pushed onto a packet, beneath the top label.  Entries into this table are referred to from mplsXCTable
    	**type**\:   :py:class:`Mplslabelstacktable <ydk.models.cisco_ios_xe.MPLS_LSR_STD_MIB.MplsLsrStdMib.Mplslabelstacktable>`
    
    .. attribute:: mplslsrobjects
    
    	
    	**type**\:   :py:class:`Mplslsrobjects <ydk.models.cisco_ios_xe.MPLS_LSR_STD_MIB.MplsLsrStdMib.Mplslsrobjects>`
    
    .. attribute:: mplsoutsegmenttable
    
    	This table contains a representation of the outgoing segments from an LSR
    	**type**\:   :py:class:`Mplsoutsegmenttable <ydk.models.cisco_ios_xe.MPLS_LSR_STD_MIB.MplsLsrStdMib.Mplsoutsegmenttable>`
    
    .. attribute:: mplsxctable
    
    	This table specifies information for switching between LSP segments.  It supports point\-to\-point, point\-to\-multipoint and multipoint\-to\-point connections.  mplsLabelStackTable specifies the label stack information for a cross\-connect LSR and is referred to from mplsXCTable
    	**type**\:   :py:class:`Mplsxctable <ydk.models.cisco_ios_xe.MPLS_LSR_STD_MIB.MplsLsrStdMib.Mplsxctable>`
    
    

    """

    _prefix = 'MPLS-LSR-STD-MIB'
    _revision = '2004-06-03'

    def __init__(self):
        self.mplsinsegmentmaptable = MplsLsrStdMib.Mplsinsegmentmaptable()
        self.mplsinsegmentmaptable.parent = self
        self.mplsinsegmenttable = MplsLsrStdMib.Mplsinsegmenttable()
        self.mplsinsegmenttable.parent = self
        self.mplsinterfacetable = MplsLsrStdMib.Mplsinterfacetable()
        self.mplsinterfacetable.parent = self
        self.mplslabelstacktable = MplsLsrStdMib.Mplslabelstacktable()
        self.mplslabelstacktable.parent = self
        self.mplslsrobjects = MplsLsrStdMib.Mplslsrobjects()
        self.mplslsrobjects.parent = self
        self.mplsoutsegmenttable = MplsLsrStdMib.Mplsoutsegmenttable()
        self.mplsoutsegmenttable.parent = self
        self.mplsxctable = MplsLsrStdMib.Mplsxctable()
        self.mplsxctable.parent = self


    class Mplslsrobjects(object):
        """
        
        
        .. attribute:: mplsinsegmentindexnext
        
        	This object contains the next available value to be used for mplsInSegmentIndex when creating entries in the mplsInSegmentTable. The special value of a string containing the single octet 0x00 indicates that no new entries can be created in this table. Agents not allowing managers to create entries in this table MUST set this object to this special value
        	**type**\:  str
        
        	**length:** 1..24
        
        .. attribute:: mplslabelstackindexnext
        
        	This object contains the next available value to be used for mplsLabelStackIndex when creating entries in the mplsLabelStackTable. The special string containing the single octet 0x00 indicates that no more new entries can be created in the relevant table.  Agents not allowing managers to create entries in this table MUST set this value to the string containing the single octet 0x00
        	**type**\:  str
        
        	**length:** 1..24
        
        .. attribute:: mplsmaxlabelstackdepth
        
        	The maximum stack depth supported by this LSR
        	**type**\:  int
        
        	**range:** 1..2147483647
        
        .. attribute:: mplsoutsegmentindexnext
        
        	This object contains the next available value to be used for mplsOutSegmentIndex when creating entries in the mplsOutSegmentTable. The special value of a string containing the single octet 0x00 indicates that no new entries can be created in this table. Agents not allowing managers to create entries in this table MUST set this object to this special value
        	**type**\:  str
        
        	**length:** 1..24
        
        .. attribute:: mplsxcindexnext
        
        	This object contains the next available value to be used for mplsXCIndex when creating entries in the mplsXCTable. A special value of the zero length string indicates that no more new entries can be created in the relevant table.  Agents not allowing managers to create entries in this table MUST set this value to the zero length string
        	**type**\:  str
        
        	**length:** 1..24
        
        .. attribute:: mplsxcnotificationsenable
        
        	If this object is set to true(1), then it enables the emission of mplsXCUp and mplsXCDown notifications; otherwise these notifications are not emitted
        	**type**\:  bool
        
        

        """

        _prefix = 'MPLS-LSR-STD-MIB'
        _revision = '2004-06-03'

        def __init__(self):
            self.parent = None
            self.mplsinsegmentindexnext = None
            self.mplslabelstackindexnext = None
            self.mplsmaxlabelstackdepth = None
            self.mplsoutsegmentindexnext = None
            self.mplsxcindexnext = None
            self.mplsxcnotificationsenable = None

        @property
        def _common_path(self):

            return '/MPLS-LSR-STD-MIB:MPLS-LSR-STD-MIB/MPLS-LSR-STD-MIB:mplsLsrObjects'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.mplsinsegmentindexnext is not None:
                return True

            if self.mplslabelstackindexnext is not None:
                return True

            if self.mplsmaxlabelstackdepth is not None:
                return True

            if self.mplsoutsegmentindexnext is not None:
                return True

            if self.mplsxcindexnext is not None:
                return True

            if self.mplsxcnotificationsenable is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _MPLS_LSR_STD_MIB as meta
            return meta._meta_table['MplsLsrStdMib.Mplslsrobjects']['meta_info']


    class Mplsinterfacetable(object):
        """
        This table specifies per\-interface MPLS capability
        and associated information.
        
        .. attribute:: mplsinterfaceentry
        
        	A conceptual row in this table is created automatically by an LSR for every interface capable of supporting MPLS and which is configured to do so. A conceptual row in this table will exist if and only if a corresponding entry in ifTable exists with ifType = mpls(166). If this associated entry in ifTable is operationally disabled (thus removing MPLS capabilities on that interface), the corresponding entry in this table MUST be deleted shortly thereafter. An conceptual row with index 0 is created if the LSR supports per\-platform labels. This conceptual row represents the per\-platform label space and contains parameters that apply to all interfaces that participate in the per\-platform label space. Other conceptual rows in this table represent MPLS interfaces that may participate in either the per\-platform or per\- interface label spaces, or both.  Implementations that either only support per\-platform labels, or have only them configured, may choose to return just the mplsInterfaceEntry of 0 and not return the other rows. This will greatly reduce the number of objects returned. Further information about label space participation of an interface is provided in the DESCRIPTION clause of mplsInterfaceLabelParticipationType
        	**type**\: list of    :py:class:`Mplsinterfaceentry <ydk.models.cisco_ios_xe.MPLS_LSR_STD_MIB.MplsLsrStdMib.Mplsinterfacetable.Mplsinterfaceentry>`
        
        

        """

        _prefix = 'MPLS-LSR-STD-MIB'
        _revision = '2004-06-03'

        def __init__(self):
            self.parent = None
            self.mplsinterfaceentry = YList()
            self.mplsinterfaceentry.parent = self
            self.mplsinterfaceentry.name = 'mplsinterfaceentry'


        class Mplsinterfaceentry(object):
            """
            A conceptual row in this table is created
            automatically by an LSR for every interface capable
            of supporting MPLS and which is configured to do so.
            A conceptual row in this table will exist if and only if
            a corresponding entry in ifTable exists with ifType =
            mpls(166). If this associated entry in ifTable is
            operationally disabled (thus removing MPLS
            capabilities on that interface), the corresponding
            entry in this table MUST be deleted shortly thereafter.
            An conceptual row with index 0 is created if the LSR
            supports per\-platform labels. This conceptual row
            represents the per\-platform label space and contains
            parameters that apply to all interfaces that participate
            in the per\-platform label space. Other conceptual rows
            in this table represent MPLS interfaces that may
            participate in either the per\-platform or per\-
            interface label spaces, or both.  Implementations
            that either only support per\-platform labels,
            or have only them configured, may choose to return
            just the mplsInterfaceEntry of 0 and not return
            the other rows. This will greatly reduce the number
            of objects returned. Further information about label
            space participation of an interface is provided in
            the DESCRIPTION clause of
            mplsInterfaceLabelParticipationType.
            
            .. attribute:: mplsinterfaceindex  <key>
            
            	This is a unique index for an entry in the MplsInterfaceTable.  A non\-zero index for an entry indicates the ifIndex for the corresponding interface entry of the MPLS\-layer in the ifTable. The entry with index 0 represents the per\-platform label space and contains parameters that apply to all interfaces that participate in the per\-platform label space. Other entries defined in this table represent additional MPLS interfaces that may participate in either the per\-platform or per\-interface label spaces, or both
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: mplsinterfaceavailablebandwidth
            
            	This value indicates the total amount of available bandwidth available on this interface and is specified in kilobits per second (Kbps).  This value is calculated as the difference between the amount of bandwidth currently in use and that specified in mplsInterfaceTotalBandwidth.  This variable is not applicable when applied to the interface with index 0. When this value cannot be measured, this value should contain the nominal bandwidth
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsinterfacelabelmaxin
            
            	This is the maximum value of an MPLS label that this LSR is willing to receive on this interface
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsinterfacelabelmaxout
            
            	This is the maximum value of an MPLS label that this LSR is willing to send on this interface
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsinterfacelabelminin
            
            	This is the minimum value of an MPLS label that this LSR is willing to receive on this interface
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsinterfacelabelminout
            
            	This is the minimum value of an MPLS label that this LSR is willing to send on this interface
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsinterfacelabelparticipationtype
            
            	If the value of the mplsInterfaceIndex for this entry is zero, then this entry corresponds to the per\-platform label space for all interfaces configured to use that label space. In this case the perPlatform(0) bit MUST be set; the perInterface(1) bit is meaningless and MUST be ignored.  The remainder of this description applies to entries with a non\-zero value of mplsInterfaceIndex.  If the perInterface(1) bit is set then the value of mplsInterfaceLabelMinIn, mplsInterfaceLabelMaxIn, mplsInterfaceLabelMinOut, and mplsInterfaceLabelMaxOut for this entry reflect the label ranges for this interface.  If only the perPlatform(0) bit is set, then the value of mplsInterfaceLabelMinIn, mplsInterfaceLabelMaxIn, mplsInterfaceLabelMinOut, and mplsInterfaceLabelMaxOut for this entry MUST be identical to the instance of these objects with index 0.  These objects may only vary from the entry with index 0 if both the perPlatform(0) and perInterface(1) bits are set.  In all cases, at a minimum one of the perPlatform(0) or perInterface(1) bits MUST be set to indicate that at least one label space is in use by this interface. In all cases, agents MUST ensure that label ranges are specified consistently and MUST return an inconsistentValue error when they do not
            	**type**\:   :py:class:`Mplsinterfacelabelparticipationtype <ydk.models.cisco_ios_xe.MPLS_LSR_STD_MIB.MplsLsrStdMib.Mplsinterfacetable.Mplsinterfaceentry.Mplsinterfacelabelparticipationtype>`
            
            .. attribute:: mplsinterfaceperfinlabellookupfailures
            
            	This object counts the number of labeled packets that have been received on this interface and which were discarded because there was no matching cross\- connect entry. This object MUST count on a per\- interface basis regardless of which label space the interface participates in
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsinterfaceperfinlabelsinuse
            
            	This object counts the number of labels that are in use at this point in time on this interface in the incoming direction. If the interface participates in only the per\-platform label space, then the value of the instance of this object MUST be identical to the value of the instance with index 0. If the interface participates in the per\-interface label space, then the instance of this object MUST represent the number of per\-interface labels that are in use on this interface
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsinterfaceperfoutfragmentedpkts
            
            	This object counts the number of outgoing MPLS packets that required fragmentation before transmission on this interface. This object MUST count on a per\-interface basis regardless of which label space the interface participates in
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsinterfaceperfoutlabelsinuse
            
            	This object counts the number of top\-most labels in the outgoing label stacks that are in use at this point in time on this interface. This object MUST count on a per\-interface basis regardless of which label space the interface participates in
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsinterfacetotalbandwidth
            
            	This value indicates the total amount of usable bandwidth on this interface and is specified in kilobits per second (Kbps).  This variable is not applicable when applied to the interface with index 0. When this value cannot be measured, this value should contain the nominal bandwidth
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: kilobits per second
            
            

            """

            _prefix = 'MPLS-LSR-STD-MIB'
            _revision = '2004-06-03'

            def __init__(self):
                self.parent = None
                self.mplsinterfaceindex = None
                self.mplsinterfaceavailablebandwidth = None
                self.mplsinterfacelabelmaxin = None
                self.mplsinterfacelabelmaxout = None
                self.mplsinterfacelabelminin = None
                self.mplsinterfacelabelminout = None
                self.mplsinterfacelabelparticipationtype = MplsLsrStdMib.Mplsinterfacetable.Mplsinterfaceentry.Mplsinterfacelabelparticipationtype()
                self.mplsinterfaceperfinlabellookupfailures = None
                self.mplsinterfaceperfinlabelsinuse = None
                self.mplsinterfaceperfoutfragmentedpkts = None
                self.mplsinterfaceperfoutlabelsinuse = None
                self.mplsinterfacetotalbandwidth = None

            class Mplsinterfacelabelparticipationtype(FixedBitsDict):
                """
                Mplsinterfacelabelparticipationtype

                If the value of the mplsInterfaceIndex for this
                entry is zero, then this entry corresponds to the
                per\-platform label space for all interfaces configured
                to use that label space. In this case the perPlatform(0)
                bit MUST be set; the perInterface(1) bit is meaningless
                and MUST be ignored.
                
                The remainder of this description applies to entries
                with a non\-zero value of mplsInterfaceIndex.
                
                If the perInterface(1) bit is set then the value of
                mplsInterfaceLabelMinIn, mplsInterfaceLabelMaxIn,
                mplsInterfaceLabelMinOut, and
                mplsInterfaceLabelMaxOut for this entry reflect the
                label ranges for this interface.
                
                If only the perPlatform(0) bit is set, then the value of
                mplsInterfaceLabelMinIn, mplsInterfaceLabelMaxIn,
                mplsInterfaceLabelMinOut, and
                mplsInterfaceLabelMaxOut for this entry MUST be
                identical to the instance of these objects with
                index 0.  These objects may only vary from the entry
                with index 0 if both the perPlatform(0) and perInterface(1)
                bits are set.
                
                In all cases, at a minimum one of the perPlatform(0) or
                perInterface(1) bits MUST be set to indicate that
                at least one label space is in use by this interface. In
                all cases, agents MUST ensure that label ranges are
                specified consistently and MUST return an
                inconsistentValue error when they do not.
                Keys are:- perPlatform , perInterface

                """

                def __init__(self):
                    self._dictionary = { 
                        'perPlatform':False,
                        'perInterface':False,
                    }
                    self._pos_map = { 
                        'perPlatform':0,
                        'perInterface':1,
                    }

            @property
            def _common_path(self):
                if self.mplsinterfaceindex is None:
                    raise YPYModelError('Key property mplsinterfaceindex is None')

                return '/MPLS-LSR-STD-MIB:MPLS-LSR-STD-MIB/MPLS-LSR-STD-MIB:mplsInterfaceTable/MPLS-LSR-STD-MIB:mplsInterfaceEntry[MPLS-LSR-STD-MIB:mplsInterfaceIndex = ' + str(self.mplsinterfaceindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.mplsinterfaceindex is not None:
                    return True

                if self.mplsinterfaceavailablebandwidth is not None:
                    return True

                if self.mplsinterfacelabelmaxin is not None:
                    return True

                if self.mplsinterfacelabelmaxout is not None:
                    return True

                if self.mplsinterfacelabelminin is not None:
                    return True

                if self.mplsinterfacelabelminout is not None:
                    return True

                if self.mplsinterfacelabelparticipationtype is not None:
                    if self.mplsinterfacelabelparticipationtype._has_data():
                        return True

                if self.mplsinterfaceperfinlabellookupfailures is not None:
                    return True

                if self.mplsinterfaceperfinlabelsinuse is not None:
                    return True

                if self.mplsinterfaceperfoutfragmentedpkts is not None:
                    return True

                if self.mplsinterfaceperfoutlabelsinuse is not None:
                    return True

                if self.mplsinterfacetotalbandwidth is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _MPLS_LSR_STD_MIB as meta
                return meta._meta_table['MplsLsrStdMib.Mplsinterfacetable.Mplsinterfaceentry']['meta_info']

        @property
        def _common_path(self):

            return '/MPLS-LSR-STD-MIB:MPLS-LSR-STD-MIB/MPLS-LSR-STD-MIB:mplsInterfaceTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.mplsinterfaceentry is not None:
                for child_ref in self.mplsinterfaceentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _MPLS_LSR_STD_MIB as meta
            return meta._meta_table['MplsLsrStdMib.Mplsinterfacetable']['meta_info']


    class Mplsinsegmenttable(object):
        """
        This table contains a description of the incoming MPLS
        segments (labels) to an LSR and their associated parameters.
        The index for this table is mplsInSegmentIndex.
        The index structure of this table is specifically designed
        to handle many different MPLS implementations that manage
        their labels both in a distributed and centralized manner.
        The table is also designed to handle existing MPLS labels
        as defined in RFC3031 as well as longer ones that may
        be necessary in the future.
        
        In cases where the label cannot fit into the
        mplsInSegmentLabel object, the mplsInSegmentLabelPtr
        will indicate this by being set to the first accessible
        column in the appropriate extension table's row.
        In this case an additional table MUST
        be provided and MUST be indexed by at least the indexes
        used by this table. In all other cases when the label is
        represented within the mplsInSegmentLabel object, the
        mplsInSegmentLabelPtr MUST be set to 0.0. Due to the
        fact that MPLS labels may not exceed 24 bits, the
        mplsInSegmentLabelPtr object is only a provision for
        future\-proofing the MIB module. Thus, the definition
        of any extension tables is beyond the scope of this
        MIB module.
        
        .. attribute:: mplsinsegmententry
        
        	An entry in this table represents one incoming segment as is represented in an LSR's LFIB. An entry can be created by a network administrator or an SNMP agent, or an MPLS signaling protocol.  The creator of the entry is denoted by mplsInSegmentOwner. The value of mplsInSegmentRowStatus cannot be active(1) unless the ifTable entry corresponding to mplsInSegmentInterface exists.  An entry in this table must match any incoming packets, and indicates an instance of mplsXCEntry based on which forwarding and/or switching actions are taken
        	**type**\: list of    :py:class:`Mplsinsegmententry <ydk.models.cisco_ios_xe.MPLS_LSR_STD_MIB.MplsLsrStdMib.Mplsinsegmenttable.Mplsinsegmententry>`
        
        

        """

        _prefix = 'MPLS-LSR-STD-MIB'
        _revision = '2004-06-03'

        def __init__(self):
            self.parent = None
            self.mplsinsegmententry = YList()
            self.mplsinsegmententry.parent = self
            self.mplsinsegmententry.name = 'mplsinsegmententry'


        class Mplsinsegmententry(object):
            """
            An entry in this table represents one incoming
            segment as is represented in an LSR's LFIB.
            An entry can be created by a network
            administrator or an SNMP agent, or an MPLS signaling
            protocol.  The creator of the entry is denoted by
            mplsInSegmentOwner.
            The value of mplsInSegmentRowStatus cannot be active(1)
            unless the ifTable entry corresponding to
            mplsInSegmentInterface exists.  An entry in this table
            must match any incoming packets, and indicates an
            instance of mplsXCEntry based on which forwarding
            and/or switching actions are taken.
            
            .. attribute:: mplsinsegmentindex  <key>
            
            	The index for this in\-segment. The string containing the single octet 0x00 MUST not be used as an index
            	**type**\:  str
            
            	**length:** 1..24
            
            .. attribute:: mplsinsegmentaddrfamily
            
            	The IANA address family [IANAFamily] of packets received on this segment, which is used at an egress LSR to deliver them to the appropriate layer 3 entity. A value of other(0) indicates that the family type is either unknown or undefined; this SHOULD NOT be used at an egress LSR. This object cannot be modified if mplsInSegmentRowStatus is active(1)
            	**type**\:   :py:class:`AddressfamilynumbersEnum <ydk.models.cisco_ios_xe.IANA_ADDRESS_FAMILY_NUMBERS_MIB.AddressfamilynumbersEnum>`
            
            .. attribute:: mplsinsegmentinterface
            
            	This object represents the interface index for the incoming MPLS interface.  A value of zero represents all interfaces participating in the per\-platform label space.  This may only be used in cases where the incoming interface and label are associated with the same mplsXCEntry. Specifically, given a label and any incoming interface pair from the per\-platform label space, the outgoing label/interface mapping remains the same. If this is not the case, then individual entries MUST exist that can then be mapped to unique mplsXCEntries
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: mplsinsegmentlabel
            
            	If the corresponding instance of mplsInSegmentLabelPtr is zeroDotZero then this object MUST contain the incoming label associated with this in\-segment. If not this object SHOULD be zero and MUST be ignored
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsinsegmentlabelptr
            
            	If the label for this segment cannot be represented fully within the mplsInSegmentLabel object, this object MUST point to the first accessible column of a conceptual row in an external table containing the label.  In this case, the mplsInSegmentTopLabel object SHOULD be set to 0 and ignored. This object MUST be set to zeroDotZero otherwise
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: mplsinsegmentnpop
            
            	The number of labels to pop from the incoming packet.  Normally only the top label is popped from the packet and used for all switching decisions for that packet.  This is indicated by setting this object to the default value of 1. If an LSR supports popping of more than one label, this object MUST be set to that number. This object cannot be modified if mplsInSegmentRowStatus is active(1)
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: mplsinsegmentowner
            
            	Denotes the entity that created and is responsible for managing this segment
            	**type**\:   :py:class:`MplsownerEnum <ydk.models.cisco_ios_xe.MPLS_TC_STD_MIB.MplsownerEnum>`
            
            .. attribute:: mplsinsegmentperfdiscards
            
            	The number of labeled packets received on this in\- segment, which were chosen to be discarded even though no errors had been detected to prevent their being transmitted.  One possible reason for discarding such a labeled packet could be to free up buffer space
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsinsegmentperfdiscontinuitytime
            
            	The value of sysUpTime on the most recent occasion at which any one or more of this segment's Counter32 or Counter64 suffered a discontinuity. If no such discontinuities have occurred since the last re\- initialization of the local management subsystem, then this object contains a zero value
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsinsegmentperferrors
            
            	The number of errored packets received on this segment
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsinsegmentperfhcoctets
            
            	The total number of octets received.  This is the 64 bit version of mplsInSegmentPerfOctets, if mplsInSegmentPerfHCOctets is supported according to the rules spelled out in RFC2863
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: mplsinsegmentperfoctets
            
            	This value represents the total number of octets received by this segment. It MUST be equal to the least significant 32 bits of mplsInSegmentPerfHCOctets if mplsInSegmentPerfHCOctets is supported according to the rules spelled out in RFC2863
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsinsegmentperfpackets
            
            	Total number of packets received by this segment
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsinsegmentrowstatus
            
            	This variable is used to create, modify, and/or delete a row in this table. When a row in this table has a row in the active(1) state, no objects in this row can be modified except the mplsInSegmentRowStatus and mplsInSegmentStorageType
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: mplsinsegmentstoragetype
            
            	This variable indicates the storage type for this object. The agent MUST ensure that this object's value remains consistent with the associated mplsXCEntry. Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\:   :py:class:`StoragetypeEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.StoragetypeEnum>`
            
            .. attribute:: mplsinsegmenttrafficparamptr
            
            	This variable represents a pointer to the traffic parameter specification for this in\-segment.  This value may point at an entry in the mplsTunnelResourceTable in the MPLS\-TE\-STD\-MIB (RFC3812) to indicate which traffic parameter settings for this segment if it represents an LSP used for a TE tunnel.  This value may optionally point at an externally defined traffic parameter specification table.  A value of zeroDotZero indicates best\-effort treatment.  By having the same value of this object, two or more segments can indicate resource sharing of such things as LSP queue space, etc.  This object cannot be modified if mplsInSegmentRowStatus is active(1).  For entries in this table that are preserved after a re\-boot, the agent MUST ensure that their integrity be preserved, or this object should be set to 0.0 if it cannot
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: mplsinsegmentxcindex
            
            	Index into mplsXCTable which identifies which cross\- connect entry this segment is part of.  The string containing the single octet 0x00 indicates that this entry is not referred to by any cross\-connect entry. When a cross\-connect entry is created which this in\-segment is a part of, this object is automatically updated to reflect the value of mplsXCIndex of that cross\-connect entry
            	**type**\:  str
            
            	**length:** 1..24
            
            

            """

            _prefix = 'MPLS-LSR-STD-MIB'
            _revision = '2004-06-03'

            def __init__(self):
                self.parent = None
                self.mplsinsegmentindex = None
                self.mplsinsegmentaddrfamily = None
                self.mplsinsegmentinterface = None
                self.mplsinsegmentlabel = None
                self.mplsinsegmentlabelptr = None
                self.mplsinsegmentnpop = None
                self.mplsinsegmentowner = None
                self.mplsinsegmentperfdiscards = None
                self.mplsinsegmentperfdiscontinuitytime = None
                self.mplsinsegmentperferrors = None
                self.mplsinsegmentperfhcoctets = None
                self.mplsinsegmentperfoctets = None
                self.mplsinsegmentperfpackets = None
                self.mplsinsegmentrowstatus = None
                self.mplsinsegmentstoragetype = None
                self.mplsinsegmenttrafficparamptr = None
                self.mplsinsegmentxcindex = None

            @property
            def _common_path(self):
                if self.mplsinsegmentindex is None:
                    raise YPYModelError('Key property mplsinsegmentindex is None')

                return '/MPLS-LSR-STD-MIB:MPLS-LSR-STD-MIB/MPLS-LSR-STD-MIB:mplsInSegmentTable/MPLS-LSR-STD-MIB:mplsInSegmentEntry[MPLS-LSR-STD-MIB:mplsInSegmentIndex = ' + str(self.mplsinsegmentindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.mplsinsegmentindex is not None:
                    return True

                if self.mplsinsegmentaddrfamily is not None:
                    return True

                if self.mplsinsegmentinterface is not None:
                    return True

                if self.mplsinsegmentlabel is not None:
                    return True

                if self.mplsinsegmentlabelptr is not None:
                    return True

                if self.mplsinsegmentnpop is not None:
                    return True

                if self.mplsinsegmentowner is not None:
                    return True

                if self.mplsinsegmentperfdiscards is not None:
                    return True

                if self.mplsinsegmentperfdiscontinuitytime is not None:
                    return True

                if self.mplsinsegmentperferrors is not None:
                    return True

                if self.mplsinsegmentperfhcoctets is not None:
                    return True

                if self.mplsinsegmentperfoctets is not None:
                    return True

                if self.mplsinsegmentperfpackets is not None:
                    return True

                if self.mplsinsegmentrowstatus is not None:
                    return True

                if self.mplsinsegmentstoragetype is not None:
                    return True

                if self.mplsinsegmenttrafficparamptr is not None:
                    return True

                if self.mplsinsegmentxcindex is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _MPLS_LSR_STD_MIB as meta
                return meta._meta_table['MplsLsrStdMib.Mplsinsegmenttable.Mplsinsegmententry']['meta_info']

        @property
        def _common_path(self):

            return '/MPLS-LSR-STD-MIB:MPLS-LSR-STD-MIB/MPLS-LSR-STD-MIB:mplsInSegmentTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.mplsinsegmententry is not None:
                for child_ref in self.mplsinsegmententry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _MPLS_LSR_STD_MIB as meta
            return meta._meta_table['MplsLsrStdMib.Mplsinsegmenttable']['meta_info']


    class Mplsoutsegmenttable(object):
        """
        This table contains a representation of the outgoing
        segments from an LSR.
        
        .. attribute:: mplsoutsegmententry
        
        	An entry in this table represents one outgoing segment.  An entry can be created by a network administrator, an SNMP agent, or an MPLS signaling protocol.  The object mplsOutSegmentOwner indicates the creator of this entry. The value of mplsOutSegmentRowStatus cannot be active(1) unless the ifTable entry corresponding to mplsOutSegmentInterface exists.  Note that the indexing of this table uses a single, arbitrary index (mplsOutSegmentIndex) to indicate which out\-segment (i.e.\: label) is being switched to from which in\-segment (i.e\: label) or in\-segments. This is necessary because it is possible to have an equal\-cost multi\-path situation where two identical out\-going labels are assigned to the same cross\-connect (i.e.\: they go to two different neighboring LSRs); thus, requiring two out\-segments. In order to preserve the uniqueness of the references by the mplsXCEntry, an arbitrary integer must be used as the index for this table
        	**type**\: list of    :py:class:`Mplsoutsegmententry <ydk.models.cisco_ios_xe.MPLS_LSR_STD_MIB.MplsLsrStdMib.Mplsoutsegmenttable.Mplsoutsegmententry>`
        
        

        """

        _prefix = 'MPLS-LSR-STD-MIB'
        _revision = '2004-06-03'

        def __init__(self):
            self.parent = None
            self.mplsoutsegmententry = YList()
            self.mplsoutsegmententry.parent = self
            self.mplsoutsegmententry.name = 'mplsoutsegmententry'


        class Mplsoutsegmententry(object):
            """
            An entry in this table represents one outgoing
            segment.  An entry can be created by a network
            administrator, an SNMP agent, or an MPLS signaling
            protocol.  The object mplsOutSegmentOwner indicates
            the creator of this entry. The value of
            mplsOutSegmentRowStatus cannot be active(1) unless
            the ifTable entry corresponding to
            mplsOutSegmentInterface exists.
            
            Note that the indexing of this table uses a single,
            arbitrary index (mplsOutSegmentIndex) to indicate
            which out\-segment (i.e.\: label) is being switched to
            from which in\-segment (i.e\: label) or in\-segments.
            This is necessary because it is possible to have an
            equal\-cost multi\-path situation where two identical
            out\-going labels are assigned to the same
            cross\-connect (i.e.\: they go to two different neighboring
            LSRs); thus, requiring two out\-segments. In order to
            preserve the uniqueness of the references
            by the mplsXCEntry, an arbitrary integer must be used as
            the index for this table.
            
            .. attribute:: mplsoutsegmentindex  <key>
            
            	This value contains a unique index for this row. While a value of a string containing the single octet 0x00 is not valid as an index for entries in this table, it can be supplied as a valid value to index the mplsXCTable to represent entries for which no out\-segment has been configured or exists
            	**type**\:  str
            
            	**length:** 1..24
            
            .. attribute:: mplsoutsegmentinterface
            
            	This value must contain the interface index of the outgoing interface. This object cannot be modified if mplsOutSegmentRowStatus is active(1). The mplsOutSegmentRowStatus cannot be set to active(1) until this object is set to a value corresponding to a valid ifEntry
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: mplsoutsegmentnexthopaddr
            
            	The internet address of the next hop. The type of this address is determined by the value of the mplslOutSegmentNextHopAddrType object.  This object cannot be modified if mplsOutSegmentRowStatus is active(1)
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: mplsoutsegmentnexthopaddrtype
            
            	Indicates the next hop Internet address type. Only values unknown(0), ipv4(1) or ipv6(2) have to be supported.  A value of unknown(0) is allowed only when the outgoing interface is of type point\-to\-point. If any other unsupported values are attempted in a set operation, the agent MUST return an inconsistentValue error
            	**type**\:   :py:class:`InetaddresstypeEnum <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetaddresstypeEnum>`
            
            .. attribute:: mplsoutsegmentowner
            
            	Denotes the entity which created and is responsible for managing this segment
            	**type**\:   :py:class:`MplsownerEnum <ydk.models.cisco_ios_xe.MPLS_TC_STD_MIB.MplsownerEnum>`
            
            .. attribute:: mplsoutsegmentperfdiscards
            
            	The number of labeled packets attempted to be transmitted on this out\-segment, which were chosen to be discarded even though no errors had been detected to prevent their being transmitted. One possible reason for discarding such a labeled packet could be to free up buffer space
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsoutsegmentperfdiscontinuitytime
            
            	The value of sysUpTime on the most recent occasion at which any one or more of this segment's Counter32 or Counter64 suffered a discontinuity. If no such discontinuities have occurred since the last re\- initialization of the local management subsystem, then this object contains a zero value
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsoutsegmentperferrors
            
            	Number of packets that could not be sent due to errors on this segment
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsoutsegmentperfhcoctets
            
            	Total number of octets sent.  This is the 64 bit version of mplsOutSegmentPerfOctets, if mplsOutSegmentPerfHCOctets is supported according to the rules spelled out in RFC2863
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: mplsoutsegmentperfoctets
            
            	This value contains the total number of octets sent on this segment. It MUST be equal to the least significant 32 bits of mplsOutSegmentPerfHCOctets if mplsOutSegmentPerfHCOctets is supported according to the rules spelled out in RFC2863
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsoutsegmentperfpackets
            
            	This value contains the total number of packets sent on this segment
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsoutsegmentpushtoplabel
            
            	This value indicates whether or not a top label should be pushed onto the outgoing packet's label stack.  The value of this variable MUST be set to true(1) if the outgoing interface does not support pop\-and\-go (and no label stack remains). For example, on ATM interface, or if the segment represents a tunnel origination.  Note that it is considered an error in the case that mplsOutSegmentPushTopLabel is set to false, but the cross\-connect entry which refers to this out\-segment has a non\-zero mplsLabelStackIndex.  The LSR MUST ensure that this situation does not happen. This object cannot be modified if mplsOutSegmentRowStatus is active(1)
            	**type**\:  bool
            
            .. attribute:: mplsoutsegmentrowstatus
            
            	For creating, modifying, and deleting this row. When a row in this table has a row in the active(1) state, no objects in this row can be modified except the mplsOutSegmentRowStatus or mplsOutSegmentStorageType
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: mplsoutsegmentstoragetype
            
            	This variable indicates the storage type for this object. The agent MUST ensure that this object's value remains consistent with the associated mplsXCEntry. Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\:   :py:class:`StoragetypeEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.StoragetypeEnum>`
            
            .. attribute:: mplsoutsegmenttoplabel
            
            	If mplsOutSegmentPushTopLabel is true then this represents the label that should be pushed onto the top of the outgoing packet's label stack. Otherwise this value SHOULD be set to 0 by the management station and MUST be ignored by the agent. This object cannot be modified if mplsOutSegmentRowStatus is active(1)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsoutsegmenttoplabelptr
            
            	If the label for this segment cannot be represented fully within the mplsOutSegmentLabel object, this object MUST point to the first accessible column of a conceptual row in an external table containing the label.  In this case, the mplsOutSegmentTopLabel object SHOULD be set to 0 and ignored. This object MUST be set to zeroDotZero otherwise
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: mplsoutsegmenttrafficparamptr
            
            	This variable represents a pointer to the traffic parameter specification for this out\-segment.  This value may point at an entry in the MplsTunnelResourceEntry in the MPLS\-TE\-STD\-MIB (RFC3812)  RFC Editor\: Please fill in RFC number.  to indicate which traffic parameter settings for this segment if it represents an LSP used for a TE tunnel.  This value may optionally point at an externally defined traffic parameter specification table.  A value of zeroDotZero indicates best\-effort treatment.  By having the same value of this object, two or more segments can indicate resource sharing of such things as LSP queue space, etc.  This object cannot be modified if mplsOutSegmentRowStatus is active(1). For entries in this table that are preserved after a re\-boot, the agent MUST ensure that their integrity be preserved, or this object should be set to 0.0 if it cannot
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: mplsoutsegmentxcindex
            
            	Index into mplsXCTable which identifies which cross\- connect entry this segment is part of.  A value of the string containing the single octet 0x00 indicates that this entry is not referred to by any cross\-connect entry.  When a cross\-connect entry is created which this out\-segment is a part of, this object MUST be updated by the agent to reflect the value of mplsXCIndex of that cross\-connect entry
            	**type**\:  str
            
            	**length:** 1..24
            
            

            """

            _prefix = 'MPLS-LSR-STD-MIB'
            _revision = '2004-06-03'

            def __init__(self):
                self.parent = None
                self.mplsoutsegmentindex = None
                self.mplsoutsegmentinterface = None
                self.mplsoutsegmentnexthopaddr = None
                self.mplsoutsegmentnexthopaddrtype = None
                self.mplsoutsegmentowner = None
                self.mplsoutsegmentperfdiscards = None
                self.mplsoutsegmentperfdiscontinuitytime = None
                self.mplsoutsegmentperferrors = None
                self.mplsoutsegmentperfhcoctets = None
                self.mplsoutsegmentperfoctets = None
                self.mplsoutsegmentperfpackets = None
                self.mplsoutsegmentpushtoplabel = None
                self.mplsoutsegmentrowstatus = None
                self.mplsoutsegmentstoragetype = None
                self.mplsoutsegmenttoplabel = None
                self.mplsoutsegmenttoplabelptr = None
                self.mplsoutsegmenttrafficparamptr = None
                self.mplsoutsegmentxcindex = None

            @property
            def _common_path(self):
                if self.mplsoutsegmentindex is None:
                    raise YPYModelError('Key property mplsoutsegmentindex is None')

                return '/MPLS-LSR-STD-MIB:MPLS-LSR-STD-MIB/MPLS-LSR-STD-MIB:mplsOutSegmentTable/MPLS-LSR-STD-MIB:mplsOutSegmentEntry[MPLS-LSR-STD-MIB:mplsOutSegmentIndex = ' + str(self.mplsoutsegmentindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.mplsoutsegmentindex is not None:
                    return True

                if self.mplsoutsegmentinterface is not None:
                    return True

                if self.mplsoutsegmentnexthopaddr is not None:
                    return True

                if self.mplsoutsegmentnexthopaddrtype is not None:
                    return True

                if self.mplsoutsegmentowner is not None:
                    return True

                if self.mplsoutsegmentperfdiscards is not None:
                    return True

                if self.mplsoutsegmentperfdiscontinuitytime is not None:
                    return True

                if self.mplsoutsegmentperferrors is not None:
                    return True

                if self.mplsoutsegmentperfhcoctets is not None:
                    return True

                if self.mplsoutsegmentperfoctets is not None:
                    return True

                if self.mplsoutsegmentperfpackets is not None:
                    return True

                if self.mplsoutsegmentpushtoplabel is not None:
                    return True

                if self.mplsoutsegmentrowstatus is not None:
                    return True

                if self.mplsoutsegmentstoragetype is not None:
                    return True

                if self.mplsoutsegmenttoplabel is not None:
                    return True

                if self.mplsoutsegmenttoplabelptr is not None:
                    return True

                if self.mplsoutsegmenttrafficparamptr is not None:
                    return True

                if self.mplsoutsegmentxcindex is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _MPLS_LSR_STD_MIB as meta
                return meta._meta_table['MplsLsrStdMib.Mplsoutsegmenttable.Mplsoutsegmententry']['meta_info']

        @property
        def _common_path(self):

            return '/MPLS-LSR-STD-MIB:MPLS-LSR-STD-MIB/MPLS-LSR-STD-MIB:mplsOutSegmentTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.mplsoutsegmententry is not None:
                for child_ref in self.mplsoutsegmententry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _MPLS_LSR_STD_MIB as meta
            return meta._meta_table['MplsLsrStdMib.Mplsoutsegmenttable']['meta_info']


    class Mplsxctable(object):
        """
        This table specifies information for switching
        between LSP segments.  It supports point\-to\-point,
        point\-to\-multipoint and multipoint\-to\-point
        connections.  mplsLabelStackTable specifies the
        label stack information for a cross\-connect LSR and
        is referred to from mplsXCTable.
        
        .. attribute:: mplsxcentry
        
        	A row in this table represents one cross\-connect entry.  It is indexed by the following objects\:  \- cross\-connect index mplsXCIndex that uniquely   identifies a group of cross\-connect entries  \- in\-segment index, mplsXCInSegmentIndex  \- out\-segment index, mplsXCOutSegmentIndex  LSPs originating at this LSR\: These are represented by using the special of value of mplsXCInSegmentIndex set to the string containing a single octet 0x00. In this case the mplsXCOutSegmentIndex MUST not be the string containing a single octet 0x00.  LSPs terminating at this LSR\: These are represented by using the special value mplsXCOutSegmentIndex set to the string containing a single octet 0x00.  Special labels\: Entries indexed by the strings containing the reserved MPLS label values as a single octet 0x00 through 0x0f (inclusive) imply LSPs terminating at this LSR.  Note that situations where LSPs are terminated with incoming label equal to the string containing a single octet 0x00 can be distinguished from LSPs originating at this LSR because the mplsXCOutSegmentIndex equals the string containing the single octet 0x00.  An entry can be created by a network administrator or by an SNMP agent as instructed by an MPLS signaling protocol
        	**type**\: list of    :py:class:`Mplsxcentry <ydk.models.cisco_ios_xe.MPLS_LSR_STD_MIB.MplsLsrStdMib.Mplsxctable.Mplsxcentry>`
        
        

        """

        _prefix = 'MPLS-LSR-STD-MIB'
        _revision = '2004-06-03'

        def __init__(self):
            self.parent = None
            self.mplsxcentry = YList()
            self.mplsxcentry.parent = self
            self.mplsxcentry.name = 'mplsxcentry'


        class Mplsxcentry(object):
            """
            A row in this table represents one cross\-connect
            entry.  It is indexed by the following objects\:
            
            \- cross\-connect index mplsXCIndex that uniquely
              identifies a group of cross\-connect entries
            
            \- in\-segment index, mplsXCInSegmentIndex
            
            \- out\-segment index, mplsXCOutSegmentIndex
            
            LSPs originating at this LSR\:
            These are represented by using the special
            of value of mplsXCInSegmentIndex set to the
            string containing a single octet 0x00. In
            this case the mplsXCOutSegmentIndex
            MUST not be the string containing a single
            octet 0x00.
            
            LSPs terminating at this LSR\:
            These are represented by using the special value
            mplsXCOutSegmentIndex set to the string containing
            a single octet 0x00.
            
            Special labels\:
            Entries indexed by the strings containing the
            reserved MPLS label values as a single octet 0x00
            through 0x0f (inclusive) imply LSPs terminating at
            this LSR.  Note that situations where LSPs are
            terminated with incoming label equal to the string
            containing a single octet 0x00 can be distinguished
            from LSPs originating at this LSR because the
            mplsXCOutSegmentIndex equals the string containing the
            single octet 0x00.
            
            An entry can be created by a network administrator
            or by an SNMP agent as instructed by an MPLS
            signaling protocol.
            
            .. attribute:: mplsxcindex  <key>
            
            	Primary index for the conceptual row identifying a group of cross\-connect segments. The string containing a single octet 0x00 is an invalid index
            	**type**\:  str
            
            	**length:** 1..24
            
            .. attribute:: mplsxcinsegmentindex  <key>
            
            	Incoming label index. If this object is set to the string containing a single octet 0x00, this indicates a special case outlined in the table's description above. In this case no corresponding mplsInSegmentEntry shall exist
            	**type**\:  str
            
            	**length:** 1..24
            
            .. attribute:: mplsxcoutsegmentindex  <key>
            
            	Index of out\-segment for LSPs not terminating on this LSR if not set to the string containing the single octet 0x00. If the segment identified by this entry is terminating, then this object MUST be set to the string containing a single octet 0x00 to indicate that no corresponding mplsOutSegmentEntry shall exist
            	**type**\:  str
            
            	**length:** 1..24
            
            .. attribute:: mplsxcadminstatus
            
            	The desired operational status of this segment
            	**type**\:   :py:class:`MplsxcadminstatusEnum <ydk.models.cisco_ios_xe.MPLS_LSR_STD_MIB.MplsLsrStdMib.Mplsxctable.Mplsxcentry.MplsxcadminstatusEnum>`
            
            .. attribute:: mplsxclabelstackindex
            
            	Primary index into mplsLabelStackTable identifying a stack of labels to be pushed beneath the top label. Note that the top label identified by the out\- segment ensures that all the components of a multipoint\-to\-point connection have the same outgoing label. A value of the string containing the single octet 0x00 indicates that no labels are to be stacked beneath the top label. This object cannot be modified if mplsXCRowStatus is active(1)
            	**type**\:  str
            
            	**length:** 1..24
            
            .. attribute:: mplsxclspid
            
            	This value identifies the label switched path that this cross\-connect entry belongs to. This object cannot be modified if mplsXCRowStatus is active(1) except for this object
            	**type**\:  str
            
            	**length:** 2 \| 6
            
            .. attribute:: mplsxcoperstatus
            
            	The actual operational status of this cross\- connect
            	**type**\:   :py:class:`MplsxcoperstatusEnum <ydk.models.cisco_ios_xe.MPLS_LSR_STD_MIB.MplsLsrStdMib.Mplsxctable.Mplsxcentry.MplsxcoperstatusEnum>`
            
            .. attribute:: mplsxcowner
            
            	Denotes the entity that created and is responsible for managing this cross\-connect
            	**type**\:   :py:class:`MplsownerEnum <ydk.models.cisco_ios_xe.MPLS_TC_STD_MIB.MplsownerEnum>`
            
            .. attribute:: mplsxcrowstatus
            
            	For creating, modifying, and deleting this row. When a row in this table has a row in the active(1) state, no objects in this row except this object and the mplsXCStorageType can be modified. 
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: mplsxcstoragetype
            
            	This variable indicates the storage type for this object. The agent MUST ensure that the associated in and out segments also have the same StorageType value and are restored consistently upon system restart. This value SHOULD be set to permanent(4) if created as a result of a static LSP configuration.  Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\:   :py:class:`StoragetypeEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.StoragetypeEnum>`
            
            

            """

            _prefix = 'MPLS-LSR-STD-MIB'
            _revision = '2004-06-03'

            def __init__(self):
                self.parent = None
                self.mplsxcindex = None
                self.mplsxcinsegmentindex = None
                self.mplsxcoutsegmentindex = None
                self.mplsxcadminstatus = None
                self.mplsxclabelstackindex = None
                self.mplsxclspid = None
                self.mplsxcoperstatus = None
                self.mplsxcowner = None
                self.mplsxcrowstatus = None
                self.mplsxcstoragetype = None

            class MplsxcadminstatusEnum(Enum):
                """
                MplsxcadminstatusEnum

                The desired operational status of this segment.

                .. data:: up = 1

                .. data:: down = 2

                .. data:: testing = 3

                """

                up = 1

                down = 2

                testing = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _MPLS_LSR_STD_MIB as meta
                    return meta._meta_table['MplsLsrStdMib.Mplsxctable.Mplsxcentry.MplsxcadminstatusEnum']


            class MplsxcoperstatusEnum(Enum):
                """
                MplsxcoperstatusEnum

                The actual operational status of this cross\-

                connect.

                .. data:: up = 1

                .. data:: down = 2

                .. data:: testing = 3

                .. data:: unknown = 4

                .. data:: dormant = 5

                .. data:: notPresent = 6

                .. data:: lowerLayerDown = 7

                """

                up = 1

                down = 2

                testing = 3

                unknown = 4

                dormant = 5

                notPresent = 6

                lowerLayerDown = 7


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _MPLS_LSR_STD_MIB as meta
                    return meta._meta_table['MplsLsrStdMib.Mplsxctable.Mplsxcentry.MplsxcoperstatusEnum']


            @property
            def _common_path(self):
                if self.mplsxcindex is None:
                    raise YPYModelError('Key property mplsxcindex is None')
                if self.mplsxcinsegmentindex is None:
                    raise YPYModelError('Key property mplsxcinsegmentindex is None')
                if self.mplsxcoutsegmentindex is None:
                    raise YPYModelError('Key property mplsxcoutsegmentindex is None')

                return '/MPLS-LSR-STD-MIB:MPLS-LSR-STD-MIB/MPLS-LSR-STD-MIB:mplsXCTable/MPLS-LSR-STD-MIB:mplsXCEntry[MPLS-LSR-STD-MIB:mplsXCIndex = ' + str(self.mplsxcindex) + '][MPLS-LSR-STD-MIB:mplsXCInSegmentIndex = ' + str(self.mplsxcinsegmentindex) + '][MPLS-LSR-STD-MIB:mplsXCOutSegmentIndex = ' + str(self.mplsxcoutsegmentindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.mplsxcindex is not None:
                    return True

                if self.mplsxcinsegmentindex is not None:
                    return True

                if self.mplsxcoutsegmentindex is not None:
                    return True

                if self.mplsxcadminstatus is not None:
                    return True

                if self.mplsxclabelstackindex is not None:
                    return True

                if self.mplsxclspid is not None:
                    return True

                if self.mplsxcoperstatus is not None:
                    return True

                if self.mplsxcowner is not None:
                    return True

                if self.mplsxcrowstatus is not None:
                    return True

                if self.mplsxcstoragetype is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _MPLS_LSR_STD_MIB as meta
                return meta._meta_table['MplsLsrStdMib.Mplsxctable.Mplsxcentry']['meta_info']

        @property
        def _common_path(self):

            return '/MPLS-LSR-STD-MIB:MPLS-LSR-STD-MIB/MPLS-LSR-STD-MIB:mplsXCTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.mplsxcentry is not None:
                for child_ref in self.mplsxcentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _MPLS_LSR_STD_MIB as meta
            return meta._meta_table['MplsLsrStdMib.Mplsxctable']['meta_info']


    class Mplslabelstacktable(object):
        """
        This table specifies the label stack to be pushed
        onto a packet, beneath the top label.  Entries into
        this table are referred to from mplsXCTable.
        
        .. attribute:: mplslabelstackentry
        
        	An entry in this table represents one label which is to be pushed onto an outgoing packet, beneath the top label.  An entry can be created by a network administrator or by an SNMP agent as instructed by an MPLS signaling protocol
        	**type**\: list of    :py:class:`Mplslabelstackentry <ydk.models.cisco_ios_xe.MPLS_LSR_STD_MIB.MplsLsrStdMib.Mplslabelstacktable.Mplslabelstackentry>`
        
        

        """

        _prefix = 'MPLS-LSR-STD-MIB'
        _revision = '2004-06-03'

        def __init__(self):
            self.parent = None
            self.mplslabelstackentry = YList()
            self.mplslabelstackentry.parent = self
            self.mplslabelstackentry.name = 'mplslabelstackentry'


        class Mplslabelstackentry(object):
            """
            An entry in this table represents one label which is
            to be pushed onto an outgoing packet, beneath the
            top label.  An entry can be created by a network
            administrator or by an SNMP agent as instructed by
            an MPLS signaling protocol.
            
            .. attribute:: mplslabelstackindex  <key>
            
            	Primary index for this row identifying a stack of labels to be pushed on an outgoing packet, beneath the top label. An index containing the string with a single octet 0x00 MUST not be used
            	**type**\:  str
            
            	**length:** 1..24
            
            .. attribute:: mplslabelstacklabelindex  <key>
            
            	Secondary index for this row identifying one label of the stack.  Note that an entry with a smaller mplsLabelStackLabelIndex would refer to a label higher up the label stack and would be popped at a downstream LSR before a label represented by a higher mplsLabelStackLabelIndex at a downstream LSR
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: mplslabelstacklabel
            
            	The label to pushed
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplslabelstacklabelptr
            
            	If the label for this segment cannot be represented fully within the mplsLabelStackLabel object, this object MUST point to the first accessible column of a conceptual row in an external table containing the label.  In this case, the mplsLabelStackLabel object SHOULD be set to 0 and ignored. This object MUST be set to zeroDotZero otherwise
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: mplslabelstackrowstatus
            
            	For creating, modifying, and deleting this row. When a row in this table has a row in the active(1) state, no objects in this row except this object and the mplsLabelStackStorageType can be modified
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: mplslabelstackstoragetype
            
            	This variable indicates the storage type for this object. This object cannot be modified if mplsLabelStackRowStatus is active(1). No objects are required to be writable for rows in this table with this object set to permanent(4).  The agent MUST ensure that all related entries in this table retain the same value for this object.  Agents MUST ensure that the storage type for all entries related to a particular mplsXCEntry retain the same value for this object as the mplsXCEntry's StorageType
            	**type**\:   :py:class:`StoragetypeEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.StoragetypeEnum>`
            
            

            """

            _prefix = 'MPLS-LSR-STD-MIB'
            _revision = '2004-06-03'

            def __init__(self):
                self.parent = None
                self.mplslabelstackindex = None
                self.mplslabelstacklabelindex = None
                self.mplslabelstacklabel = None
                self.mplslabelstacklabelptr = None
                self.mplslabelstackrowstatus = None
                self.mplslabelstackstoragetype = None

            @property
            def _common_path(self):
                if self.mplslabelstackindex is None:
                    raise YPYModelError('Key property mplslabelstackindex is None')
                if self.mplslabelstacklabelindex is None:
                    raise YPYModelError('Key property mplslabelstacklabelindex is None')

                return '/MPLS-LSR-STD-MIB:MPLS-LSR-STD-MIB/MPLS-LSR-STD-MIB:mplsLabelStackTable/MPLS-LSR-STD-MIB:mplsLabelStackEntry[MPLS-LSR-STD-MIB:mplsLabelStackIndex = ' + str(self.mplslabelstackindex) + '][MPLS-LSR-STD-MIB:mplsLabelStackLabelIndex = ' + str(self.mplslabelstacklabelindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.mplslabelstackindex is not None:
                    return True

                if self.mplslabelstacklabelindex is not None:
                    return True

                if self.mplslabelstacklabel is not None:
                    return True

                if self.mplslabelstacklabelptr is not None:
                    return True

                if self.mplslabelstackrowstatus is not None:
                    return True

                if self.mplslabelstackstoragetype is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _MPLS_LSR_STD_MIB as meta
                return meta._meta_table['MplsLsrStdMib.Mplslabelstacktable.Mplslabelstackentry']['meta_info']

        @property
        def _common_path(self):

            return '/MPLS-LSR-STD-MIB:MPLS-LSR-STD-MIB/MPLS-LSR-STD-MIB:mplsLabelStackTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.mplslabelstackentry is not None:
                for child_ref in self.mplslabelstackentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _MPLS_LSR_STD_MIB as meta
            return meta._meta_table['MplsLsrStdMib.Mplslabelstacktable']['meta_info']


    class Mplsinsegmentmaptable(object):
        """
        This table specifies the mapping from the
        mplsInSegmentIndex to the corresponding
        mplsInSegmentInterface and mplsInSegmentLabel
        objects. The purpose of this table is to
        provide the manager with an alternative
        means by which to locate in\-segments.
        
        .. attribute:: mplsinsegmentmapentry
        
        	An entry in this table represents one interface and incoming label pair.  In cases where the label cannot fit into the mplsInSegmentLabel object, the mplsInSegmentLabelPtr will indicate this by being set to the first accessible column in the appropriate extension table's row, and the mplsInSegmentLabel SHOULD be set to 0. In all other cases when the label is represented within the mplsInSegmentLabel object, the mplsInSegmentLabelPtr MUST be 0.0.  Implementors need to be aware that if the value of the mplsInSegmentMapLabelPtrIndex (an OID) has more that 111 sub\-identifiers, then OIDs of column instances in this table will have more than 128 sub\-identifiers and cannot be accessed using SNMPv1, SNMPv2c, or SNMPv3
        	**type**\: list of    :py:class:`Mplsinsegmentmapentry <ydk.models.cisco_ios_xe.MPLS_LSR_STD_MIB.MplsLsrStdMib.Mplsinsegmentmaptable.Mplsinsegmentmapentry>`
        
        

        """

        _prefix = 'MPLS-LSR-STD-MIB'
        _revision = '2004-06-03'

        def __init__(self):
            self.parent = None
            self.mplsinsegmentmapentry = YList()
            self.mplsinsegmentmapentry.parent = self
            self.mplsinsegmentmapentry.name = 'mplsinsegmentmapentry'


        class Mplsinsegmentmapentry(object):
            """
            An entry in this table represents one interface
            and incoming label pair.
            
            In cases where the label cannot fit into the
            mplsInSegmentLabel object, the mplsInSegmentLabelPtr
            will indicate this by being set to the first accessible
            column in the appropriate extension table's row,
            and the mplsInSegmentLabel SHOULD be set to 0.
            In all other cases when the label is
            represented within the mplsInSegmentLabel object, the
            mplsInSegmentLabelPtr MUST be 0.0.
            
            Implementors need to be aware that if the value of
            the mplsInSegmentMapLabelPtrIndex (an OID) has more
            that 111 sub\-identifiers, then OIDs of column
            instances in this table will have more than 128
            sub\-identifiers and cannot be accessed using SNMPv1,
            SNMPv2c, or SNMPv3.
            
            .. attribute:: mplsinsegmentmapinterface  <key>
            
            	This index contains the same value as the mplsInSegmentIndex in the mplsInSegmentTable
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: mplsinsegmentmaplabel  <key>
            
            	This index contains the same value as the mplsInSegmentLabel in the mplsInSegmentTable
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsinsegmentmaplabelptrindex  <key>
            
            	This index contains the same value as the mplsInSegmentLabelPtr.  If the label for the InSegment cannot be represented fully within the mplsInSegmentLabel object, this index MUST point to the first accessible column of a conceptual row in an external table containing the label.  In this case, the mplsInSegmentTopLabel object SHOULD be set to 0 and ignored. This object MUST be set to zeroDotZero otherwise
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: mplsinsegmentmapindex
            
            	The mplsInSegmentIndex that corresponds to the mplsInSegmentInterface and mplsInSegmentLabel, or the mplsInSegmentInterface and mplsInSegmentLabelPtr, if applicable. The string containing the single octet 0x00 MUST not be returned
            	**type**\:  str
            
            	**length:** 1..24
            
            

            """

            _prefix = 'MPLS-LSR-STD-MIB'
            _revision = '2004-06-03'

            def __init__(self):
                self.parent = None
                self.mplsinsegmentmapinterface = None
                self.mplsinsegmentmaplabel = None
                self.mplsinsegmentmaplabelptrindex = None
                self.mplsinsegmentmapindex = None

            @property
            def _common_path(self):
                if self.mplsinsegmentmapinterface is None:
                    raise YPYModelError('Key property mplsinsegmentmapinterface is None')
                if self.mplsinsegmentmaplabel is None:
                    raise YPYModelError('Key property mplsinsegmentmaplabel is None')
                if self.mplsinsegmentmaplabelptrindex is None:
                    raise YPYModelError('Key property mplsinsegmentmaplabelptrindex is None')

                return '/MPLS-LSR-STD-MIB:MPLS-LSR-STD-MIB/MPLS-LSR-STD-MIB:mplsInSegmentMapTable/MPLS-LSR-STD-MIB:mplsInSegmentMapEntry[MPLS-LSR-STD-MIB:mplsInSegmentMapInterface = ' + str(self.mplsinsegmentmapinterface) + '][MPLS-LSR-STD-MIB:mplsInSegmentMapLabel = ' + str(self.mplsinsegmentmaplabel) + '][MPLS-LSR-STD-MIB:mplsInSegmentMapLabelPtrIndex = ' + str(self.mplsinsegmentmaplabelptrindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.mplsinsegmentmapinterface is not None:
                    return True

                if self.mplsinsegmentmaplabel is not None:
                    return True

                if self.mplsinsegmentmaplabelptrindex is not None:
                    return True

                if self.mplsinsegmentmapindex is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _MPLS_LSR_STD_MIB as meta
                return meta._meta_table['MplsLsrStdMib.Mplsinsegmentmaptable.Mplsinsegmentmapentry']['meta_info']

        @property
        def _common_path(self):

            return '/MPLS-LSR-STD-MIB:MPLS-LSR-STD-MIB/MPLS-LSR-STD-MIB:mplsInSegmentMapTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.mplsinsegmentmapentry is not None:
                for child_ref in self.mplsinsegmentmapentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _MPLS_LSR_STD_MIB as meta
            return meta._meta_table['MplsLsrStdMib.Mplsinsegmentmaptable']['meta_info']

    @property
    def _common_path(self):

        return '/MPLS-LSR-STD-MIB:MPLS-LSR-STD-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.mplsinsegmentmaptable is not None and self.mplsinsegmentmaptable._has_data():
            return True

        if self.mplsinsegmenttable is not None and self.mplsinsegmenttable._has_data():
            return True

        if self.mplsinterfacetable is not None and self.mplsinterfacetable._has_data():
            return True

        if self.mplslabelstacktable is not None and self.mplslabelstacktable._has_data():
            return True

        if self.mplslsrobjects is not None and self.mplslsrobjects._has_data():
            return True

        if self.mplsoutsegmenttable is not None and self.mplsoutsegmenttable._has_data():
            return True

        if self.mplsxctable is not None and self.mplsxctable._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _MPLS_LSR_STD_MIB as meta
        return meta._meta_table['MplsLsrStdMib']['meta_info']


