""" ietf_nvo_vpn 

ietf\-nvo\-vpn

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class Nvovpnmgr(object):
    """
    
    
    .. attribute:: composedvpns
    
    	
    	**type**\: list of    :py:class:`Composedvpns <ydk.models.ietf.ietf_nvo_vpn.Nvovpnmgr.Composedvpns>`
    
    

    """

    _prefix = 'VPN'
    _revision = '2016-10-24'

    def __init__(self):
        self.composedvpns = YList()
        self.composedvpns.parent = self
        self.composedvpns.name = 'composedvpns'


    class Composedvpns(object):
        """
        
        
        .. attribute:: id  <key>
        
        	UUID\-STR for service 
        	**type**\:  str
        
        	**pattern:** [0\-9a\-fA\-F]{8}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{12}
        
        .. attribute:: accesspointlist
        
        	TP list of the access links which associated with CE and PE
        	**type**\: list of    :py:class:`Accesspointlist <ydk.models.ietf.ietf_nvo_vpn.Nvovpnmgr.Composedvpns.Accesspointlist>`
        
        .. attribute:: businesstypeid
        
        	business Type Name
        	**type**\:  str
        
        	**pattern:** [0\-9a\-fA\-F]{8}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{12}
        
        .. attribute:: description
        
        	Detailed specification for the servcie
        	**type**\:  str
        
        	**length:** 0..200
        
        .. attribute:: name
        
        	Human\-readable name for the service
        	**type**\:  str
        
        	**length:** 0..200
        
        .. attribute:: operstatus
        
        	Operational status
        	**type**\:   :py:class:`OperstatusEnum <ydk.models.ietf.ietf_nvo_common_types.OperstatusEnum>`
        
        .. attribute:: segvpnlist
        
        	SegVpn list 
        	**type**\: list of    :py:class:`Segvpnlist <ydk.models.ietf.ietf_nvo_vpn.Nvovpnmgr.Composedvpns.Segvpnlist>`
        
        .. attribute:: starttime
        
        	Service lifecycle\: request for service start time
        	**type**\:  str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        .. attribute:: syncstatus
        
        	Sync status
        	**type**\:   :py:class:`SyncstatusEnum <ydk.models.ietf.ietf_nvo_common_types.SyncstatusEnum>`
        
        .. attribute:: tenantid
        
        	UUID\-STR for tenant
        	**type**\:  str
        
        	**pattern:** [0\-9a\-fA\-F]{8}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{12}
        
        .. attribute:: vpnbasicinfo
        
        	VPN BASIC INFO
        	**type**\:   :py:class:`Vpnbasicinfo <ydk.models.ietf.ietf_nvo_vpn.Nvovpnmgr.Composedvpns.Vpnbasicinfo>`
        
        

        """

        _prefix = 'VPN'
        _revision = '2016-10-24'

        def __init__(self):
            self.parent = None
            self.id = None
            self.accesspointlist = YList()
            self.accesspointlist.parent = self
            self.accesspointlist.name = 'accesspointlist'
            self.businesstypeid = None
            self.description = None
            self.name = None
            self.operstatus = None
            self.segvpnlist = YList()
            self.segvpnlist.parent = self
            self.segvpnlist.name = 'segvpnlist'
            self.starttime = None
            self.syncstatus = None
            self.tenantid = None
            self.vpnbasicinfo = Nvovpnmgr.Composedvpns.Vpnbasicinfo()
            self.vpnbasicinfo.parent = self


        class Vpnbasicinfo(object):
            """
            VPN BASIC INFO
            
            .. attribute:: adminstatus
            
            	administrative status
            	**type**\:   :py:class:`AdminstatusEnum <ydk.models.ietf.ietf_nvo_common_types.AdminstatusEnum>`
            
            .. attribute:: servicetype
            
            	current support for mpls l3vpn/vxlan/L2VPN overlay, others is reserved for future extensions
            	**type**\:   :py:class:`ServicetypeEnum <ydk.models.ietf.ietf_nvo_vpn_types.ServicetypeEnum>`
            
            .. attribute:: technology
            
            	mpls\|vxlan overlay l3vpn\|eth over sdh\|nop
            	**type**\:   :py:class:`VpntunneltypeEnum <ydk.models.ietf.ietf_nvo_vpn_types.VpntunneltypeEnum>`
            
            .. attribute:: topology
            
            	current support for full\-mesh and point\_to\_multipoint(hub\-spoke), others is reserved for future extensions
            	**type**\:   :py:class:`TopologyEnum <ydk.models.ietf.ietf_nvo_common_types.TopologyEnum>`
            
            

            """

            _prefix = 'VPN'
            _revision = '2016-10-24'

            def __init__(self):
                self.parent = None
                self.adminstatus = None
                self.servicetype = None
                self.technology = None
                self.topology = None

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/ietf-nvo-vpn:vpnBasicInfo'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.adminstatus is not None:
                    return True

                if self.servicetype is not None:
                    return True

                if self.technology is not None:
                    return True

                if self.topology is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_nvo_vpn as meta
                return meta._meta_table['Nvovpnmgr.Composedvpns.Vpnbasicinfo']['meta_info']


        class Segvpnlist(object):
            """
            SegVpn list 
            
            .. attribute:: index  <key>
            
            	index of segment VPN in a composed VPN
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: vpninfo
            
            	vpn information
            	**type**\:   :py:class:`Vpninfo <ydk.models.ietf.ietf_nvo_vpn.Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo>`
            
            .. attribute:: vpnrole
            
            	value\: nop\|vpn
            	**type**\:   :py:class:`ProtectionroleEnum <ydk.models.ietf.ietf_nvo_vpn_types.ProtectionroleEnum>`
            
            .. attribute:: vpntype
            
            	value\: nop/wanVpn
            	**type**\:  str
            
            	**length:** 0..30
            
            

            """

            _prefix = 'VPN'
            _revision = '2016-10-24'

            def __init__(self):
                self.parent = None
                self.index = None
                self.vpninfo = Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo()
                self.vpninfo.parent = self
                self.vpnrole = None
                self.vpntype = None


            class Vpninfo(object):
                """
                vpn information
                
                .. attribute:: vpn
                
                	vpn
                	**type**\:   :py:class:`Vpn <ydk.models.ietf.ietf_nvo_vpn.Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn>`
                
                

                """

                _prefix = 'VPN'
                _revision = '2016-10-24'

                def __init__(self):
                    self.parent = None
                    self.vpn = Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn()
                    self.vpn.parent = self


                class Vpn(object):
                    """
                    vpn.
                    
                    .. attribute:: accesspointlist
                    
                    	TP list of the access links which associated with CE and PE
                    	**type**\: list of    :py:class:`Accesspointlist <ydk.models.ietf.ietf_nvo_vpn.Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist>`
                    
                    .. attribute:: description
                    
                    	Detailed specification for the servcie
                    	**type**\:  str
                    
                    	**length:** 0..200
                    
                    .. attribute:: id
                    
                    	UUID\-STR for VPN
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{8}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{12}
                    
                    .. attribute:: name
                    
                    	Human\-readable name for the service
                    	**type**\:  str
                    
                    	**length:** 0..200
                    
                    .. attribute:: operstatus
                    
                    	Operational status
                    	**type**\:   :py:class:`OperstatusEnum <ydk.models.ietf.ietf_nvo_common_types.OperstatusEnum>`
                    
                    .. attribute:: syncstatus
                    
                    	Sync status
                    	**type**\:   :py:class:`SyncstatusEnum <ydk.models.ietf.ietf_nvo_common_types.SyncstatusEnum>`
                    
                    .. attribute:: vpnbasicinfo
                    
                    	vpn basic info
                    	**type**\:   :py:class:`Vpnbasicinfo <ydk.models.ietf.ietf_nvo_vpn.Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Vpnbasicinfo>`
                    
                    

                    """

                    _prefix = 'VPN'
                    _revision = '2016-10-24'

                    def __init__(self):
                        self.parent = None
                        self.accesspointlist = YList()
                        self.accesspointlist.parent = self
                        self.accesspointlist.name = 'accesspointlist'
                        self.description = None
                        self.id = None
                        self.name = None
                        self.operstatus = None
                        self.syncstatus = None
                        self.vpnbasicinfo = Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Vpnbasicinfo()
                        self.vpnbasicinfo.parent = self


                    class Vpnbasicinfo(object):
                        """
                        vpn basic info
                        
                        .. attribute:: adminstatus
                        
                        	administrative status
                        	**type**\:   :py:class:`AdminstatusEnum <ydk.models.ietf.ietf_nvo_common_types.AdminstatusEnum>`
                        
                        .. attribute:: servicetype
                        
                        	current support for mpls l3vpn/vxlan/L2VPN overlay, others is reserved for future extensions
                        	**type**\:   :py:class:`ServicetypeEnum <ydk.models.ietf.ietf_nvo_vpn_types.ServicetypeEnum>`
                        
                        .. attribute:: technology
                        
                        	mpls\|vxlan overlay l3vpn\|eth over sdh\|nop
                        	**type**\:   :py:class:`VpntunneltypeEnum <ydk.models.ietf.ietf_nvo_vpn_types.VpntunneltypeEnum>`
                        
                        .. attribute:: topology
                        
                        	current support for full\-mesh and point\_to\_multipoint(hub\-spoke), others is reserved for future extensions
                        	**type**\:   :py:class:`TopologyEnum <ydk.models.ietf.ietf_nvo_common_types.TopologyEnum>`
                        
                        

                        """

                        _prefix = 'VPN'
                        _revision = '2016-10-24'

                        def __init__(self):
                            self.parent = None
                            self.adminstatus = None
                            self.servicetype = None
                            self.technology = None
                            self.topology = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/ietf-nvo-vpn:vpnBasicInfo'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.adminstatus is not None:
                                return True

                            if self.servicetype is not None:
                                return True

                            if self.technology is not None:
                                return True

                            if self.topology is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ietf._meta import _ietf_nvo_vpn as meta
                            return meta._meta_table['Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Vpnbasicinfo']['meta_info']


                    class Accesspointlist(object):
                        """
                        TP list of the access links which associated
                        with CE and PE
                        
                        .. attribute:: id  <key>
                        
                        	yang\:uuid\-str for TP
                        	**type**\:  str
                        
                        	**pattern:** [0\-9a\-fA\-F]{8}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{12}
                        
                        .. attribute:: containingmaintpid
                        
                        	uuid\-str for main interface
                        	**type**\:  str
                        
                        	**pattern:** [0\-9a\-fA\-F]{8}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{12}
                        
                        .. attribute:: description
                        
                        	description for this tp
                        	**type**\:  str
                        
                        	**length:** 0..200
                        
                        .. attribute:: name
                        
                        	Must abbey to name rule defined in system. Example FE0/0/1, GE1/2/1.1, Eth\-Trunk1.1, etc
                        	**type**\:  str
                        
                        	**length:** 0..200
                        
                        .. attribute:: neid
                        
                        	yang\:uuid\-str for NE 
                        	**type**\:  str
                        
                        	**pattern:** [0\-9a\-fA\-F]{8}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{12}
                        
                        .. attribute:: operstatus
                        
                        	Operational status
                        	**type**\:   :py:class:`OperstatusEnum <ydk.models.ietf.ietf_nvo_common_types.OperstatusEnum>`
                        
                        .. attribute:: peercetp
                        
                        	CE TP Information
                        	**type**\:   :py:class:`Peercetp <ydk.models.ietf.ietf_nvo_vpn.Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Peercetp>`
                        
                        .. attribute:: routeprotocolspec
                        
                        	route protocol spec
                        	**type**\: list of    :py:class:`Routeprotocolspec <ydk.models.ietf.ietf_nvo_vpn.Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Routeprotocolspec>`
                        
                        .. attribute:: tpbasicinfo
                        
                        	Tp non\-instance basic info
                        	**type**\:   :py:class:`Tpbasicinfo <ydk.models.ietf.ietf_nvo_vpn.Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo>`
                        
                        

                        """

                        _prefix = 'VPN'
                        _revision = '2016-10-24'

                        def __init__(self):
                            self.parent = None
                            self.id = None
                            self.containingmaintpid = None
                            self.description = None
                            self.name = None
                            self.neid = None
                            self.operstatus = None
                            self.peercetp = Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Peercetp()
                            self.peercetp.parent = self
                            self.routeprotocolspec = YList()
                            self.routeprotocolspec.parent = self
                            self.routeprotocolspec.name = 'routeprotocolspec'
                            self.tpbasicinfo = Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo()
                            self.tpbasicinfo.parent = self


                        class Tpbasicinfo(object):
                            """
                            Tp non\-instance basic info
                            
                            .. attribute:: addtionalinfo
                            
                            	addtionalInfo
                            	**type**\: list of    :py:class:`Addtionalinfo <ydk.models.ietf.ietf_nvo_vpn.Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Addtionalinfo>`
                            
                            .. attribute:: adminstatus
                            
                            	administrative status
                            	**type**\:   :py:class:`AdminstatusEnum <ydk.models.ietf.ietf_nvo_common_types.AdminstatusEnum>`
                            
                            .. attribute:: edgepointrole
                            
                            	edge role for TP, for example\:UNI/NNI 
                            	**type**\:   :py:class:`EdgepointroleEnum <ydk.models.ietf.ietf_nvo_common_types.EdgepointroleEnum>`
                            
                            .. attribute:: flowservices
                            
                            	flow services in one TP
                            	**type**\:   :py:class:`Flowservices <ydk.models.ietf.ietf_nvo_vpn.Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Flowservices>`
                            
                            .. attribute:: topologyrole
                            
                            	hub/spoke role, etc
                            	**type**\:   :py:class:`ToponoderoleEnum <ydk.models.ietf.ietf_nvo_common_types.ToponoderoleEnum>`
                            
                            .. attribute:: tpqosnode
                            
                            	tpQosNode
                            	**type**\:   :py:class:`Tpqosnode <ydk.models.ietf.ietf_nvo_vpn.Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Tpqosnode>`
                            
                            .. attribute:: type
                            
                            	Type
                            	**type**\:   :py:class:`TptypeEnum <ydk.models.ietf.ietf_nvo_common_types.TptypeEnum>`
                            
                            .. attribute:: typespeclist
                            
                            	typeSpecList
                            	**type**\: list of    :py:class:`Typespeclist <ydk.models.ietf.ietf_nvo_vpn.Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Typespeclist>`
                            
                            .. attribute:: workinglayer
                            
                            	working layer
                            	**type**\:   :py:class:`LayerrateEnum <ydk.models.ietf.ietf_nvo_common_types.LayerrateEnum>`
                            
                            

                            """

                            _prefix = 'VPN'
                            _revision = '2016-10-24'

                            def __init__(self):
                                self.parent = None
                                self.addtionalinfo = YList()
                                self.addtionalinfo.parent = self
                                self.addtionalinfo.name = 'addtionalinfo'
                                self.adminstatus = None
                                self.edgepointrole = None
                                self.flowservices = Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Flowservices()
                                self.flowservices.parent = self
                                self.topologyrole = None
                                self.tpqosnode = Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Tpqosnode()
                                self.tpqosnode.parent = self
                                self.type = None
                                self.typespeclist = YList()
                                self.typespeclist.parent = self
                                self.typespeclist.name = 'typespeclist'
                                self.workinglayer = None


                            class Typespeclist(object):
                                """
                                typeSpecList
                                
                                .. attribute:: layerrate  <key>
                                
                                	layerRate
                                	**type**\:   :py:class:`LayerrateEnum <ydk.models.ietf.ietf_nvo_common_types.LayerrateEnum>`
                                
                                .. attribute:: ethernetspec
                                
                                	ethernetSpec
                                	**type**\:   :py:class:`Ethernetspec <ydk.models.ietf.ietf_nvo_vpn.Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Typespeclist.Ethernetspec>`
                                
                                .. attribute:: ipspec
                                
                                	ipSpec
                                	**type**\:   :py:class:`Ipspec <ydk.models.ietf.ietf_nvo_vpn.Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Typespeclist.Ipspec>`
                                
                                .. attribute:: vxlanspec
                                
                                	vxlanSpec
                                	**type**\:   :py:class:`Vxlanspec <ydk.models.ietf.ietf_nvo_vpn.Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Typespeclist.Vxlanspec>`
                                
                                

                                """

                                _prefix = 'VPN'
                                _revision = '2016-10-24'

                                def __init__(self):
                                    self.parent = None
                                    self.layerrate = None
                                    self.ethernetspec = Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Typespeclist.Ethernetspec()
                                    self.ethernetspec.parent = self
                                    self.ipspec = Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Typespeclist.Ipspec()
                                    self.ipspec.parent = self
                                    self.vxlanspec = Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Typespeclist.Vxlanspec()
                                    self.vxlanspec.parent = self


                                class Ethernetspec(object):
                                    """
                                    ethernetSpec
                                    
                                    .. attribute:: accesstype
                                    
                                    	access frame type
                                    	**type**\:   :py:class:`EthernetencaptypeEnum <ydk.models.ietf.ietf_nvo_common_types.EthernetencaptypeEnum>`
                                    
                                    .. attribute:: actionvalue
                                    
                                    	action value
                                    	**type**\:  str
                                    
                                    	**length:** 0..100
                                    
                                    .. attribute:: dot1q
                                    
                                    	dot1q
                                    	**type**\:   :py:class:`Dot1Q <ydk.models.ietf.ietf_nvo_vpn.Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Typespeclist.Ethernetspec.Dot1Q>`
                                    
                                    .. attribute:: qinqvlan
                                    
                                    	qinqVlan
                                    	**type**\:   :py:class:`Qinqvlan <ydk.models.ietf.ietf_nvo_vpn.Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Typespeclist.Ethernetspec.Qinqvlan>`
                                    
                                    .. attribute:: vlanaction
                                    
                                    	Frame type that can be accepted. not needed now
                                    	**type**\:   :py:class:`EthernetactionEnum <ydk.models.ietf.ietf_nvo_common_types.EthernetactionEnum>`
                                    
                                    

                                    """

                                    _prefix = 'VPN'
                                    _revision = '2016-10-24'

                                    def __init__(self):
                                        self.parent = None
                                        self.accesstype = None
                                        self.actionvalue = None
                                        self.dot1q = Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Typespeclist.Ethernetspec.Dot1Q()
                                        self.dot1q.parent = self
                                        self.qinqvlan = Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Typespeclist.Ethernetspec.Qinqvlan()
                                        self.qinqvlan.parent = self
                                        self.vlanaction = None


                                    class Qinqvlan(object):
                                        """
                                        qinqVlan
                                        
                                        .. attribute:: cvlanlist
                                        
                                        	cvlanList
                                        	**type**\:  list of int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: svlanlist
                                        
                                        	svlanList
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        

                                        """

                                        _prefix = 'VPN'
                                        _revision = '2016-10-24'

                                        def __init__(self):
                                            self.parent = None
                                            self.cvlanlist = YLeafList()
                                            self.cvlanlist.parent = self
                                            self.cvlanlist.name = 'cvlanlist'
                                            self.svlanlist = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/ietf-nvo-vpn:qinqVlan'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.cvlanlist is not None:
                                                for child in self.cvlanlist:
                                                    if child is not None:
                                                        return True

                                            if self.svlanlist is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.ietf._meta import _ietf_nvo_vpn as meta
                                            return meta._meta_table['Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Typespeclist.Ethernetspec.Qinqvlan']['meta_info']


                                    class Dot1Q(object):
                                        """
                                        dot1q
                                        
                                        .. attribute:: dot1qvlanlist
                                        
                                        	dot1qVlanList
                                        	**type**\:  list of int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        

                                        """

                                        _prefix = 'VPN'
                                        _revision = '2016-10-24'

                                        def __init__(self):
                                            self.parent = None
                                            self.dot1qvlanlist = YLeafList()
                                            self.dot1qvlanlist.parent = self
                                            self.dot1qvlanlist.name = 'dot1qvlanlist'

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/ietf-nvo-vpn:dot1q'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.dot1qvlanlist is not None:
                                                for child in self.dot1qvlanlist:
                                                    if child is not None:
                                                        return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.ietf._meta import _ietf_nvo_vpn as meta
                                            return meta._meta_table['Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Typespeclist.Ethernetspec.Dot1Q']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/ietf-nvo-vpn:ethernetSpec'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.accesstype is not None:
                                            return True

                                        if self.actionvalue is not None:
                                            return True

                                        if self.dot1q is not None and self.dot1q._has_data():
                                            return True

                                        if self.qinqvlan is not None and self.qinqvlan._has_data():
                                            return True

                                        if self.vlanaction is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.ietf._meta import _ietf_nvo_vpn as meta
                                        return meta._meta_table['Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Typespeclist.Ethernetspec']['meta_info']


                                class Ipspec(object):
                                    """
                                    ipSpec
                                    
                                    .. attribute:: masterip
                                    
                                    	master IP address
                                    	**type**\:  str
                                    
                                    .. attribute:: mtu
                                    
                                    	mtu for ip layer,scope\:46~9600
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'VPN'
                                    _revision = '2016-10-24'

                                    def __init__(self):
                                        self.parent = None
                                        self.masterip = None
                                        self.mtu = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/ietf-nvo-vpn:ipSpec'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.masterip is not None:
                                            return True

                                        if self.mtu is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.ietf._meta import _ietf_nvo_vpn as meta
                                        return meta._meta_table['Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Typespeclist.Ipspec']['meta_info']


                                class Vxlanspec(object):
                                    """
                                    vxlanSpec
                                    
                                    .. attribute:: vni
                                    
                                    	vni
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: vtepip
                                    
                                    	vtep ip
                                    	**type**\:  str
                                    
                                    

                                    """

                                    _prefix = 'VPN'
                                    _revision = '2016-10-24'

                                    def __init__(self):
                                        self.parent = None
                                        self.vni = None
                                        self.vtepip = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/ietf-nvo-vpn:vxlanSpec'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.vni is not None:
                                            return True

                                        if self.vtepip is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.ietf._meta import _ietf_nvo_vpn as meta
                                        return meta._meta_table['Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Typespeclist.Vxlanspec']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.layerrate is None:
                                        raise YPYModelError('Key property layerrate is None')

                                    return self.parent._common_path +'/ietf-nvo-vpn:typeSpecList[ietf-nvo-vpn:layerRate = ' + str(self.layerrate) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.layerrate is not None:
                                        return True

                                    if self.ethernetspec is not None and self.ethernetspec._has_data():
                                        return True

                                    if self.ipspec is not None and self.ipspec._has_data():
                                        return True

                                    if self.vxlanspec is not None and self.vxlanspec._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ietf._meta import _ietf_nvo_vpn as meta
                                    return meta._meta_table['Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Typespeclist']['meta_info']


                            class Tpqosnode(object):
                                """
                                tpQosNode
                                
                                .. attribute:: inqosprofileid
                                
                                	inQosProfileId
                                	**type**\:  str
                                
                                	**pattern:** [0\-9a\-fA\-F]{8}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{12}
                                
                                .. attribute:: intpcar
                                
                                	inTpCar
                                	**type**\: list of    :py:class:`Intpcar <ydk.models.ietf.ietf_nvo_vpn.Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Tpqosnode.Intpcar>`
                                
                                .. attribute:: outqosprofileid
                                
                                	outQosProfileId
                                	**type**\:  str
                                
                                	**pattern:** [0\-9a\-fA\-F]{8}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{12}
                                
                                .. attribute:: outtpcar
                                
                                	outTpCar
                                	**type**\: list of    :py:class:`Outtpcar <ydk.models.ietf.ietf_nvo_vpn.Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Tpqosnode.Outtpcar>`
                                
                                .. attribute:: qosconfigtype
                                
                                	qosConfigType
                                	**type**\:   :py:class:`QosconfigtypeEnum <ydk.models.ietf.ietf_nvo_qos_types.QosconfigtypeEnum>`
                                
                                .. attribute:: qosdetailtype
                                
                                	qosDetailType
                                	**type**\:   :py:class:`QosdetailtypeEnum <ydk.models.ietf.ietf_nvo_qos_types.QosdetailtypeEnum>`
                                
                                

                                """

                                _prefix = 'VPN'
                                _revision = '2016-10-24'

                                def __init__(self):
                                    self.parent = None
                                    self.inqosprofileid = None
                                    self.intpcar = YList()
                                    self.intpcar.parent = self
                                    self.intpcar.name = 'intpcar'
                                    self.outqosprofileid = None
                                    self.outtpcar = YList()
                                    self.outtpcar.parent = self
                                    self.outtpcar.name = 'outtpcar'
                                    self.qosconfigtype = None
                                    self.qosdetailtype = None


                                class Intpcar(object):
                                    """
                                    inTpCar
                                    
                                    .. attribute:: index  <key>
                                    
                                    	index
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: action
                                    
                                    	action
                                    	**type**\:  str
                                    
                                    .. attribute:: actiontype
                                    
                                    	actionType
                                    	**type**\:   :py:class:`ActiontypeEnum <ydk.models.ietf.ietf_nvo_qos_types.ActiontypeEnum>`
                                    
                                    .. attribute:: datakind
                                    
                                    	dataKind
                                    	**type**\:   :py:class:`DatakindEnum <ydk.models.ietf.ietf_nvo_qos_types.DatakindEnum>`
                                    
                                    

                                    """

                                    _prefix = 'VPN'
                                    _revision = '2016-10-24'

                                    def __init__(self):
                                        self.parent = None
                                        self.index = None
                                        self.action = None
                                        self.actiontype = None
                                        self.datakind = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.index is None:
                                            raise YPYModelError('Key property index is None')

                                        return self.parent._common_path +'/ietf-nvo-vpn:inTpCar[ietf-nvo-vpn:index = ' + str(self.index) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.index is not None:
                                            return True

                                        if self.action is not None:
                                            return True

                                        if self.actiontype is not None:
                                            return True

                                        if self.datakind is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.ietf._meta import _ietf_nvo_vpn as meta
                                        return meta._meta_table['Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Tpqosnode.Intpcar']['meta_info']


                                class Outtpcar(object):
                                    """
                                    outTpCar
                                    
                                    .. attribute:: index  <key>
                                    
                                    	index
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: action
                                    
                                    	action
                                    	**type**\:  str
                                    
                                    .. attribute:: actiontype
                                    
                                    	actionType
                                    	**type**\:   :py:class:`ActiontypeEnum <ydk.models.ietf.ietf_nvo_qos_types.ActiontypeEnum>`
                                    
                                    .. attribute:: datakind
                                    
                                    	dataKind
                                    	**type**\:   :py:class:`DatakindEnum <ydk.models.ietf.ietf_nvo_qos_types.DatakindEnum>`
                                    
                                    

                                    """

                                    _prefix = 'VPN'
                                    _revision = '2016-10-24'

                                    def __init__(self):
                                        self.parent = None
                                        self.index = None
                                        self.action = None
                                        self.actiontype = None
                                        self.datakind = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.index is None:
                                            raise YPYModelError('Key property index is None')

                                        return self.parent._common_path +'/ietf-nvo-vpn:outTpCar[ietf-nvo-vpn:index = ' + str(self.index) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.index is not None:
                                            return True

                                        if self.action is not None:
                                            return True

                                        if self.actiontype is not None:
                                            return True

                                        if self.datakind is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.ietf._meta import _ietf_nvo_vpn as meta
                                        return meta._meta_table['Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Tpqosnode.Outtpcar']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/ietf-nvo-vpn:tpQosNode'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.inqosprofileid is not None:
                                        return True

                                    if self.intpcar is not None:
                                        for child_ref in self.intpcar:
                                            if child_ref._has_data():
                                                return True

                                    if self.outqosprofileid is not None:
                                        return True

                                    if self.outtpcar is not None:
                                        for child_ref in self.outtpcar:
                                            if child_ref._has_data():
                                                return True

                                    if self.qosconfigtype is not None:
                                        return True

                                    if self.qosdetailtype is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ietf._meta import _ietf_nvo_vpn as meta
                                    return meta._meta_table['Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Tpqosnode']['meta_info']


                            class Flowservices(object):
                                """
                                flow services in one TP
                                
                                .. attribute:: flowqostemplateid
                                
                                	flowQosTemplateID
                                	**type**\:  str
                                
                                	**pattern:** [0\-9a\-fA\-F]{8}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{12}
                                
                                .. attribute:: flowservices
                                
                                	default in flow and behaviors
                                	**type**\: list of    :py:class:`Flowservices_ <ydk.models.ietf.ietf_nvo_vpn.Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Flowservices.Flowservices_>`
                                
                                .. attribute:: inflowqostemplateid
                                
                                	inFlowQosTemplateID
                                	**type**\:  str
                                
                                	**pattern:** [0\-9a\-fA\-F]{8}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{12}
                                
                                .. attribute:: outflowqostemplateid
                                
                                	outFlowQosTemplateID
                                	**type**\:  str
                                
                                	**pattern:** [0\-9a\-fA\-F]{8}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{12}
                                
                                .. attribute:: qosconfigtype
                                
                                	qosConfigType
                                	**type**\:   :py:class:`QosconfigtypeEnum <ydk.models.ietf.ietf_nvo_qos_types.QosconfigtypeEnum>`
                                
                                .. attribute:: qosdetailtype
                                
                                	qosDetailType
                                	**type**\:   :py:class:`QosdetailtypeEnum <ydk.models.ietf.ietf_nvo_qos_types.QosdetailtypeEnum>`
                                
                                

                                """

                                _prefix = 'VPN'
                                _revision = '2016-10-24'

                                def __init__(self):
                                    self.parent = None
                                    self.flowqostemplateid = None
                                    self.flowservices = YList()
                                    self.flowservices.parent = self
                                    self.flowservices.name = 'flowservices'
                                    self.inflowqostemplateid = None
                                    self.outflowqostemplateid = None
                                    self.qosconfigtype = None
                                    self.qosdetailtype = None


                                class Flowservices_(object):
                                    """
                                    default in flow and behaviors
                                    
                                    .. attribute:: flowclassifierid  <key>
                                    
                                    	flowClassifierId
                                    	**type**\:  str
                                    
                                    	**pattern:** [0\-9a\-fA\-F]{8}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{12}
                                    
                                    .. attribute:: flowbehaviors
                                    
                                    	flowBehaviors
                                    	**type**\: list of    :py:class:`Flowbehaviors <ydk.models.ietf.ietf_nvo_vpn.Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Flowservices.Flowservices_.Flowbehaviors>`
                                    
                                    

                                    """

                                    _prefix = 'VPN'
                                    _revision = '2016-10-24'

                                    def __init__(self):
                                        self.parent = None
                                        self.flowclassifierid = None
                                        self.flowbehaviors = YList()
                                        self.flowbehaviors.parent = self
                                        self.flowbehaviors.name = 'flowbehaviors'


                                    class Flowbehaviors(object):
                                        """
                                        flowBehaviors
                                        
                                        .. attribute:: index  <key>
                                        
                                        	index
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: action
                                        
                                        	action
                                        	**type**\:  str
                                        
                                        .. attribute:: actiontype
                                        
                                        	actionType
                                        	**type**\:   :py:class:`ActiontypeEnum <ydk.models.ietf.ietf_nvo_qos_types.ActiontypeEnum>`
                                        
                                        .. attribute:: datakind
                                        
                                        	dataKind
                                        	**type**\:   :py:class:`DatakindEnum <ydk.models.ietf.ietf_nvo_qos_types.DatakindEnum>`
                                        
                                        

                                        """

                                        _prefix = 'VPN'
                                        _revision = '2016-10-24'

                                        def __init__(self):
                                            self.parent = None
                                            self.index = None
                                            self.action = None
                                            self.actiontype = None
                                            self.datakind = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')
                                            if self.index is None:
                                                raise YPYModelError('Key property index is None')

                                            return self.parent._common_path +'/ietf-nvo-vpn:flowBehaviors[ietf-nvo-vpn:index = ' + str(self.index) + ']'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.index is not None:
                                                return True

                                            if self.action is not None:
                                                return True

                                            if self.actiontype is not None:
                                                return True

                                            if self.datakind is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.ietf._meta import _ietf_nvo_vpn as meta
                                            return meta._meta_table['Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Flowservices.Flowservices_.Flowbehaviors']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.flowclassifierid is None:
                                            raise YPYModelError('Key property flowclassifierid is None')

                                        return self.parent._common_path +'/ietf-nvo-vpn:flowServices[ietf-nvo-vpn:flowClassifierId = ' + str(self.flowclassifierid) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.flowclassifierid is not None:
                                            return True

                                        if self.flowbehaviors is not None:
                                            for child_ref in self.flowbehaviors:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.ietf._meta import _ietf_nvo_vpn as meta
                                        return meta._meta_table['Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Flowservices.Flowservices_']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/ietf-nvo-vpn:flowServices'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.flowqostemplateid is not None:
                                        return True

                                    if self.flowservices is not None:
                                        for child_ref in self.flowservices:
                                            if child_ref._has_data():
                                                return True

                                    if self.inflowqostemplateid is not None:
                                        return True

                                    if self.outflowqostemplateid is not None:
                                        return True

                                    if self.qosconfigtype is not None:
                                        return True

                                    if self.qosdetailtype is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ietf._meta import _ietf_nvo_vpn as meta
                                    return meta._meta_table['Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Flowservices']['meta_info']


                            class Addtionalinfo(object):
                                """
                                addtionalInfo
                                
                                .. attribute:: name  <key>
                                
                                	string name 
                                	**type**\:  str
                                
                                .. attribute:: value
                                
                                	string value
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'VPN'
                                _revision = '2016-10-24'

                                def __init__(self):
                                    self.parent = None
                                    self.name = None
                                    self.value = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.name is None:
                                        raise YPYModelError('Key property name is None')

                                    return self.parent._common_path +'/ietf-nvo-vpn:addtionalInfo[ietf-nvo-vpn:name = ' + str(self.name) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.name is not None:
                                        return True

                                    if self.value is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ietf._meta import _ietf_nvo_vpn as meta
                                    return meta._meta_table['Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Addtionalinfo']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/ietf-nvo-vpn:tpBasicInfo'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.addtionalinfo is not None:
                                    for child_ref in self.addtionalinfo:
                                        if child_ref._has_data():
                                            return True

                                if self.adminstatus is not None:
                                    return True

                                if self.edgepointrole is not None:
                                    return True

                                if self.flowservices is not None and self.flowservices._has_data():
                                    return True

                                if self.topologyrole is not None:
                                    return True

                                if self.tpqosnode is not None and self.tpqosnode._has_data():
                                    return True

                                if self.type is not None:
                                    return True

                                if self.typespeclist is not None:
                                    for child_ref in self.typespeclist:
                                        if child_ref._has_data():
                                            return True

                                if self.workinglayer is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ietf._meta import _ietf_nvo_vpn as meta
                                return meta._meta_table['Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo']['meta_info']


                        class Peercetp(object):
                            """
                            CE TP Information
                            
                            .. attribute:: cedirectneid
                            
                            	direction connected NE ID, only valid in asbr 
                            	**type**\:  str
                            
                            	**pattern:** [0\-9a\-fA\-F]{8}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{12}
                            
                            .. attribute:: cedirecttpid
                            
                            	ce Direct TP id, only valid in asbr
                            	**type**\:  str
                            
                            	**pattern:** [0\-9a\-fA\-F]{8}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{12}
                            
                            .. attribute:: ceid
                            
                            	Site router ID
                            	**type**\:  str
                            
                            	**pattern:** [0\-9a\-fA\-F]{8}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{12}
                            
                            .. attribute:: ceifmasterip
                            
                            	ceIfmasterIp
                            	**type**\:  str
                            
                            .. attribute:: location
                            
                            	CE device location 
                            	**type**\:  str
                            
                            	**length:** 0..400
                            
                            

                            """

                            _prefix = 'VPN'
                            _revision = '2016-10-24'

                            def __init__(self):
                                self.parent = None
                                self.cedirectneid = None
                                self.cedirecttpid = None
                                self.ceid = None
                                self.ceifmasterip = None
                                self.location = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/ietf-nvo-vpn:peerCeTp'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.cedirectneid is not None:
                                    return True

                                if self.cedirecttpid is not None:
                                    return True

                                if self.ceid is not None:
                                    return True

                                if self.ceifmasterip is not None:
                                    return True

                                if self.location is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ietf._meta import _ietf_nvo_vpn as meta
                                return meta._meta_table['Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Peercetp']['meta_info']


                        class Routeprotocolspec(object):
                            """
                            route protocol spec
                            
                            .. attribute:: type  <key>
                            
                            	Protocol type
                            	**type**\:   :py:class:`RouteprotocoltypeEnum <ydk.models.ietf.ietf_nvo_common_types.RouteprotocoltypeEnum>`
                            
                            .. attribute:: bgpprotocols
                            
                            	bgpProtocols
                            	**type**\: list of    :py:class:`Bgpprotocols <ydk.models.ietf.ietf_nvo_vpn.Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Routeprotocolspec.Bgpprotocols>`
                            
                            .. attribute:: staticrouteitems
                            
                            	staticRouteItems
                            	**type**\: list of    :py:class:`Staticrouteitems <ydk.models.ietf.ietf_nvo_vpn.Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Routeprotocolspec.Staticrouteitems>`
                            
                            

                            """

                            _prefix = 'VPN'
                            _revision = '2016-10-24'

                            def __init__(self):
                                self.parent = None
                                self.type = None
                                self.bgpprotocols = YList()
                                self.bgpprotocols.parent = self
                                self.bgpprotocols.name = 'bgpprotocols'
                                self.staticrouteitems = YList()
                                self.staticrouteitems.parent = self
                                self.staticrouteitems.name = 'staticrouteitems'


                            class Staticrouteitems(object):
                                """
                                staticRouteItems
                                
                                .. attribute:: index  <key>
                                
                                	static item index
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: destinationcidr
                                
                                	destination ip cidr. 
                                	**type**\:  str
                                
                                .. attribute:: egresstp
                                
                                	egress tp
                                	**type**\:  str
                                
                                	**pattern:** [0\-9a\-fA\-F]{8}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{12}
                                
                                .. attribute:: nexthopip
                                
                                	nextHopIp
                                	**type**\:  str
                                
                                	**length:** 0..200
                                
                                .. attribute:: routepreference
                                
                                	route priority. Ordinary, work route have higher priority
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'VPN'
                                _revision = '2016-10-24'

                                def __init__(self):
                                    self.parent = None
                                    self.index = None
                                    self.destinationcidr = None
                                    self.egresstp = None
                                    self.nexthopip = None
                                    self.routepreference = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.index is None:
                                        raise YPYModelError('Key property index is None')

                                    return self.parent._common_path +'/ietf-nvo-vpn:staticRouteItems[ietf-nvo-vpn:index = ' + str(self.index) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.index is not None:
                                        return True

                                    if self.destinationcidr is not None:
                                        return True

                                    if self.egresstp is not None:
                                        return True

                                    if self.nexthopip is not None:
                                        return True

                                    if self.routepreference is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ietf._meta import _ietf_nvo_vpn as meta
                                    return meta._meta_table['Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Routeprotocolspec.Staticrouteitems']['meta_info']


                            class Bgpprotocols(object):
                                """
                                bgpProtocols
                                
                                .. attribute:: index  <key>
                                
                                	index of BGP protocol item
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: bgpmaxprefix
                                
                                	
                                	**type**\:  int
                                
                                	**range:** \-2147483648..2147483647
                                
                                .. attribute:: bgpmaxprefixalarm
                                
                                	alarm threshold of BGP rout
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: peerasnumber
                                
                                	
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: peerip
                                
                                	peerIp
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'VPN'
                                _revision = '2016-10-24'

                                def __init__(self):
                                    self.parent = None
                                    self.index = None
                                    self.bgpmaxprefix = None
                                    self.bgpmaxprefixalarm = None
                                    self.peerasnumber = None
                                    self.peerip = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.index is None:
                                        raise YPYModelError('Key property index is None')

                                    return self.parent._common_path +'/ietf-nvo-vpn:bgpProtocols[ietf-nvo-vpn:index = ' + str(self.index) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.index is not None:
                                        return True

                                    if self.bgpmaxprefix is not None:
                                        return True

                                    if self.bgpmaxprefixalarm is not None:
                                        return True

                                    if self.peerasnumber is not None:
                                        return True

                                    if self.peerip is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ietf._meta import _ietf_nvo_vpn as meta
                                    return meta._meta_table['Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Routeprotocolspec.Bgpprotocols']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.type is None:
                                    raise YPYModelError('Key property type is None')

                                return self.parent._common_path +'/ietf-nvo-vpn:routeProtocolSpec[ietf-nvo-vpn:type = ' + str(self.type) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.type is not None:
                                    return True

                                if self.bgpprotocols is not None:
                                    for child_ref in self.bgpprotocols:
                                        if child_ref._has_data():
                                            return True

                                if self.staticrouteitems is not None:
                                    for child_ref in self.staticrouteitems:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ietf._meta import _ietf_nvo_vpn as meta
                                return meta._meta_table['Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Routeprotocolspec']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.id is None:
                                raise YPYModelError('Key property id is None')

                            return self.parent._common_path +'/ietf-nvo-vpn:accessPointList[ietf-nvo-vpn:id = ' + str(self.id) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.id is not None:
                                return True

                            if self.containingmaintpid is not None:
                                return True

                            if self.description is not None:
                                return True

                            if self.name is not None:
                                return True

                            if self.neid is not None:
                                return True

                            if self.operstatus is not None:
                                return True

                            if self.peercetp is not None and self.peercetp._has_data():
                                return True

                            if self.routeprotocolspec is not None:
                                for child_ref in self.routeprotocolspec:
                                    if child_ref._has_data():
                                        return True

                            if self.tpbasicinfo is not None and self.tpbasicinfo._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ietf._meta import _ietf_nvo_vpn as meta
                            return meta._meta_table['Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/ietf-nvo-vpn:vpn'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.accesspointlist is not None:
                            for child_ref in self.accesspointlist:
                                if child_ref._has_data():
                                    return True

                        if self.description is not None:
                            return True

                        if self.id is not None:
                            return True

                        if self.name is not None:
                            return True

                        if self.operstatus is not None:
                            return True

                        if self.syncstatus is not None:
                            return True

                        if self.vpnbasicinfo is not None and self.vpnbasicinfo._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_nvo_vpn as meta
                        return meta._meta_table['Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-nvo-vpn:vpnInfo'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.vpn is not None and self.vpn._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_nvo_vpn as meta
                    return meta._meta_table['Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')
                if self.index is None:
                    raise YPYModelError('Key property index is None')

                return self.parent._common_path +'/ietf-nvo-vpn:segVpnList[ietf-nvo-vpn:index = ' + str(self.index) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.index is not None:
                    return True

                if self.vpninfo is not None and self.vpninfo._has_data():
                    return True

                if self.vpnrole is not None:
                    return True

                if self.vpntype is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_nvo_vpn as meta
                return meta._meta_table['Nvovpnmgr.Composedvpns.Segvpnlist']['meta_info']


        class Accesspointlist(object):
            """
            TP list of the access links which associated
            with CE and PE
            
            .. attribute:: id  <key>
            
            	yang\:uuid\-str for TP
            	**type**\:  str
            
            	**pattern:** [0\-9a\-fA\-F]{8}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{12}
            
            .. attribute:: containingmaintpid
            
            	uuid\-str for main interface
            	**type**\:  str
            
            	**pattern:** [0\-9a\-fA\-F]{8}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{12}
            
            .. attribute:: description
            
            	description for this tp
            	**type**\:  str
            
            	**length:** 0..200
            
            .. attribute:: name
            
            	Must abbey to name rule defined in system. Example FE0/0/1, GE1/2/1.1, Eth\-Trunk1.1, etc
            	**type**\:  str
            
            	**length:** 0..200
            
            .. attribute:: neid
            
            	yang\:uuid\-str for NE 
            	**type**\:  str
            
            	**pattern:** [0\-9a\-fA\-F]{8}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{12}
            
            .. attribute:: operstatus
            
            	Operational status
            	**type**\:   :py:class:`OperstatusEnum <ydk.models.ietf.ietf_nvo_common_types.OperstatusEnum>`
            
            .. attribute:: peercetp
            
            	CE TP Information
            	**type**\:   :py:class:`Peercetp <ydk.models.ietf.ietf_nvo_vpn.Nvovpnmgr.Composedvpns.Accesspointlist.Peercetp>`
            
            .. attribute:: routeprotocolspec
            
            	route protocol spec
            	**type**\: list of    :py:class:`Routeprotocolspec <ydk.models.ietf.ietf_nvo_vpn.Nvovpnmgr.Composedvpns.Accesspointlist.Routeprotocolspec>`
            
            .. attribute:: tpbasicinfo
            
            	Tp non\-instance basic info
            	**type**\:   :py:class:`Tpbasicinfo <ydk.models.ietf.ietf_nvo_vpn.Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo>`
            
            

            """

            _prefix = 'VPN'
            _revision = '2016-10-24'

            def __init__(self):
                self.parent = None
                self.id = None
                self.containingmaintpid = None
                self.description = None
                self.name = None
                self.neid = None
                self.operstatus = None
                self.peercetp = Nvovpnmgr.Composedvpns.Accesspointlist.Peercetp()
                self.peercetp.parent = self
                self.routeprotocolspec = YList()
                self.routeprotocolspec.parent = self
                self.routeprotocolspec.name = 'routeprotocolspec'
                self.tpbasicinfo = Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo()
                self.tpbasicinfo.parent = self


            class Tpbasicinfo(object):
                """
                Tp non\-instance basic info
                
                .. attribute:: addtionalinfo
                
                	addtionalInfo
                	**type**\: list of    :py:class:`Addtionalinfo <ydk.models.ietf.ietf_nvo_vpn.Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Addtionalinfo>`
                
                .. attribute:: adminstatus
                
                	administrative status
                	**type**\:   :py:class:`AdminstatusEnum <ydk.models.ietf.ietf_nvo_common_types.AdminstatusEnum>`
                
                .. attribute:: edgepointrole
                
                	edge role for TP, for example\:UNI/NNI 
                	**type**\:   :py:class:`EdgepointroleEnum <ydk.models.ietf.ietf_nvo_common_types.EdgepointroleEnum>`
                
                .. attribute:: flowservices
                
                	flow services in one TP
                	**type**\:   :py:class:`Flowservices <ydk.models.ietf.ietf_nvo_vpn.Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Flowservices>`
                
                .. attribute:: topologyrole
                
                	hub/spoke role, etc
                	**type**\:   :py:class:`ToponoderoleEnum <ydk.models.ietf.ietf_nvo_common_types.ToponoderoleEnum>`
                
                .. attribute:: tpqosnode
                
                	tpQosNode
                	**type**\:   :py:class:`Tpqosnode <ydk.models.ietf.ietf_nvo_vpn.Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Tpqosnode>`
                
                .. attribute:: type
                
                	Type
                	**type**\:   :py:class:`TptypeEnum <ydk.models.ietf.ietf_nvo_common_types.TptypeEnum>`
                
                .. attribute:: typespeclist
                
                	typeSpecList
                	**type**\: list of    :py:class:`Typespeclist <ydk.models.ietf.ietf_nvo_vpn.Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Typespeclist>`
                
                .. attribute:: workinglayer
                
                	working layer
                	**type**\:   :py:class:`LayerrateEnum <ydk.models.ietf.ietf_nvo_common_types.LayerrateEnum>`
                
                

                """

                _prefix = 'VPN'
                _revision = '2016-10-24'

                def __init__(self):
                    self.parent = None
                    self.addtionalinfo = YList()
                    self.addtionalinfo.parent = self
                    self.addtionalinfo.name = 'addtionalinfo'
                    self.adminstatus = None
                    self.edgepointrole = None
                    self.flowservices = Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Flowservices()
                    self.flowservices.parent = self
                    self.topologyrole = None
                    self.tpqosnode = Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Tpqosnode()
                    self.tpqosnode.parent = self
                    self.type = None
                    self.typespeclist = YList()
                    self.typespeclist.parent = self
                    self.typespeclist.name = 'typespeclist'
                    self.workinglayer = None


                class Typespeclist(object):
                    """
                    typeSpecList
                    
                    .. attribute:: layerrate  <key>
                    
                    	layerRate
                    	**type**\:   :py:class:`LayerrateEnum <ydk.models.ietf.ietf_nvo_common_types.LayerrateEnum>`
                    
                    .. attribute:: ethernetspec
                    
                    	ethernetSpec
                    	**type**\:   :py:class:`Ethernetspec <ydk.models.ietf.ietf_nvo_vpn.Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Typespeclist.Ethernetspec>`
                    
                    .. attribute:: ipspec
                    
                    	ipSpec
                    	**type**\:   :py:class:`Ipspec <ydk.models.ietf.ietf_nvo_vpn.Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Typespeclist.Ipspec>`
                    
                    .. attribute:: vxlanspec
                    
                    	vxlanSpec
                    	**type**\:   :py:class:`Vxlanspec <ydk.models.ietf.ietf_nvo_vpn.Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Typespeclist.Vxlanspec>`
                    
                    

                    """

                    _prefix = 'VPN'
                    _revision = '2016-10-24'

                    def __init__(self):
                        self.parent = None
                        self.layerrate = None
                        self.ethernetspec = Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Typespeclist.Ethernetspec()
                        self.ethernetspec.parent = self
                        self.ipspec = Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Typespeclist.Ipspec()
                        self.ipspec.parent = self
                        self.vxlanspec = Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Typespeclist.Vxlanspec()
                        self.vxlanspec.parent = self


                    class Ethernetspec(object):
                        """
                        ethernetSpec
                        
                        .. attribute:: accesstype
                        
                        	access frame type
                        	**type**\:   :py:class:`EthernetencaptypeEnum <ydk.models.ietf.ietf_nvo_common_types.EthernetencaptypeEnum>`
                        
                        .. attribute:: actionvalue
                        
                        	action value
                        	**type**\:  str
                        
                        	**length:** 0..100
                        
                        .. attribute:: dot1q
                        
                        	dot1q
                        	**type**\:   :py:class:`Dot1Q <ydk.models.ietf.ietf_nvo_vpn.Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Typespeclist.Ethernetspec.Dot1Q>`
                        
                        .. attribute:: qinqvlan
                        
                        	qinqVlan
                        	**type**\:   :py:class:`Qinqvlan <ydk.models.ietf.ietf_nvo_vpn.Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Typespeclist.Ethernetspec.Qinqvlan>`
                        
                        .. attribute:: vlanaction
                        
                        	Frame type that can be accepted. not needed now
                        	**type**\:   :py:class:`EthernetactionEnum <ydk.models.ietf.ietf_nvo_common_types.EthernetactionEnum>`
                        
                        

                        """

                        _prefix = 'VPN'
                        _revision = '2016-10-24'

                        def __init__(self):
                            self.parent = None
                            self.accesstype = None
                            self.actionvalue = None
                            self.dot1q = Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Typespeclist.Ethernetspec.Dot1Q()
                            self.dot1q.parent = self
                            self.qinqvlan = Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Typespeclist.Ethernetspec.Qinqvlan()
                            self.qinqvlan.parent = self
                            self.vlanaction = None


                        class Qinqvlan(object):
                            """
                            qinqVlan
                            
                            .. attribute:: cvlanlist
                            
                            	cvlanList
                            	**type**\:  list of int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: svlanlist
                            
                            	svlanList
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'VPN'
                            _revision = '2016-10-24'

                            def __init__(self):
                                self.parent = None
                                self.cvlanlist = YLeafList()
                                self.cvlanlist.parent = self
                                self.cvlanlist.name = 'cvlanlist'
                                self.svlanlist = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/ietf-nvo-vpn:qinqVlan'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.cvlanlist is not None:
                                    for child in self.cvlanlist:
                                        if child is not None:
                                            return True

                                if self.svlanlist is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ietf._meta import _ietf_nvo_vpn as meta
                                return meta._meta_table['Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Typespeclist.Ethernetspec.Qinqvlan']['meta_info']


                        class Dot1Q(object):
                            """
                            dot1q
                            
                            .. attribute:: dot1qvlanlist
                            
                            	dot1qVlanList
                            	**type**\:  list of int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'VPN'
                            _revision = '2016-10-24'

                            def __init__(self):
                                self.parent = None
                                self.dot1qvlanlist = YLeafList()
                                self.dot1qvlanlist.parent = self
                                self.dot1qvlanlist.name = 'dot1qvlanlist'

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/ietf-nvo-vpn:dot1q'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.dot1qvlanlist is not None:
                                    for child in self.dot1qvlanlist:
                                        if child is not None:
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ietf._meta import _ietf_nvo_vpn as meta
                                return meta._meta_table['Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Typespeclist.Ethernetspec.Dot1Q']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/ietf-nvo-vpn:ethernetSpec'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.accesstype is not None:
                                return True

                            if self.actionvalue is not None:
                                return True

                            if self.dot1q is not None and self.dot1q._has_data():
                                return True

                            if self.qinqvlan is not None and self.qinqvlan._has_data():
                                return True

                            if self.vlanaction is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ietf._meta import _ietf_nvo_vpn as meta
                            return meta._meta_table['Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Typespeclist.Ethernetspec']['meta_info']


                    class Ipspec(object):
                        """
                        ipSpec
                        
                        .. attribute:: masterip
                        
                        	master IP address
                        	**type**\:  str
                        
                        .. attribute:: mtu
                        
                        	mtu for ip layer,scope\:46~9600
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'VPN'
                        _revision = '2016-10-24'

                        def __init__(self):
                            self.parent = None
                            self.masterip = None
                            self.mtu = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/ietf-nvo-vpn:ipSpec'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.masterip is not None:
                                return True

                            if self.mtu is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ietf._meta import _ietf_nvo_vpn as meta
                            return meta._meta_table['Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Typespeclist.Ipspec']['meta_info']


                    class Vxlanspec(object):
                        """
                        vxlanSpec
                        
                        .. attribute:: vni
                        
                        	vni
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: vtepip
                        
                        	vtep ip
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'VPN'
                        _revision = '2016-10-24'

                        def __init__(self):
                            self.parent = None
                            self.vni = None
                            self.vtepip = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/ietf-nvo-vpn:vxlanSpec'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.vni is not None:
                                return True

                            if self.vtepip is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ietf._meta import _ietf_nvo_vpn as meta
                            return meta._meta_table['Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Typespeclist.Vxlanspec']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.layerrate is None:
                            raise YPYModelError('Key property layerrate is None')

                        return self.parent._common_path +'/ietf-nvo-vpn:typeSpecList[ietf-nvo-vpn:layerRate = ' + str(self.layerrate) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.layerrate is not None:
                            return True

                        if self.ethernetspec is not None and self.ethernetspec._has_data():
                            return True

                        if self.ipspec is not None and self.ipspec._has_data():
                            return True

                        if self.vxlanspec is not None and self.vxlanspec._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_nvo_vpn as meta
                        return meta._meta_table['Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Typespeclist']['meta_info']


                class Tpqosnode(object):
                    """
                    tpQosNode
                    
                    .. attribute:: inqosprofileid
                    
                    	inQosProfileId
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{8}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{12}
                    
                    .. attribute:: intpcar
                    
                    	inTpCar
                    	**type**\: list of    :py:class:`Intpcar <ydk.models.ietf.ietf_nvo_vpn.Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Tpqosnode.Intpcar>`
                    
                    .. attribute:: outqosprofileid
                    
                    	outQosProfileId
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{8}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{12}
                    
                    .. attribute:: outtpcar
                    
                    	outTpCar
                    	**type**\: list of    :py:class:`Outtpcar <ydk.models.ietf.ietf_nvo_vpn.Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Tpqosnode.Outtpcar>`
                    
                    .. attribute:: qosconfigtype
                    
                    	qosConfigType
                    	**type**\:   :py:class:`QosconfigtypeEnum <ydk.models.ietf.ietf_nvo_qos_types.QosconfigtypeEnum>`
                    
                    .. attribute:: qosdetailtype
                    
                    	qosDetailType
                    	**type**\:   :py:class:`QosdetailtypeEnum <ydk.models.ietf.ietf_nvo_qos_types.QosdetailtypeEnum>`
                    
                    

                    """

                    _prefix = 'VPN'
                    _revision = '2016-10-24'

                    def __init__(self):
                        self.parent = None
                        self.inqosprofileid = None
                        self.intpcar = YList()
                        self.intpcar.parent = self
                        self.intpcar.name = 'intpcar'
                        self.outqosprofileid = None
                        self.outtpcar = YList()
                        self.outtpcar.parent = self
                        self.outtpcar.name = 'outtpcar'
                        self.qosconfigtype = None
                        self.qosdetailtype = None


                    class Intpcar(object):
                        """
                        inTpCar
                        
                        .. attribute:: index  <key>
                        
                        	index
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: action
                        
                        	action
                        	**type**\:  str
                        
                        .. attribute:: actiontype
                        
                        	actionType
                        	**type**\:   :py:class:`ActiontypeEnum <ydk.models.ietf.ietf_nvo_qos_types.ActiontypeEnum>`
                        
                        .. attribute:: datakind
                        
                        	dataKind
                        	**type**\:   :py:class:`DatakindEnum <ydk.models.ietf.ietf_nvo_qos_types.DatakindEnum>`
                        
                        

                        """

                        _prefix = 'VPN'
                        _revision = '2016-10-24'

                        def __init__(self):
                            self.parent = None
                            self.index = None
                            self.action = None
                            self.actiontype = None
                            self.datakind = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.index is None:
                                raise YPYModelError('Key property index is None')

                            return self.parent._common_path +'/ietf-nvo-vpn:inTpCar[ietf-nvo-vpn:index = ' + str(self.index) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.index is not None:
                                return True

                            if self.action is not None:
                                return True

                            if self.actiontype is not None:
                                return True

                            if self.datakind is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ietf._meta import _ietf_nvo_vpn as meta
                            return meta._meta_table['Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Tpqosnode.Intpcar']['meta_info']


                    class Outtpcar(object):
                        """
                        outTpCar
                        
                        .. attribute:: index  <key>
                        
                        	index
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: action
                        
                        	action
                        	**type**\:  str
                        
                        .. attribute:: actiontype
                        
                        	actionType
                        	**type**\:   :py:class:`ActiontypeEnum <ydk.models.ietf.ietf_nvo_qos_types.ActiontypeEnum>`
                        
                        .. attribute:: datakind
                        
                        	dataKind
                        	**type**\:   :py:class:`DatakindEnum <ydk.models.ietf.ietf_nvo_qos_types.DatakindEnum>`
                        
                        

                        """

                        _prefix = 'VPN'
                        _revision = '2016-10-24'

                        def __init__(self):
                            self.parent = None
                            self.index = None
                            self.action = None
                            self.actiontype = None
                            self.datakind = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.index is None:
                                raise YPYModelError('Key property index is None')

                            return self.parent._common_path +'/ietf-nvo-vpn:outTpCar[ietf-nvo-vpn:index = ' + str(self.index) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.index is not None:
                                return True

                            if self.action is not None:
                                return True

                            if self.actiontype is not None:
                                return True

                            if self.datakind is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ietf._meta import _ietf_nvo_vpn as meta
                            return meta._meta_table['Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Tpqosnode.Outtpcar']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/ietf-nvo-vpn:tpQosNode'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.inqosprofileid is not None:
                            return True

                        if self.intpcar is not None:
                            for child_ref in self.intpcar:
                                if child_ref._has_data():
                                    return True

                        if self.outqosprofileid is not None:
                            return True

                        if self.outtpcar is not None:
                            for child_ref in self.outtpcar:
                                if child_ref._has_data():
                                    return True

                        if self.qosconfigtype is not None:
                            return True

                        if self.qosdetailtype is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_nvo_vpn as meta
                        return meta._meta_table['Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Tpqosnode']['meta_info']


                class Flowservices(object):
                    """
                    flow services in one TP
                    
                    .. attribute:: flowqostemplateid
                    
                    	flowQosTemplateID
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{8}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{12}
                    
                    .. attribute:: flowservices
                    
                    	default in flow and behaviors
                    	**type**\: list of    :py:class:`Flowservices_ <ydk.models.ietf.ietf_nvo_vpn.Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Flowservices.Flowservices_>`
                    
                    .. attribute:: inflowqostemplateid
                    
                    	inFlowQosTemplateID
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{8}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{12}
                    
                    .. attribute:: outflowqostemplateid
                    
                    	outFlowQosTemplateID
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{8}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{12}
                    
                    .. attribute:: qosconfigtype
                    
                    	qosConfigType
                    	**type**\:   :py:class:`QosconfigtypeEnum <ydk.models.ietf.ietf_nvo_qos_types.QosconfigtypeEnum>`
                    
                    .. attribute:: qosdetailtype
                    
                    	qosDetailType
                    	**type**\:   :py:class:`QosdetailtypeEnum <ydk.models.ietf.ietf_nvo_qos_types.QosdetailtypeEnum>`
                    
                    

                    """

                    _prefix = 'VPN'
                    _revision = '2016-10-24'

                    def __init__(self):
                        self.parent = None
                        self.flowqostemplateid = None
                        self.flowservices = YList()
                        self.flowservices.parent = self
                        self.flowservices.name = 'flowservices'
                        self.inflowqostemplateid = None
                        self.outflowqostemplateid = None
                        self.qosconfigtype = None
                        self.qosdetailtype = None


                    class Flowservices_(object):
                        """
                        default in flow and behaviors
                        
                        .. attribute:: flowclassifierid  <key>
                        
                        	flowClassifierId
                        	**type**\:  str
                        
                        	**pattern:** [0\-9a\-fA\-F]{8}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{12}
                        
                        .. attribute:: flowbehaviors
                        
                        	flowBehaviors
                        	**type**\: list of    :py:class:`Flowbehaviors <ydk.models.ietf.ietf_nvo_vpn.Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Flowservices.Flowservices_.Flowbehaviors>`
                        
                        

                        """

                        _prefix = 'VPN'
                        _revision = '2016-10-24'

                        def __init__(self):
                            self.parent = None
                            self.flowclassifierid = None
                            self.flowbehaviors = YList()
                            self.flowbehaviors.parent = self
                            self.flowbehaviors.name = 'flowbehaviors'


                        class Flowbehaviors(object):
                            """
                            flowBehaviors
                            
                            .. attribute:: index  <key>
                            
                            	index
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: action
                            
                            	action
                            	**type**\:  str
                            
                            .. attribute:: actiontype
                            
                            	actionType
                            	**type**\:   :py:class:`ActiontypeEnum <ydk.models.ietf.ietf_nvo_qos_types.ActiontypeEnum>`
                            
                            .. attribute:: datakind
                            
                            	dataKind
                            	**type**\:   :py:class:`DatakindEnum <ydk.models.ietf.ietf_nvo_qos_types.DatakindEnum>`
                            
                            

                            """

                            _prefix = 'VPN'
                            _revision = '2016-10-24'

                            def __init__(self):
                                self.parent = None
                                self.index = None
                                self.action = None
                                self.actiontype = None
                                self.datakind = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.index is None:
                                    raise YPYModelError('Key property index is None')

                                return self.parent._common_path +'/ietf-nvo-vpn:flowBehaviors[ietf-nvo-vpn:index = ' + str(self.index) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.index is not None:
                                    return True

                                if self.action is not None:
                                    return True

                                if self.actiontype is not None:
                                    return True

                                if self.datakind is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ietf._meta import _ietf_nvo_vpn as meta
                                return meta._meta_table['Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Flowservices.Flowservices_.Flowbehaviors']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.flowclassifierid is None:
                                raise YPYModelError('Key property flowclassifierid is None')

                            return self.parent._common_path +'/ietf-nvo-vpn:flowServices[ietf-nvo-vpn:flowClassifierId = ' + str(self.flowclassifierid) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.flowclassifierid is not None:
                                return True

                            if self.flowbehaviors is not None:
                                for child_ref in self.flowbehaviors:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ietf._meta import _ietf_nvo_vpn as meta
                            return meta._meta_table['Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Flowservices.Flowservices_']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/ietf-nvo-vpn:flowServices'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.flowqostemplateid is not None:
                            return True

                        if self.flowservices is not None:
                            for child_ref in self.flowservices:
                                if child_ref._has_data():
                                    return True

                        if self.inflowqostemplateid is not None:
                            return True

                        if self.outflowqostemplateid is not None:
                            return True

                        if self.qosconfigtype is not None:
                            return True

                        if self.qosdetailtype is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_nvo_vpn as meta
                        return meta._meta_table['Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Flowservices']['meta_info']


                class Addtionalinfo(object):
                    """
                    addtionalInfo
                    
                    .. attribute:: name  <key>
                    
                    	string name 
                    	**type**\:  str
                    
                    .. attribute:: value
                    
                    	string value
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'VPN'
                    _revision = '2016-10-24'

                    def __init__(self):
                        self.parent = None
                        self.name = None
                        self.value = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.name is None:
                            raise YPYModelError('Key property name is None')

                        return self.parent._common_path +'/ietf-nvo-vpn:addtionalInfo[ietf-nvo-vpn:name = ' + str(self.name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.name is not None:
                            return True

                        if self.value is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_nvo_vpn as meta
                        return meta._meta_table['Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Addtionalinfo']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-nvo-vpn:tpBasicInfo'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.addtionalinfo is not None:
                        for child_ref in self.addtionalinfo:
                            if child_ref._has_data():
                                return True

                    if self.adminstatus is not None:
                        return True

                    if self.edgepointrole is not None:
                        return True

                    if self.flowservices is not None and self.flowservices._has_data():
                        return True

                    if self.topologyrole is not None:
                        return True

                    if self.tpqosnode is not None and self.tpqosnode._has_data():
                        return True

                    if self.type is not None:
                        return True

                    if self.typespeclist is not None:
                        for child_ref in self.typespeclist:
                            if child_ref._has_data():
                                return True

                    if self.workinglayer is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_nvo_vpn as meta
                    return meta._meta_table['Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo']['meta_info']


            class Peercetp(object):
                """
                CE TP Information
                
                .. attribute:: cedirectneid
                
                	direction connected NE ID, only valid in asbr 
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{8}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{12}
                
                .. attribute:: cedirecttpid
                
                	ce Direct TP id, only valid in asbr
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{8}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{12}
                
                .. attribute:: ceid
                
                	Site router ID
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{8}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{12}
                
                .. attribute:: ceifmasterip
                
                	ceIfmasterIp
                	**type**\:  str
                
                .. attribute:: location
                
                	CE device location 
                	**type**\:  str
                
                	**length:** 0..400
                
                

                """

                _prefix = 'VPN'
                _revision = '2016-10-24'

                def __init__(self):
                    self.parent = None
                    self.cedirectneid = None
                    self.cedirecttpid = None
                    self.ceid = None
                    self.ceifmasterip = None
                    self.location = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-nvo-vpn:peerCeTp'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.cedirectneid is not None:
                        return True

                    if self.cedirecttpid is not None:
                        return True

                    if self.ceid is not None:
                        return True

                    if self.ceifmasterip is not None:
                        return True

                    if self.location is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_nvo_vpn as meta
                    return meta._meta_table['Nvovpnmgr.Composedvpns.Accesspointlist.Peercetp']['meta_info']


            class Routeprotocolspec(object):
                """
                route protocol spec
                
                .. attribute:: type  <key>
                
                	Protocol type
                	**type**\:   :py:class:`RouteprotocoltypeEnum <ydk.models.ietf.ietf_nvo_common_types.RouteprotocoltypeEnum>`
                
                .. attribute:: bgpprotocols
                
                	bgpProtocols
                	**type**\: list of    :py:class:`Bgpprotocols <ydk.models.ietf.ietf_nvo_vpn.Nvovpnmgr.Composedvpns.Accesspointlist.Routeprotocolspec.Bgpprotocols>`
                
                .. attribute:: staticrouteitems
                
                	staticRouteItems
                	**type**\: list of    :py:class:`Staticrouteitems <ydk.models.ietf.ietf_nvo_vpn.Nvovpnmgr.Composedvpns.Accesspointlist.Routeprotocolspec.Staticrouteitems>`
                
                

                """

                _prefix = 'VPN'
                _revision = '2016-10-24'

                def __init__(self):
                    self.parent = None
                    self.type = None
                    self.bgpprotocols = YList()
                    self.bgpprotocols.parent = self
                    self.bgpprotocols.name = 'bgpprotocols'
                    self.staticrouteitems = YList()
                    self.staticrouteitems.parent = self
                    self.staticrouteitems.name = 'staticrouteitems'


                class Staticrouteitems(object):
                    """
                    staticRouteItems
                    
                    .. attribute:: index  <key>
                    
                    	static item index
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: destinationcidr
                    
                    	destination ip cidr. 
                    	**type**\:  str
                    
                    .. attribute:: egresstp
                    
                    	egress tp
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{8}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{12}
                    
                    .. attribute:: nexthopip
                    
                    	nextHopIp
                    	**type**\:  str
                    
                    	**length:** 0..200
                    
                    .. attribute:: routepreference
                    
                    	route priority. Ordinary, work route have higher priority
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'VPN'
                    _revision = '2016-10-24'

                    def __init__(self):
                        self.parent = None
                        self.index = None
                        self.destinationcidr = None
                        self.egresstp = None
                        self.nexthopip = None
                        self.routepreference = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.index is None:
                            raise YPYModelError('Key property index is None')

                        return self.parent._common_path +'/ietf-nvo-vpn:staticRouteItems[ietf-nvo-vpn:index = ' + str(self.index) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.index is not None:
                            return True

                        if self.destinationcidr is not None:
                            return True

                        if self.egresstp is not None:
                            return True

                        if self.nexthopip is not None:
                            return True

                        if self.routepreference is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_nvo_vpn as meta
                        return meta._meta_table['Nvovpnmgr.Composedvpns.Accesspointlist.Routeprotocolspec.Staticrouteitems']['meta_info']


                class Bgpprotocols(object):
                    """
                    bgpProtocols
                    
                    .. attribute:: index  <key>
                    
                    	index of BGP protocol item
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: bgpmaxprefix
                    
                    	
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: bgpmaxprefixalarm
                    
                    	alarm threshold of BGP rout
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: peerasnumber
                    
                    	
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: peerip
                    
                    	peerIp
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'VPN'
                    _revision = '2016-10-24'

                    def __init__(self):
                        self.parent = None
                        self.index = None
                        self.bgpmaxprefix = None
                        self.bgpmaxprefixalarm = None
                        self.peerasnumber = None
                        self.peerip = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.index is None:
                            raise YPYModelError('Key property index is None')

                        return self.parent._common_path +'/ietf-nvo-vpn:bgpProtocols[ietf-nvo-vpn:index = ' + str(self.index) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.index is not None:
                            return True

                        if self.bgpmaxprefix is not None:
                            return True

                        if self.bgpmaxprefixalarm is not None:
                            return True

                        if self.peerasnumber is not None:
                            return True

                        if self.peerip is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_nvo_vpn as meta
                        return meta._meta_table['Nvovpnmgr.Composedvpns.Accesspointlist.Routeprotocolspec.Bgpprotocols']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.type is None:
                        raise YPYModelError('Key property type is None')

                    return self.parent._common_path +'/ietf-nvo-vpn:routeProtocolSpec[ietf-nvo-vpn:type = ' + str(self.type) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.type is not None:
                        return True

                    if self.bgpprotocols is not None:
                        for child_ref in self.bgpprotocols:
                            if child_ref._has_data():
                                return True

                    if self.staticrouteitems is not None:
                        for child_ref in self.staticrouteitems:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_nvo_vpn as meta
                    return meta._meta_table['Nvovpnmgr.Composedvpns.Accesspointlist.Routeprotocolspec']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')
                if self.id is None:
                    raise YPYModelError('Key property id is None')

                return self.parent._common_path +'/ietf-nvo-vpn:accessPointList[ietf-nvo-vpn:id = ' + str(self.id) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.id is not None:
                    return True

                if self.containingmaintpid is not None:
                    return True

                if self.description is not None:
                    return True

                if self.name is not None:
                    return True

                if self.neid is not None:
                    return True

                if self.operstatus is not None:
                    return True

                if self.peercetp is not None and self.peercetp._has_data():
                    return True

                if self.routeprotocolspec is not None:
                    for child_ref in self.routeprotocolspec:
                        if child_ref._has_data():
                            return True

                if self.tpbasicinfo is not None and self.tpbasicinfo._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_nvo_vpn as meta
                return meta._meta_table['Nvovpnmgr.Composedvpns.Accesspointlist']['meta_info']

        @property
        def _common_path(self):
            if self.id is None:
                raise YPYModelError('Key property id is None')

            return '/ietf-nvo-vpn:nvoVPNMgr/ietf-nvo-vpn:composedVPNs[ietf-nvo-vpn:id = ' + str(self.id) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.id is not None:
                return True

            if self.accesspointlist is not None:
                for child_ref in self.accesspointlist:
                    if child_ref._has_data():
                        return True

            if self.businesstypeid is not None:
                return True

            if self.description is not None:
                return True

            if self.name is not None:
                return True

            if self.operstatus is not None:
                return True

            if self.segvpnlist is not None:
                for child_ref in self.segvpnlist:
                    if child_ref._has_data():
                        return True

            if self.starttime is not None:
                return True

            if self.syncstatus is not None:
                return True

            if self.tenantid is not None:
                return True

            if self.vpnbasicinfo is not None and self.vpnbasicinfo._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_nvo_vpn as meta
            return meta._meta_table['Nvovpnmgr.Composedvpns']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-nvo-vpn:nvoVPNMgr'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.composedvpns is not None:
            for child_ref in self.composedvpns:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_nvo_vpn as meta
        return meta._meta_table['Nvovpnmgr']['meta_info']


