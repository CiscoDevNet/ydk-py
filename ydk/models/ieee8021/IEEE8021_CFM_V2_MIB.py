""" IEEE8021_CFM_V2_MIB 

Connectivity Fault Management V2 module for 
managing IEEE 802.1ag\-2007.

Unless otherwise indicated, the references in this MIB
module are to IEEE 802.1Q\-2005 as amended by IEEE 802.1ad,
IEEE 802.1ak, IEEE 802.1ag and IEEE 802.1ah.

Copyright (C) IEEE.
This version of this MIB module is part of IEEE802.1Q;
see the draft itself for full legal notices.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.ieee8021.IEEE8021_CFM_MIB import Dot1agCfmConfigErrors_Bits
from ydk.models.ieee8021.IEEE8021_CFM_MIB import Dot1agCfmIdPermission_Enum
from ydk.models.ieee8021.IEEE8021_CFM_MIB import Dot1agCfmMhfCreation_Enum
from ydk.models.ieee8021.IEEE8021_CFM_MIB import Dot1agCfmMpDirection_Enum
from ydk.models.ieee8021.IEEE8021_TC_MIB import IEEE8021ServiceSelectorType_Enum
from ydk.models.snmpv2.SNMPv2_TC import RowStatus_Enum


class IEEE8021CFMV2MIB(object):
    """
    
    
    .. attribute:: ieee8021cfmconfigerrorlisttable
    
    	The CFM Configuration Error List table provides a list of Interfaces and VIDs that are incorrectly configured
    	**type**\: :py:class:`Ieee8021CfmConfigErrorListTable <ydk.models.ieee8021.IEEE8021_CFM_V2_MIB.IEEE8021CFMV2MIB.Ieee8021CfmConfigErrorListTable>`
    
    .. attribute:: ieee8021cfmdefaultmdtable
    
    	For each bridge component, the Default MD Level Managed Object controls MHF creation for VIDs that are not attached to a specific Maintenance Association Managed Object, and Sender ID TLV transmission by those MHFs.  For each Bridge Port, and for each VLAN ID whose data can pass through that Bridge Port, an entry in this table is used by the algorithm in subclause 22.2.3 only if there is no entry in the Maintenance Association table defining an MA for the same VLAN ID and MD Level as this table's entry, and on which MA an Up MEP is defined.  If there exists such an MA, that MA's objects are used by the algorithm in subclause 22.2.3 in place of this table entry's objects.  The agent maintains the value of ieee8021CfmDefaultMdStatus to indicate whether this entry is overridden by an MA.  When first initialized, the agent creates this table automatically with entries for all VLAN IDs, with the default values specified for each object.  After this initialization, the writable objects in this table need to be persistent upon reboot or restart of a device
    	**type**\: :py:class:`Ieee8021CfmDefaultMdTable <ydk.models.ieee8021.IEEE8021_CFM_V2_MIB.IEEE8021CFMV2MIB.Ieee8021CfmDefaultMdTable>`
    
    .. attribute:: ieee8021cfmmacomptable
    
    	The Maintenance Association table.  Each row in the table represents an MA.  An MA is a set of MEPs, each configured with a single service instance.  This is the part of the complete MA table that is variable across the Bridges in a Maintenance Domain, or across the components of a single Bridge.  That part of the MA table that is constant across the Bridges and their components in a Maintenance Domain is contained in the ieee8021CfmMaNetTable.  This table uses three indices, first index is the IEEE8021PbbComponentIdentifier that identifies the component within the Bridge for which the information in the ieee8021CfmMaCompEntry applies.  The second is the index of the Maintenance Domain table.  The third index is the same as the index of the ieee8021CfmMaNetEntry for the same MA.  The writable objects in this table need to be persistent upon reboot or restart of a device
    	**type**\: :py:class:`Ieee8021CfmMaCompTable <ydk.models.ieee8021.IEEE8021_CFM_V2_MIB.IEEE8021CFMV2MIB.Ieee8021CfmMaCompTable>`
    
    .. attribute:: ieee8021cfmstacktable
    
    	There is one CFM Stack table per bridge. It permits the retrieval of information about the Maintenance Points configured on any given interface
    	**type**\: :py:class:`Ieee8021CfmStackTable <ydk.models.ieee8021.IEEE8021_CFM_V2_MIB.IEEE8021CFMV2MIB.Ieee8021CfmStackTable>`
    
    .. attribute:: ieee8021cfmvlantable
    
    	This table defines the association of VIDs into VLANs.  There is an entry in this table, for each component of the bridge, for each VID that is\:     a) a VID belonging to a VLAN associated with more than        one VID; and     b) not the Primary VLAN of that VID. The entry in this table contains the Primary VID of the VLAN.  By default, this table is empty, meaning that every VID is the Primary VID of a single\-VID VLAN.  VLANs that are associated with only one VID SHOULD NOT have an entry in this table.  The writable objects in this table need to be persistent upon reboot or restart of a device
    	**type**\: :py:class:`Ieee8021CfmVlanTable <ydk.models.ieee8021.IEEE8021_CFM_V2_MIB.IEEE8021CFMV2MIB.Ieee8021CfmVlanTable>`
    
    

    """

    _prefix = 'ieee8021-cfm-v2'
    _revision = '2008-10-15'

    def __init__(self):
        self.ieee8021cfmconfigerrorlisttable = IEEE8021CFMV2MIB.Ieee8021CfmConfigErrorListTable()
        self.ieee8021cfmconfigerrorlisttable.parent = self
        self.ieee8021cfmdefaultmdtable = IEEE8021CFMV2MIB.Ieee8021CfmDefaultMdTable()
        self.ieee8021cfmdefaultmdtable.parent = self
        self.ieee8021cfmmacomptable = IEEE8021CFMV2MIB.Ieee8021CfmMaCompTable()
        self.ieee8021cfmmacomptable.parent = self
        self.ieee8021cfmstacktable = IEEE8021CFMV2MIB.Ieee8021CfmStackTable()
        self.ieee8021cfmstacktable.parent = self
        self.ieee8021cfmvlantable = IEEE8021CFMV2MIB.Ieee8021CfmVlanTable()
        self.ieee8021cfmvlantable.parent = self


    class Ieee8021CfmConfigErrorListTable(object):
        """
        The CFM Configuration Error List table provides a list of
        Interfaces and VIDs that are incorrectly configured.
        
        .. attribute:: ieee8021cfmconfigerrorlistentry
        
        	The Config Error List Table  entry
        	**type**\: list of :py:class:`Ieee8021CfmConfigErrorListEntry <ydk.models.ieee8021.IEEE8021_CFM_V2_MIB.IEEE8021CFMV2MIB.Ieee8021CfmConfigErrorListTable.Ieee8021CfmConfigErrorListEntry>`
        
        

        """

        _prefix = 'ieee8021-cfm-v2'
        _revision = '2008-10-15'

        def __init__(self):
            self.parent = None
            self.ieee8021cfmconfigerrorlistentry = YList()
            self.ieee8021cfmconfigerrorlistentry.parent = self
            self.ieee8021cfmconfigerrorlistentry.name = 'ieee8021cfmconfigerrorlistentry'


        class Ieee8021CfmConfigErrorListEntry(object):
            """
            The Config Error List Table  entry
            
            .. attribute:: ieee8021cfmconfigerrorlistifindex
            
            	This object is the IfIndex of the interface.  Upon a restart of the system, the system SHALL, if necessary, change the value of this variable so that it indexes the entry in the interface table with the same value of ifAlias that it indexed before the system restart.  If no such entry exists, then the system SHALL delete any entries in ieee8021CfmConfigErrorListTable indexed by that InterfaceIndex value
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: ieee8021cfmconfigerrorlistselector
            
            	The Service Selector Identifier of the Service with interfaces in error. See IEEE8021ServiceSelectorValue for details
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: ieee8021cfmconfigerrorlistselectortype
            
            	Type of the Service Selector identifier indicated by ieee8021CfmConfigErrorListSelector. See textual  convention IEEE8021ServiceSelectorType for details
            	**type**\: :py:class:`IEEE8021ServiceSelectorType_Enum <ydk.models.ieee8021.IEEE8021_TC_MIB.IEEE8021ServiceSelectorType_Enum>`
            
            .. attribute:: ieee8021cfmconfigerrorlisterrortype
            
            	A vector of Boolean error conditions from 22.2.4, any of which may be true\:  0) CFMleak; 1) ConflictingVids; 2) ExcessiveLevels; 3) OverlappedLevels
            	**type**\: :py:class:`Dot1agCfmConfigErrors_Bits <ydk.models.ieee8021.IEEE8021_CFM_MIB.Dot1agCfmConfigErrors_Bits>`
            
            

            """

            _prefix = 'ieee8021-cfm-v2'
            _revision = '2008-10-15'

            def __init__(self):
                self.parent = None
                self.ieee8021cfmconfigerrorlistifindex = None
                self.ieee8021cfmconfigerrorlistselector = None
                self.ieee8021cfmconfigerrorlistselectortype = None
                self.ieee8021cfmconfigerrorlisterrortype = Dot1agCfmConfigErrors_Bits()

            @property
            def _common_path(self):
                if self.ieee8021cfmconfigerrorlistifindex is None:
                    raise YPYDataValidationError('Key property ieee8021cfmconfigerrorlistifindex is None')
                if self.ieee8021cfmconfigerrorlistselector is None:
                    raise YPYDataValidationError('Key property ieee8021cfmconfigerrorlistselector is None')
                if self.ieee8021cfmconfigerrorlistselectortype is None:
                    raise YPYDataValidationError('Key property ieee8021cfmconfigerrorlistselectortype is None')

                return '/IEEE8021-CFM-V2-MIB:IEEE8021-CFM-V2-MIB/IEEE8021-CFM-V2-MIB:ieee8021CfmConfigErrorListTable/IEEE8021-CFM-V2-MIB:ieee8021CfmConfigErrorListEntry[IEEE8021-CFM-V2-MIB:ieee8021CfmConfigErrorListIfIndex = ' + str(self.ieee8021cfmconfigerrorlistifindex) + '][IEEE8021-CFM-V2-MIB:ieee8021CfmConfigErrorListSelector = ' + str(self.ieee8021cfmconfigerrorlistselector) + '][IEEE8021-CFM-V2-MIB:ieee8021CfmConfigErrorListSelectorType = ' + str(self.ieee8021cfmconfigerrorlistselectortype) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ieee8021cfmconfigerrorlistifindex is not None:
                    return True

                if self.ieee8021cfmconfigerrorlistselector is not None:
                    return True

                if self.ieee8021cfmconfigerrorlistselectortype is not None:
                    return True

                if self.ieee8021cfmconfigerrorlisterrortype is not None:
                    if self.ieee8021cfmconfigerrorlisterrortype._has_data():
                        return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ieee8021._meta import _IEEE8021_CFM_V2_MIB as meta
                return meta._meta_table['IEEE8021CFMV2MIB.Ieee8021CfmConfigErrorListTable.Ieee8021CfmConfigErrorListEntry']['meta_info']

        @property
        def _common_path(self):

            return '/IEEE8021-CFM-V2-MIB:IEEE8021-CFM-V2-MIB/IEEE8021-CFM-V2-MIB:ieee8021CfmConfigErrorListTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ieee8021cfmconfigerrorlistentry is not None:
                for child_ref in self.ieee8021cfmconfigerrorlistentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ieee8021._meta import _IEEE8021_CFM_V2_MIB as meta
            return meta._meta_table['IEEE8021CFMV2MIB.Ieee8021CfmConfigErrorListTable']['meta_info']


    class Ieee8021CfmDefaultMdTable(object):
        """
        For each bridge component, the Default MD Level Managed Object
        controls MHF creation for VIDs that are not attached to a
        specific Maintenance Association Managed Object, and Sender ID
        TLV transmission by those MHFs.
        
        For each Bridge Port, and for each VLAN ID whose data can
        pass through that Bridge Port, an entry in this table is
        used by the algorithm in subclause 22.2.3 only if there is no
        entry in the Maintenance Association table defining an MA
        for the same VLAN ID and MD Level as this table's entry, and
        on which MA an Up MEP is defined.  If there exists such an
        MA, that MA's objects are used by the algorithm in
        subclause 22.2.3 in place of this table entry's objects.  The
        agent maintains the value of ieee8021CfmDefaultMdStatus to
        indicate whether this entry is overridden by an MA.
        
        When first initialized, the agent creates this table
        automatically with entries for all VLAN IDs,
        with the default values specified for each object.
        
        After this initialization, the writable objects in this
        table need to be persistent upon reboot or restart of a
        device.
        
        .. attribute:: ieee8021cfmdefaultmdentry
        
        	The Default MD Level table entry
        	**type**\: list of :py:class:`Ieee8021CfmDefaultMdEntry <ydk.models.ieee8021.IEEE8021_CFM_V2_MIB.IEEE8021CFMV2MIB.Ieee8021CfmDefaultMdTable.Ieee8021CfmDefaultMdEntry>`
        
        

        """

        _prefix = 'ieee8021-cfm-v2'
        _revision = '2008-10-15'

        def __init__(self):
            self.parent = None
            self.ieee8021cfmdefaultmdentry = YList()
            self.ieee8021cfmdefaultmdentry.parent = self
            self.ieee8021cfmdefaultmdentry.name = 'ieee8021cfmdefaultmdentry'


        class Ieee8021CfmDefaultMdEntry(object):
            """
            The Default MD Level table entry.
            
            .. attribute:: ieee8021cfmdefaultmdcomponentid
            
            	The bridge component within the system to which the information in this ieee8021CfmDefaultMdEntry applies.  If the system is not a Bridge, or if only one component is present in the Bridge, then this variable (index) MUST be equal to 1
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: ieee8021cfmdefaultmdprimaryselector
            
            	Primary Service Selector identifier of a Service Instance with  no MA configured. See IEEE8021ServiceSelectorValue for details
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: ieee8021cfmdefaultmdprimaryselectortype
            
            	Type of the Primary Service Selector identifier indicated by  ieee8021CfmDefaultMdPrimarySelector. See textual convention IEEE8021ServiceSelectorType for details
            	**type**\: :py:class:`IEEE8021ServiceSelectorType_Enum <ydk.models.ieee8021.IEEE8021_TC_MIB.IEEE8021ServiceSelectorType_Enum>`
            
            .. attribute:: ieee8021cfmdefaultmdidpermission
            
            	Enumerated value indicating what, if anything, is to be included in the Sender ID TLV (21.5.3) transmitted by MHFs created by the Default Maintenance Domain.  If this object has the value sendIdDefer, Sender ID TLV transmission for this VLAN is controlled by ieee8021CfmDefaultMdDefIdPermission.  The value of this variable is meaningless if the values of ieee8021CfmDefaultMdStatus is false
            	**type**\: :py:class:`Dot1agCfmIdPermission_Enum <ydk.models.ieee8021.IEEE8021_CFM_MIB.Dot1agCfmIdPermission_Enum>`
            
            .. attribute:: ieee8021cfmdefaultmdlevel
            
            	A value indicating the MD Level at which MHFs are to be created, and Sender ID TLV transmission by those MHFs is to be controlled, for the VLAN to which this entry's objects apply.  If this object has the value \-1, the MD Level for MHF creation for this VLAN is controlled by ieee8021CfmDefaultMdDefLevel
            	**type**\: int
            
            	**range:** \-1..7
            
            .. attribute:: ieee8021cfmdefaultmdmhfcreation
            
            	A value indicating if the Management entity can create MHFs (MIP Half Function) for this VID at this MD Level.  If this object has the value defMHFdefer, MHF creation for this VLAN is controlled by ieee8021CfmDefaultMdDefMhfCreation.  The value of this variable is meaningless if the values of ieee8021CfmDefaultMdStatus is false
            	**type**\: :py:class:`Dot1agCfmMhfCreation_Enum <ydk.models.ieee8021.IEEE8021_CFM_MIB.Dot1agCfmMhfCreation_Enum>`
            
            .. attribute:: ieee8021cfmdefaultmdstatus
            
            	State of this Default MD Level table entry.  True if there is no entry in the Maintenance Association table defining an MA for the same VLAN ID and MD Level as this table's entry, and on which MA an Up MEP is defined, else false
            	**type**\: bool
            
            

            """

            _prefix = 'ieee8021-cfm-v2'
            _revision = '2008-10-15'

            def __init__(self):
                self.parent = None
                self.ieee8021cfmdefaultmdcomponentid = None
                self.ieee8021cfmdefaultmdprimaryselector = None
                self.ieee8021cfmdefaultmdprimaryselectortype = None
                self.ieee8021cfmdefaultmdidpermission = None
                self.ieee8021cfmdefaultmdlevel = None
                self.ieee8021cfmdefaultmdmhfcreation = None
                self.ieee8021cfmdefaultmdstatus = None

            @property
            def _common_path(self):
                if self.ieee8021cfmdefaultmdcomponentid is None:
                    raise YPYDataValidationError('Key property ieee8021cfmdefaultmdcomponentid is None')
                if self.ieee8021cfmdefaultmdprimaryselector is None:
                    raise YPYDataValidationError('Key property ieee8021cfmdefaultmdprimaryselector is None')
                if self.ieee8021cfmdefaultmdprimaryselectortype is None:
                    raise YPYDataValidationError('Key property ieee8021cfmdefaultmdprimaryselectortype is None')

                return '/IEEE8021-CFM-V2-MIB:IEEE8021-CFM-V2-MIB/IEEE8021-CFM-V2-MIB:ieee8021CfmDefaultMdTable/IEEE8021-CFM-V2-MIB:ieee8021CfmDefaultMdEntry[IEEE8021-CFM-V2-MIB:ieee8021CfmDefaultMdComponentId = ' + str(self.ieee8021cfmdefaultmdcomponentid) + '][IEEE8021-CFM-V2-MIB:ieee8021CfmDefaultMdPrimarySelector = ' + str(self.ieee8021cfmdefaultmdprimaryselector) + '][IEEE8021-CFM-V2-MIB:ieee8021CfmDefaultMdPrimarySelectorType = ' + str(self.ieee8021cfmdefaultmdprimaryselectortype) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ieee8021cfmdefaultmdcomponentid is not None:
                    return True

                if self.ieee8021cfmdefaultmdprimaryselector is not None:
                    return True

                if self.ieee8021cfmdefaultmdprimaryselectortype is not None:
                    return True

                if self.ieee8021cfmdefaultmdidpermission is not None:
                    return True

                if self.ieee8021cfmdefaultmdlevel is not None:
                    return True

                if self.ieee8021cfmdefaultmdmhfcreation is not None:
                    return True

                if self.ieee8021cfmdefaultmdstatus is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ieee8021._meta import _IEEE8021_CFM_V2_MIB as meta
                return meta._meta_table['IEEE8021CFMV2MIB.Ieee8021CfmDefaultMdTable.Ieee8021CfmDefaultMdEntry']['meta_info']

        @property
        def _common_path(self):

            return '/IEEE8021-CFM-V2-MIB:IEEE8021-CFM-V2-MIB/IEEE8021-CFM-V2-MIB:ieee8021CfmDefaultMdTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ieee8021cfmdefaultmdentry is not None:
                for child_ref in self.ieee8021cfmdefaultmdentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ieee8021._meta import _IEEE8021_CFM_V2_MIB as meta
            return meta._meta_table['IEEE8021CFMV2MIB.Ieee8021CfmDefaultMdTable']['meta_info']


    class Ieee8021CfmMaCompTable(object):
        """
        The Maintenance Association table.  Each row in the table
        represents an MA.  An MA is a set of MEPs, each configured
        with a single service instance.
        
        This is the part of the complete MA table that is variable
        across the Bridges in a Maintenance Domain, or across the
        components of a single Bridge.  That part of the MA table that
        is constant across the Bridges and their components in a
        Maintenance Domain is contained in the ieee8021CfmMaNetTable.
        
        This table uses three indices, first index is the
        IEEE8021PbbComponentIdentifier that identifies the component
        within the Bridge for which the information in the
        ieee8021CfmMaCompEntry applies.  The second is the index of the
        Maintenance Domain table.  The third index is the same as the
        index of the ieee8021CfmMaNetEntry for the same MA.
        
        The writable objects in this table need to be persistent
        upon reboot or restart of a device.
        
        .. attribute:: ieee8021cfmmacompentry
        
        	The MA table entry
        	**type**\: list of :py:class:`Ieee8021CfmMaCompEntry <ydk.models.ieee8021.IEEE8021_CFM_V2_MIB.IEEE8021CFMV2MIB.Ieee8021CfmMaCompTable.Ieee8021CfmMaCompEntry>`
        
        

        """

        _prefix = 'ieee8021-cfm-v2'
        _revision = '2008-10-15'

        def __init__(self):
            self.parent = None
            self.ieee8021cfmmacompentry = YList()
            self.ieee8021cfmmacompentry.parent = self
            self.ieee8021cfmmacompentry.name = 'ieee8021cfmmacompentry'


        class Ieee8021CfmMaCompEntry(object):
            """
            The MA table entry.
            
            .. attribute:: dot1agcfmmaindex
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: dot1agcfmmdindex
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: ieee8021cfmmacomponentid
            
            	The bridge component within the system to which the information in this ieee8021CfmMaCompEntry applies.  If the system is not a Bridge, or if only one component is present in the Bridge, then this variable (index) MUST be equal to 1
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: ieee8021cfmmacompidpermission
            
            	Enumerated value indicating what, if anything, is to be included in the Sender ID TLV (21.5.3) transmitted by MPs configured in this MA
            	**type**\: :py:class:`Dot1agCfmIdPermission_Enum <ydk.models.ieee8021.IEEE8021_CFM_MIB.Dot1agCfmIdPermission_Enum>`
            
            .. attribute:: ieee8021cfmmacompmhfcreation
            
            	Indicates if the Management entity can create MHFs (MIP Half Function) for this MA
            	**type**\: :py:class:`Dot1agCfmMhfCreation_Enum <ydk.models.ieee8021.IEEE8021_CFM_MIB.Dot1agCfmMhfCreation_Enum>`
            
            .. attribute:: ieee8021cfmmacompnumberofvids
            
            	The number of VIDs associated with the MA
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ieee8021cfmmacompprimaryselectorornone
            
            	Service Selector identifier to which the MP is attached, or 0, if none. If the MA is associated with more than one Service Selectors Identifiers, the ieee8021CfmVlanTable lists them
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ieee8021cfmmacompprimaryselectortype
            
            	Type of the Service Selector identifiers indicated by  ieee8021CfmMaCompPrimarySelectorOrNone. If the service instance is defined by more  than one Service Selector, this parameter also indicates the type of the  ieee8021CfmVlanPrimarySelector and ieee8021CfmVlanSelector in the ieee8021CfmVlanTable.  In Services instances made of multiple Service Selector identifiers, ensures that the type of the Service selector identifiers is the same. See textual convention  Dot1agCfmServiceSelectorType for details
            	**type**\: :py:class:`IEEE8021ServiceSelectorType_Enum <ydk.models.ieee8021.IEEE8021_TC_MIB.IEEE8021ServiceSelectorType_Enum>`
            
            .. attribute:: ieee8021cfmmacomprowstatus
            
            	The status of the row.  The writable columns in a row can not be changed if the row is active. All columns MUST have a valid value before a row can be activated
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            

            """

            _prefix = 'ieee8021-cfm-v2'
            _revision = '2008-10-15'

            def __init__(self):
                self.parent = None
                self.dot1agcfmmaindex = None
                self.dot1agcfmmdindex = None
                self.ieee8021cfmmacomponentid = None
                self.ieee8021cfmmacompidpermission = None
                self.ieee8021cfmmacompmhfcreation = None
                self.ieee8021cfmmacompnumberofvids = None
                self.ieee8021cfmmacompprimaryselectorornone = None
                self.ieee8021cfmmacompprimaryselectortype = None
                self.ieee8021cfmmacomprowstatus = None

            @property
            def _common_path(self):
                if self.dot1agcfmmaindex is None:
                    raise YPYDataValidationError('Key property dot1agcfmmaindex is None')
                if self.dot1agcfmmdindex is None:
                    raise YPYDataValidationError('Key property dot1agcfmmdindex is None')
                if self.ieee8021cfmmacomponentid is None:
                    raise YPYDataValidationError('Key property ieee8021cfmmacomponentid is None')

                return '/IEEE8021-CFM-V2-MIB:IEEE8021-CFM-V2-MIB/IEEE8021-CFM-V2-MIB:ieee8021CfmMaCompTable/IEEE8021-CFM-V2-MIB:ieee8021CfmMaCompEntry[IEEE8021-CFM-V2-MIB:dot1agCfmMaIndex = ' + str(self.dot1agcfmmaindex) + '][IEEE8021-CFM-V2-MIB:dot1agCfmMdIndex = ' + str(self.dot1agcfmmdindex) + '][IEEE8021-CFM-V2-MIB:ieee8021CfmMaComponentId = ' + str(self.ieee8021cfmmacomponentid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.dot1agcfmmaindex is not None:
                    return True

                if self.dot1agcfmmdindex is not None:
                    return True

                if self.ieee8021cfmmacomponentid is not None:
                    return True

                if self.ieee8021cfmmacompidpermission is not None:
                    return True

                if self.ieee8021cfmmacompmhfcreation is not None:
                    return True

                if self.ieee8021cfmmacompnumberofvids is not None:
                    return True

                if self.ieee8021cfmmacompprimaryselectorornone is not None:
                    return True

                if self.ieee8021cfmmacompprimaryselectortype is not None:
                    return True

                if self.ieee8021cfmmacomprowstatus is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ieee8021._meta import _IEEE8021_CFM_V2_MIB as meta
                return meta._meta_table['IEEE8021CFMV2MIB.Ieee8021CfmMaCompTable.Ieee8021CfmMaCompEntry']['meta_info']

        @property
        def _common_path(self):

            return '/IEEE8021-CFM-V2-MIB:IEEE8021-CFM-V2-MIB/IEEE8021-CFM-V2-MIB:ieee8021CfmMaCompTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ieee8021cfmmacompentry is not None:
                for child_ref in self.ieee8021cfmmacompentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ieee8021._meta import _IEEE8021_CFM_V2_MIB as meta
            return meta._meta_table['IEEE8021CFMV2MIB.Ieee8021CfmMaCompTable']['meta_info']


    class Ieee8021CfmStackTable(object):
        """
        There is one CFM Stack table per bridge. It permits
        the retrieval of information about the Maintenance Points
        configured on any given interface.
        
        .. attribute:: ieee8021cfmstackentry
        
        	The Stack table entry
        	**type**\: list of :py:class:`Ieee8021CfmStackEntry <ydk.models.ieee8021.IEEE8021_CFM_V2_MIB.IEEE8021CFMV2MIB.Ieee8021CfmStackTable.Ieee8021CfmStackEntry>`
        
        

        """

        _prefix = 'ieee8021-cfm-v2'
        _revision = '2008-10-15'

        def __init__(self):
            self.parent = None
            self.ieee8021cfmstackentry = YList()
            self.ieee8021cfmstackentry.parent = self
            self.ieee8021cfmstackentry.name = 'ieee8021cfmstackentry'


        class Ieee8021CfmStackEntry(object):
            """
            The Stack table entry
            
            .. attribute:: ieee8021cfmstackdirection
            
            	Direction in which the MP faces on the Bridge Port
            	**type**\: :py:class:`Dot1agCfmMpDirection_Enum <ydk.models.ieee8021.IEEE8021_CFM_MIB.Dot1agCfmMpDirection_Enum>`
            
            .. attribute:: ieee8021cfmstackifindex
            
            	This object represents the  Bridge Port or aggregated port on which MEPs or MHFs might be configured.  Upon a restart of the system, the system SHALL, if necessary, change the value of this variable, and  rearrange the ieee8021CfmStackTable, so that it indexes the entry in the interface table with the same value of ifAlias that it indexed before the system restart.  If no such entry exists, then the system SHALL delete all entries in the ieee8021CfmStackTable with the interface index
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: ieee8021cfmstackmdlevel
            
            	MD Level of the Maintenance Point
            	**type**\: int
            
            	**range:** 0..7
            
            .. attribute:: ieee8021cfmstackserviceselectorornone
            
            	Service Selector identifier to which the MP is attached, or 0, if none. See textual convention IEEE8021ServiceSelectorValue for details
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ieee8021cfmstackserviceselectortype
            
            	Type of the Service Selector identifier indicated by ieee8021CfmStackServiceSelectorOrNone. See textual convention IEEE8021ServiceSelectorType for details
            	**type**\: :py:class:`IEEE8021ServiceSelectorType_Enum <ydk.models.ieee8021.IEEE8021_TC_MIB.IEEE8021ServiceSelectorType_Enum>`
            
            .. attribute:: ieee8021cfmstackmacaddress
            
            	MAC address of the MP
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: ieee8021cfmstackmaindex
            
            	The index of the MA in the ieee8021CfmMaNetTable and ieee8021CfmMaCompTable to which the MP is associated, or 0, if none
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ieee8021cfmstackmdindex
            
            	The index of the Maintenance Domain in the ieee8021CfmMdTable to which the MP is associated, or 0, if none
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ieee8021cfmstackmepid
            
            	If an MEP is configured, the MEPID, else 0
            	**type**\: int
            
            	**range:** 0..8191
            
            

            """

            _prefix = 'ieee8021-cfm-v2'
            _revision = '2008-10-15'

            def __init__(self):
                self.parent = None
                self.ieee8021cfmstackdirection = None
                self.ieee8021cfmstackifindex = None
                self.ieee8021cfmstackmdlevel = None
                self.ieee8021cfmstackserviceselectorornone = None
                self.ieee8021cfmstackserviceselectortype = None
                self.ieee8021cfmstackmacaddress = None
                self.ieee8021cfmstackmaindex = None
                self.ieee8021cfmstackmdindex = None
                self.ieee8021cfmstackmepid = None

            @property
            def _common_path(self):
                if self.ieee8021cfmstackdirection is None:
                    raise YPYDataValidationError('Key property ieee8021cfmstackdirection is None')
                if self.ieee8021cfmstackifindex is None:
                    raise YPYDataValidationError('Key property ieee8021cfmstackifindex is None')
                if self.ieee8021cfmstackmdlevel is None:
                    raise YPYDataValidationError('Key property ieee8021cfmstackmdlevel is None')
                if self.ieee8021cfmstackserviceselectorornone is None:
                    raise YPYDataValidationError('Key property ieee8021cfmstackserviceselectorornone is None')
                if self.ieee8021cfmstackserviceselectortype is None:
                    raise YPYDataValidationError('Key property ieee8021cfmstackserviceselectortype is None')

                return '/IEEE8021-CFM-V2-MIB:IEEE8021-CFM-V2-MIB/IEEE8021-CFM-V2-MIB:ieee8021CfmStackTable/IEEE8021-CFM-V2-MIB:ieee8021CfmStackEntry[IEEE8021-CFM-V2-MIB:ieee8021CfmStackDirection = ' + str(self.ieee8021cfmstackdirection) + '][IEEE8021-CFM-V2-MIB:ieee8021CfmStackifIndex = ' + str(self.ieee8021cfmstackifindex) + '][IEEE8021-CFM-V2-MIB:ieee8021CfmStackMdLevel = ' + str(self.ieee8021cfmstackmdlevel) + '][IEEE8021-CFM-V2-MIB:ieee8021CfmStackServiceSelectorOrNone = ' + str(self.ieee8021cfmstackserviceselectorornone) + '][IEEE8021-CFM-V2-MIB:ieee8021CfmStackServiceSelectorType = ' + str(self.ieee8021cfmstackserviceselectortype) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ieee8021cfmstackdirection is not None:
                    return True

                if self.ieee8021cfmstackifindex is not None:
                    return True

                if self.ieee8021cfmstackmdlevel is not None:
                    return True

                if self.ieee8021cfmstackserviceselectorornone is not None:
                    return True

                if self.ieee8021cfmstackserviceselectortype is not None:
                    return True

                if self.ieee8021cfmstackmacaddress is not None:
                    return True

                if self.ieee8021cfmstackmaindex is not None:
                    return True

                if self.ieee8021cfmstackmdindex is not None:
                    return True

                if self.ieee8021cfmstackmepid is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ieee8021._meta import _IEEE8021_CFM_V2_MIB as meta
                return meta._meta_table['IEEE8021CFMV2MIB.Ieee8021CfmStackTable.Ieee8021CfmStackEntry']['meta_info']

        @property
        def _common_path(self):

            return '/IEEE8021-CFM-V2-MIB:IEEE8021-CFM-V2-MIB/IEEE8021-CFM-V2-MIB:ieee8021CfmStackTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ieee8021cfmstackentry is not None:
                for child_ref in self.ieee8021cfmstackentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ieee8021._meta import _IEEE8021_CFM_V2_MIB as meta
            return meta._meta_table['IEEE8021CFMV2MIB.Ieee8021CfmStackTable']['meta_info']


    class Ieee8021CfmVlanTable(object):
        """
        This table defines the association of VIDs into VLANs.  There
        is an entry in this table, for each component of the bridge,
        for each VID that is\:
            a) a VID belonging to a VLAN associated with more than
               one VID; and
            b) not the Primary VLAN of that VID.
        The entry in this table contains the Primary VID of the VLAN.
        
        By default, this table is empty, meaning that every VID is
        the Primary VID of a single\-VID VLAN.
        
        VLANs that are associated with only one VID SHOULD NOT have
        an entry in this table.
        
        The writable objects in this table need to be persistent
        upon reboot or restart of a device.
        
        .. attribute:: ieee8021cfmvlanentry
        
        	The VLAN table entry
        	**type**\: list of :py:class:`Ieee8021CfmVlanEntry <ydk.models.ieee8021.IEEE8021_CFM_V2_MIB.IEEE8021CFMV2MIB.Ieee8021CfmVlanTable.Ieee8021CfmVlanEntry>`
        
        

        """

        _prefix = 'ieee8021-cfm-v2'
        _revision = '2008-10-15'

        def __init__(self):
            self.parent = None
            self.ieee8021cfmvlanentry = YList()
            self.ieee8021cfmvlanentry.parent = self
            self.ieee8021cfmvlanentry.name = 'ieee8021cfmvlanentry'


        class Ieee8021CfmVlanEntry(object):
            """
            The VLAN table entry.
            
            .. attribute:: ieee8021cfmvlancomponentid
            
            	The bridge component within the system to which the information in this ieee8021CfmVlanEntry applies.  If the system is not a Bridge, or if only one component is present in the Bridge, then this variable (index) MUST be equal to 1
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: ieee8021cfmvlanselector
            
            	This is a service ID belonging to a service that is associated with more than one Service Selector identifiers, and this is not the Primary  Service ID of the service. The type of this Service Selector is the same as the primary Service Selector's type defined by ieee8021CfmMaCompPrimarySelectorType  in the ieee8021CfmMaCompTable
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: ieee8021cfmvlanprimaryselector
            
            	This is the Primary Service selector for a Service that is associated with more than one Service Selector identifiers. This value MUST not equal the value of ieee8021CfmVlanSelector. The type of this Service Selector is the same as the primary Service Selector's type defined by ieee8021CfmMaCompPrimarySelectorType  in the ieee8021CfmMaCompTable
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: ieee8021cfmvlanrowstatus
            
            	The status of the row.  The writable columns in a row can not be changed if the row is active. All columns MUST have a valid value before a row can be activated
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            

            """

            _prefix = 'ieee8021-cfm-v2'
            _revision = '2008-10-15'

            def __init__(self):
                self.parent = None
                self.ieee8021cfmvlancomponentid = None
                self.ieee8021cfmvlanselector = None
                self.ieee8021cfmvlanprimaryselector = None
                self.ieee8021cfmvlanrowstatus = None

            @property
            def _common_path(self):
                if self.ieee8021cfmvlancomponentid is None:
                    raise YPYDataValidationError('Key property ieee8021cfmvlancomponentid is None')
                if self.ieee8021cfmvlanselector is None:
                    raise YPYDataValidationError('Key property ieee8021cfmvlanselector is None')

                return '/IEEE8021-CFM-V2-MIB:IEEE8021-CFM-V2-MIB/IEEE8021-CFM-V2-MIB:ieee8021CfmVlanTable/IEEE8021-CFM-V2-MIB:ieee8021CfmVlanEntry[IEEE8021-CFM-V2-MIB:ieee8021CfmVlanComponentId = ' + str(self.ieee8021cfmvlancomponentid) + '][IEEE8021-CFM-V2-MIB:ieee8021CfmVlanSelector = ' + str(self.ieee8021cfmvlanselector) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ieee8021cfmvlancomponentid is not None:
                    return True

                if self.ieee8021cfmvlanselector is not None:
                    return True

                if self.ieee8021cfmvlanprimaryselector is not None:
                    return True

                if self.ieee8021cfmvlanrowstatus is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ieee8021._meta import _IEEE8021_CFM_V2_MIB as meta
                return meta._meta_table['IEEE8021CFMV2MIB.Ieee8021CfmVlanTable.Ieee8021CfmVlanEntry']['meta_info']

        @property
        def _common_path(self):

            return '/IEEE8021-CFM-V2-MIB:IEEE8021-CFM-V2-MIB/IEEE8021-CFM-V2-MIB:ieee8021CfmVlanTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ieee8021cfmvlanentry is not None:
                for child_ref in self.ieee8021cfmvlanentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ieee8021._meta import _IEEE8021_CFM_V2_MIB as meta
            return meta._meta_table['IEEE8021CFMV2MIB.Ieee8021CfmVlanTable']['meta_info']

    @property
    def _common_path(self):

        return '/IEEE8021-CFM-V2-MIB:IEEE8021-CFM-V2-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.ieee8021cfmconfigerrorlisttable is not None and self.ieee8021cfmconfigerrorlisttable._has_data():
            return True

        if self.ieee8021cfmconfigerrorlisttable is not None and self.ieee8021cfmconfigerrorlisttable.is_presence():
            return True

        if self.ieee8021cfmdefaultmdtable is not None and self.ieee8021cfmdefaultmdtable._has_data():
            return True

        if self.ieee8021cfmdefaultmdtable is not None and self.ieee8021cfmdefaultmdtable.is_presence():
            return True

        if self.ieee8021cfmmacomptable is not None and self.ieee8021cfmmacomptable._has_data():
            return True

        if self.ieee8021cfmmacomptable is not None and self.ieee8021cfmmacomptable.is_presence():
            return True

        if self.ieee8021cfmstacktable is not None and self.ieee8021cfmstacktable._has_data():
            return True

        if self.ieee8021cfmstacktable is not None and self.ieee8021cfmstacktable.is_presence():
            return True

        if self.ieee8021cfmvlantable is not None and self.ieee8021cfmvlantable._has_data():
            return True

        if self.ieee8021cfmvlantable is not None and self.ieee8021cfmvlantable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ieee8021._meta import _IEEE8021_CFM_V2_MIB as meta
        return meta._meta_table['IEEE8021CFMV2MIB']['meta_info']


