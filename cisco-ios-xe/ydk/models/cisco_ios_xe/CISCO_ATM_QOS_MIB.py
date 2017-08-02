""" CISCO_ATM_QOS_MIB 

The MIB is created to provide ATM QoS information in
these areas\:

1. Traffic shaping on a per\-VC basis
2. Traffic shaping on a per\-VP basis 
3. Per\-VC queuing/buffering

Although the initial requirements of the MIB are
driven to support the GSR TAZ line card,
CISCO\-ATM\-QOS\-MIB is designed as a generic MIB to
support ATM interfaces across all platforms.

Here are the tables defined in this MIB\:
ciscoAtmQosVccTable 
     \- to provide information on traffic shaping on 
       a per\-VC basis.
                      
ciscoAtmQosVpcTable 
     \- to provide information on traffic shaping on
       a per\-VP basis.
    
ciscoAtmQosVcQueuingTable
ciscoAtmQosVcQueuingClassTable
     \- to provide information on per\-VC
       queuing/buffering.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Vcparamconfiglocation(Enum):
    """
    Vcparamconfiglocation

    The configuration source of a vc parameter\:

    1 \- Not configured \- using default

    2 \- Configured on vc directly

    3 \- VC\-class configured on vc

    4 \- VC\-class configured on sub\-interface

    5 \- VC\-class configured on main\-interface.

    .. data:: configDefault = 1

    .. data:: configVcDirect = 2

    .. data:: configVcClass = 3

    .. data:: configVcClassSubInterface = 4

    .. data:: configVcClassInterface = 5

    """

    configDefault = Enum.YLeaf(1, "configDefault")

    configVcDirect = Enum.YLeaf(2, "configVcDirect")

    configVcClass = Enum.YLeaf(3, "configVcClass")

    configVcClassSubInterface = Enum.YLeaf(4, "configVcClassSubInterface")

    configVcClassInterface = Enum.YLeaf(5, "configVcClassInterface")


class Vpstate(Enum):
    """
    Vpstate

    States of virtual path\:

    1 \- Inactive

    2 \- Active

    .. data:: vpStateInactive = 1

    .. data:: vpStateActive = 2

    """

    vpStateInactive = Enum.YLeaf(1, "vpStateInactive")

    vpStateActive = Enum.YLeaf(2, "vpStateActive")



class CiscoAtmQosMib(Entity):
    """
    
    
    .. attribute:: caqqueuingparamsclasstable
    
    	This table provides queuing information for all  queuing classes associating with a VC
    	**type**\:   :py:class:`Caqqueuingparamsclasstable <ydk.models.cisco_ios_xe.CISCO_ATM_QOS_MIB.CiscoAtmQosMib.Caqqueuingparamsclasstable>`
    
    .. attribute:: caqqueuingparamstable
    
    	This table provides queuing related information for a VC existing on an ATM interface
    	**type**\:   :py:class:`Caqqueuingparamstable <ydk.models.cisco_ios_xe.CISCO_ATM_QOS_MIB.CiscoAtmQosMib.Caqqueuingparamstable>`
    
    .. attribute:: caqvccparamstable
    
    	This table is defined to provide QoS information for each active ATM VC existing on the interface
    	**type**\:   :py:class:`Caqvccparamstable <ydk.models.cisco_ios_xe.CISCO_ATM_QOS_MIB.CiscoAtmQosMib.Caqvccparamstable>`
    
    .. attribute:: caqvpcparamstable
    
    	This table is defined to provide QoS information for each active ATM VP existing on the interface
    	**type**\:   :py:class:`Caqvpcparamstable <ydk.models.cisco_ios_xe.CISCO_ATM_QOS_MIB.CiscoAtmQosMib.Caqvpcparamstable>`
    
    

    """

    _prefix = 'CISCO-ATM-QOS-MIB'
    _revision = '2002-06-10'

    def __init__(self):
        super(CiscoAtmQosMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-ATM-QOS-MIB"
        self.yang_parent_name = "CISCO-ATM-QOS-MIB"

        self.caqqueuingparamsclasstable = CiscoAtmQosMib.Caqqueuingparamsclasstable()
        self.caqqueuingparamsclasstable.parent = self
        self._children_name_map["caqqueuingparamsclasstable"] = "caqQueuingParamsClassTable"
        self._children_yang_names.add("caqQueuingParamsClassTable")

        self.caqqueuingparamstable = CiscoAtmQosMib.Caqqueuingparamstable()
        self.caqqueuingparamstable.parent = self
        self._children_name_map["caqqueuingparamstable"] = "caqQueuingParamsTable"
        self._children_yang_names.add("caqQueuingParamsTable")

        self.caqvccparamstable = CiscoAtmQosMib.Caqvccparamstable()
        self.caqvccparamstable.parent = self
        self._children_name_map["caqvccparamstable"] = "caqVccParamsTable"
        self._children_yang_names.add("caqVccParamsTable")

        self.caqvpcparamstable = CiscoAtmQosMib.Caqvpcparamstable()
        self.caqvpcparamstable.parent = self
        self._children_name_map["caqvpcparamstable"] = "caqVpcParamsTable"
        self._children_yang_names.add("caqVpcParamsTable")


    class Caqvccparamstable(Entity):
        """
        This table is defined to provide QoS information for
        each active ATM VC existing on the interface.
        
        .. attribute:: caqvccparamsentry
        
        	This list contains the ATM QoS parameters provided by ciscoAtmQosVccEntry
        	**type**\: list of    :py:class:`Caqvccparamsentry <ydk.models.cisco_ios_xe.CISCO_ATM_QOS_MIB.CiscoAtmQosMib.Caqvccparamstable.Caqvccparamsentry>`
        
        

        """

        _prefix = 'CISCO-ATM-QOS-MIB'
        _revision = '2002-06-10'

        def __init__(self):
            super(CiscoAtmQosMib.Caqvccparamstable, self).__init__()

            self.yang_name = "caqVccParamsTable"
            self.yang_parent_name = "CISCO-ATM-QOS-MIB"

            self.caqvccparamsentry = YList(self)

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
                        super(CiscoAtmQosMib.Caqvccparamstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoAtmQosMib.Caqvccparamstable, self).__setattr__(name, value)


        class Caqvccparamsentry(Entity):
            """
            This list contains the ATM QoS parameters provided by
            ciscoAtmQosVccEntry.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: atmvclvpi  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4095
            
            	**refers to**\:  :py:class:`atmvclvpi <ydk.models.cisco_ios_xe.ATM_MIB.AtmMib.Atmvcltable.Atmvclentry>`
            
            .. attribute:: atmvclvci  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..65535
            
            	**refers to**\:  :py:class:`atmvclvci <ydk.models.cisco_ios_xe.ATM_MIB.AtmMib.Atmvcltable.Atmvclentry>`
            
            .. attribute:: caqvccparamsadtf
            
            	Allowed cell rate decrease time factor
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: caqvccparamsbcsin0
            
            	Input Burst Cell Size (BCS) for connection with VBR type of QoS and Cell Loss Priority bit set to 0 (clp0)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: caqvccparamsbcsin01
            
            	Input Burst Cell Size (BCS) for connection with VBR type of QoS and Cell Loss Priority bit set to 1 (clp01)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: caqvccparamsbcsout0
            
            	Output Burst Cell Size (BCS) for connection with VBR type of QoS and  Cell Loss Priority bit set to 0 (clp0)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: caqvccparamsbcsout01
            
            	Output Burst Cell Size (BCS) for connection with VBR type of QoS and Cell Loss Priority bit set to 1 (clp01)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: caqvccparamscdv
            
            	Cell delay variation
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: caqvccparamscdvt
            
            	Cell delay variation tolerance
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: caqvccparamsfrtt
            
            	Fixed round\-trip time
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: caqvccparamsicr
            
            	Initial cell rate
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: caqvccparamsinheritlevel
            
            	The source of configuration for peak cell rate
            	**type**\:   :py:class:`Vcparamconfiglocation <ydk.models.cisco_ios_xe.CISCO_ATM_QOS_MIB.Vcparamconfiglocation>`
            
            .. attribute:: caqvccparamsinvcdf
            
            	Inverse of cutoff decrease factor
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: caqvccparamsinvrdf
            
            	Inverse of rate decrease factor
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: caqvccparamsinvrif
            
            	Inverse of rate increase factor
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: caqvccparamsinvtrm
            
            	Maximum time between forward rm cells
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: caqvccparamsmcrin
            
            	Input Minimum Cell Rate (MCR) in kbps for connection with VBR\-nrt or ABR type of QoS
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: caqvccparamsmcrout
            
            	Output Minimum Cell Rate (MCR) in kbps for connection with VBR\-nrt or ABR type of QoS
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: caqvccparamsnrm
            
            	Maximum number of tx cells for each forward rm cell
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: caqvccparamspcrin0
            
            	Input Peak Cell Rate (PCR) in kbps with  Cell Loss Priority bit set to 0 (clp0)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: caqvccparamspcrin01
            
            	Number of OAM F5 end to end loopback cells sent through the VCC
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: caqvccparamspcrout0
            
            	Output Peak Cell Rate (PCR) in kbps with Cell Loss Priority bit set to 0 (clp0)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: caqvccparamspcrout01
            
            	Output Peak Cell Rate (PCR) in kbps with Cell Loss Priority bit set to 1 (clp01)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: caqvccparamsrfl
            
            	The source of configuration for rate factor
            	**type**\:   :py:class:`Vcparamconfiglocation <ydk.models.cisco_ios_xe.CISCO_ATM_QOS_MIB.Vcparamconfiglocation>`
            
            .. attribute:: caqvccparamsscrin0
            
            	Input Sustained Cell Rate (SCR) in kbps for connection with VBR type of QoS and Cell Loss Priority bit set to 0 (clp0)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: caqvccparamsscrin01
            
            	Input Sustained Cell Rate (SCR) in kbps for connection with VBR type of QoS and Cell Loss Priority bit set to 1 (clp01)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: caqvccparamsscrout0
            
            	Output Sustained Cell Rate (SCR) in kbps for connection with VBR type of QoS and Cell Loss Priority bit set to 0 (clp0)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: caqvccparamsscrout01
            
            	Output Sustained Cell Rate (SCR) in kbps for connection with VBR type of QoS and Cell Loss Priority bit set to 1 (clp01)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: caqvccparamstbe
            
            	Transient buffer exposure
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: caqvccparamstype
            
            	The service category of this virtual circuit connection
            	**type**\:   :py:class:`Atmservicecategory <ydk.models.cisco_ios_xe.ATM_FORUM_TC_MIB.Atmservicecategory>`
            
            

            """

            _prefix = 'CISCO-ATM-QOS-MIB'
            _revision = '2002-06-10'

            def __init__(self):
                super(CiscoAtmQosMib.Caqvccparamstable.Caqvccparamsentry, self).__init__()

                self.yang_name = "caqVccParamsEntry"
                self.yang_parent_name = "caqVccParamsTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.atmvclvpi = YLeaf(YType.str, "atmVclVpi")

                self.atmvclvci = YLeaf(YType.str, "atmVclVci")

                self.caqvccparamsadtf = YLeaf(YType.uint32, "caqVccParamsAdtf")

                self.caqvccparamsbcsin0 = YLeaf(YType.uint32, "caqVccParamsBcsIn0")

                self.caqvccparamsbcsin01 = YLeaf(YType.uint32, "caqVccParamsBcsIn01")

                self.caqvccparamsbcsout0 = YLeaf(YType.uint32, "caqVccParamsBcsOut0")

                self.caqvccparamsbcsout01 = YLeaf(YType.uint32, "caqVccParamsBcsOut01")

                self.caqvccparamscdv = YLeaf(YType.uint32, "caqVccParamsCdv")

                self.caqvccparamscdvt = YLeaf(YType.uint32, "caqVccParamsCdvt")

                self.caqvccparamsfrtt = YLeaf(YType.uint32, "caqVccParamsFrtt")

                self.caqvccparamsicr = YLeaf(YType.uint32, "caqVccParamsIcr")

                self.caqvccparamsinheritlevel = YLeaf(YType.enumeration, "caqVccParamsInheritLevel")

                self.caqvccparamsinvcdf = YLeaf(YType.uint32, "caqVccParamsInvCdf")

                self.caqvccparamsinvrdf = YLeaf(YType.uint32, "caqVccParamsInvRdf")

                self.caqvccparamsinvrif = YLeaf(YType.uint32, "caqVccParamsInvRif")

                self.caqvccparamsinvtrm = YLeaf(YType.uint32, "caqVccParamsInvTrm")

                self.caqvccparamsmcrin = YLeaf(YType.uint32, "caqVccParamsMcrIn")

                self.caqvccparamsmcrout = YLeaf(YType.uint32, "caqVccParamsMcrOut")

                self.caqvccparamsnrm = YLeaf(YType.uint32, "caqVccParamsNrm")

                self.caqvccparamspcrin0 = YLeaf(YType.uint32, "caqVccParamsPcrIn0")

                self.caqvccparamspcrin01 = YLeaf(YType.uint32, "caqVccParamsPcrIn01")

                self.caqvccparamspcrout0 = YLeaf(YType.uint32, "caqVccParamsPcrOut0")

                self.caqvccparamspcrout01 = YLeaf(YType.uint32, "caqVccParamsPcrOut01")

                self.caqvccparamsrfl = YLeaf(YType.enumeration, "caqVccParamsRfl")

                self.caqvccparamsscrin0 = YLeaf(YType.uint32, "caqVccParamsScrIn0")

                self.caqvccparamsscrin01 = YLeaf(YType.uint32, "caqVccParamsScrIn01")

                self.caqvccparamsscrout0 = YLeaf(YType.uint32, "caqVccParamsScrOut0")

                self.caqvccparamsscrout01 = YLeaf(YType.uint32, "caqVccParamsScrOut01")

                self.caqvccparamstbe = YLeaf(YType.uint32, "caqVccParamsTbe")

                self.caqvccparamstype = YLeaf(YType.enumeration, "caqVccParamsType")

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
                                "caqvccparamsadtf",
                                "caqvccparamsbcsin0",
                                "caqvccparamsbcsin01",
                                "caqvccparamsbcsout0",
                                "caqvccparamsbcsout01",
                                "caqvccparamscdv",
                                "caqvccparamscdvt",
                                "caqvccparamsfrtt",
                                "caqvccparamsicr",
                                "caqvccparamsinheritlevel",
                                "caqvccparamsinvcdf",
                                "caqvccparamsinvrdf",
                                "caqvccparamsinvrif",
                                "caqvccparamsinvtrm",
                                "caqvccparamsmcrin",
                                "caqvccparamsmcrout",
                                "caqvccparamsnrm",
                                "caqvccparamspcrin0",
                                "caqvccparamspcrin01",
                                "caqvccparamspcrout0",
                                "caqvccparamspcrout01",
                                "caqvccparamsrfl",
                                "caqvccparamsscrin0",
                                "caqvccparamsscrin01",
                                "caqvccparamsscrout0",
                                "caqvccparamsscrout01",
                                "caqvccparamstbe",
                                "caqvccparamstype") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoAtmQosMib.Caqvccparamstable.Caqvccparamsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoAtmQosMib.Caqvccparamstable.Caqvccparamsentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.atmvclvpi.is_set or
                    self.atmvclvci.is_set or
                    self.caqvccparamsadtf.is_set or
                    self.caqvccparamsbcsin0.is_set or
                    self.caqvccparamsbcsin01.is_set or
                    self.caqvccparamsbcsout0.is_set or
                    self.caqvccparamsbcsout01.is_set or
                    self.caqvccparamscdv.is_set or
                    self.caqvccparamscdvt.is_set or
                    self.caqvccparamsfrtt.is_set or
                    self.caqvccparamsicr.is_set or
                    self.caqvccparamsinheritlevel.is_set or
                    self.caqvccparamsinvcdf.is_set or
                    self.caqvccparamsinvrdf.is_set or
                    self.caqvccparamsinvrif.is_set or
                    self.caqvccparamsinvtrm.is_set or
                    self.caqvccparamsmcrin.is_set or
                    self.caqvccparamsmcrout.is_set or
                    self.caqvccparamsnrm.is_set or
                    self.caqvccparamspcrin0.is_set or
                    self.caqvccparamspcrin01.is_set or
                    self.caqvccparamspcrout0.is_set or
                    self.caqvccparamspcrout01.is_set or
                    self.caqvccparamsrfl.is_set or
                    self.caqvccparamsscrin0.is_set or
                    self.caqvccparamsscrin01.is_set or
                    self.caqvccparamsscrout0.is_set or
                    self.caqvccparamsscrout01.is_set or
                    self.caqvccparamstbe.is_set or
                    self.caqvccparamstype.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.atmvclvpi.yfilter != YFilter.not_set or
                    self.atmvclvci.yfilter != YFilter.not_set or
                    self.caqvccparamsadtf.yfilter != YFilter.not_set or
                    self.caqvccparamsbcsin0.yfilter != YFilter.not_set or
                    self.caqvccparamsbcsin01.yfilter != YFilter.not_set or
                    self.caqvccparamsbcsout0.yfilter != YFilter.not_set or
                    self.caqvccparamsbcsout01.yfilter != YFilter.not_set or
                    self.caqvccparamscdv.yfilter != YFilter.not_set or
                    self.caqvccparamscdvt.yfilter != YFilter.not_set or
                    self.caqvccparamsfrtt.yfilter != YFilter.not_set or
                    self.caqvccparamsicr.yfilter != YFilter.not_set or
                    self.caqvccparamsinheritlevel.yfilter != YFilter.not_set or
                    self.caqvccparamsinvcdf.yfilter != YFilter.not_set or
                    self.caqvccparamsinvrdf.yfilter != YFilter.not_set or
                    self.caqvccparamsinvrif.yfilter != YFilter.not_set or
                    self.caqvccparamsinvtrm.yfilter != YFilter.not_set or
                    self.caqvccparamsmcrin.yfilter != YFilter.not_set or
                    self.caqvccparamsmcrout.yfilter != YFilter.not_set or
                    self.caqvccparamsnrm.yfilter != YFilter.not_set or
                    self.caqvccparamspcrin0.yfilter != YFilter.not_set or
                    self.caqvccparamspcrin01.yfilter != YFilter.not_set or
                    self.caqvccparamspcrout0.yfilter != YFilter.not_set or
                    self.caqvccparamspcrout01.yfilter != YFilter.not_set or
                    self.caqvccparamsrfl.yfilter != YFilter.not_set or
                    self.caqvccparamsscrin0.yfilter != YFilter.not_set or
                    self.caqvccparamsscrin01.yfilter != YFilter.not_set or
                    self.caqvccparamsscrout0.yfilter != YFilter.not_set or
                    self.caqvccparamsscrout01.yfilter != YFilter.not_set or
                    self.caqvccparamstbe.yfilter != YFilter.not_set or
                    self.caqvccparamstype.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "caqVccParamsEntry" + "[ifIndex='" + self.ifindex.get() + "']" + "[atmVclVpi='" + self.atmvclvpi.get() + "']" + "[atmVclVci='" + self.atmvclvci.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-ATM-QOS-MIB:CISCO-ATM-QOS-MIB/caqVccParamsTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.atmvclvpi.is_set or self.atmvclvpi.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvclvpi.get_name_leafdata())
                if (self.atmvclvci.is_set or self.atmvclvci.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvclvci.get_name_leafdata())
                if (self.caqvccparamsadtf.is_set or self.caqvccparamsadtf.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.caqvccparamsadtf.get_name_leafdata())
                if (self.caqvccparamsbcsin0.is_set or self.caqvccparamsbcsin0.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.caqvccparamsbcsin0.get_name_leafdata())
                if (self.caqvccparamsbcsin01.is_set or self.caqvccparamsbcsin01.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.caqvccparamsbcsin01.get_name_leafdata())
                if (self.caqvccparamsbcsout0.is_set or self.caqvccparamsbcsout0.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.caqvccparamsbcsout0.get_name_leafdata())
                if (self.caqvccparamsbcsout01.is_set or self.caqvccparamsbcsout01.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.caqvccparamsbcsout01.get_name_leafdata())
                if (self.caqvccparamscdv.is_set or self.caqvccparamscdv.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.caqvccparamscdv.get_name_leafdata())
                if (self.caqvccparamscdvt.is_set or self.caqvccparamscdvt.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.caqvccparamscdvt.get_name_leafdata())
                if (self.caqvccparamsfrtt.is_set or self.caqvccparamsfrtt.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.caqvccparamsfrtt.get_name_leafdata())
                if (self.caqvccparamsicr.is_set or self.caqvccparamsicr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.caqvccparamsicr.get_name_leafdata())
                if (self.caqvccparamsinheritlevel.is_set or self.caqvccparamsinheritlevel.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.caqvccparamsinheritlevel.get_name_leafdata())
                if (self.caqvccparamsinvcdf.is_set or self.caqvccparamsinvcdf.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.caqvccparamsinvcdf.get_name_leafdata())
                if (self.caqvccparamsinvrdf.is_set or self.caqvccparamsinvrdf.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.caqvccparamsinvrdf.get_name_leafdata())
                if (self.caqvccparamsinvrif.is_set or self.caqvccparamsinvrif.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.caqvccparamsinvrif.get_name_leafdata())
                if (self.caqvccparamsinvtrm.is_set or self.caqvccparamsinvtrm.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.caqvccparamsinvtrm.get_name_leafdata())
                if (self.caqvccparamsmcrin.is_set or self.caqvccparamsmcrin.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.caqvccparamsmcrin.get_name_leafdata())
                if (self.caqvccparamsmcrout.is_set or self.caqvccparamsmcrout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.caqvccparamsmcrout.get_name_leafdata())
                if (self.caqvccparamsnrm.is_set or self.caqvccparamsnrm.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.caqvccparamsnrm.get_name_leafdata())
                if (self.caqvccparamspcrin0.is_set or self.caqvccparamspcrin0.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.caqvccparamspcrin0.get_name_leafdata())
                if (self.caqvccparamspcrin01.is_set or self.caqvccparamspcrin01.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.caqvccparamspcrin01.get_name_leafdata())
                if (self.caqvccparamspcrout0.is_set or self.caqvccparamspcrout0.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.caqvccparamspcrout0.get_name_leafdata())
                if (self.caqvccparamspcrout01.is_set or self.caqvccparamspcrout01.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.caqvccparamspcrout01.get_name_leafdata())
                if (self.caqvccparamsrfl.is_set or self.caqvccparamsrfl.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.caqvccparamsrfl.get_name_leafdata())
                if (self.caqvccparamsscrin0.is_set or self.caqvccparamsscrin0.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.caqvccparamsscrin0.get_name_leafdata())
                if (self.caqvccparamsscrin01.is_set or self.caqvccparamsscrin01.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.caqvccparamsscrin01.get_name_leafdata())
                if (self.caqvccparamsscrout0.is_set or self.caqvccparamsscrout0.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.caqvccparamsscrout0.get_name_leafdata())
                if (self.caqvccparamsscrout01.is_set or self.caqvccparamsscrout01.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.caqvccparamsscrout01.get_name_leafdata())
                if (self.caqvccparamstbe.is_set or self.caqvccparamstbe.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.caqvccparamstbe.get_name_leafdata())
                if (self.caqvccparamstype.is_set or self.caqvccparamstype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.caqvccparamstype.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "atmVclVpi" or name == "atmVclVci" or name == "caqVccParamsAdtf" or name == "caqVccParamsBcsIn0" or name == "caqVccParamsBcsIn01" or name == "caqVccParamsBcsOut0" or name == "caqVccParamsBcsOut01" or name == "caqVccParamsCdv" or name == "caqVccParamsCdvt" or name == "caqVccParamsFrtt" or name == "caqVccParamsIcr" or name == "caqVccParamsInheritLevel" or name == "caqVccParamsInvCdf" or name == "caqVccParamsInvRdf" or name == "caqVccParamsInvRif" or name == "caqVccParamsInvTrm" or name == "caqVccParamsMcrIn" or name == "caqVccParamsMcrOut" or name == "caqVccParamsNrm" or name == "caqVccParamsPcrIn0" or name == "caqVccParamsPcrIn01" or name == "caqVccParamsPcrOut0" or name == "caqVccParamsPcrOut01" or name == "caqVccParamsRfl" or name == "caqVccParamsScrIn0" or name == "caqVccParamsScrIn01" or name == "caqVccParamsScrOut0" or name == "caqVccParamsScrOut01" or name == "caqVccParamsTbe" or name == "caqVccParamsType"):
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
                if(value_path == "caqVccParamsAdtf"):
                    self.caqvccparamsadtf = value
                    self.caqvccparamsadtf.value_namespace = name_space
                    self.caqvccparamsadtf.value_namespace_prefix = name_space_prefix
                if(value_path == "caqVccParamsBcsIn0"):
                    self.caqvccparamsbcsin0 = value
                    self.caqvccparamsbcsin0.value_namespace = name_space
                    self.caqvccparamsbcsin0.value_namespace_prefix = name_space_prefix
                if(value_path == "caqVccParamsBcsIn01"):
                    self.caqvccparamsbcsin01 = value
                    self.caqvccparamsbcsin01.value_namespace = name_space
                    self.caqvccparamsbcsin01.value_namespace_prefix = name_space_prefix
                if(value_path == "caqVccParamsBcsOut0"):
                    self.caqvccparamsbcsout0 = value
                    self.caqvccparamsbcsout0.value_namespace = name_space
                    self.caqvccparamsbcsout0.value_namespace_prefix = name_space_prefix
                if(value_path == "caqVccParamsBcsOut01"):
                    self.caqvccparamsbcsout01 = value
                    self.caqvccparamsbcsout01.value_namespace = name_space
                    self.caqvccparamsbcsout01.value_namespace_prefix = name_space_prefix
                if(value_path == "caqVccParamsCdv"):
                    self.caqvccparamscdv = value
                    self.caqvccparamscdv.value_namespace = name_space
                    self.caqvccparamscdv.value_namespace_prefix = name_space_prefix
                if(value_path == "caqVccParamsCdvt"):
                    self.caqvccparamscdvt = value
                    self.caqvccparamscdvt.value_namespace = name_space
                    self.caqvccparamscdvt.value_namespace_prefix = name_space_prefix
                if(value_path == "caqVccParamsFrtt"):
                    self.caqvccparamsfrtt = value
                    self.caqvccparamsfrtt.value_namespace = name_space
                    self.caqvccparamsfrtt.value_namespace_prefix = name_space_prefix
                if(value_path == "caqVccParamsIcr"):
                    self.caqvccparamsicr = value
                    self.caqvccparamsicr.value_namespace = name_space
                    self.caqvccparamsicr.value_namespace_prefix = name_space_prefix
                if(value_path == "caqVccParamsInheritLevel"):
                    self.caqvccparamsinheritlevel = value
                    self.caqvccparamsinheritlevel.value_namespace = name_space
                    self.caqvccparamsinheritlevel.value_namespace_prefix = name_space_prefix
                if(value_path == "caqVccParamsInvCdf"):
                    self.caqvccparamsinvcdf = value
                    self.caqvccparamsinvcdf.value_namespace = name_space
                    self.caqvccparamsinvcdf.value_namespace_prefix = name_space_prefix
                if(value_path == "caqVccParamsInvRdf"):
                    self.caqvccparamsinvrdf = value
                    self.caqvccparamsinvrdf.value_namespace = name_space
                    self.caqvccparamsinvrdf.value_namespace_prefix = name_space_prefix
                if(value_path == "caqVccParamsInvRif"):
                    self.caqvccparamsinvrif = value
                    self.caqvccparamsinvrif.value_namespace = name_space
                    self.caqvccparamsinvrif.value_namespace_prefix = name_space_prefix
                if(value_path == "caqVccParamsInvTrm"):
                    self.caqvccparamsinvtrm = value
                    self.caqvccparamsinvtrm.value_namespace = name_space
                    self.caqvccparamsinvtrm.value_namespace_prefix = name_space_prefix
                if(value_path == "caqVccParamsMcrIn"):
                    self.caqvccparamsmcrin = value
                    self.caqvccparamsmcrin.value_namespace = name_space
                    self.caqvccparamsmcrin.value_namespace_prefix = name_space_prefix
                if(value_path == "caqVccParamsMcrOut"):
                    self.caqvccparamsmcrout = value
                    self.caqvccparamsmcrout.value_namespace = name_space
                    self.caqvccparamsmcrout.value_namespace_prefix = name_space_prefix
                if(value_path == "caqVccParamsNrm"):
                    self.caqvccparamsnrm = value
                    self.caqvccparamsnrm.value_namespace = name_space
                    self.caqvccparamsnrm.value_namespace_prefix = name_space_prefix
                if(value_path == "caqVccParamsPcrIn0"):
                    self.caqvccparamspcrin0 = value
                    self.caqvccparamspcrin0.value_namespace = name_space
                    self.caqvccparamspcrin0.value_namespace_prefix = name_space_prefix
                if(value_path == "caqVccParamsPcrIn01"):
                    self.caqvccparamspcrin01 = value
                    self.caqvccparamspcrin01.value_namespace = name_space
                    self.caqvccparamspcrin01.value_namespace_prefix = name_space_prefix
                if(value_path == "caqVccParamsPcrOut0"):
                    self.caqvccparamspcrout0 = value
                    self.caqvccparamspcrout0.value_namespace = name_space
                    self.caqvccparamspcrout0.value_namespace_prefix = name_space_prefix
                if(value_path == "caqVccParamsPcrOut01"):
                    self.caqvccparamspcrout01 = value
                    self.caqvccparamspcrout01.value_namespace = name_space
                    self.caqvccparamspcrout01.value_namespace_prefix = name_space_prefix
                if(value_path == "caqVccParamsRfl"):
                    self.caqvccparamsrfl = value
                    self.caqvccparamsrfl.value_namespace = name_space
                    self.caqvccparamsrfl.value_namespace_prefix = name_space_prefix
                if(value_path == "caqVccParamsScrIn0"):
                    self.caqvccparamsscrin0 = value
                    self.caqvccparamsscrin0.value_namespace = name_space
                    self.caqvccparamsscrin0.value_namespace_prefix = name_space_prefix
                if(value_path == "caqVccParamsScrIn01"):
                    self.caqvccparamsscrin01 = value
                    self.caqvccparamsscrin01.value_namespace = name_space
                    self.caqvccparamsscrin01.value_namespace_prefix = name_space_prefix
                if(value_path == "caqVccParamsScrOut0"):
                    self.caqvccparamsscrout0 = value
                    self.caqvccparamsscrout0.value_namespace = name_space
                    self.caqvccparamsscrout0.value_namespace_prefix = name_space_prefix
                if(value_path == "caqVccParamsScrOut01"):
                    self.caqvccparamsscrout01 = value
                    self.caqvccparamsscrout01.value_namespace = name_space
                    self.caqvccparamsscrout01.value_namespace_prefix = name_space_prefix
                if(value_path == "caqVccParamsTbe"):
                    self.caqvccparamstbe = value
                    self.caqvccparamstbe.value_namespace = name_space
                    self.caqvccparamstbe.value_namespace_prefix = name_space_prefix
                if(value_path == "caqVccParamsType"):
                    self.caqvccparamstype = value
                    self.caqvccparamstype.value_namespace = name_space
                    self.caqvccparamstype.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.caqvccparamsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.caqvccparamsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "caqVccParamsTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-ATM-QOS-MIB:CISCO-ATM-QOS-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "caqVccParamsEntry"):
                for c in self.caqvccparamsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoAtmQosMib.Caqvccparamstable.Caqvccparamsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.caqvccparamsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "caqVccParamsEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Caqvpcparamstable(Entity):
        """
        This table is defined to provide QoS information for
        each active ATM VP existing on the interface.
        
        .. attribute:: caqvpcparamsentry
        
        	This list contains the ATM QoS parameters provided by ciscoAtmQosVpcEntry
        	**type**\: list of    :py:class:`Caqvpcparamsentry <ydk.models.cisco_ios_xe.CISCO_ATM_QOS_MIB.CiscoAtmQosMib.Caqvpcparamstable.Caqvpcparamsentry>`
        
        

        """

        _prefix = 'CISCO-ATM-QOS-MIB'
        _revision = '2002-06-10'

        def __init__(self):
            super(CiscoAtmQosMib.Caqvpcparamstable, self).__init__()

            self.yang_name = "caqVpcParamsTable"
            self.yang_parent_name = "CISCO-ATM-QOS-MIB"

            self.caqvpcparamsentry = YList(self)

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
                        super(CiscoAtmQosMib.Caqvpcparamstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoAtmQosMib.Caqvpcparamstable, self).__setattr__(name, value)


        class Caqvpcparamsentry(Entity):
            """
            This list contains the ATM QoS parameters provided by
            ciscoAtmQosVpcEntry.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: atmvplvpi  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4095
            
            	**refers to**\:  :py:class:`atmvplvpi <ydk.models.cisco_ios_xe.ATM_MIB.AtmMib.Atmvpltable.Atmvplentry>`
            
            .. attribute:: caqvpcparamsavailbw
            
            	Bandwidth in Kbps currently currently available on this PVP
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: caqvpcparamscesrate
            
            	Maximum rate in kbps at which CES VCs can transmit data with the associated permanent virtual path
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: caqvpcparamscesvccount
            
            	Number of CES VCs currently associated with the permanent virtual path
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: caqvpcparamsdatavccount
            
            	Number of data VCs currently associated with the permanent virtual path
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: caqvpcparamsmbs
            
            	Maximum burst size associated with the PVP
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: caqvpcparamspeakrate
            
            	Maximum rate in kbps at which the associated permanent virtual path can transmit data
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: caqvpcparamsscr
            
            	Sustained cell rate associated with the PVP
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: caqvpcparamsvcdf4ete
            
            	Vcd for F4 OAM end to end processing
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: caqvpcparamsvcdf4seg
            
            	Vcd for F4 OAM segment processing
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: caqvpcparamsvpstate
            
            	VP state of the current permanent virtual path
            	**type**\:   :py:class:`Vpstate <ydk.models.cisco_ios_xe.CISCO_ATM_QOS_MIB.Vpstate>`
            
            

            """

            _prefix = 'CISCO-ATM-QOS-MIB'
            _revision = '2002-06-10'

            def __init__(self):
                super(CiscoAtmQosMib.Caqvpcparamstable.Caqvpcparamsentry, self).__init__()

                self.yang_name = "caqVpcParamsEntry"
                self.yang_parent_name = "caqVpcParamsTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.atmvplvpi = YLeaf(YType.str, "atmVplVpi")

                self.caqvpcparamsavailbw = YLeaf(YType.uint32, "caqVpcParamsAvailBw")

                self.caqvpcparamscesrate = YLeaf(YType.uint32, "caqVpcParamsCesRate")

                self.caqvpcparamscesvccount = YLeaf(YType.int32, "caqVpcParamsCesVcCount")

                self.caqvpcparamsdatavccount = YLeaf(YType.int32, "caqVpcParamsDataVcCount")

                self.caqvpcparamsmbs = YLeaf(YType.uint32, "caqVpcParamsMbs")

                self.caqvpcparamspeakrate = YLeaf(YType.uint32, "caqVpcParamsPeakRate")

                self.caqvpcparamsscr = YLeaf(YType.uint32, "caqVpcParamsScr")

                self.caqvpcparamsvcdf4ete = YLeaf(YType.int32, "caqVpcParamsVcdF4Ete")

                self.caqvpcparamsvcdf4seg = YLeaf(YType.int32, "caqVpcParamsVcdF4Seg")

                self.caqvpcparamsvpstate = YLeaf(YType.enumeration, "caqVpcParamsVpState")

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
                                "caqvpcparamsavailbw",
                                "caqvpcparamscesrate",
                                "caqvpcparamscesvccount",
                                "caqvpcparamsdatavccount",
                                "caqvpcparamsmbs",
                                "caqvpcparamspeakrate",
                                "caqvpcparamsscr",
                                "caqvpcparamsvcdf4ete",
                                "caqvpcparamsvcdf4seg",
                                "caqvpcparamsvpstate") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoAtmQosMib.Caqvpcparamstable.Caqvpcparamsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoAtmQosMib.Caqvpcparamstable.Caqvpcparamsentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.atmvplvpi.is_set or
                    self.caqvpcparamsavailbw.is_set or
                    self.caqvpcparamscesrate.is_set or
                    self.caqvpcparamscesvccount.is_set or
                    self.caqvpcparamsdatavccount.is_set or
                    self.caqvpcparamsmbs.is_set or
                    self.caqvpcparamspeakrate.is_set or
                    self.caqvpcparamsscr.is_set or
                    self.caqvpcparamsvcdf4ete.is_set or
                    self.caqvpcparamsvcdf4seg.is_set or
                    self.caqvpcparamsvpstate.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.atmvplvpi.yfilter != YFilter.not_set or
                    self.caqvpcparamsavailbw.yfilter != YFilter.not_set or
                    self.caqvpcparamscesrate.yfilter != YFilter.not_set or
                    self.caqvpcparamscesvccount.yfilter != YFilter.not_set or
                    self.caqvpcparamsdatavccount.yfilter != YFilter.not_set or
                    self.caqvpcparamsmbs.yfilter != YFilter.not_set or
                    self.caqvpcparamspeakrate.yfilter != YFilter.not_set or
                    self.caqvpcparamsscr.yfilter != YFilter.not_set or
                    self.caqvpcparamsvcdf4ete.yfilter != YFilter.not_set or
                    self.caqvpcparamsvcdf4seg.yfilter != YFilter.not_set or
                    self.caqvpcparamsvpstate.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "caqVpcParamsEntry" + "[ifIndex='" + self.ifindex.get() + "']" + "[atmVplVpi='" + self.atmvplvpi.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-ATM-QOS-MIB:CISCO-ATM-QOS-MIB/caqVpcParamsTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.atmvplvpi.is_set or self.atmvplvpi.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvplvpi.get_name_leafdata())
                if (self.caqvpcparamsavailbw.is_set or self.caqvpcparamsavailbw.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.caqvpcparamsavailbw.get_name_leafdata())
                if (self.caqvpcparamscesrate.is_set or self.caqvpcparamscesrate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.caqvpcparamscesrate.get_name_leafdata())
                if (self.caqvpcparamscesvccount.is_set or self.caqvpcparamscesvccount.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.caqvpcparamscesvccount.get_name_leafdata())
                if (self.caqvpcparamsdatavccount.is_set or self.caqvpcparamsdatavccount.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.caqvpcparamsdatavccount.get_name_leafdata())
                if (self.caqvpcparamsmbs.is_set or self.caqvpcparamsmbs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.caqvpcparamsmbs.get_name_leafdata())
                if (self.caqvpcparamspeakrate.is_set or self.caqvpcparamspeakrate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.caqvpcparamspeakrate.get_name_leafdata())
                if (self.caqvpcparamsscr.is_set or self.caqvpcparamsscr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.caqvpcparamsscr.get_name_leafdata())
                if (self.caqvpcparamsvcdf4ete.is_set or self.caqvpcparamsvcdf4ete.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.caqvpcparamsvcdf4ete.get_name_leafdata())
                if (self.caqvpcparamsvcdf4seg.is_set or self.caqvpcparamsvcdf4seg.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.caqvpcparamsvcdf4seg.get_name_leafdata())
                if (self.caqvpcparamsvpstate.is_set or self.caqvpcparamsvpstate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.caqvpcparamsvpstate.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "atmVplVpi" or name == "caqVpcParamsAvailBw" or name == "caqVpcParamsCesRate" or name == "caqVpcParamsCesVcCount" or name == "caqVpcParamsDataVcCount" or name == "caqVpcParamsMbs" or name == "caqVpcParamsPeakRate" or name == "caqVpcParamsScr" or name == "caqVpcParamsVcdF4Ete" or name == "caqVpcParamsVcdF4Seg" or name == "caqVpcParamsVpState"):
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
                if(value_path == "caqVpcParamsAvailBw"):
                    self.caqvpcparamsavailbw = value
                    self.caqvpcparamsavailbw.value_namespace = name_space
                    self.caqvpcparamsavailbw.value_namespace_prefix = name_space_prefix
                if(value_path == "caqVpcParamsCesRate"):
                    self.caqvpcparamscesrate = value
                    self.caqvpcparamscesrate.value_namespace = name_space
                    self.caqvpcparamscesrate.value_namespace_prefix = name_space_prefix
                if(value_path == "caqVpcParamsCesVcCount"):
                    self.caqvpcparamscesvccount = value
                    self.caqvpcparamscesvccount.value_namespace = name_space
                    self.caqvpcparamscesvccount.value_namespace_prefix = name_space_prefix
                if(value_path == "caqVpcParamsDataVcCount"):
                    self.caqvpcparamsdatavccount = value
                    self.caqvpcparamsdatavccount.value_namespace = name_space
                    self.caqvpcparamsdatavccount.value_namespace_prefix = name_space_prefix
                if(value_path == "caqVpcParamsMbs"):
                    self.caqvpcparamsmbs = value
                    self.caqvpcparamsmbs.value_namespace = name_space
                    self.caqvpcparamsmbs.value_namespace_prefix = name_space_prefix
                if(value_path == "caqVpcParamsPeakRate"):
                    self.caqvpcparamspeakrate = value
                    self.caqvpcparamspeakrate.value_namespace = name_space
                    self.caqvpcparamspeakrate.value_namespace_prefix = name_space_prefix
                if(value_path == "caqVpcParamsScr"):
                    self.caqvpcparamsscr = value
                    self.caqvpcparamsscr.value_namespace = name_space
                    self.caqvpcparamsscr.value_namespace_prefix = name_space_prefix
                if(value_path == "caqVpcParamsVcdF4Ete"):
                    self.caqvpcparamsvcdf4ete = value
                    self.caqvpcparamsvcdf4ete.value_namespace = name_space
                    self.caqvpcparamsvcdf4ete.value_namespace_prefix = name_space_prefix
                if(value_path == "caqVpcParamsVcdF4Seg"):
                    self.caqvpcparamsvcdf4seg = value
                    self.caqvpcparamsvcdf4seg.value_namespace = name_space
                    self.caqvpcparamsvcdf4seg.value_namespace_prefix = name_space_prefix
                if(value_path == "caqVpcParamsVpState"):
                    self.caqvpcparamsvpstate = value
                    self.caqvpcparamsvpstate.value_namespace = name_space
                    self.caqvpcparamsvpstate.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.caqvpcparamsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.caqvpcparamsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "caqVpcParamsTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-ATM-QOS-MIB:CISCO-ATM-QOS-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "caqVpcParamsEntry"):
                for c in self.caqvpcparamsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoAtmQosMib.Caqvpcparamstable.Caqvpcparamsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.caqvpcparamsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "caqVpcParamsEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Caqqueuingparamstable(Entity):
        """
        This table provides queuing related information
        for a VC existing on an ATM interface.
        
        .. attribute:: caqqueuingparamsentry
        
        	This is defined as an entry in caqQueuingParamsTable
        	**type**\: list of    :py:class:`Caqqueuingparamsentry <ydk.models.cisco_ios_xe.CISCO_ATM_QOS_MIB.CiscoAtmQosMib.Caqqueuingparamstable.Caqqueuingparamsentry>`
        
        

        """

        _prefix = 'CISCO-ATM-QOS-MIB'
        _revision = '2002-06-10'

        def __init__(self):
            super(CiscoAtmQosMib.Caqqueuingparamstable, self).__init__()

            self.yang_name = "caqQueuingParamsTable"
            self.yang_parent_name = "CISCO-ATM-QOS-MIB"

            self.caqqueuingparamsentry = YList(self)

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
                        super(CiscoAtmQosMib.Caqqueuingparamstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoAtmQosMib.Caqqueuingparamstable, self).__setattr__(name, value)


        class Caqqueuingparamsentry(Entity):
            """
            This is defined as an entry in caqQueuingParamsTable.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: atmvclvpi  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4095
            
            	**refers to**\:  :py:class:`atmvclvpi <ydk.models.cisco_ios_xe.ATM_MIB.AtmMib.Atmvcltable.Atmvclentry>`
            
            .. attribute:: atmvclvci  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..65535
            
            	**refers to**\:  :py:class:`atmvclvci <ydk.models.cisco_ios_xe.ATM_MIB.AtmMib.Atmvcltable.Atmvclentry>`
            
            .. attribute:: caqqueuingparamsmeanqdepth
            
            	Mean Queue Depth associated with the vc.  This value is calculated based on the actual queue depth on the interface and the exponential weighting constant
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-ATM-QOS-MIB'
            _revision = '2002-06-10'

            def __init__(self):
                super(CiscoAtmQosMib.Caqqueuingparamstable.Caqqueuingparamsentry, self).__init__()

                self.yang_name = "caqQueuingParamsEntry"
                self.yang_parent_name = "caqQueuingParamsTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.atmvclvpi = YLeaf(YType.str, "atmVclVpi")

                self.atmvclvci = YLeaf(YType.str, "atmVclVci")

                self.caqqueuingparamsmeanqdepth = YLeaf(YType.uint32, "caqQueuingParamsMeanQDepth")

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
                                "caqqueuingparamsmeanqdepth") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoAtmQosMib.Caqqueuingparamstable.Caqqueuingparamsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoAtmQosMib.Caqqueuingparamstable.Caqqueuingparamsentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.atmvclvpi.is_set or
                    self.atmvclvci.is_set or
                    self.caqqueuingparamsmeanqdepth.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.atmvclvpi.yfilter != YFilter.not_set or
                    self.atmvclvci.yfilter != YFilter.not_set or
                    self.caqqueuingparamsmeanqdepth.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "caqQueuingParamsEntry" + "[ifIndex='" + self.ifindex.get() + "']" + "[atmVclVpi='" + self.atmvclvpi.get() + "']" + "[atmVclVci='" + self.atmvclvci.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-ATM-QOS-MIB:CISCO-ATM-QOS-MIB/caqQueuingParamsTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.atmvclvpi.is_set or self.atmvclvpi.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvclvpi.get_name_leafdata())
                if (self.atmvclvci.is_set or self.atmvclvci.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvclvci.get_name_leafdata())
                if (self.caqqueuingparamsmeanqdepth.is_set or self.caqqueuingparamsmeanqdepth.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.caqqueuingparamsmeanqdepth.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "atmVclVpi" or name == "atmVclVci" or name == "caqQueuingParamsMeanQDepth"):
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
                if(value_path == "caqQueuingParamsMeanQDepth"):
                    self.caqqueuingparamsmeanqdepth = value
                    self.caqqueuingparamsmeanqdepth.value_namespace = name_space
                    self.caqqueuingparamsmeanqdepth.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.caqqueuingparamsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.caqqueuingparamsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "caqQueuingParamsTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-ATM-QOS-MIB:CISCO-ATM-QOS-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "caqQueuingParamsEntry"):
                for c in self.caqqueuingparamsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoAtmQosMib.Caqqueuingparamstable.Caqqueuingparamsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.caqqueuingparamsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "caqQueuingParamsEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Caqqueuingparamsclasstable(Entity):
        """
        This table provides queuing information for all 
        queuing classes associating with a VC.
        
        .. attribute:: caqqueuingparamsclassentry
        
        	This is defined as an entry in ciscoAtmQosVcQueuingClassTable to provide queuing information of a specific class
        	**type**\: list of    :py:class:`Caqqueuingparamsclassentry <ydk.models.cisco_ios_xe.CISCO_ATM_QOS_MIB.CiscoAtmQosMib.Caqqueuingparamsclasstable.Caqqueuingparamsclassentry>`
        
        

        """

        _prefix = 'CISCO-ATM-QOS-MIB'
        _revision = '2002-06-10'

        def __init__(self):
            super(CiscoAtmQosMib.Caqqueuingparamsclasstable, self).__init__()

            self.yang_name = "caqQueuingParamsClassTable"
            self.yang_parent_name = "CISCO-ATM-QOS-MIB"

            self.caqqueuingparamsclassentry = YList(self)

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
                        super(CiscoAtmQosMib.Caqqueuingparamsclasstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoAtmQosMib.Caqqueuingparamsclasstable, self).__setattr__(name, value)


        class Caqqueuingparamsclassentry(Entity):
            """
            This is defined as an entry in ciscoAtmQosVcQueuingClassTable
            to provide queuing information of a specific class.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: atmvclvpi  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4095
            
            	**refers to**\:  :py:class:`atmvclvpi <ydk.models.cisco_ios_xe.ATM_MIB.AtmMib.Atmvcltable.Atmvclentry>`
            
            .. attribute:: atmvclvci  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..65535
            
            	**refers to**\:  :py:class:`atmvclvci <ydk.models.cisco_ios_xe.ATM_MIB.AtmMib.Atmvcltable.Atmvclentry>`
            
            .. attribute:: caqqueuingparamsclassindex  <key>
            
            	A class index, which associates with an IP precedence (0 to 8), is defined to reference individual caqQueuingParamsClassEntry
            	**type**\:  int
            
            	**range:** 0..8
            
            .. attribute:: caqqueuingparamsclassmaxthre
            
            	Maximum Threshold value in kbps
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: caqqueuingparamsclassminthre
            
            	Minimum Threshold value in kbps
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: caqqueuingparamsclassmrkprob
            
            	Mark probability denominator.  This is the value used in the calculation of a packet being dropped when the average queue size is between the minimum threshold and the maximum threshold
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: caqqueuingparamsclassranddrp
            
            	Number of packets dropped when Mean Queue Length is between Minimum Threshold and Maximum Threshold range
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: caqqueuingparamsclasstaildrp
            
            	Number of packets dropped because the Mean Queue Depth exceeds the Maximum Threshold value
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-ATM-QOS-MIB'
            _revision = '2002-06-10'

            def __init__(self):
                super(CiscoAtmQosMib.Caqqueuingparamsclasstable.Caqqueuingparamsclassentry, self).__init__()

                self.yang_name = "caqQueuingParamsClassEntry"
                self.yang_parent_name = "caqQueuingParamsClassTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.atmvclvpi = YLeaf(YType.str, "atmVclVpi")

                self.atmvclvci = YLeaf(YType.str, "atmVclVci")

                self.caqqueuingparamsclassindex = YLeaf(YType.int32, "caqQueuingParamsClassIndex")

                self.caqqueuingparamsclassmaxthre = YLeaf(YType.uint32, "caqQueuingParamsClassMaxThre")

                self.caqqueuingparamsclassminthre = YLeaf(YType.uint32, "caqQueuingParamsClassMinThre")

                self.caqqueuingparamsclassmrkprob = YLeaf(YType.uint32, "caqQueuingParamsClassMrkProb")

                self.caqqueuingparamsclassranddrp = YLeaf(YType.uint32, "caqQueuingParamsClassRandDrp")

                self.caqqueuingparamsclasstaildrp = YLeaf(YType.uint32, "caqQueuingParamsClassTailDrp")

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
                                "caqqueuingparamsclassindex",
                                "caqqueuingparamsclassmaxthre",
                                "caqqueuingparamsclassminthre",
                                "caqqueuingparamsclassmrkprob",
                                "caqqueuingparamsclassranddrp",
                                "caqqueuingparamsclasstaildrp") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoAtmQosMib.Caqqueuingparamsclasstable.Caqqueuingparamsclassentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoAtmQosMib.Caqqueuingparamsclasstable.Caqqueuingparamsclassentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.atmvclvpi.is_set or
                    self.atmvclvci.is_set or
                    self.caqqueuingparamsclassindex.is_set or
                    self.caqqueuingparamsclassmaxthre.is_set or
                    self.caqqueuingparamsclassminthre.is_set or
                    self.caqqueuingparamsclassmrkprob.is_set or
                    self.caqqueuingparamsclassranddrp.is_set or
                    self.caqqueuingparamsclasstaildrp.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.atmvclvpi.yfilter != YFilter.not_set or
                    self.atmvclvci.yfilter != YFilter.not_set or
                    self.caqqueuingparamsclassindex.yfilter != YFilter.not_set or
                    self.caqqueuingparamsclassmaxthre.yfilter != YFilter.not_set or
                    self.caqqueuingparamsclassminthre.yfilter != YFilter.not_set or
                    self.caqqueuingparamsclassmrkprob.yfilter != YFilter.not_set or
                    self.caqqueuingparamsclassranddrp.yfilter != YFilter.not_set or
                    self.caqqueuingparamsclasstaildrp.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "caqQueuingParamsClassEntry" + "[ifIndex='" + self.ifindex.get() + "']" + "[atmVclVpi='" + self.atmvclvpi.get() + "']" + "[atmVclVci='" + self.atmvclvci.get() + "']" + "[caqQueuingParamsClassIndex='" + self.caqqueuingparamsclassindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-ATM-QOS-MIB:CISCO-ATM-QOS-MIB/caqQueuingParamsClassTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.atmvclvpi.is_set or self.atmvclvpi.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvclvpi.get_name_leafdata())
                if (self.atmvclvci.is_set or self.atmvclvci.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvclvci.get_name_leafdata())
                if (self.caqqueuingparamsclassindex.is_set or self.caqqueuingparamsclassindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.caqqueuingparamsclassindex.get_name_leafdata())
                if (self.caqqueuingparamsclassmaxthre.is_set or self.caqqueuingparamsclassmaxthre.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.caqqueuingparamsclassmaxthre.get_name_leafdata())
                if (self.caqqueuingparamsclassminthre.is_set or self.caqqueuingparamsclassminthre.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.caqqueuingparamsclassminthre.get_name_leafdata())
                if (self.caqqueuingparamsclassmrkprob.is_set or self.caqqueuingparamsclassmrkprob.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.caqqueuingparamsclassmrkprob.get_name_leafdata())
                if (self.caqqueuingparamsclassranddrp.is_set or self.caqqueuingparamsclassranddrp.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.caqqueuingparamsclassranddrp.get_name_leafdata())
                if (self.caqqueuingparamsclasstaildrp.is_set or self.caqqueuingparamsclasstaildrp.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.caqqueuingparamsclasstaildrp.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "atmVclVpi" or name == "atmVclVci" or name == "caqQueuingParamsClassIndex" or name == "caqQueuingParamsClassMaxThre" or name == "caqQueuingParamsClassMinThre" or name == "caqQueuingParamsClassMrkProb" or name == "caqQueuingParamsClassRandDrp" or name == "caqQueuingParamsClassTailDrp"):
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
                if(value_path == "caqQueuingParamsClassIndex"):
                    self.caqqueuingparamsclassindex = value
                    self.caqqueuingparamsclassindex.value_namespace = name_space
                    self.caqqueuingparamsclassindex.value_namespace_prefix = name_space_prefix
                if(value_path == "caqQueuingParamsClassMaxThre"):
                    self.caqqueuingparamsclassmaxthre = value
                    self.caqqueuingparamsclassmaxthre.value_namespace = name_space
                    self.caqqueuingparamsclassmaxthre.value_namespace_prefix = name_space_prefix
                if(value_path == "caqQueuingParamsClassMinThre"):
                    self.caqqueuingparamsclassminthre = value
                    self.caqqueuingparamsclassminthre.value_namespace = name_space
                    self.caqqueuingparamsclassminthre.value_namespace_prefix = name_space_prefix
                if(value_path == "caqQueuingParamsClassMrkProb"):
                    self.caqqueuingparamsclassmrkprob = value
                    self.caqqueuingparamsclassmrkprob.value_namespace = name_space
                    self.caqqueuingparamsclassmrkprob.value_namespace_prefix = name_space_prefix
                if(value_path == "caqQueuingParamsClassRandDrp"):
                    self.caqqueuingparamsclassranddrp = value
                    self.caqqueuingparamsclassranddrp.value_namespace = name_space
                    self.caqqueuingparamsclassranddrp.value_namespace_prefix = name_space_prefix
                if(value_path == "caqQueuingParamsClassTailDrp"):
                    self.caqqueuingparamsclasstaildrp = value
                    self.caqqueuingparamsclasstaildrp.value_namespace = name_space
                    self.caqqueuingparamsclasstaildrp.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.caqqueuingparamsclassentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.caqqueuingparamsclassentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "caqQueuingParamsClassTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-ATM-QOS-MIB:CISCO-ATM-QOS-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "caqQueuingParamsClassEntry"):
                for c in self.caqqueuingparamsclassentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoAtmQosMib.Caqqueuingparamsclasstable.Caqqueuingparamsclassentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.caqqueuingparamsclassentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "caqQueuingParamsClassEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.caqqueuingparamsclasstable is not None and self.caqqueuingparamsclasstable.has_data()) or
            (self.caqqueuingparamstable is not None and self.caqqueuingparamstable.has_data()) or
            (self.caqvccparamstable is not None and self.caqvccparamstable.has_data()) or
            (self.caqvpcparamstable is not None and self.caqvpcparamstable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.caqqueuingparamsclasstable is not None and self.caqqueuingparamsclasstable.has_operation()) or
            (self.caqqueuingparamstable is not None and self.caqqueuingparamstable.has_operation()) or
            (self.caqvccparamstable is not None and self.caqvccparamstable.has_operation()) or
            (self.caqvpcparamstable is not None and self.caqvpcparamstable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-ATM-QOS-MIB:CISCO-ATM-QOS-MIB" + path_buffer

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

        if (child_yang_name == "caqQueuingParamsClassTable"):
            if (self.caqqueuingparamsclasstable is None):
                self.caqqueuingparamsclasstable = CiscoAtmQosMib.Caqqueuingparamsclasstable()
                self.caqqueuingparamsclasstable.parent = self
                self._children_name_map["caqqueuingparamsclasstable"] = "caqQueuingParamsClassTable"
            return self.caqqueuingparamsclasstable

        if (child_yang_name == "caqQueuingParamsTable"):
            if (self.caqqueuingparamstable is None):
                self.caqqueuingparamstable = CiscoAtmQosMib.Caqqueuingparamstable()
                self.caqqueuingparamstable.parent = self
                self._children_name_map["caqqueuingparamstable"] = "caqQueuingParamsTable"
            return self.caqqueuingparamstable

        if (child_yang_name == "caqVccParamsTable"):
            if (self.caqvccparamstable is None):
                self.caqvccparamstable = CiscoAtmQosMib.Caqvccparamstable()
                self.caqvccparamstable.parent = self
                self._children_name_map["caqvccparamstable"] = "caqVccParamsTable"
            return self.caqvccparamstable

        if (child_yang_name == "caqVpcParamsTable"):
            if (self.caqvpcparamstable is None):
                self.caqvpcparamstable = CiscoAtmQosMib.Caqvpcparamstable()
                self.caqvpcparamstable.parent = self
                self._children_name_map["caqvpcparamstable"] = "caqVpcParamsTable"
            return self.caqvpcparamstable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "caqQueuingParamsClassTable" or name == "caqQueuingParamsTable" or name == "caqVccParamsTable" or name == "caqVpcParamsTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoAtmQosMib()
        return self._top_entity

