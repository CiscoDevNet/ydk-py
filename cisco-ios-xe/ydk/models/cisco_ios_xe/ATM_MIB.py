""" ATM_MIB 

This is the MIB Module for ATM and AAL5\-related
objects for managing ATM interfaces, ATM virtual
links, ATM cross\-connects, AAL5 entities, and
and AAL5 connections.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class AtmMib(object):
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
        self.aal5vcctable = AtmMib.Aal5Vcctable()
        self.aal5vcctable.parent = self
        self.atminterfaceconftable = AtmMib.Atminterfaceconftable()
        self.atminterfaceconftable.parent = self
        self.atminterfaceds3plcptable = AtmMib.Atminterfaceds3Plcptable()
        self.atminterfaceds3plcptable.parent = self
        self.atminterfacetctable = AtmMib.Atminterfacetctable()
        self.atminterfacetctable.parent = self
        self.atmmibobjects = AtmMib.Atmmibobjects()
        self.atmmibobjects.parent = self
        self.atmtrafficdescrparamtable = AtmMib.Atmtrafficdescrparamtable()
        self.atmtrafficdescrparamtable.parent = self
        self.atmvccrossconnecttable = AtmMib.Atmvccrossconnecttable()
        self.atmvccrossconnecttable.parent = self
        self.atmvcltable = AtmMib.Atmvcltable()
        self.atmvcltable.parent = self
        self.atmvpcrossconnecttable = AtmMib.Atmvpcrossconnecttable()
        self.atmvpcrossconnecttable.parent = self
        self.atmvpltable = AtmMib.Atmvpltable()
        self.atmvpltable.parent = self


    class Atmmibobjects(object):
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
            self.parent = None
            self.atmtrafficdescrparamindexnext = None
            self.atmvccrossconnectindexnext = None
            self.atmvpcrossconnectindexnext = None

        @property
        def _common_path(self):

            return '/ATM-MIB:ATM-MIB/ATM-MIB:atmMIBObjects'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.atmtrafficdescrparamindexnext is not None:
                return True

            if self.atmvccrossconnectindexnext is not None:
                return True

            if self.atmvpcrossconnectindexnext is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _ATM_MIB as meta
            return meta._meta_table['AtmMib.Atmmibobjects']['meta_info']


    class Atminterfaceconftable(object):
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
            self.parent = None
            self.atminterfaceconfentry = YList()
            self.atminterfaceconfentry.parent = self
            self.atminterfaceconfentry.name = 'atminterfaceconfentry'


        class Atminterfaceconfentry(object):
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
            	**type**\:   :py:class:`AtminterfaceaddresstypeEnum <ydk.models.cisco_ios_xe.ATM_MIB.AtmMib.Atminterfaceconftable.Atminterfaceconfentry.AtminterfaceaddresstypeEnum>`
            
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
            	**type**\:   :py:class:`CatmoamfailuretypeEnum <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CatmoamfailuretypeEnum>`
            
            .. attribute:: catmintftypeofoamrecover
            
            	Type of OAM Recovered
            	**type**\:   :py:class:`CatmoamrecoverytypeEnum <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CatmoamrecoverytypeEnum>`
            
            

            """

            _prefix = 'ATM-MIB'
            _revision = '1998-10-19'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.atminterfaceaddresstype = None
                self.atminterfaceadminaddress = None
                self.atminterfaceconfvccs = None
                self.atminterfaceconfvpcs = None
                self.atminterfacecurrentmaxvcibits = None
                self.atminterfacecurrentmaxvpibits = None
                self.atminterfaceilmivci = None
                self.atminterfaceilmivpi = None
                self.atminterfacemaxactivevcibits = None
                self.atminterfacemaxactivevpibits = None
                self.atminterfacemaxvccs = None
                self.atminterfacemaxvpcs = None
                self.atminterfacemyneighborifname = None
                self.atminterfacemyneighboripaddress = None
                self.atminterfacesubscraddress = None
                self.atmintfcurrentlydowntouppvcls = None
                self.atmintfcurrentlyfailingpvcls = None
                self.atmintfcurrentlyoamfailingpvcls = None
                self.atmintfoamfailedpvcls = None
                self.atmintfpvcfailures = None
                self.atmintfpvcfailurestrapenable = None
                self.atmintfpvcnotificationinterval = None
                self.atmpreviouslyfailedpvclinterval = None
                self.catmintfaisrdioamfailedpvcls = None
                self.catmintfaisrdioamrcovedpvcls = None
                self.catmintfanyoamfailedpvcls = None
                self.catmintfanyoamrcovedpvcls = None
                self.catmintfcuraisrdioamfailingpvcls = None
                self.catmintfcuraisrdioamrcovingpvcls = None
                self.catmintfcuranyoamfailingpvcls = None
                self.catmintfcuranyoamrcovingpvcls = None
                self.catmintfcurendccoamfailingpvcls = None
                self.catmintfcurendccoamrcovingpvcls = None
                self.catmintfcurrentlydowntouppvcls = None
                self.catmintfcurrentoamfailingpvcls = None
                self.catmintfcurrentoamrcovingpvcls = None
                self.catmintfcursegccoamfailingpvcls = None
                self.catmintfcursegccoamrcovingpvcls = None
                self.catmintfendccoamfailedpvcls = None
                self.catmintfendccoamrcovedpvcls = None
                self.catmintfoamfailedpvcls = None
                self.catmintfoamrcovedpvcls = None
                self.catmintfsegccoamfailedpvcls = None
                self.catmintfsegccoamrcovedpvcls = None
                self.catmintftypeofoamfailure = None
                self.catmintftypeofoamrecover = None

            class AtminterfaceaddresstypeEnum(Enum):
                """
                AtminterfaceaddresstypeEnum

                The type of primary ATM address configured

                for use at this ATM interface.

                .. data:: private = 1

                .. data:: nsapE164 = 2

                .. data:: nativeE164 = 3

                .. data:: other = 4

                """

                private = 1

                nsapE164 = 2

                nativeE164 = 3

                other = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _ATM_MIB as meta
                    return meta._meta_table['AtmMib.Atminterfaceconftable.Atminterfaceconfentry.AtminterfaceaddresstypeEnum']


            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYModelError('Key property ifindex is None')

                return '/ATM-MIB:ATM-MIB/ATM-MIB:atmInterfaceConfTable/ATM-MIB:atmInterfaceConfEntry[ATM-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ifindex is not None:
                    return True

                if self.atminterfaceaddresstype is not None:
                    return True

                if self.atminterfaceadminaddress is not None:
                    return True

                if self.atminterfaceconfvccs is not None:
                    return True

                if self.atminterfaceconfvpcs is not None:
                    return True

                if self.atminterfacecurrentmaxvcibits is not None:
                    return True

                if self.atminterfacecurrentmaxvpibits is not None:
                    return True

                if self.atminterfaceilmivci is not None:
                    return True

                if self.atminterfaceilmivpi is not None:
                    return True

                if self.atminterfacemaxactivevcibits is not None:
                    return True

                if self.atminterfacemaxactivevpibits is not None:
                    return True

                if self.atminterfacemaxvccs is not None:
                    return True

                if self.atminterfacemaxvpcs is not None:
                    return True

                if self.atminterfacemyneighborifname is not None:
                    return True

                if self.atminterfacemyneighboripaddress is not None:
                    return True

                if self.atminterfacesubscraddress is not None:
                    return True

                if self.atmintfcurrentlydowntouppvcls is not None:
                    return True

                if self.atmintfcurrentlyfailingpvcls is not None:
                    return True

                if self.atmintfcurrentlyoamfailingpvcls is not None:
                    return True

                if self.atmintfoamfailedpvcls is not None:
                    return True

                if self.atmintfpvcfailures is not None:
                    return True

                if self.atmintfpvcfailurestrapenable is not None:
                    return True

                if self.atmintfpvcnotificationinterval is not None:
                    return True

                if self.atmpreviouslyfailedpvclinterval is not None:
                    return True

                if self.catmintfaisrdioamfailedpvcls is not None:
                    return True

                if self.catmintfaisrdioamrcovedpvcls is not None:
                    return True

                if self.catmintfanyoamfailedpvcls is not None:
                    return True

                if self.catmintfanyoamrcovedpvcls is not None:
                    return True

                if self.catmintfcuraisrdioamfailingpvcls is not None:
                    return True

                if self.catmintfcuraisrdioamrcovingpvcls is not None:
                    return True

                if self.catmintfcuranyoamfailingpvcls is not None:
                    return True

                if self.catmintfcuranyoamrcovingpvcls is not None:
                    return True

                if self.catmintfcurendccoamfailingpvcls is not None:
                    return True

                if self.catmintfcurendccoamrcovingpvcls is not None:
                    return True

                if self.catmintfcurrentlydowntouppvcls is not None:
                    return True

                if self.catmintfcurrentoamfailingpvcls is not None:
                    return True

                if self.catmintfcurrentoamrcovingpvcls is not None:
                    return True

                if self.catmintfcursegccoamfailingpvcls is not None:
                    return True

                if self.catmintfcursegccoamrcovingpvcls is not None:
                    return True

                if self.catmintfendccoamfailedpvcls is not None:
                    return True

                if self.catmintfendccoamrcovedpvcls is not None:
                    return True

                if self.catmintfoamfailedpvcls is not None:
                    return True

                if self.catmintfoamrcovedpvcls is not None:
                    return True

                if self.catmintfsegccoamfailedpvcls is not None:
                    return True

                if self.catmintfsegccoamrcovedpvcls is not None:
                    return True

                if self.catmintftypeofoamfailure is not None:
                    return True

                if self.catmintftypeofoamrecover is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _ATM_MIB as meta
                return meta._meta_table['AtmMib.Atminterfaceconftable.Atminterfaceconfentry']['meta_info']

        @property
        def _common_path(self):

            return '/ATM-MIB:ATM-MIB/ATM-MIB:atmInterfaceConfTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.atminterfaceconfentry is not None:
                for child_ref in self.atminterfaceconfentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _ATM_MIB as meta
            return meta._meta_table['AtmMib.Atminterfaceconftable']['meta_info']


    class Atminterfaceds3Plcptable(object):
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
            self.parent = None
            self.atminterfaceds3plcpentry = YList()
            self.atminterfaceds3plcpentry.parent = self
            self.atminterfaceds3plcpentry.name = 'atminterfaceds3plcpentry'


        class Atminterfaceds3Plcpentry(object):
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
            	**type**\:   :py:class:`Atminterfaceds3PlcpalarmstateEnum <ydk.models.cisco_ios_xe.ATM_MIB.AtmMib.Atminterfaceds3Plcptable.Atminterfaceds3Plcpentry.Atminterfaceds3PlcpalarmstateEnum>`
            
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
                self.parent = None
                self.ifindex = None
                self.atminterfaceds3plcpalarmstate = None
                self.atminterfaceds3plcpsefss = None
                self.atminterfaceds3plcpuass = None

            class Atminterfaceds3PlcpalarmstateEnum(Enum):
                """
                Atminterfaceds3PlcpalarmstateEnum

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

                noAlarm = 1

                receivedFarEndAlarm = 2

                incomingLOF = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _ATM_MIB as meta
                    return meta._meta_table['AtmMib.Atminterfaceds3Plcptable.Atminterfaceds3Plcpentry.Atminterfaceds3PlcpalarmstateEnum']


            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYModelError('Key property ifindex is None')

                return '/ATM-MIB:ATM-MIB/ATM-MIB:atmInterfaceDs3PlcpTable/ATM-MIB:atmInterfaceDs3PlcpEntry[ATM-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ifindex is not None:
                    return True

                if self.atminterfaceds3plcpalarmstate is not None:
                    return True

                if self.atminterfaceds3plcpsefss is not None:
                    return True

                if self.atminterfaceds3plcpuass is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _ATM_MIB as meta
                return meta._meta_table['AtmMib.Atminterfaceds3Plcptable.Atminterfaceds3Plcpentry']['meta_info']

        @property
        def _common_path(self):

            return '/ATM-MIB:ATM-MIB/ATM-MIB:atmInterfaceDs3PlcpTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.atminterfaceds3plcpentry is not None:
                for child_ref in self.atminterfaceds3plcpentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _ATM_MIB as meta
            return meta._meta_table['AtmMib.Atminterfaceds3Plcptable']['meta_info']


    class Atminterfacetctable(object):
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
            self.parent = None
            self.atminterfacetcentry = YList()
            self.atminterfacetcentry.parent = self
            self.atminterfacetcentry.name = 'atminterfacetcentry'


        class Atminterfacetcentry(object):
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
            	**type**\:   :py:class:`AtminterfacetcalarmstateEnum <ydk.models.cisco_ios_xe.ATM_MIB.AtmMib.Atminterfacetctable.Atminterfacetcentry.AtminterfacetcalarmstateEnum>`
            
            

            """

            _prefix = 'ATM-MIB'
            _revision = '1998-10-19'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.atminterfaceocdevents = None
                self.atminterfacetcalarmstate = None

            class AtminterfacetcalarmstateEnum(Enum):
                """
                AtminterfacetcalarmstateEnum

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

                noAlarm = 1

                lcdFailure = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _ATM_MIB as meta
                    return meta._meta_table['AtmMib.Atminterfacetctable.Atminterfacetcentry.AtminterfacetcalarmstateEnum']


            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYModelError('Key property ifindex is None')

                return '/ATM-MIB:ATM-MIB/ATM-MIB:atmInterfaceTCTable/ATM-MIB:atmInterfaceTCEntry[ATM-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ifindex is not None:
                    return True

                if self.atminterfaceocdevents is not None:
                    return True

                if self.atminterfacetcalarmstate is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _ATM_MIB as meta
                return meta._meta_table['AtmMib.Atminterfacetctable.Atminterfacetcentry']['meta_info']

        @property
        def _common_path(self):

            return '/ATM-MIB:ATM-MIB/ATM-MIB:atmInterfaceTCTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.atminterfacetcentry is not None:
                for child_ref in self.atminterfacetcentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _ATM_MIB as meta
            return meta._meta_table['AtmMib.Atminterfacetctable']['meta_info']


    class Atmtrafficdescrparamtable(object):
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
            self.parent = None
            self.atmtrafficdescrparamentry = YList()
            self.atmtrafficdescrparamentry.parent = self
            self.atmtrafficdescrparamentry.name = 'atmtrafficdescrparamentry'


        class Atmtrafficdescrparamentry(object):
            """
            This list contains ATM traffic descriptor
            type and the associated parameters.
            
            .. attribute:: atmtrafficdescrparamindex  <key>
            
            	This object is used by the virtual link table (i.e., VPL or VCL table) to identify the row of this table. When creating a new row in the table the value of this index may be obtained by retrieving the value of atmTrafficDescrParamIndexNext
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: atmservicecategory
            
            	The ATM service category
            	**type**\:   :py:class:`AtmservicecategoryEnum <ydk.models.cisco_ios_xe.ATM_TC_MIB.AtmservicecategoryEnum>`
            
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
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
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
                self.parent = None
                self.atmtrafficdescrparamindex = None
                self.atmservicecategory = None
                self.atmtrafficdescrparam1 = None
                self.atmtrafficdescrparam2 = None
                self.atmtrafficdescrparam3 = None
                self.atmtrafficdescrparam4 = None
                self.atmtrafficdescrparam5 = None
                self.atmtrafficdescrrowstatus = None
                self.atmtrafficdescrtype = None
                self.atmtrafficframediscard = None
                self.atmtrafficqosclass = None

            @property
            def _common_path(self):
                if self.atmtrafficdescrparamindex is None:
                    raise YPYModelError('Key property atmtrafficdescrparamindex is None')

                return '/ATM-MIB:ATM-MIB/ATM-MIB:atmTrafficDescrParamTable/ATM-MIB:atmTrafficDescrParamEntry[ATM-MIB:atmTrafficDescrParamIndex = ' + str(self.atmtrafficdescrparamindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.atmtrafficdescrparamindex is not None:
                    return True

                if self.atmservicecategory is not None:
                    return True

                if self.atmtrafficdescrparam1 is not None:
                    return True

                if self.atmtrafficdescrparam2 is not None:
                    return True

                if self.atmtrafficdescrparam3 is not None:
                    return True

                if self.atmtrafficdescrparam4 is not None:
                    return True

                if self.atmtrafficdescrparam5 is not None:
                    return True

                if self.atmtrafficdescrrowstatus is not None:
                    return True

                if self.atmtrafficdescrtype is not None:
                    return True

                if self.atmtrafficframediscard is not None:
                    return True

                if self.atmtrafficqosclass is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _ATM_MIB as meta
                return meta._meta_table['AtmMib.Atmtrafficdescrparamtable.Atmtrafficdescrparamentry']['meta_info']

        @property
        def _common_path(self):

            return '/ATM-MIB:ATM-MIB/ATM-MIB:atmTrafficDescrParamTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.atmtrafficdescrparamentry is not None:
                for child_ref in self.atmtrafficdescrparamentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _ATM_MIB as meta
            return meta._meta_table['AtmMib.Atmtrafficdescrparamtable']['meta_info']


    class Atmvpltable(object):
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
            self.parent = None
            self.atmvplentry = YList()
            self.atmvplentry.parent = self
            self.atmvplentry.name = 'atmvplentry'


        class Atmvplentry(object):
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
            	**type**\:   :py:class:`AtmvorxadminstatusEnum <ydk.models.cisco_ios_xe.ATM_TC_MIB.AtmvorxadminstatusEnum>`
            
            .. attribute:: atmvplcasttype
            
            	The connection topology type
            	**type**\:   :py:class:`AtmconncasttypeEnum <ydk.models.cisco_ios_xe.ATM_TC_MIB.AtmconncasttypeEnum>`
            
            .. attribute:: atmvplconnkind
            
            	The use of call control
            	**type**\:   :py:class:`AtmconnkindEnum <ydk.models.cisco_ios_xe.ATM_TC_MIB.AtmconnkindEnum>`
            
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
            	**type**\:   :py:class:`AtmvorxoperstatusEnum <ydk.models.cisco_ios_xe.ATM_TC_MIB.AtmvorxoperstatusEnum>`
            
            .. attribute:: atmvplreceivetrafficdescrindex
            
            	The value of this object identifies the row in the atmTrafficDescrParamTable which applies to the receive direction of the VPL
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: atmvplrowstatus
            
            	This object is used to create, delete or modify a row in this table. To create a new VCL, this object is initially set to 'createAndWait' or 'createAndGo'.  This object should not be set to 'active' unless the following columnar objects have been set to their desired value in this row\: atmVplReceiveTrafficDescrIndex and atmVplTransmitTrafficDescrIndex. The DESCRIPTION of atmVplEntry provides further guidance to row treatment in this table
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: atmvpltransmittrafficdescrindex
            
            	The value of this object identifies the row in the atmTrafficDescrParamTable which applies to the transmit direction of the VPL
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            

            """

            _prefix = 'ATM-MIB'
            _revision = '1998-10-19'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.atmvplvpi = None
                self.atmvpladminstatus = None
                self.atmvplcasttype = None
                self.atmvplconnkind = None
                self.atmvplcrossconnectidentifier = None
                self.atmvpllastchange = None
                self.atmvploperstatus = None
                self.atmvplreceivetrafficdescrindex = None
                self.atmvplrowstatus = None
                self.atmvpltransmittrafficdescrindex = None

            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYModelError('Key property ifindex is None')
                if self.atmvplvpi is None:
                    raise YPYModelError('Key property atmvplvpi is None')

                return '/ATM-MIB:ATM-MIB/ATM-MIB:atmVplTable/ATM-MIB:atmVplEntry[ATM-MIB:ifIndex = ' + str(self.ifindex) + '][ATM-MIB:atmVplVpi = ' + str(self.atmvplvpi) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ifindex is not None:
                    return True

                if self.atmvplvpi is not None:
                    return True

                if self.atmvpladminstatus is not None:
                    return True

                if self.atmvplcasttype is not None:
                    return True

                if self.atmvplconnkind is not None:
                    return True

                if self.atmvplcrossconnectidentifier is not None:
                    return True

                if self.atmvpllastchange is not None:
                    return True

                if self.atmvploperstatus is not None:
                    return True

                if self.atmvplreceivetrafficdescrindex is not None:
                    return True

                if self.atmvplrowstatus is not None:
                    return True

                if self.atmvpltransmittrafficdescrindex is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _ATM_MIB as meta
                return meta._meta_table['AtmMib.Atmvpltable.Atmvplentry']['meta_info']

        @property
        def _common_path(self):

            return '/ATM-MIB:ATM-MIB/ATM-MIB:atmVplTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.atmvplentry is not None:
                for child_ref in self.atmvplentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _ATM_MIB as meta
            return meta._meta_table['AtmMib.Atmvpltable']['meta_info']


    class Atmvcltable(object):
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
            self.parent = None
            self.atmvclentry = YList()
            self.atmvclentry.parent = self
            self.atmvclentry.name = 'atmvclentry'


        class Atmvclentry(object):
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
            	**type**\:   :py:class:`Atmvccaal5EncapstypeEnum <ydk.models.cisco_ios_xe.ATM_MIB.AtmMib.Atmvcltable.Atmvclentry.Atmvccaal5EncapstypeEnum>`
            
            .. attribute:: atmvccaaltype
            
            	An instance of this object only exists when the local VCL end\-point is also the VCC end\-point, and AAL is in use. The type of AAL used on this VCC. The AAL type includes AAL1, AAL2, AAL3/4, and AAL5. The other(4) may be user\-defined AAL type.  The unknown type indicates that the AAL type cannot be determined
            	**type**\:   :py:class:`AtmvccaaltypeEnum <ydk.models.cisco_ios_xe.ATM_MIB.AtmMib.Atmvcltable.Atmvclentry.AtmvccaaltypeEnum>`
            
            .. attribute:: atmvcladminstatus
            
            	This object is instanciated only for a VCL which terminates a VCC (i.e., one which is NOT cross\-connected to other VCLs). Its value specifies the desired administrative state of the VCL
            	**type**\:   :py:class:`AtmvorxadminstatusEnum <ydk.models.cisco_ios_xe.ATM_TC_MIB.AtmvorxadminstatusEnum>`
            
            .. attribute:: atmvclcasttype
            
            	The connection topology type
            	**type**\:   :py:class:`AtmconncasttypeEnum <ydk.models.cisco_ios_xe.ATM_TC_MIB.AtmconncasttypeEnum>`
            
            .. attribute:: atmvclconnkind
            
            	The use of call control
            	**type**\:   :py:class:`AtmconnkindEnum <ydk.models.cisco_ios_xe.ATM_TC_MIB.AtmconnkindEnum>`
            
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
            	**type**\:   :py:class:`AtmvorxoperstatusEnum <ydk.models.cisco_ios_xe.ATM_TC_MIB.AtmvorxoperstatusEnum>`
            
            .. attribute:: atmvclreceivetrafficdescrindex
            
            	The value of this object identifies the row in the ATM Traffic Descriptor Table which applies to the receive direction of this VCL
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: atmvclrowstatus
            
            	This object is used to create, delete or modify a row in this table.  To create a new VCL, this object is initially set to 'createAndWait' or 'createAndGo'. This object should not be set to 'active' unless the following columnar objects have been set to their desired value in this row\: atmVclReceiveTrafficDescrIndex, atmVclTransmitTrafficDescrIndex. In addition, if the local VCL end\-point is also the VCC end\-point\: atmVccAalType. In addition, for AAL5 connections only\: atmVccAal5CpcsTransmitSduSize, atmVccAal5CpcsReceiveSduSize, and atmVccAal5EncapsType. (The existence of these objects imply the AAL connection type.). The DESCRIPTION of atmVclEntry provides further guidance to row treatment in this table
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
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
            	**type**\:   :py:class:`OamccstatusEnum <ydk.models.cisco_ios_xe.CISCO_ATM_EXT_MIB.OamccstatusEnum>`
            
            .. attribute:: catmxvcloamendccvcstate
            
            	Indicates OAM End\-to\-end Continuity check (CC)  VC state
            	**type**\:   :py:class:`OamccvcstateEnum <ydk.models.cisco_ios_xe.CISCO_ATM_EXT_MIB.OamccvcstateEnum>`
            
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
            	**type**\:   :py:class:`CatmxvcloamloopbkstatusEnum <ydk.models.cisco_ios_xe.ATM_MIB.AtmMib.Atmvcltable.Atmvclentry.CatmxvcloamloopbkstatusEnum>`
            
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
            	**type**\:   :py:class:`OamccstatusEnum <ydk.models.cisco_ios_xe.CISCO_ATM_EXT_MIB.OamccstatusEnum>`
            
            .. attribute:: catmxvcloamsegccvcstate
            
            	Indicates OAM Segment Continuity check (CC) VC  state
            	**type**\:   :py:class:`OamccvcstateEnum <ydk.models.cisco_ios_xe.CISCO_ATM_EXT_MIB.OamccvcstateEnum>`
            
            .. attribute:: catmxvcloamupretrycount
            
            	Specifies OAM retry count before declaring a VC  is up
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmxvcloamvcstate
            
            	Indicates the state of VC OAM. downRetry(1)   \-\-  Loopback failed. Retry sending                     loopbacks with retry frequency.                     VC is up. verified(2)    \-\-  Loopback is successful. notVerified(3) \-\-  Not verified by loopback,                     AIS/RDI conditions are cleared. upRetry(4)     \-\-  Retry successive loopbacks.                     VC is down. aisRDI(5)      \-\-  Received AIS/RDI. Loopback are                     not sent in this state. aisOut(6)      \-\-  Sending AIS. Loopback and reply are                     not sent in this state. notManaged(7)  \-\-  VC is not managed by OAM
            	**type**\:   :py:class:`CatmxvcloamvcstateEnum <ydk.models.cisco_ios_xe.ATM_MIB.AtmMib.Atmvcltable.Atmvclentry.CatmxvcloamvcstateEnum>`
            
            

            """

            _prefix = 'ATM-MIB'
            _revision = '1998-10-19'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.atmvclvpi = None
                self.atmvclvci = None
                self.atmvccaal5cpcsreceivesdusize = None
                self.atmvccaal5cpcstransmitsdusize = None
                self.atmvccaal5encapstype = None
                self.atmvccaaltype = None
                self.atmvcladminstatus = None
                self.atmvclcasttype = None
                self.atmvclconnkind = None
                self.atmvclcrossconnectidentifier = None
                self.atmvcllastchange = None
                self.atmvcloperstatus = None
                self.atmvclreceivetrafficdescrindex = None
                self.atmvclrowstatus = None
                self.atmvcltransmittrafficdescrindex = None
                self.catmxvcloamcellsdropped = None
                self.catmxvcloamcellsreceived = None
                self.catmxvcloamcellssent = None
                self.catmxvcloamdownretrycount = None
                self.catmxvcloamendccactcount = None
                self.catmxvcloamendccdeactcount = None
                self.catmxvcloamendccretryfreq = None
                self.catmxvcloamendccstatus = None
                self.catmxvcloamendccvcstate = None
                self.catmxvcloaminf5ais = None
                self.catmxvcloaminf5rdi = None
                self.catmxvcloamloopbackfreq = None
                self.catmxvcloamloopbkstatus = None
                self.catmxvcloammanage = None
                self.catmxvcloamoutf5ais = None
                self.catmxvcloamoutf5rdi = None
                self.catmxvcloamretryfreq = None
                self.catmxvcloamsegccactcount = None
                self.catmxvcloamsegccdeactcount = None
                self.catmxvcloamsegccretryfreq = None
                self.catmxvcloamsegccstatus = None
                self.catmxvcloamsegccvcstate = None
                self.catmxvcloamupretrycount = None
                self.catmxvcloamvcstate = None

            class Atmvccaal5EncapstypeEnum(Enum):
                """
                Atmvccaal5EncapstypeEnum

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

                vcMultiplexRoutedProtocol = 1

                vcMultiplexBridgedProtocol8023 = 2

                vcMultiplexBridgedProtocol8025 = 3

                vcMultiplexBridgedProtocol8026 = 4

                vcMultiplexLANemulation8023 = 5

                vcMultiplexLANemulation8025 = 6

                llcEncapsulation = 7

                multiprotocolFrameRelaySscs = 8

                other = 9

                unknown = 10


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _ATM_MIB as meta
                    return meta._meta_table['AtmMib.Atmvcltable.Atmvclentry.Atmvccaal5EncapstypeEnum']


            class AtmvccaaltypeEnum(Enum):
                """
                AtmvccaaltypeEnum

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

                aal1 = 1

                aal34 = 2

                aal5 = 3

                other = 4

                unknown = 5

                aal2 = 6


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _ATM_MIB as meta
                    return meta._meta_table['AtmMib.Atmvcltable.Atmvclentry.AtmvccaaltypeEnum']


            class CatmxvcloamloopbkstatusEnum(Enum):
                """
                CatmxvcloamloopbkstatusEnum

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

                disabled = 1

                sent = 2

                received = 3

                failed = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _ATM_MIB as meta
                    return meta._meta_table['AtmMib.Atmvcltable.Atmvclentry.CatmxvcloamloopbkstatusEnum']


            class CatmxvcloamvcstateEnum(Enum):
                """
                CatmxvcloamvcstateEnum

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

                downRetry = 1

                verified = 2

                notVerified = 3

                upRetry = 4

                aisRDI = 5

                aisOut = 6

                notManaged = 7


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _ATM_MIB as meta
                    return meta._meta_table['AtmMib.Atmvcltable.Atmvclentry.CatmxvcloamvcstateEnum']


            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYModelError('Key property ifindex is None')
                if self.atmvclvpi is None:
                    raise YPYModelError('Key property atmvclvpi is None')
                if self.atmvclvci is None:
                    raise YPYModelError('Key property atmvclvci is None')

                return '/ATM-MIB:ATM-MIB/ATM-MIB:atmVclTable/ATM-MIB:atmVclEntry[ATM-MIB:ifIndex = ' + str(self.ifindex) + '][ATM-MIB:atmVclVpi = ' + str(self.atmvclvpi) + '][ATM-MIB:atmVclVci = ' + str(self.atmvclvci) + ']'

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

                if self.atmvccaal5cpcsreceivesdusize is not None:
                    return True

                if self.atmvccaal5cpcstransmitsdusize is not None:
                    return True

                if self.atmvccaal5encapstype is not None:
                    return True

                if self.atmvccaaltype is not None:
                    return True

                if self.atmvcladminstatus is not None:
                    return True

                if self.atmvclcasttype is not None:
                    return True

                if self.atmvclconnkind is not None:
                    return True

                if self.atmvclcrossconnectidentifier is not None:
                    return True

                if self.atmvcllastchange is not None:
                    return True

                if self.atmvcloperstatus is not None:
                    return True

                if self.atmvclreceivetrafficdescrindex is not None:
                    return True

                if self.atmvclrowstatus is not None:
                    return True

                if self.atmvcltransmittrafficdescrindex is not None:
                    return True

                if self.catmxvcloamcellsdropped is not None:
                    return True

                if self.catmxvcloamcellsreceived is not None:
                    return True

                if self.catmxvcloamcellssent is not None:
                    return True

                if self.catmxvcloamdownretrycount is not None:
                    return True

                if self.catmxvcloamendccactcount is not None:
                    return True

                if self.catmxvcloamendccdeactcount is not None:
                    return True

                if self.catmxvcloamendccretryfreq is not None:
                    return True

                if self.catmxvcloamendccstatus is not None:
                    return True

                if self.catmxvcloamendccvcstate is not None:
                    return True

                if self.catmxvcloaminf5ais is not None:
                    return True

                if self.catmxvcloaminf5rdi is not None:
                    return True

                if self.catmxvcloamloopbackfreq is not None:
                    return True

                if self.catmxvcloamloopbkstatus is not None:
                    return True

                if self.catmxvcloammanage is not None:
                    return True

                if self.catmxvcloamoutf5ais is not None:
                    return True

                if self.catmxvcloamoutf5rdi is not None:
                    return True

                if self.catmxvcloamretryfreq is not None:
                    return True

                if self.catmxvcloamsegccactcount is not None:
                    return True

                if self.catmxvcloamsegccdeactcount is not None:
                    return True

                if self.catmxvcloamsegccretryfreq is not None:
                    return True

                if self.catmxvcloamsegccstatus is not None:
                    return True

                if self.catmxvcloamsegccvcstate is not None:
                    return True

                if self.catmxvcloamupretrycount is not None:
                    return True

                if self.catmxvcloamvcstate is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _ATM_MIB as meta
                return meta._meta_table['AtmMib.Atmvcltable.Atmvclentry']['meta_info']

        @property
        def _common_path(self):

            return '/ATM-MIB:ATM-MIB/ATM-MIB:atmVclTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.atmvclentry is not None:
                for child_ref in self.atmvclentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _ATM_MIB as meta
            return meta._meta_table['AtmMib.Atmvcltable']['meta_info']


    class Atmvpcrossconnecttable(object):
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
            self.parent = None
            self.atmvpcrossconnectentry = YList()
            self.atmvpcrossconnectentry.parent = self
            self.atmvpcrossconnectentry.name = 'atmvpcrossconnectentry'


        class Atmvpcrossconnectentry(object):
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
            	**type**\:   :py:class:`AtmvorxadminstatusEnum <ydk.models.cisco_ios_xe.ATM_TC_MIB.AtmvorxadminstatusEnum>`
            
            .. attribute:: atmvpcrossconnecth2llastchange
            
            	The value of sysUpTime at the time this VP cross\-connect entered its current operational in the high to low direction
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: atmvpcrossconnecth2loperstatus
            
            	The operational status of the VP cross\-connect in one direction; (i.e., from the high to low direction)
            	**type**\:   :py:class:`AtmvorxoperstatusEnum <ydk.models.cisco_ios_xe.ATM_TC_MIB.AtmvorxoperstatusEnum>`
            
            .. attribute:: atmvpcrossconnectl2hlastchange
            
            	The value of sysUpTime at the time this VP cross\-connect entered its current operational state in the low to high direction
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: atmvpcrossconnectl2hoperstatus
            
            	The operational status of the VP cross\-connect in one direction; (i.e., from the low to high direction)
            	**type**\:   :py:class:`AtmvorxoperstatusEnum <ydk.models.cisco_ios_xe.ATM_TC_MIB.AtmvorxoperstatusEnum>`
            
            .. attribute:: atmvpcrossconnectrowstatus
            
            	The status of this entry in the atmVpCrossConnectTable.  This object is used to create a cross\-connect for cross\-connecting VPLs which are created using the atmVplTable or to change or delete an existing cross\-connect. This object must be initially set to `createAndWait' or 'createAndGo'. To turn on a VP cross\-connect, the atmVpCrossConnectAdminStatus is set to `up'
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            

            """

            _prefix = 'ATM-MIB'
            _revision = '1998-10-19'

            def __init__(self):
                self.parent = None
                self.atmvpcrossconnectindex = None
                self.atmvpcrossconnectlowifindex = None
                self.atmvpcrossconnectlowvpi = None
                self.atmvpcrossconnecthighifindex = None
                self.atmvpcrossconnecthighvpi = None
                self.atmvpcrossconnectadminstatus = None
                self.atmvpcrossconnecth2llastchange = None
                self.atmvpcrossconnecth2loperstatus = None
                self.atmvpcrossconnectl2hlastchange = None
                self.atmvpcrossconnectl2hoperstatus = None
                self.atmvpcrossconnectrowstatus = None

            @property
            def _common_path(self):
                if self.atmvpcrossconnectindex is None:
                    raise YPYModelError('Key property atmvpcrossconnectindex is None')
                if self.atmvpcrossconnectlowifindex is None:
                    raise YPYModelError('Key property atmvpcrossconnectlowifindex is None')
                if self.atmvpcrossconnectlowvpi is None:
                    raise YPYModelError('Key property atmvpcrossconnectlowvpi is None')
                if self.atmvpcrossconnecthighifindex is None:
                    raise YPYModelError('Key property atmvpcrossconnecthighifindex is None')
                if self.atmvpcrossconnecthighvpi is None:
                    raise YPYModelError('Key property atmvpcrossconnecthighvpi is None')

                return '/ATM-MIB:ATM-MIB/ATM-MIB:atmVpCrossConnectTable/ATM-MIB:atmVpCrossConnectEntry[ATM-MIB:atmVpCrossConnectIndex = ' + str(self.atmvpcrossconnectindex) + '][ATM-MIB:atmVpCrossConnectLowIfIndex = ' + str(self.atmvpcrossconnectlowifindex) + '][ATM-MIB:atmVpCrossConnectLowVpi = ' + str(self.atmvpcrossconnectlowvpi) + '][ATM-MIB:atmVpCrossConnectHighIfIndex = ' + str(self.atmvpcrossconnecthighifindex) + '][ATM-MIB:atmVpCrossConnectHighVpi = ' + str(self.atmvpcrossconnecthighvpi) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.atmvpcrossconnectindex is not None:
                    return True

                if self.atmvpcrossconnectlowifindex is not None:
                    return True

                if self.atmvpcrossconnectlowvpi is not None:
                    return True

                if self.atmvpcrossconnecthighifindex is not None:
                    return True

                if self.atmvpcrossconnecthighvpi is not None:
                    return True

                if self.atmvpcrossconnectadminstatus is not None:
                    return True

                if self.atmvpcrossconnecth2llastchange is not None:
                    return True

                if self.atmvpcrossconnecth2loperstatus is not None:
                    return True

                if self.atmvpcrossconnectl2hlastchange is not None:
                    return True

                if self.atmvpcrossconnectl2hoperstatus is not None:
                    return True

                if self.atmvpcrossconnectrowstatus is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _ATM_MIB as meta
                return meta._meta_table['AtmMib.Atmvpcrossconnecttable.Atmvpcrossconnectentry']['meta_info']

        @property
        def _common_path(self):

            return '/ATM-MIB:ATM-MIB/ATM-MIB:atmVpCrossConnectTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.atmvpcrossconnectentry is not None:
                for child_ref in self.atmvpcrossconnectentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _ATM_MIB as meta
            return meta._meta_table['AtmMib.Atmvpcrossconnecttable']['meta_info']


    class Atmvccrossconnecttable(object):
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
            self.parent = None
            self.atmvccrossconnectentry = YList()
            self.atmvccrossconnectentry.parent = self
            self.atmvccrossconnectentry.name = 'atmvccrossconnectentry'


        class Atmvccrossconnectentry(object):
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
            	**type**\:   :py:class:`AtmvorxadminstatusEnum <ydk.models.cisco_ios_xe.ATM_TC_MIB.AtmvorxadminstatusEnum>`
            
            .. attribute:: atmvccrossconnecth2llastchange
            
            	The value of sysUpTime at the time this VC cross\-connect entered its current operational state in high to low direction
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: atmvccrossconnecth2loperstatus
            
            	The current operational status of the VC cross\-connect in one direction; (i.e., from the high to low direction)
            	**type**\:   :py:class:`AtmvorxoperstatusEnum <ydk.models.cisco_ios_xe.ATM_TC_MIB.AtmvorxoperstatusEnum>`
            
            .. attribute:: atmvccrossconnectl2hlastchange
            
            	The value of sysUpTime at the time this VC cross\-connect entered its current operational state in low to high direction
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: atmvccrossconnectl2hoperstatus
            
            	The current operational status of the VC cross\-connect in one direction; (i.e., from the low to high direction)
            	**type**\:   :py:class:`AtmvorxoperstatusEnum <ydk.models.cisco_ios_xe.ATM_TC_MIB.AtmvorxoperstatusEnum>`
            
            .. attribute:: atmvccrossconnectrowstatus
            
            	The status of this entry in the atmVcCrossConnectTable.  This object is used to create a new cross\-connect for cross\-connecting VCLs which are created using the atmVclTable or to change or delete existing cross\-connect. This object must be initially set to `createAndWait' or 'createAndGo'. To turn on a VC cross\-connect, the atmVcCrossConnectAdminStatus is set to `up'
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            

            """

            _prefix = 'ATM-MIB'
            _revision = '1998-10-19'

            def __init__(self):
                self.parent = None
                self.atmvccrossconnectindex = None
                self.atmvccrossconnectlowifindex = None
                self.atmvccrossconnectlowvpi = None
                self.atmvccrossconnectlowvci = None
                self.atmvccrossconnecthighifindex = None
                self.atmvccrossconnecthighvpi = None
                self.atmvccrossconnecthighvci = None
                self.atmvccrossconnectadminstatus = None
                self.atmvccrossconnecth2llastchange = None
                self.atmvccrossconnecth2loperstatus = None
                self.atmvccrossconnectl2hlastchange = None
                self.atmvccrossconnectl2hoperstatus = None
                self.atmvccrossconnectrowstatus = None

            @property
            def _common_path(self):
                if self.atmvccrossconnectindex is None:
                    raise YPYModelError('Key property atmvccrossconnectindex is None')
                if self.atmvccrossconnectlowifindex is None:
                    raise YPYModelError('Key property atmvccrossconnectlowifindex is None')
                if self.atmvccrossconnectlowvpi is None:
                    raise YPYModelError('Key property atmvccrossconnectlowvpi is None')
                if self.atmvccrossconnectlowvci is None:
                    raise YPYModelError('Key property atmvccrossconnectlowvci is None')
                if self.atmvccrossconnecthighifindex is None:
                    raise YPYModelError('Key property atmvccrossconnecthighifindex is None')
                if self.atmvccrossconnecthighvpi is None:
                    raise YPYModelError('Key property atmvccrossconnecthighvpi is None')
                if self.atmvccrossconnecthighvci is None:
                    raise YPYModelError('Key property atmvccrossconnecthighvci is None')

                return '/ATM-MIB:ATM-MIB/ATM-MIB:atmVcCrossConnectTable/ATM-MIB:atmVcCrossConnectEntry[ATM-MIB:atmVcCrossConnectIndex = ' + str(self.atmvccrossconnectindex) + '][ATM-MIB:atmVcCrossConnectLowIfIndex = ' + str(self.atmvccrossconnectlowifindex) + '][ATM-MIB:atmVcCrossConnectLowVpi = ' + str(self.atmvccrossconnectlowvpi) + '][ATM-MIB:atmVcCrossConnectLowVci = ' + str(self.atmvccrossconnectlowvci) + '][ATM-MIB:atmVcCrossConnectHighIfIndex = ' + str(self.atmvccrossconnecthighifindex) + '][ATM-MIB:atmVcCrossConnectHighVpi = ' + str(self.atmvccrossconnecthighvpi) + '][ATM-MIB:atmVcCrossConnectHighVci = ' + str(self.atmvccrossconnecthighvci) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.atmvccrossconnectindex is not None:
                    return True

                if self.atmvccrossconnectlowifindex is not None:
                    return True

                if self.atmvccrossconnectlowvpi is not None:
                    return True

                if self.atmvccrossconnectlowvci is not None:
                    return True

                if self.atmvccrossconnecthighifindex is not None:
                    return True

                if self.atmvccrossconnecthighvpi is not None:
                    return True

                if self.atmvccrossconnecthighvci is not None:
                    return True

                if self.atmvccrossconnectadminstatus is not None:
                    return True

                if self.atmvccrossconnecth2llastchange is not None:
                    return True

                if self.atmvccrossconnecth2loperstatus is not None:
                    return True

                if self.atmvccrossconnectl2hlastchange is not None:
                    return True

                if self.atmvccrossconnectl2hoperstatus is not None:
                    return True

                if self.atmvccrossconnectrowstatus is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _ATM_MIB as meta
                return meta._meta_table['AtmMib.Atmvccrossconnecttable.Atmvccrossconnectentry']['meta_info']

        @property
        def _common_path(self):

            return '/ATM-MIB:ATM-MIB/ATM-MIB:atmVcCrossConnectTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.atmvccrossconnectentry is not None:
                for child_ref in self.atmvccrossconnectentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _ATM_MIB as meta
            return meta._meta_table['AtmMib.Atmvccrossconnecttable']['meta_info']


    class Aal5Vcctable(object):
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
            self.parent = None
            self.aal5vccentry = YList()
            self.aal5vccentry.parent = self
            self.aal5vccentry.name = 'aal5vccentry'


        class Aal5Vccentry(object):
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
                self.parent = None
                self.ifindex = None
                self.aal5vccvpi = None
                self.aal5vccvci = None
                self.aal5vcccrcerrors = None
                self.aal5vccoversizedsdus = None
                self.aal5vccsartimeouts = None
                self.caal5vccextcompenabled = None
                self.caal5vccextinf5oamcells = None
                self.caal5vccextoutf5oamcells = None
                self.caal5vccextvoice = None
                self.caal5vcchcinoctets = None
                self.caal5vcchcinpkts = None
                self.caal5vcchcoutoctets = None
                self.caal5vcchcoutpkts = None
                self.caal5vccindroppedoctets = None
                self.caal5vccindroppedpkts = None
                self.caal5vccinoctets = None
                self.caal5vccinpkts = None
                self.caal5vccoutdroppedoctets = None
                self.caal5vccoutdroppedpkts = None
                self.caal5vccoutoctets = None
                self.caal5vccoutpkts = None

            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYModelError('Key property ifindex is None')
                if self.aal5vccvpi is None:
                    raise YPYModelError('Key property aal5vccvpi is None')
                if self.aal5vccvci is None:
                    raise YPYModelError('Key property aal5vccvci is None')

                return '/ATM-MIB:ATM-MIB/ATM-MIB:aal5VccTable/ATM-MIB:aal5VccEntry[ATM-MIB:ifIndex = ' + str(self.ifindex) + '][ATM-MIB:aal5VccVpi = ' + str(self.aal5vccvpi) + '][ATM-MIB:aal5VccVci = ' + str(self.aal5vccvci) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ifindex is not None:
                    return True

                if self.aal5vccvpi is not None:
                    return True

                if self.aal5vccvci is not None:
                    return True

                if self.aal5vcccrcerrors is not None:
                    return True

                if self.aal5vccoversizedsdus is not None:
                    return True

                if self.aal5vccsartimeouts is not None:
                    return True

                if self.caal5vccextcompenabled is not None:
                    return True

                if self.caal5vccextinf5oamcells is not None:
                    return True

                if self.caal5vccextoutf5oamcells is not None:
                    return True

                if self.caal5vccextvoice is not None:
                    return True

                if self.caal5vcchcinoctets is not None:
                    return True

                if self.caal5vcchcinpkts is not None:
                    return True

                if self.caal5vcchcoutoctets is not None:
                    return True

                if self.caal5vcchcoutpkts is not None:
                    return True

                if self.caal5vccindroppedoctets is not None:
                    return True

                if self.caal5vccindroppedpkts is not None:
                    return True

                if self.caal5vccinoctets is not None:
                    return True

                if self.caal5vccinpkts is not None:
                    return True

                if self.caal5vccoutdroppedoctets is not None:
                    return True

                if self.caal5vccoutdroppedpkts is not None:
                    return True

                if self.caal5vccoutoctets is not None:
                    return True

                if self.caal5vccoutpkts is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _ATM_MIB as meta
                return meta._meta_table['AtmMib.Aal5Vcctable.Aal5Vccentry']['meta_info']

        @property
        def _common_path(self):

            return '/ATM-MIB:ATM-MIB/ATM-MIB:aal5VccTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.aal5vccentry is not None:
                for child_ref in self.aal5vccentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _ATM_MIB as meta
            return meta._meta_table['AtmMib.Aal5Vcctable']['meta_info']

    @property
    def _common_path(self):

        return '/ATM-MIB:ATM-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.aal5vcctable is not None and self.aal5vcctable._has_data():
            return True

        if self.atminterfaceconftable is not None and self.atminterfaceconftable._has_data():
            return True

        if self.atminterfaceds3plcptable is not None and self.atminterfaceds3plcptable._has_data():
            return True

        if self.atminterfacetctable is not None and self.atminterfacetctable._has_data():
            return True

        if self.atmmibobjects is not None and self.atmmibobjects._has_data():
            return True

        if self.atmtrafficdescrparamtable is not None and self.atmtrafficdescrparamtable._has_data():
            return True

        if self.atmvccrossconnecttable is not None and self.atmvccrossconnecttable._has_data():
            return True

        if self.atmvcltable is not None and self.atmvcltable._has_data():
            return True

        if self.atmvpcrossconnecttable is not None and self.atmvpcrossconnecttable._has_data():
            return True

        if self.atmvpltable is not None and self.atmvpltable._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _ATM_MIB as meta
        return meta._meta_table['AtmMib']['meta_info']


