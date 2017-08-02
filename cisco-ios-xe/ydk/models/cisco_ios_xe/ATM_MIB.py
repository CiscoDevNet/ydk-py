""" ATM_MIB 

This is the MIB Module for ATM and AAL5\-related
objects for managing ATM interfaces, ATM virtual
links, ATM cross\-connects, AAL5 entities, and
and AAL5 connections.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class AtmMib(Entity):
    """
    
    
    .. attribute:: aal5vcctable
    
    	This table contains AAL5 VCC performance parameters
    	**type**\:   :py:class:`Aal5Vcctable <ydk.models.cisco_ios_xe.ATM_MIB.AtmMib.Aal5Vcctable>`
    
    .. attribute:: atminterfaceconftable
    
    	This table contains ATM local interface configuration parameters, one entry per ATM interface port
    	**type**\:   :py:class:`Atminterfaceconftable <ydk.models.cisco_ios_xe.ATM_MIB.AtmMib.Atminterfaceconftable>`
    
    .. attribute:: atminterfaceds3plcptable
    
    	This table contains ATM interface DS3 PLCP parameters and state variables, one entry per ATM interface port
    	**type**\:   :py:class:`Atminterfaceds3Plcptable <ydk.models.cisco_ios_xe.ATM_MIB.AtmMib.Atminterfaceds3Plcptable>`
    
    .. attribute:: atminterfacetctable
    
    	This table contains ATM interface TC Sublayer parameters and state variables, one entry per ATM interface port
    	**type**\:   :py:class:`Atminterfacetctable <ydk.models.cisco_ios_xe.ATM_MIB.AtmMib.Atminterfacetctable>`
    
    .. attribute:: atmmibobjects
    
    	
    	**type**\:   :py:class:`Atmmibobjects <ydk.models.cisco_ios_xe.ATM_MIB.AtmMib.Atmmibobjects>`
    
    .. attribute:: atmtrafficdescrparamtable
    
    	This table contains information on ATM traffic descriptor type and the associated parameters
    	**type**\:   :py:class:`Atmtrafficdescrparamtable <ydk.models.cisco_ios_xe.ATM_MIB.AtmMib.Atmtrafficdescrparamtable>`
    
    .. attribute:: atmvccrossconnecttable
    
    	The ATM VC Cross Connect table for PVCs. An entry in this table models two cross\-connected VCLs. Each VCL must have its atmConnKind set to pvc(1)
    	**type**\:   :py:class:`Atmvccrossconnecttable <ydk.models.cisco_ios_xe.ATM_MIB.AtmMib.Atmvccrossconnecttable>`
    
    .. attribute:: atmvcltable
    
    	The Virtual Channel Link (VCL) table.  A bi\-directional VCL is modeled as one entry in this table. This table can be used for PVCs, SVCs and Soft PVCs
    	**type**\:   :py:class:`Atmvcltable <ydk.models.cisco_ios_xe.ATM_MIB.AtmMib.Atmvcltable>`
    
    .. attribute:: atmvpcrossconnecttable
    
    	The ATM VP Cross Connect table for PVCs. An entry in this table models two cross\-connected VPLs. Each VPL must have its atmConnKind set to pvc(1)
    	**type**\:   :py:class:`Atmvpcrossconnecttable <ydk.models.cisco_ios_xe.ATM_MIB.AtmMib.Atmvpcrossconnecttable>`
    
    .. attribute:: atmvpltable
    
    	The Virtual Path Link (VPL) table.  A bi\-directional VPL is modeled as one entry in this table. This table can be used for PVCs, SVCs and Soft PVCs. Entries are not present in this table for the VPIs used by entries in the atmVclTable
    	**type**\:   :py:class:`Atmvpltable <ydk.models.cisco_ios_xe.ATM_MIB.AtmMib.Atmvpltable>`
    
    

    """

    _prefix = 'ATM-MIB'
    _revision = '1998-10-19'

    def __init__(self):
        super(AtmMib, self).__init__()
        self._top_entity = None

        self.yang_name = "ATM-MIB"
        self.yang_parent_name = "ATM-MIB"

        self.aal5vcctable = AtmMib.Aal5Vcctable()
        self.aal5vcctable.parent = self
        self._children_name_map["aal5vcctable"] = "aal5VccTable"
        self._children_yang_names.add("aal5VccTable")

        self.atminterfaceconftable = AtmMib.Atminterfaceconftable()
        self.atminterfaceconftable.parent = self
        self._children_name_map["atminterfaceconftable"] = "atmInterfaceConfTable"
        self._children_yang_names.add("atmInterfaceConfTable")

        self.atminterfaceds3plcptable = AtmMib.Atminterfaceds3Plcptable()
        self.atminterfaceds3plcptable.parent = self
        self._children_name_map["atminterfaceds3plcptable"] = "atmInterfaceDs3PlcpTable"
        self._children_yang_names.add("atmInterfaceDs3PlcpTable")

        self.atminterfacetctable = AtmMib.Atminterfacetctable()
        self.atminterfacetctable.parent = self
        self._children_name_map["atminterfacetctable"] = "atmInterfaceTCTable"
        self._children_yang_names.add("atmInterfaceTCTable")

        self.atmmibobjects = AtmMib.Atmmibobjects()
        self.atmmibobjects.parent = self
        self._children_name_map["atmmibobjects"] = "atmMIBObjects"
        self._children_yang_names.add("atmMIBObjects")

        self.atmtrafficdescrparamtable = AtmMib.Atmtrafficdescrparamtable()
        self.atmtrafficdescrparamtable.parent = self
        self._children_name_map["atmtrafficdescrparamtable"] = "atmTrafficDescrParamTable"
        self._children_yang_names.add("atmTrafficDescrParamTable")

        self.atmvccrossconnecttable = AtmMib.Atmvccrossconnecttable()
        self.atmvccrossconnecttable.parent = self
        self._children_name_map["atmvccrossconnecttable"] = "atmVcCrossConnectTable"
        self._children_yang_names.add("atmVcCrossConnectTable")

        self.atmvcltable = AtmMib.Atmvcltable()
        self.atmvcltable.parent = self
        self._children_name_map["atmvcltable"] = "atmVclTable"
        self._children_yang_names.add("atmVclTable")

        self.atmvpcrossconnecttable = AtmMib.Atmvpcrossconnecttable()
        self.atmvpcrossconnecttable.parent = self
        self._children_name_map["atmvpcrossconnecttable"] = "atmVpCrossConnectTable"
        self._children_yang_names.add("atmVpCrossConnectTable")

        self.atmvpltable = AtmMib.Atmvpltable()
        self.atmvpltable.parent = self
        self._children_name_map["atmvpltable"] = "atmVplTable"
        self._children_yang_names.add("atmVplTable")


    class Atmmibobjects(Entity):
        """
        
        
        .. attribute:: atmtrafficdescrparamindexnext
        
        	This object contains an appropriate value to be used for atmTrafficDescrParamIndex when creating entries in the atmTrafficDescrParamTable. The value 0 indicates that no unassigned entries are available. To obtain the atmTrafficDescrParamIndex value for a new entry, the manager issues a management protocol retrieval operation to obtain the current value of this object.  After each retrieval, the agent should modify the value to the next unassigned index. After a manager retrieves a value the agent will determine through its local policy when this index value will be made available for reuse
        	**type**\:  int
        
        	**range:** 0..2147483647
        
        .. attribute:: atmvccrossconnectindexnext
        
        	This object contains an appropriate value to be used for atmVcCrossConnectIndex when creating entries in the atmVcCrossConnectTable.  The value 0 indicates that no unassigned entries are available. To obtain the atmVcCrossConnectIndex value for a new entry, the manager issues a management protocol retrieval operation to obtain the current value of this object.  After each retrieval, the agent should modify the value to the next unassigned index. After a manager retrieves a value the agent will determine through its local policy when this index value will be made available for reuse
        	**type**\:  int
        
        	**range:** 0..2147483647
        
        .. attribute:: atmvpcrossconnectindexnext
        
        	This object contains an appropriate value to be used for atmVpCrossConnectIndex when creating entries in the atmVpCrossConnectTable.  The value 0 indicates that no unassigned entries are available. To obtain the atmVpCrossConnectIndex value for a new entry, the manager issues a management protocol retrieval operation to obtain the current value of this object.  After each retrieval, the agent should modify the value to the next unassigned index. After a manager retrieves a value the agent will determine through its local policy when this index value will be made available for reuse
        	**type**\:  int
        
        	**range:** 0..2147483647
        
        

        """

        _prefix = 'ATM-MIB'
        _revision = '1998-10-19'

        def __init__(self):
            super(AtmMib.Atmmibobjects, self).__init__()

            self.yang_name = "atmMIBObjects"
            self.yang_parent_name = "ATM-MIB"

            self.atmtrafficdescrparamindexnext = YLeaf(YType.int32, "atmTrafficDescrParamIndexNext")

            self.atmvccrossconnectindexnext = YLeaf(YType.int32, "atmVcCrossConnectIndexNext")

            self.atmvpcrossconnectindexnext = YLeaf(YType.int32, "atmVpCrossConnectIndexNext")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("atmtrafficdescrparamindexnext",
                            "atmvccrossconnectindexnext",
                            "atmvpcrossconnectindexnext") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(AtmMib.Atmmibobjects, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(AtmMib.Atmmibobjects, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.atmtrafficdescrparamindexnext.is_set or
                self.atmvccrossconnectindexnext.is_set or
                self.atmvpcrossconnectindexnext.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.atmtrafficdescrparamindexnext.yfilter != YFilter.not_set or
                self.atmvccrossconnectindexnext.yfilter != YFilter.not_set or
                self.atmvpcrossconnectindexnext.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "atmMIBObjects" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "ATM-MIB:ATM-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.atmtrafficdescrparamindexnext.is_set or self.atmtrafficdescrparamindexnext.yfilter != YFilter.not_set):
                leaf_name_data.append(self.atmtrafficdescrparamindexnext.get_name_leafdata())
            if (self.atmvccrossconnectindexnext.is_set or self.atmvccrossconnectindexnext.yfilter != YFilter.not_set):
                leaf_name_data.append(self.atmvccrossconnectindexnext.get_name_leafdata())
            if (self.atmvpcrossconnectindexnext.is_set or self.atmvpcrossconnectindexnext.yfilter != YFilter.not_set):
                leaf_name_data.append(self.atmvpcrossconnectindexnext.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "atmTrafficDescrParamIndexNext" or name == "atmVcCrossConnectIndexNext" or name == "atmVpCrossConnectIndexNext"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "atmTrafficDescrParamIndexNext"):
                self.atmtrafficdescrparamindexnext = value
                self.atmtrafficdescrparamindexnext.value_namespace = name_space
                self.atmtrafficdescrparamindexnext.value_namespace_prefix = name_space_prefix
            if(value_path == "atmVcCrossConnectIndexNext"):
                self.atmvccrossconnectindexnext = value
                self.atmvccrossconnectindexnext.value_namespace = name_space
                self.atmvccrossconnectindexnext.value_namespace_prefix = name_space_prefix
            if(value_path == "atmVpCrossConnectIndexNext"):
                self.atmvpcrossconnectindexnext = value
                self.atmvpcrossconnectindexnext.value_namespace = name_space
                self.atmvpcrossconnectindexnext.value_namespace_prefix = name_space_prefix


    class Atminterfaceconftable(Entity):
        """
        This table contains ATM local interface
        configuration parameters, one entry per ATM
        interface port.
        
        .. attribute:: atminterfaceconfentry
        
        	This list contains ATM interface configuration parameters and state variables and is indexed by ifIndex values of ATM interfaces
        	**type**\: list of    :py:class:`Atminterfaceconfentry <ydk.models.cisco_ios_xe.ATM_MIB.AtmMib.Atminterfaceconftable.Atminterfaceconfentry>`
        
        

        """

        _prefix = 'ATM-MIB'
        _revision = '1998-10-19'

        def __init__(self):
            super(AtmMib.Atminterfaceconftable, self).__init__()

            self.yang_name = "atmInterfaceConfTable"
            self.yang_parent_name = "ATM-MIB"

            self.atminterfaceconfentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(AtmMib.Atminterfaceconftable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(AtmMib.Atminterfaceconftable, self).__setattr__(name, value)


        class Atminterfaceconfentry(Entity):
            """
            This list contains ATM interface configuration
            parameters and state variables and is indexed
            by ifIndex values of ATM interfaces.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: atminterfaceaddresstype
            
            	The type of primary ATM address configured for use at this ATM interface
            	**type**\:   :py:class:`Atminterfaceaddresstype <ydk.models.cisco_ios_xe.ATM_MIB.AtmMib.Atminterfaceconftable.Atminterfaceconfentry.Atminterfaceaddresstype>`
            
            	**status**\: deprecated
            
            .. attribute:: atminterfaceadminaddress
            
            	The primary address assigned for administrative purposes, for example, an address associated with the service provider side of a public network UNI (thus, the value of this address corresponds with the value of ifPhysAddress at the host side). If this interface has no assigned administrative address, or when the address used for administrative purposes is the same as that used for ifPhysAddress, then this is an octet string of zero length
            	**type**\:  str
            
            	**status**\: deprecated
            
            .. attribute:: atminterfaceconfvccs
            
            	The number of VCCs (PVCC, Soft PVCC and SVCC) currently in use at this ATM interface.  It includes the number of PVCCs and Soft PVCCs that are configured at the interface, plus the number of SVCCs that are currently  established at the interface
            	**type**\:  int
            
            	**range:** 0..65536
            
            .. attribute:: atminterfaceconfvpcs
            
            	The number of VPCs (PVPC, Soft PVPC and SVPC) currently in use at this ATM interface.  It includes the number of PVPCs and Soft PVPCs that are configured at the interface, plus the number of SVPCs that are currently  established at the interface.  At the ATM UNI, the configured number of VPCs (PVPCs and SVPCs) can range from 0 to 256 only
            	**type**\:  int
            
            	**range:** 0..4096
            
            .. attribute:: atminterfacecurrentmaxvcibits
            
            	The maximum number of VCI Bits that may currently be used at this ATM interface. The value is the minimum of atmInterfaceMaxActiveVciBits, and the atmInterfaceMaxActiveVciBits of the interface's UNI/NNI peer.  If the interface does not negotiate with its peer to determine the number of VCI Bits that can be used on the interface, then the value of this object must equal atmInterfaceMaxActiveVciBits
            	**type**\:  int
            
            	**range:** 0..16
            
            .. attribute:: atminterfacecurrentmaxvpibits
            
            	The maximum number of VPI Bits that may currently be used at this ATM interface. The value is the minimum of atmInterfaceMaxActiveVpiBits, and the atmInterfaceMaxActiveVpiBits of the interface's UNI/NNI peer.  If the interface does not negotiate with its peer to determine the number of VPI Bits that can be used on the interface, then the value of this object must equal atmInterfaceMaxActiveVpiBits
            	**type**\:  int
            
            	**range:** 0..12
            
            .. attribute:: atminterfaceilmivci
            
            	The VCI value of the VCC supporting the ILMI at this ATM interface.  If the values of atmInterfaceIlmiVpi and atmInterfaceIlmiVci are both equal to zero then the ILMI is not supported at this ATM interface
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: atminterfaceilmivpi
            
            	The VPI value of the VCC supporting the ILMI at this ATM interface.  If the values of atmInterfaceIlmiVpi and atmInterfaceIlmiVci are both equal to zero then the ILMI is not supported at this ATM interface
            	**type**\:  int
            
            	**range:** 0..4095
            
            .. attribute:: atminterfacemaxactivevcibits
            
            	The maximum number of active VCI bits configured for use at this ATM interface
            	**type**\:  int
            
            	**range:** 0..16
            
            .. attribute:: atminterfacemaxactivevpibits
            
            	The  maximum number of active VPI bits configured for use at the ATM interface. At the ATM UNI, the maximum number of active VPI bits configured for use ranges from 0 to 8 only
            	**type**\:  int
            
            	**range:** 0..12
            
            .. attribute:: atminterfacemaxvccs
            
            	The maximum number of VCCs (PVCCs and SVCCs) supported at this ATM interface
            	**type**\:  int
            
            	**range:** 0..65536
            
            .. attribute:: atminterfacemaxvpcs
            
            	The maximum number of VPCs (PVPCs and SVPCs) supported at this ATM interface. At the ATM UNI, the maximum number of VPCs (PVPCs and SVPCs) ranges from 0 to 256 only
            	**type**\:  int
            
            	**range:** 0..4096
            
            .. attribute:: atminterfacemyneighborifname
            
            	The textual name of the interface on the neighbor system on the far end of this interface, and to which this interface connects.  If the neighbor system is manageable through SNMP and supports the object ifName, the value of this object must be identical with that of ifName for the ifEntry of the lowest level physical interface for this port.  If this interface does not have a textual name, the value of this object is a zero length string.  Note that the value of this object may be obtained in different ways, e.g., by manual configuration, or through ILMI interaction with the neighbor system
            	**type**\:  str
            
            .. attribute:: atminterfacemyneighboripaddress
            
            	The IP address of the neighbor system connected to the  far end of this interface, to which a Network Management Station can send SNMP messages, as IP datagrams sent to UDP port 161, in order to access network management information concerning the operation of that system.  Note that the value of this object may be obtained in different ways, e.g., by manual configuration, or through ILMI interaction with the neighbor system
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: atminterfacesubscraddress
            
            	The identifier assigned by a service provider to the network side of a public network UNI. If this interface has no assigned service provider address, or for other interfaces this is an octet string of zero length
            	**type**\:  str
            
            .. attribute:: atmintfcurrentlydowntouppvcls
            
            	The current number PVCLs on this interface which  changed state to 'up' since the last  atmIntPvcUpTrap was sent
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: atmintfcurrentlyfailingpvcls
            
            	The current number of VCLs on this interface for which there is an active row in the atmVclTable having an atmVclConnKind value of `pvc' and an atmVclOperStatus with a value other than `up'
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: atmintfcurrentlyoamfailingpvcls
            
            	The current number of PVCLs on this interface for which the oam loop back has failed but the status of each PVCL remain  in the 'up' state in the last notification interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: atmintfoamfailedpvcls
            
            	The total number of PVCLs in this interface which  are currently in the oam loopback failed condition but  the status of each PVCL remain in the 'up' state
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: atmintfpvcfailures
            
            	The number of times the operational status of a PVCL on this interface has gone down
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: atmintfpvcfailurestrapenable
            
            	Allows the generation of traps in response to PVCL failures on this interface
            	**type**\:  bool
            
            .. attribute:: atmintfpvcnotificationinterval
            
            	The minimum interval between the sending of cIntfPvcFailuresTrap notifications for this interface
            	**type**\:  int
            
            	**range:** 1..3600
            
            	**units**\: seconds
            
            .. attribute:: atmpreviouslyfailedpvclinterval
            
            	The interval for storing the failed time in atmPreviouslyFailedPVclTimeStamp
            	**type**\:  int
            
            	**range:** 0..3600
            
            	**units**\: seconds
            
            .. attribute:: catmintfaisrdioamfailedpvcls
            
            	The total number of PVCLs in this interface which  are currently in the AIS RDI OAM failed condition but  the status of each PVCL remain in the 'up' state
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmintfaisrdioamrcovedpvcls
            
            	The total number of PVCLs in this interface which  are currently in the AIS RDI OAM recovered condition and  the status of each PVCL is in the 'up' state
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmintfanyoamfailedpvcls
            
            	The total number of PVCLs in this interface which  are currently in any type of OAM failed condition but  the status of each PVCL remain in the 'up' state
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmintfanyoamrcovedpvcls
            
            	The total number of PVCLs in this interface which  are currently in any type of OAM recovered condition and  the status of each PVCL is in the 'up' state
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmintfcuraisrdioamfailingpvcls
            
            	The current number of PVCLs on this interface for which the AIS RDI OAM has failed but the status of each PVCL remain  in the 'up' state in the last notification interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmintfcuraisrdioamrcovingpvcls
            
            	The current number of PVCLs on this interface for which the AIS RDI OAM has recovered and the status of each PVCL is  in the 'up' state in the last notification interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmintfcuranyoamfailingpvcls
            
            	The current number of PVCLs on this interface for which  any of OAM has failed but the status of each PVCL remain  in the 'up' state in the last notification interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmintfcuranyoamrcovingpvcls
            
            	The current number of PVCLs on this interface for which  any of OAM has recovered and the status of each PVCL is  in the 'up' state in the last notification interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmintfcurendccoamfailingpvcls
            
            	The current number of PVCLs on this interface for which the End\-to\-End CC OAM has failed but the status of each PVCL  remain in the 'up' state in the last notification interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmintfcurendccoamrcovingpvcls
            
            	The current number of PVCLs on this interface for which the End\-to\-End CC OAM has recovered and the status of each PVCL  is in the 'up' state in the last notification interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmintfcurrentlydowntouppvcls
            
            	The current number PVCLs on this interface which  changed state to 'up' since the last  atmIntPvcUp2Trap was sent
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmintfcurrentoamfailingpvcls
            
            	The current number of PVCLs on this interface for which the OAM loop back has failed but the status of each PVCL remain  in the 'up' state in the last notification interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmintfcurrentoamrcovingpvcls
            
            	The current number of PVCLs on this interface for which the OAM loop back has recovered and the status of each PVCL is  in the 'up' state in the last notification interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmintfcursegccoamfailingpvcls
            
            	The current number of PVCLs on this interface for which the Segment CC OAM has failed but the status of each PVCL remain  in the 'up' state in the last notification interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmintfcursegccoamrcovingpvcls
            
            	The current number of PVCLs on this interface for which the Segment CC OAM has recovered and the status of each PVCL is  in the 'up' state in the last notification interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmintfendccoamfailedpvcls
            
            	The total number of PVCLs in this interface which  are currently in the End\-to\-End CC OAM failed condition  but the status of each PVCL remain in the 'up' state
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmintfendccoamrcovedpvcls
            
            	The total number of PVCLs in this interface which  are currently in the End\-to\-End CC OAM recovered condition  and the status of each PVCL is in the 'up' state
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmintfoamfailedpvcls
            
            	The total number of PVCLs in this interface which  are currently in the OAM loopback failed condition but  the status of each PVCL remain in the 'up' state
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmintfoamrcovedpvcls
            
            	The total number of PVCLs in this interface which  are currently in the OAM loopback recovered condition and  the status of each PVCL is in the 'up' state
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmintfsegccoamfailedpvcls
            
            	The total number of PVCLs in this interface which  are currently in the Segment CC OAM failed condition  but the status of each PVCL remain in the 'up' state
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmintfsegccoamrcovedpvcls
            
            	The total number of PVCLs in this interface which  are currently in the Segment CC OAM recovered condition  and the status of each PVCL is in the 'up' state
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmintftypeofoamfailure
            
            	Type of OAM failure
            	**type**\:   :py:class:`Catmoamfailuretype <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.Catmoamfailuretype>`
            
            .. attribute:: catmintftypeofoamrecover
            
            	Type of OAM Recovered
            	**type**\:   :py:class:`Catmoamrecoverytype <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.Catmoamrecoverytype>`
            
            

            """

            _prefix = 'ATM-MIB'
            _revision = '1998-10-19'

            def __init__(self):
                super(AtmMib.Atminterfaceconftable.Atminterfaceconfentry, self).__init__()

                self.yang_name = "atmInterfaceConfEntry"
                self.yang_parent_name = "atmInterfaceConfTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.atminterfaceaddresstype = YLeaf(YType.enumeration, "atmInterfaceAddressType")

                self.atminterfaceadminaddress = YLeaf(YType.str, "atmInterfaceAdminAddress")

                self.atminterfaceconfvccs = YLeaf(YType.int32, "atmInterfaceConfVccs")

                self.atminterfaceconfvpcs = YLeaf(YType.int32, "atmInterfaceConfVpcs")

                self.atminterfacecurrentmaxvcibits = YLeaf(YType.int32, "atmInterfaceCurrentMaxVciBits")

                self.atminterfacecurrentmaxvpibits = YLeaf(YType.int32, "atmInterfaceCurrentMaxVpiBits")

                self.atminterfaceilmivci = YLeaf(YType.int32, "atmInterfaceIlmiVci")

                self.atminterfaceilmivpi = YLeaf(YType.int32, "atmInterfaceIlmiVpi")

                self.atminterfacemaxactivevcibits = YLeaf(YType.int32, "atmInterfaceMaxActiveVciBits")

                self.atminterfacemaxactivevpibits = YLeaf(YType.int32, "atmInterfaceMaxActiveVpiBits")

                self.atminterfacemaxvccs = YLeaf(YType.int32, "atmInterfaceMaxVccs")

                self.atminterfacemaxvpcs = YLeaf(YType.int32, "atmInterfaceMaxVpcs")

                self.atminterfacemyneighborifname = YLeaf(YType.str, "atmInterfaceMyNeighborIfName")

                self.atminterfacemyneighboripaddress = YLeaf(YType.str, "atmInterfaceMyNeighborIpAddress")

                self.atminterfacesubscraddress = YLeaf(YType.str, "atmInterfaceSubscrAddress")

                self.atmintfcurrentlydowntouppvcls = YLeaf(YType.uint32, "CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN:atmIntfCurrentlyDownToUpPVcls")

                self.atmintfcurrentlyfailingpvcls = YLeaf(YType.uint32, "CISCO-IETF-ATM2-PVCTRAP-MIB:atmIntfCurrentlyFailingPVcls")

                self.atmintfcurrentlyoamfailingpvcls = YLeaf(YType.uint32, "CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN:atmIntfCurrentlyOAMFailingPVcls")

                self.atmintfoamfailedpvcls = YLeaf(YType.uint32, "CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN:atmIntfOAMFailedPVcls")

                self.atmintfpvcfailures = YLeaf(YType.uint32, "CISCO-IETF-ATM2-PVCTRAP-MIB:atmIntfPvcFailures")

                self.atmintfpvcfailurestrapenable = YLeaf(YType.boolean, "CISCO-IETF-ATM2-PVCTRAP-MIB:atmIntfPvcFailuresTrapEnable")

                self.atmintfpvcnotificationinterval = YLeaf(YType.int32, "CISCO-IETF-ATM2-PVCTRAP-MIB:atmIntfPvcNotificationInterval")

                self.atmpreviouslyfailedpvclinterval = YLeaf(YType.int32, "CISCO-IETF-ATM2-PVCTRAP-MIB:atmPreviouslyFailedPVclInterval")

                self.catmintfaisrdioamfailedpvcls = YLeaf(YType.uint32, "CISCO-ATM-PVCTRAP-EXTN-MIB:catmIntfAISRDIOAMFailedPVcls")

                self.catmintfaisrdioamrcovedpvcls = YLeaf(YType.uint32, "CISCO-ATM-PVCTRAP-EXTN-MIB:catmIntfAISRDIOAMRcovedPVcls")

                self.catmintfanyoamfailedpvcls = YLeaf(YType.uint32, "CISCO-ATM-PVCTRAP-EXTN-MIB:catmIntfAnyOAMFailedPVcls")

                self.catmintfanyoamrcovedpvcls = YLeaf(YType.uint32, "CISCO-ATM-PVCTRAP-EXTN-MIB:catmIntfAnyOAMRcovedPVcls")

                self.catmintfcuraisrdioamfailingpvcls = YLeaf(YType.uint32, "CISCO-ATM-PVCTRAP-EXTN-MIB:catmIntfCurAISRDIOAMFailingPVcls")

                self.catmintfcuraisrdioamrcovingpvcls = YLeaf(YType.uint32, "CISCO-ATM-PVCTRAP-EXTN-MIB:catmIntfCurAISRDIOAMRcovingPVcls")

                self.catmintfcuranyoamfailingpvcls = YLeaf(YType.uint32, "CISCO-ATM-PVCTRAP-EXTN-MIB:catmIntfCurAnyOAMFailingPVcls")

                self.catmintfcuranyoamrcovingpvcls = YLeaf(YType.uint32, "CISCO-ATM-PVCTRAP-EXTN-MIB:catmIntfCurAnyOAMRcovingPVcls")

                self.catmintfcurendccoamfailingpvcls = YLeaf(YType.uint32, "CISCO-ATM-PVCTRAP-EXTN-MIB:catmIntfCurEndCCOAMFailingPVcls")

                self.catmintfcurendccoamrcovingpvcls = YLeaf(YType.uint32, "CISCO-ATM-PVCTRAP-EXTN-MIB:catmIntfCurEndCCOAMRcovingPVcls")

                self.catmintfcurrentlydowntouppvcls = YLeaf(YType.uint32, "CISCO-ATM-PVCTRAP-EXTN-MIB:catmIntfCurrentlyDownToUpPVcls")

                self.catmintfcurrentoamfailingpvcls = YLeaf(YType.uint32, "CISCO-ATM-PVCTRAP-EXTN-MIB:catmIntfCurrentOAMFailingPVcls")

                self.catmintfcurrentoamrcovingpvcls = YLeaf(YType.uint32, "CISCO-ATM-PVCTRAP-EXTN-MIB:catmIntfCurrentOAMRcovingPVcls")

                self.catmintfcursegccoamfailingpvcls = YLeaf(YType.uint32, "CISCO-ATM-PVCTRAP-EXTN-MIB:catmIntfCurSegCCOAMFailingPVcls")

                self.catmintfcursegccoamrcovingpvcls = YLeaf(YType.uint32, "CISCO-ATM-PVCTRAP-EXTN-MIB:catmIntfCurSegCCOAMRcovingPVcls")

                self.catmintfendccoamfailedpvcls = YLeaf(YType.uint32, "CISCO-ATM-PVCTRAP-EXTN-MIB:catmIntfEndCCOAMFailedPVcls")

                self.catmintfendccoamrcovedpvcls = YLeaf(YType.uint32, "CISCO-ATM-PVCTRAP-EXTN-MIB:catmIntfEndCCOAMRcovedPVcls")

                self.catmintfoamfailedpvcls = YLeaf(YType.uint32, "CISCO-ATM-PVCTRAP-EXTN-MIB:catmIntfOAMFailedPVcls")

                self.catmintfoamrcovedpvcls = YLeaf(YType.uint32, "CISCO-ATM-PVCTRAP-EXTN-MIB:catmIntfOAMRcovedPVcls")

                self.catmintfsegccoamfailedpvcls = YLeaf(YType.uint32, "CISCO-ATM-PVCTRAP-EXTN-MIB:catmIntfSegCCOAMFailedPVcls")

                self.catmintfsegccoamrcovedpvcls = YLeaf(YType.uint32, "CISCO-ATM-PVCTRAP-EXTN-MIB:catmIntfSegCCOAMRcovedPVcls")

                self.catmintftypeofoamfailure = YLeaf(YType.enumeration, "CISCO-ATM-PVCTRAP-EXTN-MIB:catmIntfTypeOfOAMFailure")

                self.catmintftypeofoamrecover = YLeaf(YType.enumeration, "CISCO-ATM-PVCTRAP-EXTN-MIB:catmIntfTypeOfOAMRecover")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ifindex",
                                "atminterfaceaddresstype",
                                "atminterfaceadminaddress",
                                "atminterfaceconfvccs",
                                "atminterfaceconfvpcs",
                                "atminterfacecurrentmaxvcibits",
                                "atminterfacecurrentmaxvpibits",
                                "atminterfaceilmivci",
                                "atminterfaceilmivpi",
                                "atminterfacemaxactivevcibits",
                                "atminterfacemaxactivevpibits",
                                "atminterfacemaxvccs",
                                "atminterfacemaxvpcs",
                                "atminterfacemyneighborifname",
                                "atminterfacemyneighboripaddress",
                                "atminterfacesubscraddress",
                                "atmintfcurrentlydowntouppvcls",
                                "atmintfcurrentlyfailingpvcls",
                                "atmintfcurrentlyoamfailingpvcls",
                                "atmintfoamfailedpvcls",
                                "atmintfpvcfailures",
                                "atmintfpvcfailurestrapenable",
                                "atmintfpvcnotificationinterval",
                                "atmpreviouslyfailedpvclinterval",
                                "catmintfaisrdioamfailedpvcls",
                                "catmintfaisrdioamrcovedpvcls",
                                "catmintfanyoamfailedpvcls",
                                "catmintfanyoamrcovedpvcls",
                                "catmintfcuraisrdioamfailingpvcls",
                                "catmintfcuraisrdioamrcovingpvcls",
                                "catmintfcuranyoamfailingpvcls",
                                "catmintfcuranyoamrcovingpvcls",
                                "catmintfcurendccoamfailingpvcls",
                                "catmintfcurendccoamrcovingpvcls",
                                "catmintfcurrentlydowntouppvcls",
                                "catmintfcurrentoamfailingpvcls",
                                "catmintfcurrentoamrcovingpvcls",
                                "catmintfcursegccoamfailingpvcls",
                                "catmintfcursegccoamrcovingpvcls",
                                "catmintfendccoamfailedpvcls",
                                "catmintfendccoamrcovedpvcls",
                                "catmintfoamfailedpvcls",
                                "catmintfoamrcovedpvcls",
                                "catmintfsegccoamfailedpvcls",
                                "catmintfsegccoamrcovedpvcls",
                                "catmintftypeofoamfailure",
                                "catmintftypeofoamrecover") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(AtmMib.Atminterfaceconftable.Atminterfaceconfentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(AtmMib.Atminterfaceconftable.Atminterfaceconfentry, self).__setattr__(name, value)

            class Atminterfaceaddresstype(Enum):
                """
                Atminterfaceaddresstype

                The type of primary ATM address configured

                for use at this ATM interface.

                .. data:: private = 1

                .. data:: nsapE164 = 2

                .. data:: nativeE164 = 3

                .. data:: other = 4

                """

                private = Enum.YLeaf(1, "private")

                nsapE164 = Enum.YLeaf(2, "nsapE164")

                nativeE164 = Enum.YLeaf(3, "nativeE164")

                other = Enum.YLeaf(4, "other")


            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.atminterfaceaddresstype.is_set or
                    self.atminterfaceadminaddress.is_set or
                    self.atminterfaceconfvccs.is_set or
                    self.atminterfaceconfvpcs.is_set or
                    self.atminterfacecurrentmaxvcibits.is_set or
                    self.atminterfacecurrentmaxvpibits.is_set or
                    self.atminterfaceilmivci.is_set or
                    self.atminterfaceilmivpi.is_set or
                    self.atminterfacemaxactivevcibits.is_set or
                    self.atminterfacemaxactivevpibits.is_set or
                    self.atminterfacemaxvccs.is_set or
                    self.atminterfacemaxvpcs.is_set or
                    self.atminterfacemyneighborifname.is_set or
                    self.atminterfacemyneighboripaddress.is_set or
                    self.atminterfacesubscraddress.is_set or
                    self.atmintfcurrentlydowntouppvcls.is_set or
                    self.atmintfcurrentlyfailingpvcls.is_set or
                    self.atmintfcurrentlyoamfailingpvcls.is_set or
                    self.atmintfoamfailedpvcls.is_set or
                    self.atmintfpvcfailures.is_set or
                    self.atmintfpvcfailurestrapenable.is_set or
                    self.atmintfpvcnotificationinterval.is_set or
                    self.atmpreviouslyfailedpvclinterval.is_set or
                    self.catmintfaisrdioamfailedpvcls.is_set or
                    self.catmintfaisrdioamrcovedpvcls.is_set or
                    self.catmintfanyoamfailedpvcls.is_set or
                    self.catmintfanyoamrcovedpvcls.is_set or
                    self.catmintfcuraisrdioamfailingpvcls.is_set or
                    self.catmintfcuraisrdioamrcovingpvcls.is_set or
                    self.catmintfcuranyoamfailingpvcls.is_set or
                    self.catmintfcuranyoamrcovingpvcls.is_set or
                    self.catmintfcurendccoamfailingpvcls.is_set or
                    self.catmintfcurendccoamrcovingpvcls.is_set or
                    self.catmintfcurrentlydowntouppvcls.is_set or
                    self.catmintfcurrentoamfailingpvcls.is_set or
                    self.catmintfcurrentoamrcovingpvcls.is_set or
                    self.catmintfcursegccoamfailingpvcls.is_set or
                    self.catmintfcursegccoamrcovingpvcls.is_set or
                    self.catmintfendccoamfailedpvcls.is_set or
                    self.catmintfendccoamrcovedpvcls.is_set or
                    self.catmintfoamfailedpvcls.is_set or
                    self.catmintfoamrcovedpvcls.is_set or
                    self.catmintfsegccoamfailedpvcls.is_set or
                    self.catmintfsegccoamrcovedpvcls.is_set or
                    self.catmintftypeofoamfailure.is_set or
                    self.catmintftypeofoamrecover.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.atminterfaceaddresstype.yfilter != YFilter.not_set or
                    self.atminterfaceadminaddress.yfilter != YFilter.not_set or
                    self.atminterfaceconfvccs.yfilter != YFilter.not_set or
                    self.atminterfaceconfvpcs.yfilter != YFilter.not_set or
                    self.atminterfacecurrentmaxvcibits.yfilter != YFilter.not_set or
                    self.atminterfacecurrentmaxvpibits.yfilter != YFilter.not_set or
                    self.atminterfaceilmivci.yfilter != YFilter.not_set or
                    self.atminterfaceilmivpi.yfilter != YFilter.not_set or
                    self.atminterfacemaxactivevcibits.yfilter != YFilter.not_set or
                    self.atminterfacemaxactivevpibits.yfilter != YFilter.not_set or
                    self.atminterfacemaxvccs.yfilter != YFilter.not_set or
                    self.atminterfacemaxvpcs.yfilter != YFilter.not_set or
                    self.atminterfacemyneighborifname.yfilter != YFilter.not_set or
                    self.atminterfacemyneighboripaddress.yfilter != YFilter.not_set or
                    self.atminterfacesubscraddress.yfilter != YFilter.not_set or
                    self.atmintfcurrentlydowntouppvcls.yfilter != YFilter.not_set or
                    self.atmintfcurrentlyfailingpvcls.yfilter != YFilter.not_set or
                    self.atmintfcurrentlyoamfailingpvcls.yfilter != YFilter.not_set or
                    self.atmintfoamfailedpvcls.yfilter != YFilter.not_set or
                    self.atmintfpvcfailures.yfilter != YFilter.not_set or
                    self.atmintfpvcfailurestrapenable.yfilter != YFilter.not_set or
                    self.atmintfpvcnotificationinterval.yfilter != YFilter.not_set or
                    self.atmpreviouslyfailedpvclinterval.yfilter != YFilter.not_set or
                    self.catmintfaisrdioamfailedpvcls.yfilter != YFilter.not_set or
                    self.catmintfaisrdioamrcovedpvcls.yfilter != YFilter.not_set or
                    self.catmintfanyoamfailedpvcls.yfilter != YFilter.not_set or
                    self.catmintfanyoamrcovedpvcls.yfilter != YFilter.not_set or
                    self.catmintfcuraisrdioamfailingpvcls.yfilter != YFilter.not_set or
                    self.catmintfcuraisrdioamrcovingpvcls.yfilter != YFilter.not_set or
                    self.catmintfcuranyoamfailingpvcls.yfilter != YFilter.not_set or
                    self.catmintfcuranyoamrcovingpvcls.yfilter != YFilter.not_set or
                    self.catmintfcurendccoamfailingpvcls.yfilter != YFilter.not_set or
                    self.catmintfcurendccoamrcovingpvcls.yfilter != YFilter.not_set or
                    self.catmintfcurrentlydowntouppvcls.yfilter != YFilter.not_set or
                    self.catmintfcurrentoamfailingpvcls.yfilter != YFilter.not_set or
                    self.catmintfcurrentoamrcovingpvcls.yfilter != YFilter.not_set or
                    self.catmintfcursegccoamfailingpvcls.yfilter != YFilter.not_set or
                    self.catmintfcursegccoamrcovingpvcls.yfilter != YFilter.not_set or
                    self.catmintfendccoamfailedpvcls.yfilter != YFilter.not_set or
                    self.catmintfendccoamrcovedpvcls.yfilter != YFilter.not_set or
                    self.catmintfoamfailedpvcls.yfilter != YFilter.not_set or
                    self.catmintfoamrcovedpvcls.yfilter != YFilter.not_set or
                    self.catmintfsegccoamfailedpvcls.yfilter != YFilter.not_set or
                    self.catmintfsegccoamrcovedpvcls.yfilter != YFilter.not_set or
                    self.catmintftypeofoamfailure.yfilter != YFilter.not_set or
                    self.catmintftypeofoamrecover.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "atmInterfaceConfEntry" + "[ifIndex='" + self.ifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "ATM-MIB:ATM-MIB/atmInterfaceConfTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.atminterfaceaddresstype.is_set or self.atminterfaceaddresstype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atminterfaceaddresstype.get_name_leafdata())
                if (self.atminterfaceadminaddress.is_set or self.atminterfaceadminaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atminterfaceadminaddress.get_name_leafdata())
                if (self.atminterfaceconfvccs.is_set or self.atminterfaceconfvccs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atminterfaceconfvccs.get_name_leafdata())
                if (self.atminterfaceconfvpcs.is_set or self.atminterfaceconfvpcs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atminterfaceconfvpcs.get_name_leafdata())
                if (self.atminterfacecurrentmaxvcibits.is_set or self.atminterfacecurrentmaxvcibits.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atminterfacecurrentmaxvcibits.get_name_leafdata())
                if (self.atminterfacecurrentmaxvpibits.is_set or self.atminterfacecurrentmaxvpibits.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atminterfacecurrentmaxvpibits.get_name_leafdata())
                if (self.atminterfaceilmivci.is_set or self.atminterfaceilmivci.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atminterfaceilmivci.get_name_leafdata())
                if (self.atminterfaceilmivpi.is_set or self.atminterfaceilmivpi.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atminterfaceilmivpi.get_name_leafdata())
                if (self.atminterfacemaxactivevcibits.is_set or self.atminterfacemaxactivevcibits.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atminterfacemaxactivevcibits.get_name_leafdata())
                if (self.atminterfacemaxactivevpibits.is_set or self.atminterfacemaxactivevpibits.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atminterfacemaxactivevpibits.get_name_leafdata())
                if (self.atminterfacemaxvccs.is_set or self.atminterfacemaxvccs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atminterfacemaxvccs.get_name_leafdata())
                if (self.atminterfacemaxvpcs.is_set or self.atminterfacemaxvpcs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atminterfacemaxvpcs.get_name_leafdata())
                if (self.atminterfacemyneighborifname.is_set or self.atminterfacemyneighborifname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atminterfacemyneighborifname.get_name_leafdata())
                if (self.atminterfacemyneighboripaddress.is_set or self.atminterfacemyneighboripaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atminterfacemyneighboripaddress.get_name_leafdata())
                if (self.atminterfacesubscraddress.is_set or self.atminterfacesubscraddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atminterfacesubscraddress.get_name_leafdata())
                if (self.atmintfcurrentlydowntouppvcls.is_set or self.atmintfcurrentlydowntouppvcls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmintfcurrentlydowntouppvcls.get_name_leafdata())
                if (self.atmintfcurrentlyfailingpvcls.is_set or self.atmintfcurrentlyfailingpvcls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmintfcurrentlyfailingpvcls.get_name_leafdata())
                if (self.atmintfcurrentlyoamfailingpvcls.is_set or self.atmintfcurrentlyoamfailingpvcls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmintfcurrentlyoamfailingpvcls.get_name_leafdata())
                if (self.atmintfoamfailedpvcls.is_set or self.atmintfoamfailedpvcls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmintfoamfailedpvcls.get_name_leafdata())
                if (self.atmintfpvcfailures.is_set or self.atmintfpvcfailures.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmintfpvcfailures.get_name_leafdata())
                if (self.atmintfpvcfailurestrapenable.is_set or self.atmintfpvcfailurestrapenable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmintfpvcfailurestrapenable.get_name_leafdata())
                if (self.atmintfpvcnotificationinterval.is_set or self.atmintfpvcnotificationinterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmintfpvcnotificationinterval.get_name_leafdata())
                if (self.atmpreviouslyfailedpvclinterval.is_set or self.atmpreviouslyfailedpvclinterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmpreviouslyfailedpvclinterval.get_name_leafdata())
                if (self.catmintfaisrdioamfailedpvcls.is_set or self.catmintfaisrdioamfailedpvcls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmintfaisrdioamfailedpvcls.get_name_leafdata())
                if (self.catmintfaisrdioamrcovedpvcls.is_set or self.catmintfaisrdioamrcovedpvcls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmintfaisrdioamrcovedpvcls.get_name_leafdata())
                if (self.catmintfanyoamfailedpvcls.is_set or self.catmintfanyoamfailedpvcls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmintfanyoamfailedpvcls.get_name_leafdata())
                if (self.catmintfanyoamrcovedpvcls.is_set or self.catmintfanyoamrcovedpvcls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmintfanyoamrcovedpvcls.get_name_leafdata())
                if (self.catmintfcuraisrdioamfailingpvcls.is_set or self.catmintfcuraisrdioamfailingpvcls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmintfcuraisrdioamfailingpvcls.get_name_leafdata())
                if (self.catmintfcuraisrdioamrcovingpvcls.is_set or self.catmintfcuraisrdioamrcovingpvcls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmintfcuraisrdioamrcovingpvcls.get_name_leafdata())
                if (self.catmintfcuranyoamfailingpvcls.is_set or self.catmintfcuranyoamfailingpvcls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmintfcuranyoamfailingpvcls.get_name_leafdata())
                if (self.catmintfcuranyoamrcovingpvcls.is_set or self.catmintfcuranyoamrcovingpvcls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmintfcuranyoamrcovingpvcls.get_name_leafdata())
                if (self.catmintfcurendccoamfailingpvcls.is_set or self.catmintfcurendccoamfailingpvcls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmintfcurendccoamfailingpvcls.get_name_leafdata())
                if (self.catmintfcurendccoamrcovingpvcls.is_set or self.catmintfcurendccoamrcovingpvcls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmintfcurendccoamrcovingpvcls.get_name_leafdata())
                if (self.catmintfcurrentlydowntouppvcls.is_set or self.catmintfcurrentlydowntouppvcls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmintfcurrentlydowntouppvcls.get_name_leafdata())
                if (self.catmintfcurrentoamfailingpvcls.is_set or self.catmintfcurrentoamfailingpvcls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmintfcurrentoamfailingpvcls.get_name_leafdata())
                if (self.catmintfcurrentoamrcovingpvcls.is_set or self.catmintfcurrentoamrcovingpvcls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmintfcurrentoamrcovingpvcls.get_name_leafdata())
                if (self.catmintfcursegccoamfailingpvcls.is_set or self.catmintfcursegccoamfailingpvcls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmintfcursegccoamfailingpvcls.get_name_leafdata())
                if (self.catmintfcursegccoamrcovingpvcls.is_set or self.catmintfcursegccoamrcovingpvcls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmintfcursegccoamrcovingpvcls.get_name_leafdata())
                if (self.catmintfendccoamfailedpvcls.is_set or self.catmintfendccoamfailedpvcls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmintfendccoamfailedpvcls.get_name_leafdata())
                if (self.catmintfendccoamrcovedpvcls.is_set or self.catmintfendccoamrcovedpvcls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmintfendccoamrcovedpvcls.get_name_leafdata())
                if (self.catmintfoamfailedpvcls.is_set or self.catmintfoamfailedpvcls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmintfoamfailedpvcls.get_name_leafdata())
                if (self.catmintfoamrcovedpvcls.is_set or self.catmintfoamrcovedpvcls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmintfoamrcovedpvcls.get_name_leafdata())
                if (self.catmintfsegccoamfailedpvcls.is_set or self.catmintfsegccoamfailedpvcls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmintfsegccoamfailedpvcls.get_name_leafdata())
                if (self.catmintfsegccoamrcovedpvcls.is_set or self.catmintfsegccoamrcovedpvcls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmintfsegccoamrcovedpvcls.get_name_leafdata())
                if (self.catmintftypeofoamfailure.is_set or self.catmintftypeofoamfailure.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmintftypeofoamfailure.get_name_leafdata())
                if (self.catmintftypeofoamrecover.is_set or self.catmintftypeofoamrecover.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmintftypeofoamrecover.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "atmInterfaceAddressType" or name == "atmInterfaceAdminAddress" or name == "atmInterfaceConfVccs" or name == "atmInterfaceConfVpcs" or name == "atmInterfaceCurrentMaxVciBits" or name == "atmInterfaceCurrentMaxVpiBits" or name == "atmInterfaceIlmiVci" or name == "atmInterfaceIlmiVpi" or name == "atmInterfaceMaxActiveVciBits" or name == "atmInterfaceMaxActiveVpiBits" or name == "atmInterfaceMaxVccs" or name == "atmInterfaceMaxVpcs" or name == "atmInterfaceMyNeighborIfName" or name == "atmInterfaceMyNeighborIpAddress" or name == "atmInterfaceSubscrAddress" or name == "atmIntfCurrentlyDownToUpPVcls" or name == "atmIntfCurrentlyFailingPVcls" or name == "atmIntfCurrentlyOAMFailingPVcls" or name == "atmIntfOAMFailedPVcls" or name == "atmIntfPvcFailures" or name == "atmIntfPvcFailuresTrapEnable" or name == "atmIntfPvcNotificationInterval" or name == "atmPreviouslyFailedPVclInterval" or name == "catmIntfAISRDIOAMFailedPVcls" or name == "catmIntfAISRDIOAMRcovedPVcls" or name == "catmIntfAnyOAMFailedPVcls" or name == "catmIntfAnyOAMRcovedPVcls" or name == "catmIntfCurAISRDIOAMFailingPVcls" or name == "catmIntfCurAISRDIOAMRcovingPVcls" or name == "catmIntfCurAnyOAMFailingPVcls" or name == "catmIntfCurAnyOAMRcovingPVcls" or name == "catmIntfCurEndCCOAMFailingPVcls" or name == "catmIntfCurEndCCOAMRcovingPVcls" or name == "catmIntfCurrentlyDownToUpPVcls" or name == "catmIntfCurrentOAMFailingPVcls" or name == "catmIntfCurrentOAMRcovingPVcls" or name == "catmIntfCurSegCCOAMFailingPVcls" or name == "catmIntfCurSegCCOAMRcovingPVcls" or name == "catmIntfEndCCOAMFailedPVcls" or name == "catmIntfEndCCOAMRcovedPVcls" or name == "catmIntfOAMFailedPVcls" or name == "catmIntfOAMRcovedPVcls" or name == "catmIntfSegCCOAMFailedPVcls" or name == "catmIntfSegCCOAMRcovedPVcls" or name == "catmIntfTypeOfOAMFailure" or name == "catmIntfTypeOfOAMRecover"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "atmInterfaceAddressType"):
                    self.atminterfaceaddresstype = value
                    self.atminterfaceaddresstype.value_namespace = name_space
                    self.atminterfaceaddresstype.value_namespace_prefix = name_space_prefix
                if(value_path == "atmInterfaceAdminAddress"):
                    self.atminterfaceadminaddress = value
                    self.atminterfaceadminaddress.value_namespace = name_space
                    self.atminterfaceadminaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "atmInterfaceConfVccs"):
                    self.atminterfaceconfvccs = value
                    self.atminterfaceconfvccs.value_namespace = name_space
                    self.atminterfaceconfvccs.value_namespace_prefix = name_space_prefix
                if(value_path == "atmInterfaceConfVpcs"):
                    self.atminterfaceconfvpcs = value
                    self.atminterfaceconfvpcs.value_namespace = name_space
                    self.atminterfaceconfvpcs.value_namespace_prefix = name_space_prefix
                if(value_path == "atmInterfaceCurrentMaxVciBits"):
                    self.atminterfacecurrentmaxvcibits = value
                    self.atminterfacecurrentmaxvcibits.value_namespace = name_space
                    self.atminterfacecurrentmaxvcibits.value_namespace_prefix = name_space_prefix
                if(value_path == "atmInterfaceCurrentMaxVpiBits"):
                    self.atminterfacecurrentmaxvpibits = value
                    self.atminterfacecurrentmaxvpibits.value_namespace = name_space
                    self.atminterfacecurrentmaxvpibits.value_namespace_prefix = name_space_prefix
                if(value_path == "atmInterfaceIlmiVci"):
                    self.atminterfaceilmivci = value
                    self.atminterfaceilmivci.value_namespace = name_space
                    self.atminterfaceilmivci.value_namespace_prefix = name_space_prefix
                if(value_path == "atmInterfaceIlmiVpi"):
                    self.atminterfaceilmivpi = value
                    self.atminterfaceilmivpi.value_namespace = name_space
                    self.atminterfaceilmivpi.value_namespace_prefix = name_space_prefix
                if(value_path == "atmInterfaceMaxActiveVciBits"):
                    self.atminterfacemaxactivevcibits = value
                    self.atminterfacemaxactivevcibits.value_namespace = name_space
                    self.atminterfacemaxactivevcibits.value_namespace_prefix = name_space_prefix
                if(value_path == "atmInterfaceMaxActiveVpiBits"):
                    self.atminterfacemaxactivevpibits = value
                    self.atminterfacemaxactivevpibits.value_namespace = name_space
                    self.atminterfacemaxactivevpibits.value_namespace_prefix = name_space_prefix
                if(value_path == "atmInterfaceMaxVccs"):
                    self.atminterfacemaxvccs = value
                    self.atminterfacemaxvccs.value_namespace = name_space
                    self.atminterfacemaxvccs.value_namespace_prefix = name_space_prefix
                if(value_path == "atmInterfaceMaxVpcs"):
                    self.atminterfacemaxvpcs = value
                    self.atminterfacemaxvpcs.value_namespace = name_space
                    self.atminterfacemaxvpcs.value_namespace_prefix = name_space_prefix
                if(value_path == "atmInterfaceMyNeighborIfName"):
                    self.atminterfacemyneighborifname = value
                    self.atminterfacemyneighborifname.value_namespace = name_space
                    self.atminterfacemyneighborifname.value_namespace_prefix = name_space_prefix
                if(value_path == "atmInterfaceMyNeighborIpAddress"):
                    self.atminterfacemyneighboripaddress = value
                    self.atminterfacemyneighboripaddress.value_namespace = name_space
                    self.atminterfacemyneighboripaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "atmInterfaceSubscrAddress"):
                    self.atminterfacesubscraddress = value
                    self.atminterfacesubscraddress.value_namespace = name_space
                    self.atminterfacesubscraddress.value_namespace_prefix = name_space_prefix
                if(value_path == "atmIntfCurrentlyDownToUpPVcls"):
                    self.atmintfcurrentlydowntouppvcls = value
                    self.atmintfcurrentlydowntouppvcls.value_namespace = name_space
                    self.atmintfcurrentlydowntouppvcls.value_namespace_prefix = name_space_prefix
                if(value_path == "atmIntfCurrentlyFailingPVcls"):
                    self.atmintfcurrentlyfailingpvcls = value
                    self.atmintfcurrentlyfailingpvcls.value_namespace = name_space
                    self.atmintfcurrentlyfailingpvcls.value_namespace_prefix = name_space_prefix
                if(value_path == "atmIntfCurrentlyOAMFailingPVcls"):
                    self.atmintfcurrentlyoamfailingpvcls = value
                    self.atmintfcurrentlyoamfailingpvcls.value_namespace = name_space
                    self.atmintfcurrentlyoamfailingpvcls.value_namespace_prefix = name_space_prefix
                if(value_path == "atmIntfOAMFailedPVcls"):
                    self.atmintfoamfailedpvcls = value
                    self.atmintfoamfailedpvcls.value_namespace = name_space
                    self.atmintfoamfailedpvcls.value_namespace_prefix = name_space_prefix
                if(value_path == "atmIntfPvcFailures"):
                    self.atmintfpvcfailures = value
                    self.atmintfpvcfailures.value_namespace = name_space
                    self.atmintfpvcfailures.value_namespace_prefix = name_space_prefix
                if(value_path == "atmIntfPvcFailuresTrapEnable"):
                    self.atmintfpvcfailurestrapenable = value
                    self.atmintfpvcfailurestrapenable.value_namespace = name_space
                    self.atmintfpvcfailurestrapenable.value_namespace_prefix = name_space_prefix
                if(value_path == "atmIntfPvcNotificationInterval"):
                    self.atmintfpvcnotificationinterval = value
                    self.atmintfpvcnotificationinterval.value_namespace = name_space
                    self.atmintfpvcnotificationinterval.value_namespace_prefix = name_space_prefix
                if(value_path == "atmPreviouslyFailedPVclInterval"):
                    self.atmpreviouslyfailedpvclinterval = value
                    self.atmpreviouslyfailedpvclinterval.value_namespace = name_space
                    self.atmpreviouslyfailedpvclinterval.value_namespace_prefix = name_space_prefix
                if(value_path == "catmIntfAISRDIOAMFailedPVcls"):
                    self.catmintfaisrdioamfailedpvcls = value
                    self.catmintfaisrdioamfailedpvcls.value_namespace = name_space
                    self.catmintfaisrdioamfailedpvcls.value_namespace_prefix = name_space_prefix
                if(value_path == "catmIntfAISRDIOAMRcovedPVcls"):
                    self.catmintfaisrdioamrcovedpvcls = value
                    self.catmintfaisrdioamrcovedpvcls.value_namespace = name_space
                    self.catmintfaisrdioamrcovedpvcls.value_namespace_prefix = name_space_prefix
                if(value_path == "catmIntfAnyOAMFailedPVcls"):
                    self.catmintfanyoamfailedpvcls = value
                    self.catmintfanyoamfailedpvcls.value_namespace = name_space
                    self.catmintfanyoamfailedpvcls.value_namespace_prefix = name_space_prefix
                if(value_path == "catmIntfAnyOAMRcovedPVcls"):
                    self.catmintfanyoamrcovedpvcls = value
                    self.catmintfanyoamrcovedpvcls.value_namespace = name_space
                    self.catmintfanyoamrcovedpvcls.value_namespace_prefix = name_space_prefix
                if(value_path == "catmIntfCurAISRDIOAMFailingPVcls"):
                    self.catmintfcuraisrdioamfailingpvcls = value
                    self.catmintfcuraisrdioamfailingpvcls.value_namespace = name_space
                    self.catmintfcuraisrdioamfailingpvcls.value_namespace_prefix = name_space_prefix
                if(value_path == "catmIntfCurAISRDIOAMRcovingPVcls"):
                    self.catmintfcuraisrdioamrcovingpvcls = value
                    self.catmintfcuraisrdioamrcovingpvcls.value_namespace = name_space
                    self.catmintfcuraisrdioamrcovingpvcls.value_namespace_prefix = name_space_prefix
                if(value_path == "catmIntfCurAnyOAMFailingPVcls"):
                    self.catmintfcuranyoamfailingpvcls = value
                    self.catmintfcuranyoamfailingpvcls.value_namespace = name_space
                    self.catmintfcuranyoamfailingpvcls.value_namespace_prefix = name_space_prefix
                if(value_path == "catmIntfCurAnyOAMRcovingPVcls"):
                    self.catmintfcuranyoamrcovingpvcls = value
                    self.catmintfcuranyoamrcovingpvcls.value_namespace = name_space
                    self.catmintfcuranyoamrcovingpvcls.value_namespace_prefix = name_space_prefix
                if(value_path == "catmIntfCurEndCCOAMFailingPVcls"):
                    self.catmintfcurendccoamfailingpvcls = value
                    self.catmintfcurendccoamfailingpvcls.value_namespace = name_space
                    self.catmintfcurendccoamfailingpvcls.value_namespace_prefix = name_space_prefix
                if(value_path == "catmIntfCurEndCCOAMRcovingPVcls"):
                    self.catmintfcurendccoamrcovingpvcls = value
                    self.catmintfcurendccoamrcovingpvcls.value_namespace = name_space
                    self.catmintfcurendccoamrcovingpvcls.value_namespace_prefix = name_space_prefix
                if(value_path == "catmIntfCurrentlyDownToUpPVcls"):
                    self.catmintfcurrentlydowntouppvcls = value
                    self.catmintfcurrentlydowntouppvcls.value_namespace = name_space
                    self.catmintfcurrentlydowntouppvcls.value_namespace_prefix = name_space_prefix
                if(value_path == "catmIntfCurrentOAMFailingPVcls"):
                    self.catmintfcurrentoamfailingpvcls = value
                    self.catmintfcurrentoamfailingpvcls.value_namespace = name_space
                    self.catmintfcurrentoamfailingpvcls.value_namespace_prefix = name_space_prefix
                if(value_path == "catmIntfCurrentOAMRcovingPVcls"):
                    self.catmintfcurrentoamrcovingpvcls = value
                    self.catmintfcurrentoamrcovingpvcls.value_namespace = name_space
                    self.catmintfcurrentoamrcovingpvcls.value_namespace_prefix = name_space_prefix
                if(value_path == "catmIntfCurSegCCOAMFailingPVcls"):
                    self.catmintfcursegccoamfailingpvcls = value
                    self.catmintfcursegccoamfailingpvcls.value_namespace = name_space
                    self.catmintfcursegccoamfailingpvcls.value_namespace_prefix = name_space_prefix
                if(value_path == "catmIntfCurSegCCOAMRcovingPVcls"):
                    self.catmintfcursegccoamrcovingpvcls = value
                    self.catmintfcursegccoamrcovingpvcls.value_namespace = name_space
                    self.catmintfcursegccoamrcovingpvcls.value_namespace_prefix = name_space_prefix
                if(value_path == "catmIntfEndCCOAMFailedPVcls"):
                    self.catmintfendccoamfailedpvcls = value
                    self.catmintfendccoamfailedpvcls.value_namespace = name_space
                    self.catmintfendccoamfailedpvcls.value_namespace_prefix = name_space_prefix
                if(value_path == "catmIntfEndCCOAMRcovedPVcls"):
                    self.catmintfendccoamrcovedpvcls = value
                    self.catmintfendccoamrcovedpvcls.value_namespace = name_space
                    self.catmintfendccoamrcovedpvcls.value_namespace_prefix = name_space_prefix
                if(value_path == "catmIntfOAMFailedPVcls"):
                    self.catmintfoamfailedpvcls = value
                    self.catmintfoamfailedpvcls.value_namespace = name_space
                    self.catmintfoamfailedpvcls.value_namespace_prefix = name_space_prefix
                if(value_path == "catmIntfOAMRcovedPVcls"):
                    self.catmintfoamrcovedpvcls = value
                    self.catmintfoamrcovedpvcls.value_namespace = name_space
                    self.catmintfoamrcovedpvcls.value_namespace_prefix = name_space_prefix
                if(value_path == "catmIntfSegCCOAMFailedPVcls"):
                    self.catmintfsegccoamfailedpvcls = value
                    self.catmintfsegccoamfailedpvcls.value_namespace = name_space
                    self.catmintfsegccoamfailedpvcls.value_namespace_prefix = name_space_prefix
                if(value_path == "catmIntfSegCCOAMRcovedPVcls"):
                    self.catmintfsegccoamrcovedpvcls = value
                    self.catmintfsegccoamrcovedpvcls.value_namespace = name_space
                    self.catmintfsegccoamrcovedpvcls.value_namespace_prefix = name_space_prefix
                if(value_path == "catmIntfTypeOfOAMFailure"):
                    self.catmintftypeofoamfailure = value
                    self.catmintftypeofoamfailure.value_namespace = name_space
                    self.catmintftypeofoamfailure.value_namespace_prefix = name_space_prefix
                if(value_path == "catmIntfTypeOfOAMRecover"):
                    self.catmintftypeofoamrecover = value
                    self.catmintftypeofoamrecover.value_namespace = name_space
                    self.catmintftypeofoamrecover.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.atminterfaceconfentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.atminterfaceconfentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "atmInterfaceConfTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "ATM-MIB:ATM-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "atmInterfaceConfEntry"):
                for c in self.atminterfaceconfentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = AtmMib.Atminterfaceconftable.Atminterfaceconfentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.atminterfaceconfentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "atmInterfaceConfEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Atminterfaceds3Plcptable(Entity):
        """
        This table contains ATM interface DS3 PLCP
        parameters and state variables, one entry per
        ATM interface port.
        
        .. attribute:: atminterfaceds3plcpentry
        
        	This list contains DS3 PLCP parameters and state variables at the ATM interface and is indexed by the ifIndex value of the ATM interface
        	**type**\: list of    :py:class:`Atminterfaceds3Plcpentry <ydk.models.cisco_ios_xe.ATM_MIB.AtmMib.Atminterfaceds3Plcptable.Atminterfaceds3Plcpentry>`
        
        

        """

        _prefix = 'ATM-MIB'
        _revision = '1998-10-19'

        def __init__(self):
            super(AtmMib.Atminterfaceds3Plcptable, self).__init__()

            self.yang_name = "atmInterfaceDs3PlcpTable"
            self.yang_parent_name = "ATM-MIB"

            self.atminterfaceds3plcpentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(AtmMib.Atminterfaceds3Plcptable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(AtmMib.Atminterfaceds3Plcptable, self).__setattr__(name, value)


        class Atminterfaceds3Plcpentry(Entity):
            """
            This list contains DS3 PLCP parameters and
            state variables at the ATM interface and is
            indexed by the ifIndex value of the ATM interface.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: atminterfaceds3plcpalarmstate
            
            	This variable indicates if there is an alarm present for the DS3 PLCP.  The value receivedFarEndAlarm means that the DS3 PLCP has received an incoming Yellow Signal, the value incomingLOF means that the DS3 PLCP has declared a loss of frame (LOF) failure condition, and the value noAlarm means that there are no alarms present. Transition from the failure to the no alarm state occurs when no defects (e.g., LOF) are received for more than 10 seconds
            	**type**\:   :py:class:`Atminterfaceds3Plcpalarmstate <ydk.models.cisco_ios_xe.ATM_MIB.AtmMib.Atminterfaceds3Plcptable.Atminterfaceds3Plcpentry.Atminterfaceds3Plcpalarmstate>`
            
            .. attribute:: atminterfaceds3plcpsefss
            
            	The number of DS3 PLCP Severely Errored Framing Seconds (SEFS). Each SEFS represents a one\-second interval which contains one or more SEF events
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: atminterfaceds3plcpuass
            
            	The counter associated with the number of Unavailable Seconds encountered by the PLCP
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'ATM-MIB'
            _revision = '1998-10-19'

            def __init__(self):
                super(AtmMib.Atminterfaceds3Plcptable.Atminterfaceds3Plcpentry, self).__init__()

                self.yang_name = "atmInterfaceDs3PlcpEntry"
                self.yang_parent_name = "atmInterfaceDs3PlcpTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.atminterfaceds3plcpalarmstate = YLeaf(YType.enumeration, "atmInterfaceDs3PlcpAlarmState")

                self.atminterfaceds3plcpsefss = YLeaf(YType.uint32, "atmInterfaceDs3PlcpSEFSs")

                self.atminterfaceds3plcpuass = YLeaf(YType.uint32, "atmInterfaceDs3PlcpUASs")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ifindex",
                                "atminterfaceds3plcpalarmstate",
                                "atminterfaceds3plcpsefss",
                                "atminterfaceds3plcpuass") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(AtmMib.Atminterfaceds3Plcptable.Atminterfaceds3Plcpentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(AtmMib.Atminterfaceds3Plcptable.Atminterfaceds3Plcpentry, self).__setattr__(name, value)

            class Atminterfaceds3Plcpalarmstate(Enum):
                """
                Atminterfaceds3Plcpalarmstate

                This variable indicates if there is an

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

                .. data:: noAlarm = 1

                .. data:: receivedFarEndAlarm = 2

                .. data:: incomingLOF = 3

                """

                noAlarm = Enum.YLeaf(1, "noAlarm")

                receivedFarEndAlarm = Enum.YLeaf(2, "receivedFarEndAlarm")

                incomingLOF = Enum.YLeaf(3, "incomingLOF")


            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.atminterfaceds3plcpalarmstate.is_set or
                    self.atminterfaceds3plcpsefss.is_set or
                    self.atminterfaceds3plcpuass.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.atminterfaceds3plcpalarmstate.yfilter != YFilter.not_set or
                    self.atminterfaceds3plcpsefss.yfilter != YFilter.not_set or
                    self.atminterfaceds3plcpuass.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "atmInterfaceDs3PlcpEntry" + "[ifIndex='" + self.ifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "ATM-MIB:ATM-MIB/atmInterfaceDs3PlcpTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.atminterfaceds3plcpalarmstate.is_set or self.atminterfaceds3plcpalarmstate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atminterfaceds3plcpalarmstate.get_name_leafdata())
                if (self.atminterfaceds3plcpsefss.is_set or self.atminterfaceds3plcpsefss.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atminterfaceds3plcpsefss.get_name_leafdata())
                if (self.atminterfaceds3plcpuass.is_set or self.atminterfaceds3plcpuass.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atminterfaceds3plcpuass.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "atmInterfaceDs3PlcpAlarmState" or name == "atmInterfaceDs3PlcpSEFSs" or name == "atmInterfaceDs3PlcpUASs"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "atmInterfaceDs3PlcpAlarmState"):
                    self.atminterfaceds3plcpalarmstate = value
                    self.atminterfaceds3plcpalarmstate.value_namespace = name_space
                    self.atminterfaceds3plcpalarmstate.value_namespace_prefix = name_space_prefix
                if(value_path == "atmInterfaceDs3PlcpSEFSs"):
                    self.atminterfaceds3plcpsefss = value
                    self.atminterfaceds3plcpsefss.value_namespace = name_space
                    self.atminterfaceds3plcpsefss.value_namespace_prefix = name_space_prefix
                if(value_path == "atmInterfaceDs3PlcpUASs"):
                    self.atminterfaceds3plcpuass = value
                    self.atminterfaceds3plcpuass.value_namespace = name_space
                    self.atminterfaceds3plcpuass.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.atminterfaceds3plcpentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.atminterfaceds3plcpentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "atmInterfaceDs3PlcpTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "ATM-MIB:ATM-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "atmInterfaceDs3PlcpEntry"):
                for c in self.atminterfaceds3plcpentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = AtmMib.Atminterfaceds3Plcptable.Atminterfaceds3Plcpentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.atminterfaceds3plcpentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "atmInterfaceDs3PlcpEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Atminterfacetctable(Entity):
        """
        This table contains ATM interface TC
        Sublayer parameters and state variables,
        one entry per ATM interface port.
        
        .. attribute:: atminterfacetcentry
        
        	This list contains TC Sublayer parameters and state variables at the ATM interface and is indexed by the ifIndex value of the ATM interface
        	**type**\: list of    :py:class:`Atminterfacetcentry <ydk.models.cisco_ios_xe.ATM_MIB.AtmMib.Atminterfacetctable.Atminterfacetcentry>`
        
        

        """

        _prefix = 'ATM-MIB'
        _revision = '1998-10-19'

        def __init__(self):
            super(AtmMib.Atminterfacetctable, self).__init__()

            self.yang_name = "atmInterfaceTCTable"
            self.yang_parent_name = "ATM-MIB"

            self.atminterfacetcentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(AtmMib.Atminterfacetctable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(AtmMib.Atminterfacetctable, self).__setattr__(name, value)


        class Atminterfacetcentry(Entity):
            """
            This list contains TC Sublayer parameters
            and state variables at the ATM interface and is
            indexed by the ifIndex value of the ATM interface.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: atminterfaceocdevents
            
            	The number of times the Out of Cell Delineation (OCD) events occur.  If seven consecutive ATM cells have Header Error Control (HEC) violations, an OCD event occurs. A high number of OCD events may indicate a problem with the TC Sublayer
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: atminterfacetcalarmstate
            
            	This variable indicates if there is an alarm present for the TC Sublayer.  The value lcdFailure(2) indicates that the TC Sublayer is currently in the Loss of Cell Delineation (LCD) defect maintenance state.  The value noAlarm(1) indicates that the TC Sublayer is currently not in the LCD defect maintenance state
            	**type**\:   :py:class:`Atminterfacetcalarmstate <ydk.models.cisco_ios_xe.ATM_MIB.AtmMib.Atminterfacetctable.Atminterfacetcentry.Atminterfacetcalarmstate>`
            
            

            """

            _prefix = 'ATM-MIB'
            _revision = '1998-10-19'

            def __init__(self):
                super(AtmMib.Atminterfacetctable.Atminterfacetcentry, self).__init__()

                self.yang_name = "atmInterfaceTCEntry"
                self.yang_parent_name = "atmInterfaceTCTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.atminterfaceocdevents = YLeaf(YType.uint32, "atmInterfaceOCDEvents")

                self.atminterfacetcalarmstate = YLeaf(YType.enumeration, "atmInterfaceTCAlarmState")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ifindex",
                                "atminterfaceocdevents",
                                "atminterfacetcalarmstate") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(AtmMib.Atminterfacetctable.Atminterfacetcentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(AtmMib.Atminterfacetctable.Atminterfacetcentry, self).__setattr__(name, value)

            class Atminterfacetcalarmstate(Enum):
                """
                Atminterfacetcalarmstate

                This variable indicates if there is an

                alarm present for the TC Sublayer.  The value

                lcdFailure(2) indicates that the TC Sublayer

                is currently in the Loss of Cell Delineation

                (LCD) defect maintenance state.  The value

                noAlarm(1) indicates that the TC Sublayer

                is currently not in the LCD defect

                maintenance state.

                .. data:: noAlarm = 1

                .. data:: lcdFailure = 2

                """

                noAlarm = Enum.YLeaf(1, "noAlarm")

                lcdFailure = Enum.YLeaf(2, "lcdFailure")


            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.atminterfaceocdevents.is_set or
                    self.atminterfacetcalarmstate.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.atminterfaceocdevents.yfilter != YFilter.not_set or
                    self.atminterfacetcalarmstate.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "atmInterfaceTCEntry" + "[ifIndex='" + self.ifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "ATM-MIB:ATM-MIB/atmInterfaceTCTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.atminterfaceocdevents.is_set or self.atminterfaceocdevents.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atminterfaceocdevents.get_name_leafdata())
                if (self.atminterfacetcalarmstate.is_set or self.atminterfacetcalarmstate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atminterfacetcalarmstate.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "atmInterfaceOCDEvents" or name == "atmInterfaceTCAlarmState"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "atmInterfaceOCDEvents"):
                    self.atminterfaceocdevents = value
                    self.atminterfaceocdevents.value_namespace = name_space
                    self.atminterfaceocdevents.value_namespace_prefix = name_space_prefix
                if(value_path == "atmInterfaceTCAlarmState"):
                    self.atminterfacetcalarmstate = value
                    self.atminterfacetcalarmstate.value_namespace = name_space
                    self.atminterfacetcalarmstate.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.atminterfacetcentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.atminterfacetcentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "atmInterfaceTCTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "ATM-MIB:ATM-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "atmInterfaceTCEntry"):
                for c in self.atminterfacetcentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = AtmMib.Atminterfacetctable.Atminterfacetcentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.atminterfacetcentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "atmInterfaceTCEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Atmtrafficdescrparamtable(Entity):
        """
        This table contains information on ATM traffic
        descriptor type and the associated parameters.
        
        .. attribute:: atmtrafficdescrparamentry
        
        	This list contains ATM traffic descriptor type and the associated parameters
        	**type**\: list of    :py:class:`Atmtrafficdescrparamentry <ydk.models.cisco_ios_xe.ATM_MIB.AtmMib.Atmtrafficdescrparamtable.Atmtrafficdescrparamentry>`
        
        

        """

        _prefix = 'ATM-MIB'
        _revision = '1998-10-19'

        def __init__(self):
            super(AtmMib.Atmtrafficdescrparamtable, self).__init__()

            self.yang_name = "atmTrafficDescrParamTable"
            self.yang_parent_name = "ATM-MIB"

            self.atmtrafficdescrparamentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(AtmMib.Atmtrafficdescrparamtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(AtmMib.Atmtrafficdescrparamtable, self).__setattr__(name, value)


        class Atmtrafficdescrparamentry(Entity):
            """
            This list contains ATM traffic descriptor
            type and the associated parameters.
            
            .. attribute:: atmtrafficdescrparamindex  <key>
            
            	This object is used by the virtual link table (i.e., VPL or VCL table) to identify the row of this table. When creating a new row in the table the value of this index may be obtained by retrieving the value of atmTrafficDescrParamIndexNext
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: atmservicecategory
            
            	The ATM service category
            	**type**\:   :py:class:`Atmservicecategory <ydk.models.cisco_ios_xe.ATM_TC_MIB.Atmservicecategory>`
            
            .. attribute:: atmtrafficdescrparam1
            
            	The first parameter of the ATM traffic descriptor used according to the value of atmTrafficDescrType
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: atmtrafficdescrparam2
            
            	The second parameter of the ATM traffic descriptor used according to the value of atmTrafficDescrType
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: atmtrafficdescrparam3
            
            	The third parameter of the ATM traffic descriptor used according to the value of atmTrafficDescrType
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: atmtrafficdescrparam4
            
            	The fourth parameter of the ATM traffic descriptor used according to the value of atmTrafficDescrType
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: atmtrafficdescrparam5
            
            	The fifth parameter of the ATM traffic descriptor used according to the value of atmTrafficDescrType
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: atmtrafficdescrrowstatus
            
            	This object is used to create a new row or modify or delete an existing row in this table
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: atmtrafficdescrtype
            
            	The value of this object identifies the type of ATM traffic descriptor. The type may indicate no traffic descriptor or traffic descriptor with one or more parameters. These parameters are specified as a parameter vector, in the corresponding instances of the objects\:     atmTrafficDescrParam1     atmTrafficDescrParam2     atmTrafficDescrParam3     atmTrafficDescrParam4     atmTrafficDescrParam5
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: atmtrafficframediscard
            
            	If set to 'true', this object indicates that the network is requested to treat data for this connection, in the given direction, as frames (e.g. AAL5 CPCS\_PDU's) rather than as individual cells.  While the precise implementation is network\-specific, this treatment may for example involve discarding entire frames during congestion, rather than a few cells from many frames
            	**type**\:  bool
            
            .. attribute:: atmtrafficqosclass
            
            	The value of this object identifies the QoS Class. Four Service classes have been specified in the ATM Forum UNI Specification\: Service Class A\: Constant bit rate video and                  Circuit emulation Service Class B\: Variable bit rate video/audio Service Class C\: Connection\-oriented data Service Class D\: Connectionless data Four QoS classes numbered 1, 2, 3, and 4 have been specified with the aim to support service classes A, B, C, and D respectively. An unspecified QoS Class numbered `0' is used for best effort traffic
            	**type**\:  int
            
            	**range:** 0..255
            
            	**status**\: deprecated
            
            

            """

            _prefix = 'ATM-MIB'
            _revision = '1998-10-19'

            def __init__(self):
                super(AtmMib.Atmtrafficdescrparamtable.Atmtrafficdescrparamentry, self).__init__()

                self.yang_name = "atmTrafficDescrParamEntry"
                self.yang_parent_name = "atmTrafficDescrParamTable"

                self.atmtrafficdescrparamindex = YLeaf(YType.int32, "atmTrafficDescrParamIndex")

                self.atmservicecategory = YLeaf(YType.enumeration, "atmServiceCategory")

                self.atmtrafficdescrparam1 = YLeaf(YType.int32, "atmTrafficDescrParam1")

                self.atmtrafficdescrparam2 = YLeaf(YType.int32, "atmTrafficDescrParam2")

                self.atmtrafficdescrparam3 = YLeaf(YType.int32, "atmTrafficDescrParam3")

                self.atmtrafficdescrparam4 = YLeaf(YType.int32, "atmTrafficDescrParam4")

                self.atmtrafficdescrparam5 = YLeaf(YType.int32, "atmTrafficDescrParam5")

                self.atmtrafficdescrrowstatus = YLeaf(YType.enumeration, "atmTrafficDescrRowStatus")

                self.atmtrafficdescrtype = YLeaf(YType.str, "atmTrafficDescrType")

                self.atmtrafficframediscard = YLeaf(YType.boolean, "atmTrafficFrameDiscard")

                self.atmtrafficqosclass = YLeaf(YType.int32, "atmTrafficQoSClass")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("atmtrafficdescrparamindex",
                                "atmservicecategory",
                                "atmtrafficdescrparam1",
                                "atmtrafficdescrparam2",
                                "atmtrafficdescrparam3",
                                "atmtrafficdescrparam4",
                                "atmtrafficdescrparam5",
                                "atmtrafficdescrrowstatus",
                                "atmtrafficdescrtype",
                                "atmtrafficframediscard",
                                "atmtrafficqosclass") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(AtmMib.Atmtrafficdescrparamtable.Atmtrafficdescrparamentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(AtmMib.Atmtrafficdescrparamtable.Atmtrafficdescrparamentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.atmtrafficdescrparamindex.is_set or
                    self.atmservicecategory.is_set or
                    self.atmtrafficdescrparam1.is_set or
                    self.atmtrafficdescrparam2.is_set or
                    self.atmtrafficdescrparam3.is_set or
                    self.atmtrafficdescrparam4.is_set or
                    self.atmtrafficdescrparam5.is_set or
                    self.atmtrafficdescrrowstatus.is_set or
                    self.atmtrafficdescrtype.is_set or
                    self.atmtrafficframediscard.is_set or
                    self.atmtrafficqosclass.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.atmtrafficdescrparamindex.yfilter != YFilter.not_set or
                    self.atmservicecategory.yfilter != YFilter.not_set or
                    self.atmtrafficdescrparam1.yfilter != YFilter.not_set or
                    self.atmtrafficdescrparam2.yfilter != YFilter.not_set or
                    self.atmtrafficdescrparam3.yfilter != YFilter.not_set or
                    self.atmtrafficdescrparam4.yfilter != YFilter.not_set or
                    self.atmtrafficdescrparam5.yfilter != YFilter.not_set or
                    self.atmtrafficdescrrowstatus.yfilter != YFilter.not_set or
                    self.atmtrafficdescrtype.yfilter != YFilter.not_set or
                    self.atmtrafficframediscard.yfilter != YFilter.not_set or
                    self.atmtrafficqosclass.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "atmTrafficDescrParamEntry" + "[atmTrafficDescrParamIndex='" + self.atmtrafficdescrparamindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "ATM-MIB:ATM-MIB/atmTrafficDescrParamTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.atmtrafficdescrparamindex.is_set or self.atmtrafficdescrparamindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmtrafficdescrparamindex.get_name_leafdata())
                if (self.atmservicecategory.is_set or self.atmservicecategory.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmservicecategory.get_name_leafdata())
                if (self.atmtrafficdescrparam1.is_set or self.atmtrafficdescrparam1.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmtrafficdescrparam1.get_name_leafdata())
                if (self.atmtrafficdescrparam2.is_set or self.atmtrafficdescrparam2.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmtrafficdescrparam2.get_name_leafdata())
                if (self.atmtrafficdescrparam3.is_set or self.atmtrafficdescrparam3.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmtrafficdescrparam3.get_name_leafdata())
                if (self.atmtrafficdescrparam4.is_set or self.atmtrafficdescrparam4.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmtrafficdescrparam4.get_name_leafdata())
                if (self.atmtrafficdescrparam5.is_set or self.atmtrafficdescrparam5.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmtrafficdescrparam5.get_name_leafdata())
                if (self.atmtrafficdescrrowstatus.is_set or self.atmtrafficdescrrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmtrafficdescrrowstatus.get_name_leafdata())
                if (self.atmtrafficdescrtype.is_set or self.atmtrafficdescrtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmtrafficdescrtype.get_name_leafdata())
                if (self.atmtrafficframediscard.is_set or self.atmtrafficframediscard.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmtrafficframediscard.get_name_leafdata())
                if (self.atmtrafficqosclass.is_set or self.atmtrafficqosclass.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmtrafficqosclass.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "atmTrafficDescrParamIndex" or name == "atmServiceCategory" or name == "atmTrafficDescrParam1" or name == "atmTrafficDescrParam2" or name == "atmTrafficDescrParam3" or name == "atmTrafficDescrParam4" or name == "atmTrafficDescrParam5" or name == "atmTrafficDescrRowStatus" or name == "atmTrafficDescrType" or name == "atmTrafficFrameDiscard" or name == "atmTrafficQoSClass"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "atmTrafficDescrParamIndex"):
                    self.atmtrafficdescrparamindex = value
                    self.atmtrafficdescrparamindex.value_namespace = name_space
                    self.atmtrafficdescrparamindex.value_namespace_prefix = name_space_prefix
                if(value_path == "atmServiceCategory"):
                    self.atmservicecategory = value
                    self.atmservicecategory.value_namespace = name_space
                    self.atmservicecategory.value_namespace_prefix = name_space_prefix
                if(value_path == "atmTrafficDescrParam1"):
                    self.atmtrafficdescrparam1 = value
                    self.atmtrafficdescrparam1.value_namespace = name_space
                    self.atmtrafficdescrparam1.value_namespace_prefix = name_space_prefix
                if(value_path == "atmTrafficDescrParam2"):
                    self.atmtrafficdescrparam2 = value
                    self.atmtrafficdescrparam2.value_namespace = name_space
                    self.atmtrafficdescrparam2.value_namespace_prefix = name_space_prefix
                if(value_path == "atmTrafficDescrParam3"):
                    self.atmtrafficdescrparam3 = value
                    self.atmtrafficdescrparam3.value_namespace = name_space
                    self.atmtrafficdescrparam3.value_namespace_prefix = name_space_prefix
                if(value_path == "atmTrafficDescrParam4"):
                    self.atmtrafficdescrparam4 = value
                    self.atmtrafficdescrparam4.value_namespace = name_space
                    self.atmtrafficdescrparam4.value_namespace_prefix = name_space_prefix
                if(value_path == "atmTrafficDescrParam5"):
                    self.atmtrafficdescrparam5 = value
                    self.atmtrafficdescrparam5.value_namespace = name_space
                    self.atmtrafficdescrparam5.value_namespace_prefix = name_space_prefix
                if(value_path == "atmTrafficDescrRowStatus"):
                    self.atmtrafficdescrrowstatus = value
                    self.atmtrafficdescrrowstatus.value_namespace = name_space
                    self.atmtrafficdescrrowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "atmTrafficDescrType"):
                    self.atmtrafficdescrtype = value
                    self.atmtrafficdescrtype.value_namespace = name_space
                    self.atmtrafficdescrtype.value_namespace_prefix = name_space_prefix
                if(value_path == "atmTrafficFrameDiscard"):
                    self.atmtrafficframediscard = value
                    self.atmtrafficframediscard.value_namespace = name_space
                    self.atmtrafficframediscard.value_namespace_prefix = name_space_prefix
                if(value_path == "atmTrafficQoSClass"):
                    self.atmtrafficqosclass = value
                    self.atmtrafficqosclass.value_namespace = name_space
                    self.atmtrafficqosclass.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.atmtrafficdescrparamentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.atmtrafficdescrparamentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "atmTrafficDescrParamTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "ATM-MIB:ATM-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "atmTrafficDescrParamEntry"):
                for c in self.atmtrafficdescrparamentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = AtmMib.Atmtrafficdescrparamtable.Atmtrafficdescrparamentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.atmtrafficdescrparamentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "atmTrafficDescrParamEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Atmvpltable(Entity):
        """
        The Virtual Path Link (VPL) table.  A
        bi\-directional VPL is modeled as one entry
        in this table. This table can be used for
        PVCs, SVCs and Soft PVCs.
        Entries are not present in this table for
        the VPIs used by entries in the atmVclTable.
        
        .. attribute:: atmvplentry
        
        	An entry in the VPL table.  This entry is used to model a bi\-directional VPL. To create a VPL at an ATM interface, either of the following procedures are used\:  Negotiated VPL establishment  (1) The management application creates   a VPL entry in the atmVplTable   by setting atmVplRowStatus to createAndWait(5).   This may fail for the following reasons\:   \- The selected VPI value is unavailable,   \- The selected VPI value is in use.   Otherwise, the agent creates a row and   reserves the VPI value on that port.  (2) The manager selects an existing row(s) in the   atmTrafficDescrParamTable,   thereby, selecting a set of self\-consistent   ATM traffic parameters and the service category   for receive and transmit directions of the VPL.  (2a) If no suitable row(s) in the   atmTrafficDescrParamTable exists,   the manager must create a new row(s)   in that table.  (2b) The manager characterizes the VPL's traffic   parameters through setting the   atmVplReceiveTrafficDescrIndex and the   atmVplTransmitTrafficDescrIndex values   in the VPL table, which point to the rows   containing desired ATM traffic parameter values   in the atmTrafficDescrParamTable.  The agent   will check the availability of resources and   may refuse the request.   If the transmit and receive service categories   are inconsistent, the agent should refuse the   request.  (3) The manager activates the VPL by setting the   the atmVplRowStatus to active(1).   If this set is successful, the agent has   reserved the resources to satisfy the requested   traffic parameter values and the service category   for that VPL.  (4) If the VPL terminates a VPC in the ATM host   or switch, the manager turns on the   atmVplAdminStatus to up(1) to turn the VPL   traffic flow on.  Otherwise, the   atmVpCrossConnectTable  must be used   to cross\-connect the VPL to another VPL(s)   in an ATM switch or network.  One\-Shot VPL Establishment  A VPL may also be established in one step by a set\-request with all necessary VPL parameter values and atmVplRowStatus set to createAndGo(4).  In contrast to the negotiated VPL establishment which allows for detailed error checking (i.e., set errors are explicitly linked to particular resource acquisition failures), the one\-shot VPL establishment performs the setup on one operation but does not have the advantage of step\-wise error checking.  VPL Retirement  A VPL is released by setting atmVplRowStatus to destroy(6), and the agent may release all associated resources
        	**type**\: list of    :py:class:`Atmvplentry <ydk.models.cisco_ios_xe.ATM_MIB.AtmMib.Atmvpltable.Atmvplentry>`
        
        

        """

        _prefix = 'ATM-MIB'
        _revision = '1998-10-19'

        def __init__(self):
            super(AtmMib.Atmvpltable, self).__init__()

            self.yang_name = "atmVplTable"
            self.yang_parent_name = "ATM-MIB"

            self.atmvplentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(AtmMib.Atmvpltable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(AtmMib.Atmvpltable, self).__setattr__(name, value)


        class Atmvplentry(Entity):
            """
            An entry in the VPL table.  This entry is
            used to model a bi\-directional VPL.
            To create a VPL at an ATM interface,
            either of the following procedures are used\:
            
            Negotiated VPL establishment
            
            (1) The management application creates
              a VPL entry in the atmVplTable
              by setting atmVplRowStatus to createAndWait(5).
              This may fail for the following reasons\:
              \- The selected VPI value is unavailable,
              \- The selected VPI value is in use.
              Otherwise, the agent creates a row and
              reserves the VPI value on that port.
            
            (2) The manager selects an existing row(s) in the
              atmTrafficDescrParamTable,
              thereby, selecting a set of self\-consistent
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
              to cross\-connect the VPL to another VPL(s)
              in an ATM switch or network.
            
            One\-Shot VPL Establishment
            
            A VPL may also be established in one step by a
            set\-request with all necessary VPL parameter
            values and atmVplRowStatus set to createAndGo(4).
            
            In contrast to the negotiated VPL establishment
            which allows for detailed error checking
            (i.e., set errors are explicitly linked to
            particular resource acquisition failures),
            the one\-shot VPL establishment
            performs the setup on one operation but
            does not have the advantage of step\-wise
            error checking.
            
            VPL Retirement
            
            A VPL is released by setting atmVplRowStatus to
            destroy(6), and the agent may release all
            associated resources.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: atmvplvpi  <key>
            
            	The VPI value of the VPL
            	**type**\:  int
            
            	**range:** 0..4095
            
            .. attribute:: atmvpladminstatus
            
            	This object is instanciated only for a VPL which terminates a VPC (i.e., one which is NOT cross\-connected to other VPLs). Its value specifies the desired administrative state of the VPL
            	**type**\:   :py:class:`Atmvorxadminstatus <ydk.models.cisco_ios_xe.ATM_TC_MIB.Atmvorxadminstatus>`
            
            .. attribute:: atmvplcasttype
            
            	The connection topology type
            	**type**\:   :py:class:`Atmconncasttype <ydk.models.cisco_ios_xe.ATM_TC_MIB.Atmconncasttype>`
            
            .. attribute:: atmvplconnkind
            
            	The use of call control
            	**type**\:   :py:class:`Atmconnkind <ydk.models.cisco_ios_xe.ATM_TC_MIB.Atmconnkind>`
            
            .. attribute:: atmvplcrossconnectidentifier
            
            	This object is instantiated only for a VPL which is cross\-connected to other VPLs that belong to the same VPC.  All such associated VPLs have the same value of this object, and all their cross\-connections are identified either by entries that are indexed by the same value of atmVpCrossConnectIndex in the atmVpCrossConnectTable of this MIB module or by the same value of the cross\-connect index in the cross\-connect table for SVCs and Soft PVCs (defined in a separate MIB module). At no time should entries in these respective cross\-connect tables exist simultaneously with the same cross\-connect index value. The value of this object is initialized by the agent after the associated entries in the atmVpCrossConnectTable have been created
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: atmvpllastchange
            
            	The value of sysUpTime at the time this VPL entered its current operational state
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: atmvploperstatus
            
            	The current operational status of the VPL
            	**type**\:   :py:class:`Atmvorxoperstatus <ydk.models.cisco_ios_xe.ATM_TC_MIB.Atmvorxoperstatus>`
            
            .. attribute:: atmvplreceivetrafficdescrindex
            
            	The value of this object identifies the row in the atmTrafficDescrParamTable which applies to the receive direction of the VPL
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: atmvplrowstatus
            
            	This object is used to create, delete or modify a row in this table. To create a new VCL, this object is initially set to 'createAndWait' or 'createAndGo'.  This object should not be set to 'active' unless the following columnar objects have been set to their desired value in this row\: atmVplReceiveTrafficDescrIndex and atmVplTransmitTrafficDescrIndex. The DESCRIPTION of atmVplEntry provides further guidance to row treatment in this table
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: atmvpltransmittrafficdescrindex
            
            	The value of this object identifies the row in the atmTrafficDescrParamTable which applies to the transmit direction of the VPL
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            

            """

            _prefix = 'ATM-MIB'
            _revision = '1998-10-19'

            def __init__(self):
                super(AtmMib.Atmvpltable.Atmvplentry, self).__init__()

                self.yang_name = "atmVplEntry"
                self.yang_parent_name = "atmVplTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.atmvplvpi = YLeaf(YType.int32, "atmVplVpi")

                self.atmvpladminstatus = YLeaf(YType.enumeration, "atmVplAdminStatus")

                self.atmvplcasttype = YLeaf(YType.enumeration, "atmVplCastType")

                self.atmvplconnkind = YLeaf(YType.enumeration, "atmVplConnKind")

                self.atmvplcrossconnectidentifier = YLeaf(YType.int32, "atmVplCrossConnectIdentifier")

                self.atmvpllastchange = YLeaf(YType.uint32, "atmVplLastChange")

                self.atmvploperstatus = YLeaf(YType.enumeration, "atmVplOperStatus")

                self.atmvplreceivetrafficdescrindex = YLeaf(YType.int32, "atmVplReceiveTrafficDescrIndex")

                self.atmvplrowstatus = YLeaf(YType.enumeration, "atmVplRowStatus")

                self.atmvpltransmittrafficdescrindex = YLeaf(YType.int32, "atmVplTransmitTrafficDescrIndex")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ifindex",
                                "atmvplvpi",
                                "atmvpladminstatus",
                                "atmvplcasttype",
                                "atmvplconnkind",
                                "atmvplcrossconnectidentifier",
                                "atmvpllastchange",
                                "atmvploperstatus",
                                "atmvplreceivetrafficdescrindex",
                                "atmvplrowstatus",
                                "atmvpltransmittrafficdescrindex") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(AtmMib.Atmvpltable.Atmvplentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(AtmMib.Atmvpltable.Atmvplentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.atmvplvpi.is_set or
                    self.atmvpladminstatus.is_set or
                    self.atmvplcasttype.is_set or
                    self.atmvplconnkind.is_set or
                    self.atmvplcrossconnectidentifier.is_set or
                    self.atmvpllastchange.is_set or
                    self.atmvploperstatus.is_set or
                    self.atmvplreceivetrafficdescrindex.is_set or
                    self.atmvplrowstatus.is_set or
                    self.atmvpltransmittrafficdescrindex.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.atmvplvpi.yfilter != YFilter.not_set or
                    self.atmvpladminstatus.yfilter != YFilter.not_set or
                    self.atmvplcasttype.yfilter != YFilter.not_set or
                    self.atmvplconnkind.yfilter != YFilter.not_set or
                    self.atmvplcrossconnectidentifier.yfilter != YFilter.not_set or
                    self.atmvpllastchange.yfilter != YFilter.not_set or
                    self.atmvploperstatus.yfilter != YFilter.not_set or
                    self.atmvplreceivetrafficdescrindex.yfilter != YFilter.not_set or
                    self.atmvplrowstatus.yfilter != YFilter.not_set or
                    self.atmvpltransmittrafficdescrindex.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "atmVplEntry" + "[ifIndex='" + self.ifindex.get() + "']" + "[atmVplVpi='" + self.atmvplvpi.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "ATM-MIB:ATM-MIB/atmVplTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.atmvplvpi.is_set or self.atmvplvpi.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvplvpi.get_name_leafdata())
                if (self.atmvpladminstatus.is_set or self.atmvpladminstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvpladminstatus.get_name_leafdata())
                if (self.atmvplcasttype.is_set or self.atmvplcasttype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvplcasttype.get_name_leafdata())
                if (self.atmvplconnkind.is_set or self.atmvplconnkind.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvplconnkind.get_name_leafdata())
                if (self.atmvplcrossconnectidentifier.is_set or self.atmvplcrossconnectidentifier.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvplcrossconnectidentifier.get_name_leafdata())
                if (self.atmvpllastchange.is_set or self.atmvpllastchange.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvpllastchange.get_name_leafdata())
                if (self.atmvploperstatus.is_set or self.atmvploperstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvploperstatus.get_name_leafdata())
                if (self.atmvplreceivetrafficdescrindex.is_set or self.atmvplreceivetrafficdescrindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvplreceivetrafficdescrindex.get_name_leafdata())
                if (self.atmvplrowstatus.is_set or self.atmvplrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvplrowstatus.get_name_leafdata())
                if (self.atmvpltransmittrafficdescrindex.is_set or self.atmvpltransmittrafficdescrindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvpltransmittrafficdescrindex.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "atmVplVpi" or name == "atmVplAdminStatus" or name == "atmVplCastType" or name == "atmVplConnKind" or name == "atmVplCrossConnectIdentifier" or name == "atmVplLastChange" or name == "atmVplOperStatus" or name == "atmVplReceiveTrafficDescrIndex" or name == "atmVplRowStatus" or name == "atmVplTransmitTrafficDescrIndex"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "atmVplVpi"):
                    self.atmvplvpi = value
                    self.atmvplvpi.value_namespace = name_space
                    self.atmvplvpi.value_namespace_prefix = name_space_prefix
                if(value_path == "atmVplAdminStatus"):
                    self.atmvpladminstatus = value
                    self.atmvpladminstatus.value_namespace = name_space
                    self.atmvpladminstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "atmVplCastType"):
                    self.atmvplcasttype = value
                    self.atmvplcasttype.value_namespace = name_space
                    self.atmvplcasttype.value_namespace_prefix = name_space_prefix
                if(value_path == "atmVplConnKind"):
                    self.atmvplconnkind = value
                    self.atmvplconnkind.value_namespace = name_space
                    self.atmvplconnkind.value_namespace_prefix = name_space_prefix
                if(value_path == "atmVplCrossConnectIdentifier"):
                    self.atmvplcrossconnectidentifier = value
                    self.atmvplcrossconnectidentifier.value_namespace = name_space
                    self.atmvplcrossconnectidentifier.value_namespace_prefix = name_space_prefix
                if(value_path == "atmVplLastChange"):
                    self.atmvpllastchange = value
                    self.atmvpllastchange.value_namespace = name_space
                    self.atmvpllastchange.value_namespace_prefix = name_space_prefix
                if(value_path == "atmVplOperStatus"):
                    self.atmvploperstatus = value
                    self.atmvploperstatus.value_namespace = name_space
                    self.atmvploperstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "atmVplReceiveTrafficDescrIndex"):
                    self.atmvplreceivetrafficdescrindex = value
                    self.atmvplreceivetrafficdescrindex.value_namespace = name_space
                    self.atmvplreceivetrafficdescrindex.value_namespace_prefix = name_space_prefix
                if(value_path == "atmVplRowStatus"):
                    self.atmvplrowstatus = value
                    self.atmvplrowstatus.value_namespace = name_space
                    self.atmvplrowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "atmVplTransmitTrafficDescrIndex"):
                    self.atmvpltransmittrafficdescrindex = value
                    self.atmvpltransmittrafficdescrindex.value_namespace = name_space
                    self.atmvpltransmittrafficdescrindex.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.atmvplentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.atmvplentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "atmVplTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "ATM-MIB:ATM-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "atmVplEntry"):
                for c in self.atmvplentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = AtmMib.Atmvpltable.Atmvplentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.atmvplentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "atmVplEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Atmvcltable(Entity):
        """
        The Virtual Channel Link (VCL) table.  A
        bi\-directional VCL is modeled as one entry
        in this table. This table can be used for
        PVCs, SVCs and Soft PVCs.
        
        .. attribute:: atmvclentry
        
        	An entry in the VCL table. This entry is used to model a bi\-directional VCL. To create a VCL at an ATM interface, either of the following procedures are used\:  Negotiated VCL establishment  (1) The management application creates   a VCL entry in the atmVclTable   by setting atmVclRowStatus to createAndWait(5).   This may fail for the following reasons\:   \- The selected VPI/VCI values are unavailable,   \- The selected VPI/VCI values are in use.   Otherwise, the agent creates a row and   reserves the VPI/VCI values on that port.  (2) The manager selects an existing row(s) in the   atmTrafficDescrParamTable,   thereby, selecting a set of self\-consistent   ATM traffic parameters and the service category   for receive and transmit directions of the VCL.   (2a) If no suitable row(s) in the   atmTrafficDescrParamTable exists,   the manager must create a new row(s)   in that table.  (2b) The manager characterizes the VCL's traffic   parameters through setting the   atmVclReceiveTrafficDescrIndex and the   atmVclTransmitTrafficDescrIndex values   in the VCL table, which point to the rows   containing desired ATM traffic parameter values   in the atmTrafficDescrParamTable.  The agent   will check the availability of resources and   may refuse the request.   If the transmit and receive service categories   are inconsistent, the agent should refuse the   request.  (3) The manager activates the VCL by setting the   the atmVclRowStatus to active(1) (for   requirements on this activation see the   description of atmVclRowStatus).   If this set is successful, the agent has   reserved the resources to satisfy the requested   traffic parameter values and the service category   for that VCL. (4) If the VCL terminates a VCC in the ATM host   or switch, the manager turns on the   atmVclAdminStatus to up(1) to turn the VCL   traffic flow on.  Otherwise, the   atmVcCrossConnectTable  must be used   to cross\-connect the VCL to another VCL(s)   in an ATM switch or network.  One\-Shot VCL Establishment  A VCL may also be established in one step by a set\-request with all necessary VCL parameter values and atmVclRowStatus set to createAndGo(4).  In contrast to the negotiated VCL establishment which allows for detailed error checking (i.e., set errors are explicitly linked to particular resource acquisition failures), the one\-shot VCL establishment performs the setup on one operation but does not have the advantage of step\-wise error checking.  VCL Retirement  A VCL is released by setting atmVclRowStatus to destroy(6), and the agent may release all associated resources
        	**type**\: list of    :py:class:`Atmvclentry <ydk.models.cisco_ios_xe.ATM_MIB.AtmMib.Atmvcltable.Atmvclentry>`
        
        

        """

        _prefix = 'ATM-MIB'
        _revision = '1998-10-19'

        def __init__(self):
            super(AtmMib.Atmvcltable, self).__init__()

            self.yang_name = "atmVclTable"
            self.yang_parent_name = "ATM-MIB"

            self.atmvclentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(AtmMib.Atmvcltable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(AtmMib.Atmvcltable, self).__setattr__(name, value)


        class Atmvclentry(Entity):
            """
            An entry in the VCL table. This entry is
            used to model a bi\-directional VCL.
            To create a VCL at an ATM interface,
            either of the following procedures are used\:
            
            Negotiated VCL establishment
            
            (1) The management application creates
              a VCL entry in the atmVclTable
              by setting atmVclRowStatus to createAndWait(5).
              This may fail for the following reasons\:
              \- The selected VPI/VCI values are unavailable,
              \- The selected VPI/VCI values are in use.
              Otherwise, the agent creates a row and
              reserves the VPI/VCI values on that port.
            
            (2) The manager selects an existing row(s) in the
              atmTrafficDescrParamTable,
              thereby, selecting a set of self\-consistent
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
              to cross\-connect the VCL to another VCL(s)
              in an ATM switch or network.
            
            One\-Shot VCL Establishment
            
            A VCL may also be established in one step by a
            set\-request with all necessary VCL parameter
            values and atmVclRowStatus set to createAndGo(4).
            
            In contrast to the negotiated VCL establishment
            which allows for detailed error checking
            (i.e., set errors are explicitly linked to
            particular resource acquisition failures),
            the one\-shot VCL establishment
            performs the setup on one operation but
            does not have the advantage of step\-wise
            error checking.
            
            VCL Retirement
            
            A VCL is released by setting atmVclRowStatus to
            destroy(6), and the agent may release all
            associated resources.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: atmvclvpi  <key>
            
            	The VPI value of the VCL
            	**type**\:  int
            
            	**range:** 0..4095
            
            .. attribute:: atmvclvci  <key>
            
            	The VCI value of the VCL
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: atmvccaal5cpcsreceivesdusize
            
            	An instance of this object only exists when the local VCL end\-point is also the VCC end\-point, and AAL5 is in use. The maximum AAL5 CPCS SDU size in octets that is supported on the receive direction of this VCC
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: atmvccaal5cpcstransmitsdusize
            
            	An instance of this object only exists when the local VCL end\-point is also the VCC end\-point, and AAL5 is in use. The maximum AAL5 CPCS SDU size in octets that is supported on the transmit direction of this VCC
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: atmvccaal5encapstype
            
            	An instance of this object only exists when the local VCL end\-point is also the VCC end\-point, and AAL5 is in use. The type of data encapsulation used over the AAL5 SSCS layer. The definitions reference RFC 1483 Multiprotocol Encapsulation over ATM AAL5 and to the ATM Forum LAN Emulation specification
            	**type**\:   :py:class:`Atmvccaal5Encapstype <ydk.models.cisco_ios_xe.ATM_MIB.AtmMib.Atmvcltable.Atmvclentry.Atmvccaal5Encapstype>`
            
            .. attribute:: atmvccaaltype
            
            	An instance of this object only exists when the local VCL end\-point is also the VCC end\-point, and AAL is in use. The type of AAL used on this VCC. The AAL type includes AAL1, AAL2, AAL3/4, and AAL5. The other(4) may be user\-defined AAL type.  The unknown type indicates that the AAL type cannot be determined
            	**type**\:   :py:class:`Atmvccaaltype <ydk.models.cisco_ios_xe.ATM_MIB.AtmMib.Atmvcltable.Atmvclentry.Atmvccaaltype>`
            
            .. attribute:: atmvcladminstatus
            
            	This object is instanciated only for a VCL which terminates a VCC (i.e., one which is NOT cross\-connected to other VCLs). Its value specifies the desired administrative state of the VCL
            	**type**\:   :py:class:`Atmvorxadminstatus <ydk.models.cisco_ios_xe.ATM_TC_MIB.Atmvorxadminstatus>`
            
            .. attribute:: atmvclcasttype
            
            	The connection topology type
            	**type**\:   :py:class:`Atmconncasttype <ydk.models.cisco_ios_xe.ATM_TC_MIB.Atmconncasttype>`
            
            .. attribute:: atmvclconnkind
            
            	The use of call control
            	**type**\:   :py:class:`Atmconnkind <ydk.models.cisco_ios_xe.ATM_TC_MIB.Atmconnkind>`
            
            .. attribute:: atmvclcrossconnectidentifier
            
            	This object is instantiated only for a VCL which is cross\-connected to other VCLs that belong to the same VCC.  All such associated VCLs have the same value of this object, and all their cross\-connections are identified either by entries that are indexed by the same value of atmVcCrossConnectIndex in the atmVcCrossConnectTable of this MIB module or by the same value of the cross\-connect index in the cross\-connect table for SVCs and Soft PVCs (defined in a separate MIB module).  At no time should entries in these respective cross\-connect tables exist simultaneously with the same cross\-connect index value. The value of this object is initialized by the agent after the associated entries in the atmVcCrossConnectTable have been created
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: atmvcllastchange
            
            	The value of sysUpTime at the time this VCL entered its current operational state
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: atmvcloperstatus
            
            	The current operational status of the VCL
            	**type**\:   :py:class:`Atmvorxoperstatus <ydk.models.cisco_ios_xe.ATM_TC_MIB.Atmvorxoperstatus>`
            
            .. attribute:: atmvclreceivetrafficdescrindex
            
            	The value of this object identifies the row in the ATM Traffic Descriptor Table which applies to the receive direction of this VCL
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: atmvclrowstatus
            
            	This object is used to create, delete or modify a row in this table.  To create a new VCL, this object is initially set to 'createAndWait' or 'createAndGo'. This object should not be set to 'active' unless the following columnar objects have been set to their desired value in this row\: atmVclReceiveTrafficDescrIndex, atmVclTransmitTrafficDescrIndex. In addition, if the local VCL end\-point is also the VCC end\-point\: atmVccAalType. In addition, for AAL5 connections only\: atmVccAal5CpcsTransmitSduSize, atmVccAal5CpcsReceiveSduSize, and atmVccAal5EncapsType. (The existence of these objects imply the AAL connection type.). The DESCRIPTION of atmVclEntry provides further guidance to row treatment in this table
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: atmvcltransmittrafficdescrindex
            
            	The value of this object identifies the row of the ATM Traffic Descriptor Table which applies to the transmit direction of this VCL
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: catmxvcloamcellsdropped
            
            	Indicates the number of OAM cells dropped on  this VC
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: cells
            
            .. attribute:: catmxvcloamcellsreceived
            
            	Indicates the number of OAM cells received on  this VC
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: cells
            
            .. attribute:: catmxvcloamcellssent
            
            	Indicates the number of OAM cells sent on  this VC
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: cells
            
            .. attribute:: catmxvcloamdownretrycount
            
            	Specifies OAM retry count before declaring a VC  is down
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmxvcloamendccactcount
            
            	Specifies OAM End\-to\-end Continuity check (CC)  Activation retry count
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmxvcloamendccdeactcount
            
            	Specifies OAM End\-to\-end Continuity check (CC)  Deactivation retry count
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmxvcloamendccretryfreq
            
            	Specifies OAM End\-to\-end Continuity check (CC)  Activation/Deactivation retry frequency
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: catmxvcloamendccstatus
            
            	Indicates OAM End\-to\-end Continuity check (CC)  status
            	**type**\:   :py:class:`Oamccstatus <ydk.models.cisco_ios_xe.CISCO_ATM_EXT_MIB.Oamccstatus>`
            
            .. attribute:: catmxvcloamendccvcstate
            
            	Indicates OAM End\-to\-end Continuity check (CC)  VC state
            	**type**\:   :py:class:`Oamccvcstate <ydk.models.cisco_ios_xe.CISCO_ATM_EXT_MIB.Oamccvcstate>`
            
            .. attribute:: catmxvcloaminf5ais
            
            	Indicates the number of received OAM  F5 Alarm Indication Signal (AIS) cells from the VC
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: cells
            
            .. attribute:: catmxvcloaminf5rdi
            
            	Indicates the number of received OAM  F5 Remote Detection Indication (RDI) cells from  the VC
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: cells
            
            .. attribute:: catmxvcloamloopbackfreq
            
            	Specifies OAM loopback frequency
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: catmxvcloamloopbkstatus
            
            	Indicates OAM loopback status of the VC. disabled(1)  \-\-   No OAMs on this VC. sent(2)      \-\-   OAM sent, waiting for echo. received(3)  \-\-   OAM received from target. failed(4)    \-\-   Last OAM did not return
            	**type**\:   :py:class:`Catmxvcloamloopbkstatus <ydk.models.cisco_ios_xe.ATM_MIB.AtmMib.Atmvcltable.Atmvclentry.Catmxvcloamloopbkstatus>`
            
            .. attribute:: catmxvcloammanage
            
            	Specifies OAM Enable/Disable on the VC. true(1) indicates that OAM is enabled on the VC. false(2) indicates that OAM is disabled on the VC
            	**type**\:  bool
            
            .. attribute:: catmxvcloamoutf5ais
            
            	Indicates the number of transmitted OAM  F5 Alarm Indication Signal (AIS) cells to the VC
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: cells
            
            .. attribute:: catmxvcloamoutf5rdi
            
            	Indicates the number of transmitted OAM  F5 Remote Detection Indication (RDI) cells to the VC
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: cells
            
            .. attribute:: catmxvcloamretryfreq
            
            	Specifies OAM retry polling frequency
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: catmxvcloamsegccactcount
            
            	Specifies OAM Segment Continuity check (CC)  Activation retry count
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmxvcloamsegccdeactcount
            
            	Specifies OAM Segment Continuity check (CC)  Deactivation retry count
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmxvcloamsegccretryfreq
            
            	Specifies OAM Segment Continuity check (CC)  Activation/Deactivation retry frequency
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: catmxvcloamsegccstatus
            
            	Indicates OAM Segment Continuity check (CC) status
            	**type**\:   :py:class:`Oamccstatus <ydk.models.cisco_ios_xe.CISCO_ATM_EXT_MIB.Oamccstatus>`
            
            .. attribute:: catmxvcloamsegccvcstate
            
            	Indicates OAM Segment Continuity check (CC) VC  state
            	**type**\:   :py:class:`Oamccvcstate <ydk.models.cisco_ios_xe.CISCO_ATM_EXT_MIB.Oamccvcstate>`
            
            .. attribute:: catmxvcloamupretrycount
            
            	Specifies OAM retry count before declaring a VC  is up
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmxvcloamvcstate
            
            	Indicates the state of VC OAM. downRetry(1)   \-\-  Loopback failed. Retry sending                     loopbacks with retry frequency.                     VC is up. verified(2)    \-\-  Loopback is successful. notVerified(3) \-\-  Not verified by loopback,                     AIS/RDI conditions are cleared. upRetry(4)     \-\-  Retry successive loopbacks.                     VC is down. aisRDI(5)      \-\-  Received AIS/RDI. Loopback are                     not sent in this state. aisOut(6)      \-\-  Sending AIS. Loopback and reply are                     not sent in this state. notManaged(7)  \-\-  VC is not managed by OAM
            	**type**\:   :py:class:`Catmxvcloamvcstate <ydk.models.cisco_ios_xe.ATM_MIB.AtmMib.Atmvcltable.Atmvclentry.Catmxvcloamvcstate>`
            
            

            """

            _prefix = 'ATM-MIB'
            _revision = '1998-10-19'

            def __init__(self):
                super(AtmMib.Atmvcltable.Atmvclentry, self).__init__()

                self.yang_name = "atmVclEntry"
                self.yang_parent_name = "atmVclTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.atmvclvpi = YLeaf(YType.int32, "atmVclVpi")

                self.atmvclvci = YLeaf(YType.int32, "atmVclVci")

                self.atmvccaal5cpcsreceivesdusize = YLeaf(YType.int32, "atmVccAal5CpcsReceiveSduSize")

                self.atmvccaal5cpcstransmitsdusize = YLeaf(YType.int32, "atmVccAal5CpcsTransmitSduSize")

                self.atmvccaal5encapstype = YLeaf(YType.enumeration, "atmVccAal5EncapsType")

                self.atmvccaaltype = YLeaf(YType.enumeration, "atmVccAalType")

                self.atmvcladminstatus = YLeaf(YType.enumeration, "atmVclAdminStatus")

                self.atmvclcasttype = YLeaf(YType.enumeration, "atmVclCastType")

                self.atmvclconnkind = YLeaf(YType.enumeration, "atmVclConnKind")

                self.atmvclcrossconnectidentifier = YLeaf(YType.int32, "atmVclCrossConnectIdentifier")

                self.atmvcllastchange = YLeaf(YType.uint32, "atmVclLastChange")

                self.atmvcloperstatus = YLeaf(YType.enumeration, "atmVclOperStatus")

                self.atmvclreceivetrafficdescrindex = YLeaf(YType.int32, "atmVclReceiveTrafficDescrIndex")

                self.atmvclrowstatus = YLeaf(YType.enumeration, "atmVclRowStatus")

                self.atmvcltransmittrafficdescrindex = YLeaf(YType.int32, "atmVclTransmitTrafficDescrIndex")

                self.catmxvcloamcellsdropped = YLeaf(YType.uint32, "CISCO-ATM-EXT-MIB:catmxVclOamCellsDropped")

                self.catmxvcloamcellsreceived = YLeaf(YType.uint32, "CISCO-ATM-EXT-MIB:catmxVclOamCellsReceived")

                self.catmxvcloamcellssent = YLeaf(YType.uint32, "CISCO-ATM-EXT-MIB:catmxVclOamCellsSent")

                self.catmxvcloamdownretrycount = YLeaf(YType.uint32, "CISCO-ATM-EXT-MIB:catmxVclOamDownRetryCount")

                self.catmxvcloamendccactcount = YLeaf(YType.uint32, "CISCO-ATM-EXT-MIB:catmxVclOamEndCCActCount")

                self.catmxvcloamendccdeactcount = YLeaf(YType.uint32, "CISCO-ATM-EXT-MIB:catmxVclOamEndCCDeActCount")

                self.catmxvcloamendccretryfreq = YLeaf(YType.uint32, "CISCO-ATM-EXT-MIB:catmxVclOamEndCCRetryFreq")

                self.catmxvcloamendccstatus = YLeaf(YType.enumeration, "CISCO-ATM-EXT-MIB:catmxVclOamEndCCStatus")

                self.catmxvcloamendccvcstate = YLeaf(YType.enumeration, "CISCO-ATM-EXT-MIB:catmxVclOamEndCCVcState")

                self.catmxvcloaminf5ais = YLeaf(YType.uint32, "CISCO-ATM-EXT-MIB:catmxVclOamInF5ais")

                self.catmxvcloaminf5rdi = YLeaf(YType.uint32, "CISCO-ATM-EXT-MIB:catmxVclOamInF5rdi")

                self.catmxvcloamloopbackfreq = YLeaf(YType.uint32, "CISCO-ATM-EXT-MIB:catmxVclOamLoopbackFreq")

                self.catmxvcloamloopbkstatus = YLeaf(YType.enumeration, "CISCO-ATM-EXT-MIB:catmxVclOamLoopBkStatus")

                self.catmxvcloammanage = YLeaf(YType.boolean, "CISCO-ATM-EXT-MIB:catmxVclOamManage")

                self.catmxvcloamoutf5ais = YLeaf(YType.uint32, "CISCO-ATM-EXT-MIB:catmxVclOamOutF5ais")

                self.catmxvcloamoutf5rdi = YLeaf(YType.uint32, "CISCO-ATM-EXT-MIB:catmxVclOamOutF5rdi")

                self.catmxvcloamretryfreq = YLeaf(YType.uint32, "CISCO-ATM-EXT-MIB:catmxVclOamRetryFreq")

                self.catmxvcloamsegccactcount = YLeaf(YType.uint32, "CISCO-ATM-EXT-MIB:catmxVclOamSegCCActCount")

                self.catmxvcloamsegccdeactcount = YLeaf(YType.uint32, "CISCO-ATM-EXT-MIB:catmxVclOamSegCCDeActCount")

                self.catmxvcloamsegccretryfreq = YLeaf(YType.uint32, "CISCO-ATM-EXT-MIB:catmxVclOamSegCCRetryFreq")

                self.catmxvcloamsegccstatus = YLeaf(YType.enumeration, "CISCO-ATM-EXT-MIB:catmxVclOamSegCCStatus")

                self.catmxvcloamsegccvcstate = YLeaf(YType.enumeration, "CISCO-ATM-EXT-MIB:catmxVclOamSegCCVcState")

                self.catmxvcloamupretrycount = YLeaf(YType.uint32, "CISCO-ATM-EXT-MIB:catmxVclOamUpRetryCount")

                self.catmxvcloamvcstate = YLeaf(YType.enumeration, "CISCO-ATM-EXT-MIB:catmxVclOamVcState")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ifindex",
                                "atmvclvpi",
                                "atmvclvci",
                                "atmvccaal5cpcsreceivesdusize",
                                "atmvccaal5cpcstransmitsdusize",
                                "atmvccaal5encapstype",
                                "atmvccaaltype",
                                "atmvcladminstatus",
                                "atmvclcasttype",
                                "atmvclconnkind",
                                "atmvclcrossconnectidentifier",
                                "atmvcllastchange",
                                "atmvcloperstatus",
                                "atmvclreceivetrafficdescrindex",
                                "atmvclrowstatus",
                                "atmvcltransmittrafficdescrindex",
                                "catmxvcloamcellsdropped",
                                "catmxvcloamcellsreceived",
                                "catmxvcloamcellssent",
                                "catmxvcloamdownretrycount",
                                "catmxvcloamendccactcount",
                                "catmxvcloamendccdeactcount",
                                "catmxvcloamendccretryfreq",
                                "catmxvcloamendccstatus",
                                "catmxvcloamendccvcstate",
                                "catmxvcloaminf5ais",
                                "catmxvcloaminf5rdi",
                                "catmxvcloamloopbackfreq",
                                "catmxvcloamloopbkstatus",
                                "catmxvcloammanage",
                                "catmxvcloamoutf5ais",
                                "catmxvcloamoutf5rdi",
                                "catmxvcloamretryfreq",
                                "catmxvcloamsegccactcount",
                                "catmxvcloamsegccdeactcount",
                                "catmxvcloamsegccretryfreq",
                                "catmxvcloamsegccstatus",
                                "catmxvcloamsegccvcstate",
                                "catmxvcloamupretrycount",
                                "catmxvcloamvcstate") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(AtmMib.Atmvcltable.Atmvclentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(AtmMib.Atmvcltable.Atmvclentry, self).__setattr__(name, value)

            class Atmvccaal5Encapstype(Enum):
                """
                Atmvccaal5Encapstype

                An instance of this object only exists when the

                local VCL end\-point is also the VCC end\-point,

                and AAL5 is in use.

                The type of data encapsulation used over

                the AAL5 SSCS layer. The definitions reference

                RFC 1483 Multiprotocol Encapsulation

                over ATM AAL5 and to the ATM Forum

                LAN Emulation specification.

                .. data:: vcMultiplexRoutedProtocol = 1

                .. data:: vcMultiplexBridgedProtocol8023 = 2

                .. data:: vcMultiplexBridgedProtocol8025 = 3

                .. data:: vcMultiplexBridgedProtocol8026 = 4

                .. data:: vcMultiplexLANemulation8023 = 5

                .. data:: vcMultiplexLANemulation8025 = 6

                .. data:: llcEncapsulation = 7

                .. data:: multiprotocolFrameRelaySscs = 8

                .. data:: other = 9

                .. data:: unknown = 10

                """

                vcMultiplexRoutedProtocol = Enum.YLeaf(1, "vcMultiplexRoutedProtocol")

                vcMultiplexBridgedProtocol8023 = Enum.YLeaf(2, "vcMultiplexBridgedProtocol8023")

                vcMultiplexBridgedProtocol8025 = Enum.YLeaf(3, "vcMultiplexBridgedProtocol8025")

                vcMultiplexBridgedProtocol8026 = Enum.YLeaf(4, "vcMultiplexBridgedProtocol8026")

                vcMultiplexLANemulation8023 = Enum.YLeaf(5, "vcMultiplexLANemulation8023")

                vcMultiplexLANemulation8025 = Enum.YLeaf(6, "vcMultiplexLANemulation8025")

                llcEncapsulation = Enum.YLeaf(7, "llcEncapsulation")

                multiprotocolFrameRelaySscs = Enum.YLeaf(8, "multiprotocolFrameRelaySscs")

                other = Enum.YLeaf(9, "other")

                unknown = Enum.YLeaf(10, "unknown")


            class Atmvccaaltype(Enum):
                """
                Atmvccaaltype

                An instance of this object only exists when the

                local VCL end\-point is also the VCC end\-point,

                and AAL is in use.

                The type of AAL used on this VCC.

                The AAL type includes AAL1, AAL2, AAL3/4,

                and AAL5. The other(4) may be user\-defined

                AAL type.  The unknown type indicates that

                the AAL type cannot be determined.

                .. data:: aal1 = 1

                .. data:: aal34 = 2

                .. data:: aal5 = 3

                .. data:: other = 4

                .. data:: unknown = 5

                .. data:: aal2 = 6

                """

                aal1 = Enum.YLeaf(1, "aal1")

                aal34 = Enum.YLeaf(2, "aal34")

                aal5 = Enum.YLeaf(3, "aal5")

                other = Enum.YLeaf(4, "other")

                unknown = Enum.YLeaf(5, "unknown")

                aal2 = Enum.YLeaf(6, "aal2")


            class Catmxvcloamloopbkstatus(Enum):
                """
                Catmxvcloamloopbkstatus

                Indicates OAM loopback status of the VC.

                disabled(1)  \-\-   No OAMs on this VC.

                sent(2)      \-\-   OAM sent, waiting for echo.

                received(3)  \-\-   OAM received from target.

                failed(4)    \-\-   Last OAM did not return.

                .. data:: disabled = 1

                .. data:: sent = 2

                .. data:: received = 3

                .. data:: failed = 4

                """

                disabled = Enum.YLeaf(1, "disabled")

                sent = Enum.YLeaf(2, "sent")

                received = Enum.YLeaf(3, "received")

                failed = Enum.YLeaf(4, "failed")


            class Catmxvcloamvcstate(Enum):
                """
                Catmxvcloamvcstate

                Indicates the state of VC OAM.

                downRetry(1)   \-\-  Loopback failed. Retry sending 

                                   loopbacks with retry frequency. 

                                   VC is up.

                verified(2)    \-\-  Loopback is successful.

                notVerified(3) \-\-  Not verified by loopback, 

                                   AIS/RDI conditions are cleared.

                upRetry(4)     \-\-  Retry successive loopbacks. 

                                   VC is down.

                aisRDI(5)      \-\-  Received AIS/RDI. Loopback are 

                                   not sent in this state.

                aisOut(6)      \-\-  Sending AIS. Loopback and reply are 

                                   not sent in this state.

                notManaged(7)  \-\-  VC is not managed by OAM.

                .. data:: downRetry = 1

                .. data:: verified = 2

                .. data:: notVerified = 3

                .. data:: upRetry = 4

                .. data:: aisRDI = 5

                .. data:: aisOut = 6

                .. data:: notManaged = 7

                """

                downRetry = Enum.YLeaf(1, "downRetry")

                verified = Enum.YLeaf(2, "verified")

                notVerified = Enum.YLeaf(3, "notVerified")

                upRetry = Enum.YLeaf(4, "upRetry")

                aisRDI = Enum.YLeaf(5, "aisRDI")

                aisOut = Enum.YLeaf(6, "aisOut")

                notManaged = Enum.YLeaf(7, "notManaged")


            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.atmvclvpi.is_set or
                    self.atmvclvci.is_set or
                    self.atmvccaal5cpcsreceivesdusize.is_set or
                    self.atmvccaal5cpcstransmitsdusize.is_set or
                    self.atmvccaal5encapstype.is_set or
                    self.atmvccaaltype.is_set or
                    self.atmvcladminstatus.is_set or
                    self.atmvclcasttype.is_set or
                    self.atmvclconnkind.is_set or
                    self.atmvclcrossconnectidentifier.is_set or
                    self.atmvcllastchange.is_set or
                    self.atmvcloperstatus.is_set or
                    self.atmvclreceivetrafficdescrindex.is_set or
                    self.atmvclrowstatus.is_set or
                    self.atmvcltransmittrafficdescrindex.is_set or
                    self.catmxvcloamcellsdropped.is_set or
                    self.catmxvcloamcellsreceived.is_set or
                    self.catmxvcloamcellssent.is_set or
                    self.catmxvcloamdownretrycount.is_set or
                    self.catmxvcloamendccactcount.is_set or
                    self.catmxvcloamendccdeactcount.is_set or
                    self.catmxvcloamendccretryfreq.is_set or
                    self.catmxvcloamendccstatus.is_set or
                    self.catmxvcloamendccvcstate.is_set or
                    self.catmxvcloaminf5ais.is_set or
                    self.catmxvcloaminf5rdi.is_set or
                    self.catmxvcloamloopbackfreq.is_set or
                    self.catmxvcloamloopbkstatus.is_set or
                    self.catmxvcloammanage.is_set or
                    self.catmxvcloamoutf5ais.is_set or
                    self.catmxvcloamoutf5rdi.is_set or
                    self.catmxvcloamretryfreq.is_set or
                    self.catmxvcloamsegccactcount.is_set or
                    self.catmxvcloamsegccdeactcount.is_set or
                    self.catmxvcloamsegccretryfreq.is_set or
                    self.catmxvcloamsegccstatus.is_set or
                    self.catmxvcloamsegccvcstate.is_set or
                    self.catmxvcloamupretrycount.is_set or
                    self.catmxvcloamvcstate.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.atmvclvpi.yfilter != YFilter.not_set or
                    self.atmvclvci.yfilter != YFilter.not_set or
                    self.atmvccaal5cpcsreceivesdusize.yfilter != YFilter.not_set or
                    self.atmvccaal5cpcstransmitsdusize.yfilter != YFilter.not_set or
                    self.atmvccaal5encapstype.yfilter != YFilter.not_set or
                    self.atmvccaaltype.yfilter != YFilter.not_set or
                    self.atmvcladminstatus.yfilter != YFilter.not_set or
                    self.atmvclcasttype.yfilter != YFilter.not_set or
                    self.atmvclconnkind.yfilter != YFilter.not_set or
                    self.atmvclcrossconnectidentifier.yfilter != YFilter.not_set or
                    self.atmvcllastchange.yfilter != YFilter.not_set or
                    self.atmvcloperstatus.yfilter != YFilter.not_set or
                    self.atmvclreceivetrafficdescrindex.yfilter != YFilter.not_set or
                    self.atmvclrowstatus.yfilter != YFilter.not_set or
                    self.atmvcltransmittrafficdescrindex.yfilter != YFilter.not_set or
                    self.catmxvcloamcellsdropped.yfilter != YFilter.not_set or
                    self.catmxvcloamcellsreceived.yfilter != YFilter.not_set or
                    self.catmxvcloamcellssent.yfilter != YFilter.not_set or
                    self.catmxvcloamdownretrycount.yfilter != YFilter.not_set or
                    self.catmxvcloamendccactcount.yfilter != YFilter.not_set or
                    self.catmxvcloamendccdeactcount.yfilter != YFilter.not_set or
                    self.catmxvcloamendccretryfreq.yfilter != YFilter.not_set or
                    self.catmxvcloamendccstatus.yfilter != YFilter.not_set or
                    self.catmxvcloamendccvcstate.yfilter != YFilter.not_set or
                    self.catmxvcloaminf5ais.yfilter != YFilter.not_set or
                    self.catmxvcloaminf5rdi.yfilter != YFilter.not_set or
                    self.catmxvcloamloopbackfreq.yfilter != YFilter.not_set or
                    self.catmxvcloamloopbkstatus.yfilter != YFilter.not_set or
                    self.catmxvcloammanage.yfilter != YFilter.not_set or
                    self.catmxvcloamoutf5ais.yfilter != YFilter.not_set or
                    self.catmxvcloamoutf5rdi.yfilter != YFilter.not_set or
                    self.catmxvcloamretryfreq.yfilter != YFilter.not_set or
                    self.catmxvcloamsegccactcount.yfilter != YFilter.not_set or
                    self.catmxvcloamsegccdeactcount.yfilter != YFilter.not_set or
                    self.catmxvcloamsegccretryfreq.yfilter != YFilter.not_set or
                    self.catmxvcloamsegccstatus.yfilter != YFilter.not_set or
                    self.catmxvcloamsegccvcstate.yfilter != YFilter.not_set or
                    self.catmxvcloamupretrycount.yfilter != YFilter.not_set or
                    self.catmxvcloamvcstate.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "atmVclEntry" + "[ifIndex='" + self.ifindex.get() + "']" + "[atmVclVpi='" + self.atmvclvpi.get() + "']" + "[atmVclVci='" + self.atmvclvci.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "ATM-MIB:ATM-MIB/atmVclTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.atmvclvpi.is_set or self.atmvclvpi.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvclvpi.get_name_leafdata())
                if (self.atmvclvci.is_set or self.atmvclvci.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvclvci.get_name_leafdata())
                if (self.atmvccaal5cpcsreceivesdusize.is_set or self.atmvccaal5cpcsreceivesdusize.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvccaal5cpcsreceivesdusize.get_name_leafdata())
                if (self.atmvccaal5cpcstransmitsdusize.is_set or self.atmvccaal5cpcstransmitsdusize.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvccaal5cpcstransmitsdusize.get_name_leafdata())
                if (self.atmvccaal5encapstype.is_set or self.atmvccaal5encapstype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvccaal5encapstype.get_name_leafdata())
                if (self.atmvccaaltype.is_set or self.atmvccaaltype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvccaaltype.get_name_leafdata())
                if (self.atmvcladminstatus.is_set or self.atmvcladminstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvcladminstatus.get_name_leafdata())
                if (self.atmvclcasttype.is_set or self.atmvclcasttype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvclcasttype.get_name_leafdata())
                if (self.atmvclconnkind.is_set or self.atmvclconnkind.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvclconnkind.get_name_leafdata())
                if (self.atmvclcrossconnectidentifier.is_set or self.atmvclcrossconnectidentifier.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvclcrossconnectidentifier.get_name_leafdata())
                if (self.atmvcllastchange.is_set or self.atmvcllastchange.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvcllastchange.get_name_leafdata())
                if (self.atmvcloperstatus.is_set or self.atmvcloperstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvcloperstatus.get_name_leafdata())
                if (self.atmvclreceivetrafficdescrindex.is_set or self.atmvclreceivetrafficdescrindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvclreceivetrafficdescrindex.get_name_leafdata())
                if (self.atmvclrowstatus.is_set or self.atmvclrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvclrowstatus.get_name_leafdata())
                if (self.atmvcltransmittrafficdescrindex.is_set or self.atmvcltransmittrafficdescrindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvcltransmittrafficdescrindex.get_name_leafdata())
                if (self.catmxvcloamcellsdropped.is_set or self.catmxvcloamcellsdropped.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmxvcloamcellsdropped.get_name_leafdata())
                if (self.catmxvcloamcellsreceived.is_set or self.catmxvcloamcellsreceived.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmxvcloamcellsreceived.get_name_leafdata())
                if (self.catmxvcloamcellssent.is_set or self.catmxvcloamcellssent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmxvcloamcellssent.get_name_leafdata())
                if (self.catmxvcloamdownretrycount.is_set or self.catmxvcloamdownretrycount.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmxvcloamdownretrycount.get_name_leafdata())
                if (self.catmxvcloamendccactcount.is_set or self.catmxvcloamendccactcount.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmxvcloamendccactcount.get_name_leafdata())
                if (self.catmxvcloamendccdeactcount.is_set or self.catmxvcloamendccdeactcount.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmxvcloamendccdeactcount.get_name_leafdata())
                if (self.catmxvcloamendccretryfreq.is_set or self.catmxvcloamendccretryfreq.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmxvcloamendccretryfreq.get_name_leafdata())
                if (self.catmxvcloamendccstatus.is_set or self.catmxvcloamendccstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmxvcloamendccstatus.get_name_leafdata())
                if (self.catmxvcloamendccvcstate.is_set or self.catmxvcloamendccvcstate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmxvcloamendccvcstate.get_name_leafdata())
                if (self.catmxvcloaminf5ais.is_set or self.catmxvcloaminf5ais.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmxvcloaminf5ais.get_name_leafdata())
                if (self.catmxvcloaminf5rdi.is_set or self.catmxvcloaminf5rdi.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmxvcloaminf5rdi.get_name_leafdata())
                if (self.catmxvcloamloopbackfreq.is_set or self.catmxvcloamloopbackfreq.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmxvcloamloopbackfreq.get_name_leafdata())
                if (self.catmxvcloamloopbkstatus.is_set or self.catmxvcloamloopbkstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmxvcloamloopbkstatus.get_name_leafdata())
                if (self.catmxvcloammanage.is_set or self.catmxvcloammanage.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmxvcloammanage.get_name_leafdata())
                if (self.catmxvcloamoutf5ais.is_set or self.catmxvcloamoutf5ais.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmxvcloamoutf5ais.get_name_leafdata())
                if (self.catmxvcloamoutf5rdi.is_set or self.catmxvcloamoutf5rdi.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmxvcloamoutf5rdi.get_name_leafdata())
                if (self.catmxvcloamretryfreq.is_set or self.catmxvcloamretryfreq.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmxvcloamretryfreq.get_name_leafdata())
                if (self.catmxvcloamsegccactcount.is_set or self.catmxvcloamsegccactcount.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmxvcloamsegccactcount.get_name_leafdata())
                if (self.catmxvcloamsegccdeactcount.is_set or self.catmxvcloamsegccdeactcount.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmxvcloamsegccdeactcount.get_name_leafdata())
                if (self.catmxvcloamsegccretryfreq.is_set or self.catmxvcloamsegccretryfreq.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmxvcloamsegccretryfreq.get_name_leafdata())
                if (self.catmxvcloamsegccstatus.is_set or self.catmxvcloamsegccstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmxvcloamsegccstatus.get_name_leafdata())
                if (self.catmxvcloamsegccvcstate.is_set or self.catmxvcloamsegccvcstate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmxvcloamsegccvcstate.get_name_leafdata())
                if (self.catmxvcloamupretrycount.is_set or self.catmxvcloamupretrycount.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmxvcloamupretrycount.get_name_leafdata())
                if (self.catmxvcloamvcstate.is_set or self.catmxvcloamvcstate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.catmxvcloamvcstate.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "atmVclVpi" or name == "atmVclVci" or name == "atmVccAal5CpcsReceiveSduSize" or name == "atmVccAal5CpcsTransmitSduSize" or name == "atmVccAal5EncapsType" or name == "atmVccAalType" or name == "atmVclAdminStatus" or name == "atmVclCastType" or name == "atmVclConnKind" or name == "atmVclCrossConnectIdentifier" or name == "atmVclLastChange" or name == "atmVclOperStatus" or name == "atmVclReceiveTrafficDescrIndex" or name == "atmVclRowStatus" or name == "atmVclTransmitTrafficDescrIndex" or name == "catmxVclOamCellsDropped" or name == "catmxVclOamCellsReceived" or name == "catmxVclOamCellsSent" or name == "catmxVclOamDownRetryCount" or name == "catmxVclOamEndCCActCount" or name == "catmxVclOamEndCCDeActCount" or name == "catmxVclOamEndCCRetryFreq" or name == "catmxVclOamEndCCStatus" or name == "catmxVclOamEndCCVcState" or name == "catmxVclOamInF5ais" or name == "catmxVclOamInF5rdi" or name == "catmxVclOamLoopbackFreq" or name == "catmxVclOamLoopBkStatus" or name == "catmxVclOamManage" or name == "catmxVclOamOutF5ais" or name == "catmxVclOamOutF5rdi" or name == "catmxVclOamRetryFreq" or name == "catmxVclOamSegCCActCount" or name == "catmxVclOamSegCCDeActCount" or name == "catmxVclOamSegCCRetryFreq" or name == "catmxVclOamSegCCStatus" or name == "catmxVclOamSegCCVcState" or name == "catmxVclOamUpRetryCount" or name == "catmxVclOamVcState"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "atmVclVpi"):
                    self.atmvclvpi = value
                    self.atmvclvpi.value_namespace = name_space
                    self.atmvclvpi.value_namespace_prefix = name_space_prefix
                if(value_path == "atmVclVci"):
                    self.atmvclvci = value
                    self.atmvclvci.value_namespace = name_space
                    self.atmvclvci.value_namespace_prefix = name_space_prefix
                if(value_path == "atmVccAal5CpcsReceiveSduSize"):
                    self.atmvccaal5cpcsreceivesdusize = value
                    self.atmvccaal5cpcsreceivesdusize.value_namespace = name_space
                    self.atmvccaal5cpcsreceivesdusize.value_namespace_prefix = name_space_prefix
                if(value_path == "atmVccAal5CpcsTransmitSduSize"):
                    self.atmvccaal5cpcstransmitsdusize = value
                    self.atmvccaal5cpcstransmitsdusize.value_namespace = name_space
                    self.atmvccaal5cpcstransmitsdusize.value_namespace_prefix = name_space_prefix
                if(value_path == "atmVccAal5EncapsType"):
                    self.atmvccaal5encapstype = value
                    self.atmvccaal5encapstype.value_namespace = name_space
                    self.atmvccaal5encapstype.value_namespace_prefix = name_space_prefix
                if(value_path == "atmVccAalType"):
                    self.atmvccaaltype = value
                    self.atmvccaaltype.value_namespace = name_space
                    self.atmvccaaltype.value_namespace_prefix = name_space_prefix
                if(value_path == "atmVclAdminStatus"):
                    self.atmvcladminstatus = value
                    self.atmvcladminstatus.value_namespace = name_space
                    self.atmvcladminstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "atmVclCastType"):
                    self.atmvclcasttype = value
                    self.atmvclcasttype.value_namespace = name_space
                    self.atmvclcasttype.value_namespace_prefix = name_space_prefix
                if(value_path == "atmVclConnKind"):
                    self.atmvclconnkind = value
                    self.atmvclconnkind.value_namespace = name_space
                    self.atmvclconnkind.value_namespace_prefix = name_space_prefix
                if(value_path == "atmVclCrossConnectIdentifier"):
                    self.atmvclcrossconnectidentifier = value
                    self.atmvclcrossconnectidentifier.value_namespace = name_space
                    self.atmvclcrossconnectidentifier.value_namespace_prefix = name_space_prefix
                if(value_path == "atmVclLastChange"):
                    self.atmvcllastchange = value
                    self.atmvcllastchange.value_namespace = name_space
                    self.atmvcllastchange.value_namespace_prefix = name_space_prefix
                if(value_path == "atmVclOperStatus"):
                    self.atmvcloperstatus = value
                    self.atmvcloperstatus.value_namespace = name_space
                    self.atmvcloperstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "atmVclReceiveTrafficDescrIndex"):
                    self.atmvclreceivetrafficdescrindex = value
                    self.atmvclreceivetrafficdescrindex.value_namespace = name_space
                    self.atmvclreceivetrafficdescrindex.value_namespace_prefix = name_space_prefix
                if(value_path == "atmVclRowStatus"):
                    self.atmvclrowstatus = value
                    self.atmvclrowstatus.value_namespace = name_space
                    self.atmvclrowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "atmVclTransmitTrafficDescrIndex"):
                    self.atmvcltransmittrafficdescrindex = value
                    self.atmvcltransmittrafficdescrindex.value_namespace = name_space
                    self.atmvcltransmittrafficdescrindex.value_namespace_prefix = name_space_prefix
                if(value_path == "catmxVclOamCellsDropped"):
                    self.catmxvcloamcellsdropped = value
                    self.catmxvcloamcellsdropped.value_namespace = name_space
                    self.catmxvcloamcellsdropped.value_namespace_prefix = name_space_prefix
                if(value_path == "catmxVclOamCellsReceived"):
                    self.catmxvcloamcellsreceived = value
                    self.catmxvcloamcellsreceived.value_namespace = name_space
                    self.catmxvcloamcellsreceived.value_namespace_prefix = name_space_prefix
                if(value_path == "catmxVclOamCellsSent"):
                    self.catmxvcloamcellssent = value
                    self.catmxvcloamcellssent.value_namespace = name_space
                    self.catmxvcloamcellssent.value_namespace_prefix = name_space_prefix
                if(value_path == "catmxVclOamDownRetryCount"):
                    self.catmxvcloamdownretrycount = value
                    self.catmxvcloamdownretrycount.value_namespace = name_space
                    self.catmxvcloamdownretrycount.value_namespace_prefix = name_space_prefix
                if(value_path == "catmxVclOamEndCCActCount"):
                    self.catmxvcloamendccactcount = value
                    self.catmxvcloamendccactcount.value_namespace = name_space
                    self.catmxvcloamendccactcount.value_namespace_prefix = name_space_prefix
                if(value_path == "catmxVclOamEndCCDeActCount"):
                    self.catmxvcloamendccdeactcount = value
                    self.catmxvcloamendccdeactcount.value_namespace = name_space
                    self.catmxvcloamendccdeactcount.value_namespace_prefix = name_space_prefix
                if(value_path == "catmxVclOamEndCCRetryFreq"):
                    self.catmxvcloamendccretryfreq = value
                    self.catmxvcloamendccretryfreq.value_namespace = name_space
                    self.catmxvcloamendccretryfreq.value_namespace_prefix = name_space_prefix
                if(value_path == "catmxVclOamEndCCStatus"):
                    self.catmxvcloamendccstatus = value
                    self.catmxvcloamendccstatus.value_namespace = name_space
                    self.catmxvcloamendccstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "catmxVclOamEndCCVcState"):
                    self.catmxvcloamendccvcstate = value
                    self.catmxvcloamendccvcstate.value_namespace = name_space
                    self.catmxvcloamendccvcstate.value_namespace_prefix = name_space_prefix
                if(value_path == "catmxVclOamInF5ais"):
                    self.catmxvcloaminf5ais = value
                    self.catmxvcloaminf5ais.value_namespace = name_space
                    self.catmxvcloaminf5ais.value_namespace_prefix = name_space_prefix
                if(value_path == "catmxVclOamInF5rdi"):
                    self.catmxvcloaminf5rdi = value
                    self.catmxvcloaminf5rdi.value_namespace = name_space
                    self.catmxvcloaminf5rdi.value_namespace_prefix = name_space_prefix
                if(value_path == "catmxVclOamLoopbackFreq"):
                    self.catmxvcloamloopbackfreq = value
                    self.catmxvcloamloopbackfreq.value_namespace = name_space
                    self.catmxvcloamloopbackfreq.value_namespace_prefix = name_space_prefix
                if(value_path == "catmxVclOamLoopBkStatus"):
                    self.catmxvcloamloopbkstatus = value
                    self.catmxvcloamloopbkstatus.value_namespace = name_space
                    self.catmxvcloamloopbkstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "catmxVclOamManage"):
                    self.catmxvcloammanage = value
                    self.catmxvcloammanage.value_namespace = name_space
                    self.catmxvcloammanage.value_namespace_prefix = name_space_prefix
                if(value_path == "catmxVclOamOutF5ais"):
                    self.catmxvcloamoutf5ais = value
                    self.catmxvcloamoutf5ais.value_namespace = name_space
                    self.catmxvcloamoutf5ais.value_namespace_prefix = name_space_prefix
                if(value_path == "catmxVclOamOutF5rdi"):
                    self.catmxvcloamoutf5rdi = value
                    self.catmxvcloamoutf5rdi.value_namespace = name_space
                    self.catmxvcloamoutf5rdi.value_namespace_prefix = name_space_prefix
                if(value_path == "catmxVclOamRetryFreq"):
                    self.catmxvcloamretryfreq = value
                    self.catmxvcloamretryfreq.value_namespace = name_space
                    self.catmxvcloamretryfreq.value_namespace_prefix = name_space_prefix
                if(value_path == "catmxVclOamSegCCActCount"):
                    self.catmxvcloamsegccactcount = value
                    self.catmxvcloamsegccactcount.value_namespace = name_space
                    self.catmxvcloamsegccactcount.value_namespace_prefix = name_space_prefix
                if(value_path == "catmxVclOamSegCCDeActCount"):
                    self.catmxvcloamsegccdeactcount = value
                    self.catmxvcloamsegccdeactcount.value_namespace = name_space
                    self.catmxvcloamsegccdeactcount.value_namespace_prefix = name_space_prefix
                if(value_path == "catmxVclOamSegCCRetryFreq"):
                    self.catmxvcloamsegccretryfreq = value
                    self.catmxvcloamsegccretryfreq.value_namespace = name_space
                    self.catmxvcloamsegccretryfreq.value_namespace_prefix = name_space_prefix
                if(value_path == "catmxVclOamSegCCStatus"):
                    self.catmxvcloamsegccstatus = value
                    self.catmxvcloamsegccstatus.value_namespace = name_space
                    self.catmxvcloamsegccstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "catmxVclOamSegCCVcState"):
                    self.catmxvcloamsegccvcstate = value
                    self.catmxvcloamsegccvcstate.value_namespace = name_space
                    self.catmxvcloamsegccvcstate.value_namespace_prefix = name_space_prefix
                if(value_path == "catmxVclOamUpRetryCount"):
                    self.catmxvcloamupretrycount = value
                    self.catmxvcloamupretrycount.value_namespace = name_space
                    self.catmxvcloamupretrycount.value_namespace_prefix = name_space_prefix
                if(value_path == "catmxVclOamVcState"):
                    self.catmxvcloamvcstate = value
                    self.catmxvcloamvcstate.value_namespace = name_space
                    self.catmxvcloamvcstate.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.atmvclentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.atmvclentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "atmVclTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "ATM-MIB:ATM-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "atmVclEntry"):
                for c in self.atmvclentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = AtmMib.Atmvcltable.Atmvclentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.atmvclentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "atmVclEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Atmvpcrossconnecttable(Entity):
        """
        The ATM VP Cross Connect table for PVCs.
        An entry in this table models two
        cross\-connected VPLs.
        Each VPL must have its atmConnKind set
        to pvc(1).
        
        .. attribute:: atmvpcrossconnectentry
        
        	An entry in the ATM VP Cross Connect table. This entry is used to model a bi\-directional ATM VP cross\-connect which cross\-connects two VPLs.  Step\-wise Procedures to set up a VP Cross\-connect  Once the entries in the atmVplTable are created, the following procedures are used to cross\-connect the VPLs together.  (1) The manager obtains a unique    atmVpCrossConnectIndex by reading the    atmVpCrossConnectIndexNext object.  (2) Next, the manager creates a set of one    or more rows in the ATM VP Cross Connect    Table, one for each cross\-connection between    two VPLs.  Each row is indexed by the ATM    interface port numbers and VPI values of the    two ends of that cross\-connection.    This set of rows specifies the topology of the    VPC cross\-connect and is identified by a single    value of atmVpCrossConnectIndex.  Negotiated VP Cross\-Connect Establishment  (2a) The manager creates a row in this table by    setting atmVpCrossConnectRowStatus to    createAndWait(5).  The agent checks the    requested topology and the mutual sanity of    the ATM traffic parameters and    service categories, i.e., the row creation    fails if\:    \- the requested topology is incompatible with      associated values of atmVplCastType,    \- the requested topology is not supported      by the agent,    \- the traffic/service category parameter values      associated with the requested row are      incompatible with those of already existing      rows for this VP cross\-connect.    [For example, for setting up    a point\-to\-point VP cross\-connect, the    ATM traffic parameters in the receive direction    of a VPL at the low end of the cross\-connect    must equal to the traffic parameters in the    transmit direction of the other VPL at the    high end of the cross\-connect,    otherwise, the row creation fails.]    The agent also checks for internal errors    in building the cross\-connect.     The atmVpCrossConnectIndex values in the    corresponding atmVplTable rows are filled    in by the agent at this point.  (2b) The manager promotes the row in the    atmVpCrossConnectTable by setting    atmVpCrossConnectRowStatus to active(1).  If    this set is successful, the agent has reserved    the resources specified by the ATM traffic    parameter and Service category values    for each direction of the VP cross\-connect    in an ATM switch or network.  (3) The manager sets the    atmVpCrossConnectAdminStatus to up(1) in all    rows of this VP cross\-connect to turn the    traffic flow on.   One\-Shot VP Cross\-Connect Establishment  A VP cross\-connect may also be established in one step by a set\-request with all necessary parameter values and atmVpCrossConnectRowStatus set to createAndGo(4).  In contrast to the negotiated VP cross\-connect establishment which allows for detailed error checking (i.e., set errors are explicitly linked to particular resource acquisition failures), the one\-shot VP cross\-connect establishment performs the setup on one operation but does not have the advantage of step\-wise error checking.  VP Cross\-Connect Retirement  A VP cross\-connect identified by a particular value of atmVpCrossConnectIndex is released by\:  (1) Setting atmVpCrossConnectRowStatus of all    rows identified by this value of    atmVpCrossConnectIndex to destroy(6).    The agent may release all    associated resources, and the    atmVpCrossConnectIndex values in the    corresponding atmVplTable row are removed.    Note that a situation when only a subset of    the associated rows are deleted corresponds    to a VP topology change.  (2) After deletion of the appropriate    atmVpCrossConnectEntries, the manager may    set atmVplRowStatus to destroy(6) the    associated VPLs.  The agent releases    the resources and removes the associated    rows in the atmVplTable.  VP Cross\-connect Reconfiguration  At the discretion of the agent, a VP cross\-connect may be reconfigured by adding and/or deleting leafs to/from the VP topology as per the VP cross\-connect establishment/retirement procedures. Reconfiguration of traffic/service category parameter values requires release of the VP cross\-connect before those parameter values may by changed for individual VPLs
        	**type**\: list of    :py:class:`Atmvpcrossconnectentry <ydk.models.cisco_ios_xe.ATM_MIB.AtmMib.Atmvpcrossconnecttable.Atmvpcrossconnectentry>`
        
        

        """

        _prefix = 'ATM-MIB'
        _revision = '1998-10-19'

        def __init__(self):
            super(AtmMib.Atmvpcrossconnecttable, self).__init__()

            self.yang_name = "atmVpCrossConnectTable"
            self.yang_parent_name = "ATM-MIB"

            self.atmvpcrossconnectentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(AtmMib.Atmvpcrossconnecttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(AtmMib.Atmvpcrossconnecttable, self).__setattr__(name, value)


        class Atmvpcrossconnectentry(Entity):
            """
            An entry in the ATM VP Cross Connect table.
            This entry is used to model a bi\-directional
            ATM VP cross\-connect which cross\-connects
            two VPLs.
            
            Step\-wise Procedures to set up a VP Cross\-connect
            
            Once the entries in the atmVplTable are created,
            the following procedures are used
            to cross\-connect the VPLs together.
            
            (1) The manager obtains a unique
               atmVpCrossConnectIndex by reading the
               atmVpCrossConnectIndexNext object.
            
            (2) Next, the manager creates a set of one
               or more rows in the ATM VP Cross Connect
               Table, one for each cross\-connection between
               two VPLs.  Each row is indexed by the ATM
               interface port numbers and VPI values of the
               two ends of that cross\-connection.
               This set of rows specifies the topology of the
               VPC cross\-connect and is identified by a single
               value of atmVpCrossConnectIndex.
            
            Negotiated VP Cross\-Connect Establishment
            
            (2a) The manager creates a row in this table by
               setting atmVpCrossConnectRowStatus to
               createAndWait(5).  The agent checks the
               requested topology and the mutual sanity of
               the ATM traffic parameters and
               service categories, i.e., the row creation
               fails if\:
               \- the requested topology is incompatible with
                 associated values of atmVplCastType,
               \- the requested topology is not supported
                 by the agent,
               \- the traffic/service category parameter values
                 associated with the requested row are
                 incompatible with those of already existing
                 rows for this VP cross\-connect.
               [For example, for setting up
               a point\-to\-point VP cross\-connect, the
               ATM traffic parameters in the receive direction
               of a VPL at the low end of the cross\-connect
               must equal to the traffic parameters in the
               transmit direction of the other VPL at the
               high end of the cross\-connect,
               otherwise, the row creation fails.]
               The agent also checks for internal errors
               in building the cross\-connect.
            
               The atmVpCrossConnectIndex values in the
               corresponding atmVplTable rows are filled
               in by the agent at this point.
            
            (2b) The manager promotes the row in the
               atmVpCrossConnectTable by setting
               atmVpCrossConnectRowStatus to active(1).  If
               this set is successful, the agent has reserved
               the resources specified by the ATM traffic
               parameter and Service category values
               for each direction of the VP cross\-connect
               in an ATM switch or network.
            
            (3) The manager sets the
               atmVpCrossConnectAdminStatus to up(1) in all
               rows of this VP cross\-connect to turn the
               traffic flow on.
            
            
            One\-Shot VP Cross\-Connect Establishment
            
            A VP cross\-connect may also be established in
            one step by a set\-request with all necessary
            parameter values and atmVpCrossConnectRowStatus
            set to createAndGo(4).
            
            In contrast to the negotiated VP cross\-connect
            establishment which allows for detailed error
            checking (i.e., set errors are explicitly linked
            to particular resource acquisition failures),
            the one\-shot VP cross\-connect establishment
            performs the setup on one operation but does not
            have the advantage of step\-wise error checking.
            
            VP Cross\-Connect Retirement
            
            A VP cross\-connect identified by a particular
            value of atmVpCrossConnectIndex is released by\:
            
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
            
            VP Cross\-connect Reconfiguration
            
            At the discretion of the agent, a VP
            cross\-connect may be reconfigured by
            adding and/or deleting leafs to/from
            the VP topology as per the VP cross\-connect
            establishment/retirement procedures.
            Reconfiguration of traffic/service category parameter
            values requires release of the VP cross\-connect
            before those parameter values may by changed
            for individual VPLs.
            
            .. attribute:: atmvpcrossconnectindex  <key>
            
            	A unique value to identify this VP cross\-connect. For each VPL associated with this cross\-connect, the agent reports this cross\-connect index value in the atmVplCrossConnectIdentifier attribute of the corresponding atmVplTable entries
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: atmvpcrossconnectlowifindex  <key>
            
            	The ifIndex value of the ATM interface for this VP cross\-connect. The term low implies that this ATM interface has the numerically lower ifIndex value than the other ATM interface identified in the same atmVpCrossConnectEntry
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: atmvpcrossconnectlowvpi  <key>
            
            	The VPI value at the ATM interface associated with the VP cross\-connect that is identified by atmVpCrossConnectLowIfIndex
            	**type**\:  int
            
            	**range:** 0..4095
            
            .. attribute:: atmvpcrossconnecthighifindex  <key>
            
            	The ifIndex value of the ATM interface for this VP cross\-connect. The term high implies that this ATM interface has the numerically higher ifIndex value than the  other ATM interface identified in the same atmVpCrossConnectEntry
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: atmvpcrossconnecthighvpi  <key>
            
            	The VPI value at the ATM interface associated with the VP cross\-connect that is identified by atmVpCrossConnectHighIfIndex
            	**type**\:  int
            
            	**range:** 0..4095
            
            .. attribute:: atmvpcrossconnectadminstatus
            
            	The desired administrative status of this bi\-directional VP cross\-connect
            	**type**\:   :py:class:`Atmvorxadminstatus <ydk.models.cisco_ios_xe.ATM_TC_MIB.Atmvorxadminstatus>`
            
            .. attribute:: atmvpcrossconnecth2llastchange
            
            	The value of sysUpTime at the time this VP cross\-connect entered its current operational in the high to low direction
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: atmvpcrossconnecth2loperstatus
            
            	The operational status of the VP cross\-connect in one direction; (i.e., from the high to low direction)
            	**type**\:   :py:class:`Atmvorxoperstatus <ydk.models.cisco_ios_xe.ATM_TC_MIB.Atmvorxoperstatus>`
            
            .. attribute:: atmvpcrossconnectl2hlastchange
            
            	The value of sysUpTime at the time this VP cross\-connect entered its current operational state in the low to high direction
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: atmvpcrossconnectl2hoperstatus
            
            	The operational status of the VP cross\-connect in one direction; (i.e., from the low to high direction)
            	**type**\:   :py:class:`Atmvorxoperstatus <ydk.models.cisco_ios_xe.ATM_TC_MIB.Atmvorxoperstatus>`
            
            .. attribute:: atmvpcrossconnectrowstatus
            
            	The status of this entry in the atmVpCrossConnectTable.  This object is used to create a cross\-connect for cross\-connecting VPLs which are created using the atmVplTable or to change or delete an existing cross\-connect. This object must be initially set to `createAndWait' or 'createAndGo'. To turn on a VP cross\-connect, the atmVpCrossConnectAdminStatus is set to `up'
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            

            """

            _prefix = 'ATM-MIB'
            _revision = '1998-10-19'

            def __init__(self):
                super(AtmMib.Atmvpcrossconnecttable.Atmvpcrossconnectentry, self).__init__()

                self.yang_name = "atmVpCrossConnectEntry"
                self.yang_parent_name = "atmVpCrossConnectTable"

                self.atmvpcrossconnectindex = YLeaf(YType.int32, "atmVpCrossConnectIndex")

                self.atmvpcrossconnectlowifindex = YLeaf(YType.int32, "atmVpCrossConnectLowIfIndex")

                self.atmvpcrossconnectlowvpi = YLeaf(YType.int32, "atmVpCrossConnectLowVpi")

                self.atmvpcrossconnecthighifindex = YLeaf(YType.int32, "atmVpCrossConnectHighIfIndex")

                self.atmvpcrossconnecthighvpi = YLeaf(YType.int32, "atmVpCrossConnectHighVpi")

                self.atmvpcrossconnectadminstatus = YLeaf(YType.enumeration, "atmVpCrossConnectAdminStatus")

                self.atmvpcrossconnecth2llastchange = YLeaf(YType.uint32, "atmVpCrossConnectH2LLastChange")

                self.atmvpcrossconnecth2loperstatus = YLeaf(YType.enumeration, "atmVpCrossConnectH2LOperStatus")

                self.atmvpcrossconnectl2hlastchange = YLeaf(YType.uint32, "atmVpCrossConnectL2HLastChange")

                self.atmvpcrossconnectl2hoperstatus = YLeaf(YType.enumeration, "atmVpCrossConnectL2HOperStatus")

                self.atmvpcrossconnectrowstatus = YLeaf(YType.enumeration, "atmVpCrossConnectRowStatus")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("atmvpcrossconnectindex",
                                "atmvpcrossconnectlowifindex",
                                "atmvpcrossconnectlowvpi",
                                "atmvpcrossconnecthighifindex",
                                "atmvpcrossconnecthighvpi",
                                "atmvpcrossconnectadminstatus",
                                "atmvpcrossconnecth2llastchange",
                                "atmvpcrossconnecth2loperstatus",
                                "atmvpcrossconnectl2hlastchange",
                                "atmvpcrossconnectl2hoperstatus",
                                "atmvpcrossconnectrowstatus") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(AtmMib.Atmvpcrossconnecttable.Atmvpcrossconnectentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(AtmMib.Atmvpcrossconnecttable.Atmvpcrossconnectentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.atmvpcrossconnectindex.is_set or
                    self.atmvpcrossconnectlowifindex.is_set or
                    self.atmvpcrossconnectlowvpi.is_set or
                    self.atmvpcrossconnecthighifindex.is_set or
                    self.atmvpcrossconnecthighvpi.is_set or
                    self.atmvpcrossconnectadminstatus.is_set or
                    self.atmvpcrossconnecth2llastchange.is_set or
                    self.atmvpcrossconnecth2loperstatus.is_set or
                    self.atmvpcrossconnectl2hlastchange.is_set or
                    self.atmvpcrossconnectl2hoperstatus.is_set or
                    self.atmvpcrossconnectrowstatus.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.atmvpcrossconnectindex.yfilter != YFilter.not_set or
                    self.atmvpcrossconnectlowifindex.yfilter != YFilter.not_set or
                    self.atmvpcrossconnectlowvpi.yfilter != YFilter.not_set or
                    self.atmvpcrossconnecthighifindex.yfilter != YFilter.not_set or
                    self.atmvpcrossconnecthighvpi.yfilter != YFilter.not_set or
                    self.atmvpcrossconnectadminstatus.yfilter != YFilter.not_set or
                    self.atmvpcrossconnecth2llastchange.yfilter != YFilter.not_set or
                    self.atmvpcrossconnecth2loperstatus.yfilter != YFilter.not_set or
                    self.atmvpcrossconnectl2hlastchange.yfilter != YFilter.not_set or
                    self.atmvpcrossconnectl2hoperstatus.yfilter != YFilter.not_set or
                    self.atmvpcrossconnectrowstatus.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "atmVpCrossConnectEntry" + "[atmVpCrossConnectIndex='" + self.atmvpcrossconnectindex.get() + "']" + "[atmVpCrossConnectLowIfIndex='" + self.atmvpcrossconnectlowifindex.get() + "']" + "[atmVpCrossConnectLowVpi='" + self.atmvpcrossconnectlowvpi.get() + "']" + "[atmVpCrossConnectHighIfIndex='" + self.atmvpcrossconnecthighifindex.get() + "']" + "[atmVpCrossConnectHighVpi='" + self.atmvpcrossconnecthighvpi.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "ATM-MIB:ATM-MIB/atmVpCrossConnectTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.atmvpcrossconnectindex.is_set or self.atmvpcrossconnectindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvpcrossconnectindex.get_name_leafdata())
                if (self.atmvpcrossconnectlowifindex.is_set or self.atmvpcrossconnectlowifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvpcrossconnectlowifindex.get_name_leafdata())
                if (self.atmvpcrossconnectlowvpi.is_set or self.atmvpcrossconnectlowvpi.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvpcrossconnectlowvpi.get_name_leafdata())
                if (self.atmvpcrossconnecthighifindex.is_set or self.atmvpcrossconnecthighifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvpcrossconnecthighifindex.get_name_leafdata())
                if (self.atmvpcrossconnecthighvpi.is_set or self.atmvpcrossconnecthighvpi.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvpcrossconnecthighvpi.get_name_leafdata())
                if (self.atmvpcrossconnectadminstatus.is_set or self.atmvpcrossconnectadminstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvpcrossconnectadminstatus.get_name_leafdata())
                if (self.atmvpcrossconnecth2llastchange.is_set or self.atmvpcrossconnecth2llastchange.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvpcrossconnecth2llastchange.get_name_leafdata())
                if (self.atmvpcrossconnecth2loperstatus.is_set or self.atmvpcrossconnecth2loperstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvpcrossconnecth2loperstatus.get_name_leafdata())
                if (self.atmvpcrossconnectl2hlastchange.is_set or self.atmvpcrossconnectl2hlastchange.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvpcrossconnectl2hlastchange.get_name_leafdata())
                if (self.atmvpcrossconnectl2hoperstatus.is_set or self.atmvpcrossconnectl2hoperstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvpcrossconnectl2hoperstatus.get_name_leafdata())
                if (self.atmvpcrossconnectrowstatus.is_set or self.atmvpcrossconnectrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvpcrossconnectrowstatus.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "atmVpCrossConnectIndex" or name == "atmVpCrossConnectLowIfIndex" or name == "atmVpCrossConnectLowVpi" or name == "atmVpCrossConnectHighIfIndex" or name == "atmVpCrossConnectHighVpi" or name == "atmVpCrossConnectAdminStatus" or name == "atmVpCrossConnectH2LLastChange" or name == "atmVpCrossConnectH2LOperStatus" or name == "atmVpCrossConnectL2HLastChange" or name == "atmVpCrossConnectL2HOperStatus" or name == "atmVpCrossConnectRowStatus"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "atmVpCrossConnectIndex"):
                    self.atmvpcrossconnectindex = value
                    self.atmvpcrossconnectindex.value_namespace = name_space
                    self.atmvpcrossconnectindex.value_namespace_prefix = name_space_prefix
                if(value_path == "atmVpCrossConnectLowIfIndex"):
                    self.atmvpcrossconnectlowifindex = value
                    self.atmvpcrossconnectlowifindex.value_namespace = name_space
                    self.atmvpcrossconnectlowifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "atmVpCrossConnectLowVpi"):
                    self.atmvpcrossconnectlowvpi = value
                    self.atmvpcrossconnectlowvpi.value_namespace = name_space
                    self.atmvpcrossconnectlowvpi.value_namespace_prefix = name_space_prefix
                if(value_path == "atmVpCrossConnectHighIfIndex"):
                    self.atmvpcrossconnecthighifindex = value
                    self.atmvpcrossconnecthighifindex.value_namespace = name_space
                    self.atmvpcrossconnecthighifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "atmVpCrossConnectHighVpi"):
                    self.atmvpcrossconnecthighvpi = value
                    self.atmvpcrossconnecthighvpi.value_namespace = name_space
                    self.atmvpcrossconnecthighvpi.value_namespace_prefix = name_space_prefix
                if(value_path == "atmVpCrossConnectAdminStatus"):
                    self.atmvpcrossconnectadminstatus = value
                    self.atmvpcrossconnectadminstatus.value_namespace = name_space
                    self.atmvpcrossconnectadminstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "atmVpCrossConnectH2LLastChange"):
                    self.atmvpcrossconnecth2llastchange = value
                    self.atmvpcrossconnecth2llastchange.value_namespace = name_space
                    self.atmvpcrossconnecth2llastchange.value_namespace_prefix = name_space_prefix
                if(value_path == "atmVpCrossConnectH2LOperStatus"):
                    self.atmvpcrossconnecth2loperstatus = value
                    self.atmvpcrossconnecth2loperstatus.value_namespace = name_space
                    self.atmvpcrossconnecth2loperstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "atmVpCrossConnectL2HLastChange"):
                    self.atmvpcrossconnectl2hlastchange = value
                    self.atmvpcrossconnectl2hlastchange.value_namespace = name_space
                    self.atmvpcrossconnectl2hlastchange.value_namespace_prefix = name_space_prefix
                if(value_path == "atmVpCrossConnectL2HOperStatus"):
                    self.atmvpcrossconnectl2hoperstatus = value
                    self.atmvpcrossconnectl2hoperstatus.value_namespace = name_space
                    self.atmvpcrossconnectl2hoperstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "atmVpCrossConnectRowStatus"):
                    self.atmvpcrossconnectrowstatus = value
                    self.atmvpcrossconnectrowstatus.value_namespace = name_space
                    self.atmvpcrossconnectrowstatus.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.atmvpcrossconnectentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.atmvpcrossconnectentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "atmVpCrossConnectTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "ATM-MIB:ATM-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "atmVpCrossConnectEntry"):
                for c in self.atmvpcrossconnectentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = AtmMib.Atmvpcrossconnecttable.Atmvpcrossconnectentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.atmvpcrossconnectentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "atmVpCrossConnectEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Atmvccrossconnecttable(Entity):
        """
        The ATM VC Cross Connect table for PVCs.
        An entry in this table models two
        cross\-connected VCLs.
        Each VCL must have its atmConnKind set
        to pvc(1).
        
        .. attribute:: atmvccrossconnectentry
        
        	An entry in the ATM VC Cross Connect table. This entry is used to model a bi\-directional ATM VC cross\-connect cross\-connecting two end points.  Step\-wise Procedures to set up a VC Cross\-connect  Once the entries in the atmVclTable are created, the following procedures are used to cross\-connect the VCLs together to form a VCC segment.  (1) The manager obtains a unique    atmVcCrossConnectIndex by reading the    atmVcCrossConnectIndexNext object.  (2) Next, the manager creates a set of one    or more rows in the ATM VC Cross Connect    Table, one for each cross\-connection between    two VCLs.  Each row is indexed by the ATM    interface port numbers and VPI/VCI values of    the two ends of that cross\-connection.    This set of rows specifies the topology of the    VCC cross\-connect and is identified by a single    value of atmVcCrossConnectIndex.  Negotiated VC Cross\-Connect Establishment  (2a) The manager creates a row in this table by    setting atmVcCrossConnectRowStatus to    createAndWait(5).  The agent checks the    requested topology and the mutual sanity of    the ATM traffic parameters and    service categories, i.e., the row creation    fails if\:    \- the requested topology is incompatible with      associated values of atmVclCastType,    \- the requested topology is not supported      by the agent,    \- the traffic/service category parameter values      associated with the requested row are      incompatible with those of already existing      rows for this VC cross\-connect.    [For example, for setting up    a point\-to\-point VC cross\-connect, the    ATM traffic parameters in the receive direction    of a VCL at the low end of the cross\-connect    must equal to the traffic parameters in the    transmit direction of the other VCL at the    high end of the cross\-connect,    otherwise, the row creation fails.]    The agent also checks for internal errors    in building the cross\-connect.     The atmVcCrossConnectIndex values in the    corresponding atmVclTable rows are filled    in by the agent at this point.  (2b) The manager promotes the row in the    atmVcCrossConnectTable by setting    atmVcCrossConnectRowStatus to active(1).  If    this set is successful, the agent has reserved    the resources specified by the ATM traffic    parameter and Service category values    for each direction of the VC cross\-connect    in an ATM switch or network.  (3) The manager sets the    atmVcCrossConnectAdminStatus to up(1)    in all rows of this VC cross\-connect to    turn the traffic flow on.   One\-Shot VC Cross\-Connect Establishment  A VC cross\-connect may also be established in one step by a set\-request with all necessary parameter values and atmVcCrossConnectRowStatus set to createAndGo(4).  In contrast to the negotiated VC cross\-connect establishment which allows for detailed error checking i.e., set errors are explicitly linked to particular resource acquisition failures), the one\-shot VC cross\-connect establishment performs the setup on one operation but does not have the advantage of step\-wise error checking.  VC Cross\-Connect Retirement  A VC cross\-connect identified by a particular value of atmVcCrossConnectIndex is released by\:  (1) Setting atmVcCrossConnectRowStatus of all rows    identified by this value of    atmVcCrossConnectIndex to destroy(6).    The agent may release all    associated resources, and the    atmVcCrossConnectIndex values in the    corresponding atmVclTable row are removed.    Note that a situation when only a subset of    the associated rows are deleted corresponds    to a VC topology change.  (2) After deletion of the appropriate    atmVcCrossConnectEntries, the manager may    set atmVclRowStatus to destroy(6) the    associated VCLs.  The agent releases    the resources and removes the associated    rows in the atmVclTable.  VC Cross\-Connect Reconfiguration  At the discretion of the agent, a VC cross\-connect may be reconfigured by adding and/or deleting leafs to/from the VC topology as per the VC cross\-connect establishment/retirement procedures. Reconfiguration of traffic/service category parameter values requires release of the VC cross\-connect before those parameter values may by changed for individual VCLs
        	**type**\: list of    :py:class:`Atmvccrossconnectentry <ydk.models.cisco_ios_xe.ATM_MIB.AtmMib.Atmvccrossconnecttable.Atmvccrossconnectentry>`
        
        

        """

        _prefix = 'ATM-MIB'
        _revision = '1998-10-19'

        def __init__(self):
            super(AtmMib.Atmvccrossconnecttable, self).__init__()

            self.yang_name = "atmVcCrossConnectTable"
            self.yang_parent_name = "ATM-MIB"

            self.atmvccrossconnectentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(AtmMib.Atmvccrossconnecttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(AtmMib.Atmvccrossconnecttable, self).__setattr__(name, value)


        class Atmvccrossconnectentry(Entity):
            """
            An entry in the ATM VC Cross Connect table.
            This entry is used to model a bi\-directional ATM
            VC cross\-connect cross\-connecting two end points.
            
            Step\-wise Procedures to set up a VC Cross\-connect
            
            Once the entries in the atmVclTable are created,
            the following procedures are used
            to cross\-connect the VCLs together to
            form a VCC segment.
            
            (1) The manager obtains a unique
               atmVcCrossConnectIndex by reading the
               atmVcCrossConnectIndexNext object.
            
            (2) Next, the manager creates a set of one
               or more rows in the ATM VC Cross Connect
               Table, one for each cross\-connection between
               two VCLs.  Each row is indexed by the ATM
               interface port numbers and VPI/VCI values of
               the two ends of that cross\-connection.
               This set of rows specifies the topology of the
               VCC cross\-connect and is identified by a single
               value of atmVcCrossConnectIndex.
            
            Negotiated VC Cross\-Connect Establishment
            
            (2a) The manager creates a row in this table by
               setting atmVcCrossConnectRowStatus to
               createAndWait(5).  The agent checks the
               requested topology and the mutual sanity of
               the ATM traffic parameters and
               service categories, i.e., the row creation
               fails if\:
               \- the requested topology is incompatible with
                 associated values of atmVclCastType,
               \- the requested topology is not supported
                 by the agent,
               \- the traffic/service category parameter values
                 associated with the requested row are
                 incompatible with those of already existing
                 rows for this VC cross\-connect.
               [For example, for setting up
               a point\-to\-point VC cross\-connect, the
               ATM traffic parameters in the receive direction
               of a VCL at the low end of the cross\-connect
               must equal to the traffic parameters in the
               transmit direction of the other VCL at the
               high end of the cross\-connect,
               otherwise, the row creation fails.]
               The agent also checks for internal errors
               in building the cross\-connect.
            
               The atmVcCrossConnectIndex values in the
               corresponding atmVclTable rows are filled
               in by the agent at this point.
            
            (2b) The manager promotes the row in the
               atmVcCrossConnectTable by setting
               atmVcCrossConnectRowStatus to active(1).  If
               this set is successful, the agent has reserved
               the resources specified by the ATM traffic
               parameter and Service category values
               for each direction of the VC cross\-connect
               in an ATM switch or network.
            
            (3) The manager sets the
               atmVcCrossConnectAdminStatus to up(1)
               in all rows of this VC cross\-connect to
               turn the traffic flow on.
            
            
            One\-Shot VC Cross\-Connect Establishment
            
            A VC cross\-connect may also be established in
            one step by a set\-request with all necessary
            parameter values and atmVcCrossConnectRowStatus
            set to createAndGo(4).
            
            In contrast to the negotiated VC cross\-connect
            establishment which allows for detailed error
            checking i.e., set errors are explicitly linked to
            particular resource acquisition failures), the
            one\-shot VC cross\-connect establishment
            performs the setup on one operation but does
            not have the advantage of step\-wise error
            checking.
            
            VC Cross\-Connect Retirement
            
            A VC cross\-connect identified by a particular
            value of atmVcCrossConnectIndex is released by\:
            
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
            
            VC Cross\-Connect Reconfiguration
            
            At the discretion of the agent, a VC
            cross\-connect may be reconfigured by
            adding and/or deleting leafs to/from
            the VC topology as per the VC cross\-connect
            establishment/retirement procedures.
            Reconfiguration of traffic/service category parameter
            values requires release of the VC cross\-connect
            before those parameter values may by changed
            for individual VCLs.
            
            .. attribute:: atmvccrossconnectindex  <key>
            
            	A unique value to identify this VC cross\-connect. For each VCL associated with this cross\-connect, the agent reports this cross\-connect index value in the atmVclCrossConnectIdentifier attribute of the corresponding atmVclTable entries
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: atmvccrossconnectlowifindex  <key>
            
            	The ifIndex value of the ATM interface for this VC cross\-connect. The term low implies that this ATM interface has the numerically lower ifIndex value than the other ATM interface identified in the same atmVcCrossConnectEntry
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: atmvccrossconnectlowvpi  <key>
            
            	The VPI value at the ATM interface associated with the VC cross\-connect that is identified by atmVcCrossConnectLowIfIndex
            	**type**\:  int
            
            	**range:** 0..4095
            
            .. attribute:: atmvccrossconnectlowvci  <key>
            
            	The VCI value at the ATM interface associated with this VC cross\-connect that is identified by atmVcCrossConnectLowIfIndex
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: atmvccrossconnecthighifindex  <key>
            
            	The ifIndex value for the ATM interface for this VC cross\-connect. The term high implies that this ATM interface has the numerically higher ifIndex value than the other ATM interface identified in the same atmVcCrossConnectEntry
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: atmvccrossconnecthighvpi  <key>
            
            	The VPI value at the ATM interface associated with the VC cross\-connect that is identified by atmVcCrossConnectHighIfIndex
            	**type**\:  int
            
            	**range:** 0..4095
            
            .. attribute:: atmvccrossconnecthighvci  <key>
            
            	The VCI value at the ATM interface associated with the VC cross\-connect that is identified by atmVcCrossConnectHighIfIndex
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: atmvccrossconnectadminstatus
            
            	The desired administrative status of this bi\-directional VC cross\-connect
            	**type**\:   :py:class:`Atmvorxadminstatus <ydk.models.cisco_ios_xe.ATM_TC_MIB.Atmvorxadminstatus>`
            
            .. attribute:: atmvccrossconnecth2llastchange
            
            	The value of sysUpTime at the time this VC cross\-connect entered its current operational state in high to low direction
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: atmvccrossconnecth2loperstatus
            
            	The current operational status of the VC cross\-connect in one direction; (i.e., from the high to low direction)
            	**type**\:   :py:class:`Atmvorxoperstatus <ydk.models.cisco_ios_xe.ATM_TC_MIB.Atmvorxoperstatus>`
            
            .. attribute:: atmvccrossconnectl2hlastchange
            
            	The value of sysUpTime at the time this VC cross\-connect entered its current operational state in low to high direction
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: atmvccrossconnectl2hoperstatus
            
            	The current operational status of the VC cross\-connect in one direction; (i.e., from the low to high direction)
            	**type**\:   :py:class:`Atmvorxoperstatus <ydk.models.cisco_ios_xe.ATM_TC_MIB.Atmvorxoperstatus>`
            
            .. attribute:: atmvccrossconnectrowstatus
            
            	The status of this entry in the atmVcCrossConnectTable.  This object is used to create a new cross\-connect for cross\-connecting VCLs which are created using the atmVclTable or to change or delete existing cross\-connect. This object must be initially set to `createAndWait' or 'createAndGo'. To turn on a VC cross\-connect, the atmVcCrossConnectAdminStatus is set to `up'
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            

            """

            _prefix = 'ATM-MIB'
            _revision = '1998-10-19'

            def __init__(self):
                super(AtmMib.Atmvccrossconnecttable.Atmvccrossconnectentry, self).__init__()

                self.yang_name = "atmVcCrossConnectEntry"
                self.yang_parent_name = "atmVcCrossConnectTable"

                self.atmvccrossconnectindex = YLeaf(YType.int32, "atmVcCrossConnectIndex")

                self.atmvccrossconnectlowifindex = YLeaf(YType.int32, "atmVcCrossConnectLowIfIndex")

                self.atmvccrossconnectlowvpi = YLeaf(YType.int32, "atmVcCrossConnectLowVpi")

                self.atmvccrossconnectlowvci = YLeaf(YType.int32, "atmVcCrossConnectLowVci")

                self.atmvccrossconnecthighifindex = YLeaf(YType.int32, "atmVcCrossConnectHighIfIndex")

                self.atmvccrossconnecthighvpi = YLeaf(YType.int32, "atmVcCrossConnectHighVpi")

                self.atmvccrossconnecthighvci = YLeaf(YType.int32, "atmVcCrossConnectHighVci")

                self.atmvccrossconnectadminstatus = YLeaf(YType.enumeration, "atmVcCrossConnectAdminStatus")

                self.atmvccrossconnecth2llastchange = YLeaf(YType.uint32, "atmVcCrossConnectH2LLastChange")

                self.atmvccrossconnecth2loperstatus = YLeaf(YType.enumeration, "atmVcCrossConnectH2LOperStatus")

                self.atmvccrossconnectl2hlastchange = YLeaf(YType.uint32, "atmVcCrossConnectL2HLastChange")

                self.atmvccrossconnectl2hoperstatus = YLeaf(YType.enumeration, "atmVcCrossConnectL2HOperStatus")

                self.atmvccrossconnectrowstatus = YLeaf(YType.enumeration, "atmVcCrossConnectRowStatus")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("atmvccrossconnectindex",
                                "atmvccrossconnectlowifindex",
                                "atmvccrossconnectlowvpi",
                                "atmvccrossconnectlowvci",
                                "atmvccrossconnecthighifindex",
                                "atmvccrossconnecthighvpi",
                                "atmvccrossconnecthighvci",
                                "atmvccrossconnectadminstatus",
                                "atmvccrossconnecth2llastchange",
                                "atmvccrossconnecth2loperstatus",
                                "atmvccrossconnectl2hlastchange",
                                "atmvccrossconnectl2hoperstatus",
                                "atmvccrossconnectrowstatus") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(AtmMib.Atmvccrossconnecttable.Atmvccrossconnectentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(AtmMib.Atmvccrossconnecttable.Atmvccrossconnectentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.atmvccrossconnectindex.is_set or
                    self.atmvccrossconnectlowifindex.is_set or
                    self.atmvccrossconnectlowvpi.is_set or
                    self.atmvccrossconnectlowvci.is_set or
                    self.atmvccrossconnecthighifindex.is_set or
                    self.atmvccrossconnecthighvpi.is_set or
                    self.atmvccrossconnecthighvci.is_set or
                    self.atmvccrossconnectadminstatus.is_set or
                    self.atmvccrossconnecth2llastchange.is_set or
                    self.atmvccrossconnecth2loperstatus.is_set or
                    self.atmvccrossconnectl2hlastchange.is_set or
                    self.atmvccrossconnectl2hoperstatus.is_set or
                    self.atmvccrossconnectrowstatus.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.atmvccrossconnectindex.yfilter != YFilter.not_set or
                    self.atmvccrossconnectlowifindex.yfilter != YFilter.not_set or
                    self.atmvccrossconnectlowvpi.yfilter != YFilter.not_set or
                    self.atmvccrossconnectlowvci.yfilter != YFilter.not_set or
                    self.atmvccrossconnecthighifindex.yfilter != YFilter.not_set or
                    self.atmvccrossconnecthighvpi.yfilter != YFilter.not_set or
                    self.atmvccrossconnecthighvci.yfilter != YFilter.not_set or
                    self.atmvccrossconnectadminstatus.yfilter != YFilter.not_set or
                    self.atmvccrossconnecth2llastchange.yfilter != YFilter.not_set or
                    self.atmvccrossconnecth2loperstatus.yfilter != YFilter.not_set or
                    self.atmvccrossconnectl2hlastchange.yfilter != YFilter.not_set or
                    self.atmvccrossconnectl2hoperstatus.yfilter != YFilter.not_set or
                    self.atmvccrossconnectrowstatus.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "atmVcCrossConnectEntry" + "[atmVcCrossConnectIndex='" + self.atmvccrossconnectindex.get() + "']" + "[atmVcCrossConnectLowIfIndex='" + self.atmvccrossconnectlowifindex.get() + "']" + "[atmVcCrossConnectLowVpi='" + self.atmvccrossconnectlowvpi.get() + "']" + "[atmVcCrossConnectLowVci='" + self.atmvccrossconnectlowvci.get() + "']" + "[atmVcCrossConnectHighIfIndex='" + self.atmvccrossconnecthighifindex.get() + "']" + "[atmVcCrossConnectHighVpi='" + self.atmvccrossconnecthighvpi.get() + "']" + "[atmVcCrossConnectHighVci='" + self.atmvccrossconnecthighvci.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "ATM-MIB:ATM-MIB/atmVcCrossConnectTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.atmvccrossconnectindex.is_set or self.atmvccrossconnectindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvccrossconnectindex.get_name_leafdata())
                if (self.atmvccrossconnectlowifindex.is_set or self.atmvccrossconnectlowifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvccrossconnectlowifindex.get_name_leafdata())
                if (self.atmvccrossconnectlowvpi.is_set or self.atmvccrossconnectlowvpi.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvccrossconnectlowvpi.get_name_leafdata())
                if (self.atmvccrossconnectlowvci.is_set or self.atmvccrossconnectlowvci.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvccrossconnectlowvci.get_name_leafdata())
                if (self.atmvccrossconnecthighifindex.is_set or self.atmvccrossconnecthighifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvccrossconnecthighifindex.get_name_leafdata())
                if (self.atmvccrossconnecthighvpi.is_set or self.atmvccrossconnecthighvpi.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvccrossconnecthighvpi.get_name_leafdata())
                if (self.atmvccrossconnecthighvci.is_set or self.atmvccrossconnecthighvci.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvccrossconnecthighvci.get_name_leafdata())
                if (self.atmvccrossconnectadminstatus.is_set or self.atmvccrossconnectadminstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvccrossconnectadminstatus.get_name_leafdata())
                if (self.atmvccrossconnecth2llastchange.is_set or self.atmvccrossconnecth2llastchange.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvccrossconnecth2llastchange.get_name_leafdata())
                if (self.atmvccrossconnecth2loperstatus.is_set or self.atmvccrossconnecth2loperstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvccrossconnecth2loperstatus.get_name_leafdata())
                if (self.atmvccrossconnectl2hlastchange.is_set or self.atmvccrossconnectl2hlastchange.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvccrossconnectl2hlastchange.get_name_leafdata())
                if (self.atmvccrossconnectl2hoperstatus.is_set or self.atmvccrossconnectl2hoperstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvccrossconnectl2hoperstatus.get_name_leafdata())
                if (self.atmvccrossconnectrowstatus.is_set or self.atmvccrossconnectrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvccrossconnectrowstatus.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "atmVcCrossConnectIndex" or name == "atmVcCrossConnectLowIfIndex" or name == "atmVcCrossConnectLowVpi" or name == "atmVcCrossConnectLowVci" or name == "atmVcCrossConnectHighIfIndex" or name == "atmVcCrossConnectHighVpi" or name == "atmVcCrossConnectHighVci" or name == "atmVcCrossConnectAdminStatus" or name == "atmVcCrossConnectH2LLastChange" or name == "atmVcCrossConnectH2LOperStatus" or name == "atmVcCrossConnectL2HLastChange" or name == "atmVcCrossConnectL2HOperStatus" or name == "atmVcCrossConnectRowStatus"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "atmVcCrossConnectIndex"):
                    self.atmvccrossconnectindex = value
                    self.atmvccrossconnectindex.value_namespace = name_space
                    self.atmvccrossconnectindex.value_namespace_prefix = name_space_prefix
                if(value_path == "atmVcCrossConnectLowIfIndex"):
                    self.atmvccrossconnectlowifindex = value
                    self.atmvccrossconnectlowifindex.value_namespace = name_space
                    self.atmvccrossconnectlowifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "atmVcCrossConnectLowVpi"):
                    self.atmvccrossconnectlowvpi = value
                    self.atmvccrossconnectlowvpi.value_namespace = name_space
                    self.atmvccrossconnectlowvpi.value_namespace_prefix = name_space_prefix
                if(value_path == "atmVcCrossConnectLowVci"):
                    self.atmvccrossconnectlowvci = value
                    self.atmvccrossconnectlowvci.value_namespace = name_space
                    self.atmvccrossconnectlowvci.value_namespace_prefix = name_space_prefix
                if(value_path == "atmVcCrossConnectHighIfIndex"):
                    self.atmvccrossconnecthighifindex = value
                    self.atmvccrossconnecthighifindex.value_namespace = name_space
                    self.atmvccrossconnecthighifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "atmVcCrossConnectHighVpi"):
                    self.atmvccrossconnecthighvpi = value
                    self.atmvccrossconnecthighvpi.value_namespace = name_space
                    self.atmvccrossconnecthighvpi.value_namespace_prefix = name_space_prefix
                if(value_path == "atmVcCrossConnectHighVci"):
                    self.atmvccrossconnecthighvci = value
                    self.atmvccrossconnecthighvci.value_namespace = name_space
                    self.atmvccrossconnecthighvci.value_namespace_prefix = name_space_prefix
                if(value_path == "atmVcCrossConnectAdminStatus"):
                    self.atmvccrossconnectadminstatus = value
                    self.atmvccrossconnectadminstatus.value_namespace = name_space
                    self.atmvccrossconnectadminstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "atmVcCrossConnectH2LLastChange"):
                    self.atmvccrossconnecth2llastchange = value
                    self.atmvccrossconnecth2llastchange.value_namespace = name_space
                    self.atmvccrossconnecth2llastchange.value_namespace_prefix = name_space_prefix
                if(value_path == "atmVcCrossConnectH2LOperStatus"):
                    self.atmvccrossconnecth2loperstatus = value
                    self.atmvccrossconnecth2loperstatus.value_namespace = name_space
                    self.atmvccrossconnecth2loperstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "atmVcCrossConnectL2HLastChange"):
                    self.atmvccrossconnectl2hlastchange = value
                    self.atmvccrossconnectl2hlastchange.value_namespace = name_space
                    self.atmvccrossconnectl2hlastchange.value_namespace_prefix = name_space_prefix
                if(value_path == "atmVcCrossConnectL2HOperStatus"):
                    self.atmvccrossconnectl2hoperstatus = value
                    self.atmvccrossconnectl2hoperstatus.value_namespace = name_space
                    self.atmvccrossconnectl2hoperstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "atmVcCrossConnectRowStatus"):
                    self.atmvccrossconnectrowstatus = value
                    self.atmvccrossconnectrowstatus.value_namespace = name_space
                    self.atmvccrossconnectrowstatus.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.atmvccrossconnectentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.atmvccrossconnectentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "atmVcCrossConnectTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "ATM-MIB:ATM-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "atmVcCrossConnectEntry"):
                for c in self.atmvccrossconnectentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = AtmMib.Atmvccrossconnecttable.Atmvccrossconnectentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.atmvccrossconnectentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "atmVcCrossConnectEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Aal5Vcctable(Entity):
        """
        This table contains AAL5 VCC performance
        parameters.
        
        .. attribute:: aal5vccentry
        
        	This list contains the AAL5 VCC performance parameters and is indexed by ifIndex values of AAL5 interfaces and the associated VPI/VCI values
        	**type**\: list of    :py:class:`Aal5Vccentry <ydk.models.cisco_ios_xe.ATM_MIB.AtmMib.Aal5Vcctable.Aal5Vccentry>`
        
        

        """

        _prefix = 'ATM-MIB'
        _revision = '1998-10-19'

        def __init__(self):
            super(AtmMib.Aal5Vcctable, self).__init__()

            self.yang_name = "aal5VccTable"
            self.yang_parent_name = "ATM-MIB"

            self.aal5vccentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(AtmMib.Aal5Vcctable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(AtmMib.Aal5Vcctable, self).__setattr__(name, value)


        class Aal5Vccentry(Entity):
            """
            This list contains the AAL5 VCC
            performance parameters and is indexed
            by ifIndex values of AAL5 interfaces
            and the associated VPI/VCI values.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: aal5vccvpi  <key>
            
            	The VPI value of the AAL5 VCC at the interface identified by the ifIndex
            	**type**\:  int
            
            	**range:** 0..4095
            
            .. attribute:: aal5vccvci  <key>
            
            	The VCI value of the AAL5 VCC at the interface identified by the ifIndex
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: aal5vcccrcerrors
            
            	The number of AAL5 CPCS PDUs received with CRC\-32 errors on this AAL5 VCC at the interface associated with an AAL5 entity
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: aal5vccoversizedsdus
            
            	The number of AAL5 CPCS PDUs discarded on this AAL5 VCC at the interface associated with an AAL5 entity because the AAL5 SDUs were too large
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: aal5vccsartimeouts
            
            	The number of partially re\-assembled AAL5 CPCS PDUs which were discarded on this AAL5 VCC at the interface associated with an AAL5 entity because they were not fully re\-assembled within the required time period.  If the re\-assembly timer is not supported, then this object contains a zero value
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: caal5vccextcompenabled
            
            	Boolean, if compression enabled for VCC
            	**type**\:  bool
            
            .. attribute:: caal5vccextinf5oamcells
            
            	Number of OAM F5 end to end loopback cells  received through the VCC
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: caal5vccextoutf5oamcells
            
            	Number of OAM F5 end to end loopback cells sent  through the VCC
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: caal5vccextvoice
            
            	Boolean, TRUE if VCC is used to carry voice
            	**type**\:  bool
            
            .. attribute:: caal5vcchcinoctets
            
            	This is 64bit (High Capacity) version of cAal5VccInOctets  counters
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: caal5vcchcinpkts
            
            	This is 64bit (High Capacity) version of cAal5VccInPkts  counters
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: caal5vcchcoutoctets
            
            	This is 64bit (High Capacity) version of cAal5VccOutOctets  counters
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: caal5vcchcoutpkts
            
            	This is 64bit (High Capacity) version of cAal5VccOutPkts  counters
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: caal5vccindroppedoctets
            
            	The number of AAL5 CPCS PDU Octets dropped at the  receive side of this AAL5 VCC at the interface  associated with an AAL5 entity
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: octets
            
            .. attribute:: caal5vccindroppedpkts
            
            	The number of AAL5 CPCS PDUs dropped at the  receive side of this AAL5 VCC at the interface  associated with an AAL5 entity
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: caal5vccinoctets
            
            	The number of AAL5 CPCS PDU octets received on this AAL5 VCC at the interface associated with an AAL5 entity
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: octets
            
            .. attribute:: caal5vccinpkts
            
            	The number of AAL5 CPCS PDUs received on this AAL5 VCC at the interface associated with an AAL5 entity
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: caal5vccoutdroppedoctets
            
            	The number of AAL5 CPCS PDU Octets dropped at the  transmit side of this AAL5 VCC at the interface  associated with an AAL5 entity
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: octets
            
            .. attribute:: caal5vccoutdroppedpkts
            
            	The number of AAL5 CPCS PDUs dropped at the transmit side  of this AAL5 VCC at the interface associated with an  AAL5 entity
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: caal5vccoutoctets
            
            	The number of AAL5 CPCS PDU octets transmitted on this AAL5  VCC at the interface associated with an AAL5 entity
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: octets
            
            .. attribute:: caal5vccoutpkts
            
            	The number of AAL5 CPCS PDUs transmitted on this AAL5 VCC at the interface associated with an AAL5 entity
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            

            """

            _prefix = 'ATM-MIB'
            _revision = '1998-10-19'

            def __init__(self):
                super(AtmMib.Aal5Vcctable.Aal5Vccentry, self).__init__()

                self.yang_name = "aal5VccEntry"
                self.yang_parent_name = "aal5VccTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.aal5vccvpi = YLeaf(YType.int32, "aal5VccVpi")

                self.aal5vccvci = YLeaf(YType.int32, "aal5VccVci")

                self.aal5vcccrcerrors = YLeaf(YType.uint32, "aal5VccCrcErrors")

                self.aal5vccoversizedsdus = YLeaf(YType.uint32, "aal5VccOverSizedSDUs")

                self.aal5vccsartimeouts = YLeaf(YType.uint32, "aal5VccSarTimeOuts")

                self.caal5vccextcompenabled = YLeaf(YType.boolean, "CISCO-ATM-EXT-MIB:cAal5VccExtCompEnabled")

                self.caal5vccextinf5oamcells = YLeaf(YType.uint32, "CISCO-ATM-EXT-MIB:cAal5VccExtInF5OamCells")

                self.caal5vccextoutf5oamcells = YLeaf(YType.uint32, "CISCO-ATM-EXT-MIB:cAal5VccExtOutF5OamCells")

                self.caal5vccextvoice = YLeaf(YType.boolean, "CISCO-ATM-EXT-MIB:cAal5VccExtVoice")

                self.caal5vcchcinoctets = YLeaf(YType.uint64, "CISCO-AAL5-MIB:cAal5VccHCInOctets")

                self.caal5vcchcinpkts = YLeaf(YType.uint64, "CISCO-AAL5-MIB:cAal5VccHCInPkts")

                self.caal5vcchcoutoctets = YLeaf(YType.uint64, "CISCO-AAL5-MIB:cAal5VccHCOutOctets")

                self.caal5vcchcoutpkts = YLeaf(YType.uint64, "CISCO-AAL5-MIB:cAal5VccHCOutPkts")

                self.caal5vccindroppedoctets = YLeaf(YType.uint32, "CISCO-AAL5-MIB:cAal5VccInDroppedOctets")

                self.caal5vccindroppedpkts = YLeaf(YType.uint32, "CISCO-AAL5-MIB:cAal5VccInDroppedPkts")

                self.caal5vccinoctets = YLeaf(YType.uint32, "CISCO-AAL5-MIB:cAal5VccInOctets")

                self.caal5vccinpkts = YLeaf(YType.uint32, "CISCO-AAL5-MIB:cAal5VccInPkts")

                self.caal5vccoutdroppedoctets = YLeaf(YType.uint32, "CISCO-AAL5-MIB:cAal5VccOutDroppedOctets")

                self.caal5vccoutdroppedpkts = YLeaf(YType.uint32, "CISCO-AAL5-MIB:cAal5VccOutDroppedPkts")

                self.caal5vccoutoctets = YLeaf(YType.uint32, "CISCO-AAL5-MIB:cAal5VccOutOctets")

                self.caal5vccoutpkts = YLeaf(YType.uint32, "CISCO-AAL5-MIB:cAal5VccOutPkts")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ifindex",
                                "aal5vccvpi",
                                "aal5vccvci",
                                "aal5vcccrcerrors",
                                "aal5vccoversizedsdus",
                                "aal5vccsartimeouts",
                                "caal5vccextcompenabled",
                                "caal5vccextinf5oamcells",
                                "caal5vccextoutf5oamcells",
                                "caal5vccextvoice",
                                "caal5vcchcinoctets",
                                "caal5vcchcinpkts",
                                "caal5vcchcoutoctets",
                                "caal5vcchcoutpkts",
                                "caal5vccindroppedoctets",
                                "caal5vccindroppedpkts",
                                "caal5vccinoctets",
                                "caal5vccinpkts",
                                "caal5vccoutdroppedoctets",
                                "caal5vccoutdroppedpkts",
                                "caal5vccoutoctets",
                                "caal5vccoutpkts") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(AtmMib.Aal5Vcctable.Aal5Vccentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(AtmMib.Aal5Vcctable.Aal5Vccentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.aal5vccvpi.is_set or
                    self.aal5vccvci.is_set or
                    self.aal5vcccrcerrors.is_set or
                    self.aal5vccoversizedsdus.is_set or
                    self.aal5vccsartimeouts.is_set or
                    self.caal5vccextcompenabled.is_set or
                    self.caal5vccextinf5oamcells.is_set or
                    self.caal5vccextoutf5oamcells.is_set or
                    self.caal5vccextvoice.is_set or
                    self.caal5vcchcinoctets.is_set or
                    self.caal5vcchcinpkts.is_set or
                    self.caal5vcchcoutoctets.is_set or
                    self.caal5vcchcoutpkts.is_set or
                    self.caal5vccindroppedoctets.is_set or
                    self.caal5vccindroppedpkts.is_set or
                    self.caal5vccinoctets.is_set or
                    self.caal5vccinpkts.is_set or
                    self.caal5vccoutdroppedoctets.is_set or
                    self.caal5vccoutdroppedpkts.is_set or
                    self.caal5vccoutoctets.is_set or
                    self.caal5vccoutpkts.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.aal5vccvpi.yfilter != YFilter.not_set or
                    self.aal5vccvci.yfilter != YFilter.not_set or
                    self.aal5vcccrcerrors.yfilter != YFilter.not_set or
                    self.aal5vccoversizedsdus.yfilter != YFilter.not_set or
                    self.aal5vccsartimeouts.yfilter != YFilter.not_set or
                    self.caal5vccextcompenabled.yfilter != YFilter.not_set or
                    self.caal5vccextinf5oamcells.yfilter != YFilter.not_set or
                    self.caal5vccextoutf5oamcells.yfilter != YFilter.not_set or
                    self.caal5vccextvoice.yfilter != YFilter.not_set or
                    self.caal5vcchcinoctets.yfilter != YFilter.not_set or
                    self.caal5vcchcinpkts.yfilter != YFilter.not_set or
                    self.caal5vcchcoutoctets.yfilter != YFilter.not_set or
                    self.caal5vcchcoutpkts.yfilter != YFilter.not_set or
                    self.caal5vccindroppedoctets.yfilter != YFilter.not_set or
                    self.caal5vccindroppedpkts.yfilter != YFilter.not_set or
                    self.caal5vccinoctets.yfilter != YFilter.not_set or
                    self.caal5vccinpkts.yfilter != YFilter.not_set or
                    self.caal5vccoutdroppedoctets.yfilter != YFilter.not_set or
                    self.caal5vccoutdroppedpkts.yfilter != YFilter.not_set or
                    self.caal5vccoutoctets.yfilter != YFilter.not_set or
                    self.caal5vccoutpkts.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "aal5VccEntry" + "[ifIndex='" + self.ifindex.get() + "']" + "[aal5VccVpi='" + self.aal5vccvpi.get() + "']" + "[aal5VccVci='" + self.aal5vccvci.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "ATM-MIB:ATM-MIB/aal5VccTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.aal5vccvpi.is_set or self.aal5vccvpi.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.aal5vccvpi.get_name_leafdata())
                if (self.aal5vccvci.is_set or self.aal5vccvci.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.aal5vccvci.get_name_leafdata())
                if (self.aal5vcccrcerrors.is_set or self.aal5vcccrcerrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.aal5vcccrcerrors.get_name_leafdata())
                if (self.aal5vccoversizedsdus.is_set or self.aal5vccoversizedsdus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.aal5vccoversizedsdus.get_name_leafdata())
                if (self.aal5vccsartimeouts.is_set or self.aal5vccsartimeouts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.aal5vccsartimeouts.get_name_leafdata())
                if (self.caal5vccextcompenabled.is_set or self.caal5vccextcompenabled.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.caal5vccextcompenabled.get_name_leafdata())
                if (self.caal5vccextinf5oamcells.is_set or self.caal5vccextinf5oamcells.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.caal5vccextinf5oamcells.get_name_leafdata())
                if (self.caal5vccextoutf5oamcells.is_set or self.caal5vccextoutf5oamcells.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.caal5vccextoutf5oamcells.get_name_leafdata())
                if (self.caal5vccextvoice.is_set or self.caal5vccextvoice.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.caal5vccextvoice.get_name_leafdata())
                if (self.caal5vcchcinoctets.is_set or self.caal5vcchcinoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.caal5vcchcinoctets.get_name_leafdata())
                if (self.caal5vcchcinpkts.is_set or self.caal5vcchcinpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.caal5vcchcinpkts.get_name_leafdata())
                if (self.caal5vcchcoutoctets.is_set or self.caal5vcchcoutoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.caal5vcchcoutoctets.get_name_leafdata())
                if (self.caal5vcchcoutpkts.is_set or self.caal5vcchcoutpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.caal5vcchcoutpkts.get_name_leafdata())
                if (self.caal5vccindroppedoctets.is_set or self.caal5vccindroppedoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.caal5vccindroppedoctets.get_name_leafdata())
                if (self.caal5vccindroppedpkts.is_set or self.caal5vccindroppedpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.caal5vccindroppedpkts.get_name_leafdata())
                if (self.caal5vccinoctets.is_set or self.caal5vccinoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.caal5vccinoctets.get_name_leafdata())
                if (self.caal5vccinpkts.is_set or self.caal5vccinpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.caal5vccinpkts.get_name_leafdata())
                if (self.caal5vccoutdroppedoctets.is_set or self.caal5vccoutdroppedoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.caal5vccoutdroppedoctets.get_name_leafdata())
                if (self.caal5vccoutdroppedpkts.is_set or self.caal5vccoutdroppedpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.caal5vccoutdroppedpkts.get_name_leafdata())
                if (self.caal5vccoutoctets.is_set or self.caal5vccoutoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.caal5vccoutoctets.get_name_leafdata())
                if (self.caal5vccoutpkts.is_set or self.caal5vccoutpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.caal5vccoutpkts.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "aal5VccVpi" or name == "aal5VccVci" or name == "aal5VccCrcErrors" or name == "aal5VccOverSizedSDUs" or name == "aal5VccSarTimeOuts" or name == "cAal5VccExtCompEnabled" or name == "cAal5VccExtInF5OamCells" or name == "cAal5VccExtOutF5OamCells" or name == "cAal5VccExtVoice" or name == "cAal5VccHCInOctets" or name == "cAal5VccHCInPkts" or name == "cAal5VccHCOutOctets" or name == "cAal5VccHCOutPkts" or name == "cAal5VccInDroppedOctets" or name == "cAal5VccInDroppedPkts" or name == "cAal5VccInOctets" or name == "cAal5VccInPkts" or name == "cAal5VccOutDroppedOctets" or name == "cAal5VccOutDroppedPkts" or name == "cAal5VccOutOctets" or name == "cAal5VccOutPkts"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "aal5VccVpi"):
                    self.aal5vccvpi = value
                    self.aal5vccvpi.value_namespace = name_space
                    self.aal5vccvpi.value_namespace_prefix = name_space_prefix
                if(value_path == "aal5VccVci"):
                    self.aal5vccvci = value
                    self.aal5vccvci.value_namespace = name_space
                    self.aal5vccvci.value_namespace_prefix = name_space_prefix
                if(value_path == "aal5VccCrcErrors"):
                    self.aal5vcccrcerrors = value
                    self.aal5vcccrcerrors.value_namespace = name_space
                    self.aal5vcccrcerrors.value_namespace_prefix = name_space_prefix
                if(value_path == "aal5VccOverSizedSDUs"):
                    self.aal5vccoversizedsdus = value
                    self.aal5vccoversizedsdus.value_namespace = name_space
                    self.aal5vccoversizedsdus.value_namespace_prefix = name_space_prefix
                if(value_path == "aal5VccSarTimeOuts"):
                    self.aal5vccsartimeouts = value
                    self.aal5vccsartimeouts.value_namespace = name_space
                    self.aal5vccsartimeouts.value_namespace_prefix = name_space_prefix
                if(value_path == "cAal5VccExtCompEnabled"):
                    self.caal5vccextcompenabled = value
                    self.caal5vccextcompenabled.value_namespace = name_space
                    self.caal5vccextcompenabled.value_namespace_prefix = name_space_prefix
                if(value_path == "cAal5VccExtInF5OamCells"):
                    self.caal5vccextinf5oamcells = value
                    self.caal5vccextinf5oamcells.value_namespace = name_space
                    self.caal5vccextinf5oamcells.value_namespace_prefix = name_space_prefix
                if(value_path == "cAal5VccExtOutF5OamCells"):
                    self.caal5vccextoutf5oamcells = value
                    self.caal5vccextoutf5oamcells.value_namespace = name_space
                    self.caal5vccextoutf5oamcells.value_namespace_prefix = name_space_prefix
                if(value_path == "cAal5VccExtVoice"):
                    self.caal5vccextvoice = value
                    self.caal5vccextvoice.value_namespace = name_space
                    self.caal5vccextvoice.value_namespace_prefix = name_space_prefix
                if(value_path == "cAal5VccHCInOctets"):
                    self.caal5vcchcinoctets = value
                    self.caal5vcchcinoctets.value_namespace = name_space
                    self.caal5vcchcinoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "cAal5VccHCInPkts"):
                    self.caal5vcchcinpkts = value
                    self.caal5vcchcinpkts.value_namespace = name_space
                    self.caal5vcchcinpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "cAal5VccHCOutOctets"):
                    self.caal5vcchcoutoctets = value
                    self.caal5vcchcoutoctets.value_namespace = name_space
                    self.caal5vcchcoutoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "cAal5VccHCOutPkts"):
                    self.caal5vcchcoutpkts = value
                    self.caal5vcchcoutpkts.value_namespace = name_space
                    self.caal5vcchcoutpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "cAal5VccInDroppedOctets"):
                    self.caal5vccindroppedoctets = value
                    self.caal5vccindroppedoctets.value_namespace = name_space
                    self.caal5vccindroppedoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "cAal5VccInDroppedPkts"):
                    self.caal5vccindroppedpkts = value
                    self.caal5vccindroppedpkts.value_namespace = name_space
                    self.caal5vccindroppedpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "cAal5VccInOctets"):
                    self.caal5vccinoctets = value
                    self.caal5vccinoctets.value_namespace = name_space
                    self.caal5vccinoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "cAal5VccInPkts"):
                    self.caal5vccinpkts = value
                    self.caal5vccinpkts.value_namespace = name_space
                    self.caal5vccinpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "cAal5VccOutDroppedOctets"):
                    self.caal5vccoutdroppedoctets = value
                    self.caal5vccoutdroppedoctets.value_namespace = name_space
                    self.caal5vccoutdroppedoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "cAal5VccOutDroppedPkts"):
                    self.caal5vccoutdroppedpkts = value
                    self.caal5vccoutdroppedpkts.value_namespace = name_space
                    self.caal5vccoutdroppedpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "cAal5VccOutOctets"):
                    self.caal5vccoutoctets = value
                    self.caal5vccoutoctets.value_namespace = name_space
                    self.caal5vccoutoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "cAal5VccOutPkts"):
                    self.caal5vccoutpkts = value
                    self.caal5vccoutpkts.value_namespace = name_space
                    self.caal5vccoutpkts.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.aal5vccentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.aal5vccentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "aal5VccTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "ATM-MIB:ATM-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "aal5VccEntry"):
                for c in self.aal5vccentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = AtmMib.Aal5Vcctable.Aal5Vccentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.aal5vccentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "aal5VccEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.aal5vcctable is not None and self.aal5vcctable.has_data()) or
            (self.atminterfaceconftable is not None and self.atminterfaceconftable.has_data()) or
            (self.atminterfaceds3plcptable is not None and self.atminterfaceds3plcptable.has_data()) or
            (self.atminterfacetctable is not None and self.atminterfacetctable.has_data()) or
            (self.atmmibobjects is not None and self.atmmibobjects.has_data()) or
            (self.atmtrafficdescrparamtable is not None and self.atmtrafficdescrparamtable.has_data()) or
            (self.atmvccrossconnecttable is not None and self.atmvccrossconnecttable.has_data()) or
            (self.atmvcltable is not None and self.atmvcltable.has_data()) or
            (self.atmvpcrossconnecttable is not None and self.atmvpcrossconnecttable.has_data()) or
            (self.atmvpltable is not None and self.atmvpltable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.aal5vcctable is not None and self.aal5vcctable.has_operation()) or
            (self.atminterfaceconftable is not None and self.atminterfaceconftable.has_operation()) or
            (self.atminterfaceds3plcptable is not None and self.atminterfaceds3plcptable.has_operation()) or
            (self.atminterfacetctable is not None and self.atminterfacetctable.has_operation()) or
            (self.atmmibobjects is not None and self.atmmibobjects.has_operation()) or
            (self.atmtrafficdescrparamtable is not None and self.atmtrafficdescrparamtable.has_operation()) or
            (self.atmvccrossconnecttable is not None and self.atmvccrossconnecttable.has_operation()) or
            (self.atmvcltable is not None and self.atmvcltable.has_operation()) or
            (self.atmvpcrossconnecttable is not None and self.atmvpcrossconnecttable.has_operation()) or
            (self.atmvpltable is not None and self.atmvpltable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "ATM-MIB:ATM-MIB" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "aal5VccTable"):
            if (self.aal5vcctable is None):
                self.aal5vcctable = AtmMib.Aal5Vcctable()
                self.aal5vcctable.parent = self
                self._children_name_map["aal5vcctable"] = "aal5VccTable"
            return self.aal5vcctable

        if (child_yang_name == "atmInterfaceConfTable"):
            if (self.atminterfaceconftable is None):
                self.atminterfaceconftable = AtmMib.Atminterfaceconftable()
                self.atminterfaceconftable.parent = self
                self._children_name_map["atminterfaceconftable"] = "atmInterfaceConfTable"
            return self.atminterfaceconftable

        if (child_yang_name == "atmInterfaceDs3PlcpTable"):
            if (self.atminterfaceds3plcptable is None):
                self.atminterfaceds3plcptable = AtmMib.Atminterfaceds3Plcptable()
                self.atminterfaceds3plcptable.parent = self
                self._children_name_map["atminterfaceds3plcptable"] = "atmInterfaceDs3PlcpTable"
            return self.atminterfaceds3plcptable

        if (child_yang_name == "atmInterfaceTCTable"):
            if (self.atminterfacetctable is None):
                self.atminterfacetctable = AtmMib.Atminterfacetctable()
                self.atminterfacetctable.parent = self
                self._children_name_map["atminterfacetctable"] = "atmInterfaceTCTable"
            return self.atminterfacetctable

        if (child_yang_name == "atmMIBObjects"):
            if (self.atmmibobjects is None):
                self.atmmibobjects = AtmMib.Atmmibobjects()
                self.atmmibobjects.parent = self
                self._children_name_map["atmmibobjects"] = "atmMIBObjects"
            return self.atmmibobjects

        if (child_yang_name == "atmTrafficDescrParamTable"):
            if (self.atmtrafficdescrparamtable is None):
                self.atmtrafficdescrparamtable = AtmMib.Atmtrafficdescrparamtable()
                self.atmtrafficdescrparamtable.parent = self
                self._children_name_map["atmtrafficdescrparamtable"] = "atmTrafficDescrParamTable"
            return self.atmtrafficdescrparamtable

        if (child_yang_name == "atmVcCrossConnectTable"):
            if (self.atmvccrossconnecttable is None):
                self.atmvccrossconnecttable = AtmMib.Atmvccrossconnecttable()
                self.atmvccrossconnecttable.parent = self
                self._children_name_map["atmvccrossconnecttable"] = "atmVcCrossConnectTable"
            return self.atmvccrossconnecttable

        if (child_yang_name == "atmVclTable"):
            if (self.atmvcltable is None):
                self.atmvcltable = AtmMib.Atmvcltable()
                self.atmvcltable.parent = self
                self._children_name_map["atmvcltable"] = "atmVclTable"
            return self.atmvcltable

        if (child_yang_name == "atmVpCrossConnectTable"):
            if (self.atmvpcrossconnecttable is None):
                self.atmvpcrossconnecttable = AtmMib.Atmvpcrossconnecttable()
                self.atmvpcrossconnecttable.parent = self
                self._children_name_map["atmvpcrossconnecttable"] = "atmVpCrossConnectTable"
            return self.atmvpcrossconnecttable

        if (child_yang_name == "atmVplTable"):
            if (self.atmvpltable is None):
                self.atmvpltable = AtmMib.Atmvpltable()
                self.atmvpltable.parent = self
                self._children_name_map["atmvpltable"] = "atmVplTable"
            return self.atmvpltable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "aal5VccTable" or name == "atmInterfaceConfTable" or name == "atmInterfaceDs3PlcpTable" or name == "atmInterfaceTCTable" or name == "atmMIBObjects" or name == "atmTrafficDescrParamTable" or name == "atmVcCrossConnectTable" or name == "atmVclTable" or name == "atmVpCrossConnectTable" or name == "atmVplTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = AtmMib()
        return self._top_entity

