""" CISCO_IETF_PW_ENET_MIB 

This MIB describes a model for managing Ethernet  
point\-to\-point pseudo wire services over a Packet  
Switched Network (PSN).

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class CiscoIetfPwEnetMib(object):
    """
    
    
    .. attribute:: cpwvcenetmplsprimappingtable
    
    	This table may be used for MPLS PSNs if there is a need   to hold multiple VC, each with different COS, for the same  user service (port + PW VLAN). Such a need may arise if the  MPLS network is capable of L\-LSP or E\-LSP without multiple  COS capabilities.  Each row is indexed by the cpwVcIndex   and indicate the PRI bits on the packet recieved from the   user port (or VPLS virtual port) that are  classified to this VC. Note that the EXP bit value of the VC  is configured in the CISCO\-IETF\-PW\-MPLS\-MIB
    	**type**\:   :py:class:`Cpwvcenetmplsprimappingtable <ydk.models.cisco_ios_xe.CISCO_IETF_PW_ENET_MIB.CiscoIetfPwEnetMib.Cpwvcenetmplsprimappingtable>`
    
    .. attribute:: cpwvcenetstatstable
    
    	This table contains statistical counters specific for   Ethernet PW
    	**type**\:   :py:class:`Cpwvcenetstatstable <ydk.models.cisco_ios_xe.CISCO_IETF_PW_ENET_MIB.CiscoIetfPwEnetMib.Cpwvcenetstatstable>`
    
    .. attribute:: cpwvcenettable
    
    	This table contains the index to the Ethernet tables   associated with this ETH VC, the VLAN configuration and   VLAN mode
    	**type**\:   :py:class:`Cpwvcenettable <ydk.models.cisco_ios_xe.CISCO_IETF_PW_ENET_MIB.CiscoIetfPwEnetMib.Cpwvcenettable>`
    
    

    """

    _prefix = 'CISCO-IETF-PW-ENET-MIB'
    _revision = '2002-09-22'

    def __init__(self):
        self.cpwvcenetmplsprimappingtable = CiscoIetfPwEnetMib.Cpwvcenetmplsprimappingtable()
        self.cpwvcenetmplsprimappingtable.parent = self
        self.cpwvcenetstatstable = CiscoIetfPwEnetMib.Cpwvcenetstatstable()
        self.cpwvcenetstatstable.parent = self
        self.cpwvcenettable = CiscoIetfPwEnetMib.Cpwvcenettable()
        self.cpwvcenettable.parent = self


    class Cpwvcenettable(object):
        """
        This table contains the index to the Ethernet tables  
        associated with this ETH VC, the VLAN configuration and  
        VLAN mode.
        
        .. attribute:: cpwvcenetentry
        
        	This table is indexed by the same index that was created   for the associated entry in the PW VC Table in the  CISCO\-IETF\-PW\-MIB.  The CpwVcIndex and the cpwVcEnetPwVlan  are used as indexes to allow multiple VLANs to exist on  the same PW.   An entry is created in this table by the agent for every   entry in the cpwVc table with a VcType of 'ethernetVLAN',  'ethernet' or 'ethernetVPLS'. Additional rows may be   created by the operator or the agent if multiple entries  are required for the same VC.   This table provides Ethernet port mapping and VLAN   configuration for each Ethernet VC
        	**type**\: list of    :py:class:`Cpwvcenetentry <ydk.models.cisco_ios_xe.CISCO_IETF_PW_ENET_MIB.CiscoIetfPwEnetMib.Cpwvcenettable.Cpwvcenetentry>`
        
        

        """

        _prefix = 'CISCO-IETF-PW-ENET-MIB'
        _revision = '2002-09-22'

        def __init__(self):
            self.parent = None
            self.cpwvcenetentry = YList()
            self.cpwvcenetentry.parent = self
            self.cpwvcenetentry.name = 'cpwvcenetentry'


        class Cpwvcenetentry(object):
            """
            This table is indexed by the same index that was created  
            for the associated entry in the PW VC Table in the 
            CISCO\-IETF\-PW\-MIB.  The CpwVcIndex and the cpwVcEnetPwVlan 
            are used as indexes to allow multiple VLANs to exist on 
            the same PW. 
            
            An entry is created in this table by the agent for every  
            entry in the cpwVc table with a VcType of 'ethernetVLAN', 
            'ethernet' or 'ethernetVPLS'. Additional rows may be  
            created by the operator or the agent if multiple entries 
            are required for the same VC. 
            
            This table provides Ethernet port mapping and VLAN  
            configuration for each Ethernet VC.
            
            .. attribute:: cpwvcindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`cpwvcindex <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CiscoIetfPwMib.Cpwvctable.Cpwvcentry>`
            
            .. attribute:: cpwvcenetpwvlan  <key>
            
            	This Object defines the VLAN on the VC. The value of 4097  is used if the object is not applicable, for example when  mapping all packets from an Ethernet port to this VC.  The value of 4096 is used to indicate untagged frames (at   least from the PW point of view), for example if   cpwVcEnetVlanMode is equal 'removeVLAN' or when   cpwVcEnetVlanMode equal 'noChange' and cpwVcEnetPortVlan  is equal 4096
            	**type**\:  int
            
            	**range:** 0..4097
            
            .. attribute:: cpwvcenetportifindex
            
            	This object is used to specify the ifIndex of the ETHERNET  port associated with this VC for point\-to\-point Ethernet   service, or the ifIndex of the virtual interface of the VPLS   instance associated with the PW if the service is VPLS. Two   rows in this table can point to the same ifIndex only if\:   1) It is required to support multiple COS on a MPLS PSN      for the same service (i.e.\: a combination of ports and      VLANs) by the use of multiple VC, each with a different     COS.   2) There is no overlap of VLAN values specified in      cpwVcEnetPortVlan that are associated with this port.   A value of zero indicate that association to an ifIndex is  not yet known
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: cpwvcenetportvlan
            
            	This object define the VLAN value on the physical port (or   VPLS virtual port) if a change is required to the VLAN value  between the VC and the physical/virtual port.   The value of this object can be ignored if the whole traffic   from the port is forwarded to one VC independent of the   tagging on the port, but it is RECOMENDED that the value in  this case will be '4097' indicating not relevant.   It MUST be equal to cpwVcEnetPwVlan if 'noChange' mode  is used.   The value 4096 indicate that no VLAN (i.e. untagged   frames) on the port are associated to this VC. This   allows the same behaviors as assigning 'Default VLAN'   to un\-tagged frames. 
            	**type**\:  int
            
            	**range:** 0..4097
            
            .. attribute:: cpwvcenetrowstatus
            
            	Enable creating, deleting and modifying this row
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: cpwvcenetstoragetype
            
            	Indicates the storage type of this row
            	**type**\:   :py:class:`StoragetypeEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.StoragetypeEnum>`
            
            .. attribute:: cpwvcenetvcifindex
            
            	It is sometimes convenient to model the VC PW as a   virtual interface in the ifTable. In these cases this   object hold the value of the ifIndex in the ifTable   representing this VC PW. A value of zero indicate no such   association or association is not yet known
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: cpwvcenetvlanmode
            
            	Indicate the mode of VLAN handling between the port   associated to the VC and the VC encapsulation itself.   \- 'other' indicate operation that is not defined by    this MIB.   \- 'portBased' indicates that the forwarder will forward    packets between the port and the PW independent of their    structure.   \- 'noChange' indicates that the VC contains the original     user VLAN, as specified in cpwVcEnetPortVlan.   \- 'changeVlan' indicates that the VLAN field on the VC     may be different than the VLAN field on the user's     port.   \- 'removeVlan' indicates that the encapsulation on the     VC does not include the original VLAN field. Note     that PRI bits transparency is lost in this case.   \- 'addVlan' indicate that a VLAN field will be added    on the PSN bound direction. cpwVcEnetPwVlan indicate    the value that will be added.    \- 'removeVlan', 'addVlan' and 'changeVlan' implementation    is not required. 
            	**type**\:   :py:class:`CpwvcenetvlanmodeEnum <ydk.models.cisco_ios_xe.CISCO_IETF_PW_ENET_MIB.CiscoIetfPwEnetMib.Cpwvcenettable.Cpwvcenetentry.CpwvcenetvlanmodeEnum>`
            
            

            """

            _prefix = 'CISCO-IETF-PW-ENET-MIB'
            _revision = '2002-09-22'

            def __init__(self):
                self.parent = None
                self.cpwvcindex = None
                self.cpwvcenetpwvlan = None
                self.cpwvcenetportifindex = None
                self.cpwvcenetportvlan = None
                self.cpwvcenetrowstatus = None
                self.cpwvcenetstoragetype = None
                self.cpwvcenetvcifindex = None
                self.cpwvcenetvlanmode = None

            class CpwvcenetvlanmodeEnum(Enum):
                """
                CpwvcenetvlanmodeEnum

                Indicate the mode of VLAN handling between the port  

                associated to the VC and the VC encapsulation itself. 

                \- 'other' indicate operation that is not defined by 

                  this MIB. 

                \- 'portBased' indicates that the forwarder will forward 

                  packets between the port and the PW independent of their 

                  structure. 

                \- 'noChange' indicates that the VC contains the original 

                   user VLAN, as specified in cpwVcEnetPortVlan. 

                \- 'changeVlan' indicates that the VLAN field on the VC  

                  may be different than the VLAN field on the user's  

                  port. 

                \- 'removeVlan' indicates that the encapsulation on the  

                  VC does not include the original VLAN field. Note  

                  that PRI bits transparency is lost in this case. 

                \- 'addVlan' indicate that a VLAN field will be added 

                  on the PSN bound direction. cpwVcEnetPwVlan indicate 

                  the value that will be added.  

                \- 'removeVlan', 'addVlan' and 'changeVlan' implementation 

                  is not required. 

                .. data:: other = 0

                .. data:: portBased = 1

                .. data:: noChange = 2

                .. data:: changeVlan = 3

                .. data:: addVlan = 4

                .. data:: removeVlan = 5

                """

                other = 0

                portBased = 1

                noChange = 2

                changeVlan = 3

                addVlan = 4

                removeVlan = 5


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_PW_ENET_MIB as meta
                    return meta._meta_table['CiscoIetfPwEnetMib.Cpwvcenettable.Cpwvcenetentry.CpwvcenetvlanmodeEnum']


            @property
            def _common_path(self):
                if self.cpwvcindex is None:
                    raise YPYModelError('Key property cpwvcindex is None')
                if self.cpwvcenetpwvlan is None:
                    raise YPYModelError('Key property cpwvcenetpwvlan is None')

                return '/CISCO-IETF-PW-ENET-MIB:CISCO-IETF-PW-ENET-MIB/CISCO-IETF-PW-ENET-MIB:cpwVcEnetTable/CISCO-IETF-PW-ENET-MIB:cpwVcEnetEntry[CISCO-IETF-PW-ENET-MIB:cpwVcIndex = ' + str(self.cpwvcindex) + '][CISCO-IETF-PW-ENET-MIB:cpwVcEnetPwVlan = ' + str(self.cpwvcenetpwvlan) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cpwvcindex is not None:
                    return True

                if self.cpwvcenetpwvlan is not None:
                    return True

                if self.cpwvcenetportifindex is not None:
                    return True

                if self.cpwvcenetportvlan is not None:
                    return True

                if self.cpwvcenetrowstatus is not None:
                    return True

                if self.cpwvcenetstoragetype is not None:
                    return True

                if self.cpwvcenetvcifindex is not None:
                    return True

                if self.cpwvcenetvlanmode is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_PW_ENET_MIB as meta
                return meta._meta_table['CiscoIetfPwEnetMib.Cpwvcenettable.Cpwvcenetentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IETF-PW-ENET-MIB:CISCO-IETF-PW-ENET-MIB/CISCO-IETF-PW-ENET-MIB:cpwVcEnetTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cpwvcenetentry is not None:
                for child_ref in self.cpwvcenetentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_PW_ENET_MIB as meta
            return meta._meta_table['CiscoIetfPwEnetMib.Cpwvcenettable']['meta_info']


    class Cpwvcenetmplsprimappingtable(object):
        """
        This table may be used for MPLS PSNs if there is a need  
        to hold multiple VC, each with different COS, for the same 
        user service (port + PW VLAN). Such a need may arise if the 
        MPLS network is capable of L\-LSP or E\-LSP without multiple 
        COS capabilities.  Each row is indexed by the cpwVcIndex  
        and indicate the PRI bits on the packet recieved from the  
        user port (or VPLS virtual port) that are 
        classified to this VC. Note that the EXP bit value of the VC 
        is configured in the CISCO\-IETF\-PW\-MPLS\-MIB.
        
        .. attribute:: cpwvcenetmplsprimappingtableentry
        
        	Each entry is created if special classification based on   the PRI bits is required for this VC
        	**type**\: list of    :py:class:`Cpwvcenetmplsprimappingtableentry <ydk.models.cisco_ios_xe.CISCO_IETF_PW_ENET_MIB.CiscoIetfPwEnetMib.Cpwvcenetmplsprimappingtable.Cpwvcenetmplsprimappingtableentry>`
        
        

        """

        _prefix = 'CISCO-IETF-PW-ENET-MIB'
        _revision = '2002-09-22'

        def __init__(self):
            self.parent = None
            self.cpwvcenetmplsprimappingtableentry = YList()
            self.cpwvcenetmplsprimappingtableentry.parent = self
            self.cpwvcenetmplsprimappingtableentry.name = 'cpwvcenetmplsprimappingtableentry'


        class Cpwvcenetmplsprimappingtableentry(object):
            """
            Each entry is created if special classification based on  
            the PRI bits is required for this VC.
            
            .. attribute:: cpwvcindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`cpwvcindex <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CiscoIetfPwMib.Cpwvctable.Cpwvcentry>`
            
            .. attribute:: cpwvcenetmplsprimapping
            
            	This object defines the groups of user PRI mapped into  this VC. Each bit set indicates that this user priority   is assigned to this VC.   The value 'untagged' is used to indicate that untagged   frames are also associated to this VC.   This object allow the use of different PSN COS based on   user marking of PRI bits in MPLS PSN with L\-LSP or   E\-LSP without multiple COS support. In all other cases,   the default value MUST be used.   It is REQUIRED that there is no overlap on this object   between rows serving the same service (port+ PW VLAN).   In case of missing BIT configuration between rows to   the same service, incoming packets with PRI marking not   configured should be handled by the VC with the lowest   COS. 
            	**type**\:   :py:class:`Cpwvcenetmplsprimapping <ydk.models.cisco_ios_xe.CISCO_IETF_PW_ENET_MIB.CiscoIetfPwEnetMib.Cpwvcenetmplsprimappingtable.Cpwvcenetmplsprimappingtableentry.Cpwvcenetmplsprimapping>`
            
            .. attribute:: cpwvcenetmplsprimappingrowstatus
            
            	Enable creating, deleting and modifying this row
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: cpwvcenetmplsprimappingstoragetype
            
            	Indicates the storage type of this row
            	**type**\:   :py:class:`StoragetypeEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.StoragetypeEnum>`
            
            

            """

            _prefix = 'CISCO-IETF-PW-ENET-MIB'
            _revision = '2002-09-22'

            def __init__(self):
                self.parent = None
                self.cpwvcindex = None
                self.cpwvcenetmplsprimapping = CiscoIetfPwEnetMib.Cpwvcenetmplsprimappingtable.Cpwvcenetmplsprimappingtableentry.Cpwvcenetmplsprimapping()
                self.cpwvcenetmplsprimappingrowstatus = None
                self.cpwvcenetmplsprimappingstoragetype = None

            class Cpwvcenetmplsprimapping(FixedBitsDict):
                """
                Cpwvcenetmplsprimapping

                This object defines the groups of user PRI mapped into 
                this VC. Each bit set indicates that this user priority  
                is assigned to this VC. 
                
                The value 'untagged' is used to indicate that untagged  
                frames are also associated to this VC. 
                
                This object allow the use of different PSN COS based on  
                user marking of PRI bits in MPLS PSN with L\-LSP or  
                E\-LSP without multiple COS support. In all other cases,  
                the default value MUST be used. 
                
                It is REQUIRED that there is no overlap on this object  
                between rows serving the same service (port+ PW VLAN). 
                
                In case of missing BIT configuration between rows to  
                the same service, incoming packets with PRI marking not  
                configured should be handled by the VC with the lowest  
                COS. 
                Keys are:- pri101 , pri010 , untagged , pri001 , pri011 , pri110 , pri100 , pri000 , pri111

                """

                def __init__(self):
                    self._dictionary = { 
                        'pri101':False,
                        'pri010':False,
                        'untagged':False,
                        'pri001':False,
                        'pri011':False,
                        'pri110':False,
                        'pri100':False,
                        'pri000':False,
                        'pri111':False,
                    }
                    self._pos_map = { 
                        'pri101':5,
                        'pri010':2,
                        'untagged':8,
                        'pri001':1,
                        'pri011':3,
                        'pri110':6,
                        'pri100':4,
                        'pri000':0,
                        'pri111':7,
                    }

            @property
            def _common_path(self):
                if self.cpwvcindex is None:
                    raise YPYModelError('Key property cpwvcindex is None')

                return '/CISCO-IETF-PW-ENET-MIB:CISCO-IETF-PW-ENET-MIB/CISCO-IETF-PW-ENET-MIB:cpwVcEnetMplsPriMappingTable/CISCO-IETF-PW-ENET-MIB:cpwVcEnetMplsPriMappingTableEntry[CISCO-IETF-PW-ENET-MIB:cpwVcIndex = ' + str(self.cpwvcindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cpwvcindex is not None:
                    return True

                if self.cpwvcenetmplsprimapping is not None:
                    if self.cpwvcenetmplsprimapping._has_data():
                        return True

                if self.cpwvcenetmplsprimappingrowstatus is not None:
                    return True

                if self.cpwvcenetmplsprimappingstoragetype is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_PW_ENET_MIB as meta
                return meta._meta_table['CiscoIetfPwEnetMib.Cpwvcenetmplsprimappingtable.Cpwvcenetmplsprimappingtableentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IETF-PW-ENET-MIB:CISCO-IETF-PW-ENET-MIB/CISCO-IETF-PW-ENET-MIB:cpwVcEnetMplsPriMappingTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cpwvcenetmplsprimappingtableentry is not None:
                for child_ref in self.cpwvcenetmplsprimappingtableentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_PW_ENET_MIB as meta
            return meta._meta_table['CiscoIetfPwEnetMib.Cpwvcenetmplsprimappingtable']['meta_info']


    class Cpwvcenetstatstable(object):
        """
        This table contains statistical counters specific for  
        Ethernet PW.
        
        .. attribute:: cpwvcenetstatsentry
        
        	Each entry represents the statistics gathered for the   VC carrying the Ethernet packets since this VC was   first created in the cpwVcEnetTable
        	**type**\: list of    :py:class:`Cpwvcenetstatsentry <ydk.models.cisco_ios_xe.CISCO_IETF_PW_ENET_MIB.CiscoIetfPwEnetMib.Cpwvcenetstatstable.Cpwvcenetstatsentry>`
        
        

        """

        _prefix = 'CISCO-IETF-PW-ENET-MIB'
        _revision = '2002-09-22'

        def __init__(self):
            self.parent = None
            self.cpwvcenetstatsentry = YList()
            self.cpwvcenetstatsentry.parent = self
            self.cpwvcenetstatsentry.name = 'cpwvcenetstatsentry'


        class Cpwvcenetstatsentry(object):
            """
            Each entry represents the statistics gathered for the  
            VC carrying the Ethernet packets since this VC was  
            first created in the cpwVcEnetTable.
            
            .. attribute:: cpwvcindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`cpwvcindex <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CiscoIetfPwMib.Cpwvctable.Cpwvcentry>`
            
            .. attribute:: cpwvcenetstatsillegallength
            
            	The number of packets that were received with an illegal   Ethernet packet length on this VC. An illegal length is defined  as being greater than the value in the advertised maximum MTU   supported, or shorter than the allowed Ethernet packet size
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cpwvcenetstatsillegalvlan
            
            	The number of packets received (from the PSN) on this VC with   an illegal VLAN field, missing VLAN field that was expected, or   A VLAN field when it was not expected. This counter is not   relevant if the VC type is 'ethernet' (i.e. raw mode), and   should be set to 0 by the agent to indicate this
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'CISCO-IETF-PW-ENET-MIB'
            _revision = '2002-09-22'

            def __init__(self):
                self.parent = None
                self.cpwvcindex = None
                self.cpwvcenetstatsillegallength = None
                self.cpwvcenetstatsillegalvlan = None

            @property
            def _common_path(self):
                if self.cpwvcindex is None:
                    raise YPYModelError('Key property cpwvcindex is None')

                return '/CISCO-IETF-PW-ENET-MIB:CISCO-IETF-PW-ENET-MIB/CISCO-IETF-PW-ENET-MIB:cpwVcEnetStatsTable/CISCO-IETF-PW-ENET-MIB:cpwVcEnetStatsEntry[CISCO-IETF-PW-ENET-MIB:cpwVcIndex = ' + str(self.cpwvcindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cpwvcindex is not None:
                    return True

                if self.cpwvcenetstatsillegallength is not None:
                    return True

                if self.cpwvcenetstatsillegalvlan is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_PW_ENET_MIB as meta
                return meta._meta_table['CiscoIetfPwEnetMib.Cpwvcenetstatstable.Cpwvcenetstatsentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IETF-PW-ENET-MIB:CISCO-IETF-PW-ENET-MIB/CISCO-IETF-PW-ENET-MIB:cpwVcEnetStatsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cpwvcenetstatsentry is not None:
                for child_ref in self.cpwvcenetstatsentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_PW_ENET_MIB as meta
            return meta._meta_table['CiscoIetfPwEnetMib.Cpwvcenetstatstable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-IETF-PW-ENET-MIB:CISCO-IETF-PW-ENET-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.cpwvcenetmplsprimappingtable is not None and self.cpwvcenetmplsprimappingtable._has_data():
            return True

        if self.cpwvcenetstatstable is not None and self.cpwvcenetstatstable._has_data():
            return True

        if self.cpwvcenettable is not None and self.cpwvcenettable._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_PW_ENET_MIB as meta
        return meta._meta_table['CiscoIetfPwEnetMib']['meta_info']


