""" CISCO_DYNAMIC_TEMPLATE_MIB 

This MIB defines objects that describe dynamic templates.  A
dynamic template is a set of configuration attributes that a
system can dynamically apply to a target.

The target of a dynamic template is the entity configured by the
system using the configuration attributes contained by a 
template. At the time of this writing, an interface represents
the only valid target of a dynamic template.  However, the
architecture does not prevent other target types, and hence, the
MIB definition generalizes the notion of a target to allow for
this.

Generally, the system does not directly apply the attributes
contained by a dynamic template to an associated
target.  The system might generate a derived configuration from
the set of dynamic templates associated with the target.  A
derived configuration represents the union of the configuration
attributes contained by each associated dynamic template.  In
the case of a conflict (i.e., more than one dynamic template
specifies the same configuration attribute), the system accepts
the configuration attribute from the dynamic template with the
highest precedence.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.dynamic.CISCO_DYNAMIC_TEMPLATE_TC_MIB import DynamicTemplateTargetType_Enum
from ydk.models.dynamic.CISCO_DYNAMIC_TEMPLATE_TC_MIB import DynamicTemplateType_Enum
from ydk.models.ip.CISCO_IP_URPF_MIB import UnicastRpfOptions_Bits
from ydk.models.ip.CISCO_IP_URPF_MIB import UnicastRpfType_Enum
from ydk.models.snmpv2.SNMPv2_TC import RowStatus_Enum
from ydk.models.snmpv2.SNMPv2_TC import StorageType_Enum


class CISCODYNAMICTEMPLATEMIB(object):
    """
    
    
    .. attribute:: cdtethernettemplatetable
    
    	This table contains attributes relating to dynamic interfaces initiated on Ethernet virtual interfaces (e.g., EoMPLS) or automatically created VLANs.  This table has a sparse\-dependent relationship on the cdtTemplateTable, containing a row for each dynamic template having a cdtTemplateType of one of the following values\:      'derived'     'ethernet'
    	**type**\: :py:class:`CdtEthernetTemplateTable <ydk.models.dynamic.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtEthernetTemplateTable>`
    
    .. attribute:: cdtiftemplatetable
    
    	This table contains attributes relating to interface configuration.  This table has a sparse\-dependent relationship on the cdtTemplateTable, containing a row for each dynamic template having a cdtTemplateType of one of the following values\:      'derived'     'ppp'     'ethernet'     'ipSubscriber'
    	**type**\: :py:class:`CdtIfTemplateTable <ydk.models.dynamic.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtIfTemplateTable>`
    
    .. attribute:: cdtppppeeripaddrpooltable
    
    	This table contains a prioritized list of named pools for each PPP template.  A list corresponding to a PPP template specifies the pools the system searches in an attempt to assign an IP address to the peer of a target PPP connection. The system searches the pools in the order of their priority.  This table has an expansion dependent relationship on the cdtPppTemplateTable, containing zero or more rows for each PPP template
    	**type**\: :py:class:`CdtPppPeerIpAddrPoolTable <ydk.models.dynamic.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtPppPeerIpAddrPoolTable>`
    
    .. attribute:: cdtppptemplatetable
    
    	This table contains attributes relating to PPP connection configuration.  This table has a sparse\-dependent relationship on the cdtTemplateTable, containing a row for each dynamic template having a cdtTemplateType of one of the following values\:      'derived'     'ppp'
    	**type**\: :py:class:`CdtPppTemplateTable <ydk.models.dynamic.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtPppTemplateTable>`
    
    .. attribute:: cdtsrvtemplatetable
    
    	This table contains attributes relating to a service.  This table has a sparse\-dependent relationship on the cdtTemplateTable, containing a row for each dynamic template having a cdtTemplateType of one of the following values\:      'derived'     'service'
    	**type**\: :py:class:`CdtSrvTemplateTable <ydk.models.dynamic.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtSrvTemplateTable>`
    
    .. attribute:: cdttemplateassociationtable
    
    	This table contains a list of templates associated with each target.  This table has an expansion dependent relationship on the cdtTemplateTargetTable, containing zero or more rows for each target
    	**type**\: :py:class:`CdtTemplateAssociationTable <ydk.models.dynamic.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtTemplateAssociationTable>`
    
    .. attribute:: cdttemplatecommontable
    
    	This table contains attributes relating to all dynamic templates.  Observe that the type of dynamic templates containing these attributes may change with the addition of new dynamic template types.  This table has a sparse\-dependent relationship on the cdtTemplateTable, containing a row for each dynamic template having a cdtTemplateType of one of the following values\:      'derived'     'ppp'     'ethernet'     'ipSubscriber'     'service'
    	**type**\: :py:class:`CdtTemplateCommonTable <ydk.models.dynamic.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtTemplateCommonTable>`
    
    .. attribute:: cdttemplatetable
    
    	This table lists the dynamic templates maintained by the system, including those that have been locally\-configured on the system and those pushed to the system by external policy servers
    	**type**\: :py:class:`CdtTemplateTable <ydk.models.dynamic.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtTemplateTable>`
    
    .. attribute:: cdttemplatetargettable
    
    	This table contains a list of targets associated with one or more dynamic templates
    	**type**\: :py:class:`CdtTemplateTargetTable <ydk.models.dynamic.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtTemplateTargetTable>`
    
    .. attribute:: cdttemplateusagetable
    
    	This table contains a list of targets using each dynamic template.  This table has an expansion dependent relationship on the cdtTemplateTable, containing zero or more rows for each dynamic template
    	**type**\: :py:class:`CdtTemplateUsageTable <ydk.models.dynamic.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtTemplateUsageTable>`
    
    

    """

    _prefix = 'cisco-dynamic-template'
    _revision = '2007-09-06'

    def __init__(self):
        self.cdtethernettemplatetable = CISCODYNAMICTEMPLATEMIB.CdtEthernetTemplateTable()
        self.cdtethernettemplatetable.parent = self
        self.cdtiftemplatetable = CISCODYNAMICTEMPLATEMIB.CdtIfTemplateTable()
        self.cdtiftemplatetable.parent = self
        self.cdtppppeeripaddrpooltable = CISCODYNAMICTEMPLATEMIB.CdtPppPeerIpAddrPoolTable()
        self.cdtppppeeripaddrpooltable.parent = self
        self.cdtppptemplatetable = CISCODYNAMICTEMPLATEMIB.CdtPppTemplateTable()
        self.cdtppptemplatetable.parent = self
        self.cdtsrvtemplatetable = CISCODYNAMICTEMPLATEMIB.CdtSrvTemplateTable()
        self.cdtsrvtemplatetable.parent = self
        self.cdttemplateassociationtable = CISCODYNAMICTEMPLATEMIB.CdtTemplateAssociationTable()
        self.cdttemplateassociationtable.parent = self
        self.cdttemplatecommontable = CISCODYNAMICTEMPLATEMIB.CdtTemplateCommonTable()
        self.cdttemplatecommontable.parent = self
        self.cdttemplatetable = CISCODYNAMICTEMPLATEMIB.CdtTemplateTable()
        self.cdttemplatetable.parent = self
        self.cdttemplatetargettable = CISCODYNAMICTEMPLATEMIB.CdtTemplateTargetTable()
        self.cdttemplatetargettable.parent = self
        self.cdttemplateusagetable = CISCODYNAMICTEMPLATEMIB.CdtTemplateUsageTable()
        self.cdttemplateusagetable.parent = self


    class CdtEthernetTemplateTable(object):
        """
        This table contains attributes relating to dynamic interfaces
        initiated on Ethernet virtual interfaces (e.g., EoMPLS) or
        automatically created VLANs.
        
        This table has a sparse\-dependent relationship on the
        cdtTemplateTable, containing a row for each dynamic template
        having a cdtTemplateType of one of the following values\:
        
            'derived'
            'ethernet'
        
        .. attribute:: cdtethernettemplateentry
        
        	An entry containing attributes relating to dynamic interfaces initiated on Ethernet virtual interfaces (e.g., EoMPLS) or automatically created VLANs.  The system automatically creates an entry when the system or the EMS/NMS creates a row in the cdtTemplateTable with a cdtTemplateType of one of the following values\:      'derived'     'ethernet'  Likewise, the system automatically destroys an entry when the system or the EMS/NMS destroys the corresponding row in the cdtTemplateTable
        	**type**\: list of :py:class:`CdtEthernetTemplateEntry <ydk.models.dynamic.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtEthernetTemplateTable.CdtEthernetTemplateEntry>`
        
        

        """

        _prefix = 'cisco-dynamic-template'
        _revision = '2007-09-06'

        def __init__(self):
            self.parent = None
            self.cdtethernettemplateentry = YList()
            self.cdtethernettemplateentry.parent = self
            self.cdtethernettemplateentry.name = 'cdtethernettemplateentry'


        class CdtEthernetTemplateEntry(object):
            """
            An entry containing attributes relating to dynamic interfaces
            initiated on Ethernet virtual interfaces (e.g., EoMPLS) or
            automatically created VLANs.
            
            The system automatically creates an entry when the system or the
            EMS/NMS creates a row in the cdtTemplateTable with a
            cdtTemplateType of one of the following values\:
            
                'derived'
                'ethernet'
            
            Likewise, the system automatically destroys an entry when the
            system or the EMS/NMS destroys the corresponding row in the
            cdtTemplateTable.
            
            .. attribute:: cdttemplatename
            
            	
            	**type**\: str
            
            	**range:** 1..64
            
            .. attribute:: cdtethernetbridgedomain
            
            	This object specifies the name of the bridge domain..
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cdtethernetipv4pointtopoint
            
            	This object specifies whether..
            	**type**\: bool
            
            .. attribute:: cdtethernetmacaddr
            
            	This object specifies the..
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: cdtethernetpppoeenable
            
            	This object specifies whether..
            	**type**\: bool
            
            .. attribute:: cdtethernetvalid
            
            	This object specifies which attributes in the dynamic template have been configured to valid values.  Each bit in this bit string corresponds to a column in this table.  If the bit is '0', then the value of the corresponding column is not valid.  If the bit is '1', then the value of the corresponding column has been configured to a valid value.  The following list specifies the mappings between bits and the columns\:      bridgeDomain     => cdtEthernetBridgeDomain     pppoeEnable      => cdtEthernetPppoeEnable     ipv4PointToPoint => cdtEthernetIpv4PointToPoint     macAddr          => cdtEthernetMacAddr
            	**type**\: :py:class:`CdtEthernetValid_Bits <ydk.models.dynamic.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtEthernetTemplateTable.CdtEthernetTemplateEntry.CdtEthernetValid_Bits>`
            
            

            """

            _prefix = 'cisco-dynamic-template'
            _revision = '2007-09-06'

            def __init__(self):
                self.parent = None
                self.cdttemplatename = None
                self.cdtethernetbridgedomain = None
                self.cdtethernetipv4pointtopoint = None
                self.cdtethernetmacaddr = None
                self.cdtethernetpppoeenable = None
                self.cdtethernetvalid = CISCODYNAMICTEMPLATEMIB.CdtEthernetTemplateTable.CdtEthernetTemplateEntry.CdtEthernetValid_Bits()

            class CdtEthernetValid_Bits(FixedBitsDict):
                """
                CdtEthernetValid_Bits

                This object specifies which attributes in the dynamic template
                have been configured to valid values.
                
                Each bit in this bit string corresponds to a column in this
                table.  If the bit is '0', then the value of the corresponding
                column is not valid.  If the bit is '1', then the value of the
                corresponding column has been configured to a valid value.
                
                The following list specifies the mappings between bits and the
                columns\:
                
                    bridgeDomain     => cdtEthernetBridgeDomain
                    pppoeEnable      => cdtEthernetPppoeEnable
                    ipv4PointToPoint => cdtEthernetIpv4PointToPoint
                    macAddr          => cdtEthernetMacAddr
                Keys are:- ipv4PointToPoint , macAddr , pppoeEnable , bridgeDomain

                """

                def __init__(self):
                    self._dictionary = { 
                        'ipv4PointToPoint':False,
                        'macAddr':False,
                        'pppoeEnable':False,
                        'bridgeDomain':False,
                    }
                    self._pos_map = { 
                        'ipv4PointToPoint':2,
                        'macAddr':3,
                        'pppoeEnable':1,
                        'bridgeDomain':0,
                    }

            @property
            def _common_path(self):
                if self.cdttemplatename is None:
                    raise YPYDataValidationError('Key property cdttemplatename is None')

                return '/CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/CISCO-DYNAMIC-TEMPLATE-MIB:cdtEthernetTemplateTable/CISCO-DYNAMIC-TEMPLATE-MIB:cdtEthernetTemplateEntry[CISCO-DYNAMIC-TEMPLATE-MIB:cdtTemplateName = ' + str(self.cdttemplatename) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cdttemplatename is not None:
                    return True

                if self.cdtethernetbridgedomain is not None:
                    return True

                if self.cdtethernetipv4pointtopoint is not None:
                    return True

                if self.cdtethernetmacaddr is not None:
                    return True

                if self.cdtethernetpppoeenable is not None:
                    return True

                if self.cdtethernetvalid is not None:
                    if self.cdtethernetvalid._has_data():
                        return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.dynamic._meta import _CISCO_DYNAMIC_TEMPLATE_MIB as meta
                return meta._meta_table['CISCODYNAMICTEMPLATEMIB.CdtEthernetTemplateTable.CdtEthernetTemplateEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/CISCO-DYNAMIC-TEMPLATE-MIB:cdtEthernetTemplateTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cdtethernettemplateentry is not None:
                for child_ref in self.cdtethernettemplateentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.dynamic._meta import _CISCO_DYNAMIC_TEMPLATE_MIB as meta
            return meta._meta_table['CISCODYNAMICTEMPLATEMIB.CdtEthernetTemplateTable']['meta_info']


    class CdtIfTemplateTable(object):
        """
        This table contains attributes relating to interface
        configuration.
        
        This table has a sparse\-dependent relationship on the
        cdtTemplateTable, containing a row for each dynamic template
        having a cdtTemplateType of one of the following values\:
        
            'derived'
            'ppp'
            'ethernet'
            'ipSubscriber'
        
        .. attribute:: cdtiftemplateentry
        
        	An entry containing attributes relating to interface configuration.  The system automatically creates an entry when the system or the EMS/NMS creates a row in the cdtTemplateTable with a cdtTemplateType of one of the following values\:      'derived'     'ppp'     'ethernet'     'ipSubscriber'  Likewise, the system automatically destroys an entry when the system or the EMS/NMS destroys the corresponding row in the cdtTemplateTable
        	**type**\: list of :py:class:`CdtIfTemplateEntry <ydk.models.dynamic.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtIfTemplateTable.CdtIfTemplateEntry>`
        
        

        """

        _prefix = 'cisco-dynamic-template'
        _revision = '2007-09-06'

        def __init__(self):
            self.parent = None
            self.cdtiftemplateentry = YList()
            self.cdtiftemplateentry.parent = self
            self.cdtiftemplateentry.name = 'cdtiftemplateentry'


        class CdtIfTemplateEntry(object):
            """
            An entry containing attributes relating to interface
            configuration.
            
            The system automatically creates an entry when the system or the
            EMS/NMS creates a row in the cdtTemplateTable with a
            cdtTemplateType of one of the following values\:
            
                'derived'
                'ppp'
                'ethernet'
                'ipSubscriber'
            
            Likewise, the system automatically destroys an entry when the
            system or the EMS/NMS destroys the corresponding row in the
            cdtTemplateTable.
            
            .. attribute:: cdttemplatename
            
            	
            	**type**\: str
            
            	**range:** 1..64
            
            .. attribute:: cdtifcdpenable
            
            	This object specifies whether the target interface participates in the Cisco Discovery Protocol (CDP).  This column is valid only if the 'cdpEnable' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\: bool
            
            .. attribute:: cdtifflowmonitor
            
            	This object specifies the name of the flow monitor associated with the target interface.  This column is valid only if the 'flowMonitor' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cdtifipv4mtu
            
            	This object specifies the Maximum Transfer Unit (MTU) size for IPv4 packets sent on the target interface.  The value '0' cannot be written to an instance of this object. However, it serves as a convenient value when the column is not valid.  This column is valid only if the 'ipv4Mtu' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\: int
            
            	**range:** 0 \| 128..65535
            
            .. attribute:: cdtifipv4subenable
            
            	This object specifies whether the target interface allows IPv4 subscriber sessions.  This column is valid only if the 'ipv4SubEnable' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\: bool
            
            .. attribute:: cdtifipv4tcpmssadjust
            
            	This object specifies the adjustment to the Maximum Segment Size (MSS) of TCP SYN packets received by the target interface contained in IPv4 datagrams.  The value '0' cannot be written to an instance of this object. However, it serves as a convenient value when the column is not valid.  This column is valid only if the 'ipv4TcpMssAdjust' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\: int
            
            	**range:** 0 \| 500..1460
            
            .. attribute:: cdtifipv4unnumbered
            
            	This object specifies the interface of the source address that the target interface uses when originating IPv4 packets.  The value '0' cannot be written to an instance of this object. However, it serves as a convenient value when the column is not valid (e.g., immediately following the creation of an instance of the object).  This column is valid only if the 'ipv4Unnumbered' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: cdtifipv4verifyunirpf
            
            	This object specifies whether the type of unicast RPF the system performs on IPv4 packets received by the target interface.  This column is valid only if the 'ipv4VerifyUniRpf' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\: :py:class:`UnicastRpfType_Enum <ydk.models.ip.CISCO_IP_URPF_MIB.UnicastRpfType_Enum>`
            
            .. attribute:: cdtifipv4verifyunirpfacl
            
            	This object specifies the name (or number) of the IPv4 ACL used to determine whether the system should permit/deny packets received by the target interface that fail unicast RPF verification.  This column is valid only if the 'ipv4VerifyUniRpfAcl' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cdtifipv4verifyunirpfopts
            
            	This object specifies the options that affect how the system performs unicast RPF on IPv4 packets received by the target interface.  This column is valid only if the 'ipv4VerifyUniRpfOpts' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\: :py:class:`UnicastRpfOptions_Bits <ydk.models.ip.CISCO_IP_URPF_MIB.UnicastRpfOptions_Bits>`
            
            .. attribute:: cdtifipv6enable
            
            	This object specifies whether the system processes IPv6 packets received by the target interface.  This column is valid only if the 'ipv6Enable' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\: bool
            
            .. attribute:: cdtifipv6nddadattempts
            
            	This object specifies the number of consecutive neighbor solitication messages the system sends on the target interface while performing duplicate address detection on unicast IPv6 addresses on the target interface.  The value '0' disables duplicate address detection on the target interface.  This column is valid only if the 'ipv6NdDadAttempts' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\: int
            
            	**range:** 0..600
            
            .. attribute:: cdtifipv6ndnsinterval
            
            	This object specifies the interval between neighbor solicitation retransmissions on the target interface.  This column is valid only if the 'ipv6NdNsIntervals' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\: int
            
            	**range:** 1000..3600000
            
            .. attribute:: cdtifipv6ndopts
            
            	This object specifies options that affect advertisements sent on the target interface\:      'advertise'         This option specifies that the system should advertise         the IPv6 prefix (i.e., the corresponding instance of         cdtIfIpv6NdPrefix).      'onlink'         This option specifies that the IPv6 prefix has been         assigned to a link.  If set to '0', the system         advertises the IPv6 prefix as 'offlink'.      'router'         This option indicates that the router will send the full         router address and not set the 'R' bit in prefix         advertisements.      'autoConfig'         This option indicates to hosts on the local link that         the specified prefix supports IPv6 auto\-configuration.      'advertisementInterval'         This option specifies the advertisement interval option         in router advertisements sent on the target interface.      'managedConfigFlag'         This option causes the system to set the 'managed         address configuration flag' in router advertisements         sent on the target interface.      'otherConfigFlag'         This option causes the system to set the 'other stateful         configuration' flag in router advertisements sent on the         target interface.      'frameIpv6Prefix'         This option causes the system to add the prefix in a         received RADIUS framed IPv6 prefix attribute to the         target interface's neighbor discovery prefix queue and         includes it in router advertisements sent on the target         interface.      'raSupress'         This option suppresses the transmission of router         advertisements on the target interface.  This column is valid only if the 'ipv6NdOpts' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\: :py:class:`CdtIfIpv6NdOpts_Bits <ydk.models.dynamic.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtIfTemplateTable.CdtIfTemplateEntry.CdtIfIpv6NdOpts_Bits>`
            
            .. attribute:: cdtifipv6ndpreferredlife
            
            	This object specifies the interval that the system advertises the IPv6 prefix (i.e., the corresponding instance of cdtIfIpv6NdPrefix) as 'preferred' for IPv6 router advertisements sent on the target interface.  This column is valid only if the 'ipv6NdPreferredLife' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: cdtifipv6ndprefix
            
            	This object specifies the IPv6 network number included in IPv6 router advertisements sent on the target interface.  This column is valid only if the 'ipv6NdPrefix' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\: str
            
            .. attribute:: cdtifipv6ndprefixlength
            
            	This object specifies the length of the IPv6 prefix specified by the corresponding instance of cdtIpv6NdPrefix.  This column is valid only if the 'ipv6NdPrefix' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\: int
            
            	**range:** 0..2040
            
            .. attribute:: cdtifipv6ndraintervalmax
            
            	This object specifies the maximum interval between IPv6 router advertisements sent on the target interface.  The value '0' cannot be written to an instance of this object. However, it serves as a convenient value when the column is not valid.  This column is valid only if the 'ipv6NdRaInterval' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cdtifipv6ndraintervalmin
            
            	This object specifies the minimum interval between IPv6 router advertisements sent on the target interface.  The value of this column has the following restrictions\:  1)  This value cannot be less than 75% of the value specified     for cdtIfIpv6NdRaIntervalMax.  2)  If the corresponding instance of cdtIfIpv6NdRaIntervalUnits     is 'seconds', then this value cannot be less than '3'.  3)  If the corresponding instance of cdtIfIpv6NdRaIntervalUnits     is 'milliseconds', then this value cannot be less than '30'.  If the target interface template does not specify this value, then the system automatically assumes a minimum interval that is 75% of the corresponding instance of cdtIfIpv6NdRaIntervalMax.  The value '0' cannot be written to an instance of this object. However, it serves as a convenient value when the column is not valid.  This column is valid only if the 'ipv6NdRaInterval' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cdtifipv6ndraintervalunits
            
            	This object specifies the units of time for the corresponding instances of cdtIfIpv6NdRaIntervalMin and cdtIfIpv6NdRaIntervalMax.  This column is valid only if the 'ipv6NdRaInterval' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\: :py:class:`CdtIfIpv6NdRaIntervalUnits_Enum <ydk.models.dynamic.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtIfTemplateTable.CdtIfTemplateEntry.CdtIfIpv6NdRaIntervalUnits_Enum>`
            
            .. attribute:: cdtifipv6ndralife
            
            	This object specifies the router lifetime value in IPv6 router advertisements sent on the target interface.  The value '0' specifies that neighbors should not consider the router as a default router
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cdtifipv6ndreachabletime
            
            	This object specifies the amount of time the system considers a neighbor of the target interface reachable after a reachability confirmation event has occurred.  The value '0' disables neighbor reachability detection on the target interface.  This column is valid only if the 'ipv6NdReachable' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cdtifipv6ndrouterpreference
            
            	This object specifies the Default Router Preference (DRP) for the router on the target interface.  This column is valid only if the 'ipv6NdRouterPreference' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\: :py:class:`CdtIfIpv6NdRouterPreference_Enum <ydk.models.dynamic.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtIfTemplateTable.CdtIfTemplateEntry.CdtIfIpv6NdRouterPreference_Enum>`
            
            .. attribute:: cdtifipv6ndvalidlife
            
            	This object specifies the interval that the system advertises the IPv6 prefix (i.e., the corresponding instance of cdtIfIpv6NdPrefix) as 'valid' for IPv6 router advertisements sent on the target interface.  This column is valid only if the 'ipv6NdValidLife' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: cdtifipv6subenable
            
            	This object specifies whether the target interface allows IPv6 subscriber sessions.  This column is valid only if the 'ipv6SubEnable' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\: bool
            
            .. attribute:: cdtifipv6tcpmssadjust
            
            	This object specifies the adjustment to the Maximum Segment Size (MSS) of TCP SYN packets received by the target interface contained in IPv6 datagrams.  The value '0' cannot be written to an instance of this object. However, it serves as a convenient value when the column is not valid.  This column is valid only if the 'ipv6TcpMssAdjust' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\: int
            
            	**range:** 0 \| 500..1460
            
            .. attribute:: cdtifipv6verifyunirpf
            
            	This object specifies whether the type of unicast RPF the system performs on IPv6 packets received by the target interface.  This column is valid only if the 'ipv6VerifyUniRpf' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\: :py:class:`UnicastRpfType_Enum <ydk.models.ip.CISCO_IP_URPF_MIB.UnicastRpfType_Enum>`
            
            .. attribute:: cdtifipv6verifyunirpfacl
            
            	This object specifies the name (or number) of the IPv6 ACL used to determine whether the system should permit/deny packets received by the target interface that fail unicast RPF verification.  This column is valid only if the 'ipv6VerifyUniRpfAcl' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cdtifipv6verifyunirpfopts
            
            	This object specifies the options that affect how the system performs unicast RPF on IPv6 packets received by the target interface.  This column is valid only if the 'ipv6VerifyUniRpfOpts' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\: :py:class:`UnicastRpfOptions_Bits <ydk.models.ip.CISCO_IP_URPF_MIB.UnicastRpfOptions_Bits>`
            
            .. attribute:: cdtifmtu
            
            	This object specifies the Maximum Transfer Unit (MTU) size for all packets sent on the target interface.  The value '0' cannot be written to an instance of this object. However, it serves as a convenient value when the column is not valid.  This column is valid only if the 'mtu' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\: int
            
            	**range:** 0 \| 64..65535
            
            .. attribute:: cdtifvalid
            
            	This object specifies which attributes in the dynamic template have been configured to valid values.  Each bit in this bit string corresponds to a column in this table.  If the bit is '0', then the value of the corresponding column is not valid.  If the bit is '1', then the value of the corresponding column has been configured to a valid value.  The following list specifies the mappings between bits and the columns\:      'mtu'                     => cdtIfMtu     'cdpEnable'               => cdtIfCdpEnable     'flowMonitor'             => cdtIfFlowMonitor     'ipv4Unnumbered'          => cdtIfIpv4Unnumbered     'ipv4SubEnable'           => cdtIfIpv4SubEnable     'ipv4Mtu'                 => cdtIfIpv4Mtu     'ipv4TcpMssAdjust'        => cdtIfIpv4TcpMssAdjust     'ipv4VerifyUniRpf'        => cdtIfIpv4VerifyUniRpf     'ipv4VerifyUniRpfAcl'     => cdtIfIpv4VerifyUniRpfAcl     'ipv4VerifyUniRpfOpts'    => cdtIfIpv4VerifyUniRpfOpts     'ipv6Enable'              => cdtIfIpv6Enable     'ipv6SubEnable'           => cdtIfIpv6SubEnable     'ipv6TcpMssAdjust'        => cdtIfIpv6TcpMssAdjust     'ipv6VerifyUniRpf'        => cdtIfIpv6VerifyUniRpf     'ipv6VerifyUniRpfAcl'     => cdtIfIpv6VerifyUniRpfAcl     'ipv6VerifyUniRpfOpts'    => cdtIfIpv6VerifyUniRpfOpts     'ipv6NdPrefix'            => cdtIfIpv6NdPrefix,                                  cdtIfIpv6NdPrefixLength     'ipv6NdValidLife'         => cdtIfIpv6NdValidLife     'ipv6NdPreferredLife'     => cdtIfIpv6NdPreferredLife     'ipv6NdOpts'              => cdtIfIpv6NdOpts     'ipv6NdDadAttempts'       => cdtIfIpv6NdDadAttempts     'ipv6NdNsInterval'        => cdtIfIpv6NdNsInterval     'ipv6NdReacableTime'      => cdtIfIpv6NdReacableTime     'ipv6NdRaIntervalMax'     => cdtIfIpv6NdRaIntervalUnits,                                  cdtIfIpv6NdRaIntervalMax     'ipv6NdRaIntervalMin'     => cdtIfIpv6NdRaIntervalMin     'ipv6NdRaLife'            => cdtIfIpv6NdRaLife     'ipv6NdRouterPreference'' => cdtIfIpv6NdRouterPreference
            	**type**\: :py:class:`CdtIfValid_Bits <ydk.models.dynamic.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtIfTemplateTable.CdtIfTemplateEntry.CdtIfValid_Bits>`
            
            

            """

            _prefix = 'cisco-dynamic-template'
            _revision = '2007-09-06'

            def __init__(self):
                self.parent = None
                self.cdttemplatename = None
                self.cdtifcdpenable = None
                self.cdtifflowmonitor = None
                self.cdtifipv4mtu = None
                self.cdtifipv4subenable = None
                self.cdtifipv4tcpmssadjust = None
                self.cdtifipv4unnumbered = None
                self.cdtifipv4verifyunirpf = None
                self.cdtifipv4verifyunirpfacl = None
                self.cdtifipv4verifyunirpfopts = UnicastRpfOptions_Bits()
                self.cdtifipv6enable = None
                self.cdtifipv6nddadattempts = None
                self.cdtifipv6ndnsinterval = None
                self.cdtifipv6ndopts = CISCODYNAMICTEMPLATEMIB.CdtIfTemplateTable.CdtIfTemplateEntry.CdtIfIpv6NdOpts_Bits()
                self.cdtifipv6ndpreferredlife = None
                self.cdtifipv6ndprefix = None
                self.cdtifipv6ndprefixlength = None
                self.cdtifipv6ndraintervalmax = None
                self.cdtifipv6ndraintervalmin = None
                self.cdtifipv6ndraintervalunits = None
                self.cdtifipv6ndralife = None
                self.cdtifipv6ndreachabletime = None
                self.cdtifipv6ndrouterpreference = None
                self.cdtifipv6ndvalidlife = None
                self.cdtifipv6subenable = None
                self.cdtifipv6tcpmssadjust = None
                self.cdtifipv6verifyunirpf = None
                self.cdtifipv6verifyunirpfacl = None
                self.cdtifipv6verifyunirpfopts = UnicastRpfOptions_Bits()
                self.cdtifmtu = None
                self.cdtifvalid = CISCODYNAMICTEMPLATEMIB.CdtIfTemplateTable.CdtIfTemplateEntry.CdtIfValid_Bits()

            class CdtIfIpv6NdRaIntervalUnits_Enum(Enum):
                """
                CdtIfIpv6NdRaIntervalUnits_Enum

                This object specifies the units of time for the corresponding
                instances of cdtIfIpv6NdRaIntervalMin and
                cdtIfIpv6NdRaIntervalMax.
                
                This column is valid only if the 'ipv6NdRaInterval' bit of the
                corresponding instance of cdtIfValid is '1'.

                """

                SECONDS = 1

                MILLISECONDS = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.dynamic._meta import _CISCO_DYNAMIC_TEMPLATE_MIB as meta
                    return meta._meta_table['CISCODYNAMICTEMPLATEMIB.CdtIfTemplateTable.CdtIfTemplateEntry.CdtIfIpv6NdRaIntervalUnits_Enum']


            class CdtIfIpv6NdRouterPreference_Enum(Enum):
                """
                CdtIfIpv6NdRouterPreference_Enum

                This object specifies the Default Router Preference (DRP) for
                the router on the target interface.
                
                This column is valid only if the 'ipv6NdRouterPreference' bit of
                the corresponding instance of cdtIfValid is '1'.

                """

                HIGH = 1

                MEDIUM = 2

                LOW = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.dynamic._meta import _CISCO_DYNAMIC_TEMPLATE_MIB as meta
                    return meta._meta_table['CISCODYNAMICTEMPLATEMIB.CdtIfTemplateTable.CdtIfTemplateEntry.CdtIfIpv6NdRouterPreference_Enum']


            class CdtIfIpv6NdOpts_Bits(FixedBitsDict):
                """
                CdtIfIpv6NdOpts_Bits

                This object specifies options that affect advertisements sent
                on the target interface\:
                
                    'advertise'
                        This option specifies that the system should advertise
                        the IPv6 prefix (i.e., the corresponding instance of
                        cdtIfIpv6NdPrefix).
                
                    'onlink'
                        This option specifies that the IPv6 prefix has been
                        assigned to a link.  If set to '0', the system
                        advertises the IPv6 prefix as 'offlink'.
                
                    'router'
                        This option indicates that the router will send the full
                        router address and not set the 'R' bit in prefix
                        advertisements.
                
                    'autoConfig'
                        This option indicates to hosts on the local link that
                        the specified prefix supports IPv6 auto\-configuration.
                
                    'advertisementInterval'
                        This option specifies the advertisement interval option
                        in router advertisements sent on the target interface.
                
                    'managedConfigFlag'
                        This option causes the system to set the 'managed
                        address configuration flag' in router advertisements
                        sent on the target interface.
                
                    'otherConfigFlag'
                        This option causes the system to set the 'other stateful
                        configuration' flag in router advertisements sent on the
                        target interface.
                
                    'frameIpv6Prefix'
                        This option causes the system to add the prefix in a
                        received RADIUS framed IPv6 prefix attribute to the
                        target interface's neighbor discovery prefix queue and
                        includes it in router advertisements sent on the target
                        interface.
                
                    'raSupress'
                        This option suppresses the transmission of router
                        advertisements on the target interface.
                
                This column is valid only if the 'ipv6NdOpts' bit of the
                corresponding instance of cdtIfValid is '1'.
                Keys are:- framedIpv6Prefix , managedConfigFlag , raSuppress , otherConfigFlag , advertisementInterval , router , onlink , advertise , autoConfig

                """

                def __init__(self):
                    self._dictionary = { 
                        'framedIpv6Prefix':False,
                        'managedConfigFlag':False,
                        'raSuppress':False,
                        'otherConfigFlag':False,
                        'advertisementInterval':False,
                        'router':False,
                        'onlink':False,
                        'advertise':False,
                        'autoConfig':False,
                    }
                    self._pos_map = { 
                        'framedIpv6Prefix':7,
                        'managedConfigFlag':5,
                        'raSuppress':8,
                        'otherConfigFlag':6,
                        'advertisementInterval':4,
                        'router':2,
                        'onlink':1,
                        'advertise':0,
                        'autoConfig':3,
                    }

            class CdtIfValid_Bits(FixedBitsDict):
                """
                CdtIfValid_Bits

                This object specifies which attributes in the dynamic template
                have been configured to valid values.
                
                Each bit in this bit string corresponds to a column in this
                table.  If the bit is '0', then the value of the corresponding
                column is not valid.  If the bit is '1', then the value of the
                corresponding column has been configured to a valid value.
                
                The following list specifies the mappings between bits and the
                columns\:
                
                    'mtu'                     => cdtIfMtu
                    'cdpEnable'               => cdtIfCdpEnable
                    'flowMonitor'             => cdtIfFlowMonitor
                    'ipv4Unnumbered'          => cdtIfIpv4Unnumbered
                    'ipv4SubEnable'           => cdtIfIpv4SubEnable
                    'ipv4Mtu'                 => cdtIfIpv4Mtu
                    'ipv4TcpMssAdjust'        => cdtIfIpv4TcpMssAdjust
                    'ipv4VerifyUniRpf'        => cdtIfIpv4VerifyUniRpf
                    'ipv4VerifyUniRpfAcl'     => cdtIfIpv4VerifyUniRpfAcl
                    'ipv4VerifyUniRpfOpts'    => cdtIfIpv4VerifyUniRpfOpts
                    'ipv6Enable'              => cdtIfIpv6Enable
                    'ipv6SubEnable'           => cdtIfIpv6SubEnable
                    'ipv6TcpMssAdjust'        => cdtIfIpv6TcpMssAdjust
                    'ipv6VerifyUniRpf'        => cdtIfIpv6VerifyUniRpf
                    'ipv6VerifyUniRpfAcl'     => cdtIfIpv6VerifyUniRpfAcl
                    'ipv6VerifyUniRpfOpts'    => cdtIfIpv6VerifyUniRpfOpts
                    'ipv6NdPrefix'            => cdtIfIpv6NdPrefix,
                                                 cdtIfIpv6NdPrefixLength
                    'ipv6NdValidLife'         => cdtIfIpv6NdValidLife
                    'ipv6NdPreferredLife'     => cdtIfIpv6NdPreferredLife
                    'ipv6NdOpts'              => cdtIfIpv6NdOpts
                    'ipv6NdDadAttempts'       => cdtIfIpv6NdDadAttempts
                    'ipv6NdNsInterval'        => cdtIfIpv6NdNsInterval
                    'ipv6NdReacableTime'      => cdtIfIpv6NdReacableTime
                    'ipv6NdRaIntervalMax'     => cdtIfIpv6NdRaIntervalUnits,
                                                 cdtIfIpv6NdRaIntervalMax
                    'ipv6NdRaIntervalMin'     => cdtIfIpv6NdRaIntervalMin
                    'ipv6NdRaLife'            => cdtIfIpv6NdRaLife
                    'ipv6NdRouterPreference'' => cdtIfIpv6NdRouterPreference
                Keys are:- ipv6NdOpts , ipv4TcpMssAdjust , ipv6NdRaRouterPreference , ipv6NdValidLife , ipv6SubEnable , flowMonitor , cdpEnable , ipv4VerifyUniRpfOpts , ipv6NdReachableTime , ipv4VerifyUniRpfAcl , ipv6NdPreferredLife , ipv6NdRaIntervalMax , ipv6VerifyUniRpfOpts , ipv6NdRaIntervalMin , ipv6TcpMssAdjust , ipv6NdNsInterval , ipv6NdPrefix , ipv4Unnumbered , ipv6NdRaLife , ipv4Mtu , ipv6VerifyUniRpf , ipv6Enable , mtu , ipv6NdDadAttempts , ipv6VerifyUniRpfAcl , ipv4VerifyUniRpf , ipv4SubEnable

                """

                def __init__(self):
                    self._dictionary = { 
                        'ipv6NdOpts':False,
                        'ipv4TcpMssAdjust':False,
                        'ipv6NdRaRouterPreference':False,
                        'ipv6NdValidLife':False,
                        'ipv6SubEnable':False,
                        'flowMonitor':False,
                        'cdpEnable':False,
                        'ipv4VerifyUniRpfOpts':False,
                        'ipv6NdReachableTime':False,
                        'ipv4VerifyUniRpfAcl':False,
                        'ipv6NdPreferredLife':False,
                        'ipv6NdRaIntervalMax':False,
                        'ipv6VerifyUniRpfOpts':False,
                        'ipv6NdRaIntervalMin':False,
                        'ipv6TcpMssAdjust':False,
                        'ipv6NdNsInterval':False,
                        'ipv6NdPrefix':False,
                        'ipv4Unnumbered':False,
                        'ipv6NdRaLife':False,
                        'ipv4Mtu':False,
                        'ipv6VerifyUniRpf':False,
                        'ipv6Enable':False,
                        'mtu':False,
                        'ipv6NdDadAttempts':False,
                        'ipv6VerifyUniRpfAcl':False,
                        'ipv4VerifyUniRpf':False,
                        'ipv4SubEnable':False,
                    }
                    self._pos_map = { 
                        'ipv6NdOpts':19,
                        'ipv4TcpMssAdjust':6,
                        'ipv6NdRaRouterPreference':26,
                        'ipv6NdValidLife':17,
                        'ipv6SubEnable':11,
                        'flowMonitor':2,
                        'cdpEnable':1,
                        'ipv4VerifyUniRpfOpts':9,
                        'ipv6NdReachableTime':22,
                        'ipv4VerifyUniRpfAcl':8,
                        'ipv6NdPreferredLife':18,
                        'ipv6NdRaIntervalMax':23,
                        'ipv6VerifyUniRpfOpts':15,
                        'ipv6NdRaIntervalMin':24,
                        'ipv6TcpMssAdjust':12,
                        'ipv6NdNsInterval':21,
                        'ipv6NdPrefix':16,
                        'ipv4Unnumbered':3,
                        'ipv6NdRaLife':25,
                        'ipv4Mtu':5,
                        'ipv6VerifyUniRpf':13,
                        'ipv6Enable':10,
                        'mtu':0,
                        'ipv6NdDadAttempts':20,
                        'ipv6VerifyUniRpfAcl':14,
                        'ipv4VerifyUniRpf':7,
                        'ipv4SubEnable':4,
                    }

            @property
            def _common_path(self):
                if self.cdttemplatename is None:
                    raise YPYDataValidationError('Key property cdttemplatename is None')

                return '/CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/CISCO-DYNAMIC-TEMPLATE-MIB:cdtIfTemplateTable/CISCO-DYNAMIC-TEMPLATE-MIB:cdtIfTemplateEntry[CISCO-DYNAMIC-TEMPLATE-MIB:cdtTemplateName = ' + str(self.cdttemplatename) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cdttemplatename is not None:
                    return True

                if self.cdtifcdpenable is not None:
                    return True

                if self.cdtifflowmonitor is not None:
                    return True

                if self.cdtifipv4mtu is not None:
                    return True

                if self.cdtifipv4subenable is not None:
                    return True

                if self.cdtifipv4tcpmssadjust is not None:
                    return True

                if self.cdtifipv4unnumbered is not None:
                    return True

                if self.cdtifipv4verifyunirpf is not None:
                    return True

                if self.cdtifipv4verifyunirpfacl is not None:
                    return True

                if self.cdtifipv4verifyunirpfopts is not None:
                    if self.cdtifipv4verifyunirpfopts._has_data():
                        return True

                if self.cdtifipv6enable is not None:
                    return True

                if self.cdtifipv6nddadattempts is not None:
                    return True

                if self.cdtifipv6ndnsinterval is not None:
                    return True

                if self.cdtifipv6ndopts is not None:
                    if self.cdtifipv6ndopts._has_data():
                        return True

                if self.cdtifipv6ndpreferredlife is not None:
                    return True

                if self.cdtifipv6ndprefix is not None:
                    return True

                if self.cdtifipv6ndprefixlength is not None:
                    return True

                if self.cdtifipv6ndraintervalmax is not None:
                    return True

                if self.cdtifipv6ndraintervalmin is not None:
                    return True

                if self.cdtifipv6ndraintervalunits is not None:
                    return True

                if self.cdtifipv6ndralife is not None:
                    return True

                if self.cdtifipv6ndreachabletime is not None:
                    return True

                if self.cdtifipv6ndrouterpreference is not None:
                    return True

                if self.cdtifipv6ndvalidlife is not None:
                    return True

                if self.cdtifipv6subenable is not None:
                    return True

                if self.cdtifipv6tcpmssadjust is not None:
                    return True

                if self.cdtifipv6verifyunirpf is not None:
                    return True

                if self.cdtifipv6verifyunirpfacl is not None:
                    return True

                if self.cdtifipv6verifyunirpfopts is not None:
                    if self.cdtifipv6verifyunirpfopts._has_data():
                        return True

                if self.cdtifmtu is not None:
                    return True

                if self.cdtifvalid is not None:
                    if self.cdtifvalid._has_data():
                        return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.dynamic._meta import _CISCO_DYNAMIC_TEMPLATE_MIB as meta
                return meta._meta_table['CISCODYNAMICTEMPLATEMIB.CdtIfTemplateTable.CdtIfTemplateEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/CISCO-DYNAMIC-TEMPLATE-MIB:cdtIfTemplateTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cdtiftemplateentry is not None:
                for child_ref in self.cdtiftemplateentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.dynamic._meta import _CISCO_DYNAMIC_TEMPLATE_MIB as meta
            return meta._meta_table['CISCODYNAMICTEMPLATEMIB.CdtIfTemplateTable']['meta_info']


    class CdtPppPeerIpAddrPoolTable(object):
        """
        This table contains a prioritized list of named pools for each
        PPP template.  A list corresponding to a PPP template
        specifies the pools the system searches in an attempt to
        assign an IP address to the peer of a target PPP connection.
        The system searches the pools in the order of their priority.
        
        This table has an expansion dependent relationship on the
        cdtPppTemplateTable, containing zero or more rows for each PPP
        template.
        
        .. attribute:: cdtppppeeripaddrpoolentry
        
        	An entry specifies a named pool in a list of pools associated with a PPP template.  A PPP template can only have named pools associated with it if it has a cdtPppPeerIpAddrSrc of 'pool'.  Any attempt to create an entry for a PPP template that does not have a cdtPppPeerIpAddrSrc of 'pool' must result in a response having an error\-status of 'inconsistentValue'.  The system automatically creates a corresponding entry when the system associates a named pool with a PPP template through another management entity (e.g., the system's local console).  The system automatically destroys an entry under the following circumstances\:  1)  The system or EMS/NMS destroys the corresponding row in the     cdtTemplateTable.  2)  The system or EMS/NMS sets the corresponding instance of     cdtPppPeerIpAddrSrc with a value other than 'pool'
        	**type**\: list of :py:class:`CdtPppPeerIpAddrPoolEntry <ydk.models.dynamic.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtPppPeerIpAddrPoolTable.CdtPppPeerIpAddrPoolEntry>`
        
        

        """

        _prefix = 'cisco-dynamic-template'
        _revision = '2007-09-06'

        def __init__(self):
            self.parent = None
            self.cdtppppeeripaddrpoolentry = YList()
            self.cdtppppeeripaddrpoolentry.parent = self
            self.cdtppppeeripaddrpoolentry.name = 'cdtppppeeripaddrpoolentry'


        class CdtPppPeerIpAddrPoolEntry(object):
            """
            An entry specifies a named pool in a list of pools associated
            with a PPP template.  A PPP template can only have named
            pools associated with it if it has a cdtPppPeerIpAddrSrc of
            'pool'.
            
            Any attempt to create an entry for a PPP template that does not
            have a cdtPppPeerIpAddrSrc of 'pool' must result in a response
            having an error\-status of 'inconsistentValue'.
            
            The system automatically creates a corresponding entry when the
            system associates a named pool with a PPP template through
            another management entity (e.g., the system's local console).
            
            The system automatically destroys an entry under the following
            circumstances\:
            
            1)  The system or EMS/NMS destroys the corresponding row in the
                cdtTemplateTable.
            
            2)  The system or EMS/NMS sets the corresponding instance of
                cdtPppPeerIpAddrSrc with a value other than 'pool'.
            
            .. attribute:: cdtppppeeripaddrpoolpriority
            
            	This object indicates the relative priority of the named pool in the list corresponding to a PPP template.  The system searches pools in the order of priority, where lower values represent higher priority
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: cdttemplatename
            
            	
            	**type**\: str
            
            	**range:** 1..64
            
            .. attribute:: cdtppppeeripaddrpoolname
            
            	This object specifies the name of the IP address pool associated with the PPP template
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cdtppppeeripaddrpoolstatus
            
            	This object specifies the status of the entry.  The following columns must be valid before activating a subscriber access profile\:      \- cdtPppPeerIpAddrPoolStorage     \- cdtPppPeerIpAddrPoolName  However, these objects specify a default value.  Thus, it is possible to use create\-and\-go semantics without setting any additional columns.  An implementation must not allow the EMS/NMS to create an entry if the corresponding instance of cdtPppPeerIpAddrSrc is not 'pool'.  An implementation must allow the EMS/NMS to modify any column when this column is 'active'
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: cdtppppeeripaddrpoolstorage
            
            	This object specifies what happens to the name pool entry upon restart.  If the corresponding instance of cdtTemplateSrc is not 'local', then this column must be 'volatile'
            	**type**\: :py:class:`StorageType_Enum <ydk.models.snmpv2.SNMPv2_TC.StorageType_Enum>`
            
            

            """

            _prefix = 'cisco-dynamic-template'
            _revision = '2007-09-06'

            def __init__(self):
                self.parent = None
                self.cdtppppeeripaddrpoolpriority = None
                self.cdttemplatename = None
                self.cdtppppeeripaddrpoolname = None
                self.cdtppppeeripaddrpoolstatus = None
                self.cdtppppeeripaddrpoolstorage = None

            @property
            def _common_path(self):
                if self.cdtppppeeripaddrpoolpriority is None:
                    raise YPYDataValidationError('Key property cdtppppeeripaddrpoolpriority is None')
                if self.cdttemplatename is None:
                    raise YPYDataValidationError('Key property cdttemplatename is None')

                return '/CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/CISCO-DYNAMIC-TEMPLATE-MIB:cdtPppPeerIpAddrPoolTable/CISCO-DYNAMIC-TEMPLATE-MIB:cdtPppPeerIpAddrPoolEntry[CISCO-DYNAMIC-TEMPLATE-MIB:cdtPppPeerIpAddrPoolPriority = ' + str(self.cdtppppeeripaddrpoolpriority) + '][CISCO-DYNAMIC-TEMPLATE-MIB:cdtTemplateName = ' + str(self.cdttemplatename) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cdtppppeeripaddrpoolpriority is not None:
                    return True

                if self.cdttemplatename is not None:
                    return True

                if self.cdtppppeeripaddrpoolname is not None:
                    return True

                if self.cdtppppeeripaddrpoolstatus is not None:
                    return True

                if self.cdtppppeeripaddrpoolstorage is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.dynamic._meta import _CISCO_DYNAMIC_TEMPLATE_MIB as meta
                return meta._meta_table['CISCODYNAMICTEMPLATEMIB.CdtPppPeerIpAddrPoolTable.CdtPppPeerIpAddrPoolEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/CISCO-DYNAMIC-TEMPLATE-MIB:cdtPppPeerIpAddrPoolTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cdtppppeeripaddrpoolentry is not None:
                for child_ref in self.cdtppppeeripaddrpoolentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.dynamic._meta import _CISCO_DYNAMIC_TEMPLATE_MIB as meta
            return meta._meta_table['CISCODYNAMICTEMPLATEMIB.CdtPppPeerIpAddrPoolTable']['meta_info']


    class CdtPppTemplateTable(object):
        """
        This table contains attributes relating to PPP connection
        configuration.
        
        This table has a sparse\-dependent relationship on the
        cdtTemplateTable, containing a row for each dynamic template
        having a cdtTemplateType of one of the following values\:
        
            'derived'
            'ppp'
        
        .. attribute:: cdtppptemplateentry
        
        	An entry containing attributes relating to PPP connection configuration.  The system automatically creates an entry when the system or the EMS/NMS creates a row in the cdtTemplateTable with a cdtTemplateType of one of the following values\:      'derived'     'ppp'  Likewise, the system automatically destroys an entry when the system or the EMS/NMS destroys the corresponding row in the cdtTemplateTable
        	**type**\: list of :py:class:`CdtPppTemplateEntry <ydk.models.dynamic.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtPppTemplateTable.CdtPppTemplateEntry>`
        
        

        """

        _prefix = 'cisco-dynamic-template'
        _revision = '2007-09-06'

        def __init__(self):
            self.parent = None
            self.cdtppptemplateentry = YList()
            self.cdtppptemplateentry.parent = self
            self.cdtppptemplateentry.name = 'cdtppptemplateentry'


        class CdtPppTemplateEntry(object):
            """
            An entry containing attributes relating to PPP connection
            configuration.
            
            The system automatically creates an entry when the system or the
            EMS/NMS creates a row in the cdtTemplateTable with a
            cdtTemplateType of one of the following values\:
            
                'derived'
                'ppp'
            
            Likewise, the system automatically destroys an entry when the
            system or the EMS/NMS destroys the corresponding row in the
            cdtTemplateTable.
            
            .. attribute:: cdttemplatename
            
            	
            	**type**\: str
            
            	**range:** 1..64
            
            .. attribute:: cdtpppaccounting
            
            	This object specifies whether the system applies accounting services to the target PPP connection.  This column is valid only if the 'accounting' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\: bool
            
            .. attribute:: cdtpppauthentication
            
            	This object specifies authentication services applied to a target PPP connection and other options affecting authentication services\:      'chap'         This option enables the Challenge Handshake Protocol (CHAP)         on a target PPP connection.      'msChap'         This option enables Microsoft's CHAP on a target PPP         connection.      'msChapV2'         This option enables version 2 of Microsoft's CHAP on a         target PPP connection.      'pap'         This option enables Password Authentication Protocol (PAP)         on a target PPP connection.      'eap'         This option enables Extensible Authentication Protocol (EAP)         on a target PPP connection.      'optional'         This option specifies that the system accepts the connection         even if the peer of a target PPP connection refuses to         accept the authentication methods the system has         requested.      'callin'         This option specifies that authentication should only happen         for incoming calls.      'oneTime'         This option specifies that the system accepts the username         and password in the username field of authentication         responses received on a target PPP connection.  This column is valid only if the 'authentication' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\: :py:class:`CdtPppAuthentication_Bits <ydk.models.dynamic.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtPppTemplateTable.CdtPppTemplateEntry.CdtPppAuthentication_Bits>`
            
            .. attribute:: cdtpppauthenticationmethods
            
            	This object specifies the name of a list of authentication methods used on a target PPP connection.  If the template does not include this attribute, then the system uses the default method list.  This column is valid only if the 'authentication' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cdtpppauthorization
            
            	This object specifies whether the system applies authorization services to a target PPP connection.  This column is valid only if the 'authorization' bit of the corresponding instance of cditPppValid is '1'
            	**type**\: bool
            
            .. attribute:: cdtpppchaphostname
            
            	This object specifies the hostname sent in a CHAP response on a target PPP connection.  If the template does not include this attribute, then the system uses its assigned hostname.  This column is valid only if the 'chapHostname' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cdtpppchapopts
            
            	This object specifies how the system processes the CHAP on a target PPP connection\:      'refuse'         This option specifies that the system should refuse CHAP         requests from peers of a target PPP connection.      'callin'         This option specifies that the system should only refuse         CHAP requests for incoming calls on a target PPP         connection.  This option is only relevant if the         'refuse' option is set to '1'.      'wait'         This option delays CHAP authentication until after the         peer of a target PPP connection has authenticated itself         to the system.      'encrypted'         This option specifies that the value specified by the         corresponding instance of cdtPppChapPassword is already         encrypted.  This column is valid only if the 'chapOpts' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\: :py:class:`CdtPppChapOpts_Bits <ydk.models.dynamic.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtPppTemplateTable.CdtPppTemplateEntry.CdtPppChapOpts_Bits>`
            
            .. attribute:: cdtpppchappassword
            
            	This object specifies the password used to construct a CHAP response on the target PPP connection.  This column is valid only if the 'chapPassword' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cdtpppeapidentity
            
            	This object specifies the identity sent in an EAP response on a target PPP connection.  This column is valid only if the 'eapIdentity' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cdtpppeapopts
            
            	This object specifies how the system processes the EAP on a target PPP connection\:      'refuse'         This option specifies that the system should refuse EAP         requests from peers of a target PPP connection.      'callin'         This option specifies that the system should only refuse EAP         requests for incoming calls on a target PPP connection.         This option is only relevant if the 'refuse' option is         set to '1'.      'wait'         This option delays EAP authentication until after the         peer of a target PPP connection has authenticated itself         to the system.      'local'         This option specifies that the system should locally         authenticate the peer of a target PPP connection,         rather than acting as a proxy to an external AAA server.  This column is valid only if the 'eapOpts' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\: :py:class:`CdtPppEapOpts_Bits <ydk.models.dynamic.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtPppTemplateTable.CdtPppTemplateEntry.CdtPppEapOpts_Bits>`
            
            .. attribute:: cdtpppeappassword
            
            	This object specifies the password used to construct an EAP response on a target PPP connection.  This column is valid only if the 'eapPassword' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cdtpppipcpaddroption
            
            	This object specifies the IPCP address option for a target PPP connection\:      'other'         The implementation of this MIB module does not recognize         the configured IPCP address option.      'accept'         The system accepts any non\-zero IP address from the peer         of a target PPP connection.      'required'         The system disconnects the peer of a target PPP         connection if it could not negotiate an IP address.      'unique'         The system disconnects the peer of a target PPP         connection if the IP address is already in use.  This column is valid only if the 'ipcpAddrOption' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\: :py:class:`CdtPppIpcpAddrOption_Enum <ydk.models.dynamic.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtPppTemplateTable.CdtPppTemplateEntry.CdtPppIpcpAddrOption_Enum>`
            
            .. attribute:: cdtpppipcpdnsoption
            
            	This object specifies the IPCP DNS option for the dynamic interface\:      'other'         The implementation of this MIB module does not recognize         the configured DNS option.      'accept'         The system accepts any non\-zero DNS address form the         peer of a target PPP connection.      'request'         The system requests the DNS address from the peer of a         target PPP connection.      'reject'         The system rejects the DNS option from the peer of a         target PPP connection.  This column is valid only if the 'ipcpDnsOption' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\: :py:class:`CdtPppIpcpDnsOption_Enum <ydk.models.dynamic.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtPppTemplateTable.CdtPppTemplateEntry.CdtPppIpcpDnsOption_Enum>`
            
            .. attribute:: cdtpppipcpdnsprimary
            
            	This object specifies the IP address of the primary DNS server offered to the peer of a target PPP connection.  This column is valid only if the 'ipcpDnsPrimary' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\: str
            
            .. attribute:: cdtpppipcpdnssecondary
            
            	This object specifies the IP address of the secondary DNS server offered to the peer of a target PPP connection.  This column is valid only if the 'ipcpDnsSecondary' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\: str
            
            .. attribute:: cdtpppipcpmask
            
            	This object specifies the IP address mask offered to the peer of a target PPP connection.  This column is valid only if the 'ipcpMask' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\: str
            
            .. attribute:: cdtpppipcpmaskoption
            
            	This object specifies the IPCP IP subnet mask option for a target PPP connection\:      'other'         The implementation of this MIB module does not recognize         the configured IP subnet mask option.      'request'         The system requests the IP subnet mask from the peer of         a target PPP connection.      'reject'         The system rejects the IP subnet mask option from the         peer of a target PPP connection.  This column is valid only if the 'ipcpMaskOption' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\: :py:class:`CdtPppIpcpMaskOption_Enum <ydk.models.dynamic.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtPppTemplateTable.CdtPppTemplateEntry.CdtPppIpcpMaskOption_Enum>`
            
            .. attribute:: cdtpppipcpwinsoption
            
            	This object specifies the IPCP WINS option for a target PPP connection\:      'other'         The implementation of this MIB module does not recognize         the configured WINS option.      'accept'         The system accepts any non\-zero WINS address from the         peer of a target PPP connection.      'request'         The system requests the WINS address from the peer of         a target PPP connection.      'reject'         The system rejects the WINS option from the peer of a         target PPP connection.  This column is valid only if the 'ipcpWinsOption' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\: :py:class:`CdtPppIpcpWinsOption_Enum <ydk.models.dynamic.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtPppTemplateTable.CdtPppTemplateEntry.CdtPppIpcpWinsOption_Enum>`
            
            .. attribute:: cdtpppipcpwinsprimary
            
            	This object specifies the IP address of the primary WINS server offered to the peer of a target PPP connection.  This column is valid only if the 'ipcpWinsPrimary' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\: str
            
            .. attribute:: cdtpppipcpwinssecondary
            
            	This object specifies the IP address of the secondary WINS server offered to the peer of a target PPP connection.  This column is valid only if the 'ipcpWinsSecondary' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\: str
            
            .. attribute:: cdtppploopbackignore
            
            	This object specifies whether the system ignores loopback on a target PPP connection.  When the system ignores loopback, loopback detection is disabled.  This column is valid only if the 'loopbackIgnore' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\: bool
            
            .. attribute:: cdtpppmaxbadauth
            
            	This object specifies the number of authentication failures allowed by the system before a target PPP connection is reset.  The value '0' cannot be written to an instance of this object. However, it serves as a convenient value when the column is not valid.  This column is valid only if the 'maxBadAuth' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cdtpppmaxconfigure
            
            	This object specifies the number of unacknowledged Configure\-Request messages a target PPP connection can send before the system abandons LCP or NCP negotiations.  This column is valid only if the 'maxConfigure' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: cdtpppmaxfailure
            
            	This object specifies the number of Configure\-Nak messages a target PPP connection can receive before the system abandons LCP or NCP negotiations.  This column is valid only if the 'maxFailure' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: cdtpppmaxterminate
            
            	This object specifies the number of unacknowledged Terminate\-Request messages a target PPP connection can send before the system abandons LCP or NCP negotiations.  This column is valid only if the 'maxTerminate' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: cdtpppmschapv1hostname
            
            	This object specifies the hostname sent in a Microsoft CHAP (v1) response on a target PPP connection.  If the template does not include this attribute, then the system uses its assigned hostname.  This column is valid only if the 'msChapV1Hostname' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cdtpppmschapv1opts
            
            	This object specifies how the system processes version 1 of Microsoft CHAP on a target PPP connection\:      'refuse'         This option specifies that the system should refuse         Microsoft CHAP (v1) requests from peers of a target PPP         connection.      'callin'         This option specifies that the system should only refuse         Microsoft CHAP (v1) requests for incoming calls on a         target PPP connection.  This option is only relevant if         the 'refuse' option is set to '1'.      'wait'         This option delays Microsoft CHAP (v1) authentication         until after the peer of a target PPP connection has         authenticated itself to the system.      'encrypted'         This option specifies that the value specified by the         corresponding instance of cdtPppMsChapV1Password is         already encrypted.  This column is valid only if the 'msChapV1Opts' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\: :py:class:`CdtPppMsChapV1Opts_Bits <ydk.models.dynamic.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtPppTemplateTable.CdtPppTemplateEntry.CdtPppMsChapV1Opts_Bits>`
            
            .. attribute:: cdtpppmschapv1password
            
            	This object specifies the password used to construct a Microsoft CHAP (v1) response on a target PPP connection.  This column is valid only if the 'msChapV1Password' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cdtpppmschapv2hostname
            
            	This object specifies the hostname sent in a Microsoft CHAP (v2) response on a target PPP connection.  If the template does not include this attribute, then the system uses its assigned hostname.  This column is valid only if the 'msChapV2Hostname' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cdtpppmschapv2opts
            
            	This object specifies how the system processes version 2 of Microsoft CHAP on a target PPP connection\:      'refuse'         This option specifies that the system should refuse         Microsoft CHAP (v2) requests from peers of a target PPP         connection.      'callin'         This option specifies that the system should only refuse         Microsoft CHAP (v2) requests for incoming calls on a         target PPP connection.  This option is only relevant if         the 'refuse' option is set to '1'.      'wait'         This option delays Microsoft CHAP (v2) authentication         until after the peer of a target PPP connection has         authenticated itself to the system.      'encrypted'         This option specifies that the value specified by the         corresponding instance of cdtPppMsChapV2Password is         already encrypted.  This column is valid only if the 'msChapV2Opts' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\: :py:class:`CdtPppMsChapV2Opts_Bits <ydk.models.dynamic.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtPppTemplateTable.CdtPppTemplateEntry.CdtPppMsChapV2Opts_Bits>`
            
            .. attribute:: cdtpppmschapv2password
            
            	This object specifies the password used to construct a Microsoft CHAP (v2) response on a target PPP connection.  This column is valid only if the 'msChapV2Password' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cdtppppapopts
            
            	This object specifies how the system processes the PAP on a target PPP connection\:      'refuse'         This option specifies that the system should refuse PAP         requests from peers of a target PPP connection.      'encrypted'         This option specifies that the value specified by the         corresponding instance of cdtPppPapSentPassword is         already encrypted.  This column is valid only if the 'papOpts' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\: :py:class:`CdtPppPapOpts_Bits <ydk.models.dynamic.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtPppTemplateTable.CdtPppTemplateEntry.CdtPppPapOpts_Bits>`
            
            .. attribute:: cdtppppappassword
            
            	This object specifies the username used to construct a PAP response on a target PPP connection.  This column is valid only if the 'papPassword' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cdtppppapusername
            
            	This object specifies the username sent in a PAP response on a target PPP connection.  This column is valid only if the 'papUsername' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cdtppppeerdefipaddr
            
            	This object specifies the IP address the system assigns to the peer of a target PPP connection.  This column is valid only if the 'peerDefIpAddr' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\: str
            
            .. attribute:: cdtppppeerdefipaddropts
            
            	This object specifies options that affect how the system assigns an IP address to the peer of a target PPP connection\:      'ipAddrForced'         This option forces the system to assign the next         available IP address in the pool to the peer of a         target PPP connection.  When disabled, the peer may         negotiate a specific IP address or the system can assign         the peer its previously assigned IP address.      'matchAaaPools'         This option specifies that the names of the IP address         pools provided by an external AAA server must appear in         the corresponding list of IP address pool specified by         the cdtPppPeerIpAddrPoolTable.      'backupPools'         This option specifies that the corresponding names of         the IP address pools specified by the         cditPppPeerIpAddrPoolTable serve as backup pools to         those provided by an external AAA server.      'staticPools'         This option suppresses an attempt to load pools from an         external AAA server when the system encounters a missing         pool name.  This column is valid only if the 'peerIpAddrOpts' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\: :py:class:`CdtPppPeerDefIpAddrOpts_Bits <ydk.models.dynamic.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtPppTemplateTable.CdtPppTemplateEntry.CdtPppPeerDefIpAddrOpts_Bits>`
            
            .. attribute:: cdtppppeerdefipaddrsrc
            
            	This object specifies how the system assigns an IP address to the peer of a target PPP connection\:      'static'         The system assigns the IP address specified by the         corresponding instance of cdtPppPeerDefIpAddr.      'pool'         The system allocates the first available IP address from         the corresponding list of named pools contained by the         cdtPppPeerIpAddrPoolTable.      'dhcp'         The system acts as a DHCP proxy\-client to obtain an IP         address.  This column is valid only if the 'peerDefIpAddrSrc' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\: :py:class:`CdtPppPeerDefIpAddrSrc_Enum <ydk.models.dynamic.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtPppTemplateTable.CdtPppTemplateEntry.CdtPppPeerDefIpAddrSrc_Enum>`
            
            .. attribute:: cdtppptimeoutauthentication
            
            	This objects specifies the maximum time the system will wait for a response to an authentication request on a target PPP connection.  This column is valid only if the 'timeoutAuthentication' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\: int
            
            	**range:** 1..255
            
            .. attribute:: cdtppptimeoutretry
            
            	This objects specifies the maximum time the system will wait for a response to a PPP control packets on a target PPP connection.  This column is valid only if the 'timeoutRetry' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\: int
            
            	**range:** 1..255
            
            .. attribute:: cdtpppvalid
            
            	This object specifies which attributes in the dynamic template have been configured to valid values.  Each bit in this bit string corresponds to a column in this table.  If the bit is '0', then the value of the corresponding column is not valid.  If the bit is '1', then the value of the corresponding column has been configured to a valid value.  The following list specifies the mappings between bits and the columns\:      accounting              => cdtPppAccounting     authentication          => cdtPppAuthentication     authenticationMethods   => cdtPppAuthenticationMethods     authorization           => cdtPppAuthorization     loopbackIgnore          => cdtPppLoopbackIgnore     maxBadAuth              => cdtPppMaxBadAuth     maxConfigure            => cdtPppMaxConfigure     maxFailure              => cdtPppMaxFailure     maxTerminate            => cdtPppMaxTerminate     timeoutAuthentication   => cdtPppTimeoutAuthentication     timeoutRetry            => cdtPppTimeoutRetry     chapOpts                => cdtPppChapOpts     chapHostname            => cdtPppChapHostname     chapPassword            => cdtPppChapPassword     msChapV1Opts            => cdtPppMsChapV1Opts     msChapV1Hostname        => cdtPppMsChapV1Hostname     msChapV1Password        => cdtPppMsChapV1Password     msChapV2Opts            => cdtPppMsChapV2Opts     msChapV2Hostname        => cdtPppMsChapV2Hostname     msChapV2Password        => cdtPppMsChapV2Password     papOpts                 => cdtPppPapOpts     papSentUsername         => cdtPppPapUsername     papSentPassword         => cdtPppPapPassword     eapOpts                 => cdtPppEapOpts     eapIdentity             => cdtPppEapIdentity     eapPassword             => cdtPppEapPassword     ipcpAddrOption          => cdtPppIpcpAddrOption     ipcpDnsOption           => cdtPppIpcpDnsOption     ipcpDnsPrimary          => cdtPppIpcpDnsPrimary     ipcpDnsSecondary        => cdtPppIpcpDnsSecondary     ipcpWinsOption          => cdtPppIpcpWinsOption     ipcpWinsPrimary         => cdtPppIpcpWinsPrimary     ipcpWinsSecondary       => cdtPppIpcpWinsSecondary     ipcpMaskOption          => cdtPppIpcpMaskOption     ipcpMask                => cdtPppIpcpMask     peerDefIpAddrOpts       => cdtPppPeerOpts     peerDefIpAddrSrc        => cdtPppPeerDefIpAddrSrc     peerDefIpAddr           => cdtPppPeerDefIpAddr
            	**type**\: :py:class:`CdtPppValid_Bits <ydk.models.dynamic.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtPppTemplateTable.CdtPppTemplateEntry.CdtPppValid_Bits>`
            
            

            """

            _prefix = 'cisco-dynamic-template'
            _revision = '2007-09-06'

            def __init__(self):
                self.parent = None
                self.cdttemplatename = None
                self.cdtpppaccounting = None
                self.cdtpppauthentication = CISCODYNAMICTEMPLATEMIB.CdtPppTemplateTable.CdtPppTemplateEntry.CdtPppAuthentication_Bits()
                self.cdtpppauthenticationmethods = None
                self.cdtpppauthorization = None
                self.cdtpppchaphostname = None
                self.cdtpppchapopts = CISCODYNAMICTEMPLATEMIB.CdtPppTemplateTable.CdtPppTemplateEntry.CdtPppChapOpts_Bits()
                self.cdtpppchappassword = None
                self.cdtpppeapidentity = None
                self.cdtpppeapopts = CISCODYNAMICTEMPLATEMIB.CdtPppTemplateTable.CdtPppTemplateEntry.CdtPppEapOpts_Bits()
                self.cdtpppeappassword = None
                self.cdtpppipcpaddroption = None
                self.cdtpppipcpdnsoption = None
                self.cdtpppipcpdnsprimary = None
                self.cdtpppipcpdnssecondary = None
                self.cdtpppipcpmask = None
                self.cdtpppipcpmaskoption = None
                self.cdtpppipcpwinsoption = None
                self.cdtpppipcpwinsprimary = None
                self.cdtpppipcpwinssecondary = None
                self.cdtppploopbackignore = None
                self.cdtpppmaxbadauth = None
                self.cdtpppmaxconfigure = None
                self.cdtpppmaxfailure = None
                self.cdtpppmaxterminate = None
                self.cdtpppmschapv1hostname = None
                self.cdtpppmschapv1opts = CISCODYNAMICTEMPLATEMIB.CdtPppTemplateTable.CdtPppTemplateEntry.CdtPppMsChapV1Opts_Bits()
                self.cdtpppmschapv1password = None
                self.cdtpppmschapv2hostname = None
                self.cdtpppmschapv2opts = CISCODYNAMICTEMPLATEMIB.CdtPppTemplateTable.CdtPppTemplateEntry.CdtPppMsChapV2Opts_Bits()
                self.cdtpppmschapv2password = None
                self.cdtppppapopts = CISCODYNAMICTEMPLATEMIB.CdtPppTemplateTable.CdtPppTemplateEntry.CdtPppPapOpts_Bits()
                self.cdtppppappassword = None
                self.cdtppppapusername = None
                self.cdtppppeerdefipaddr = None
                self.cdtppppeerdefipaddropts = CISCODYNAMICTEMPLATEMIB.CdtPppTemplateTable.CdtPppTemplateEntry.CdtPppPeerDefIpAddrOpts_Bits()
                self.cdtppppeerdefipaddrsrc = None
                self.cdtppptimeoutauthentication = None
                self.cdtppptimeoutretry = None
                self.cdtpppvalid = CISCODYNAMICTEMPLATEMIB.CdtPppTemplateTable.CdtPppTemplateEntry.CdtPppValid_Bits()

            class CdtPppIpcpAddrOption_Enum(Enum):
                """
                CdtPppIpcpAddrOption_Enum

                This object specifies the IPCP address option for a target PPP
                connection\:
                
                    'other'
                        The implementation of this MIB module does not recognize
                        the configured IPCP address option.
                
                    'accept'
                        The system accepts any non\-zero IP address from the peer
                        of a target PPP connection.
                
                    'required'
                        The system disconnects the peer of a target PPP
                        connection if it could not negotiate an IP address.
                
                    'unique'
                        The system disconnects the peer of a target PPP
                        connection if the IP address is already in use.
                
                This column is valid only if the 'ipcpAddrOption' bit of the
                corresponding instance of cdtPppValid is '1'.

                """

                OTHER = 1

                ACCEPT = 2

                REQUIRED = 3

                UNIQUE = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.dynamic._meta import _CISCO_DYNAMIC_TEMPLATE_MIB as meta
                    return meta._meta_table['CISCODYNAMICTEMPLATEMIB.CdtPppTemplateTable.CdtPppTemplateEntry.CdtPppIpcpAddrOption_Enum']


            class CdtPppIpcpDnsOption_Enum(Enum):
                """
                CdtPppIpcpDnsOption_Enum

                This object specifies the IPCP DNS option for the dynamic
                interface\:
                
                    'other'
                        The implementation of this MIB module does not recognize
                        the configured DNS option.
                
                    'accept'
                        The system accepts any non\-zero DNS address form the
                        peer of a target PPP connection.
                
                    'request'
                        The system requests the DNS address from the peer of a
                        target PPP connection.
                
                    'reject'
                        The system rejects the DNS option from the peer of a
                        target PPP connection.
                
                This column is valid only if the 'ipcpDnsOption' bit of the
                corresponding instance of cdtPppValid is '1'.

                """

                OTHER = 1

                ACCEPT = 2

                REQUEST = 3

                REJECT = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.dynamic._meta import _CISCO_DYNAMIC_TEMPLATE_MIB as meta
                    return meta._meta_table['CISCODYNAMICTEMPLATEMIB.CdtPppTemplateTable.CdtPppTemplateEntry.CdtPppIpcpDnsOption_Enum']


            class CdtPppIpcpMaskOption_Enum(Enum):
                """
                CdtPppIpcpMaskOption_Enum

                This object specifies the IPCP IP subnet mask option for a
                target PPP connection\:
                
                    'other'
                        The implementation of this MIB module does not recognize
                        the configured IP subnet mask option.
                
                    'request'
                        The system requests the IP subnet mask from the peer of
                        a target PPP connection.
                
                    'reject'
                        The system rejects the IP subnet mask option from the
                        peer of a target PPP connection.
                
                This column is valid only if the 'ipcpMaskOption' bit of the
                corresponding instance of cdtPppValid is '1'.

                """

                OTHER = 1

                REQUEST = 2

                REJECT = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.dynamic._meta import _CISCO_DYNAMIC_TEMPLATE_MIB as meta
                    return meta._meta_table['CISCODYNAMICTEMPLATEMIB.CdtPppTemplateTable.CdtPppTemplateEntry.CdtPppIpcpMaskOption_Enum']


            class CdtPppIpcpWinsOption_Enum(Enum):
                """
                CdtPppIpcpWinsOption_Enum

                This object specifies the IPCP WINS option for a target PPP
                connection\:
                
                    'other'
                        The implementation of this MIB module does not recognize
                        the configured WINS option.
                
                    'accept'
                        The system accepts any non\-zero WINS address from the
                        peer of a target PPP connection.
                
                    'request'
                        The system requests the WINS address from the peer of
                        a target PPP connection.
                
                    'reject'
                        The system rejects the WINS option from the peer of a
                        target PPP connection.
                
                This column is valid only if the 'ipcpWinsOption' bit of the
                corresponding instance of cdtPppValid is '1'.

                """

                OTHER = 1

                ACCEPT = 2

                REQUEST = 3

                REJECT = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.dynamic._meta import _CISCO_DYNAMIC_TEMPLATE_MIB as meta
                    return meta._meta_table['CISCODYNAMICTEMPLATEMIB.CdtPppTemplateTable.CdtPppTemplateEntry.CdtPppIpcpWinsOption_Enum']


            class CdtPppPeerDefIpAddrSrc_Enum(Enum):
                """
                CdtPppPeerDefIpAddrSrc_Enum

                This object specifies how the system assigns an IP address to
                the peer of a target PPP connection\:
                
                    'static'
                        The system assigns the IP address specified by the
                        corresponding instance of cdtPppPeerDefIpAddr.
                
                    'pool'
                        The system allocates the first available IP address from
                        the corresponding list of named pools contained by the
                        cdtPppPeerIpAddrPoolTable.
                
                    'dhcp'
                        The system acts as a DHCP proxy\-client to obtain an IP
                        address.
                
                This column is valid only if the 'peerDefIpAddrSrc' bit of the
                corresponding instance of cdtPppValid is '1'.

                """

                STATIC = 1

                POOL = 2

                DHCP = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.dynamic._meta import _CISCO_DYNAMIC_TEMPLATE_MIB as meta
                    return meta._meta_table['CISCODYNAMICTEMPLATEMIB.CdtPppTemplateTable.CdtPppTemplateEntry.CdtPppPeerDefIpAddrSrc_Enum']


            class CdtPppAuthentication_Bits(FixedBitsDict):
                """
                CdtPppAuthentication_Bits

                This object specifies authentication services applied to a
                target PPP connection and other options affecting authentication
                services\:
                
                    'chap'
                        This option enables the Challenge Handshake Protocol (CHAP)
                        on a target PPP connection.
                
                    'msChap'
                        This option enables Microsoft's CHAP on a target PPP
                        connection.
                
                    'msChapV2'
                        This option enables version 2 of Microsoft's CHAP on a
                        target PPP connection.
                
                    'pap'
                        This option enables Password Authentication Protocol (PAP)
                        on a target PPP connection.
                
                    'eap'
                        This option enables Extensible Authentication Protocol (EAP)
                        on a target PPP connection.
                
                    'optional'
                        This option specifies that the system accepts the connection
                        even if the peer of a target PPP connection refuses to
                        accept the authentication methods the system has
                        requested.
                
                    'callin'
                        This option specifies that authentication should only happen
                        for incoming calls.
                
                    'oneTime'
                        This option specifies that the system accepts the username
                        and password in the username field of authentication
                        responses received on a target PPP connection.
                
                This column is valid only if the 'authentication' bit of the
                corresponding instance of cdtPppValid is '1'.
                Keys are:- pap , msChapV2 , callin , msChap , oneTime , chap , eap , optional

                """

                def __init__(self):
                    self._dictionary = { 
                        'pap':False,
                        'msChapV2':False,
                        'callin':False,
                        'msChap':False,
                        'oneTime':False,
                        'chap':False,
                        'eap':False,
                        'optional':False,
                    }
                    self._pos_map = { 
                        'pap':3,
                        'msChapV2':2,
                        'callin':6,
                        'msChap':1,
                        'oneTime':7,
                        'chap':0,
                        'eap':4,
                        'optional':5,
                    }

            class CdtPppChapOpts_Bits(FixedBitsDict):
                """
                CdtPppChapOpts_Bits

                This object specifies how the system processes the CHAP on a
                target PPP connection\:
                
                    'refuse'
                        This option specifies that the system should refuse CHAP
                        requests from peers of a target PPP connection.
                
                    'callin'
                        This option specifies that the system should only refuse
                        CHAP requests for incoming calls on a target PPP
                        connection.  This option is only relevant if the
                        'refuse' option is set to '1'.
                
                    'wait'
                        This option delays CHAP authentication until after the
                        peer of a target PPP connection has authenticated itself
                        to the system.
                
                    'encrypted'
                        This option specifies that the value specified by the
                        corresponding instance of cdtPppChapPassword is already
                        encrypted.
                
                This column is valid only if the 'chapOpts' bit of the
                corresponding instance of cdtPppValid is '1'.
                Keys are:- encrypted , refuse , callin , wait

                """

                def __init__(self):
                    self._dictionary = { 
                        'encrypted':False,
                        'refuse':False,
                        'callin':False,
                        'wait':False,
                    }
                    self._pos_map = { 
                        'encrypted':3,
                        'refuse':0,
                        'callin':1,
                        'wait':2,
                    }

            class CdtPppEapOpts_Bits(FixedBitsDict):
                """
                CdtPppEapOpts_Bits

                This object specifies how the system processes the EAP on a
                target PPP connection\:
                
                    'refuse'
                        This option specifies that the system should refuse EAP
                        requests from peers of a target PPP connection.
                
                    'callin'
                        This option specifies that the system should only refuse EAP
                        requests for incoming calls on a target PPP connection.
                        This option is only relevant if the 'refuse' option is
                        set to '1'.
                
                    'wait'
                        This option delays EAP authentication until after the
                        peer of a target PPP connection has authenticated itself
                        to the system.
                
                    'local'
                        This option specifies that the system should locally
                        authenticate the peer of a target PPP connection,
                        rather than acting as a proxy to an external AAA server.
                
                This column is valid only if the 'eapOpts' bit of the
                corresponding instance of cdtPppValid is '1'.
                Keys are:- refuse , callin , local , wait

                """

                def __init__(self):
                    self._dictionary = { 
                        'refuse':False,
                        'callin':False,
                        'local':False,
                        'wait':False,
                    }
                    self._pos_map = { 
                        'refuse':0,
                        'callin':1,
                        'local':3,
                        'wait':2,
                    }

            class CdtPppMsChapV1Opts_Bits(FixedBitsDict):
                """
                CdtPppMsChapV1Opts_Bits

                This object specifies how the system processes version 1 of
                Microsoft CHAP on a target PPP connection\:
                
                    'refuse'
                        This option specifies that the system should refuse
                        Microsoft CHAP (v1) requests from peers of a target PPP
                        connection.
                
                    'callin'
                        This option specifies that the system should only refuse
                        Microsoft CHAP (v1) requests for incoming calls on a
                        target PPP connection.  This option is only relevant if
                        the 'refuse' option is set to '1'.
                
                    'wait'
                        This option delays Microsoft CHAP (v1) authentication
                        until after the peer of a target PPP connection has
                        authenticated itself to the system.
                
                    'encrypted'
                        This option specifies that the value specified by the
                        corresponding instance of cdtPppMsChapV1Password is
                        already encrypted.
                
                This column is valid only if the 'msChapV1Opts' bit of the
                corresponding instance of cdtPppValid is '1'.
                Keys are:- encrypted , refuse , callin , wait

                """

                def __init__(self):
                    self._dictionary = { 
                        'encrypted':False,
                        'refuse':False,
                        'callin':False,
                        'wait':False,
                    }
                    self._pos_map = { 
                        'encrypted':3,
                        'refuse':0,
                        'callin':1,
                        'wait':2,
                    }

            class CdtPppMsChapV2Opts_Bits(FixedBitsDict):
                """
                CdtPppMsChapV2Opts_Bits

                This object specifies how the system processes version 2 of
                Microsoft CHAP on a target PPP connection\:
                
                    'refuse'
                        This option specifies that the system should refuse
                        Microsoft CHAP (v2) requests from peers of a target PPP
                        connection.
                
                    'callin'
                        This option specifies that the system should only refuse
                        Microsoft CHAP (v2) requests for incoming calls on a
                        target PPP connection.  This option is only relevant if
                        the 'refuse' option is set to '1'.
                
                    'wait'
                        This option delays Microsoft CHAP (v2) authentication
                        until after the peer of a target PPP connection has
                        authenticated itself to the system.
                
                    'encrypted'
                        This option specifies that the value specified by the
                        corresponding instance of cdtPppMsChapV2Password is
                        already encrypted.
                
                This column is valid only if the 'msChapV2Opts' bit of the
                corresponding instance of cdtPppValid is '1'.
                Keys are:- encrypted , refuse , callin , wait

                """

                def __init__(self):
                    self._dictionary = { 
                        'encrypted':False,
                        'refuse':False,
                        'callin':False,
                        'wait':False,
                    }
                    self._pos_map = { 
                        'encrypted':3,
                        'refuse':0,
                        'callin':1,
                        'wait':2,
                    }

            class CdtPppPapOpts_Bits(FixedBitsDict):
                """
                CdtPppPapOpts_Bits

                This object specifies how the system processes the PAP on a
                target PPP connection\:
                
                    'refuse'
                        This option specifies that the system should refuse PAP
                        requests from peers of a target PPP connection.
                
                    'encrypted'
                        This option specifies that the value specified by the
                        corresponding instance of cdtPppPapSentPassword is
                        already encrypted.
                
                This column is valid only if the 'papOpts' bit of the
                corresponding instance of cdtPppValid is '1'.
                Keys are:- encrypted , refuse

                """

                def __init__(self):
                    self._dictionary = { 
                        'encrypted':False,
                        'refuse':False,
                    }
                    self._pos_map = { 
                        'encrypted':1,
                        'refuse':0,
                    }

            class CdtPppPeerDefIpAddrOpts_Bits(FixedBitsDict):
                """
                CdtPppPeerDefIpAddrOpts_Bits

                This object specifies options that affect how the system
                assigns an IP address to the peer of a target PPP connection\:
                
                    'ipAddrForced'
                        This option forces the system to assign the next
                        available IP address in the pool to the peer of a
                        target PPP connection.  When disabled, the peer may
                        negotiate a specific IP address or the system can assign
                        the peer its previously assigned IP address.
                
                    'matchAaaPools'
                        This option specifies that the names of the IP address
                        pools provided by an external AAA server must appear in
                        the corresponding list of IP address pool specified by
                        the cdtPppPeerIpAddrPoolTable.
                
                    'backupPools'
                        This option specifies that the corresponding names of
                        the IP address pools specified by the
                        cditPppPeerIpAddrPoolTable serve as backup pools to
                        those provided by an external AAA server.
                
                    'staticPools'
                        This option suppresses an attempt to load pools from an
                        external AAA server when the system encounters a missing
                        pool name.
                
                This column is valid only if the 'peerIpAddrOpts' bit of the
                corresponding instance of cdtPppValid is '1'.
                Keys are:- matchAaaPools , ipAddrForced , staticPool

                """

                def __init__(self):
                    self._dictionary = { 
                        'matchAaaPools':False,
                        'ipAddrForced':False,
                        'staticPool':False,
                    }
                    self._pos_map = { 
                        'matchAaaPools':1,
                        'ipAddrForced':0,
                        'staticPool':2,
                    }

            class CdtPppValid_Bits(FixedBitsDict):
                """
                CdtPppValid_Bits

                This object specifies which attributes in the dynamic template
                have been configured to valid values.
                
                Each bit in this bit string corresponds to a column in this
                table.  If the bit is '0', then the value of the corresponding
                column is not valid.  If the bit is '1', then the value of the
                corresponding column has been configured to a valid value.
                
                The following list specifies the mappings between bits and the
                columns\:
                
                    accounting              => cdtPppAccounting
                    authentication          => cdtPppAuthentication
                    authenticationMethods   => cdtPppAuthenticationMethods
                    authorization           => cdtPppAuthorization
                    loopbackIgnore          => cdtPppLoopbackIgnore
                    maxBadAuth              => cdtPppMaxBadAuth
                    maxConfigure            => cdtPppMaxConfigure
                    maxFailure              => cdtPppMaxFailure
                    maxTerminate            => cdtPppMaxTerminate
                    timeoutAuthentication   => cdtPppTimeoutAuthentication
                    timeoutRetry            => cdtPppTimeoutRetry
                    chapOpts                => cdtPppChapOpts
                    chapHostname            => cdtPppChapHostname
                    chapPassword            => cdtPppChapPassword
                    msChapV1Opts            => cdtPppMsChapV1Opts
                    msChapV1Hostname        => cdtPppMsChapV1Hostname
                    msChapV1Password        => cdtPppMsChapV1Password
                    msChapV2Opts            => cdtPppMsChapV2Opts
                    msChapV2Hostname        => cdtPppMsChapV2Hostname
                    msChapV2Password        => cdtPppMsChapV2Password
                    papOpts                 => cdtPppPapOpts
                    papSentUsername         => cdtPppPapUsername
                    papSentPassword         => cdtPppPapPassword
                    eapOpts                 => cdtPppEapOpts
                    eapIdentity             => cdtPppEapIdentity
                    eapPassword             => cdtPppEapPassword
                    ipcpAddrOption          => cdtPppIpcpAddrOption
                    ipcpDnsOption           => cdtPppIpcpDnsOption
                    ipcpDnsPrimary          => cdtPppIpcpDnsPrimary
                    ipcpDnsSecondary        => cdtPppIpcpDnsSecondary
                    ipcpWinsOption          => cdtPppIpcpWinsOption
                    ipcpWinsPrimary         => cdtPppIpcpWinsPrimary
                    ipcpWinsSecondary       => cdtPppIpcpWinsSecondary
                    ipcpMaskOption          => cdtPppIpcpMaskOption
                    ipcpMask                => cdtPppIpcpMask
                    peerDefIpAddrOpts       => cdtPppPeerOpts
                    peerDefIpAddrSrc        => cdtPppPeerDefIpAddrSrc
                    peerDefIpAddr           => cdtPppPeerDefIpAddr
                Keys are:- chapHostname , timeoutRetry , loopbackIgnore , timeoutAuthentication , accounting , eapOpts , peerDefIpAddrOpts , msChapV1Password , ipcpWinsOption , ipcpMask , maxFailure , ipcpDnsOption , autthenticationMethods , ipcpDnsSecondary , authentication , valid , ipcpAddrOption , peerDefIpAddr , chapPassword , ipcpWinsSecondary , ipcpWinsPrimary , authorization , maxTerminate , maxConfigure , papPassword , eapPassword , papOpts , eapIdentity , msChapV2Hostname , peerDefIpAddrSrc , msChapV2Password , msChapV1Hostname , msChapV2Opts , ipcpMaskOption , ipcpDnsPrimary , msChapV1Opts , chapOpts , maxBadAuth , papUsername

                """

                def __init__(self):
                    self._dictionary = { 
                        'chapHostname':False,
                        'timeoutRetry':False,
                        'loopbackIgnore':False,
                        'timeoutAuthentication':False,
                        'accounting':False,
                        'eapOpts':False,
                        'peerDefIpAddrOpts':False,
                        'msChapV1Password':False,
                        'ipcpWinsOption':False,
                        'ipcpMask':False,
                        'maxFailure':False,
                        'ipcpDnsOption':False,
                        'autthenticationMethods':False,
                        'ipcpDnsSecondary':False,
                        'authentication':False,
                        'valid':False,
                        'ipcpAddrOption':False,
                        'peerDefIpAddr':False,
                        'chapPassword':False,
                        'ipcpWinsSecondary':False,
                        'ipcpWinsPrimary':False,
                        'authorization':False,
                        'maxTerminate':False,
                        'maxConfigure':False,
                        'papPassword':False,
                        'eapPassword':False,
                        'papOpts':False,
                        'eapIdentity':False,
                        'msChapV2Hostname':False,
                        'peerDefIpAddrSrc':False,
                        'msChapV2Password':False,
                        'msChapV1Hostname':False,
                        'msChapV2Opts':False,
                        'ipcpMaskOption':False,
                        'ipcpDnsPrimary':False,
                        'msChapV1Opts':False,
                        'chapOpts':False,
                        'maxBadAuth':False,
                        'papUsername':False,
                    }
                    self._pos_map = { 
                        'chapHostname':13,
                        'timeoutRetry':11,
                        'loopbackIgnore':5,
                        'timeoutAuthentication':10,
                        'accounting':1,
                        'eapOpts':24,
                        'peerDefIpAddrOpts':36,
                        'msChapV1Password':17,
                        'ipcpWinsOption':31,
                        'ipcpMask':35,
                        'maxFailure':8,
                        'ipcpDnsOption':28,
                        'autthenticationMethods':3,
                        'ipcpDnsSecondary':30,
                        'authentication':2,
                        'valid':0,
                        'ipcpAddrOption':27,
                        'peerDefIpAddr':38,
                        'chapPassword':14,
                        'ipcpWinsSecondary':33,
                        'ipcpWinsPrimary':32,
                        'authorization':4,
                        'maxTerminate':9,
                        'maxConfigure':7,
                        'papPassword':23,
                        'eapPassword':26,
                        'papOpts':21,
                        'eapIdentity':25,
                        'msChapV2Hostname':19,
                        'peerDefIpAddrSrc':37,
                        'msChapV2Password':20,
                        'msChapV1Hostname':16,
                        'msChapV2Opts':18,
                        'ipcpMaskOption':34,
                        'ipcpDnsPrimary':29,
                        'msChapV1Opts':15,
                        'chapOpts':12,
                        'maxBadAuth':6,
                        'papUsername':22,
                    }

            @property
            def _common_path(self):
                if self.cdttemplatename is None:
                    raise YPYDataValidationError('Key property cdttemplatename is None')

                return '/CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/CISCO-DYNAMIC-TEMPLATE-MIB:cdtPppTemplateTable/CISCO-DYNAMIC-TEMPLATE-MIB:cdtPppTemplateEntry[CISCO-DYNAMIC-TEMPLATE-MIB:cdtTemplateName = ' + str(self.cdttemplatename) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cdttemplatename is not None:
                    return True

                if self.cdtpppaccounting is not None:
                    return True

                if self.cdtpppauthentication is not None:
                    if self.cdtpppauthentication._has_data():
                        return True

                if self.cdtpppauthenticationmethods is not None:
                    return True

                if self.cdtpppauthorization is not None:
                    return True

                if self.cdtpppchaphostname is not None:
                    return True

                if self.cdtpppchapopts is not None:
                    if self.cdtpppchapopts._has_data():
                        return True

                if self.cdtpppchappassword is not None:
                    return True

                if self.cdtpppeapidentity is not None:
                    return True

                if self.cdtpppeapopts is not None:
                    if self.cdtpppeapopts._has_data():
                        return True

                if self.cdtpppeappassword is not None:
                    return True

                if self.cdtpppipcpaddroption is not None:
                    return True

                if self.cdtpppipcpdnsoption is not None:
                    return True

                if self.cdtpppipcpdnsprimary is not None:
                    return True

                if self.cdtpppipcpdnssecondary is not None:
                    return True

                if self.cdtpppipcpmask is not None:
                    return True

                if self.cdtpppipcpmaskoption is not None:
                    return True

                if self.cdtpppipcpwinsoption is not None:
                    return True

                if self.cdtpppipcpwinsprimary is not None:
                    return True

                if self.cdtpppipcpwinssecondary is not None:
                    return True

                if self.cdtppploopbackignore is not None:
                    return True

                if self.cdtpppmaxbadauth is not None:
                    return True

                if self.cdtpppmaxconfigure is not None:
                    return True

                if self.cdtpppmaxfailure is not None:
                    return True

                if self.cdtpppmaxterminate is not None:
                    return True

                if self.cdtpppmschapv1hostname is not None:
                    return True

                if self.cdtpppmschapv1opts is not None:
                    if self.cdtpppmschapv1opts._has_data():
                        return True

                if self.cdtpppmschapv1password is not None:
                    return True

                if self.cdtpppmschapv2hostname is not None:
                    return True

                if self.cdtpppmschapv2opts is not None:
                    if self.cdtpppmschapv2opts._has_data():
                        return True

                if self.cdtpppmschapv2password is not None:
                    return True

                if self.cdtppppapopts is not None:
                    if self.cdtppppapopts._has_data():
                        return True

                if self.cdtppppappassword is not None:
                    return True

                if self.cdtppppapusername is not None:
                    return True

                if self.cdtppppeerdefipaddr is not None:
                    return True

                if self.cdtppppeerdefipaddropts is not None:
                    if self.cdtppppeerdefipaddropts._has_data():
                        return True

                if self.cdtppppeerdefipaddrsrc is not None:
                    return True

                if self.cdtppptimeoutauthentication is not None:
                    return True

                if self.cdtppptimeoutretry is not None:
                    return True

                if self.cdtpppvalid is not None:
                    if self.cdtpppvalid._has_data():
                        return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.dynamic._meta import _CISCO_DYNAMIC_TEMPLATE_MIB as meta
                return meta._meta_table['CISCODYNAMICTEMPLATEMIB.CdtPppTemplateTable.CdtPppTemplateEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/CISCO-DYNAMIC-TEMPLATE-MIB:cdtPppTemplateTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cdtppptemplateentry is not None:
                for child_ref in self.cdtppptemplateentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.dynamic._meta import _CISCO_DYNAMIC_TEMPLATE_MIB as meta
            return meta._meta_table['CISCODYNAMICTEMPLATEMIB.CdtPppTemplateTable']['meta_info']


    class CdtSrvTemplateTable(object):
        """
        This table contains attributes relating to a service.
        
        This table has a sparse\-dependent relationship on the
        cdtTemplateTable, containing a row for each dynamic template
        having a cdtTemplateType of one of the following values\:
        
            'derived'
            'service'
        
        .. attribute:: cdtsrvtemplateentry
        
        	An entry containing attributes relating to a service.  The system automatically creates entry when the system or the EMS/NMS creates a row in the cdtTemplateTable with a cdtTemplateType of one of the following values\:      'derived'     'service'  Likewise, the system automatically destroys an entry when the system or the EMS/NMS destroys the corresponding row in the cdtTemplateTable
        	**type**\: list of :py:class:`CdtSrvTemplateEntry <ydk.models.dynamic.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtSrvTemplateTable.CdtSrvTemplateEntry>`
        
        

        """

        _prefix = 'cisco-dynamic-template'
        _revision = '2007-09-06'

        def __init__(self):
            self.parent = None
            self.cdtsrvtemplateentry = YList()
            self.cdtsrvtemplateentry.parent = self
            self.cdtsrvtemplateentry.name = 'cdtsrvtemplateentry'


        class CdtSrvTemplateEntry(object):
            """
            An entry containing attributes relating to a service.
            
            The system automatically creates entry when the system or the
            EMS/NMS creates a row in the cdtTemplateTable with a
            cdtTemplateType of one of the following values\:
            
                'derived'
                'service'
            
            Likewise, the system automatically destroys an entry when the
            system or the EMS/NMS destroys the corresponding row in the
            cdtTemplateTable.
            
            .. attribute:: cdttemplatename
            
            	
            	**type**\: str
            
            	**range:** 1..64
            
            .. attribute:: cdtsrvmulticast
            
            	This objects specifies whether the system enables multicast service for subscriber sessions of the target service.  This column is valid only if the 'sgSrvMcastRoutingIf' bit of the corresponding instance of cdtSrvValid is '1'
            	**type**\: bool
            
            .. attribute:: cdtsrvnetworksrv
            
            	This object specifies the type of network service provided by the target service\:      'other'         The implementation of this MIB module does not recognize         the configured network service.      'none'         The target subscriber service does not provide a network         service to subscribers sessions.      'local'         The target subscriber service provides local termination         for subscriber sessions.      'vpdn'         The target subscriber service provides a Virtual Private         Dialup Network service for subscriber sessions.  This column is valid only if the 'networkSrv' bit of the corresponding instance of cdtSrvValid is '1'
            	**type**\: :py:class:`CdtSrvNetworkSrv_Enum <ydk.models.dynamic.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtSrvTemplateTable.CdtSrvTemplateEntry.CdtSrvNetworkSrv_Enum>`
            
            .. attribute:: cdtsrvsgsrvgroup
            
            	This object specifies the name of the service group with which the system associates subscriber sessions.  A service group specifies a set of services that may be active simultaneously for a given subscriber session.  Typically, a service group contains a primary service and one or more secondary services.  This column is valid only if the 'sgSrvGroup' bit of the corresponding instance of cdtSrvValid is '1'
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cdtsrvsgsrvtype
            
            	This object specifies whether the target service specifies a network\-forwarding policy\:      'primary'         The target service specifies a network\-forwarding         policy.  Primary services are mutually exclusive; that         is, only one primary service can be activated for any         given subscriber session.      'secondary'         The target service has a dependence on the primary         service in the group specified by the corresponding         instance of cdtSuBSrvSgSrvGroup.  After the system         activates the primary service, it activates secondary         services.  When the system deactivates the primary         service, then it deactivates all the secondary services         in the service group.  This column is valid only if the 'sgSrvType' bit of the corresponding instance of cdtSrvValid is '1'
            	**type**\: :py:class:`CdtSrvSgSrvType_Enum <ydk.models.dynamic.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtSrvTemplateTable.CdtSrvTemplateEntry.CdtSrvSgSrvType_Enum>`
            
            .. attribute:: cdtsrvvalid
            
            	This object specifies which attributes in the dynamic template have been configured to valid values.  Each bit in this bit string corresponds to a column in this table.  If the bit is '0', then the value of the corresponding column is not valid.  If the bit is '1', then the value of the corresponding column has been configured to a valid value.  The following list specifies the mappings between bits and the columns\:      networkSrv     => cdtSrvNetworkSrv     vpdnGroup      => cdtSrvVpdnGroup     sgSrvGroup     => cdtSrvGroup     sgSrvType      => cdtSrvSgSrvType     multicast      => cdtSrvMulticast
            	**type**\: :py:class:`CdtSrvValid_Bits <ydk.models.dynamic.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtSrvTemplateTable.CdtSrvTemplateEntry.CdtSrvValid_Bits>`
            
            .. attribute:: cdtsrvvpdngroup
            
            	This object specifies the name of the VPDN group used to configure the network service.  This column is valid only if the 'vpdnGroup' bit of the corresponding instance of cdtSrvValid is '1'
            	**type**\: str
            
            	**range:** 0..255
            
            

            """

            _prefix = 'cisco-dynamic-template'
            _revision = '2007-09-06'

            def __init__(self):
                self.parent = None
                self.cdttemplatename = None
                self.cdtsrvmulticast = None
                self.cdtsrvnetworksrv = None
                self.cdtsrvsgsrvgroup = None
                self.cdtsrvsgsrvtype = None
                self.cdtsrvvalid = CISCODYNAMICTEMPLATEMIB.CdtSrvTemplateTable.CdtSrvTemplateEntry.CdtSrvValid_Bits()
                self.cdtsrvvpdngroup = None

            class CdtSrvNetworkSrv_Enum(Enum):
                """
                CdtSrvNetworkSrv_Enum

                This object specifies the type of network service provided by
                the target service\:
                
                    'other'
                        The implementation of this MIB module does not recognize
                        the configured network service.
                
                    'none'
                        The target subscriber service does not provide a network
                        service to subscribers sessions.
                
                    'local'
                        The target subscriber service provides local termination
                        for subscriber sessions.
                
                    'vpdn'
                        The target subscriber service provides a Virtual Private
                        Dialup Network service for subscriber sessions.
                
                This column is valid only if the 'networkSrv' bit of the
                corresponding instance of cdtSrvValid is '1'.

                """

                OTHER = 1

                NONE = 2

                LOCAL = 3

                VPDN = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.dynamic._meta import _CISCO_DYNAMIC_TEMPLATE_MIB as meta
                    return meta._meta_table['CISCODYNAMICTEMPLATEMIB.CdtSrvTemplateTable.CdtSrvTemplateEntry.CdtSrvNetworkSrv_Enum']


            class CdtSrvSgSrvType_Enum(Enum):
                """
                CdtSrvSgSrvType_Enum

                This object specifies whether the target service specifies a
                network\-forwarding policy\:
                
                    'primary'
                        The target service specifies a network\-forwarding
                        policy.  Primary services are mutually exclusive; that
                        is, only one primary service can be activated for any
                        given subscriber session.
                
                    'secondary'
                        The target service has a dependence on the primary
                        service in the group specified by the corresponding
                        instance of cdtSuBSrvSgSrvGroup.  After the system
                        activates the primary service, it activates secondary
                        services.  When the system deactivates the primary
                        service, then it deactivates all the secondary services
                        in the service group.
                
                This column is valid only if the 'sgSrvType' bit of the
                corresponding instance of cdtSrvValid is '1'.

                """

                PRIMARY = 1

                SECONDARY = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.dynamic._meta import _CISCO_DYNAMIC_TEMPLATE_MIB as meta
                    return meta._meta_table['CISCODYNAMICTEMPLATEMIB.CdtSrvTemplateTable.CdtSrvTemplateEntry.CdtSrvSgSrvType_Enum']


            class CdtSrvValid_Bits(FixedBitsDict):
                """
                CdtSrvValid_Bits

                This object specifies which attributes in the dynamic template
                have been configured to valid values.
                
                Each bit in this bit string corresponds to a column in this
                table.  If the bit is '0', then the value of the corresponding
                column is not valid.  If the bit is '1', then the value of the
                corresponding column has been configured to a valid value.
                
                The following list specifies the mappings between bits and the
                columns\:
                
                    networkSrv     => cdtSrvNetworkSrv
                    vpdnGroup      => cdtSrvVpdnGroup
                    sgSrvGroup     => cdtSrvGroup
                    sgSrvType      => cdtSrvSgSrvType
                    multicast      => cdtSrvMulticast
                Keys are:- vpdnGroup , sgSrvGroup , networkSrv , sgSrvType , multicast

                """

                def __init__(self):
                    self._dictionary = { 
                        'vpdnGroup':False,
                        'sgSrvGroup':False,
                        'networkSrv':False,
                        'sgSrvType':False,
                        'multicast':False,
                    }
                    self._pos_map = { 
                        'vpdnGroup':1,
                        'sgSrvGroup':2,
                        'networkSrv':0,
                        'sgSrvType':3,
                        'multicast':4,
                    }

            @property
            def _common_path(self):
                if self.cdttemplatename is None:
                    raise YPYDataValidationError('Key property cdttemplatename is None')

                return '/CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/CISCO-DYNAMIC-TEMPLATE-MIB:cdtSrvTemplateTable/CISCO-DYNAMIC-TEMPLATE-MIB:cdtSrvTemplateEntry[CISCO-DYNAMIC-TEMPLATE-MIB:cdtTemplateName = ' + str(self.cdttemplatename) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cdttemplatename is not None:
                    return True

                if self.cdtsrvmulticast is not None:
                    return True

                if self.cdtsrvnetworksrv is not None:
                    return True

                if self.cdtsrvsgsrvgroup is not None:
                    return True

                if self.cdtsrvsgsrvtype is not None:
                    return True

                if self.cdtsrvvalid is not None:
                    if self.cdtsrvvalid._has_data():
                        return True

                if self.cdtsrvvpdngroup is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.dynamic._meta import _CISCO_DYNAMIC_TEMPLATE_MIB as meta
                return meta._meta_table['CISCODYNAMICTEMPLATEMIB.CdtSrvTemplateTable.CdtSrvTemplateEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/CISCO-DYNAMIC-TEMPLATE-MIB:cdtSrvTemplateTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cdtsrvtemplateentry is not None:
                for child_ref in self.cdtsrvtemplateentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.dynamic._meta import _CISCO_DYNAMIC_TEMPLATE_MIB as meta
            return meta._meta_table['CISCODYNAMICTEMPLATEMIB.CdtSrvTemplateTable']['meta_info']


    class CdtTemplateAssociationTable(object):
        """
        This table contains a list of templates associated with each
        target.
        
        This table has an expansion dependent relationship on the
        cdtTemplateTargetTable, containing zero or more rows for each
        target.
        
        .. attribute:: cdttemplateassociationentry
        
        	An entry indicates an association of a dynamic template with a target.  The system automatically creates an entry when it associates a dynamic template to a target.  The system also creates an entry when it derives the configuration that it applies to a target.  The system automatically destroys an entry under the following circumstances\:  1)  The target indicated by the entry no longer exists.  2)  The association between the target and the dynamic template     no longer exists
        	**type**\: list of :py:class:`CdtTemplateAssociationEntry <ydk.models.dynamic.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtTemplateAssociationTable.CdtTemplateAssociationEntry>`
        
        

        """

        _prefix = 'cisco-dynamic-template'
        _revision = '2007-09-06'

        def __init__(self):
            self.parent = None
            self.cdttemplateassociationentry = YList()
            self.cdttemplateassociationentry.parent = self
            self.cdttemplateassociationentry.name = 'cdttemplateassociationentry'


        class CdtTemplateAssociationEntry(object):
            """
            An entry indicates an association of a dynamic template with a
            target.
            
            The system automatically creates an entry when it associates a
            dynamic template to a target.
            
            The system also creates an entry when it derives the
            configuration that it applies to a target.
            
            The system automatically destroys an entry under the following
            circumstances\:
            
            1)  The target indicated by the entry no longer exists.
            
            2)  The association between the target and the dynamic template
                no longer exists.
            
            .. attribute:: cdttemplateassociationname
            
            	This object indicates the name of the template associated with the target
            	**type**\: str
            
            	**range:** 1..64
            
            .. attribute:: cdttemplatetargetid
            
            	
            	**type**\: str
            
            	**range:** 1..20
            
            .. attribute:: cdttemplatetargettype
            
            	
            	**type**\: :py:class:`DynamicTemplateTargetType_Enum <ydk.models.dynamic.CISCO_DYNAMIC_TEMPLATE_TC_MIB.DynamicTemplateTargetType_Enum>`
            
            .. attribute:: cdttemplateassociationprecedence
            
            	This object indicates the relative precedence of the associated dynamic template.  Lower values have higher precedence than higher values
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-dynamic-template'
            _revision = '2007-09-06'

            def __init__(self):
                self.parent = None
                self.cdttemplateassociationname = None
                self.cdttemplatetargetid = None
                self.cdttemplatetargettype = None
                self.cdttemplateassociationprecedence = None

            @property
            def _common_path(self):
                if self.cdttemplateassociationname is None:
                    raise YPYDataValidationError('Key property cdttemplateassociationname is None')
                if self.cdttemplatetargetid is None:
                    raise YPYDataValidationError('Key property cdttemplatetargetid is None')
                if self.cdttemplatetargettype is None:
                    raise YPYDataValidationError('Key property cdttemplatetargettype is None')

                return '/CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/CISCO-DYNAMIC-TEMPLATE-MIB:cdtTemplateAssociationTable/CISCO-DYNAMIC-TEMPLATE-MIB:cdtTemplateAssociationEntry[CISCO-DYNAMIC-TEMPLATE-MIB:cdtTemplateAssociationName = ' + str(self.cdttemplateassociationname) + '][CISCO-DYNAMIC-TEMPLATE-MIB:cdtTemplateTargetId = ' + str(self.cdttemplatetargetid) + '][CISCO-DYNAMIC-TEMPLATE-MIB:cdtTemplateTargetType = ' + str(self.cdttemplatetargettype) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cdttemplateassociationname is not None:
                    return True

                if self.cdttemplatetargetid is not None:
                    return True

                if self.cdttemplatetargettype is not None:
                    return True

                if self.cdttemplateassociationprecedence is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.dynamic._meta import _CISCO_DYNAMIC_TEMPLATE_MIB as meta
                return meta._meta_table['CISCODYNAMICTEMPLATEMIB.CdtTemplateAssociationTable.CdtTemplateAssociationEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/CISCO-DYNAMIC-TEMPLATE-MIB:cdtTemplateAssociationTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cdttemplateassociationentry is not None:
                for child_ref in self.cdttemplateassociationentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.dynamic._meta import _CISCO_DYNAMIC_TEMPLATE_MIB as meta
            return meta._meta_table['CISCODYNAMICTEMPLATEMIB.CdtTemplateAssociationTable']['meta_info']


    class CdtTemplateCommonTable(object):
        """
        This table contains attributes relating to all dynamic
        templates.  Observe that the type of dynamic templates
        containing these attributes may change with the addition of new
        dynamic template types.
        
        This table has a sparse\-dependent relationship on the
        cdtTemplateTable, containing a row for each dynamic template
        having a cdtTemplateType of one of the following values\:
        
            'derived'
            'ppp'
            'ethernet'
            'ipSubscriber'
            'service'
        
        .. attribute:: cdttemplatecommonentry
        
        	An entry containing attributes relating to any target.  The system automatically creates an entry when the system or the EMS/NMS creates a row in the cdtTemplateTable with a cdtTemplateType of on the following values\:      'derived'     'ppp'     'ethernet'     'ipSubscriber'     'service'  Likewise, the system automatically destroys an entry when the system or the EMS/NMS destroys the corresponding row in the cdtTemplateTable
        	**type**\: list of :py:class:`CdtTemplateCommonEntry <ydk.models.dynamic.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtTemplateCommonTable.CdtTemplateCommonEntry>`
        
        

        """

        _prefix = 'cisco-dynamic-template'
        _revision = '2007-09-06'

        def __init__(self):
            self.parent = None
            self.cdttemplatecommonentry = YList()
            self.cdttemplatecommonentry.parent = self
            self.cdttemplatecommonentry.name = 'cdttemplatecommonentry'


        class CdtTemplateCommonEntry(object):
            """
            An entry containing attributes relating to any target.
            
            The system automatically creates an entry when the system or the
            EMS/NMS creates a row in the cdtTemplateTable with a
            cdtTemplateType of on the following values\:
            
                'derived'
                'ppp'
                'ethernet'
                'ipSubscriber'
                'service'
            
            Likewise, the system automatically destroys an entry when the
            system or the EMS/NMS destroys the corresponding row in the
            cdtTemplateTable.
            
            .. attribute:: cdttemplatename
            
            	
            	**type**\: str
            
            	**range:** 1..64
            
            .. attribute:: cdtcommonaddrpool
            
            	This object specifies the name of the IP address pool the system will use to assign an IP address to a peer of a target.  This column is valid only if the 'addrPool' bit of the corresponding instance of cdtCommonValid is '1'
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cdtcommondescr
            
            	This object specifies a human\-readable description for the dynamic template.  This column is valid only if the 'descr' bit of the corresponding instance of cdtCommonValid is '1'
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cdtcommonipv4accessgroup
            
            	This object specifies the name (or number) of the IPv4 ACL applied to a target.  This column is valid only if the 'ipv4AccessGroup' bit of the corresponding instance of cdtCommonValid is '1'
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cdtcommonipv4unreachables
            
            	This object specifies whether a target generates ICMPv4 unreachable messages.  This column is valid only if the 'ipv4Unreachables' bit of the corresponding instance of cdtCommonValid is '1'
            	**type**\: bool
            
            .. attribute:: cdtcommonipv6accessgroup
            
            	This object specifies the name (or number) of the IPv4 ACL applied to a target.  This column is valid only if the 'ipv6AccessGroup' bit of the corresponding instance of cdtCommonValid is '1'
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cdtcommonipv6unreachables
            
            	This object specifies whether a target generates ICMPv6 unreachable messages.  This column is valid only if the 'ipv6Unreachables' bit of the corresponding instance of cdtCommonValid is '1'
            	**type**\: bool
            
            .. attribute:: cdtcommonkeepaliveint
            
            	This object specifies the interval that the system sends keepalive messages to a target.  This column is valid only if the 'keepaliveInterval' bit of the corresponding instance of cdtCommonValid is '1'
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: cdtcommonkeepaliveretries
            
            	This object specifies the number of times the system will resend a keepalive message without a response before it transitions a target to an operationally down state.  This column is valid only if the 'keepaliveRetries' bit of the corresponding instance of cdtCommonValid is '1'
            	**type**\: int
            
            	**range:** 1..255
            
            .. attribute:: cdtcommonsrvacct
            
            	This object specifies the name of the traffic accounting policy applied to a target.  The system should assume that the cbpPolicyMapType (defined by the CISCO\-CBP\-BASE\-CFG\-MIB) of the policy is cbpPmtTrafficAccounting (defined by the CISCO\-CBP\-TYPE\-OID\-MIB).  This column is valid only if the 'srvAcct' bit of the corresponding instance of cdtCommonValid is '1'
            	**type**\: str
            
            .. attribute:: cdtcommonsrvnetflow
            
            	This object specifies the name of the NetFlow policy applied to a target.  The system should assume that the cbpPolicyMapType (defined by the CISCO\-CBP\-BASE\-CFG\-MIB) of the policy is cbpPmtNetflow (defined by the CISCO\-CBP\-TYPE\-OID\-MIB).  This column is valid only if the 'srvNetflow' bit of the corresponding instance of cdtCommonValid is '1'
            	**type**\: str
            
            .. attribute:: cdtcommonsrvqos
            
            	This object specifies the name of the traffic QoS policy applied to a target.  The system should assume that the cbpPolicyMapType (defined by the CISCO\-CBP\-BASE\-CFG\-MIB) of the policy is cbpPmtQos (defined by the CISCO\-CBP\-TYPE\-OID\-MIB).  This column is valid only if the 'srvQos' bit of the corresponding instance of cdtCommonValid is '1'
            	**type**\: str
            
            .. attribute:: cdtcommonsrvredirect
            
            	This object specifies the name of the traffic redirect policy applied to a target.  The system should assume that the cbpPolicyMapType (defined by the CISCO\-CBP\-BASE\-CFG\-MIB) of the policy is cbpPmtTrafficRedirect (defined by the CISCO\-CBP\-TYPE\-OID\-MIB).  This column is valid only if the 'srvRedirect' bit of the corresponding instance of cdtCommonValid is '1'
            	**type**\: str
            
            .. attribute:: cdtcommonsrvsubcontrol
            
            	This object specifies the name of the subscriber control policy applied to a target.  The system should assume that the cbpPolicyMapType (defined by the CISCO\-CBP\-BASE\-CFG\-MIB) of the policy is cbpPmtControlSubscriber (defined by the CISCO\-CBP\-TYPE\-OID\-MIB).  This column is valid only if the 'srvSubControl' bit of the corresponding instance of cdtCommonValid is '1'
            	**type**\: str
            
            .. attribute:: cdtcommonvalid
            
            	This object specifies which attributes in the dynamic template have been configured to valid values.  Each bit in this bit string corresponds to a column in this table.  If the bit is '0', then the value of the corresponding column is not valid.  If the bit is '1', then the value of the corresponding column has been configured to a valid value.  The following list specifies the mappings between bits and the columns\:      'descr'             => cdtCommonDescr     'keepaliveInt'      => cdtCommonKeepaliveInt     'keepaliveRetries'  => cdtCommonKeepaliveRetries     'vrf'               => cdtCommonVrf     'addrPool'          => cdtCommonAddrPool     'ipv4AccessGroup'   => cdtCommonIpv4AccessGroup     'ipv4Unreachables'  => cdtCommonIpv4Unreachables     'ipv6AccessGroup'   => cdtCommonIpv6AccessGroup     'ipv6Unreachables'  => cdtCommonIpv6Unreachables     'srvSubControl'     => cdtCommonSrvSubControl     'srvRedirect'       => cdtCommonSrvRedirect     'srvAcct'           => cdtCommonSrvAcct     'srvQos'            => cdtCommonSrvQos     'srvNetflow'        => cdtCommonSrvNetflow
            	**type**\: :py:class:`CdtCommonValid_Bits <ydk.models.dynamic.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtTemplateCommonTable.CdtTemplateCommonEntry.CdtCommonValid_Bits>`
            
            .. attribute:: cdtcommonvrf
            
            	This object specifies the name of the VRF with which a target has an association.  This column is valid only if the 'vrf' bit of the corresponding instance of cdtCommonValid is '1'
            	**type**\: str
            
            	**range:** 0..32
            
            

            """

            _prefix = 'cisco-dynamic-template'
            _revision = '2007-09-06'

            def __init__(self):
                self.parent = None
                self.cdttemplatename = None
                self.cdtcommonaddrpool = None
                self.cdtcommondescr = None
                self.cdtcommonipv4accessgroup = None
                self.cdtcommonipv4unreachables = None
                self.cdtcommonipv6accessgroup = None
                self.cdtcommonipv6unreachables = None
                self.cdtcommonkeepaliveint = None
                self.cdtcommonkeepaliveretries = None
                self.cdtcommonsrvacct = None
                self.cdtcommonsrvnetflow = None
                self.cdtcommonsrvqos = None
                self.cdtcommonsrvredirect = None
                self.cdtcommonsrvsubcontrol = None
                self.cdtcommonvalid = CISCODYNAMICTEMPLATEMIB.CdtTemplateCommonTable.CdtTemplateCommonEntry.CdtCommonValid_Bits()
                self.cdtcommonvrf = None

            class CdtCommonValid_Bits(FixedBitsDict):
                """
                CdtCommonValid_Bits

                This object specifies which attributes in the dynamic template
                have been configured to valid values.
                
                Each bit in this bit string corresponds to a column in this
                table.  If the bit is '0', then the value of the corresponding
                column is not valid.  If the bit is '1', then the value of the
                corresponding column has been configured to a valid value.
                
                The following list specifies the mappings between bits and the
                columns\:
                
                    'descr'             => cdtCommonDescr
                    'keepaliveInt'      => cdtCommonKeepaliveInt
                    'keepaliveRetries'  => cdtCommonKeepaliveRetries
                    'vrf'               => cdtCommonVrf
                    'addrPool'          => cdtCommonAddrPool
                    'ipv4AccessGroup'   => cdtCommonIpv4AccessGroup
                    'ipv4Unreachables'  => cdtCommonIpv4Unreachables
                    'ipv6AccessGroup'   => cdtCommonIpv6AccessGroup
                    'ipv6Unreachables'  => cdtCommonIpv6Unreachables
                    'srvSubControl'     => cdtCommonSrvSubControl
                    'srvRedirect'       => cdtCommonSrvRedirect
                    'srvAcct'           => cdtCommonSrvAcct
                    'srvQos'            => cdtCommonSrvQos
                    'srvNetflow'        => cdtCommonSrvNetflow
                Keys are:- ipv6AccessGroup , srvRedirect , addrPool , descr , ipv4Unreachables , srvNetflow , srvQos , ipv4AccessGroup , vrf , ipv6Unreachables , srvSubControl , srvAcct , keepalive

                """

                def __init__(self):
                    self._dictionary = { 
                        'ipv6AccessGroup':False,
                        'srvRedirect':False,
                        'addrPool':False,
                        'descr':False,
                        'ipv4Unreachables':False,
                        'srvNetflow':False,
                        'srvQos':False,
                        'ipv4AccessGroup':False,
                        'vrf':False,
                        'ipv6Unreachables':False,
                        'srvSubControl':False,
                        'srvAcct':False,
                        'keepalive':False,
                    }
                    self._pos_map = { 
                        'ipv6AccessGroup':6,
                        'srvRedirect':9,
                        'addrPool':3,
                        'descr':0,
                        'ipv4Unreachables':5,
                        'srvNetflow':12,
                        'srvQos':11,
                        'ipv4AccessGroup':4,
                        'vrf':2,
                        'ipv6Unreachables':7,
                        'srvSubControl':8,
                        'srvAcct':10,
                        'keepalive':1,
                    }

            @property
            def _common_path(self):
                if self.cdttemplatename is None:
                    raise YPYDataValidationError('Key property cdttemplatename is None')

                return '/CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/CISCO-DYNAMIC-TEMPLATE-MIB:cdtTemplateCommonTable/CISCO-DYNAMIC-TEMPLATE-MIB:cdtTemplateCommonEntry[CISCO-DYNAMIC-TEMPLATE-MIB:cdtTemplateName = ' + str(self.cdttemplatename) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cdttemplatename is not None:
                    return True

                if self.cdtcommonaddrpool is not None:
                    return True

                if self.cdtcommondescr is not None:
                    return True

                if self.cdtcommonipv4accessgroup is not None:
                    return True

                if self.cdtcommonipv4unreachables is not None:
                    return True

                if self.cdtcommonipv6accessgroup is not None:
                    return True

                if self.cdtcommonipv6unreachables is not None:
                    return True

                if self.cdtcommonkeepaliveint is not None:
                    return True

                if self.cdtcommonkeepaliveretries is not None:
                    return True

                if self.cdtcommonsrvacct is not None:
                    return True

                if self.cdtcommonsrvnetflow is not None:
                    return True

                if self.cdtcommonsrvqos is not None:
                    return True

                if self.cdtcommonsrvredirect is not None:
                    return True

                if self.cdtcommonsrvsubcontrol is not None:
                    return True

                if self.cdtcommonvalid is not None:
                    if self.cdtcommonvalid._has_data():
                        return True

                if self.cdtcommonvrf is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.dynamic._meta import _CISCO_DYNAMIC_TEMPLATE_MIB as meta
                return meta._meta_table['CISCODYNAMICTEMPLATEMIB.CdtTemplateCommonTable.CdtTemplateCommonEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/CISCO-DYNAMIC-TEMPLATE-MIB:cdtTemplateCommonTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cdttemplatecommonentry is not None:
                for child_ref in self.cdttemplatecommonentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.dynamic._meta import _CISCO_DYNAMIC_TEMPLATE_MIB as meta
            return meta._meta_table['CISCODYNAMICTEMPLATEMIB.CdtTemplateCommonTable']['meta_info']


    class CdtTemplateTable(object):
        """
        This table lists the dynamic templates maintained by the
        system, including those that have been locally\-configured on the
        system and those pushed to the system by external policy
        servers.
        
        .. attribute:: cdttemplateentry
        
        	An entry describes a dynamic template, which serves as a container for configuration attributes.  The configuration attributes contained by a dynamic template depends on its type.  The system automatically creates a corresponding entry when a dynamic template has been created through another management entity (e.g., the system's local console).  Likewise, the system automatically destroys a corresponding entry when a dynamic template has been destroyed through another management entity.  The system automatically creates a corresponding entry when an external policy server pushes a user profile or a service profile to the system.  The system automatically creates a corresponding entry when it generates a derived configuration
        	**type**\: list of :py:class:`CdtTemplateEntry <ydk.models.dynamic.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtTemplateTable.CdtTemplateEntry>`
        
        

        """

        _prefix = 'cisco-dynamic-template'
        _revision = '2007-09-06'

        def __init__(self):
            self.parent = None
            self.cdttemplateentry = YList()
            self.cdttemplateentry.parent = self
            self.cdttemplateentry.name = 'cdttemplateentry'


        class CdtTemplateEntry(object):
            """
            An entry describes a dynamic template, which serves as a
            container for configuration attributes.  The configuration
            attributes contained by a dynamic template depends on its type.
            
            The system automatically creates a corresponding entry when a
            dynamic template has been created through another management
            entity (e.g., the system's local console).  Likewise, the system
            automatically destroys a corresponding entry when a dynamic
            template has been destroyed through another management entity.
            
            The system automatically creates a corresponding entry when an
            external policy server pushes a user profile or a service
            profile to the system.
            
            The system automatically creates a corresponding entry when it
            generates a derived configuration.
            
            .. attribute:: cdttemplatename
            
            	This object indicates a string\-value that uniquely identifies the dynamic template.  If the corresponding instance of cdtTemplateSrc is not 'local', then the system automatically generates the name identifying the dynamic template
            	**type**\: str
            
            	**range:** 1..64
            
            .. attribute:: cdttemplatesrc
            
            	This object specifies the source of the dynamic template\:  'other'     The implementation of the MIB module does not recognize the     source of the dynamic template.  'derived'     The system created the set of attributes from one or     more dynamic templates.  'local'     The dynamic template was locally configured through a     management entity, such as the local console or a SNMP     entity.  'aaaUserProfile'     The dynamic template originated from a user profile     pushed from an external policy server.  'aaaServiceProfile'     The dynamic template originated from a service profile     pushed from an external policy server
            	**type**\: :py:class:`CdtTemplateSrc_Enum <ydk.models.dynamic.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtTemplateTable.CdtTemplateEntry.CdtTemplateSrc_Enum>`
            
            .. attribute:: cdttemplatestatus
            
            	This object specifies the status of the dynamic template.  The following columns must be valid before activating a dynamic template\:      \- cdtTemplateStorage     \- cdtTemplateType  However, these objects specify a default value.  Thus, it is possible to use create\-and\-go semantics without setting any additional columns.  An implementation must allow the EMS/NMS to modify any column when this column is 'active', including columns defined in tables that have a one\-to\-one or sparse dependent relationship on this table
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: cdttemplatestorage
            
            	This object specifies what happens to the dynamic template upon restart.  If the corresponding instance of cdtTemplateSrc is not 'local', then this column must be 'volatile'
            	**type**\: :py:class:`StorageType_Enum <ydk.models.snmpv2.SNMPv2_TC.StorageType_Enum>`
            
            .. attribute:: cdttemplatetype
            
            	This object indicates the types of dynamic template
            	**type**\: :py:class:`DynamicTemplateType_Enum <ydk.models.dynamic.CISCO_DYNAMIC_TEMPLATE_TC_MIB.DynamicTemplateType_Enum>`
            
            .. attribute:: cdttemplateusagecount
            
            	This object specifies the number of targets using a dynamic template
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-dynamic-template'
            _revision = '2007-09-06'

            def __init__(self):
                self.parent = None
                self.cdttemplatename = None
                self.cdttemplatesrc = None
                self.cdttemplatestatus = None
                self.cdttemplatestorage = None
                self.cdttemplatetype = None
                self.cdttemplateusagecount = None

            class CdtTemplateSrc_Enum(Enum):
                """
                CdtTemplateSrc_Enum

                This object specifies the source of the dynamic template\:
                
                'other'
                    The implementation of the MIB module does not recognize the
                    source of the dynamic template.
                
                'derived'
                    The system created the set of attributes from one or
                    more dynamic templates.
                
                'local'
                    The dynamic template was locally configured through a
                    management entity, such as the local console or a SNMP
                    entity.
                
                'aaaUserProfile'
                    The dynamic template originated from a user profile
                    pushed from an external policy server.
                
                'aaaServiceProfile'
                    The dynamic template originated from a service profile
                    pushed from an external policy server.

                """

                OTHER = 1

                DERIVED = 2

                LOCAL = 3

                AAAUSERPROFILE = 4

                AAASERVICEPROFILE = 5


                @staticmethod
                def _meta_info():
                    from ydk.models.dynamic._meta import _CISCO_DYNAMIC_TEMPLATE_MIB as meta
                    return meta._meta_table['CISCODYNAMICTEMPLATEMIB.CdtTemplateTable.CdtTemplateEntry.CdtTemplateSrc_Enum']


            @property
            def _common_path(self):
                if self.cdttemplatename is None:
                    raise YPYDataValidationError('Key property cdttemplatename is None')

                return '/CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/CISCO-DYNAMIC-TEMPLATE-MIB:cdtTemplateTable/CISCO-DYNAMIC-TEMPLATE-MIB:cdtTemplateEntry[CISCO-DYNAMIC-TEMPLATE-MIB:cdtTemplateName = ' + str(self.cdttemplatename) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cdttemplatename is not None:
                    return True

                if self.cdttemplatesrc is not None:
                    return True

                if self.cdttemplatestatus is not None:
                    return True

                if self.cdttemplatestorage is not None:
                    return True

                if self.cdttemplatetype is not None:
                    return True

                if self.cdttemplateusagecount is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.dynamic._meta import _CISCO_DYNAMIC_TEMPLATE_MIB as meta
                return meta._meta_table['CISCODYNAMICTEMPLATEMIB.CdtTemplateTable.CdtTemplateEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/CISCO-DYNAMIC-TEMPLATE-MIB:cdtTemplateTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cdttemplateentry is not None:
                for child_ref in self.cdttemplateentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.dynamic._meta import _CISCO_DYNAMIC_TEMPLATE_MIB as meta
            return meta._meta_table['CISCODYNAMICTEMPLATEMIB.CdtTemplateTable']['meta_info']


    class CdtTemplateTargetTable(object):
        """
        This table contains a list of targets associated with
        one or more dynamic templates.
        
        .. attribute:: cdttemplatetargetentry
        
        	An entry describes a target associated with one or more dynamic templates.  The system automatically creates an entry when it associates a dynamic template to a target.  Likewise, the system automatically destroys an entry when a target no longer has any associated dynamic templates
        	**type**\: list of :py:class:`CdtTemplateTargetEntry <ydk.models.dynamic.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtTemplateTargetTable.CdtTemplateTargetEntry>`
        
        

        """

        _prefix = 'cisco-dynamic-template'
        _revision = '2007-09-06'

        def __init__(self):
            self.parent = None
            self.cdttemplatetargetentry = YList()
            self.cdttemplatetargetentry.parent = self
            self.cdttemplatetargetentry.name = 'cdttemplatetargetentry'


        class CdtTemplateTargetEntry(object):
            """
            An entry describes a target associated with one or more
            dynamic templates.
            
            The system automatically creates an entry when it associates a
            dynamic template to a target.  Likewise, the system
            automatically destroys an entry when a target no longer has any
            associated dynamic templates.
            
            .. attribute:: cdttemplatetargetid
            
            	This object uniquely identifies the target within the scope of its type
            	**type**\: str
            
            	**range:** 1..20
            
            .. attribute:: cdttemplatetargettype
            
            	This object indicates the type of target
            	**type**\: :py:class:`DynamicTemplateTargetType_Enum <ydk.models.dynamic.CISCO_DYNAMIC_TEMPLATE_TC_MIB.DynamicTemplateTargetType_Enum>`
            
            .. attribute:: cdttemplatetargetstatus
            
            	This object specifies the status of the dynamic template target.  The following columns must be valid before activating a subscriber access profile\:      \- cdtTemplateTargetStorage  However, these objects specify a default value.  Thus, it is possible to use create\-and\-go semantics without setting any additional columns.  An implementation must allow the EMS/NMS to modify any column when this column is 'active', including columns defined in tables that have a one\-to\-one or sparse dependent relationship on this table
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: cdttemplatetargetstorage
            
            	This object specifies what happens to the dynamic template target upon restart
            	**type**\: :py:class:`StorageType_Enum <ydk.models.snmpv2.SNMPv2_TC.StorageType_Enum>`
            
            

            """

            _prefix = 'cisco-dynamic-template'
            _revision = '2007-09-06'

            def __init__(self):
                self.parent = None
                self.cdttemplatetargetid = None
                self.cdttemplatetargettype = None
                self.cdttemplatetargetstatus = None
                self.cdttemplatetargetstorage = None

            @property
            def _common_path(self):
                if self.cdttemplatetargetid is None:
                    raise YPYDataValidationError('Key property cdttemplatetargetid is None')
                if self.cdttemplatetargettype is None:
                    raise YPYDataValidationError('Key property cdttemplatetargettype is None')

                return '/CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/CISCO-DYNAMIC-TEMPLATE-MIB:cdtTemplateTargetTable/CISCO-DYNAMIC-TEMPLATE-MIB:cdtTemplateTargetEntry[CISCO-DYNAMIC-TEMPLATE-MIB:cdtTemplateTargetId = ' + str(self.cdttemplatetargetid) + '][CISCO-DYNAMIC-TEMPLATE-MIB:cdtTemplateTargetType = ' + str(self.cdttemplatetargettype) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cdttemplatetargetid is not None:
                    return True

                if self.cdttemplatetargettype is not None:
                    return True

                if self.cdttemplatetargetstatus is not None:
                    return True

                if self.cdttemplatetargetstorage is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.dynamic._meta import _CISCO_DYNAMIC_TEMPLATE_MIB as meta
                return meta._meta_table['CISCODYNAMICTEMPLATEMIB.CdtTemplateTargetTable.CdtTemplateTargetEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/CISCO-DYNAMIC-TEMPLATE-MIB:cdtTemplateTargetTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cdttemplatetargetentry is not None:
                for child_ref in self.cdttemplatetargetentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.dynamic._meta import _CISCO_DYNAMIC_TEMPLATE_MIB as meta
            return meta._meta_table['CISCODYNAMICTEMPLATEMIB.CdtTemplateTargetTable']['meta_info']


    class CdtTemplateUsageTable(object):
        """
        This table contains a list of targets using each dynamic
        template.
        
        This table has an expansion dependent relationship on the
        cdtTemplateTable, containing zero or more rows for each
        dynamic template.
        
        .. attribute:: cdttemplateusageentry
        
        	An entry indicates a target using the dynamic template.  The system automatically creates an entry when it associates a dynamic template to a target.  The system also creates an entry when it derives the configuration that it applies to a target.  The system automatically destroys an entry under the following circumstances\:  1)  The target indicated by the entry no longer exists.  2)  The association between the target and the dynamic template     no longer exists
        	**type**\: list of :py:class:`CdtTemplateUsageEntry <ydk.models.dynamic.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtTemplateUsageTable.CdtTemplateUsageEntry>`
        
        

        """

        _prefix = 'cisco-dynamic-template'
        _revision = '2007-09-06'

        def __init__(self):
            self.parent = None
            self.cdttemplateusageentry = YList()
            self.cdttemplateusageentry.parent = self
            self.cdttemplateusageentry.name = 'cdttemplateusageentry'


        class CdtTemplateUsageEntry(object):
            """
            An entry indicates a target using the dynamic template.
            
            The system automatically creates an entry when it associates a
            dynamic template to a target.
            
            The system also creates an entry when it derives the
            configuration that it applies to a target.
            
            The system automatically destroys an entry under the following
            circumstances\:
            
            1)  The target indicated by the entry no longer exists.
            
            2)  The association between the target and the dynamic template
                no longer exists.
            
            .. attribute:: cdttemplatename
            
            	
            	**type**\: str
            
            	**range:** 1..64
            
            .. attribute:: cdttemplateusagetargetid
            
            	This object indicates the name of the target using the dynamic template
            	**type**\: str
            
            	**range:** 1..20
            
            .. attribute:: cdttemplateusagetargettype
            
            	This object indicates the type of target using the dynamic template
            	**type**\: :py:class:`DynamicTemplateTargetType_Enum <ydk.models.dynamic.CISCO_DYNAMIC_TEMPLATE_TC_MIB.DynamicTemplateTargetType_Enum>`
            
            

            """

            _prefix = 'cisco-dynamic-template'
            _revision = '2007-09-06'

            def __init__(self):
                self.parent = None
                self.cdttemplatename = None
                self.cdttemplateusagetargetid = None
                self.cdttemplateusagetargettype = None

            @property
            def _common_path(self):
                if self.cdttemplatename is None:
                    raise YPYDataValidationError('Key property cdttemplatename is None')
                if self.cdttemplateusagetargetid is None:
                    raise YPYDataValidationError('Key property cdttemplateusagetargetid is None')
                if self.cdttemplateusagetargettype is None:
                    raise YPYDataValidationError('Key property cdttemplateusagetargettype is None')

                return '/CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/CISCO-DYNAMIC-TEMPLATE-MIB:cdtTemplateUsageTable/CISCO-DYNAMIC-TEMPLATE-MIB:cdtTemplateUsageEntry[CISCO-DYNAMIC-TEMPLATE-MIB:cdtTemplateName = ' + str(self.cdttemplatename) + '][CISCO-DYNAMIC-TEMPLATE-MIB:cdtTemplateUsageTargetId = ' + str(self.cdttemplateusagetargetid) + '][CISCO-DYNAMIC-TEMPLATE-MIB:cdtTemplateUsageTargetType = ' + str(self.cdttemplateusagetargettype) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cdttemplatename is not None:
                    return True

                if self.cdttemplateusagetargetid is not None:
                    return True

                if self.cdttemplateusagetargettype is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.dynamic._meta import _CISCO_DYNAMIC_TEMPLATE_MIB as meta
                return meta._meta_table['CISCODYNAMICTEMPLATEMIB.CdtTemplateUsageTable.CdtTemplateUsageEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/CISCO-DYNAMIC-TEMPLATE-MIB:cdtTemplateUsageTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cdttemplateusageentry is not None:
                for child_ref in self.cdttemplateusageentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.dynamic._meta import _CISCO_DYNAMIC_TEMPLATE_MIB as meta
            return meta._meta_table['CISCODYNAMICTEMPLATEMIB.CdtTemplateUsageTable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.cdtethernettemplatetable is not None and self.cdtethernettemplatetable._has_data():
            return True

        if self.cdtethernettemplatetable is not None and self.cdtethernettemplatetable.is_presence():
            return True

        if self.cdtiftemplatetable is not None and self.cdtiftemplatetable._has_data():
            return True

        if self.cdtiftemplatetable is not None and self.cdtiftemplatetable.is_presence():
            return True

        if self.cdtppppeeripaddrpooltable is not None and self.cdtppppeeripaddrpooltable._has_data():
            return True

        if self.cdtppppeeripaddrpooltable is not None and self.cdtppppeeripaddrpooltable.is_presence():
            return True

        if self.cdtppptemplatetable is not None and self.cdtppptemplatetable._has_data():
            return True

        if self.cdtppptemplatetable is not None and self.cdtppptemplatetable.is_presence():
            return True

        if self.cdtsrvtemplatetable is not None and self.cdtsrvtemplatetable._has_data():
            return True

        if self.cdtsrvtemplatetable is not None and self.cdtsrvtemplatetable.is_presence():
            return True

        if self.cdttemplateassociationtable is not None and self.cdttemplateassociationtable._has_data():
            return True

        if self.cdttemplateassociationtable is not None and self.cdttemplateassociationtable.is_presence():
            return True

        if self.cdttemplatecommontable is not None and self.cdttemplatecommontable._has_data():
            return True

        if self.cdttemplatecommontable is not None and self.cdttemplatecommontable.is_presence():
            return True

        if self.cdttemplatetable is not None and self.cdttemplatetable._has_data():
            return True

        if self.cdttemplatetable is not None and self.cdttemplatetable.is_presence():
            return True

        if self.cdttemplatetargettable is not None and self.cdttemplatetargettable._has_data():
            return True

        if self.cdttemplatetargettable is not None and self.cdttemplatetargettable.is_presence():
            return True

        if self.cdttemplateusagetable is not None and self.cdttemplateusagetable._has_data():
            return True

        if self.cdttemplateusagetable is not None and self.cdttemplateusagetable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.dynamic._meta import _CISCO_DYNAMIC_TEMPLATE_MIB as meta
        return meta._meta_table['CISCODYNAMICTEMPLATEMIB']['meta_info']


