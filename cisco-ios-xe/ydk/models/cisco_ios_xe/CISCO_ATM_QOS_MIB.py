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
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class VcParamConfigLocation(Enum):
    """
    VcParamConfigLocation

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


class VpState(Enum):
    """
    VpState

    States of virtual path\:

    1 \- Inactive

    2 \- Active

    .. data:: vpStateInactive = 1

    .. data:: vpStateActive = 2

    """

    vpStateInactive = Enum.YLeaf(1, "vpStateInactive")

    vpStateActive = Enum.YLeaf(2, "vpStateActive")



class CISCOATMQOSMIB(Entity):
    """
    
    
    .. attribute:: caqqueuingparamsclasstable
    
    	This table provides queuing information for all  queuing classes associating with a VC
    	**type**\:   :py:class:`Caqqueuingparamsclasstable <ydk.models.cisco_ios_xe.CISCO_ATM_QOS_MIB.CISCOATMQOSMIB.Caqqueuingparamsclasstable>`
    
    .. attribute:: caqqueuingparamstable
    
    	This table provides queuing related information for a VC existing on an ATM interface
    	**type**\:   :py:class:`Caqqueuingparamstable <ydk.models.cisco_ios_xe.CISCO_ATM_QOS_MIB.CISCOATMQOSMIB.Caqqueuingparamstable>`
    
    .. attribute:: caqvccparamstable
    
    	This table is defined to provide QoS information for each active ATM VC existing on the interface
    	**type**\:   :py:class:`Caqvccparamstable <ydk.models.cisco_ios_xe.CISCO_ATM_QOS_MIB.CISCOATMQOSMIB.Caqvccparamstable>`
    
    .. attribute:: caqvpcparamstable
    
    	This table is defined to provide QoS information for each active ATM VP existing on the interface
    	**type**\:   :py:class:`Caqvpcparamstable <ydk.models.cisco_ios_xe.CISCO_ATM_QOS_MIB.CISCOATMQOSMIB.Caqvpcparamstable>`
    
    

    """

    _prefix = 'CISCO-ATM-QOS-MIB'
    _revision = '2002-06-10'

    def __init__(self):
        super(CISCOATMQOSMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-ATM-QOS-MIB"
        self.yang_parent_name = "CISCO-ATM-QOS-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"caqQueuingParamsClassTable" : ("caqqueuingparamsclasstable", CISCOATMQOSMIB.Caqqueuingparamsclasstable), "caqQueuingParamsTable" : ("caqqueuingparamstable", CISCOATMQOSMIB.Caqqueuingparamstable), "caqVccParamsTable" : ("caqvccparamstable", CISCOATMQOSMIB.Caqvccparamstable), "caqVpcParamsTable" : ("caqvpcparamstable", CISCOATMQOSMIB.Caqvpcparamstable)}
        self._child_list_classes = {}

        self.caqqueuingparamsclasstable = CISCOATMQOSMIB.Caqqueuingparamsclasstable()
        self.caqqueuingparamsclasstable.parent = self
        self._children_name_map["caqqueuingparamsclasstable"] = "caqQueuingParamsClassTable"
        self._children_yang_names.add("caqQueuingParamsClassTable")

        self.caqqueuingparamstable = CISCOATMQOSMIB.Caqqueuingparamstable()
        self.caqqueuingparamstable.parent = self
        self._children_name_map["caqqueuingparamstable"] = "caqQueuingParamsTable"
        self._children_yang_names.add("caqQueuingParamsTable")

        self.caqvccparamstable = CISCOATMQOSMIB.Caqvccparamstable()
        self.caqvccparamstable.parent = self
        self._children_name_map["caqvccparamstable"] = "caqVccParamsTable"
        self._children_yang_names.add("caqVccParamsTable")

        self.caqvpcparamstable = CISCOATMQOSMIB.Caqvpcparamstable()
        self.caqvpcparamstable.parent = self
        self._children_name_map["caqvpcparamstable"] = "caqVpcParamsTable"
        self._children_yang_names.add("caqVpcParamsTable")
        self._segment_path = lambda: "CISCO-ATM-QOS-MIB:CISCO-ATM-QOS-MIB"


    class Caqqueuingparamsclasstable(Entity):
        """
        This table provides queuing information for all 
        queuing classes associating with a VC.
        
        .. attribute:: caqqueuingparamsclassentry
        
        	This is defined as an entry in ciscoAtmQosVcQueuingClassTable to provide queuing information of a specific class
        	**type**\: list of    :py:class:`Caqqueuingparamsclassentry <ydk.models.cisco_ios_xe.CISCO_ATM_QOS_MIB.CISCOATMQOSMIB.Caqqueuingparamsclasstable.Caqqueuingparamsclassentry>`
        
        

        """

        _prefix = 'CISCO-ATM-QOS-MIB'
        _revision = '2002-06-10'

        def __init__(self):
            super(CISCOATMQOSMIB.Caqqueuingparamsclasstable, self).__init__()

            self.yang_name = "caqQueuingParamsClassTable"
            self.yang_parent_name = "CISCO-ATM-QOS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"caqQueuingParamsClassEntry" : ("caqqueuingparamsclassentry", CISCOATMQOSMIB.Caqqueuingparamsclasstable.Caqqueuingparamsclassentry)}

            self.caqqueuingparamsclassentry = YList(self)
            self._segment_path = lambda: "caqQueuingParamsClassTable"
            self._absolute_path = lambda: "CISCO-ATM-QOS-MIB:CISCO-ATM-QOS-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOATMQOSMIB.Caqqueuingparamsclasstable, [], name, value)


        class Caqqueuingparamsclassentry(Entity):
            """
            This is defined as an entry in ciscoAtmQosVcQueuingClassTable
            to provide queuing information of a specific class.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: atmvclvpi  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4095
            
            	**refers to**\:  :py:class:`atmvclvpi <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.Atmvcltable.Atmvclentry>`
            
            .. attribute:: atmvclvci  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..65535
            
            	**refers to**\:  :py:class:`atmvclvci <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.Atmvcltable.Atmvclentry>`
            
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
                super(CISCOATMQOSMIB.Caqqueuingparamsclasstable.Caqqueuingparamsclassentry, self).__init__()

                self.yang_name = "caqQueuingParamsClassEntry"
                self.yang_parent_name = "caqQueuingParamsClassTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.atmvclvpi = YLeaf(YType.str, "atmVclVpi")

                self.atmvclvci = YLeaf(YType.str, "atmVclVci")

                self.caqqueuingparamsclassindex = YLeaf(YType.int32, "caqQueuingParamsClassIndex")

                self.caqqueuingparamsclassmaxthre = YLeaf(YType.uint32, "caqQueuingParamsClassMaxThre")

                self.caqqueuingparamsclassminthre = YLeaf(YType.uint32, "caqQueuingParamsClassMinThre")

                self.caqqueuingparamsclassmrkprob = YLeaf(YType.uint32, "caqQueuingParamsClassMrkProb")

                self.caqqueuingparamsclassranddrp = YLeaf(YType.uint32, "caqQueuingParamsClassRandDrp")

                self.caqqueuingparamsclasstaildrp = YLeaf(YType.uint32, "caqQueuingParamsClassTailDrp")
                self._segment_path = lambda: "caqQueuingParamsClassEntry" + "[ifIndex='" + self.ifindex.get() + "']" + "[atmVclVpi='" + self.atmvclvpi.get() + "']" + "[atmVclVci='" + self.atmvclvci.get() + "']" + "[caqQueuingParamsClassIndex='" + self.caqqueuingparamsclassindex.get() + "']"
                self._absolute_path = lambda: "CISCO-ATM-QOS-MIB:CISCO-ATM-QOS-MIB/caqQueuingParamsClassTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOATMQOSMIB.Caqqueuingparamsclasstable.Caqqueuingparamsclassentry, ['ifindex', 'atmvclvpi', 'atmvclvci', 'caqqueuingparamsclassindex', 'caqqueuingparamsclassmaxthre', 'caqqueuingparamsclassminthre', 'caqqueuingparamsclassmrkprob', 'caqqueuingparamsclassranddrp', 'caqqueuingparamsclasstaildrp'], name, value)


    class Caqqueuingparamstable(Entity):
        """
        This table provides queuing related information
        for a VC existing on an ATM interface.
        
        .. attribute:: caqqueuingparamsentry
        
        	This is defined as an entry in caqQueuingParamsTable
        	**type**\: list of    :py:class:`Caqqueuingparamsentry <ydk.models.cisco_ios_xe.CISCO_ATM_QOS_MIB.CISCOATMQOSMIB.Caqqueuingparamstable.Caqqueuingparamsentry>`
        
        

        """

        _prefix = 'CISCO-ATM-QOS-MIB'
        _revision = '2002-06-10'

        def __init__(self):
            super(CISCOATMQOSMIB.Caqqueuingparamstable, self).__init__()

            self.yang_name = "caqQueuingParamsTable"
            self.yang_parent_name = "CISCO-ATM-QOS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"caqQueuingParamsEntry" : ("caqqueuingparamsentry", CISCOATMQOSMIB.Caqqueuingparamstable.Caqqueuingparamsentry)}

            self.caqqueuingparamsentry = YList(self)
            self._segment_path = lambda: "caqQueuingParamsTable"
            self._absolute_path = lambda: "CISCO-ATM-QOS-MIB:CISCO-ATM-QOS-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOATMQOSMIB.Caqqueuingparamstable, [], name, value)


        class Caqqueuingparamsentry(Entity):
            """
            This is defined as an entry in caqQueuingParamsTable.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: atmvclvpi  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4095
            
            	**refers to**\:  :py:class:`atmvclvpi <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.Atmvcltable.Atmvclentry>`
            
            .. attribute:: atmvclvci  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..65535
            
            	**refers to**\:  :py:class:`atmvclvci <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.Atmvcltable.Atmvclentry>`
            
            .. attribute:: caqqueuingparamsmeanqdepth
            
            	Mean Queue Depth associated with the vc.  This value is calculated based on the actual queue depth on the interface and the exponential weighting constant
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-ATM-QOS-MIB'
            _revision = '2002-06-10'

            def __init__(self):
                super(CISCOATMQOSMIB.Caqqueuingparamstable.Caqqueuingparamsentry, self).__init__()

                self.yang_name = "caqQueuingParamsEntry"
                self.yang_parent_name = "caqQueuingParamsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.atmvclvpi = YLeaf(YType.str, "atmVclVpi")

                self.atmvclvci = YLeaf(YType.str, "atmVclVci")

                self.caqqueuingparamsmeanqdepth = YLeaf(YType.uint32, "caqQueuingParamsMeanQDepth")
                self._segment_path = lambda: "caqQueuingParamsEntry" + "[ifIndex='" + self.ifindex.get() + "']" + "[atmVclVpi='" + self.atmvclvpi.get() + "']" + "[atmVclVci='" + self.atmvclvci.get() + "']"
                self._absolute_path = lambda: "CISCO-ATM-QOS-MIB:CISCO-ATM-QOS-MIB/caqQueuingParamsTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOATMQOSMIB.Caqqueuingparamstable.Caqqueuingparamsentry, ['ifindex', 'atmvclvpi', 'atmvclvci', 'caqqueuingparamsmeanqdepth'], name, value)


    class Caqvccparamstable(Entity):
        """
        This table is defined to provide QoS information for
        each active ATM VC existing on the interface.
        
        .. attribute:: caqvccparamsentry
        
        	This list contains the ATM QoS parameters provided by ciscoAtmQosVccEntry
        	**type**\: list of    :py:class:`Caqvccparamsentry <ydk.models.cisco_ios_xe.CISCO_ATM_QOS_MIB.CISCOATMQOSMIB.Caqvccparamstable.Caqvccparamsentry>`
        
        

        """

        _prefix = 'CISCO-ATM-QOS-MIB'
        _revision = '2002-06-10'

        def __init__(self):
            super(CISCOATMQOSMIB.Caqvccparamstable, self).__init__()

            self.yang_name = "caqVccParamsTable"
            self.yang_parent_name = "CISCO-ATM-QOS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"caqVccParamsEntry" : ("caqvccparamsentry", CISCOATMQOSMIB.Caqvccparamstable.Caqvccparamsentry)}

            self.caqvccparamsentry = YList(self)
            self._segment_path = lambda: "caqVccParamsTable"
            self._absolute_path = lambda: "CISCO-ATM-QOS-MIB:CISCO-ATM-QOS-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOATMQOSMIB.Caqvccparamstable, [], name, value)


        class Caqvccparamsentry(Entity):
            """
            This list contains the ATM QoS parameters provided by
            ciscoAtmQosVccEntry.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: atmvclvpi  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4095
            
            	**refers to**\:  :py:class:`atmvclvpi <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.Atmvcltable.Atmvclentry>`
            
            .. attribute:: atmvclvci  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..65535
            
            	**refers to**\:  :py:class:`atmvclvci <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.Atmvcltable.Atmvclentry>`
            
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
            	**type**\:   :py:class:`VcParamConfigLocation <ydk.models.cisco_ios_xe.CISCO_ATM_QOS_MIB.VcParamConfigLocation>`
            
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
            	**type**\:   :py:class:`VcParamConfigLocation <ydk.models.cisco_ios_xe.CISCO_ATM_QOS_MIB.VcParamConfigLocation>`
            
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
            	**type**\:   :py:class:`AtmServiceCategory <ydk.models.cisco_ios_xe.ATM_FORUM_TC_MIB.AtmServiceCategory>`
            
            

            """

            _prefix = 'CISCO-ATM-QOS-MIB'
            _revision = '2002-06-10'

            def __init__(self):
                super(CISCOATMQOSMIB.Caqvccparamstable.Caqvccparamsentry, self).__init__()

                self.yang_name = "caqVccParamsEntry"
                self.yang_parent_name = "caqVccParamsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

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
                self._segment_path = lambda: "caqVccParamsEntry" + "[ifIndex='" + self.ifindex.get() + "']" + "[atmVclVpi='" + self.atmvclvpi.get() + "']" + "[atmVclVci='" + self.atmvclvci.get() + "']"
                self._absolute_path = lambda: "CISCO-ATM-QOS-MIB:CISCO-ATM-QOS-MIB/caqVccParamsTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOATMQOSMIB.Caqvccparamstable.Caqvccparamsentry, ['ifindex', 'atmvclvpi', 'atmvclvci', 'caqvccparamsadtf', 'caqvccparamsbcsin0', 'caqvccparamsbcsin01', 'caqvccparamsbcsout0', 'caqvccparamsbcsout01', 'caqvccparamscdv', 'caqvccparamscdvt', 'caqvccparamsfrtt', 'caqvccparamsicr', 'caqvccparamsinheritlevel', 'caqvccparamsinvcdf', 'caqvccparamsinvrdf', 'caqvccparamsinvrif', 'caqvccparamsinvtrm', 'caqvccparamsmcrin', 'caqvccparamsmcrout', 'caqvccparamsnrm', 'caqvccparamspcrin0', 'caqvccparamspcrin01', 'caqvccparamspcrout0', 'caqvccparamspcrout01', 'caqvccparamsrfl', 'caqvccparamsscrin0', 'caqvccparamsscrin01', 'caqvccparamsscrout0', 'caqvccparamsscrout01', 'caqvccparamstbe', 'caqvccparamstype'], name, value)


    class Caqvpcparamstable(Entity):
        """
        This table is defined to provide QoS information for
        each active ATM VP existing on the interface.
        
        .. attribute:: caqvpcparamsentry
        
        	This list contains the ATM QoS parameters provided by ciscoAtmQosVpcEntry
        	**type**\: list of    :py:class:`Caqvpcparamsentry <ydk.models.cisco_ios_xe.CISCO_ATM_QOS_MIB.CISCOATMQOSMIB.Caqvpcparamstable.Caqvpcparamsentry>`
        
        

        """

        _prefix = 'CISCO-ATM-QOS-MIB'
        _revision = '2002-06-10'

        def __init__(self):
            super(CISCOATMQOSMIB.Caqvpcparamstable, self).__init__()

            self.yang_name = "caqVpcParamsTable"
            self.yang_parent_name = "CISCO-ATM-QOS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"caqVpcParamsEntry" : ("caqvpcparamsentry", CISCOATMQOSMIB.Caqvpcparamstable.Caqvpcparamsentry)}

            self.caqvpcparamsentry = YList(self)
            self._segment_path = lambda: "caqVpcParamsTable"
            self._absolute_path = lambda: "CISCO-ATM-QOS-MIB:CISCO-ATM-QOS-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOATMQOSMIB.Caqvpcparamstable, [], name, value)


        class Caqvpcparamsentry(Entity):
            """
            This list contains the ATM QoS parameters provided by
            ciscoAtmQosVpcEntry.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: atmvplvpi  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4095
            
            	**refers to**\:  :py:class:`atmvplvpi <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.Atmvpltable.Atmvplentry>`
            
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
            	**type**\:   :py:class:`VpState <ydk.models.cisco_ios_xe.CISCO_ATM_QOS_MIB.VpState>`
            
            

            """

            _prefix = 'CISCO-ATM-QOS-MIB'
            _revision = '2002-06-10'

            def __init__(self):
                super(CISCOATMQOSMIB.Caqvpcparamstable.Caqvpcparamsentry, self).__init__()

                self.yang_name = "caqVpcParamsEntry"
                self.yang_parent_name = "caqVpcParamsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

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
                self._segment_path = lambda: "caqVpcParamsEntry" + "[ifIndex='" + self.ifindex.get() + "']" + "[atmVplVpi='" + self.atmvplvpi.get() + "']"
                self._absolute_path = lambda: "CISCO-ATM-QOS-MIB:CISCO-ATM-QOS-MIB/caqVpcParamsTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOATMQOSMIB.Caqvpcparamstable.Caqvpcparamsentry, ['ifindex', 'atmvplvpi', 'caqvpcparamsavailbw', 'caqvpcparamscesrate', 'caqvpcparamscesvccount', 'caqvpcparamsdatavccount', 'caqvpcparamsmbs', 'caqvpcparamspeakrate', 'caqvpcparamsscr', 'caqvpcparamsvcdf4ete', 'caqvpcparamsvcdf4seg', 'caqvpcparamsvpstate'], name, value)

    def clone_ptr(self):
        self._top_entity = CISCOATMQOSMIB()
        return self._top_entity

