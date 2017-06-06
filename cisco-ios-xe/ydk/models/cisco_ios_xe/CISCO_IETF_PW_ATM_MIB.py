""" CISCO_IETF_PW_ATM_MIB 

This MIB contains managed object definitions for Pseudo Wire
emulation of ATM over Packet Switched Networks(PSN).

This MIB reports to the PW\-MIB. The PW\-MIB contains
structures and MIB associations generic to Pseudo\-Wire
Virtual Circuit (VC) emulation. VC\-specific MIBs (such as
this) contain config and stats for specific VC types.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class CiscoIetfPwAtmMib(object):
    """
    
    
    .. attribute:: cpwvcatmtable
    
    	This table specifies the information for an ATM interface, VC, VP to be carried over PSN
    	**type**\:   :py:class:`Cpwvcatmtable <ydk.models.cisco_ios_xe.CISCO_IETF_PW_ATM_MIB.CiscoIetfPwAtmMib.Cpwvcatmtable>`
    
    

    """

    _prefix = 'CISCO-IETF-PW-ATM-MIB'
    _revision = '2005-04-19'

    def __init__(self):
        self.cpwvcatmtable = CiscoIetfPwAtmMib.Cpwvcatmtable()
        self.cpwvcatmtable.parent = self


    class Cpwvcatmtable(object):
        """
        This table specifies the information for an ATM interface, VC,
        VP to be carried over PSN.
        
        .. attribute:: cpwvcatmentry
        
        	A row in this table represents an ATM interface, VC, VP that needs to be adapted and carried over PSN. This table is indexed by CpwVcIndex in CISCO\-IETF\-PW\-MIB
        	**type**\: list of    :py:class:`Cpwvcatmentry <ydk.models.cisco_ios_xe.CISCO_IETF_PW_ATM_MIB.CiscoIetfPwAtmMib.Cpwvcatmtable.Cpwvcatmentry>`
        
        

        """

        _prefix = 'CISCO-IETF-PW-ATM-MIB'
        _revision = '2005-04-19'

        def __init__(self):
            self.parent = None
            self.cpwvcatmentry = YList()
            self.cpwvcatmentry.parent = self
            self.cpwvcatmentry.name = 'cpwvcatmentry'


        class Cpwvcatmentry(object):
            """
            A row in this table represents an ATM interface, VC, VP
            that needs to be adapted and carried over PSN. This table
            is indexed by CpwVcIndex in CISCO\-IETF\-PW\-MIB.
            
            .. attribute:: cpwvcindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`cpwvcindex <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CiscoIetfPwMib.Cpwvctable.Cpwvcentry>`
            
            .. attribute:: cpwatmavgcellspacked
            
            	It indicates the Average number of cells that were received in one packet
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwatmcellpacking
            
            	This object is used to identify if the VC is configured to do Cell Packing
            	**type**\:  bool
            
            .. attribute:: cpwatmcellsreceived
            
            	This object can be used to obtain the information on the number of cells that were received and sent to the PSN
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwatmcellsrejected
            
            	This Object indicates the number of cells that were rejected by this VC because of policing
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwatmcellssent
            
            	This object can be used to obtain the information on the number of cells that were received from the PSN and sent over the ATM network
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwatmcellstagged
            
            	This Object indicates the number of cells that were Tagged
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwatmclpqosmapping
            
            	This Object indicates whether the CLP bits are considered when determining the value placed in the Quality of Service fields (e.g. EXP fields of the MPLS Label Stack) of the encapsulating protocol
            	**type**\:  bool
            
            .. attribute:: cpwatmencap
            
            	This object indicates if the packet going on the pseudowire is mpls or l2tpv3 encapsulated
            	**type**\:   :py:class:`CpwatmencapEnum <ydk.models.cisco_ios_xe.CISCO_IETF_PW_ATM_MIB.CiscoIetfPwAtmMib.Cpwvcatmtable.Cpwvcatmentry.CpwatmencapEnum>`
            
            .. attribute:: cpwatmhccellsreceived
            
            	High Capacity counter for the number of cells that were received by this VC
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cpwatmhccellsrejected
            
            	High Capacity counter for the number of cells that were rejected by this VC because of policing
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cpwatmhccellstagged
            
            	High Capacity counter for the number of cells that were tagged
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cpwatmif
            
            	The ATM Interface that receives cells from the ATM network
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: cpwatmmcpttimeout
            
            	This Object represents which MCPT timeout value
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: cpwatmmncp
            
            	This object indicates the maximum number of cells that get packed in one packet
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: cpwatmoamcellsupported
            
            	This Object indicates whether OAM Cells are transported on this VC
            	**type**\:  bool
            
            .. attribute:: cpwatmpeermncp
            
            	This Object represents the maximum number of cell that can be packed in one packet for peer interface
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: cpwatmpktsreceived
            
            	This object can be used to obtain the information on the number of packets that were received and sent to the PSN
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwatmpktsrejected
            
            	This object indicates the number of packets that were rejected because of Policing
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwatmpktssent
            
            	This object indicates the number of packets that were sent to the atm network
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwatmqosscalingfactor
            
            	This Object represents the scaling factor (% value) to be applied to ATM QoS rates when calculating QoS rates for the PSN domain . For example, in the cell transport mode the bandwidth needed in the PSN domain will be higher (since PSN Transport header, PW header, and optional control word have to transmitted with every cell), whereas in the AAL5 mode the bandwidth needed in PSN domain will be less since cell headers will be removed after reassembly
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: cpwatmrowstatus
            
            	This Object is used to create, modify or delete a row in this table
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: cpwatmvci
            
            	VCI value of this ATM VC
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: cpwatmvpi
            
            	VPI value of this ATM VC
            	**type**\:  int
            
            	**range:** 0..4095
            
            

            """

            _prefix = 'CISCO-IETF-PW-ATM-MIB'
            _revision = '2005-04-19'

            def __init__(self):
                self.parent = None
                self.cpwvcindex = None
                self.cpwatmavgcellspacked = None
                self.cpwatmcellpacking = None
                self.cpwatmcellsreceived = None
                self.cpwatmcellsrejected = None
                self.cpwatmcellssent = None
                self.cpwatmcellstagged = None
                self.cpwatmclpqosmapping = None
                self.cpwatmencap = None
                self.cpwatmhccellsreceived = None
                self.cpwatmhccellsrejected = None
                self.cpwatmhccellstagged = None
                self.cpwatmif = None
                self.cpwatmmcpttimeout = None
                self.cpwatmmncp = None
                self.cpwatmoamcellsupported = None
                self.cpwatmpeermncp = None
                self.cpwatmpktsreceived = None
                self.cpwatmpktsrejected = None
                self.cpwatmpktssent = None
                self.cpwatmqosscalingfactor = None
                self.cpwatmrowstatus = None
                self.cpwatmvci = None
                self.cpwatmvpi = None

            class CpwatmencapEnum(Enum):
                """
                CpwatmencapEnum

                This object indicates if the packet going on the pseudowire

                is mpls or l2tpv3 encapsulated.

                .. data:: mpls = 1

                .. data:: l2tpv3 = 2

                .. data:: unknown = 3

                """

                mpls = 1

                l2tpv3 = 2

                unknown = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_PW_ATM_MIB as meta
                    return meta._meta_table['CiscoIetfPwAtmMib.Cpwvcatmtable.Cpwvcatmentry.CpwatmencapEnum']


            @property
            def _common_path(self):
                if self.cpwvcindex is None:
                    raise YPYModelError('Key property cpwvcindex is None')

                return '/CISCO-IETF-PW-ATM-MIB:CISCO-IETF-PW-ATM-MIB/CISCO-IETF-PW-ATM-MIB:cpwVcAtmTable/CISCO-IETF-PW-ATM-MIB:cpwVcAtmEntry[CISCO-IETF-PW-ATM-MIB:cpwVcIndex = ' + str(self.cpwvcindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cpwvcindex is not None:
                    return True

                if self.cpwatmavgcellspacked is not None:
                    return True

                if self.cpwatmcellpacking is not None:
                    return True

                if self.cpwatmcellsreceived is not None:
                    return True

                if self.cpwatmcellsrejected is not None:
                    return True

                if self.cpwatmcellssent is not None:
                    return True

                if self.cpwatmcellstagged is not None:
                    return True

                if self.cpwatmclpqosmapping is not None:
                    return True

                if self.cpwatmencap is not None:
                    return True

                if self.cpwatmhccellsreceived is not None:
                    return True

                if self.cpwatmhccellsrejected is not None:
                    return True

                if self.cpwatmhccellstagged is not None:
                    return True

                if self.cpwatmif is not None:
                    return True

                if self.cpwatmmcpttimeout is not None:
                    return True

                if self.cpwatmmncp is not None:
                    return True

                if self.cpwatmoamcellsupported is not None:
                    return True

                if self.cpwatmpeermncp is not None:
                    return True

                if self.cpwatmpktsreceived is not None:
                    return True

                if self.cpwatmpktsrejected is not None:
                    return True

                if self.cpwatmpktssent is not None:
                    return True

                if self.cpwatmqosscalingfactor is not None:
                    return True

                if self.cpwatmrowstatus is not None:
                    return True

                if self.cpwatmvci is not None:
                    return True

                if self.cpwatmvpi is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_PW_ATM_MIB as meta
                return meta._meta_table['CiscoIetfPwAtmMib.Cpwvcatmtable.Cpwvcatmentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IETF-PW-ATM-MIB:CISCO-IETF-PW-ATM-MIB/CISCO-IETF-PW-ATM-MIB:cpwVcAtmTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cpwvcatmentry is not None:
                for child_ref in self.cpwvcatmentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_PW_ATM_MIB as meta
            return meta._meta_table['CiscoIetfPwAtmMib.Cpwvcatmtable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-IETF-PW-ATM-MIB:CISCO-IETF-PW-ATM-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.cpwvcatmtable is not None and self.cpwvcatmtable._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_PW_ATM_MIB as meta
        return meta._meta_table['CiscoIetfPwAtmMib']['meta_info']


