""" ietf_nvo_tp 

This module contains a collection of YANG definitions
for tp

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class Nvotpmgr(object):
    """
    nvo tp management
    
    .. attribute:: tps
    
    	tp retrieve functions
    	**type**\: list of    :py:class:`Tps <ydk.models.ietf.ietf_nvo_tp.Nvotpmgr.Tps>`
    
    

    """

    _prefix = 'TP'
    _revision = '2016-10-24'

    def __init__(self):
        self.tps = YList()
        self.tps.parent = self
        self.tps.name = 'tps'


    class Tps(object):
        """
        tp retrieve functions
        
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
        	**type**\:   :py:class:`Peercetp <ydk.models.ietf.ietf_nvo_tp.Nvotpmgr.Tps.Peercetp>`
        
        .. attribute:: routeprotocolspec
        
        	route protocol spec
        	**type**\: list of    :py:class:`Routeprotocolspec <ydk.models.ietf.ietf_nvo_tp.Nvotpmgr.Tps.Routeprotocolspec>`
        
        .. attribute:: tpbasicinfo
        
        	Tp non\-instance basic info
        	**type**\:   :py:class:`Tpbasicinfo <ydk.models.ietf.ietf_nvo_tp.Nvotpmgr.Tps.Tpbasicinfo>`
        
        

        """

        _prefix = 'TP'
        _revision = '2016-10-24'

        def __init__(self):
            self.parent = None
            self.id = None
            self.containingmaintpid = None
            self.description = None
            self.name = None
            self.neid = None
            self.operstatus = None
            self.peercetp = Nvotpmgr.Tps.Peercetp()
            self.peercetp.parent = self
            self.routeprotocolspec = YList()
            self.routeprotocolspec.parent = self
            self.routeprotocolspec.name = 'routeprotocolspec'
            self.tpbasicinfo = Nvotpmgr.Tps.Tpbasicinfo()
            self.tpbasicinfo.parent = self


        class Tpbasicinfo(object):
            """
            Tp non\-instance basic info
            
            .. attribute:: addtionalinfo
            
            	addtionalInfo
            	**type**\: list of    :py:class:`Addtionalinfo <ydk.models.ietf.ietf_nvo_tp.Nvotpmgr.Tps.Tpbasicinfo.Addtionalinfo>`
            
            .. attribute:: adminstatus
            
            	administrative status
            	**type**\:   :py:class:`AdminstatusEnum <ydk.models.ietf.ietf_nvo_common_types.AdminstatusEnum>`
            
            .. attribute:: edgepointrole
            
            	edge role for TP, for example\:UNI/NNI 
            	**type**\:   :py:class:`EdgepointroleEnum <ydk.models.ietf.ietf_nvo_common_types.EdgepointroleEnum>`
            
            .. attribute:: flowservices
            
            	flow services in one TP
            	**type**\:   :py:class:`Flowservices <ydk.models.ietf.ietf_nvo_tp.Nvotpmgr.Tps.Tpbasicinfo.Flowservices>`
            
            .. attribute:: topologyrole
            
            	hub/spoke role, etc
            	**type**\:   :py:class:`ToponoderoleEnum <ydk.models.ietf.ietf_nvo_common_types.ToponoderoleEnum>`
            
            .. attribute:: tpqosnode
            
            	tpQosNode
            	**type**\:   :py:class:`Tpqosnode <ydk.models.ietf.ietf_nvo_tp.Nvotpmgr.Tps.Tpbasicinfo.Tpqosnode>`
            
            .. attribute:: type
            
            	Type
            	**type**\:   :py:class:`TptypeEnum <ydk.models.ietf.ietf_nvo_common_types.TptypeEnum>`
            
            .. attribute:: typespeclist
            
            	typeSpecList
            	**type**\: list of    :py:class:`Typespeclist <ydk.models.ietf.ietf_nvo_tp.Nvotpmgr.Tps.Tpbasicinfo.Typespeclist>`
            
            .. attribute:: workinglayer
            
            	working layer
            	**type**\:   :py:class:`LayerrateEnum <ydk.models.ietf.ietf_nvo_common_types.LayerrateEnum>`
            
            

            """

            _prefix = 'TP'
            _revision = '2016-10-24'

            def __init__(self):
                self.parent = None
                self.addtionalinfo = YList()
                self.addtionalinfo.parent = self
                self.addtionalinfo.name = 'addtionalinfo'
                self.adminstatus = None
                self.edgepointrole = None
                self.flowservices = Nvotpmgr.Tps.Tpbasicinfo.Flowservices()
                self.flowservices.parent = self
                self.topologyrole = None
                self.tpqosnode = Nvotpmgr.Tps.Tpbasicinfo.Tpqosnode()
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
                	**type**\:   :py:class:`Ethernetspec <ydk.models.ietf.ietf_nvo_tp.Nvotpmgr.Tps.Tpbasicinfo.Typespeclist.Ethernetspec>`
                
                .. attribute:: ipspec
                
                	ipSpec
                	**type**\:   :py:class:`Ipspec <ydk.models.ietf.ietf_nvo_tp.Nvotpmgr.Tps.Tpbasicinfo.Typespeclist.Ipspec>`
                
                .. attribute:: vxlanspec
                
                	vxlanSpec
                	**type**\:   :py:class:`Vxlanspec <ydk.models.ietf.ietf_nvo_tp.Nvotpmgr.Tps.Tpbasicinfo.Typespeclist.Vxlanspec>`
                
                

                """

                _prefix = 'TP'
                _revision = '2016-10-24'

                def __init__(self):
                    self.parent = None
                    self.layerrate = None
                    self.ethernetspec = Nvotpmgr.Tps.Tpbasicinfo.Typespeclist.Ethernetspec()
                    self.ethernetspec.parent = self
                    self.ipspec = Nvotpmgr.Tps.Tpbasicinfo.Typespeclist.Ipspec()
                    self.ipspec.parent = self
                    self.vxlanspec = Nvotpmgr.Tps.Tpbasicinfo.Typespeclist.Vxlanspec()
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
                    	**type**\:   :py:class:`Dot1Q <ydk.models.ietf.ietf_nvo_tp.Nvotpmgr.Tps.Tpbasicinfo.Typespeclist.Ethernetspec.Dot1Q>`
                    
                    .. attribute:: qinqvlan
                    
                    	qinqVlan
                    	**type**\:   :py:class:`Qinqvlan <ydk.models.ietf.ietf_nvo_tp.Nvotpmgr.Tps.Tpbasicinfo.Typespeclist.Ethernetspec.Qinqvlan>`
                    
                    .. attribute:: vlanaction
                    
                    	Frame type that can be accepted. not needed now
                    	**type**\:   :py:class:`EthernetactionEnum <ydk.models.ietf.ietf_nvo_common_types.EthernetactionEnum>`
                    
                    

                    """

                    _prefix = 'TP'
                    _revision = '2016-10-24'

                    def __init__(self):
                        self.parent = None
                        self.accesstype = None
                        self.actionvalue = None
                        self.dot1q = Nvotpmgr.Tps.Tpbasicinfo.Typespeclist.Ethernetspec.Dot1Q()
                        self.dot1q.parent = self
                        self.qinqvlan = Nvotpmgr.Tps.Tpbasicinfo.Typespeclist.Ethernetspec.Qinqvlan()
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

                        _prefix = 'TP'
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

                            return self.parent._common_path +'/ietf-nvo-tp:qinqVlan'

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
                            from ydk.models.ietf._meta import _ietf_nvo_tp as meta
                            return meta._meta_table['Nvotpmgr.Tps.Tpbasicinfo.Typespeclist.Ethernetspec.Qinqvlan']['meta_info']


                    class Dot1Q(object):
                        """
                        dot1q
                        
                        .. attribute:: dot1qvlanlist
                        
                        	dot1qVlanList
                        	**type**\:  list of int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'TP'
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

                            return self.parent._common_path +'/ietf-nvo-tp:dot1q'

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
                            from ydk.models.ietf._meta import _ietf_nvo_tp as meta
                            return meta._meta_table['Nvotpmgr.Tps.Tpbasicinfo.Typespeclist.Ethernetspec.Dot1Q']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/ietf-nvo-tp:ethernetSpec'

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
                        from ydk.models.ietf._meta import _ietf_nvo_tp as meta
                        return meta._meta_table['Nvotpmgr.Tps.Tpbasicinfo.Typespeclist.Ethernetspec']['meta_info']


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

                    _prefix = 'TP'
                    _revision = '2016-10-24'

                    def __init__(self):
                        self.parent = None
                        self.masterip = None
                        self.mtu = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/ietf-nvo-tp:ipSpec'

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
                        from ydk.models.ietf._meta import _ietf_nvo_tp as meta
                        return meta._meta_table['Nvotpmgr.Tps.Tpbasicinfo.Typespeclist.Ipspec']['meta_info']


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

                    _prefix = 'TP'
                    _revision = '2016-10-24'

                    def __init__(self):
                        self.parent = None
                        self.vni = None
                        self.vtepip = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/ietf-nvo-tp:vxlanSpec'

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
                        from ydk.models.ietf._meta import _ietf_nvo_tp as meta
                        return meta._meta_table['Nvotpmgr.Tps.Tpbasicinfo.Typespeclist.Vxlanspec']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.layerrate is None:
                        raise YPYModelError('Key property layerrate is None')

                    return self.parent._common_path +'/ietf-nvo-tp:typeSpecList[ietf-nvo-tp:layerRate = ' + str(self.layerrate) + ']'

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
                    from ydk.models.ietf._meta import _ietf_nvo_tp as meta
                    return meta._meta_table['Nvotpmgr.Tps.Tpbasicinfo.Typespeclist']['meta_info']


            class Tpqosnode(object):
                """
                tpQosNode
                
                .. attribute:: inqosprofileid
                
                	inQosProfileId
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{8}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{12}
                
                .. attribute:: intpcar
                
                	inTpCar
                	**type**\: list of    :py:class:`Intpcar <ydk.models.ietf.ietf_nvo_tp.Nvotpmgr.Tps.Tpbasicinfo.Tpqosnode.Intpcar>`
                
                .. attribute:: outqosprofileid
                
                	outQosProfileId
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{8}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{12}
                
                .. attribute:: outtpcar
                
                	outTpCar
                	**type**\: list of    :py:class:`Outtpcar <ydk.models.ietf.ietf_nvo_tp.Nvotpmgr.Tps.Tpbasicinfo.Tpqosnode.Outtpcar>`
                
                .. attribute:: qosconfigtype
                
                	qosConfigType
                	**type**\:   :py:class:`QosconfigtypeEnum <ydk.models.ietf.ietf_nvo_qos_types.QosconfigtypeEnum>`
                
                .. attribute:: qosdetailtype
                
                	qosDetailType
                	**type**\:   :py:class:`QosdetailtypeEnum <ydk.models.ietf.ietf_nvo_qos_types.QosdetailtypeEnum>`
                
                

                """

                _prefix = 'TP'
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

                    _prefix = 'TP'
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

                        return self.parent._common_path +'/ietf-nvo-tp:inTpCar[ietf-nvo-tp:index = ' + str(self.index) + ']'

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
                        from ydk.models.ietf._meta import _ietf_nvo_tp as meta
                        return meta._meta_table['Nvotpmgr.Tps.Tpbasicinfo.Tpqosnode.Intpcar']['meta_info']


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

                    _prefix = 'TP'
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

                        return self.parent._common_path +'/ietf-nvo-tp:outTpCar[ietf-nvo-tp:index = ' + str(self.index) + ']'

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
                        from ydk.models.ietf._meta import _ietf_nvo_tp as meta
                        return meta._meta_table['Nvotpmgr.Tps.Tpbasicinfo.Tpqosnode.Outtpcar']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-nvo-tp:tpQosNode'

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
                    from ydk.models.ietf._meta import _ietf_nvo_tp as meta
                    return meta._meta_table['Nvotpmgr.Tps.Tpbasicinfo.Tpqosnode']['meta_info']


            class Flowservices(object):
                """
                flow services in one TP
                
                .. attribute:: flowqostemplateid
                
                	flowQosTemplateID
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{8}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{12}
                
                .. attribute:: flowservices
                
                	default in flow and behaviors
                	**type**\: list of    :py:class:`Flowservices_ <ydk.models.ietf.ietf_nvo_tp.Nvotpmgr.Tps.Tpbasicinfo.Flowservices.Flowservices_>`
                
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

                _prefix = 'TP'
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
                    	**type**\: list of    :py:class:`Flowbehaviors <ydk.models.ietf.ietf_nvo_tp.Nvotpmgr.Tps.Tpbasicinfo.Flowservices.Flowservices_.Flowbehaviors>`
                    
                    

                    """

                    _prefix = 'TP'
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

                        _prefix = 'TP'
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

                            return self.parent._common_path +'/ietf-nvo-tp:flowBehaviors[ietf-nvo-tp:index = ' + str(self.index) + ']'

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
                            from ydk.models.ietf._meta import _ietf_nvo_tp as meta
                            return meta._meta_table['Nvotpmgr.Tps.Tpbasicinfo.Flowservices.Flowservices_.Flowbehaviors']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.flowclassifierid is None:
                            raise YPYModelError('Key property flowclassifierid is None')

                        return self.parent._common_path +'/ietf-nvo-tp:flowServices[ietf-nvo-tp:flowClassifierId = ' + str(self.flowclassifierid) + ']'

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
                        from ydk.models.ietf._meta import _ietf_nvo_tp as meta
                        return meta._meta_table['Nvotpmgr.Tps.Tpbasicinfo.Flowservices.Flowservices_']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-nvo-tp:flowServices'

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
                    from ydk.models.ietf._meta import _ietf_nvo_tp as meta
                    return meta._meta_table['Nvotpmgr.Tps.Tpbasicinfo.Flowservices']['meta_info']


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

                _prefix = 'TP'
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

                    return self.parent._common_path +'/ietf-nvo-tp:addtionalInfo[ietf-nvo-tp:name = ' + str(self.name) + ']'

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
                    from ydk.models.ietf._meta import _ietf_nvo_tp as meta
                    return meta._meta_table['Nvotpmgr.Tps.Tpbasicinfo.Addtionalinfo']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/ietf-nvo-tp:tpBasicInfo'

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
                from ydk.models.ietf._meta import _ietf_nvo_tp as meta
                return meta._meta_table['Nvotpmgr.Tps.Tpbasicinfo']['meta_info']


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

            _prefix = 'TP'
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

                return self.parent._common_path +'/ietf-nvo-tp:peerCeTp'

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
                from ydk.models.ietf._meta import _ietf_nvo_tp as meta
                return meta._meta_table['Nvotpmgr.Tps.Peercetp']['meta_info']


        class Routeprotocolspec(object):
            """
            route protocol spec
            
            .. attribute:: type  <key>
            
            	Protocol type
            	**type**\:   :py:class:`RouteprotocoltypeEnum <ydk.models.ietf.ietf_nvo_common_types.RouteprotocoltypeEnum>`
            
            .. attribute:: bgpprotocols
            
            	bgpProtocols
            	**type**\: list of    :py:class:`Bgpprotocols <ydk.models.ietf.ietf_nvo_tp.Nvotpmgr.Tps.Routeprotocolspec.Bgpprotocols>`
            
            .. attribute:: staticrouteitems
            
            	staticRouteItems
            	**type**\: list of    :py:class:`Staticrouteitems <ydk.models.ietf.ietf_nvo_tp.Nvotpmgr.Tps.Routeprotocolspec.Staticrouteitems>`
            
            

            """

            _prefix = 'TP'
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

                _prefix = 'TP'
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

                    return self.parent._common_path +'/ietf-nvo-tp:staticRouteItems[ietf-nvo-tp:index = ' + str(self.index) + ']'

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
                    from ydk.models.ietf._meta import _ietf_nvo_tp as meta
                    return meta._meta_table['Nvotpmgr.Tps.Routeprotocolspec.Staticrouteitems']['meta_info']


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

                _prefix = 'TP'
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

                    return self.parent._common_path +'/ietf-nvo-tp:bgpProtocols[ietf-nvo-tp:index = ' + str(self.index) + ']'

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
                    from ydk.models.ietf._meta import _ietf_nvo_tp as meta
                    return meta._meta_table['Nvotpmgr.Tps.Routeprotocolspec.Bgpprotocols']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')
                if self.type is None:
                    raise YPYModelError('Key property type is None')

                return self.parent._common_path +'/ietf-nvo-tp:routeProtocolSpec[ietf-nvo-tp:type = ' + str(self.type) + ']'

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
                from ydk.models.ietf._meta import _ietf_nvo_tp as meta
                return meta._meta_table['Nvotpmgr.Tps.Routeprotocolspec']['meta_info']

        @property
        def _common_path(self):
            if self.id is None:
                raise YPYModelError('Key property id is None')

            return '/ietf-nvo-tp:nvoTPMgr/ietf-nvo-tp:tps[ietf-nvo-tp:id = ' + str(self.id) + ']'

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
            from ydk.models.ietf._meta import _ietf_nvo_tp as meta
            return meta._meta_table['Nvotpmgr.Tps']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-nvo-tp:nvoTPMgr'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.tps is not None:
            for child_ref in self.tps:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_nvo_tp as meta
        return meta._meta_table['Nvotpmgr']['meta_info']


