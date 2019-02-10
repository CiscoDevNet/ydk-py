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
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class VcParamConfigLocation(Enum):
    """
    VcParamConfigLocation (Enum Class)

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
    VpState (Enum Class)

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
    
    
    .. attribute:: caqvccparamstable
    
    	This table is defined to provide QoS information for each active ATM VC existing on the interface
    	**type**\:  :py:class:`CaqVccParamsTable <ydk.models.cisco_ios_xe.CISCO_ATM_QOS_MIB.CISCOATMQOSMIB.CaqVccParamsTable>`
    
    	**config**\: False
    
    .. attribute:: caqvpcparamstable
    
    	This table is defined to provide QoS information for each active ATM VP existing on the interface
    	**type**\:  :py:class:`CaqVpcParamsTable <ydk.models.cisco_ios_xe.CISCO_ATM_QOS_MIB.CISCOATMQOSMIB.CaqVpcParamsTable>`
    
    	**config**\: False
    
    .. attribute:: caqqueuingparamstable
    
    	This table provides queuing related information for a VC existing on an ATM interface
    	**type**\:  :py:class:`CaqQueuingParamsTable <ydk.models.cisco_ios_xe.CISCO_ATM_QOS_MIB.CISCOATMQOSMIB.CaqQueuingParamsTable>`
    
    	**config**\: False
    
    .. attribute:: caqqueuingparamsclasstable
    
    	This table provides queuing information for all  queuing classes associating with a VC
    	**type**\:  :py:class:`CaqQueuingParamsClassTable <ydk.models.cisco_ios_xe.CISCO_ATM_QOS_MIB.CISCOATMQOSMIB.CaqQueuingParamsClassTable>`
    
    	**config**\: False
    
    

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
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("caqVccParamsTable", ("caqvccparamstable", CISCOATMQOSMIB.CaqVccParamsTable)), ("caqVpcParamsTable", ("caqvpcparamstable", CISCOATMQOSMIB.CaqVpcParamsTable)), ("caqQueuingParamsTable", ("caqqueuingparamstable", CISCOATMQOSMIB.CaqQueuingParamsTable)), ("caqQueuingParamsClassTable", ("caqqueuingparamsclasstable", CISCOATMQOSMIB.CaqQueuingParamsClassTable))])
        self._leafs = OrderedDict()

        self.caqvccparamstable = CISCOATMQOSMIB.CaqVccParamsTable()
        self.caqvccparamstable.parent = self
        self._children_name_map["caqvccparamstable"] = "caqVccParamsTable"

        self.caqvpcparamstable = CISCOATMQOSMIB.CaqVpcParamsTable()
        self.caqvpcparamstable.parent = self
        self._children_name_map["caqvpcparamstable"] = "caqVpcParamsTable"

        self.caqqueuingparamstable = CISCOATMQOSMIB.CaqQueuingParamsTable()
        self.caqqueuingparamstable.parent = self
        self._children_name_map["caqqueuingparamstable"] = "caqQueuingParamsTable"

        self.caqqueuingparamsclasstable = CISCOATMQOSMIB.CaqQueuingParamsClassTable()
        self.caqqueuingparamsclasstable.parent = self
        self._children_name_map["caqqueuingparamsclasstable"] = "caqQueuingParamsClassTable"
        self._segment_path = lambda: "CISCO-ATM-QOS-MIB:CISCO-ATM-QOS-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(CISCOATMQOSMIB, [], name, value)


    class CaqVccParamsTable(Entity):
        """
        This table is defined to provide QoS information for
        each active ATM VC existing on the interface.
        
        .. attribute:: caqvccparamsentry
        
        	This list contains the ATM QoS parameters provided by ciscoAtmQosVccEntry
        	**type**\: list of  		 :py:class:`CaqVccParamsEntry <ydk.models.cisco_ios_xe.CISCO_ATM_QOS_MIB.CISCOATMQOSMIB.CaqVccParamsTable.CaqVccParamsEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-ATM-QOS-MIB'
        _revision = '2002-06-10'

        def __init__(self):
            super(CISCOATMQOSMIB.CaqVccParamsTable, self).__init__()

            self.yang_name = "caqVccParamsTable"
            self.yang_parent_name = "CISCO-ATM-QOS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("caqVccParamsEntry", ("caqvccparamsentry", CISCOATMQOSMIB.CaqVccParamsTable.CaqVccParamsEntry))])
            self._leafs = OrderedDict()

            self.caqvccparamsentry = YList(self)
            self._segment_path = lambda: "caqVccParamsTable"
            self._absolute_path = lambda: "CISCO-ATM-QOS-MIB:CISCO-ATM-QOS-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOATMQOSMIB.CaqVccParamsTable, [], name, value)


        class CaqVccParamsEntry(Entity):
            """
            This list contains the ATM QoS parameters provided by
            ciscoAtmQosVccEntry.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            	**config**\: False
            
            .. attribute:: atmvclvpi  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4095
            
            	**refers to**\:  :py:class:`atmvclvpi <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.AtmVclTable.AtmVclEntry>`
            
            	**config**\: False
            
            .. attribute:: atmvclvci  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..65535
            
            	**refers to**\:  :py:class:`atmvclvci <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.AtmVclTable.AtmVclEntry>`
            
            	**config**\: False
            
            .. attribute:: caqvccparamstype
            
            	The service category of this virtual circuit connection
            	**type**\:  :py:class:`AtmServiceCategory <ydk.models.cisco_ios_xe.ATM_FORUM_TC_MIB.AtmServiceCategory>`
            
            	**config**\: False
            
            .. attribute:: caqvccparamspcrin0
            
            	Input Peak Cell Rate (PCR) in kbps with  Cell Loss Priority bit set to 0 (clp0)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: caqvccparamspcrin01
            
            	Number of OAM F5 end to end loopback cells sent through the VCC
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: caqvccparamspcrout0
            
            	Output Peak Cell Rate (PCR) in kbps with Cell Loss Priority bit set to 0 (clp0)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: caqvccparamspcrout01
            
            	Output Peak Cell Rate (PCR) in kbps with Cell Loss Priority bit set to 1 (clp01)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: caqvccparamsscrin0
            
            	Input Sustained Cell Rate (SCR) in kbps for connection with VBR type of QoS and Cell Loss Priority bit set to 0 (clp0)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: caqvccparamsscrin01
            
            	Input Sustained Cell Rate (SCR) in kbps for connection with VBR type of QoS and Cell Loss Priority bit set to 1 (clp01)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: caqvccparamsscrout0
            
            	Output Sustained Cell Rate (SCR) in kbps for connection with VBR type of QoS and Cell Loss Priority bit set to 0 (clp0)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: caqvccparamsscrout01
            
            	Output Sustained Cell Rate (SCR) in kbps for connection with VBR type of QoS and Cell Loss Priority bit set to 1 (clp01)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: caqvccparamsbcsin0
            
            	Input Burst Cell Size (BCS) for connection with VBR type of QoS and Cell Loss Priority bit set to 0 (clp0)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: caqvccparamsbcsin01
            
            	Input Burst Cell Size (BCS) for connection with VBR type of QoS and Cell Loss Priority bit set to 1 (clp01)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: caqvccparamsbcsout0
            
            	Output Burst Cell Size (BCS) for connection with VBR type of QoS and  Cell Loss Priority bit set to 0 (clp0)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: caqvccparamsbcsout01
            
            	Output Burst Cell Size (BCS) for connection with VBR type of QoS and Cell Loss Priority bit set to 1 (clp01)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: caqvccparamsinheritlevel
            
            	The source of configuration for peak cell rate
            	**type**\:  :py:class:`VcParamConfigLocation <ydk.models.cisco_ios_xe.CISCO_ATM_QOS_MIB.VcParamConfigLocation>`
            
            	**config**\: False
            
            .. attribute:: caqvccparamsmcrin
            
            	Input Minimum Cell Rate (MCR) in kbps for connection with VBR\-nrt or ABR type of QoS
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: caqvccparamsmcrout
            
            	Output Minimum Cell Rate (MCR) in kbps for connection with VBR\-nrt or ABR type of QoS
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: caqvccparamsinvrdf
            
            	Inverse of rate decrease factor
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: caqvccparamsinvrif
            
            	Inverse of rate increase factor
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: caqvccparamsrfl
            
            	The source of configuration for rate factor
            	**type**\:  :py:class:`VcParamConfigLocation <ydk.models.cisco_ios_xe.CISCO_ATM_QOS_MIB.VcParamConfigLocation>`
            
            	**config**\: False
            
            .. attribute:: caqvccparamscdv
            
            	Cell delay variation
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: caqvccparamscdvt
            
            	Cell delay variation tolerance
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: caqvccparamsicr
            
            	Initial cell rate
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: caqvccparamstbe
            
            	Transient buffer exposure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: caqvccparamsfrtt
            
            	Fixed round\-trip time
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: caqvccparamsnrm
            
            	Maximum number of tx cells for each forward rm cell
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: caqvccparamsinvtrm
            
            	Maximum time between forward rm cells
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: caqvccparamsinvcdf
            
            	Inverse of cutoff decrease factor
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: caqvccparamsadtf
            
            	Allowed cell rate decrease time factor
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-ATM-QOS-MIB'
            _revision = '2002-06-10'

            def __init__(self):
                super(CISCOATMQOSMIB.CaqVccParamsTable.CaqVccParamsEntry, self).__init__()

                self.yang_name = "caqVccParamsEntry"
                self.yang_parent_name = "caqVccParamsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','atmvclvpi','atmvclvci']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('atmvclvpi', (YLeaf(YType.str, 'atmVclVpi'), ['int'])),
                    ('atmvclvci', (YLeaf(YType.str, 'atmVclVci'), ['int'])),
                    ('caqvccparamstype', (YLeaf(YType.enumeration, 'caqVccParamsType'), [('ydk.models.cisco_ios_xe.ATM_FORUM_TC_MIB', 'AtmServiceCategory', '')])),
                    ('caqvccparamspcrin0', (YLeaf(YType.uint32, 'caqVccParamsPcrIn0'), ['int'])),
                    ('caqvccparamspcrin01', (YLeaf(YType.uint32, 'caqVccParamsPcrIn01'), ['int'])),
                    ('caqvccparamspcrout0', (YLeaf(YType.uint32, 'caqVccParamsPcrOut0'), ['int'])),
                    ('caqvccparamspcrout01', (YLeaf(YType.uint32, 'caqVccParamsPcrOut01'), ['int'])),
                    ('caqvccparamsscrin0', (YLeaf(YType.uint32, 'caqVccParamsScrIn0'), ['int'])),
                    ('caqvccparamsscrin01', (YLeaf(YType.uint32, 'caqVccParamsScrIn01'), ['int'])),
                    ('caqvccparamsscrout0', (YLeaf(YType.uint32, 'caqVccParamsScrOut0'), ['int'])),
                    ('caqvccparamsscrout01', (YLeaf(YType.uint32, 'caqVccParamsScrOut01'), ['int'])),
                    ('caqvccparamsbcsin0', (YLeaf(YType.uint32, 'caqVccParamsBcsIn0'), ['int'])),
                    ('caqvccparamsbcsin01', (YLeaf(YType.uint32, 'caqVccParamsBcsIn01'), ['int'])),
                    ('caqvccparamsbcsout0', (YLeaf(YType.uint32, 'caqVccParamsBcsOut0'), ['int'])),
                    ('caqvccparamsbcsout01', (YLeaf(YType.uint32, 'caqVccParamsBcsOut01'), ['int'])),
                    ('caqvccparamsinheritlevel', (YLeaf(YType.enumeration, 'caqVccParamsInheritLevel'), [('ydk.models.cisco_ios_xe.CISCO_ATM_QOS_MIB', 'VcParamConfigLocation', '')])),
                    ('caqvccparamsmcrin', (YLeaf(YType.uint32, 'caqVccParamsMcrIn'), ['int'])),
                    ('caqvccparamsmcrout', (YLeaf(YType.uint32, 'caqVccParamsMcrOut'), ['int'])),
                    ('caqvccparamsinvrdf', (YLeaf(YType.uint32, 'caqVccParamsInvRdf'), ['int'])),
                    ('caqvccparamsinvrif', (YLeaf(YType.uint32, 'caqVccParamsInvRif'), ['int'])),
                    ('caqvccparamsrfl', (YLeaf(YType.enumeration, 'caqVccParamsRfl'), [('ydk.models.cisco_ios_xe.CISCO_ATM_QOS_MIB', 'VcParamConfigLocation', '')])),
                    ('caqvccparamscdv', (YLeaf(YType.uint32, 'caqVccParamsCdv'), ['int'])),
                    ('caqvccparamscdvt', (YLeaf(YType.uint32, 'caqVccParamsCdvt'), ['int'])),
                    ('caqvccparamsicr', (YLeaf(YType.uint32, 'caqVccParamsIcr'), ['int'])),
                    ('caqvccparamstbe', (YLeaf(YType.uint32, 'caqVccParamsTbe'), ['int'])),
                    ('caqvccparamsfrtt', (YLeaf(YType.uint32, 'caqVccParamsFrtt'), ['int'])),
                    ('caqvccparamsnrm', (YLeaf(YType.uint32, 'caqVccParamsNrm'), ['int'])),
                    ('caqvccparamsinvtrm', (YLeaf(YType.uint32, 'caqVccParamsInvTrm'), ['int'])),
                    ('caqvccparamsinvcdf', (YLeaf(YType.uint32, 'caqVccParamsInvCdf'), ['int'])),
                    ('caqvccparamsadtf', (YLeaf(YType.uint32, 'caqVccParamsAdtf'), ['int'])),
                ])
                self.ifindex = None
                self.atmvclvpi = None
                self.atmvclvci = None
                self.caqvccparamstype = None
                self.caqvccparamspcrin0 = None
                self.caqvccparamspcrin01 = None
                self.caqvccparamspcrout0 = None
                self.caqvccparamspcrout01 = None
                self.caqvccparamsscrin0 = None
                self.caqvccparamsscrin01 = None
                self.caqvccparamsscrout0 = None
                self.caqvccparamsscrout01 = None
                self.caqvccparamsbcsin0 = None
                self.caqvccparamsbcsin01 = None
                self.caqvccparamsbcsout0 = None
                self.caqvccparamsbcsout01 = None
                self.caqvccparamsinheritlevel = None
                self.caqvccparamsmcrin = None
                self.caqvccparamsmcrout = None
                self.caqvccparamsinvrdf = None
                self.caqvccparamsinvrif = None
                self.caqvccparamsrfl = None
                self.caqvccparamscdv = None
                self.caqvccparamscdvt = None
                self.caqvccparamsicr = None
                self.caqvccparamstbe = None
                self.caqvccparamsfrtt = None
                self.caqvccparamsnrm = None
                self.caqvccparamsinvtrm = None
                self.caqvccparamsinvcdf = None
                self.caqvccparamsadtf = None
                self._segment_path = lambda: "caqVccParamsEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[atmVclVpi='" + str(self.atmvclvpi) + "']" + "[atmVclVci='" + str(self.atmvclvci) + "']"
                self._absolute_path = lambda: "CISCO-ATM-QOS-MIB:CISCO-ATM-QOS-MIB/caqVccParamsTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOATMQOSMIB.CaqVccParamsTable.CaqVccParamsEntry, ['ifindex', 'atmvclvpi', 'atmvclvci', 'caqvccparamstype', 'caqvccparamspcrin0', 'caqvccparamspcrin01', 'caqvccparamspcrout0', 'caqvccparamspcrout01', 'caqvccparamsscrin0', 'caqvccparamsscrin01', 'caqvccparamsscrout0', 'caqvccparamsscrout01', 'caqvccparamsbcsin0', 'caqvccparamsbcsin01', 'caqvccparamsbcsout0', 'caqvccparamsbcsout01', 'caqvccparamsinheritlevel', 'caqvccparamsmcrin', 'caqvccparamsmcrout', 'caqvccparamsinvrdf', 'caqvccparamsinvrif', 'caqvccparamsrfl', 'caqvccparamscdv', 'caqvccparamscdvt', 'caqvccparamsicr', 'caqvccparamstbe', 'caqvccparamsfrtt', 'caqvccparamsnrm', 'caqvccparamsinvtrm', 'caqvccparamsinvcdf', 'caqvccparamsadtf'], name, value)




    class CaqVpcParamsTable(Entity):
        """
        This table is defined to provide QoS information for
        each active ATM VP existing on the interface.
        
        .. attribute:: caqvpcparamsentry
        
        	This list contains the ATM QoS parameters provided by ciscoAtmQosVpcEntry
        	**type**\: list of  		 :py:class:`CaqVpcParamsEntry <ydk.models.cisco_ios_xe.CISCO_ATM_QOS_MIB.CISCOATMQOSMIB.CaqVpcParamsTable.CaqVpcParamsEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-ATM-QOS-MIB'
        _revision = '2002-06-10'

        def __init__(self):
            super(CISCOATMQOSMIB.CaqVpcParamsTable, self).__init__()

            self.yang_name = "caqVpcParamsTable"
            self.yang_parent_name = "CISCO-ATM-QOS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("caqVpcParamsEntry", ("caqvpcparamsentry", CISCOATMQOSMIB.CaqVpcParamsTable.CaqVpcParamsEntry))])
            self._leafs = OrderedDict()

            self.caqvpcparamsentry = YList(self)
            self._segment_path = lambda: "caqVpcParamsTable"
            self._absolute_path = lambda: "CISCO-ATM-QOS-MIB:CISCO-ATM-QOS-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOATMQOSMIB.CaqVpcParamsTable, [], name, value)


        class CaqVpcParamsEntry(Entity):
            """
            This list contains the ATM QoS parameters provided by
            ciscoAtmQosVpcEntry.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            	**config**\: False
            
            .. attribute:: atmvplvpi  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4095
            
            	**refers to**\:  :py:class:`atmvplvpi <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.AtmVplTable.AtmVplEntry>`
            
            	**config**\: False
            
            .. attribute:: caqvpcparamsvpstate
            
            	VP state of the current permanent virtual path
            	**type**\:  :py:class:`VpState <ydk.models.cisco_ios_xe.CISCO_ATM_QOS_MIB.VpState>`
            
            	**config**\: False
            
            .. attribute:: caqvpcparamspeakrate
            
            	Maximum rate in kbps at which the associated permanent virtual path can transmit data
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: caqvpcparamscesrate
            
            	Maximum rate in kbps at which CES VCs can transmit data with the associated permanent virtual path
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: caqvpcparamsdatavccount
            
            	Number of data VCs currently associated with the permanent virtual path
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: caqvpcparamscesvccount
            
            	Number of CES VCs currently associated with the permanent virtual path
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: caqvpcparamsvcdf4seg
            
            	Vcd for F4 OAM segment processing
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: caqvpcparamsvcdf4ete
            
            	Vcd for F4 OAM end to end processing
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: caqvpcparamsscr
            
            	Sustained cell rate associated with the PVP
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: caqvpcparamsmbs
            
            	Maximum burst size associated with the PVP
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: caqvpcparamsavailbw
            
            	Bandwidth in Kbps currently currently available on this PVP
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-ATM-QOS-MIB'
            _revision = '2002-06-10'

            def __init__(self):
                super(CISCOATMQOSMIB.CaqVpcParamsTable.CaqVpcParamsEntry, self).__init__()

                self.yang_name = "caqVpcParamsEntry"
                self.yang_parent_name = "caqVpcParamsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','atmvplvpi']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('atmvplvpi', (YLeaf(YType.str, 'atmVplVpi'), ['int'])),
                    ('caqvpcparamsvpstate', (YLeaf(YType.enumeration, 'caqVpcParamsVpState'), [('ydk.models.cisco_ios_xe.CISCO_ATM_QOS_MIB', 'VpState', '')])),
                    ('caqvpcparamspeakrate', (YLeaf(YType.uint32, 'caqVpcParamsPeakRate'), ['int'])),
                    ('caqvpcparamscesrate', (YLeaf(YType.uint32, 'caqVpcParamsCesRate'), ['int'])),
                    ('caqvpcparamsdatavccount', (YLeaf(YType.int32, 'caqVpcParamsDataVcCount'), ['int'])),
                    ('caqvpcparamscesvccount', (YLeaf(YType.int32, 'caqVpcParamsCesVcCount'), ['int'])),
                    ('caqvpcparamsvcdf4seg', (YLeaf(YType.int32, 'caqVpcParamsVcdF4Seg'), ['int'])),
                    ('caqvpcparamsvcdf4ete', (YLeaf(YType.int32, 'caqVpcParamsVcdF4Ete'), ['int'])),
                    ('caqvpcparamsscr', (YLeaf(YType.uint32, 'caqVpcParamsScr'), ['int'])),
                    ('caqvpcparamsmbs', (YLeaf(YType.uint32, 'caqVpcParamsMbs'), ['int'])),
                    ('caqvpcparamsavailbw', (YLeaf(YType.uint32, 'caqVpcParamsAvailBw'), ['int'])),
                ])
                self.ifindex = None
                self.atmvplvpi = None
                self.caqvpcparamsvpstate = None
                self.caqvpcparamspeakrate = None
                self.caqvpcparamscesrate = None
                self.caqvpcparamsdatavccount = None
                self.caqvpcparamscesvccount = None
                self.caqvpcparamsvcdf4seg = None
                self.caqvpcparamsvcdf4ete = None
                self.caqvpcparamsscr = None
                self.caqvpcparamsmbs = None
                self.caqvpcparamsavailbw = None
                self._segment_path = lambda: "caqVpcParamsEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[atmVplVpi='" + str(self.atmvplvpi) + "']"
                self._absolute_path = lambda: "CISCO-ATM-QOS-MIB:CISCO-ATM-QOS-MIB/caqVpcParamsTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOATMQOSMIB.CaqVpcParamsTable.CaqVpcParamsEntry, ['ifindex', 'atmvplvpi', 'caqvpcparamsvpstate', 'caqvpcparamspeakrate', 'caqvpcparamscesrate', 'caqvpcparamsdatavccount', 'caqvpcparamscesvccount', 'caqvpcparamsvcdf4seg', 'caqvpcparamsvcdf4ete', 'caqvpcparamsscr', 'caqvpcparamsmbs', 'caqvpcparamsavailbw'], name, value)




    class CaqQueuingParamsTable(Entity):
        """
        This table provides queuing related information
        for a VC existing on an ATM interface.
        
        .. attribute:: caqqueuingparamsentry
        
        	This is defined as an entry in caqQueuingParamsTable
        	**type**\: list of  		 :py:class:`CaqQueuingParamsEntry <ydk.models.cisco_ios_xe.CISCO_ATM_QOS_MIB.CISCOATMQOSMIB.CaqQueuingParamsTable.CaqQueuingParamsEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-ATM-QOS-MIB'
        _revision = '2002-06-10'

        def __init__(self):
            super(CISCOATMQOSMIB.CaqQueuingParamsTable, self).__init__()

            self.yang_name = "caqQueuingParamsTable"
            self.yang_parent_name = "CISCO-ATM-QOS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("caqQueuingParamsEntry", ("caqqueuingparamsentry", CISCOATMQOSMIB.CaqQueuingParamsTable.CaqQueuingParamsEntry))])
            self._leafs = OrderedDict()

            self.caqqueuingparamsentry = YList(self)
            self._segment_path = lambda: "caqQueuingParamsTable"
            self._absolute_path = lambda: "CISCO-ATM-QOS-MIB:CISCO-ATM-QOS-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOATMQOSMIB.CaqQueuingParamsTable, [], name, value)


        class CaqQueuingParamsEntry(Entity):
            """
            This is defined as an entry in caqQueuingParamsTable.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            	**config**\: False
            
            .. attribute:: atmvclvpi  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4095
            
            	**refers to**\:  :py:class:`atmvclvpi <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.AtmVclTable.AtmVclEntry>`
            
            	**config**\: False
            
            .. attribute:: atmvclvci  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..65535
            
            	**refers to**\:  :py:class:`atmvclvci <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.AtmVclTable.AtmVclEntry>`
            
            	**config**\: False
            
            .. attribute:: caqqueuingparamsmeanqdepth
            
            	Mean Queue Depth associated with the vc.  This value is calculated based on the actual queue depth on the interface and the exponential weighting constant
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-ATM-QOS-MIB'
            _revision = '2002-06-10'

            def __init__(self):
                super(CISCOATMQOSMIB.CaqQueuingParamsTable.CaqQueuingParamsEntry, self).__init__()

                self.yang_name = "caqQueuingParamsEntry"
                self.yang_parent_name = "caqQueuingParamsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','atmvclvpi','atmvclvci']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('atmvclvpi', (YLeaf(YType.str, 'atmVclVpi'), ['int'])),
                    ('atmvclvci', (YLeaf(YType.str, 'atmVclVci'), ['int'])),
                    ('caqqueuingparamsmeanqdepth', (YLeaf(YType.uint32, 'caqQueuingParamsMeanQDepth'), ['int'])),
                ])
                self.ifindex = None
                self.atmvclvpi = None
                self.atmvclvci = None
                self.caqqueuingparamsmeanqdepth = None
                self._segment_path = lambda: "caqQueuingParamsEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[atmVclVpi='" + str(self.atmvclvpi) + "']" + "[atmVclVci='" + str(self.atmvclvci) + "']"
                self._absolute_path = lambda: "CISCO-ATM-QOS-MIB:CISCO-ATM-QOS-MIB/caqQueuingParamsTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOATMQOSMIB.CaqQueuingParamsTable.CaqQueuingParamsEntry, ['ifindex', 'atmvclvpi', 'atmvclvci', 'caqqueuingparamsmeanqdepth'], name, value)




    class CaqQueuingParamsClassTable(Entity):
        """
        This table provides queuing information for all 
        queuing classes associating with a VC.
        
        .. attribute:: caqqueuingparamsclassentry
        
        	This is defined as an entry in ciscoAtmQosVcQueuingClassTable to provide queuing information of a specific class
        	**type**\: list of  		 :py:class:`CaqQueuingParamsClassEntry <ydk.models.cisco_ios_xe.CISCO_ATM_QOS_MIB.CISCOATMQOSMIB.CaqQueuingParamsClassTable.CaqQueuingParamsClassEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-ATM-QOS-MIB'
        _revision = '2002-06-10'

        def __init__(self):
            super(CISCOATMQOSMIB.CaqQueuingParamsClassTable, self).__init__()

            self.yang_name = "caqQueuingParamsClassTable"
            self.yang_parent_name = "CISCO-ATM-QOS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("caqQueuingParamsClassEntry", ("caqqueuingparamsclassentry", CISCOATMQOSMIB.CaqQueuingParamsClassTable.CaqQueuingParamsClassEntry))])
            self._leafs = OrderedDict()

            self.caqqueuingparamsclassentry = YList(self)
            self._segment_path = lambda: "caqQueuingParamsClassTable"
            self._absolute_path = lambda: "CISCO-ATM-QOS-MIB:CISCO-ATM-QOS-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOATMQOSMIB.CaqQueuingParamsClassTable, [], name, value)


        class CaqQueuingParamsClassEntry(Entity):
            """
            This is defined as an entry in ciscoAtmQosVcQueuingClassTable
            to provide queuing information of a specific class.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            	**config**\: False
            
            .. attribute:: atmvclvpi  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4095
            
            	**refers to**\:  :py:class:`atmvclvpi <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.AtmVclTable.AtmVclEntry>`
            
            	**config**\: False
            
            .. attribute:: atmvclvci  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..65535
            
            	**refers to**\:  :py:class:`atmvclvci <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.AtmVclTable.AtmVclEntry>`
            
            	**config**\: False
            
            .. attribute:: caqqueuingparamsclassindex  (key)
            
            	A class index, which associates with an IP precedence (0 to 8), is defined to reference individual caqQueuingParamsClassEntry
            	**type**\: int
            
            	**range:** 0..8
            
            	**config**\: False
            
            .. attribute:: caqqueuingparamsclassranddrp
            
            	Number of packets dropped when Mean Queue Length is between Minimum Threshold and Maximum Threshold range
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: caqqueuingparamsclasstaildrp
            
            	Number of packets dropped because the Mean Queue Depth exceeds the Maximum Threshold value
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: caqqueuingparamsclassminthre
            
            	Minimum Threshold value in kbps
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: caqqueuingparamsclassmaxthre
            
            	Maximum Threshold value in kbps
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: caqqueuingparamsclassmrkprob
            
            	Mark probability denominator.  This is the value used in the calculation of a packet being dropped when the average queue size is between the minimum threshold and the maximum threshold
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-ATM-QOS-MIB'
            _revision = '2002-06-10'

            def __init__(self):
                super(CISCOATMQOSMIB.CaqQueuingParamsClassTable.CaqQueuingParamsClassEntry, self).__init__()

                self.yang_name = "caqQueuingParamsClassEntry"
                self.yang_parent_name = "caqQueuingParamsClassTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','atmvclvpi','atmvclvci','caqqueuingparamsclassindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('atmvclvpi', (YLeaf(YType.str, 'atmVclVpi'), ['int'])),
                    ('atmvclvci', (YLeaf(YType.str, 'atmVclVci'), ['int'])),
                    ('caqqueuingparamsclassindex', (YLeaf(YType.int32, 'caqQueuingParamsClassIndex'), ['int'])),
                    ('caqqueuingparamsclassranddrp', (YLeaf(YType.uint32, 'caqQueuingParamsClassRandDrp'), ['int'])),
                    ('caqqueuingparamsclasstaildrp', (YLeaf(YType.uint32, 'caqQueuingParamsClassTailDrp'), ['int'])),
                    ('caqqueuingparamsclassminthre', (YLeaf(YType.uint32, 'caqQueuingParamsClassMinThre'), ['int'])),
                    ('caqqueuingparamsclassmaxthre', (YLeaf(YType.uint32, 'caqQueuingParamsClassMaxThre'), ['int'])),
                    ('caqqueuingparamsclassmrkprob', (YLeaf(YType.uint32, 'caqQueuingParamsClassMrkProb'), ['int'])),
                ])
                self.ifindex = None
                self.atmvclvpi = None
                self.atmvclvci = None
                self.caqqueuingparamsclassindex = None
                self.caqqueuingparamsclassranddrp = None
                self.caqqueuingparamsclasstaildrp = None
                self.caqqueuingparamsclassminthre = None
                self.caqqueuingparamsclassmaxthre = None
                self.caqqueuingparamsclassmrkprob = None
                self._segment_path = lambda: "caqQueuingParamsClassEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[atmVclVpi='" + str(self.atmvclvpi) + "']" + "[atmVclVci='" + str(self.atmvclvci) + "']" + "[caqQueuingParamsClassIndex='" + str(self.caqqueuingparamsclassindex) + "']"
                self._absolute_path = lambda: "CISCO-ATM-QOS-MIB:CISCO-ATM-QOS-MIB/caqQueuingParamsClassTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOATMQOSMIB.CaqQueuingParamsClassTable.CaqQueuingParamsClassEntry, ['ifindex', 'atmvclvpi', 'atmvclvci', 'caqqueuingparamsclassindex', 'caqqueuingparamsclassranddrp', 'caqqueuingparamsclasstaildrp', 'caqqueuingparamsclassminthre', 'caqqueuingparamsclassmaxthre', 'caqqueuingparamsclassmrkprob'], name, value)



    def clone_ptr(self):
        self._top_entity = CISCOATMQOSMIB()
        return self._top_entity



