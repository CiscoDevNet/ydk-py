""" CISCO_MVPN_MIB 

This MIB contains managed object definitions for
Cisco implementation of multicast in VPNs defined 
by the Internet draft\: draft\-rosen\-vpn\-mcast\-05.txt. 
Note that this MIB works along with the 
L3VPN\-MPLS\-VPN\-MIB.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.inet.INET_ADDRESS_MIB import InetAddressType_Enum
from ydk.models.snmpv2.SNMPv2_TC import RowStatus_Enum


class CISCOMVPNMIB(object):
    """
    
    
    .. attribute:: ciscomvpnbgpmdtupdatetable
    
    	This table has information about the BGP advertisement of the  the MDT groups. (These advertisements are generated  and used for source discovery when SSM is used.)
    	**type**\: :py:class:`CiscoMvpnBgpMdtUpdateTable <ydk.models.mvpn.CISCO_MVPN_MIB.CISCOMVPNMIB.CiscoMvpnBgpMdtUpdateTable>`
    
    .. attribute:: ciscomvpngenerictable
    
    	This table gives the generic information about the MVRFs  present in this device
    	**type**\: :py:class:`CiscoMvpnGenericTable <ydk.models.mvpn.CISCO_MVPN_MIB.CISCOMVPNMIB.CiscoMvpnGenericTable>`
    
    .. attribute:: ciscomvpnmdtdatatable
    
    	This table specifies the range of data MDT addresses and  associated variables for a MVRF instance
    	**type**\: :py:class:`CiscoMvpnMdtDataTable <ydk.models.mvpn.CISCO_MVPN_MIB.CISCOMVPNMIB.CiscoMvpnMdtDataTable>`
    
    .. attribute:: ciscomvpnmdtdefaulttable
    
    	This table specifies the default MDT address and the  encapsulation type used for a MVRF instance
    	**type**\: :py:class:`CiscoMvpnMdtDefaultTable <ydk.models.mvpn.CISCO_MVPN_MIB.CISCOMVPNMIB.CiscoMvpnMdtDefaultTable>`
    
    .. attribute:: ciscomvpnmdtjnrcvtable
    
    	This table has information about the data MDT join TLVs  received by a device
    	**type**\: :py:class:`CiscoMvpnMdtJnRcvTable <ydk.models.mvpn.CISCO_MVPN_MIB.CISCOMVPNMIB.CiscoMvpnMdtJnRcvTable>`
    
    .. attribute:: ciscomvpnmdtjnsendtable
    
    	This table specifies the data MDT Join TLVs sent by a  device
    	**type**\: :py:class:`CiscoMvpnMdtJnSendTable <ydk.models.mvpn.CISCO_MVPN_MIB.CISCOMVPNMIB.CiscoMvpnMdtJnSendTable>`
    
    .. attribute:: ciscomvpnmroutemdttable
    
    	Given a multicast routing entry and the context MVRF, this  table provides information about the MDT group being used for  encapsulating the traffic for the multicast routing entry in  the provider network at the instance of querying. Note that this table is a read\-only table and is the result of the  default MDT and data MDT configurations and the operational  conditions like the traffic rate and sometimes, the  implementation choices
    	**type**\: :py:class:`CiscoMvpnMrouteMdtTable <ydk.models.mvpn.CISCO_MVPN_MIB.CISCOMVPNMIB.CiscoMvpnMrouteMdtTable>`
    
    .. attribute:: ciscomvpnscalars
    
    	
    	**type**\: :py:class:`CiscoMvpnScalars <ydk.models.mvpn.CISCO_MVPN_MIB.CISCOMVPNMIB.CiscoMvpnScalars>`
    
    .. attribute:: ciscomvpntunneltable
    
    	This table gives information about the MVPN/MDT tunnels  present in the device
    	**type**\: :py:class:`CiscoMvpnTunnelTable <ydk.models.mvpn.CISCO_MVPN_MIB.CISCOMVPNMIB.CiscoMvpnTunnelTable>`
    
    

    """

    _prefix = 'cisco-mvpn'
    _revision = '2004-02-23'

    def __init__(self):
        self.ciscomvpnbgpmdtupdatetable = CISCOMVPNMIB.CiscoMvpnBgpMdtUpdateTable()
        self.ciscomvpnbgpmdtupdatetable.parent = self
        self.ciscomvpngenerictable = CISCOMVPNMIB.CiscoMvpnGenericTable()
        self.ciscomvpngenerictable.parent = self
        self.ciscomvpnmdtdatatable = CISCOMVPNMIB.CiscoMvpnMdtDataTable()
        self.ciscomvpnmdtdatatable.parent = self
        self.ciscomvpnmdtdefaulttable = CISCOMVPNMIB.CiscoMvpnMdtDefaultTable()
        self.ciscomvpnmdtdefaulttable.parent = self
        self.ciscomvpnmdtjnrcvtable = CISCOMVPNMIB.CiscoMvpnMdtJnRcvTable()
        self.ciscomvpnmdtjnrcvtable.parent = self
        self.ciscomvpnmdtjnsendtable = CISCOMVPNMIB.CiscoMvpnMdtJnSendTable()
        self.ciscomvpnmdtjnsendtable.parent = self
        self.ciscomvpnmroutemdttable = CISCOMVPNMIB.CiscoMvpnMrouteMdtTable()
        self.ciscomvpnmroutemdttable.parent = self
        self.ciscomvpnscalars = CISCOMVPNMIB.CiscoMvpnScalars()
        self.ciscomvpnscalars.parent = self
        self.ciscomvpntunneltable = CISCOMVPNMIB.CiscoMvpnTunnelTable()
        self.ciscomvpntunneltable.parent = self


    class CiscoMvpnBgpMdtUpdateTable(object):
        """
        This table has information about the BGP advertisement of the 
        the MDT groups. (These advertisements are generated 
        and used for source discovery when SSM is used.)
        
        .. attribute:: ciscomvpnbgpmdtupdateentry
        
        	An entry in this table is created when a BGP advertisement of  the MDT group is received and cached in the PE device.  An entry in this table deleted when such a cached BGP MDT  update is withdrawn
        	**type**\: list of :py:class:`CiscoMvpnBgpMdtUpdateEntry <ydk.models.mvpn.CISCO_MVPN_MIB.CISCOMVPNMIB.CiscoMvpnBgpMdtUpdateTable.CiscoMvpnBgpMdtUpdateEntry>`
        
        

        """

        _prefix = 'cisco-mvpn'
        _revision = '2004-02-23'

        def __init__(self):
            self.parent = None
            self.ciscomvpnbgpmdtupdateentry = YList()
            self.ciscomvpnbgpmdtupdateentry.parent = self
            self.ciscomvpnbgpmdtupdateentry.name = 'ciscomvpnbgpmdtupdateentry'


        class CiscoMvpnBgpMdtUpdateEntry(object):
            """
            An entry in this table is created when a BGP advertisement of 
            the MDT group is received and cached in the PE device. 
            An entry in this table deleted when such a cached BGP MDT 
            update is withdrawn.
            
            .. attribute:: ciscomvpnbgpmdtupdategroup
            
            	MDT group address in the BGP MDT advertisement
            	**type**\: str
            
            	**range:** 4 \| 16 \| 20
            
            .. attribute:: ciscomvpnbgpmdtupdatesource
            
            	MDT source address in the BGP MDT advertisement
            	**type**\: str
            
            	**range:** 4 \| 16 \| 20
            
            .. attribute:: ciscomvpnbgpmdtupdgrpaddrtype
            
            	The Internet address type of ciscoMvpnBgpMdtUpdateGroup
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: ciscomvpnbgpmdtupdsrcaddrtype
            
            	The Internet address type of ciscoMvpnBgpMdtUpdateSource
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: ciscomvpnbgpmdtupdatenexthop
            
            	The next\-hop address (address of the border router to be used to reach the destination network) in the BGP MDT  advertisement
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: ciscomvpnbgpmdtupdateoriginator
            
            	The BGP peering address of the device that originated (or  advertized) the BGP MDT update
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: ciscomvpnbgpmdtupdaterd
            
            	RD (route distinguisher) in the BGP MDT advertisement. This  is the RD corresponding to the originator PE
            	**type**\: str
            
            	**range:** 0..256
            
            .. attribute:: ciscomvpnbgpmdtupdnhaddrtype
            
            	The Internet address type of ciscoMvpnBgpMdtUpdateNexthop
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: ciscomvpnbgpmdtupdorigaddrtype
            
            	The Internet address type of ciscoMvpnBgpMdtUpdateOriginator
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            

            """

            _prefix = 'cisco-mvpn'
            _revision = '2004-02-23'

            def __init__(self):
                self.parent = None
                self.ciscomvpnbgpmdtupdategroup = None
                self.ciscomvpnbgpmdtupdatesource = None
                self.ciscomvpnbgpmdtupdgrpaddrtype = None
                self.ciscomvpnbgpmdtupdsrcaddrtype = None
                self.ciscomvpnbgpmdtupdatenexthop = None
                self.ciscomvpnbgpmdtupdateoriginator = None
                self.ciscomvpnbgpmdtupdaterd = None
                self.ciscomvpnbgpmdtupdnhaddrtype = None
                self.ciscomvpnbgpmdtupdorigaddrtype = None

            @property
            def _common_path(self):
                if self.ciscomvpnbgpmdtupdategroup is None:
                    raise YPYDataValidationError('Key property ciscomvpnbgpmdtupdategroup is None')
                if self.ciscomvpnbgpmdtupdatesource is None:
                    raise YPYDataValidationError('Key property ciscomvpnbgpmdtupdatesource is None')
                if self.ciscomvpnbgpmdtupdgrpaddrtype is None:
                    raise YPYDataValidationError('Key property ciscomvpnbgpmdtupdgrpaddrtype is None')
                if self.ciscomvpnbgpmdtupdsrcaddrtype is None:
                    raise YPYDataValidationError('Key property ciscomvpnbgpmdtupdsrcaddrtype is None')

                return '/CISCO-MVPN-MIB:CISCO-MVPN-MIB/CISCO-MVPN-MIB:ciscoMvpnBgpMdtUpdateTable/CISCO-MVPN-MIB:ciscoMvpnBgpMdtUpdateEntry[CISCO-MVPN-MIB:ciscoMvpnBgpMdtUpdateGroup = ' + str(self.ciscomvpnbgpmdtupdategroup) + '][CISCO-MVPN-MIB:ciscoMvpnBgpMdtUpdateSource = ' + str(self.ciscomvpnbgpmdtupdatesource) + '][CISCO-MVPN-MIB:ciscoMvpnBgpMdtUpdGrpAddrType = ' + str(self.ciscomvpnbgpmdtupdgrpaddrtype) + '][CISCO-MVPN-MIB:ciscoMvpnBgpMdtUpdSrcAddrType = ' + str(self.ciscomvpnbgpmdtupdsrcaddrtype) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ciscomvpnbgpmdtupdategroup is not None:
                    return True

                if self.ciscomvpnbgpmdtupdatesource is not None:
                    return True

                if self.ciscomvpnbgpmdtupdgrpaddrtype is not None:
                    return True

                if self.ciscomvpnbgpmdtupdsrcaddrtype is not None:
                    return True

                if self.ciscomvpnbgpmdtupdatenexthop is not None:
                    return True

                if self.ciscomvpnbgpmdtupdateoriginator is not None:
                    return True

                if self.ciscomvpnbgpmdtupdaterd is not None:
                    return True

                if self.ciscomvpnbgpmdtupdnhaddrtype is not None:
                    return True

                if self.ciscomvpnbgpmdtupdorigaddrtype is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.mvpn._meta import _CISCO_MVPN_MIB as meta
                return meta._meta_table['CISCOMVPNMIB.CiscoMvpnBgpMdtUpdateTable.CiscoMvpnBgpMdtUpdateEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-MVPN-MIB:CISCO-MVPN-MIB/CISCO-MVPN-MIB:ciscoMvpnBgpMdtUpdateTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ciscomvpnbgpmdtupdateentry is not None:
                for child_ref in self.ciscomvpnbgpmdtupdateentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.mvpn._meta import _CISCO_MVPN_MIB as meta
            return meta._meta_table['CISCOMVPNMIB.CiscoMvpnBgpMdtUpdateTable']['meta_info']


    class CiscoMvpnGenericTable(object):
        """
        This table gives the generic information about the MVRFs 
        present in this device.
        
        .. attribute:: ciscomvpngenericentry
        
        	An entry in this table is created for every MVRF in the  device.  Note that many implementations may have MVRF for global  VRF (VRF0) by default in the device. Also note that existence of the correspoding VRF in  L3VPN\-MPLS\-VPN\-MIB is necessary for a row to exist in this table. Deletion of corresponding VRF in  L3VPN\-MPLS\-VPN\-MIB also results in deletion of a row here.  But deletion of a row ie deletion of a MVRF here does not  result in the deletion of the corresponding VRF in  L3VPN\-MPLS\-VPN\-MIB
        	**type**\: list of :py:class:`CiscoMvpnGenericEntry <ydk.models.mvpn.CISCO_MVPN_MIB.CISCOMVPNMIB.CiscoMvpnGenericTable.CiscoMvpnGenericEntry>`
        
        

        """

        _prefix = 'cisco-mvpn'
        _revision = '2004-02-23'

        def __init__(self):
            self.parent = None
            self.ciscomvpngenericentry = YList()
            self.ciscomvpngenericentry.parent = self
            self.ciscomvpngenericentry.name = 'ciscomvpngenericentry'


        class CiscoMvpnGenericEntry(object):
            """
            An entry in this table is created for every MVRF in the 
            device. 
            Note that many implementations may have MVRF for global 
            VRF (VRF0) by default in the device.
            Also note that existence of the correspoding VRF in 
            L3VPN\-MPLS\-VPN\-MIB is necessary for a row to exist in
            this table. Deletion of corresponding VRF in 
            L3VPN\-MPLS\-VPN\-MIB also results in deletion of a row here. 
            But deletion of a row ie deletion of a MVRF here does not 
            result in the deletion of the corresponding VRF in 
            L3VPN\-MPLS\-VPN\-MIB.
            
            .. attribute:: mplsvpnvrfname
            
            	
            	**type**\: str
            
            	**range:** 0..31
            
            .. attribute:: ciscomvpngenassociatedinterfaces
            
            	Total number of interfaces associated with this MVRF (including the MDT tunnel interface) with ifOperStatus = up(1)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscomvpngenoperchangetime
            
            	The time at which the last operational change for the  MVRF in question took place. The last operational change is specified by ciscoMvpnGenOperStatusChange
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscomvpngenoperstatuschange
            
            	This object describes the last operational change that happened for the given MVRF.   createdMvrf \- indicates that the MVRF was created in the  device.  deletedMvrf \- indicates that the MVRF was deleted from  the device. A row in this table will never have  ciscoMvpnGenOperStatusChange equal to deletedMvrf(2), because in that case the row itself will be deleted  from the table. This value for  ciscoMvpnGenOperStatusChange is defined mainly for use  in ciscoMvpnMvrfChange notification.  modifiedMvrfDefMdtConfig \- indicates that the default MDT  group for the MVRF was configured, deleted or changed.  modifiedMvrfDataMdtConfig \- indicates that the data MDT  group range or a associated variable (like the threshold)  for the MVRF was configured, deleted or changed
            	**type**\: :py:class:`CiscoMvpnGenOperStatusChange_Enum <ydk.models.mvpn.CISCO_MVPN_MIB.CISCOMVPNMIB.CiscoMvpnGenericTable.CiscoMvpnGenericEntry.CiscoMvpnGenOperStatusChange_Enum>`
            
            .. attribute:: ciscomvpngenrowstatus
            
            	This variable is used to create or delete a row in this table
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            

            """

            _prefix = 'cisco-mvpn'
            _revision = '2004-02-23'

            def __init__(self):
                self.parent = None
                self.mplsvpnvrfname = None
                self.ciscomvpngenassociatedinterfaces = None
                self.ciscomvpngenoperchangetime = None
                self.ciscomvpngenoperstatuschange = None
                self.ciscomvpngenrowstatus = None

            class CiscoMvpnGenOperStatusChange_Enum(Enum):
                """
                CiscoMvpnGenOperStatusChange_Enum

                This object describes the last operational change that
                happened for the given MVRF. 
                
                createdMvrf \- indicates that the MVRF was created in the 
                device.
                
                deletedMvrf \- indicates that the MVRF was deleted from 
                the device. A row in this table will never have 
                ciscoMvpnGenOperStatusChange equal to deletedMvrf(2),
                because in that case the row itself will be deleted 
                from the table. This value for 
                ciscoMvpnGenOperStatusChange is defined mainly for use 
                in ciscoMvpnMvrfChange notification.
                
                modifiedMvrfDefMdtConfig \- indicates that the default MDT 
                group for the MVRF was configured, deleted or changed.
                
                modifiedMvrfDataMdtConfig \- indicates that the data MDT 
                group range or a associated variable (like the threshold) 
                for the MVRF was configured, deleted or changed.

                """

                CREATEDMVRF = 1

                DELETEDMVRF = 2

                MODIFIEDMVRFDEFMDTCONFIG = 3

                MODIFIEDMVRFDATAMDTCONFIG = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.mvpn._meta import _CISCO_MVPN_MIB as meta
                    return meta._meta_table['CISCOMVPNMIB.CiscoMvpnGenericTable.CiscoMvpnGenericEntry.CiscoMvpnGenOperStatusChange_Enum']


            @property
            def _common_path(self):
                if self.mplsvpnvrfname is None:
                    raise YPYDataValidationError('Key property mplsvpnvrfname is None')

                return '/CISCO-MVPN-MIB:CISCO-MVPN-MIB/CISCO-MVPN-MIB:ciscoMvpnGenericTable/CISCO-MVPN-MIB:ciscoMvpnGenericEntry[CISCO-MVPN-MIB:mplsVpnVrfName = ' + str(self.mplsvpnvrfname) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.mplsvpnvrfname is not None:
                    return True

                if self.ciscomvpngenassociatedinterfaces is not None:
                    return True

                if self.ciscomvpngenoperchangetime is not None:
                    return True

                if self.ciscomvpngenoperstatuschange is not None:
                    return True

                if self.ciscomvpngenrowstatus is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.mvpn._meta import _CISCO_MVPN_MIB as meta
                return meta._meta_table['CISCOMVPNMIB.CiscoMvpnGenericTable.CiscoMvpnGenericEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-MVPN-MIB:CISCO-MVPN-MIB/CISCO-MVPN-MIB:ciscoMvpnGenericTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ciscomvpngenericentry is not None:
                for child_ref in self.ciscomvpngenericentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.mvpn._meta import _CISCO_MVPN_MIB as meta
            return meta._meta_table['CISCOMVPNMIB.CiscoMvpnGenericTable']['meta_info']


    class CiscoMvpnMdtDataTable(object):
        """
        This table specifies the range of data MDT addresses and 
        associated variables for a MVRF instance.
        
        .. attribute:: ciscomvpnmdtdataentry
        
        	An entry in this table is created for every MVRF for which  a data MDT group range is configured. A MVRF which does not have a data MDT group range configured will not appear in this table.  Creation of a row in this table is the equivalent of  configuring data MDT addresses for the given MVRF. Deletion  of a row in this table is the equivalent of deconfiguring  data MDT address usage in the given MVRF.   Note that ciscoMvpnMdtDefaultEntry for a MVRF should be  present in the device before ciscoMvpnMdtDataEntry for  that MVRF can be created
        	**type**\: list of :py:class:`CiscoMvpnMdtDataEntry <ydk.models.mvpn.CISCO_MVPN_MIB.CISCOMVPNMIB.CiscoMvpnMdtDataTable.CiscoMvpnMdtDataEntry>`
        
        

        """

        _prefix = 'cisco-mvpn'
        _revision = '2004-02-23'

        def __init__(self):
            self.parent = None
            self.ciscomvpnmdtdataentry = YList()
            self.ciscomvpnmdtdataentry.parent = self
            self.ciscomvpnmdtdataentry.name = 'ciscomvpnmdtdataentry'


        class CiscoMvpnMdtDataEntry(object):
            """
            An entry in this table is created for every MVRF for which 
            a data MDT group range is configured. A MVRF which does
            not have a data MDT group range configured will not appear
            in this table. 
            Creation of a row in this table is the equivalent of 
            configuring data MDT addresses for the given MVRF. Deletion 
            of a row in this table is the equivalent of deconfiguring 
            data MDT address usage in the given MVRF. 
            
            Note that ciscoMvpnMdtDefaultEntry for a MVRF should be 
            present in the device before ciscoMvpnMdtDataEntry for 
            that MVRF can be created.
            
            .. attribute:: mplsvpnvrfname
            
            	
            	**type**\: str
            
            	**range:** 0..31
            
            .. attribute:: ciscomvpnmdtdatarangeaddress
            
            	The data MDT group range address for the given MVRF.  This along with ciscoMvpnMdtDataWildcardBits gives the  pool of data MDT addresses that can be used for encapsulation in the MVRF upon data MDT switchover
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: ciscomvpnmdtdatarangeaddrtype
            
            	The Internet address type of ciscoMvpnMdtDataRangeAddress
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: ciscomvpnmdtdatarowstatus
            
            	This variable is used to create, modify or delete a  row in this table
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: ciscomvpnmdtdatathreshold
            
            	The bandwidth threshold value which when exceeded for a  multicast routing entry in the given MVRF, triggers usage  of data MDT address instead of default MDT address for  encapsulation
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscomvpnmdtdatawildcardbits
            
            	Wildcard bits which when used along with data MDT range  address, give a pool of addresses to be used in a MVRF.  For example, if ciscoMvpnMdtDataRangeAddress is 239.1.2.0  and ciscoMvpnMdtDataWildcardBits is 0.0.0.3, the possible  data MDT addresses are 239.1.2.0, 239.1.2.1, 239.1.2.2  and 239.1.2.3.  Note that wild card bits should be right contiguous
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: ciscomvpnmdtdatawildcardtype
            
            	The Internet address type of ciscoMvpnMdtDataWildcardBits
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            

            """

            _prefix = 'cisco-mvpn'
            _revision = '2004-02-23'

            def __init__(self):
                self.parent = None
                self.mplsvpnvrfname = None
                self.ciscomvpnmdtdatarangeaddress = None
                self.ciscomvpnmdtdatarangeaddrtype = None
                self.ciscomvpnmdtdatarowstatus = None
                self.ciscomvpnmdtdatathreshold = None
                self.ciscomvpnmdtdatawildcardbits = None
                self.ciscomvpnmdtdatawildcardtype = None

            @property
            def _common_path(self):
                if self.mplsvpnvrfname is None:
                    raise YPYDataValidationError('Key property mplsvpnvrfname is None')

                return '/CISCO-MVPN-MIB:CISCO-MVPN-MIB/CISCO-MVPN-MIB:ciscoMvpnMdtDataTable/CISCO-MVPN-MIB:ciscoMvpnMdtDataEntry[CISCO-MVPN-MIB:mplsVpnVrfName = ' + str(self.mplsvpnvrfname) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.mplsvpnvrfname is not None:
                    return True

                if self.ciscomvpnmdtdatarangeaddress is not None:
                    return True

                if self.ciscomvpnmdtdatarangeaddrtype is not None:
                    return True

                if self.ciscomvpnmdtdatarowstatus is not None:
                    return True

                if self.ciscomvpnmdtdatathreshold is not None:
                    return True

                if self.ciscomvpnmdtdatawildcardbits is not None:
                    return True

                if self.ciscomvpnmdtdatawildcardtype is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.mvpn._meta import _CISCO_MVPN_MIB as meta
                return meta._meta_table['CISCOMVPNMIB.CiscoMvpnMdtDataTable.CiscoMvpnMdtDataEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-MVPN-MIB:CISCO-MVPN-MIB/CISCO-MVPN-MIB:ciscoMvpnMdtDataTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ciscomvpnmdtdataentry is not None:
                for child_ref in self.ciscomvpnmdtdataentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.mvpn._meta import _CISCO_MVPN_MIB as meta
            return meta._meta_table['CISCOMVPNMIB.CiscoMvpnMdtDataTable']['meta_info']


    class CiscoMvpnMdtDefaultTable(object):
        """
        This table specifies the default MDT address and the 
        encapsulation type used for a MVRF instance.
        
        .. attribute:: ciscomvpnmdtdefaultentry
        
        	An entry in this table is created for every MVRF for which  a default MDT group is configured. A MVRF which does not  have a default MDT group configured will not appear in  this table. Creation of a row in this table is the equivalent of  configuring default MDT address for the given MVRF.  Deletion of a row in this table is the equivalent of  deconfiguring default MDT address for the given MVRF
        	**type**\: list of :py:class:`CiscoMvpnMdtDefaultEntry <ydk.models.mvpn.CISCO_MVPN_MIB.CISCOMVPNMIB.CiscoMvpnMdtDefaultTable.CiscoMvpnMdtDefaultEntry>`
        
        

        """

        _prefix = 'cisco-mvpn'
        _revision = '2004-02-23'

        def __init__(self):
            self.parent = None
            self.ciscomvpnmdtdefaultentry = YList()
            self.ciscomvpnmdtdefaultentry.parent = self
            self.ciscomvpnmdtdefaultentry.name = 'ciscomvpnmdtdefaultentry'


        class CiscoMvpnMdtDefaultEntry(object):
            """
            An entry in this table is created for every MVRF for which 
            a default MDT group is configured. A MVRF which does not 
            have a default MDT group configured will not appear in 
            this table.
            Creation of a row in this table is the equivalent of 
            configuring default MDT address for the given MVRF. 
            Deletion of a row in this table is the equivalent of 
            deconfiguring default MDT address for the given MVRF.
            
            .. attribute:: mplsvpnvrfname
            
            	
            	**type**\: str
            
            	**range:** 0..31
            
            .. attribute:: ciscomvpnmdtdefaultaddress
            
            	The default MDT address to be used for the MVRF in question
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: ciscomvpnmdtdefaultaddrtype
            
            	The Internet address type of ciscoMvpnMdtDefaultAddress
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: ciscomvpnmdtdefaultrowstatus
            
            	This variable is used to create, modify or delete a  row in this table
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: ciscomvpnmdtencapstype
            
            	The encapsulation type to be used in the MVRF in question
            	**type**\: :py:class:`CiscoMvpnMdtEncapsType_Enum <ydk.models.mvpn.CISCO_MVPN_MIB.CISCOMVPNMIB.CiscoMvpnMdtDefaultTable.CiscoMvpnMdtDefaultEntry.CiscoMvpnMdtEncapsType_Enum>`
            
            

            """

            _prefix = 'cisco-mvpn'
            _revision = '2004-02-23'

            def __init__(self):
                self.parent = None
                self.mplsvpnvrfname = None
                self.ciscomvpnmdtdefaultaddress = None
                self.ciscomvpnmdtdefaultaddrtype = None
                self.ciscomvpnmdtdefaultrowstatus = None
                self.ciscomvpnmdtencapstype = None

            class CiscoMvpnMdtEncapsType_Enum(Enum):
                """
                CiscoMvpnMdtEncapsType_Enum

                The encapsulation type to be used in the MVRF in question.

                """

                GREIP = 1

                IPIP = 2

                MPLS = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.mvpn._meta import _CISCO_MVPN_MIB as meta
                    return meta._meta_table['CISCOMVPNMIB.CiscoMvpnMdtDefaultTable.CiscoMvpnMdtDefaultEntry.CiscoMvpnMdtEncapsType_Enum']


            @property
            def _common_path(self):
                if self.mplsvpnvrfname is None:
                    raise YPYDataValidationError('Key property mplsvpnvrfname is None')

                return '/CISCO-MVPN-MIB:CISCO-MVPN-MIB/CISCO-MVPN-MIB:ciscoMvpnMdtDefaultTable/CISCO-MVPN-MIB:ciscoMvpnMdtDefaultEntry[CISCO-MVPN-MIB:mplsVpnVrfName = ' + str(self.mplsvpnvrfname) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.mplsvpnvrfname is not None:
                    return True

                if self.ciscomvpnmdtdefaultaddress is not None:
                    return True

                if self.ciscomvpnmdtdefaultaddrtype is not None:
                    return True

                if self.ciscomvpnmdtdefaultrowstatus is not None:
                    return True

                if self.ciscomvpnmdtencapstype is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.mvpn._meta import _CISCO_MVPN_MIB as meta
                return meta._meta_table['CISCOMVPNMIB.CiscoMvpnMdtDefaultTable.CiscoMvpnMdtDefaultEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-MVPN-MIB:CISCO-MVPN-MIB/CISCO-MVPN-MIB:ciscoMvpnMdtDefaultTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ciscomvpnmdtdefaultentry is not None:
                for child_ref in self.ciscomvpnmdtdefaultentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.mvpn._meta import _CISCO_MVPN_MIB as meta
            return meta._meta_table['CISCOMVPNMIB.CiscoMvpnMdtDefaultTable']['meta_info']


    class CiscoMvpnMdtJnRcvTable(object):
        """
        This table has information about the data MDT join TLVs 
        received by a device.
        
        .. attribute:: ciscomvpnmdtjnrcventry
        
        	An entry in this table is created or updated for every MDT  data join TLV received and cached in the device. The value of  mplsVpnVrfName in such an entry specifies the name of the  MVRF for which the data MDT groups from the TLVs are used
        	**type**\: list of :py:class:`CiscoMvpnMdtJnRcvEntry <ydk.models.mvpn.CISCO_MVPN_MIB.CISCOMVPNMIB.CiscoMvpnMdtJnRcvTable.CiscoMvpnMdtJnRcvEntry>`
        
        

        """

        _prefix = 'cisco-mvpn'
        _revision = '2004-02-23'

        def __init__(self):
            self.parent = None
            self.ciscomvpnmdtjnrcventry = YList()
            self.ciscomvpnmdtjnrcventry.parent = self
            self.ciscomvpnmdtjnrcventry.name = 'ciscomvpnmdtjnrcventry'


        class CiscoMvpnMdtJnRcvEntry(object):
            """
            An entry in this table is created or updated for every MDT 
            data join TLV received and cached in the device. The value of 
            mplsVpnVrfName in such an entry specifies the name of the 
            MVRF for which the data MDT groups from the TLVs are used.
            
            .. attribute:: ciscomvpnmdtjnrcvgroup
            
            	Data MDT group address in the MDT join TLV
            	**type**\: str
            
            	**range:** 4 \| 16 \| 20
            
            .. attribute:: ciscomvpnmdtjnrcvgrpaddrtype
            
            	The Internet address type of ciscoMvpnMdtJnRcvGroup
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: ciscomvpnmdtjnrcvsource
            
            	Source address for the MDT multicast routing entry created  following the receipt of MDT join TLV
            	**type**\: str
            
            	**range:** 4 \| 16 \| 20
            
            .. attribute:: ciscomvpnmdtjnrcvsrcaddrtype
            
            	The Internet address type of ciscoMvpnMdtJnRcvSource
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: mplsvpnvrfname
            
            	
            	**type**\: str
            
            	**range:** 0..31
            
            .. attribute:: ciscomvpnmdtjnrcvexptime
            
            	The amount of time remaining before the cache corresponding  to this MDT join TLV is deleted from the device and the  corresponding  MDT multicast routing entry is marked as a  non\-MDT entry. Note that multiple TLVs for a data MDT group may be received  by a device. Upon receipt, the expiry timer of an already  existing entry is restarted and so ciscoMvpnMdtJnRcvExpTime  is updated
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: ciscomvpnmdtjnrcvuptime
            
            	The time since this MDT join TLV was first received by the  device
            	**type**\: int
            
            	**range:** 0..2147483647
            
            

            """

            _prefix = 'cisco-mvpn'
            _revision = '2004-02-23'

            def __init__(self):
                self.parent = None
                self.ciscomvpnmdtjnrcvgroup = None
                self.ciscomvpnmdtjnrcvgrpaddrtype = None
                self.ciscomvpnmdtjnrcvsource = None
                self.ciscomvpnmdtjnrcvsrcaddrtype = None
                self.mplsvpnvrfname = None
                self.ciscomvpnmdtjnrcvexptime = None
                self.ciscomvpnmdtjnrcvuptime = None

            @property
            def _common_path(self):
                if self.ciscomvpnmdtjnrcvgroup is None:
                    raise YPYDataValidationError('Key property ciscomvpnmdtjnrcvgroup is None')
                if self.ciscomvpnmdtjnrcvgrpaddrtype is None:
                    raise YPYDataValidationError('Key property ciscomvpnmdtjnrcvgrpaddrtype is None')
                if self.ciscomvpnmdtjnrcvsource is None:
                    raise YPYDataValidationError('Key property ciscomvpnmdtjnrcvsource is None')
                if self.ciscomvpnmdtjnrcvsrcaddrtype is None:
                    raise YPYDataValidationError('Key property ciscomvpnmdtjnrcvsrcaddrtype is None')
                if self.mplsvpnvrfname is None:
                    raise YPYDataValidationError('Key property mplsvpnvrfname is None')

                return '/CISCO-MVPN-MIB:CISCO-MVPN-MIB/CISCO-MVPN-MIB:ciscoMvpnMdtJnRcvTable/CISCO-MVPN-MIB:ciscoMvpnMdtJnRcvEntry[CISCO-MVPN-MIB:ciscoMvpnMdtJnRcvGroup = ' + str(self.ciscomvpnmdtjnrcvgroup) + '][CISCO-MVPN-MIB:ciscoMvpnMdtJnRcvGrpAddrType = ' + str(self.ciscomvpnmdtjnrcvgrpaddrtype) + '][CISCO-MVPN-MIB:ciscoMvpnMdtJnRcvSource = ' + str(self.ciscomvpnmdtjnrcvsource) + '][CISCO-MVPN-MIB:ciscoMvpnMdtJnRcvSrcAddrType = ' + str(self.ciscomvpnmdtjnrcvsrcaddrtype) + '][CISCO-MVPN-MIB:mplsVpnVrfName = ' + str(self.mplsvpnvrfname) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ciscomvpnmdtjnrcvgroup is not None:
                    return True

                if self.ciscomvpnmdtjnrcvgrpaddrtype is not None:
                    return True

                if self.ciscomvpnmdtjnrcvsource is not None:
                    return True

                if self.ciscomvpnmdtjnrcvsrcaddrtype is not None:
                    return True

                if self.mplsvpnvrfname is not None:
                    return True

                if self.ciscomvpnmdtjnrcvexptime is not None:
                    return True

                if self.ciscomvpnmdtjnrcvuptime is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.mvpn._meta import _CISCO_MVPN_MIB as meta
                return meta._meta_table['CISCOMVPNMIB.CiscoMvpnMdtJnRcvTable.CiscoMvpnMdtJnRcvEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-MVPN-MIB:CISCO-MVPN-MIB/CISCO-MVPN-MIB:ciscoMvpnMdtJnRcvTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ciscomvpnmdtjnrcventry is not None:
                for child_ref in self.ciscomvpnmdtjnrcventry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.mvpn._meta import _CISCO_MVPN_MIB as meta
            return meta._meta_table['CISCOMVPNMIB.CiscoMvpnMdtJnRcvTable']['meta_info']


    class CiscoMvpnMdtJnSendTable(object):
        """
        This table specifies the data MDT Join TLVs sent by a 
        device.
        
        .. attribute:: ciscomvpnmdtjnsendentry
        
        	Entries in this table exist for data MDT Join TLVs that are  being sent by this device to other PEs
        	**type**\: list of :py:class:`CiscoMvpnMdtJnSendEntry <ydk.models.mvpn.CISCO_MVPN_MIB.CISCOMVPNMIB.CiscoMvpnMdtJnSendTable.CiscoMvpnMdtJnSendEntry>`
        
        

        """

        _prefix = 'cisco-mvpn'
        _revision = '2004-02-23'

        def __init__(self):
            self.parent = None
            self.ciscomvpnmdtjnsendentry = YList()
            self.ciscomvpnmdtjnsendentry.parent = self
            self.ciscomvpnmdtjnsendentry.name = 'ciscomvpnmdtjnsendentry'


        class CiscoMvpnMdtJnSendEntry(object):
            """
            Entries in this table exist for data MDT Join TLVs that are 
            being sent by this device to other PEs.
            
            .. attribute:: ciscomvpnmdtjnsendgroup
            
            	This indicates the address of a multicast group in the  MVRF specified by the column mplsVpnVrfName. This along  with ciscoMvpnMdtJnSendSource identifies the multicast  routing entry for which the MDT join TLV is sent
            	**type**\: str
            
            	**range:** 4 \| 16 \| 20
            
            .. attribute:: ciscomvpnmdtjnsendgrpaddrtype
            
            	The Internet address type of ciscoMvpnMdtJnSendGroup
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: ciscomvpnmdtjnsendsource
            
            	This indicates the address of a source in the MVRF  specified by the column mplsVpnVrfName. This, along with  ciscoMvpnMdtJnSendGroup identifies the multicast routing entry for which the MDT join TLV is sent
            	**type**\: str
            
            	**range:** 4 \| 16 \| 20
            
            .. attribute:: ciscomvpnmdtjnsendsrcaddrtype
            
            	The Internet address type of ciscoMvpnMdtJnSendSource
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: mplsvpnvrfname
            
            	
            	**type**\: str
            
            	**range:** 0..31
            
            .. attribute:: ciscomvpnmdtjnsendmdtgroup
            
            	The data MDT group in the MDT Join TLV sent
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: ciscomvpnmdtjnsendmdtgrpaddrtype
            
            	The Internet address type of ciscoMvpnMdtJnSendMdtGroup
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: ciscomvpnmdtjnsendmdtrefct
            
            	Indicates how many multicast routing entries in the MVRF  specified by the column mplsVpnVrfName are using  ciscoMvpnMdtJnSendMdtGroup for encapsulation
            	**type**\: int
            
            	**range:** 0..65535
            
            

            """

            _prefix = 'cisco-mvpn'
            _revision = '2004-02-23'

            def __init__(self):
                self.parent = None
                self.ciscomvpnmdtjnsendgroup = None
                self.ciscomvpnmdtjnsendgrpaddrtype = None
                self.ciscomvpnmdtjnsendsource = None
                self.ciscomvpnmdtjnsendsrcaddrtype = None
                self.mplsvpnvrfname = None
                self.ciscomvpnmdtjnsendmdtgroup = None
                self.ciscomvpnmdtjnsendmdtgrpaddrtype = None
                self.ciscomvpnmdtjnsendmdtrefct = None

            @property
            def _common_path(self):
                if self.ciscomvpnmdtjnsendgroup is None:
                    raise YPYDataValidationError('Key property ciscomvpnmdtjnsendgroup is None')
                if self.ciscomvpnmdtjnsendgrpaddrtype is None:
                    raise YPYDataValidationError('Key property ciscomvpnmdtjnsendgrpaddrtype is None')
                if self.ciscomvpnmdtjnsendsource is None:
                    raise YPYDataValidationError('Key property ciscomvpnmdtjnsendsource is None')
                if self.ciscomvpnmdtjnsendsrcaddrtype is None:
                    raise YPYDataValidationError('Key property ciscomvpnmdtjnsendsrcaddrtype is None')
                if self.mplsvpnvrfname is None:
                    raise YPYDataValidationError('Key property mplsvpnvrfname is None')

                return '/CISCO-MVPN-MIB:CISCO-MVPN-MIB/CISCO-MVPN-MIB:ciscoMvpnMdtJnSendTable/CISCO-MVPN-MIB:ciscoMvpnMdtJnSendEntry[CISCO-MVPN-MIB:ciscoMvpnMdtJnSendGroup = ' + str(self.ciscomvpnmdtjnsendgroup) + '][CISCO-MVPN-MIB:ciscoMvpnMdtJnSendGrpAddrType = ' + str(self.ciscomvpnmdtjnsendgrpaddrtype) + '][CISCO-MVPN-MIB:ciscoMvpnMdtJnSendSource = ' + str(self.ciscomvpnmdtjnsendsource) + '][CISCO-MVPN-MIB:ciscoMvpnMdtJnSendSrcAddrType = ' + str(self.ciscomvpnmdtjnsendsrcaddrtype) + '][CISCO-MVPN-MIB:mplsVpnVrfName = ' + str(self.mplsvpnvrfname) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ciscomvpnmdtjnsendgroup is not None:
                    return True

                if self.ciscomvpnmdtjnsendgrpaddrtype is not None:
                    return True

                if self.ciscomvpnmdtjnsendsource is not None:
                    return True

                if self.ciscomvpnmdtjnsendsrcaddrtype is not None:
                    return True

                if self.mplsvpnvrfname is not None:
                    return True

                if self.ciscomvpnmdtjnsendmdtgroup is not None:
                    return True

                if self.ciscomvpnmdtjnsendmdtgrpaddrtype is not None:
                    return True

                if self.ciscomvpnmdtjnsendmdtrefct is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.mvpn._meta import _CISCO_MVPN_MIB as meta
                return meta._meta_table['CISCOMVPNMIB.CiscoMvpnMdtJnSendTable.CiscoMvpnMdtJnSendEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-MVPN-MIB:CISCO-MVPN-MIB/CISCO-MVPN-MIB:ciscoMvpnMdtJnSendTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ciscomvpnmdtjnsendentry is not None:
                for child_ref in self.ciscomvpnmdtjnsendentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.mvpn._meta import _CISCO_MVPN_MIB as meta
            return meta._meta_table['CISCOMVPNMIB.CiscoMvpnMdtJnSendTable']['meta_info']


    class CiscoMvpnMrouteMdtTable(object):
        """
        Given a multicast routing entry and the context MVRF, this 
        table provides information about the MDT group being used for 
        encapsulating the traffic for the multicast routing entry in 
        the provider network at the instance of querying. Note that
        this table is a read\-only table and is the result of the 
        default MDT and data MDT configurations and the operational 
        conditions like the traffic rate and sometimes, the 
        implementation choices.
        
        .. attribute:: ciscomvpnmroutemdtentry
        
        	An entry in this table exists for a multicast routing entry  the traffic for which is being encapsulated in a context  MVRF
        	**type**\: list of :py:class:`CiscoMvpnMrouteMdtEntry <ydk.models.mvpn.CISCO_MVPN_MIB.CISCOMVPNMIB.CiscoMvpnMrouteMdtTable.CiscoMvpnMrouteMdtEntry>`
        
        

        """

        _prefix = 'cisco-mvpn'
        _revision = '2004-02-23'

        def __init__(self):
            self.parent = None
            self.ciscomvpnmroutemdtentry = YList()
            self.ciscomvpnmroutemdtentry.parent = self
            self.ciscomvpnmroutemdtentry.name = 'ciscomvpnmroutemdtentry'


        class CiscoMvpnMrouteMdtEntry(object):
            """
            An entry in this table exists for a multicast routing entry 
            the traffic for which is being encapsulated in a context 
            MVRF.
            
            .. attribute:: ciscomvpnmroutemvrfgroup
            
            	Group adddress of multicast routing entry in question
            	**type**\: str
            
            	**range:** 4 \| 16 \| 20
            
            .. attribute:: ciscomvpnmroutemvrfgrpaddrtype
            
            	The Internet address type of ciscoMvpnMrouteMvrfGroup
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: ciscomvpnmroutemvrfsource
            
            	Source adddress of the multicast routing entry in question
            	**type**\: str
            
            	**range:** 4 \| 16 \| 20
            
            .. attribute:: ciscomvpnmroutemvrfsrcaddrtype
            
            	The Internet address type of ciscoMvpnMrouteMvrfSource
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: ciscomvpnmrouteupdownstreaminfo
            
            	Indicates if this PE is the upstream (sending) or the  downstream (receiving) router for the multicast routing entry  specified by ciscoMvpnMrouteMvrfSource and  ciscoMvpnMrouteMvrfGroup in the context MVRF specified by  mplsVpnVrfName. Note that there may be two rows for the same multicast  routing entry if the traffic is bi\-directional, one row  for PE as an upstream router the other for PE as the  downstream router
            	**type**\: :py:class:`CiscoMvpnMrouteUpDownStreamInfo_Enum <ydk.models.mvpn.CISCO_MVPN_MIB.CISCOMVPNMIB.CiscoMvpnMrouteMdtTable.CiscoMvpnMrouteMdtEntry.CiscoMvpnMrouteUpDownStreamInfo_Enum>`
            
            .. attribute:: mplsvpnvrfname
            
            	
            	**type**\: str
            
            	**range:** 0..31
            
            .. attribute:: ciscomvpnmroutemdtgroup
            
            	MDT group address used to encapsulate the multicast routing  entry specified by ciscoMvpnMrouteMvrfSource and  ciscoMvpnMrouteMvrfGroup in the context MVRF specified by  mplsVpnVrfName
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: ciscomvpnmroutemdtgrpaddrtype
            
            	The Internet address type of ciscoMvpnMrouteMdtGroup
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: ciscomvpnmroutemdttype
            
            	Indicates the type of MDT group used for encapsulation
            	**type**\: :py:class:`CiscoMvpnMrouteMdtType_Enum <ydk.models.mvpn.CISCO_MVPN_MIB.CISCOMVPNMIB.CiscoMvpnMrouteMdtTable.CiscoMvpnMrouteMdtEntry.CiscoMvpnMrouteMdtType_Enum>`
            
            

            """

            _prefix = 'cisco-mvpn'
            _revision = '2004-02-23'

            def __init__(self):
                self.parent = None
                self.ciscomvpnmroutemvrfgroup = None
                self.ciscomvpnmroutemvrfgrpaddrtype = None
                self.ciscomvpnmroutemvrfsource = None
                self.ciscomvpnmroutemvrfsrcaddrtype = None
                self.ciscomvpnmrouteupdownstreaminfo = None
                self.mplsvpnvrfname = None
                self.ciscomvpnmroutemdtgroup = None
                self.ciscomvpnmroutemdtgrpaddrtype = None
                self.ciscomvpnmroutemdttype = None

            class CiscoMvpnMrouteMdtType_Enum(Enum):
                """
                CiscoMvpnMrouteMdtType_Enum

                Indicates the type of MDT group used for encapsulation.

                """

                MDTDEFAULT = 1

                MDTDATA = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.mvpn._meta import _CISCO_MVPN_MIB as meta
                    return meta._meta_table['CISCOMVPNMIB.CiscoMvpnMrouteMdtTable.CiscoMvpnMrouteMdtEntry.CiscoMvpnMrouteMdtType_Enum']


            class CiscoMvpnMrouteUpDownStreamInfo_Enum(Enum):
                """
                CiscoMvpnMrouteUpDownStreamInfo_Enum

                Indicates if this PE is the upstream (sending) or the 
                downstream (receiving) router for the multicast routing entry 
                specified by ciscoMvpnMrouteMvrfSource and 
                ciscoMvpnMrouteMvrfGroup in the context MVRF specified by 
                mplsVpnVrfName.
                Note that there may be two rows for the same multicast 
                routing entry if the traffic is bi\-directional, one row 
                for PE as an upstream router the other for PE as the 
                downstream router.

                """

                UPSTREAM = 1

                DOWNSTREAM = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.mvpn._meta import _CISCO_MVPN_MIB as meta
                    return meta._meta_table['CISCOMVPNMIB.CiscoMvpnMrouteMdtTable.CiscoMvpnMrouteMdtEntry.CiscoMvpnMrouteUpDownStreamInfo_Enum']


            @property
            def _common_path(self):
                if self.ciscomvpnmroutemvrfgroup is None:
                    raise YPYDataValidationError('Key property ciscomvpnmroutemvrfgroup is None')
                if self.ciscomvpnmroutemvrfgrpaddrtype is None:
                    raise YPYDataValidationError('Key property ciscomvpnmroutemvrfgrpaddrtype is None')
                if self.ciscomvpnmroutemvrfsource is None:
                    raise YPYDataValidationError('Key property ciscomvpnmroutemvrfsource is None')
                if self.ciscomvpnmroutemvrfsrcaddrtype is None:
                    raise YPYDataValidationError('Key property ciscomvpnmroutemvrfsrcaddrtype is None')
                if self.ciscomvpnmrouteupdownstreaminfo is None:
                    raise YPYDataValidationError('Key property ciscomvpnmrouteupdownstreaminfo is None')
                if self.mplsvpnvrfname is None:
                    raise YPYDataValidationError('Key property mplsvpnvrfname is None')

                return '/CISCO-MVPN-MIB:CISCO-MVPN-MIB/CISCO-MVPN-MIB:ciscoMvpnMrouteMdtTable/CISCO-MVPN-MIB:ciscoMvpnMrouteMdtEntry[CISCO-MVPN-MIB:ciscoMvpnMrouteMvrfGroup = ' + str(self.ciscomvpnmroutemvrfgroup) + '][CISCO-MVPN-MIB:ciscoMvpnMrouteMvrfGrpAddrType = ' + str(self.ciscomvpnmroutemvrfgrpaddrtype) + '][CISCO-MVPN-MIB:ciscoMvpnMrouteMvrfSource = ' + str(self.ciscomvpnmroutemvrfsource) + '][CISCO-MVPN-MIB:ciscoMvpnMrouteMvrfSrcAddrType = ' + str(self.ciscomvpnmroutemvrfsrcaddrtype) + '][CISCO-MVPN-MIB:ciscoMvpnMrouteUpDownStreamInfo = ' + str(self.ciscomvpnmrouteupdownstreaminfo) + '][CISCO-MVPN-MIB:mplsVpnVrfName = ' + str(self.mplsvpnvrfname) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ciscomvpnmroutemvrfgroup is not None:
                    return True

                if self.ciscomvpnmroutemvrfgrpaddrtype is not None:
                    return True

                if self.ciscomvpnmroutemvrfsource is not None:
                    return True

                if self.ciscomvpnmroutemvrfsrcaddrtype is not None:
                    return True

                if self.ciscomvpnmrouteupdownstreaminfo is not None:
                    return True

                if self.mplsvpnvrfname is not None:
                    return True

                if self.ciscomvpnmroutemdtgroup is not None:
                    return True

                if self.ciscomvpnmroutemdtgrpaddrtype is not None:
                    return True

                if self.ciscomvpnmroutemdttype is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.mvpn._meta import _CISCO_MVPN_MIB as meta
                return meta._meta_table['CISCOMVPNMIB.CiscoMvpnMrouteMdtTable.CiscoMvpnMrouteMdtEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-MVPN-MIB:CISCO-MVPN-MIB/CISCO-MVPN-MIB:ciscoMvpnMrouteMdtTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ciscomvpnmroutemdtentry is not None:
                for child_ref in self.ciscomvpnmroutemdtentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.mvpn._meta import _CISCO_MVPN_MIB as meta
            return meta._meta_table['CISCOMVPNMIB.CiscoMvpnMrouteMdtTable']['meta_info']


    class CiscoMvpnScalars(object):
        """
        
        
        .. attribute:: ciscomvpnmvrfnumber
        
        	The number of MVRFs that are present in this device
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ciscomvpnnotificationenable
        
        	If this object is TRUE, then the generation of  all notifications defined in this MIB is enabled
        	**type**\: bool
        
        

        """

        _prefix = 'cisco-mvpn'
        _revision = '2004-02-23'

        def __init__(self):
            self.parent = None
            self.ciscomvpnmvrfnumber = None
            self.ciscomvpnnotificationenable = None

        @property
        def _common_path(self):

            return '/CISCO-MVPN-MIB:CISCO-MVPN-MIB/CISCO-MVPN-MIB:ciscoMvpnScalars'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ciscomvpnmvrfnumber is not None:
                return True

            if self.ciscomvpnnotificationenable is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.mvpn._meta import _CISCO_MVPN_MIB as meta
            return meta._meta_table['CISCOMVPNMIB.CiscoMvpnScalars']['meta_info']


    class CiscoMvpnTunnelTable(object):
        """
        This table gives information about the MVPN/MDT tunnels 
        present in the device.
        
        .. attribute:: ciscomvpntunnelentry
        
        	An entry in this table is created for every MVPN tunnel  interface present in the device. The ifType for a MVPN tunnel is 'tunnel' (131).  (A MVPN tunnel interface should have relevant generic  support in the IF\-MIB and in the internet draft, draft\-thaler\-inet\-tunnel\-mib. Only MVPN specific aspects of such a tunnel interface are to be specified in this table.)
        	**type**\: list of :py:class:`CiscoMvpnTunnelEntry <ydk.models.mvpn.CISCO_MVPN_MIB.CISCOMVPNMIB.CiscoMvpnTunnelTable.CiscoMvpnTunnelEntry>`
        
        

        """

        _prefix = 'cisco-mvpn'
        _revision = '2004-02-23'

        def __init__(self):
            self.parent = None
            self.ciscomvpntunnelentry = YList()
            self.ciscomvpntunnelentry.parent = self
            self.ciscomvpntunnelentry.name = 'ciscomvpntunnelentry'


        class CiscoMvpnTunnelEntry(object):
            """
            An entry in this table is created for every MVPN tunnel 
            interface present in the device. The ifType for a MVPN
            tunnel is 'tunnel' (131). 
            (A MVPN tunnel interface should have relevant generic 
            support in the IF\-MIB and in the internet draft,
            draft\-thaler\-inet\-tunnel\-mib. Only MVPN specific aspects
            of such a tunnel interface are to be specified in this
            table.)
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: ciscomvpntunnelmvrf
            
            	Name of the MVRF that this tunnel is associated with. This object has the same value as mplsVpnVrfName for the MVRF
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: ciscomvpntunnelname
            
            	The canonical name assigned to the tunnel. The ifName of  this tunnel interface should have a value equal to  ciscoMvpnTunnelName
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            

            """

            _prefix = 'cisco-mvpn'
            _revision = '2004-02-23'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.ciscomvpntunnelmvrf = None
                self.ciscomvpntunnelname = None

            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/CISCO-MVPN-MIB:CISCO-MVPN-MIB/CISCO-MVPN-MIB:ciscoMvpnTunnelTable/CISCO-MVPN-MIB:ciscoMvpnTunnelEntry[CISCO-MVPN-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ifindex is not None:
                    return True

                if self.ciscomvpntunnelmvrf is not None:
                    return True

                if self.ciscomvpntunnelname is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.mvpn._meta import _CISCO_MVPN_MIB as meta
                return meta._meta_table['CISCOMVPNMIB.CiscoMvpnTunnelTable.CiscoMvpnTunnelEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-MVPN-MIB:CISCO-MVPN-MIB/CISCO-MVPN-MIB:ciscoMvpnTunnelTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ciscomvpntunnelentry is not None:
                for child_ref in self.ciscomvpntunnelentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.mvpn._meta import _CISCO_MVPN_MIB as meta
            return meta._meta_table['CISCOMVPNMIB.CiscoMvpnTunnelTable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-MVPN-MIB:CISCO-MVPN-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.ciscomvpnbgpmdtupdatetable is not None and self.ciscomvpnbgpmdtupdatetable._has_data():
            return True

        if self.ciscomvpnbgpmdtupdatetable is not None and self.ciscomvpnbgpmdtupdatetable.is_presence():
            return True

        if self.ciscomvpngenerictable is not None and self.ciscomvpngenerictable._has_data():
            return True

        if self.ciscomvpngenerictable is not None and self.ciscomvpngenerictable.is_presence():
            return True

        if self.ciscomvpnmdtdatatable is not None and self.ciscomvpnmdtdatatable._has_data():
            return True

        if self.ciscomvpnmdtdatatable is not None and self.ciscomvpnmdtdatatable.is_presence():
            return True

        if self.ciscomvpnmdtdefaulttable is not None and self.ciscomvpnmdtdefaulttable._has_data():
            return True

        if self.ciscomvpnmdtdefaulttable is not None and self.ciscomvpnmdtdefaulttable.is_presence():
            return True

        if self.ciscomvpnmdtjnrcvtable is not None and self.ciscomvpnmdtjnrcvtable._has_data():
            return True

        if self.ciscomvpnmdtjnrcvtable is not None and self.ciscomvpnmdtjnrcvtable.is_presence():
            return True

        if self.ciscomvpnmdtjnsendtable is not None and self.ciscomvpnmdtjnsendtable._has_data():
            return True

        if self.ciscomvpnmdtjnsendtable is not None and self.ciscomvpnmdtjnsendtable.is_presence():
            return True

        if self.ciscomvpnmroutemdttable is not None and self.ciscomvpnmroutemdttable._has_data():
            return True

        if self.ciscomvpnmroutemdttable is not None and self.ciscomvpnmroutemdttable.is_presence():
            return True

        if self.ciscomvpnscalars is not None and self.ciscomvpnscalars._has_data():
            return True

        if self.ciscomvpnscalars is not None and self.ciscomvpnscalars.is_presence():
            return True

        if self.ciscomvpntunneltable is not None and self.ciscomvpntunneltable._has_data():
            return True

        if self.ciscomvpntunneltable is not None and self.ciscomvpntunneltable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.mvpn._meta import _CISCO_MVPN_MIB as meta
        return meta._meta_table['CISCOMVPNMIB']['meta_info']


