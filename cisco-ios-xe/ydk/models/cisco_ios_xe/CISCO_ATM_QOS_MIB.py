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


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class VcparamconfiglocationEnum(Enum):
    """
    VcparamconfiglocationEnum

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

    configDefault = 1

    configVcDirect = 2

    configVcClass = 3

    configVcClassSubInterface = 4

    configVcClassInterface = 5


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_ATM_QOS_MIB as meta
        return meta._meta_table['VcparamconfiglocationEnum']


class VpstateEnum(Enum):
    """
    VpstateEnum

    States of virtual path\:

    1 \- Inactive

    2 \- Active

    .. data:: vpStateInactive = 1

    .. data:: vpStateActive = 2

    """

    vpStateInactive = 1

    vpStateActive = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_ATM_QOS_MIB as meta
        return meta._meta_table['VpstateEnum']



class CiscoAtmQosMib(object):
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
        self.caqqueuingparamsclasstable = CiscoAtmQosMib.Caqqueuingparamsclasstable()
        self.caqqueuingparamsclasstable.parent = self
        self.caqqueuingparamstable = CiscoAtmQosMib.Caqqueuingparamstable()
        self.caqqueuingparamstable.parent = self
        self.caqvccparamstable = CiscoAtmQosMib.Caqvccparamstable()
        self.caqvccparamstable.parent = self
        self.caqvpcparamstable = CiscoAtmQosMib.Caqvpcparamstable()
        self.caqvpcparamstable.parent = self


    class Caqvccparamstable(object):
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
            self.parent = None
            self.caqvccparamsentry = YList()
            self.caqvccparamsentry.parent = self
            self.caqvccparamsentry.name = 'caqvccparamsentry'


        class Caqvccparamsentry(object):
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
            	**type**\:   :py:class:`VcparamconfiglocationEnum <ydk.models.cisco_ios_xe.CISCO_ATM_QOS_MIB.VcparamconfiglocationEnum>`
            
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
            	**type**\:   :py:class:`VcparamconfiglocationEnum <ydk.models.cisco_ios_xe.CISCO_ATM_QOS_MIB.VcparamconfiglocationEnum>`
            
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
            	**type**\:   :py:class:`AtmservicecategoryEnum <ydk.models.cisco_ios_xe.ATM_FORUM_TC_MIB.AtmservicecategoryEnum>`
            
            

            """

            _prefix = 'CISCO-ATM-QOS-MIB'
            _revision = '2002-06-10'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.atmvclvpi = None
                self.atmvclvci = None
                self.caqvccparamsadtf = None
                self.caqvccparamsbcsin0 = None
                self.caqvccparamsbcsin01 = None
                self.caqvccparamsbcsout0 = None
                self.caqvccparamsbcsout01 = None
                self.caqvccparamscdv = None
                self.caqvccparamscdvt = None
                self.caqvccparamsfrtt = None
                self.caqvccparamsicr = None
                self.caqvccparamsinheritlevel = None
                self.caqvccparamsinvcdf = None
                self.caqvccparamsinvrdf = None
                self.caqvccparamsinvrif = None
                self.caqvccparamsinvtrm = None
                self.caqvccparamsmcrin = None
                self.caqvccparamsmcrout = None
                self.caqvccparamsnrm = None
                self.caqvccparamspcrin0 = None
                self.caqvccparamspcrin01 = None
                self.caqvccparamspcrout0 = None
                self.caqvccparamspcrout01 = None
                self.caqvccparamsrfl = None
                self.caqvccparamsscrin0 = None
                self.caqvccparamsscrin01 = None
                self.caqvccparamsscrout0 = None
                self.caqvccparamsscrout01 = None
                self.caqvccparamstbe = None
                self.caqvccparamstype = None

            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYModelError('Key property ifindex is None')
                if self.atmvclvpi is None:
                    raise YPYModelError('Key property atmvclvpi is None')
                if self.atmvclvci is None:
                    raise YPYModelError('Key property atmvclvci is None')

                return '/CISCO-ATM-QOS-MIB:CISCO-ATM-QOS-MIB/CISCO-ATM-QOS-MIB:caqVccParamsTable/CISCO-ATM-QOS-MIB:caqVccParamsEntry[CISCO-ATM-QOS-MIB:ifIndex = ' + str(self.ifindex) + '][CISCO-ATM-QOS-MIB:atmVclVpi = ' + str(self.atmvclvpi) + '][CISCO-ATM-QOS-MIB:atmVclVci = ' + str(self.atmvclvci) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ifindex is not None:
                    return True

                if self.atmvclvpi is not None:
                    return True

                if self.atmvclvci is not None:
                    return True

                if self.caqvccparamsadtf is not None:
                    return True

                if self.caqvccparamsbcsin0 is not None:
                    return True

                if self.caqvccparamsbcsin01 is not None:
                    return True

                if self.caqvccparamsbcsout0 is not None:
                    return True

                if self.caqvccparamsbcsout01 is not None:
                    return True

                if self.caqvccparamscdv is not None:
                    return True

                if self.caqvccparamscdvt is not None:
                    return True

                if self.caqvccparamsfrtt is not None:
                    return True

                if self.caqvccparamsicr is not None:
                    return True

                if self.caqvccparamsinheritlevel is not None:
                    return True

                if self.caqvccparamsinvcdf is not None:
                    return True

                if self.caqvccparamsinvrdf is not None:
                    return True

                if self.caqvccparamsinvrif is not None:
                    return True

                if self.caqvccparamsinvtrm is not None:
                    return True

                if self.caqvccparamsmcrin is not None:
                    return True

                if self.caqvccparamsmcrout is not None:
                    return True

                if self.caqvccparamsnrm is not None:
                    return True

                if self.caqvccparamspcrin0 is not None:
                    return True

                if self.caqvccparamspcrin01 is not None:
                    return True

                if self.caqvccparamspcrout0 is not None:
                    return True

                if self.caqvccparamspcrout01 is not None:
                    return True

                if self.caqvccparamsrfl is not None:
                    return True

                if self.caqvccparamsscrin0 is not None:
                    return True

                if self.caqvccparamsscrin01 is not None:
                    return True

                if self.caqvccparamsscrout0 is not None:
                    return True

                if self.caqvccparamsscrout01 is not None:
                    return True

                if self.caqvccparamstbe is not None:
                    return True

                if self.caqvccparamstype is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_ATM_QOS_MIB as meta
                return meta._meta_table['CiscoAtmQosMib.Caqvccparamstable.Caqvccparamsentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ATM-QOS-MIB:CISCO-ATM-QOS-MIB/CISCO-ATM-QOS-MIB:caqVccParamsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.caqvccparamsentry is not None:
                for child_ref in self.caqvccparamsentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_ATM_QOS_MIB as meta
            return meta._meta_table['CiscoAtmQosMib.Caqvccparamstable']['meta_info']


    class Caqvpcparamstable(object):
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
            self.parent = None
            self.caqvpcparamsentry = YList()
            self.caqvpcparamsentry.parent = self
            self.caqvpcparamsentry.name = 'caqvpcparamsentry'


        class Caqvpcparamsentry(object):
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
            	**type**\:   :py:class:`VpstateEnum <ydk.models.cisco_ios_xe.CISCO_ATM_QOS_MIB.VpstateEnum>`
            
            

            """

            _prefix = 'CISCO-ATM-QOS-MIB'
            _revision = '2002-06-10'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.atmvplvpi = None
                self.caqvpcparamsavailbw = None
                self.caqvpcparamscesrate = None
                self.caqvpcparamscesvccount = None
                self.caqvpcparamsdatavccount = None
                self.caqvpcparamsmbs = None
                self.caqvpcparamspeakrate = None
                self.caqvpcparamsscr = None
                self.caqvpcparamsvcdf4ete = None
                self.caqvpcparamsvcdf4seg = None
                self.caqvpcparamsvpstate = None

            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYModelError('Key property ifindex is None')
                if self.atmvplvpi is None:
                    raise YPYModelError('Key property atmvplvpi is None')

                return '/CISCO-ATM-QOS-MIB:CISCO-ATM-QOS-MIB/CISCO-ATM-QOS-MIB:caqVpcParamsTable/CISCO-ATM-QOS-MIB:caqVpcParamsEntry[CISCO-ATM-QOS-MIB:ifIndex = ' + str(self.ifindex) + '][CISCO-ATM-QOS-MIB:atmVplVpi = ' + str(self.atmvplvpi) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ifindex is not None:
                    return True

                if self.atmvplvpi is not None:
                    return True

                if self.caqvpcparamsavailbw is not None:
                    return True

                if self.caqvpcparamscesrate is not None:
                    return True

                if self.caqvpcparamscesvccount is not None:
                    return True

                if self.caqvpcparamsdatavccount is not None:
                    return True

                if self.caqvpcparamsmbs is not None:
                    return True

                if self.caqvpcparamspeakrate is not None:
                    return True

                if self.caqvpcparamsscr is not None:
                    return True

                if self.caqvpcparamsvcdf4ete is not None:
                    return True

                if self.caqvpcparamsvcdf4seg is not None:
                    return True

                if self.caqvpcparamsvpstate is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_ATM_QOS_MIB as meta
                return meta._meta_table['CiscoAtmQosMib.Caqvpcparamstable.Caqvpcparamsentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ATM-QOS-MIB:CISCO-ATM-QOS-MIB/CISCO-ATM-QOS-MIB:caqVpcParamsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.caqvpcparamsentry is not None:
                for child_ref in self.caqvpcparamsentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_ATM_QOS_MIB as meta
            return meta._meta_table['CiscoAtmQosMib.Caqvpcparamstable']['meta_info']


    class Caqqueuingparamstable(object):
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
            self.parent = None
            self.caqqueuingparamsentry = YList()
            self.caqqueuingparamsentry.parent = self
            self.caqqueuingparamsentry.name = 'caqqueuingparamsentry'


        class Caqqueuingparamsentry(object):
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
                self.parent = None
                self.ifindex = None
                self.atmvclvpi = None
                self.atmvclvci = None
                self.caqqueuingparamsmeanqdepth = None

            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYModelError('Key property ifindex is None')
                if self.atmvclvpi is None:
                    raise YPYModelError('Key property atmvclvpi is None')
                if self.atmvclvci is None:
                    raise YPYModelError('Key property atmvclvci is None')

                return '/CISCO-ATM-QOS-MIB:CISCO-ATM-QOS-MIB/CISCO-ATM-QOS-MIB:caqQueuingParamsTable/CISCO-ATM-QOS-MIB:caqQueuingParamsEntry[CISCO-ATM-QOS-MIB:ifIndex = ' + str(self.ifindex) + '][CISCO-ATM-QOS-MIB:atmVclVpi = ' + str(self.atmvclvpi) + '][CISCO-ATM-QOS-MIB:atmVclVci = ' + str(self.atmvclvci) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ifindex is not None:
                    return True

                if self.atmvclvpi is not None:
                    return True

                if self.atmvclvci is not None:
                    return True

                if self.caqqueuingparamsmeanqdepth is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_ATM_QOS_MIB as meta
                return meta._meta_table['CiscoAtmQosMib.Caqqueuingparamstable.Caqqueuingparamsentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ATM-QOS-MIB:CISCO-ATM-QOS-MIB/CISCO-ATM-QOS-MIB:caqQueuingParamsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.caqqueuingparamsentry is not None:
                for child_ref in self.caqqueuingparamsentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_ATM_QOS_MIB as meta
            return meta._meta_table['CiscoAtmQosMib.Caqqueuingparamstable']['meta_info']


    class Caqqueuingparamsclasstable(object):
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
            self.parent = None
            self.caqqueuingparamsclassentry = YList()
            self.caqqueuingparamsclassentry.parent = self
            self.caqqueuingparamsclassentry.name = 'caqqueuingparamsclassentry'


        class Caqqueuingparamsclassentry(object):
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
                self.parent = None
                self.ifindex = None
                self.atmvclvpi = None
                self.atmvclvci = None
                self.caqqueuingparamsclassindex = None
                self.caqqueuingparamsclassmaxthre = None
                self.caqqueuingparamsclassminthre = None
                self.caqqueuingparamsclassmrkprob = None
                self.caqqueuingparamsclassranddrp = None
                self.caqqueuingparamsclasstaildrp = None

            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYModelError('Key property ifindex is None')
                if self.atmvclvpi is None:
                    raise YPYModelError('Key property atmvclvpi is None')
                if self.atmvclvci is None:
                    raise YPYModelError('Key property atmvclvci is None')
                if self.caqqueuingparamsclassindex is None:
                    raise YPYModelError('Key property caqqueuingparamsclassindex is None')

                return '/CISCO-ATM-QOS-MIB:CISCO-ATM-QOS-MIB/CISCO-ATM-QOS-MIB:caqQueuingParamsClassTable/CISCO-ATM-QOS-MIB:caqQueuingParamsClassEntry[CISCO-ATM-QOS-MIB:ifIndex = ' + str(self.ifindex) + '][CISCO-ATM-QOS-MIB:atmVclVpi = ' + str(self.atmvclvpi) + '][CISCO-ATM-QOS-MIB:atmVclVci = ' + str(self.atmvclvci) + '][CISCO-ATM-QOS-MIB:caqQueuingParamsClassIndex = ' + str(self.caqqueuingparamsclassindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ifindex is not None:
                    return True

                if self.atmvclvpi is not None:
                    return True

                if self.atmvclvci is not None:
                    return True

                if self.caqqueuingparamsclassindex is not None:
                    return True

                if self.caqqueuingparamsclassmaxthre is not None:
                    return True

                if self.caqqueuingparamsclassminthre is not None:
                    return True

                if self.caqqueuingparamsclassmrkprob is not None:
                    return True

                if self.caqqueuingparamsclassranddrp is not None:
                    return True

                if self.caqqueuingparamsclasstaildrp is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_ATM_QOS_MIB as meta
                return meta._meta_table['CiscoAtmQosMib.Caqqueuingparamsclasstable.Caqqueuingparamsclassentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ATM-QOS-MIB:CISCO-ATM-QOS-MIB/CISCO-ATM-QOS-MIB:caqQueuingParamsClassTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.caqqueuingparamsclassentry is not None:
                for child_ref in self.caqqueuingparamsclassentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_ATM_QOS_MIB as meta
            return meta._meta_table['CiscoAtmQosMib.Caqqueuingparamsclasstable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-ATM-QOS-MIB:CISCO-ATM-QOS-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.caqqueuingparamsclasstable is not None and self.caqqueuingparamsclasstable._has_data():
            return True

        if self.caqqueuingparamstable is not None and self.caqqueuingparamstable._has_data():
            return True

        if self.caqvccparamstable is not None and self.caqvccparamstable._has_data():
            return True

        if self.caqvpcparamstable is not None and self.caqvpcparamstable._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_ATM_QOS_MIB as meta
        return meta._meta_table['CiscoAtmQosMib']['meta_info']


