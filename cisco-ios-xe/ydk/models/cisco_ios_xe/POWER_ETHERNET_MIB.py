""" POWER_ETHERNET_MIB 

The MIB module for managing Power Source Equipment
(PSE) working according to the IEEE 802.af Powered
Ethernet (DTE Power via MDI) standard.

 The following terms are used throughout this
 MIB module.  For complete formal definitions,
 the IEEE 802.3 standards should be consulted
 wherever possible\:

 Group \- A recommended, but optional, entity
 defined by the IEEE 802.3 management standard,
 in order to support a modular numbering scheme.
 The classical example allows an implementor to
 represent field\-replaceable units as groups of
 ports, with the port numbering matching the
 modular hardware implementation.

Port \- This entity identifies the port within the group
for which this entry contains information.  The numbering
scheme for ports is implementation specific.

Copyright (c) The Internet Society (2003).  This version
of this MIB module is part of RFC 3621; See the RFC
itself for full legal notices.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class POWERETHERNETMIB(Entity):
    """
    
    
    .. attribute:: pethpseporttable
    
    	A table of objects that display and control the power characteristics of power Ethernet ports on a Power Source Entity (PSE) device.  This group will be implemented in managed power Ethernet switches and mid\-span devices. Values of all read\-write objects in this table are persistent at restart/reboot
    	**type**\:  :py:class:`PethPsePortTable <ydk.models.cisco_ios_xe.POWER_ETHERNET_MIB.POWERETHERNETMIB.PethPsePortTable>`
    
    .. attribute:: pethmainpsetable
    
    	A table of objects that display and control attributes of the main power source in a PSE  device.  Ethernet switches are one example of boxes that would support these objects. Values of all read\-write objects in this table are persistent at restart/reboot
    	**type**\:  :py:class:`PethMainPseTable <ydk.models.cisco_ios_xe.POWER_ETHERNET_MIB.POWERETHERNETMIB.PethMainPseTable>`
    
    .. attribute:: pethnotificationcontroltable
    
    	A table of objects that display and control the Notification on a PSE  device. Values of all read\-write objects in this table are persistent at restart/reboot
    	**type**\:  :py:class:`PethNotificationControlTable <ydk.models.cisco_ios_xe.POWER_ETHERNET_MIB.POWERETHERNETMIB.PethNotificationControlTable>`
    
    

    """

    _prefix = 'POWER-ETHERNET-MIB'
    _revision = '2003-11-24'

    def __init__(self):
        super(POWERETHERNETMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "POWER-ETHERNET-MIB"
        self.yang_parent_name = "POWER-ETHERNET-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("pethPsePortTable", ("pethpseporttable", POWERETHERNETMIB.PethPsePortTable)), ("pethMainPseTable", ("pethmainpsetable", POWERETHERNETMIB.PethMainPseTable)), ("pethNotificationControlTable", ("pethnotificationcontroltable", POWERETHERNETMIB.PethNotificationControlTable))])
        self._leafs = OrderedDict()

        self.pethpseporttable = POWERETHERNETMIB.PethPsePortTable()
        self.pethpseporttable.parent = self
        self._children_name_map["pethpseporttable"] = "pethPsePortTable"

        self.pethmainpsetable = POWERETHERNETMIB.PethMainPseTable()
        self.pethmainpsetable.parent = self
        self._children_name_map["pethmainpsetable"] = "pethMainPseTable"

        self.pethnotificationcontroltable = POWERETHERNETMIB.PethNotificationControlTable()
        self.pethnotificationcontroltable.parent = self
        self._children_name_map["pethnotificationcontroltable"] = "pethNotificationControlTable"
        self._segment_path = lambda: "POWER-ETHERNET-MIB:POWER-ETHERNET-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(POWERETHERNETMIB, [], name, value)


    class PethPsePortTable(Entity):
        """
        A table of objects that display and control the power
        characteristics of power Ethernet ports on a Power Source
        Entity (PSE) device.  This group will be implemented in
        managed power Ethernet switches and mid\-span devices.
        Values of all read\-write objects in this table are
        persistent at restart/reboot.
        
        .. attribute:: pethpseportentry
        
        	A set of objects that display and control the power characteristics of a power Ethernet PSE port
        	**type**\: list of  		 :py:class:`PethPsePortEntry <ydk.models.cisco_ios_xe.POWER_ETHERNET_MIB.POWERETHERNETMIB.PethPsePortTable.PethPsePortEntry>`
        
        

        """

        _prefix = 'POWER-ETHERNET-MIB'
        _revision = '2003-11-24'

        def __init__(self):
            super(POWERETHERNETMIB.PethPsePortTable, self).__init__()

            self.yang_name = "pethPsePortTable"
            self.yang_parent_name = "POWER-ETHERNET-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("pethPsePortEntry", ("pethpseportentry", POWERETHERNETMIB.PethPsePortTable.PethPsePortEntry))])
            self._leafs = OrderedDict()

            self.pethpseportentry = YList(self)
            self._segment_path = lambda: "pethPsePortTable"
            self._absolute_path = lambda: "POWER-ETHERNET-MIB:POWER-ETHERNET-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(POWERETHERNETMIB.PethPsePortTable, [], name, value)


        class PethPsePortEntry(Entity):
            """
            A set of objects that display and control the power
            characteristics of a power Ethernet PSE port.
            
            .. attribute:: pethpseportgroupindex  (key)
            
            	This variable uniquely identifies the group containing the port to which a power Ethernet PSE is connected.  Group means box in the stack, module in a rack and the value 1 MUST be used for non\-modular devices. Furthermore, the same value MUST be used in this variable, pethMainPseGroupIndex, and pethNotificationControlGroupIndex to refer to a given box in a stack or module in the rack
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: pethpseportindex  (key)
            
            	This variable uniquely identifies the power Ethernet PSE port within group pethPsePortGroupIndex to which the power Ethernet PSE entry is connected
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: pethpseportadminenable
            
            	true (1) An interface which can provide the PSE functions. false(2) The interface will act as it would if it had no PSE function
            	**type**\: bool
            
            .. attribute:: pethpseportpowerpairscontrolability
            
            	Describes the capability of controlling the power pairs functionality to switch pins for sourcing power. The value true indicate that the device has the capability to control the power pairs.  When false the PSE Pinout Alternative used cannot be controlled through the PethPsePortAdminEnable attribute
            	**type**\: bool
            
            .. attribute:: pethpseportpowerpairs
            
            	Describes or controls the pairs in use.  If the value of pethPsePortPowerPairsControl is true, this object is writable. A value of signal(1) means that the signal pairs only are in use. A value of spare(2) means that the spare pairs only are in use
            	**type**\:  :py:class:`PethPsePortPowerPairs <ydk.models.cisco_ios_xe.POWER_ETHERNET_MIB.POWERETHERNETMIB.PethPsePortTable.PethPsePortEntry.PethPsePortPowerPairs>`
            
            .. attribute:: pethpseportdetectionstatus
            
            	Describes the operational status of the port PD detection. A value of disabled(1)\- indicates that the PSE State diagram is in the state DISABLED. A value of deliveringPower(3) \- indicates that the PSE State diagram is in the state POWER\_ON for a duration greater than tlim max (see IEEE Std 802.3af Table 33\-5 tlim). A value of fault(4) \- indicates that the PSE State diagram is in the state TEST\_ERROR. A value of test(5) \- indicates that the PSE State diagram is in the state TEST\_MODE. A value of otherFault(6) \- indicates that the PSE State diagram is in the state IDLE due to the variable error\_conditions. A value of searching(2)\- indicates the PSE State diagram is in a state other than those listed above
            	**type**\:  :py:class:`PethPsePortDetectionStatus <ydk.models.cisco_ios_xe.POWER_ETHERNET_MIB.POWERETHERNETMIB.PethPsePortTable.PethPsePortEntry.PethPsePortDetectionStatus>`
            
            .. attribute:: pethpseportpowerpriority
            
            	This object controls the priority of the port from the point of view of a power management algorithm.  The priority that is set by this variable could be used by a control mechanism that prevents over current situations by disconnecting first ports with lower power priority.  Ports that connect devices critical to the operation of the network \- like the E911 telephones ports \- should be set to higher priority
            	**type**\:  :py:class:`PethPsePortPowerPriority <ydk.models.cisco_ios_xe.POWER_ETHERNET_MIB.POWERETHERNETMIB.PethPsePortTable.PethPsePortEntry.PethPsePortPowerPriority>`
            
            .. attribute:: pethpseportmpsabsentcounter
            
            	This counter is incremented when the PSE state diagram transitions directly from the state POWER\_ON to the state IDLE due to tmpdo\_timer\_done being asserted
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: pethpseporttype
            
            	A manager will set the value of this variable to indicate the type of powered device that is connected to the port. The default value supplied by the agent if no value has ever been set should be a zero\-length octet string
            	**type**\: str
            
            .. attribute:: pethpseportpowerclassifications
            
            	Classification is a way to tag different terminals on the Power over LAN network according to their power consumption. Devices such as IP telephones, WLAN access points and others, will be classified according to their power requirements.  The meaning of the classification labels is defined in the IEEE specification.  This variable is valid only while a PD is being powered, that is, while the attribute pethPsePortDetectionStatus is reporting the enumeration deliveringPower
            	**type**\:  :py:class:`PethPsePortPowerClassifications <ydk.models.cisco_ios_xe.POWER_ETHERNET_MIB.POWERETHERNETMIB.PethPsePortTable.PethPsePortEntry.PethPsePortPowerClassifications>`
            
            .. attribute:: pethpseportinvalidsignaturecounter
            
            	This counter is incremented when the PSE state diagram enters the state SIGNATURE\_INVALID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: pethpseportpowerdeniedcounter
            
            	This counter is incremented when the PSE state diagram enters the state POWER\_DENIED
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: pethpseportoverloadcounter
            
            	This counter is incremented when the PSE state diagram enters the state ERROR\_DELAY\_OVER
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: pethpseportshortcounter
            
            	This counter is incremented when the PSE state diagram enters the state ERROR\_DELAY\_SHORT
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpeextpseportenable
            
            	This object is an extension of the pethPsePortAdminEnable object from RFC3621. It allows the user to be more specific when enabling the PSE functions. The states, 'auto', 'static' and 'limit' correspond to a value of 'true' for the pethPsePortAdminEnable object. The state 'disable' corresponds to a value of 'false' for the pethPsePortAdminEnable object.  Setting this value to 'auto' enables Powered Device discovery on the interface and the amount of power allocated depends on the Powered Device discovered. If pethPsePortAdminEnable was 'false' prior to this set operation, then it will become 'true'.  Setting this value to 'static' will also enable Powered Device discovery. However, this is different from 'auto' in that the amount of power is pre\-allocated based on the configuration on the Power Sourcing Equipment. If pethPsePortAdminEnable was 'false' prior to this set operation, then it will become 'true'.  Setting this value to 'limit' enables Powered Device discovery on the interface. The amount of power allocated depends on the Powered Device discovered and the value of cpeExtPsePortPwrMax. The lower value will be used. If pethPsePortAdminEnable was 'false' prior to this set operation, then it will become 'true'.  Setting this value to 'disable' disables the PSE functions. The pethPsePortAdminEnable object will adopt the value of 'false' if it was 'true' prior to this set operation. When setting the pethPsePortAdminEnable object to 'false' this object cpeExtPsePortEnable will adopt the value of 'disable'.  If cpeExtPsePortPolicingCapable of the PSE port, or cpeExtMainPsePwrMonitorCapable of the PSE port's main group, has the value of 'false', this object can only be set to 'auto', 'static' or 'disable'. Otherwise, this object can be set to 'auto', 'static', 'limit' or 'disable'
            	**type**\:  :py:class:`CpeExtPsePortEnable <ydk.models.cisco_ios_xe.POWER_ETHERNET_MIB.POWERETHERNETMIB.PethPsePortTable.PethPsePortEntry.CpeExtPsePortEnable>`
            
            .. attribute:: cpeextpseportdiscovermode
            
            	This object indicates the discover mode used by the system to discover the PD.  A value of 'unknown' indicates that the discover mode on the interface is unknown.  A value of 'off' indicates that discovery is disabled on the interface.  A value of 'ieee' indicates that the discover mode on the interface is IEEE based.  A value of 'cisco' indicates that the discover mode on the interface is Cisco based.  A value of 'ieeeAndCisco' indicates that the discover mode on the interface is both IEEE and Cisco based
            	**type**\:  :py:class:`CpeExtPsePortDiscoverMode <ydk.models.cisco_ios_xe.POWER_ETHERNET_MIB.POWERETHERNETMIB.PethPsePortTable.PethPsePortEntry.CpeExtPsePortDiscoverMode>`
            
            .. attribute:: cpeextpseportdevicedetected
            
            	This object indicates if a Powered Device (PD) has been detected on the interface.  A value of 'true' indicates that a PD has been detected on the interface.  A value of 'false' indicates that no PD has been detected on the interface
            	**type**\: bool
            
            .. attribute:: cpeextpseportieeepd
            
            	This object indicates whether the Powered Device attached to the interface is an IEEE compliant Powered Device or not.  A value of 'true' indicates the attached Powered Device is an IEEE compliant Powered Device.  A value of 'false' indicates the attached Powered Device is not an IEEE compliant Powered Device. This also means that the value of the corresponding object from the pethPsePortTable, pethPsePortPowerClassifications is irrelevant
            	**type**\: bool
            
            .. attribute:: cpeextpseportadditionalstatus
            
            	This object is an extension of the pethPsePortDetectionStatus object from RFC3621 and provides additional status information.  deny\: When set, the PD attached to the interface is being       denied power due to insufficient power resources on       the Power Sourcing Equipment.  overdraw\: When set, the PD attached to the interface is            being denied power because the PD is trying            to consume more power than it has been            configured to consume.  overdrawLog\: When set, the PD attached to the interface               is trying to consume more power than it has               been configured to consume, but is not being               denied power
            	**type**\:  :py:class:`CpeExtPsePortAdditionalStatus <ydk.models.cisco_ios_xe.POWER_ETHERNET_MIB.POWERETHERNETMIB.PethPsePortTable.PethPsePortEntry.CpeExtPsePortAdditionalStatus>`
            
            .. attribute:: cpeextpseportpwrmax
            
            	This indicates the maximum amount of power that the PSE will make available to the PD connected to this interface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: milliwatts
            
            .. attribute:: cpeextpseportpwrallocated
            
            	This object indicates the amount of power allocated from the PSE for the PD
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: milliwatts
            
            .. attribute:: cpeextpseportpwravailable
            
            	This object indicates the amount of power available for the PD to use. This value may differ from the value cpeExtPsePortPwrAllocated due to the efficiency issues of delivering the power from the PSE to the PD.  When sufficient power is available to power a PD, this value should be equal to the lower of the two objects, cpeExtDefaultAllocation and cpeExtPsePortPwrMax
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: milliwatts
            
            .. attribute:: cpeextpseportpwrconsumption
            
            	This indicates the actual power consumption of the PD connected to this interface. It may not necessarily be equal to the value of cpeExtPsePortPwrAvailable
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: milliwatts
            
            .. attribute:: cpeextpseportmaxpwrdrawn
            
            	This indicates the maximum amount of power drawn by the PD connected to this interface, since it was powered on
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: milliwatts
            
            .. attribute:: cpeextpseportentphyindex
            
            	The entPhysicalIndex value that uniquely identifies the PSE port. If the PSE port does not have a corresponding  physical entry in entPhysicalTable or if the  entPhysicalTable is not supported by the management system, this object has the value of zero
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: cpeextpseportpolicingcapable
            
            	This object indicates whether the PSE port hardware is capable of policing the port for proper power consumption  based on the allocated value
            	**type**\: bool
            
            .. attribute:: cpeextpseportpolicingenable
            
            	This object allows the user to turn on or turn off the power policing of the PSE port. If the instance value of  cpeExtPsePortPolicingCapable is 'TRUE', the user is allowed to set this object to 'on' or 'off'. Otherwise, this object is read\-only and always has the value of 'off'
            	**type**\:  :py:class:`CpeExtPsePortPolicingEnable <ydk.models.cisco_ios_xe.POWER_ETHERNET_MIB.POWERETHERNETMIB.PethPsePortTable.PethPsePortEntry.CpeExtPsePortPolicingEnable>`
            
            .. attribute:: cpeextpseportpolicingaction
            
            	This object specifies the power policing action that the device will take on this PSE port when the real\-time  power consumption exceeds its max power allocation if  the value of cpeExtPsePortPolicingEnable is 'on'.       'deny'          \- the device will deny the power to                         the PSE port       'logOnly'       \- the device will not deny the power                         to the PSE port
            	**type**\:  :py:class:`CpeExtPsePortPolicingAction <ydk.models.cisco_ios_xe.POWER_ETHERNET_MIB.POWERETHERNETMIB.PethPsePortTable.PethPsePortEntry.CpeExtPsePortPolicingAction>`
            
            .. attribute:: cpeextpseportpwrmanalloc
            
            	This object specifies the manual power allocation that the PSE will allocate to the PD connected to this  interface regardless of the amount requested via CDP  or IEEE.   Setting this object value to zero disables the manual  power allocation.   Warning\: Misconfiguring this manual power allocation may  cause damage to the system and void the warranty. Take  precautions not to oversubscribe the power supply
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: milliwatts
            
            .. attribute:: cpeextpseportcapabilities
            
            	This object indicates the PSE functionality that this port supports.  If the 'policing' BIT is set, then this PSE port is capable of policing the port for proper power consumption based on the allocated value.  If the 'poePlus' BIT is set, then this PSE port supports PoE Plus functions
            	**type**\:  :py:class:`CpeExtPsePortCapabilities <ydk.models.cisco_ios_xe.POWER_ETHERNET_MIB.POWERETHERNETMIB.PethPsePortTable.PethPsePortEntry.CpeExtPsePortCapabilities>`
            
            

            """

            _prefix = 'POWER-ETHERNET-MIB'
            _revision = '2003-11-24'

            def __init__(self):
                super(POWERETHERNETMIB.PethPsePortTable.PethPsePortEntry, self).__init__()

                self.yang_name = "pethPsePortEntry"
                self.yang_parent_name = "pethPsePortTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['pethpseportgroupindex','pethpseportindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('pethpseportgroupindex', (YLeaf(YType.int32, 'pethPsePortGroupIndex'), ['int'])),
                    ('pethpseportindex', (YLeaf(YType.int32, 'pethPsePortIndex'), ['int'])),
                    ('pethpseportadminenable', (YLeaf(YType.boolean, 'pethPsePortAdminEnable'), ['bool'])),
                    ('pethpseportpowerpairscontrolability', (YLeaf(YType.boolean, 'pethPsePortPowerPairsControlAbility'), ['bool'])),
                    ('pethpseportpowerpairs', (YLeaf(YType.enumeration, 'pethPsePortPowerPairs'), [('ydk.models.cisco_ios_xe.POWER_ETHERNET_MIB', 'POWERETHERNETMIB', 'PethPsePortTable.PethPsePortEntry.PethPsePortPowerPairs')])),
                    ('pethpseportdetectionstatus', (YLeaf(YType.enumeration, 'pethPsePortDetectionStatus'), [('ydk.models.cisco_ios_xe.POWER_ETHERNET_MIB', 'POWERETHERNETMIB', 'PethPsePortTable.PethPsePortEntry.PethPsePortDetectionStatus')])),
                    ('pethpseportpowerpriority', (YLeaf(YType.enumeration, 'pethPsePortPowerPriority'), [('ydk.models.cisco_ios_xe.POWER_ETHERNET_MIB', 'POWERETHERNETMIB', 'PethPsePortTable.PethPsePortEntry.PethPsePortPowerPriority')])),
                    ('pethpseportmpsabsentcounter', (YLeaf(YType.uint32, 'pethPsePortMPSAbsentCounter'), ['int'])),
                    ('pethpseporttype', (YLeaf(YType.str, 'pethPsePortType'), ['str'])),
                    ('pethpseportpowerclassifications', (YLeaf(YType.enumeration, 'pethPsePortPowerClassifications'), [('ydk.models.cisco_ios_xe.POWER_ETHERNET_MIB', 'POWERETHERNETMIB', 'PethPsePortTable.PethPsePortEntry.PethPsePortPowerClassifications')])),
                    ('pethpseportinvalidsignaturecounter', (YLeaf(YType.uint32, 'pethPsePortInvalidSignatureCounter'), ['int'])),
                    ('pethpseportpowerdeniedcounter', (YLeaf(YType.uint32, 'pethPsePortPowerDeniedCounter'), ['int'])),
                    ('pethpseportoverloadcounter', (YLeaf(YType.uint32, 'pethPsePortOverLoadCounter'), ['int'])),
                    ('pethpseportshortcounter', (YLeaf(YType.uint32, 'pethPsePortShortCounter'), ['int'])),
                    ('cpeextpseportenable', (YLeaf(YType.enumeration, 'CISCO-POWER-ETHERNET-EXT-MIB:cpeExtPsePortEnable'), [('ydk.models.cisco_ios_xe.POWER_ETHERNET_MIB', 'POWERETHERNETMIB', 'PethPsePortTable.PethPsePortEntry.CpeExtPsePortEnable')])),
                    ('cpeextpseportdiscovermode', (YLeaf(YType.enumeration, 'CISCO-POWER-ETHERNET-EXT-MIB:cpeExtPsePortDiscoverMode'), [('ydk.models.cisco_ios_xe.POWER_ETHERNET_MIB', 'POWERETHERNETMIB', 'PethPsePortTable.PethPsePortEntry.CpeExtPsePortDiscoverMode')])),
                    ('cpeextpseportdevicedetected', (YLeaf(YType.boolean, 'CISCO-POWER-ETHERNET-EXT-MIB:cpeExtPsePortDeviceDetected'), ['bool'])),
                    ('cpeextpseportieeepd', (YLeaf(YType.boolean, 'CISCO-POWER-ETHERNET-EXT-MIB:cpeExtPsePortIeeePd'), ['bool'])),
                    ('cpeextpseportadditionalstatus', (YLeaf(YType.bits, 'CISCO-POWER-ETHERNET-EXT-MIB:cpeExtPsePortAdditionalStatus'), ['Bits'])),
                    ('cpeextpseportpwrmax', (YLeaf(YType.uint32, 'CISCO-POWER-ETHERNET-EXT-MIB:cpeExtPsePortPwrMax'), ['int'])),
                    ('cpeextpseportpwrallocated', (YLeaf(YType.uint32, 'CISCO-POWER-ETHERNET-EXT-MIB:cpeExtPsePortPwrAllocated'), ['int'])),
                    ('cpeextpseportpwravailable', (YLeaf(YType.uint32, 'CISCO-POWER-ETHERNET-EXT-MIB:cpeExtPsePortPwrAvailable'), ['int'])),
                    ('cpeextpseportpwrconsumption', (YLeaf(YType.uint32, 'CISCO-POWER-ETHERNET-EXT-MIB:cpeExtPsePortPwrConsumption'), ['int'])),
                    ('cpeextpseportmaxpwrdrawn', (YLeaf(YType.uint32, 'CISCO-POWER-ETHERNET-EXT-MIB:cpeExtPsePortMaxPwrDrawn'), ['int'])),
                    ('cpeextpseportentphyindex', (YLeaf(YType.int32, 'CISCO-POWER-ETHERNET-EXT-MIB:cpeExtPsePortEntPhyIndex'), ['int'])),
                    ('cpeextpseportpolicingcapable', (YLeaf(YType.boolean, 'CISCO-POWER-ETHERNET-EXT-MIB:cpeExtPsePortPolicingCapable'), ['bool'])),
                    ('cpeextpseportpolicingenable', (YLeaf(YType.enumeration, 'CISCO-POWER-ETHERNET-EXT-MIB:cpeExtPsePortPolicingEnable'), [('ydk.models.cisco_ios_xe.POWER_ETHERNET_MIB', 'POWERETHERNETMIB', 'PethPsePortTable.PethPsePortEntry.CpeExtPsePortPolicingEnable')])),
                    ('cpeextpseportpolicingaction', (YLeaf(YType.enumeration, 'CISCO-POWER-ETHERNET-EXT-MIB:cpeExtPsePortPolicingAction'), [('ydk.models.cisco_ios_xe.POWER_ETHERNET_MIB', 'POWERETHERNETMIB', 'PethPsePortTable.PethPsePortEntry.CpeExtPsePortPolicingAction')])),
                    ('cpeextpseportpwrmanalloc', (YLeaf(YType.uint32, 'CISCO-POWER-ETHERNET-EXT-MIB:cpeExtPsePortPwrManAlloc'), ['int'])),
                    ('cpeextpseportcapabilities', (YLeaf(YType.bits, 'CISCO-POWER-ETHERNET-EXT-MIB:cpeExtPsePortCapabilities'), ['Bits'])),
                ])
                self.pethpseportgroupindex = None
                self.pethpseportindex = None
                self.pethpseportadminenable = None
                self.pethpseportpowerpairscontrolability = None
                self.pethpseportpowerpairs = None
                self.pethpseportdetectionstatus = None
                self.pethpseportpowerpriority = None
                self.pethpseportmpsabsentcounter = None
                self.pethpseporttype = None
                self.pethpseportpowerclassifications = None
                self.pethpseportinvalidsignaturecounter = None
                self.pethpseportpowerdeniedcounter = None
                self.pethpseportoverloadcounter = None
                self.pethpseportshortcounter = None
                self.cpeextpseportenable = None
                self.cpeextpseportdiscovermode = None
                self.cpeextpseportdevicedetected = None
                self.cpeextpseportieeepd = None
                self.cpeextpseportadditionalstatus = Bits()
                self.cpeextpseportpwrmax = None
                self.cpeextpseportpwrallocated = None
                self.cpeextpseportpwravailable = None
                self.cpeextpseportpwrconsumption = None
                self.cpeextpseportmaxpwrdrawn = None
                self.cpeextpseportentphyindex = None
                self.cpeextpseportpolicingcapable = None
                self.cpeextpseportpolicingenable = None
                self.cpeextpseportpolicingaction = None
                self.cpeextpseportpwrmanalloc = None
                self.cpeextpseportcapabilities = Bits()
                self._segment_path = lambda: "pethPsePortEntry" + "[pethPsePortGroupIndex='" + str(self.pethpseportgroupindex) + "']" + "[pethPsePortIndex='" + str(self.pethpseportindex) + "']"
                self._absolute_path = lambda: "POWER-ETHERNET-MIB:POWER-ETHERNET-MIB/pethPsePortTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(POWERETHERNETMIB.PethPsePortTable.PethPsePortEntry, [u'pethpseportgroupindex', u'pethpseportindex', u'pethpseportadminenable', u'pethpseportpowerpairscontrolability', u'pethpseportpowerpairs', u'pethpseportdetectionstatus', u'pethpseportpowerpriority', u'pethpseportmpsabsentcounter', u'pethpseporttype', u'pethpseportpowerclassifications', u'pethpseportinvalidsignaturecounter', u'pethpseportpowerdeniedcounter', u'pethpseportoverloadcounter', u'pethpseportshortcounter', 'cpeextpseportenable', 'cpeextpseportdiscovermode', 'cpeextpseportdevicedetected', 'cpeextpseportieeepd', 'cpeextpseportadditionalstatus', 'cpeextpseportpwrmax', 'cpeextpseportpwrallocated', 'cpeextpseportpwravailable', 'cpeextpseportpwrconsumption', 'cpeextpseportmaxpwrdrawn', 'cpeextpseportentphyindex', 'cpeextpseportpolicingcapable', 'cpeextpseportpolicingenable', 'cpeextpseportpolicingaction', 'cpeextpseportpwrmanalloc', 'cpeextpseportcapabilities'], name, value)

            class CpeExtPsePortDiscoverMode(Enum):
                """
                CpeExtPsePortDiscoverMode (Enum Class)

                This object indicates the discover mode used by the system to

                discover the PD.

                A value of 'unknown' indicates that the discover mode on the

                interface is unknown.

                A value of 'off' indicates that discovery is disabled on the

                interface.

                A value of 'ieee' indicates that the discover mode on the

                interface is IEEE based.

                A value of 'cisco' indicates that the discover mode on the

                interface is Cisco based.

                A value of 'ieeeAndCisco' indicates that the discover mode on

                the interface is both IEEE and Cisco based.

                .. data:: unknown = 1

                .. data:: off = 2

                .. data:: ieee = 3

                .. data:: cisco = 4

                .. data:: ieeeAndCisco = 5

                """

                unknown = Enum.YLeaf(1, "unknown")

                off = Enum.YLeaf(2, "off")

                ieee = Enum.YLeaf(3, "ieee")

                cisco = Enum.YLeaf(4, "cisco")

                ieeeAndCisco = Enum.YLeaf(5, "ieeeAndCisco")


            class CpeExtPsePortEnable(Enum):
                """
                CpeExtPsePortEnable (Enum Class)

                This object is an extension of the pethPsePortAdminEnable

                object from RFC3621. It allows the user to be more specific

                when enabling the PSE functions. The states, 'auto', 'static'

                and 'limit' correspond to a value of 'true' for the

                pethPsePortAdminEnable object. The state 'disable' corresponds

                to a value of 'false' for the pethPsePortAdminEnable object.

                Setting this value to 'auto' enables Powered Device discovery

                on the interface and the amount of power allocated depends on

                the Powered Device discovered. If pethPsePortAdminEnable was

                'false' prior to this set operation, then it will become

                'true'.

                Setting this value to 'static' will also enable Powered

                Device discovery. However, this is different from 'auto'

                in that the amount of power is pre\-allocated based on the

                configuration on the Power Sourcing Equipment. If

                pethPsePortAdminEnable was 'false' prior to this set

                operation, then it will become 'true'.

                Setting this value to 'limit' enables Powered Device

                discovery on the interface. The amount of power allocated

                depends on the Powered Device discovered and the value

                of cpeExtPsePortPwrMax. The lower value will be used.

                If pethPsePortAdminEnable was 'false' prior to this set

                operation, then it will become 'true'.

                Setting this value to 'disable' disables the PSE functions.

                The pethPsePortAdminEnable object will adopt the value of

                'false' if it was 'true' prior to this set operation. When

                setting the pethPsePortAdminEnable object to 'false' this

                object cpeExtPsePortEnable will adopt the value of 'disable'.

                If cpeExtPsePortPolicingCapable of the PSE port, or

                cpeExtMainPsePwrMonitorCapable of the PSE port's

                main group, has the value of 'false', this object

                can only be set to 'auto', 'static' or 'disable'.

                Otherwise, this object can be set to 'auto', 'static',

                'limit' or 'disable'.

                .. data:: auto = 1

                .. data:: static = 2

                .. data:: limit = 3

                .. data:: disable = 4

                """

                auto = Enum.YLeaf(1, "auto")

                static = Enum.YLeaf(2, "static")

                limit = Enum.YLeaf(3, "limit")

                disable = Enum.YLeaf(4, "disable")


            class CpeExtPsePortPolicingAction(Enum):
                """
                CpeExtPsePortPolicingAction (Enum Class)

                This object specifies the power policing action that

                the device will take on this PSE port when the real\-time 

                power consumption exceeds its max power allocation if 

                the value of cpeExtPsePortPolicingEnable is 'on'. 

                     'deny'          \- the device will deny the power to 

                                       the PSE port 

                     'logOnly'       \- the device will not deny the power 

                                       to the PSE port

                .. data:: deny = 1

                .. data:: logOnly = 2

                """

                deny = Enum.YLeaf(1, "deny")

                logOnly = Enum.YLeaf(2, "logOnly")


            class CpeExtPsePortPolicingEnable(Enum):
                """
                CpeExtPsePortPolicingEnable (Enum Class)

                This object allows the user to turn on or turn off the

                power policing of the PSE port. If the instance value of 

                cpeExtPsePortPolicingCapable is 'TRUE', the user is allowed

                to set this object to 'on' or 'off'. Otherwise, this

                object is read\-only and always has the value of 'off'.

                .. data:: on = 1

                .. data:: off = 2

                """

                on = Enum.YLeaf(1, "on")

                off = Enum.YLeaf(2, "off")


            class PethPsePortDetectionStatus(Enum):
                """
                PethPsePortDetectionStatus (Enum Class)

                Describes the operational status of the port PD detection.

                A value of disabled(1)\- indicates that the PSE State diagram

                is in the state DISABLED.

                A value of deliveringPower(3) \- indicates that the PSE State

                diagram is in the state POWER\_ON for a duration greater than

                tlim max (see IEEE Std 802.3af Table 33\-5 tlim).

                A value of fault(4) \- indicates that the PSE State diagram is

                in the state TEST\_ERROR.

                A value of test(5) \- indicates that the PSE State diagram is

                in the state TEST\_MODE.

                A value of otherFault(6) \- indicates that the PSE State

                diagram is in the state IDLE due to the variable

                error\_conditions.

                A value of searching(2)\- indicates the PSE State diagram is

                in a state other than those listed above.

                .. data:: disabled = 1

                .. data:: searching = 2

                .. data:: deliveringPower = 3

                .. data:: fault = 4

                .. data:: test = 5

                .. data:: otherFault = 6

                """

                disabled = Enum.YLeaf(1, "disabled")

                searching = Enum.YLeaf(2, "searching")

                deliveringPower = Enum.YLeaf(3, "deliveringPower")

                fault = Enum.YLeaf(4, "fault")

                test = Enum.YLeaf(5, "test")

                otherFault = Enum.YLeaf(6, "otherFault")


            class PethPsePortPowerClassifications(Enum):
                """
                PethPsePortPowerClassifications (Enum Class)

                Classification is a way to tag different terminals on the

                Power over LAN network according to their power consumption.

                Devices such as IP telephones, WLAN access points and others,

                will be classified according to their power requirements.

                The meaning of the classification labels is defined in the

                IEEE specification.

                This variable is valid only while a PD is being powered,

                that is, while the attribute pethPsePortDetectionStatus

                is reporting the enumeration deliveringPower.

                .. data:: class0 = 1

                .. data:: class1 = 2

                .. data:: class2 = 3

                .. data:: class3 = 4

                .. data:: class4 = 5

                """

                class0 = Enum.YLeaf(1, "class0")

                class1 = Enum.YLeaf(2, "class1")

                class2 = Enum.YLeaf(3, "class2")

                class3 = Enum.YLeaf(4, "class3")

                class4 = Enum.YLeaf(5, "class4")


            class PethPsePortPowerPairs(Enum):
                """
                PethPsePortPowerPairs (Enum Class)

                Describes or controls the pairs in use.  If the value of

                pethPsePortPowerPairsControl is true, this object is

                writable.

                A value of signal(1) means that the signal pairs

                only are in use.

                A value of spare(2) means that the spare pairs

                only are in use.

                .. data:: signal = 1

                .. data:: spare = 2

                """

                signal = Enum.YLeaf(1, "signal")

                spare = Enum.YLeaf(2, "spare")


            class PethPsePortPowerPriority(Enum):
                """
                PethPsePortPowerPriority (Enum Class)

                This object controls the priority of the port from the point

                of view of a power management algorithm.  The priority that

                is set by this variable could be used by a control mechanism

                that prevents over current situations by disconnecting first

                ports with lower power priority.  Ports that connect devices

                critical to the operation of the network \- like the E911

                telephones ports \- should be set to higher priority.

                .. data:: critical = 1

                .. data:: high = 2

                .. data:: low = 3

                """

                critical = Enum.YLeaf(1, "critical")

                high = Enum.YLeaf(2, "high")

                low = Enum.YLeaf(3, "low")



    class PethMainPseTable(Entity):
        """
        A table of objects that display and control attributes
        of the main power source in a PSE  device.  Ethernet
        switches are one example of boxes that would support
        these objects.
        Values of all read\-write objects in this table are
        persistent at restart/reboot.
        
        .. attribute:: pethmainpseentry
        
        	A set of objects that display and control the Main power of a PSE. 
        	**type**\: list of  		 :py:class:`PethMainPseEntry <ydk.models.cisco_ios_xe.POWER_ETHERNET_MIB.POWERETHERNETMIB.PethMainPseTable.PethMainPseEntry>`
        
        

        """

        _prefix = 'POWER-ETHERNET-MIB'
        _revision = '2003-11-24'

        def __init__(self):
            super(POWERETHERNETMIB.PethMainPseTable, self).__init__()

            self.yang_name = "pethMainPseTable"
            self.yang_parent_name = "POWER-ETHERNET-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("pethMainPseEntry", ("pethmainpseentry", POWERETHERNETMIB.PethMainPseTable.PethMainPseEntry))])
            self._leafs = OrderedDict()

            self.pethmainpseentry = YList(self)
            self._segment_path = lambda: "pethMainPseTable"
            self._absolute_path = lambda: "POWER-ETHERNET-MIB:POWER-ETHERNET-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(POWERETHERNETMIB.PethMainPseTable, [], name, value)


        class PethMainPseEntry(Entity):
            """
            A set of objects that display and control the Main
            power of a PSE. 
            
            .. attribute:: pethmainpsegroupindex  (key)
            
            	This variable uniquely identifies the group to which power Ethernet PSE is connected.  Group means (box in the stack, module in a rack) and the value 1 MUST be used for non\-modular devices.  Furthermore, the same value MUST be used in this variable, pethPsePortGroupIndex, and pethNotificationControlGroupIndex to refer to a given box in a stack or module in a rack
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: pethmainpsepower
            
            	The nominal power of the PSE expressed in Watts
            	**type**\: int
            
            	**range:** 1..65535
            
            	**units**\: Watts
            
            .. attribute:: pethmainpseoperstatus
            
            	The operational status of the main PSE
            	**type**\:  :py:class:`PethMainPseOperStatus <ydk.models.cisco_ios_xe.POWER_ETHERNET_MIB.POWERETHERNETMIB.PethMainPseTable.PethMainPseEntry.PethMainPseOperStatus>`
            
            .. attribute:: pethmainpseconsumptionpower
            
            	Measured usage power expressed in Watts
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Watts
            
            .. attribute:: pethmainpseusagethreshold
            
            	The usage threshold expressed in percents for comparing the measured power and initiating an alarm if the threshold is exceeded
            	**type**\: int
            
            	**range:** 1..99
            
            	**units**\: %
            
            

            """

            _prefix = 'POWER-ETHERNET-MIB'
            _revision = '2003-11-24'

            def __init__(self):
                super(POWERETHERNETMIB.PethMainPseTable.PethMainPseEntry, self).__init__()

                self.yang_name = "pethMainPseEntry"
                self.yang_parent_name = "pethMainPseTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['pethmainpsegroupindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('pethmainpsegroupindex', (YLeaf(YType.int32, 'pethMainPseGroupIndex'), ['int'])),
                    ('pethmainpsepower', (YLeaf(YType.uint32, 'pethMainPsePower'), ['int'])),
                    ('pethmainpseoperstatus', (YLeaf(YType.enumeration, 'pethMainPseOperStatus'), [('ydk.models.cisco_ios_xe.POWER_ETHERNET_MIB', 'POWERETHERNETMIB', 'PethMainPseTable.PethMainPseEntry.PethMainPseOperStatus')])),
                    ('pethmainpseconsumptionpower', (YLeaf(YType.uint32, 'pethMainPseConsumptionPower'), ['int'])),
                    ('pethmainpseusagethreshold', (YLeaf(YType.int32, 'pethMainPseUsageThreshold'), ['int'])),
                ])
                self.pethmainpsegroupindex = None
                self.pethmainpsepower = None
                self.pethmainpseoperstatus = None
                self.pethmainpseconsumptionpower = None
                self.pethmainpseusagethreshold = None
                self._segment_path = lambda: "pethMainPseEntry" + "[pethMainPseGroupIndex='" + str(self.pethmainpsegroupindex) + "']"
                self._absolute_path = lambda: "POWER-ETHERNET-MIB:POWER-ETHERNET-MIB/pethMainPseTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(POWERETHERNETMIB.PethMainPseTable.PethMainPseEntry, [u'pethmainpsegroupindex', u'pethmainpsepower', u'pethmainpseoperstatus', u'pethmainpseconsumptionpower', u'pethmainpseusagethreshold'], name, value)

            class PethMainPseOperStatus(Enum):
                """
                PethMainPseOperStatus (Enum Class)

                The operational status of the main PSE.

                .. data:: on = 1

                .. data:: off = 2

                .. data:: faulty = 3

                """

                on = Enum.YLeaf(1, "on")

                off = Enum.YLeaf(2, "off")

                faulty = Enum.YLeaf(3, "faulty")



    class PethNotificationControlTable(Entity):
        """
        A table of objects that display and control the
        Notification on a PSE  device.
        Values of all read\-write objects in this table are
        persistent at restart/reboot.
        
        .. attribute:: pethnotificationcontrolentry
        
        	A set of objects that control the Notification events
        	**type**\: list of  		 :py:class:`PethNotificationControlEntry <ydk.models.cisco_ios_xe.POWER_ETHERNET_MIB.POWERETHERNETMIB.PethNotificationControlTable.PethNotificationControlEntry>`
        
        

        """

        _prefix = 'POWER-ETHERNET-MIB'
        _revision = '2003-11-24'

        def __init__(self):
            super(POWERETHERNETMIB.PethNotificationControlTable, self).__init__()

            self.yang_name = "pethNotificationControlTable"
            self.yang_parent_name = "POWER-ETHERNET-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("pethNotificationControlEntry", ("pethnotificationcontrolentry", POWERETHERNETMIB.PethNotificationControlTable.PethNotificationControlEntry))])
            self._leafs = OrderedDict()

            self.pethnotificationcontrolentry = YList(self)
            self._segment_path = lambda: "pethNotificationControlTable"
            self._absolute_path = lambda: "POWER-ETHERNET-MIB:POWER-ETHERNET-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(POWERETHERNETMIB.PethNotificationControlTable, [], name, value)


        class PethNotificationControlEntry(Entity):
            """
            A set of objects that control the Notification events.
            
            .. attribute:: pethnotificationcontrolgroupindex  (key)
            
            	This variable uniquely identifies the group.  Group means box in the stack, module in a rack and the value 1 MUST be used for non\-modular devices.  Furthermore, the same value MUST be used in this variable, pethPsePortGroupIndex, and pethMainPseGroupIndex to refer to a given box in a stack or module in a rack. 
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: pethnotificationcontrolenable
            
            	This object controls, on a per\-group basis, whether or not notifications from the agent are enabled.  The value true(1) means that notifications are enabled; the value false(2) means that they are not
            	**type**\: bool
            
            

            """

            _prefix = 'POWER-ETHERNET-MIB'
            _revision = '2003-11-24'

            def __init__(self):
                super(POWERETHERNETMIB.PethNotificationControlTable.PethNotificationControlEntry, self).__init__()

                self.yang_name = "pethNotificationControlEntry"
                self.yang_parent_name = "pethNotificationControlTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['pethnotificationcontrolgroupindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('pethnotificationcontrolgroupindex', (YLeaf(YType.int32, 'pethNotificationControlGroupIndex'), ['int'])),
                    ('pethnotificationcontrolenable', (YLeaf(YType.boolean, 'pethNotificationControlEnable'), ['bool'])),
                ])
                self.pethnotificationcontrolgroupindex = None
                self.pethnotificationcontrolenable = None
                self._segment_path = lambda: "pethNotificationControlEntry" + "[pethNotificationControlGroupIndex='" + str(self.pethnotificationcontrolgroupindex) + "']"
                self._absolute_path = lambda: "POWER-ETHERNET-MIB:POWER-ETHERNET-MIB/pethNotificationControlTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(POWERETHERNETMIB.PethNotificationControlTable.PethNotificationControlEntry, [u'pethnotificationcontrolgroupindex', u'pethnotificationcontrolenable'], name, value)

    def clone_ptr(self):
        self._top_entity = POWERETHERNETMIB()
        return self._top_entity

