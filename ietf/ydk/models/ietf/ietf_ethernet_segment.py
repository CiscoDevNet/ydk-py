""" ietf_ethernet_segment 

ethernet segment

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class StatusTypeEnum(Enum):
    """
    StatusTypeEnum

    status type

    .. data:: up = 0

    	Status is up

    .. data:: down = 1

    	Status is down

    """

    up = 0

    down = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_ethernet_segment as meta
        return meta._meta_table['StatusTypeEnum']



class EthernetSegments(object):
    """
    ethernet\-segment
    
    .. attribute:: ethernet_segment
    
    	An ethernet segment
    	**type**\: list of    :py:class:`EthernetSegment <ydk.models.ietf.ietf_ethernet_segment.EthernetSegments.EthernetSegment>`
    
    

    """

    _prefix = 'es'
    _revision = '2017-03-13'

    def __init__(self):
        self.ethernet_segment = YList()
        self.ethernet_segment.parent = self
        self.ethernet_segment.name = 'ethernet_segment'


    class EthernetSegment(object):
        """
        An ethernet segment
        
        .. attribute:: name  <key>
        
        	Name of the ethernet segment
        	**type**\:  str
        
        .. attribute:: ac
        
        	Eventual reference to standard attachment circuit definition
        	**type**\:  str
        
        .. attribute:: all_active_mode
        
        	all\-active\-mode
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: bgp_parameters
        
        	BGP parameters
        	**type**\:   :py:class:`BgpParameters <ydk.models.ietf.ietf_ethernet_segment.EthernetSegments.EthernetSegment.BgpParameters>`
        
        .. attribute:: df_election
        
        	df\-election
        	**type**\:   :py:class:`DfElection <ydk.models.ietf.ietf_ethernet_segment.EthernetSegments.EthernetSegment.DfElection>`
        
        .. attribute:: ead_evi_route
        
        	Enable (true) or disable (false) ead\-evi\-route
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: ethernet_segment_identifier
        
        	Ethernet segment identifier (esi)
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: pbb_parameters
        
        	PBB configuration
        	**type**\:   :py:class:`PbbParameters <ydk.models.ietf.ietf_ethernet_segment.EthernetSegments.EthernetSegment.PbbParameters>`
        
        .. attribute:: pw
        
        	Eventual reference to standard pseudowire definition
        	**type**\:  str
        
        .. attribute:: single_active_mode
        
        	single\-active\-mode
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'es'
        _revision = '2017-03-13'

        def __init__(self):
            self.parent = None
            self.name = None
            self.ac = None
            self.all_active_mode = None
            self.bgp_parameters = EthernetSegments.EthernetSegment.BgpParameters()
            self.bgp_parameters.parent = self
            self.df_election = EthernetSegments.EthernetSegment.DfElection()
            self.df_election.parent = self
            self.ead_evi_route = None
            self.ethernet_segment_identifier = None
            self.pbb_parameters = EthernetSegments.EthernetSegment.PbbParameters()
            self.pbb_parameters.parent = self
            self.pw = None
            self.single_active_mode = None


        class PbbParameters(object):
            """
            PBB configuration
            
            .. attribute:: backbone_src_mac
            
            	backbone\-src\-mac, only if this is a PBB
            	**type**\:  str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            

            """

            _prefix = 'es'
            _revision = '2017-03-13'

            def __init__(self):
                self.parent = None
                self.backbone_src_mac = None

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/ietf-ethernet-segment:pbb-parameters'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.backbone_src_mac is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_ethernet_segment as meta
                return meta._meta_table['EthernetSegments.EthernetSegment.PbbParameters']['meta_info']


        class BgpParameters(object):
            """
            BGP parameters
            
            .. attribute:: common
            
            	BGP parameters common to all pseudowires
            	**type**\:   :py:class:`Common <ydk.models.ietf.ietf_ethernet_segment.EthernetSegments.EthernetSegment.BgpParameters.Common>`
            
            

            """

            _prefix = 'es'
            _revision = '2017-03-13'

            def __init__(self):
                self.parent = None
                self.common = EthernetSegments.EthernetSegment.BgpParameters.Common()
                self.common.parent = self


            class Common(object):
                """
                BGP parameters common to all pseudowires
                
                .. attribute:: rd_rt
                
                	A list of route distinguishers and corresponding VPN route targets
                	**type**\: list of    :py:class:`RdRt <ydk.models.ietf.ietf_ethernet_segment.EthernetSegments.EthernetSegment.BgpParameters.Common.RdRt>`
                
                

                """

                _prefix = 'es'
                _revision = '2017-03-13'

                def __init__(self):
                    self.parent = None
                    self.rd_rt = YList()
                    self.rd_rt.parent = self
                    self.rd_rt.name = 'rd_rt'


                class RdRt(object):
                    """
                    A list of route distinguishers and corresponding VPN route targets
                    
                    .. attribute:: route_distinguisher  <key>
                    
                    	Route distinguisher
                    	**type**\:  str
                    
                    	**pattern:** (0\:(6553[0\-5]\|655[0\-2]\\d\|65[0\-4]\\d{2}\|6[0\-4]\\d{3}\|[0\-5]?\\d{0,3}\\d)\:(429496729[0\-5]\|42949672[0\-8]\\d\|4294967[01]\\d{2}\|429496[0\-6]\\d{3}\|42949[0\-5]\\d{4}\|4294[0\-8]\\d{5}\|429[0\-3]\\d{6}\|42[0\-8]\\d{7}\|4[01]\\d{8}\|[0\-3]?\\d{0,8}\\d))\|(1\:(((\\d\|[1\-9]\\d\|1\\d{2}\|2[0\-4]\\d\|25[0\-5])\\.){3}(\\d\|[1\-9]\\d\|1\\d{2}\|2[0\-4]\\d\|25[0\-5]))\:(6553[0\-5]\|655[0\-2]\\d\|65[0\-4]\\d{2}\|6[0\-4]\\d{3}\|[0\-5]?\\d{0,3}\\d))\|(2\:(429496729[0\-5]\|42949672[0\-8]\\d\|4294967[01]\\d{2}\|429496[0\-6]\\d{3}\|42949[0\-5]\\d{4}\|4294[0\-8]\\d{5}\|429[0\-3]\\d{6}\|42[0\-8]\\d{7}\|4[01]\\d{8}\|[0\-3]?\\d{0,8}\\d)\:(6553[0\-5]\|655[0\-2]\\d\|65[0\-4]\\d{2}\|6[0\-4]\\d{3}\|[0\-5]?\\d{0,3}\\d))\|(([3\-9a\-fA\-F]\|[1\-9a\-fA\-F][\\da\-fA\-F]{1,3})\:[\\da\-fA\-F]{1,12})
                    
                    .. attribute:: vpn_target
                    
                    	List of Route Targets
                    	**type**\: list of    :py:class:`VpnTarget <ydk.models.ietf.ietf_ethernet_segment.EthernetSegments.EthernetSegment.BgpParameters.Common.RdRt.VpnTarget>`
                    
                    

                    """

                    _prefix = 'es'
                    _revision = '2017-03-13'

                    def __init__(self):
                        self.parent = None
                        self.route_distinguisher = None
                        self.vpn_target = YList()
                        self.vpn_target.parent = self
                        self.vpn_target.name = 'vpn_target'


                    class VpnTarget(object):
                        """
                        List of Route Targets.
                        
                        .. attribute:: route_target  <key>
                        
                        	Route Target value
                        	**type**\:  str
                        
                        	**pattern:** (0\:(6553[0\-5]\|655[0\-2]\\d\|65[0\-4]\\d{2}\|6[0\-4]\\d{3}\|[0\-5]?\\d{0,3}\\d)\:(429496729[0\-5]\|42949672[0\-8]\\d\|4294967[01]\\d{2}\|429496[0\-6]\\d{3}\|42949[0\-5]\\d{4}\|4294[0\-8]\\d{5}\|429[0\-3]\\d{6}\|42[0\-8]\\d{7}\|4[01]\\d{8}\|[0\-3]?\\d{0,8}\\d))\|(1\:(((\\d\|[1\-9]\\d\|1\\d{2}\|2[0\-4]\\d\|25[0\-5])\\.){3}(\\d\|[1\-9]\\d\|1\\d{2}\|2[0\-4]\\d\|25[0\-5]))\:(6553[0\-5]\|655[0\-2]\\d\|65[0\-4]\\d{2}\|6[0\-4]\\d{3}\|[0\-5]?\\d{0,3}\\d))\|(2\:(429496729[0\-5]\|42949672[0\-8]\\d\|4294967[01]\\d{2}\|429496[0\-6]\\d{3}\|42949[0\-5]\\d{4}\|4294[0\-8]\\d{5}\|429[0\-3]\\d{6}\|42[0\-8]\\d{7}\|4[01]\\d{8}\|[0\-3]?\\d{0,8}\\d)\:(6553[0\-5]\|655[0\-2]\\d\|65[0\-4]\\d{2}\|6[0\-4]\\d{3}\|[0\-5]?\\d{0,3}\\d))
                        
                        .. attribute:: route_target_type
                        
                        	Import/export type of the Route Target
                        	**type**\:   :py:class:`RouteTargetTypeEnum <ydk.models.ietf.ietf_routing_types.RouteTargetTypeEnum>`
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'es'
                        _revision = '2017-03-13'

                        def __init__(self):
                            self.parent = None
                            self.route_target = None
                            self.route_target_type = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.route_target is None:
                                raise YPYModelError('Key property route_target is None')

                            return self.parent._common_path +'/ietf-ethernet-segment:vpn-target[ietf-ethernet-segment:route-target = ' + str(self.route_target) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.route_target is not None:
                                return True

                            if self.route_target_type is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ietf._meta import _ietf_ethernet_segment as meta
                            return meta._meta_table['EthernetSegments.EthernetSegment.BgpParameters.Common.RdRt.VpnTarget']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.route_distinguisher is None:
                            raise YPYModelError('Key property route_distinguisher is None')

                        return self.parent._common_path +'/ietf-ethernet-segment:rd-rt[ietf-ethernet-segment:route-distinguisher = ' + str(self.route_distinguisher) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.route_distinguisher is not None:
                            return True

                        if self.vpn_target is not None:
                            for child_ref in self.vpn_target:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_ethernet_segment as meta
                        return meta._meta_table['EthernetSegments.EthernetSegment.BgpParameters.Common.RdRt']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-ethernet-segment:common'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.rd_rt is not None:
                        for child_ref in self.rd_rt:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_ethernet_segment as meta
                    return meta._meta_table['EthernetSegments.EthernetSegment.BgpParameters.Common']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/ietf-ethernet-segment:bgp-parameters'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.common is not None and self.common._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_ethernet_segment as meta
                return meta._meta_table['EthernetSegments.EthernetSegment.BgpParameters']['meta_info']


        class DfElection(object):
            """
            df\-election
            
            .. attribute:: election_wait_time
            
            	election\-wait\-time
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: hrw
            
            	Enable (TRUE) or disable (FALSE) highest random weight
            	**type**\:  bool
            
            

            """

            _prefix = 'es'
            _revision = '2017-03-13'

            def __init__(self):
                self.parent = None
                self.election_wait_time = None
                self.hrw = None

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/ietf-ethernet-segment:df-election'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.election_wait_time is not None:
                    return True

                if self.hrw is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_ethernet_segment as meta
                return meta._meta_table['EthernetSegments.EthernetSegment.DfElection']['meta_info']

        @property
        def _common_path(self):
            if self.name is None:
                raise YPYModelError('Key property name is None')

            return '/ietf-ethernet-segment:ethernet-segments/ietf-ethernet-segment:ethernet-segment[ietf-ethernet-segment:name = ' + str(self.name) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.name is not None:
                return True

            if self.ac is not None:
                return True

            if self.all_active_mode is not None:
                return True

            if self.bgp_parameters is not None and self.bgp_parameters._has_data():
                return True

            if self.df_election is not None and self.df_election._has_data():
                return True

            if self.ead_evi_route is not None:
                return True

            if self.ethernet_segment_identifier is not None:
                return True

            if self.pbb_parameters is not None and self.pbb_parameters._has_data():
                return True

            if self.pw is not None:
                return True

            if self.single_active_mode is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_ethernet_segment as meta
            return meta._meta_table['EthernetSegments.EthernetSegment']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-ethernet-segment:ethernet-segments'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.ethernet_segment is not None:
            for child_ref in self.ethernet_segment:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_ethernet_segment as meta
        return meta._meta_table['EthernetSegments']['meta_info']


class EthernetSegmentsState(object):
    """
    Ethernet segmet operational state
    
    .. attribute:: ethernet_segment_state
    
    	An ethernet segment
    	**type**\: list of    :py:class:`EthernetSegmentState <ydk.models.ietf.ietf_ethernet_segment.EthernetSegmentsState.EthernetSegmentState>`
    
    

    """

    _prefix = 'es'
    _revision = '2017-03-13'

    def __init__(self):
        self.ethernet_segment_state = YList()
        self.ethernet_segment_state.parent = self
        self.ethernet_segment_state.name = 'ethernet_segment_state'


    class EthernetSegmentState(object):
        """
        An ethernet segment
        
        .. attribute:: name  <key>
        
        	Name of the ethernet segment
        	**type**\:  str
        
        .. attribute:: ac
        
        	Name of attachment circuit
        	**type**\:  str
        
        .. attribute:: active_mode
        
        	Single\-active\-mode/all\-active\-mode
        	**type**\:  str
        
        .. attribute:: bgp_parameters
        
        	BGP parameters
        	**type**\:   :py:class:`BgpParameters <ydk.models.ietf.ietf_ethernet_segment.EthernetSegmentsState.EthernetSegmentState.BgpParameters>`
        
        .. attribute:: df
        
        	df of an evpn instance's vlan
        	**type**\: list of    :py:class:`Df <ydk.models.ietf.ietf_ethernet_segment.EthernetSegmentsState.EthernetSegmentState.Df>`
        
        .. attribute:: df_election
        
        	df\-election
        	**type**\:   :py:class:`DfElection <ydk.models.ietf.ietf_ethernet_segment.EthernetSegmentsState.EthernetSegmentState.DfElection>`
        
        .. attribute:: ead_evi_route_enabled
        
        	ead\-evi\-route is enabled (TRUE) or disabled (FALSE)
        	**type**\:  bool
        
        .. attribute:: esi_label
        
        	esi\-label
        	**type**\:  str
        
        .. attribute:: ethernet_segment_identifier
        
        	Ethernet segment identifier (esi)
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: interface_status
        
        	interface status
        	**type**\:   :py:class:`StatusTypeEnum <ydk.models.ietf.ietf_ethernet_segment.StatusTypeEnum>`
        
        .. attribute:: member
        
        	member of the ethernet segment
        	**type**\: list of    :py:class:`Member <ydk.models.ietf.ietf_ethernet_segment.EthernetSegmentsState.EthernetSegmentState.Member>`
        
        .. attribute:: pbb_parameters
        
        	PBB configuration
        	**type**\:   :py:class:`PbbParameters <ydk.models.ietf.ietf_ethernet_segment.EthernetSegmentsState.EthernetSegmentState.PbbParameters>`
        
        .. attribute:: pw
        
        	Name of pseudowire
        	**type**\:  str
        
        .. attribute:: service_type
        
        	service\-type
        	**type**\:  str
        
        .. attribute:: status
        
        	Ethernet segment status
        	**type**\:   :py:class:`StatusTypeEnum <ydk.models.ietf.ietf_ethernet_segment.StatusTypeEnum>`
        
        

        """

        _prefix = 'es'
        _revision = '2017-03-13'

        def __init__(self):
            self.parent = None
            self.name = None
            self.ac = None
            self.active_mode = None
            self.bgp_parameters = EthernetSegmentsState.EthernetSegmentState.BgpParameters()
            self.bgp_parameters.parent = self
            self.df = YList()
            self.df.parent = self
            self.df.name = 'df'
            self.df_election = EthernetSegmentsState.EthernetSegmentState.DfElection()
            self.df_election.parent = self
            self.ead_evi_route_enabled = None
            self.esi_label = None
            self.ethernet_segment_identifier = None
            self.interface_status = None
            self.member = YList()
            self.member.parent = self
            self.member.name = 'member'
            self.pbb_parameters = EthernetSegmentsState.EthernetSegmentState.PbbParameters()
            self.pbb_parameters.parent = self
            self.pw = None
            self.service_type = None
            self.status = None


        class PbbParameters(object):
            """
            PBB configuration
            
            .. attribute:: backbone_src_mac
            
            	backbone\-src\-mac, only if this is a PBB
            	**type**\:  str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            

            """

            _prefix = 'es'
            _revision = '2017-03-13'

            def __init__(self):
                self.parent = None
                self.backbone_src_mac = None

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/ietf-ethernet-segment:pbb-parameters'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.backbone_src_mac is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_ethernet_segment as meta
                return meta._meta_table['EthernetSegmentsState.EthernetSegmentState.PbbParameters']['meta_info']


        class BgpParameters(object):
            """
            BGP parameters
            
            .. attribute:: common
            
            	BGP parameters common to all pseudowires
            	**type**\:   :py:class:`Common <ydk.models.ietf.ietf_ethernet_segment.EthernetSegmentsState.EthernetSegmentState.BgpParameters.Common>`
            
            

            """

            _prefix = 'es'
            _revision = '2017-03-13'

            def __init__(self):
                self.parent = None
                self.common = EthernetSegmentsState.EthernetSegmentState.BgpParameters.Common()
                self.common.parent = self


            class Common(object):
                """
                BGP parameters common to all pseudowires
                
                .. attribute:: rd_rt
                
                	A list of route distinghishers and corresponding route targets
                	**type**\: list of    :py:class:`RdRt <ydk.models.ietf.ietf_ethernet_segment.EthernetSegmentsState.EthernetSegmentState.BgpParameters.Common.RdRt>`
                
                

                """

                _prefix = 'es'
                _revision = '2017-03-13'

                def __init__(self):
                    self.parent = None
                    self.rd_rt = YList()
                    self.rd_rt.parent = self
                    self.rd_rt.name = 'rd_rt'


                class RdRt(object):
                    """
                    A list of route distinghishers and corresponding route targets
                    
                    .. attribute:: route_distinguisher  <key>
                    
                    	Route distinguisher
                    	**type**\:  str
                    
                    	**pattern:** (0\:(6553[0\-5]\|655[0\-2]\\d\|65[0\-4]\\d{2}\|6[0\-4]\\d{3}\|[0\-5]?\\d{0,3}\\d)\:(429496729[0\-5]\|42949672[0\-8]\\d\|4294967[01]\\d{2}\|429496[0\-6]\\d{3}\|42949[0\-5]\\d{4}\|4294[0\-8]\\d{5}\|429[0\-3]\\d{6}\|42[0\-8]\\d{7}\|4[01]\\d{8}\|[0\-3]?\\d{0,8}\\d))\|(1\:(((\\d\|[1\-9]\\d\|1\\d{2}\|2[0\-4]\\d\|25[0\-5])\\.){3}(\\d\|[1\-9]\\d\|1\\d{2}\|2[0\-4]\\d\|25[0\-5]))\:(6553[0\-5]\|655[0\-2]\\d\|65[0\-4]\\d{2}\|6[0\-4]\\d{3}\|[0\-5]?\\d{0,3}\\d))\|(2\:(429496729[0\-5]\|42949672[0\-8]\\d\|4294967[01]\\d{2}\|429496[0\-6]\\d{3}\|42949[0\-5]\\d{4}\|4294[0\-8]\\d{5}\|429[0\-3]\\d{6}\|42[0\-8]\\d{7}\|4[01]\\d{8}\|[0\-3]?\\d{0,8}\\d)\:(6553[0\-5]\|655[0\-2]\\d\|65[0\-4]\\d{2}\|6[0\-4]\\d{3}\|[0\-5]?\\d{0,3}\\d))\|(([3\-9a\-fA\-F]\|[1\-9a\-fA\-F][\\da\-fA\-F]{1,3})\:[\\da\-fA\-F]{1,12})
                    
                    .. attribute:: vpn_target
                    
                    	List of Route Targets
                    	**type**\: list of    :py:class:`VpnTarget <ydk.models.ietf.ietf_ethernet_segment.EthernetSegmentsState.EthernetSegmentState.BgpParameters.Common.RdRt.VpnTarget>`
                    
                    

                    """

                    _prefix = 'es'
                    _revision = '2017-03-13'

                    def __init__(self):
                        self.parent = None
                        self.route_distinguisher = None
                        self.vpn_target = YList()
                        self.vpn_target.parent = self
                        self.vpn_target.name = 'vpn_target'


                    class VpnTarget(object):
                        """
                        List of Route Targets.
                        
                        .. attribute:: route_target  <key>
                        
                        	Route Target value
                        	**type**\:  str
                        
                        	**pattern:** (0\:(6553[0\-5]\|655[0\-2]\\d\|65[0\-4]\\d{2}\|6[0\-4]\\d{3}\|[0\-5]?\\d{0,3}\\d)\:(429496729[0\-5]\|42949672[0\-8]\\d\|4294967[01]\\d{2}\|429496[0\-6]\\d{3}\|42949[0\-5]\\d{4}\|4294[0\-8]\\d{5}\|429[0\-3]\\d{6}\|42[0\-8]\\d{7}\|4[01]\\d{8}\|[0\-3]?\\d{0,8}\\d))\|(1\:(((\\d\|[1\-9]\\d\|1\\d{2}\|2[0\-4]\\d\|25[0\-5])\\.){3}(\\d\|[1\-9]\\d\|1\\d{2}\|2[0\-4]\\d\|25[0\-5]))\:(6553[0\-5]\|655[0\-2]\\d\|65[0\-4]\\d{2}\|6[0\-4]\\d{3}\|[0\-5]?\\d{0,3}\\d))\|(2\:(429496729[0\-5]\|42949672[0\-8]\\d\|4294967[01]\\d{2}\|429496[0\-6]\\d{3}\|42949[0\-5]\\d{4}\|4294[0\-8]\\d{5}\|429[0\-3]\\d{6}\|42[0\-8]\\d{7}\|4[01]\\d{8}\|[0\-3]?\\d{0,8}\\d)\:(6553[0\-5]\|655[0\-2]\\d\|65[0\-4]\\d{2}\|6[0\-4]\\d{3}\|[0\-5]?\\d{0,3}\\d))
                        
                        .. attribute:: route_target_type
                        
                        	Import/export type of the Route Target
                        	**type**\:   :py:class:`RouteTargetTypeEnum <ydk.models.ietf.ietf_routing_types.RouteTargetTypeEnum>`
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'es'
                        _revision = '2017-03-13'

                        def __init__(self):
                            self.parent = None
                            self.route_target = None
                            self.route_target_type = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.route_target is None:
                                raise YPYModelError('Key property route_target is None')

                            return self.parent._common_path +'/ietf-ethernet-segment:vpn-target[ietf-ethernet-segment:route-target = ' + str(self.route_target) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.route_target is not None:
                                return True

                            if self.route_target_type is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ietf._meta import _ietf_ethernet_segment as meta
                            return meta._meta_table['EthernetSegmentsState.EthernetSegmentState.BgpParameters.Common.RdRt.VpnTarget']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.route_distinguisher is None:
                            raise YPYModelError('Key property route_distinguisher is None')

                        return self.parent._common_path +'/ietf-ethernet-segment:rd-rt[ietf-ethernet-segment:route-distinguisher = ' + str(self.route_distinguisher) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.route_distinguisher is not None:
                            return True

                        if self.vpn_target is not None:
                            for child_ref in self.vpn_target:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_ethernet_segment as meta
                        return meta._meta_table['EthernetSegmentsState.EthernetSegmentState.BgpParameters.Common.RdRt']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-ethernet-segment:common'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.rd_rt is not None:
                        for child_ref in self.rd_rt:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_ethernet_segment as meta
                    return meta._meta_table['EthernetSegmentsState.EthernetSegmentState.BgpParameters.Common']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/ietf-ethernet-segment:bgp-parameters'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.common is not None and self.common._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_ethernet_segment as meta
                return meta._meta_table['EthernetSegmentsState.EthernetSegmentState.BgpParameters']['meta_info']


        class DfElection(object):
            """
            df\-election
            
            .. attribute:: election_wait_time
            
            	election\-wait\-time
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: hrw_enabled
            
            	hrw\-enabled is enabled (TRUE) or disabled (FALSE)
            	**type**\:  bool
            
            

            """

            _prefix = 'es'
            _revision = '2017-03-13'

            def __init__(self):
                self.parent = None
                self.election_wait_time = None
                self.hrw_enabled = None

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/ietf-ethernet-segment:df-election'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.election_wait_time is not None:
                    return True

                if self.hrw_enabled is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_ethernet_segment as meta
                return meta._meta_table['EthernetSegmentsState.EthernetSegmentState.DfElection']['meta_info']


        class Member(object):
            """
            member of the ethernet segment
            
            .. attribute:: ip_address
            
            	ip\-address
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            
            ----
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            
            ----
            

            """

            _prefix = 'es'
            _revision = '2017-03-13'

            def __init__(self):
                self.parent = None
                self.ip_address = None

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/ietf-ethernet-segment:member'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.ip_address is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_ethernet_segment as meta
                return meta._meta_table['EthernetSegmentsState.EthernetSegmentState.Member']['meta_info']


        class Df(object):
            """
            df of an evpn instance's vlan
            
            .. attribute:: ip_address
            
            	ip\-address
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            
            ----
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            
            ----
            .. attribute:: service_identifier
            
            	service\-identifier
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: vlan
            
            	vlan
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'es'
            _revision = '2017-03-13'

            def __init__(self):
                self.parent = None
                self.ip_address = None
                self.service_identifier = None
                self.vlan = None

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/ietf-ethernet-segment:df'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.ip_address is not None:
                    return True

                if self.service_identifier is not None:
                    return True

                if self.vlan is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_ethernet_segment as meta
                return meta._meta_table['EthernetSegmentsState.EthernetSegmentState.Df']['meta_info']

        @property
        def _common_path(self):
            if self.name is None:
                raise YPYModelError('Key property name is None')

            return '/ietf-ethernet-segment:ethernet-segments-state/ietf-ethernet-segment:ethernet-segment-state[ietf-ethernet-segment:name = ' + str(self.name) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.name is not None:
                return True

            if self.ac is not None:
                return True

            if self.active_mode is not None:
                return True

            if self.bgp_parameters is not None and self.bgp_parameters._has_data():
                return True

            if self.df is not None:
                for child_ref in self.df:
                    if child_ref._has_data():
                        return True

            if self.df_election is not None and self.df_election._has_data():
                return True

            if self.ead_evi_route_enabled is not None:
                return True

            if self.esi_label is not None:
                return True

            if self.ethernet_segment_identifier is not None:
                return True

            if self.interface_status is not None:
                return True

            if self.member is not None:
                for child_ref in self.member:
                    if child_ref._has_data():
                        return True

            if self.pbb_parameters is not None and self.pbb_parameters._has_data():
                return True

            if self.pw is not None:
                return True

            if self.service_type is not None:
                return True

            if self.status is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_ethernet_segment as meta
            return meta._meta_table['EthernetSegmentsState.EthernetSegmentState']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-ethernet-segment:ethernet-segments-state'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.ethernet_segment_state is not None:
            for child_ref in self.ethernet_segment_state:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_ethernet_segment as meta
        return meta._meta_table['EthernetSegmentsState']['meta_info']


