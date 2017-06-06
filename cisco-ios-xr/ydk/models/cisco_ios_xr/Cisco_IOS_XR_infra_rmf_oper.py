""" Cisco_IOS_XR_infra_rmf_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-rmf package operational data.

This module contains definitions
for the following management objects\:
  redundancy\: Redundancy show information

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class Redundancy(object):
    """
    Redundancy show information
    
    .. attribute:: nodes
    
    	Location show information
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rmf_oper.Redundancy.Nodes>`
    
    .. attribute:: summary
    
    	Redundancy Summary of Nodes
    	**type**\:   :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rmf_oper.Redundancy.Summary>`
    
    

    """

    _prefix = 'infra-rmf-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.nodes = Redundancy.Nodes()
        self.nodes.parent = self
        self.summary = Redundancy.Summary()
        self.summary.parent = self


    class Nodes(object):
        """
        Location show information
        
        .. attribute:: node
        
        	Redundancy Node Information
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rmf_oper.Redundancy.Nodes.Node>`
        
        

        """

        _prefix = 'infra-rmf-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
            """
            Redundancy Node Information
            
            .. attribute:: node_id  <key>
            
            	Node Location
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: active_reboot_reason
            
            	Active node reload
            	**type**\:  str
            
            .. attribute:: err_log
            
            	Error Log
            	**type**\:  str
            
            .. attribute:: log
            
            	Reload and boot logs
            	**type**\:  str
            
            .. attribute:: redundancy
            
            	Row information
            	**type**\:   :py:class:`Redundancy_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rmf_oper.Redundancy.Nodes.Node.Redundancy_>`
            
            .. attribute:: standby_reboot_reason
            
            	Standby node reload
            	**type**\:  str
            
            

            """

            _prefix = 'infra-rmf-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.node_id = None
                self.active_reboot_reason = None
                self.err_log = None
                self.log = None
                self.redundancy = Redundancy.Nodes.Node.Redundancy_()
                self.redundancy.parent = self
                self.standby_reboot_reason = None


            class Redundancy_(object):
                """
                Row information
                
                .. attribute:: active
                
                	Active node name R/S/I
                	**type**\:  str
                
                .. attribute:: groupinfo
                
                	groupinfo
                	**type**\: list of    :py:class:`Groupinfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rmf_oper.Redundancy.Nodes.Node.Redundancy_.Groupinfo>`
                
                .. attribute:: ha_state
                
                	High Availability state Ready/Not Ready
                	**type**\:  str
                
                .. attribute:: nsr_state
                
                	NSR state Configured/Not Configured
                	**type**\:  str
                
                .. attribute:: standby
                
                	Standby node name R/S/I
                	**type**\:  str
                
                

                """

                _prefix = 'infra-rmf-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.active = None
                    self.groupinfo = YList()
                    self.groupinfo.parent = self
                    self.groupinfo.name = 'groupinfo'
                    self.ha_state = None
                    self.nsr_state = None
                    self.standby = None


                class Groupinfo(object):
                    """
                    groupinfo
                    
                    .. attribute:: active
                    
                    	Active
                    	**type**\:  str
                    
                    .. attribute:: ha_state
                    
                    	HAState
                    	**type**\:  str
                    
                    .. attribute:: nsr_state
                    
                    	NSRState
                    	**type**\:  str
                    
                    .. attribute:: standby
                    
                    	Standby
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'infra-rmf-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.active = None
                        self.ha_state = None
                        self.nsr_state = None
                        self.standby = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-rmf-oper:groupinfo'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.active is not None:
                            return True

                        if self.ha_state is not None:
                            return True

                        if self.nsr_state is not None:
                            return True

                        if self.standby is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rmf_oper as meta
                        return meta._meta_table['Redundancy.Nodes.Node.Redundancy_.Groupinfo']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-rmf-oper:redundancy'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.active is not None:
                        return True

                    if self.groupinfo is not None:
                        for child_ref in self.groupinfo:
                            if child_ref._has_data():
                                return True

                    if self.ha_state is not None:
                        return True

                    if self.nsr_state is not None:
                        return True

                    if self.standby is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rmf_oper as meta
                    return meta._meta_table['Redundancy.Nodes.Node.Redundancy_']['meta_info']

            @property
            def _common_path(self):
                if self.node_id is None:
                    raise YPYModelError('Key property node_id is None')

                return '/Cisco-IOS-XR-infra-rmf-oper:redundancy/Cisco-IOS-XR-infra-rmf-oper:nodes/Cisco-IOS-XR-infra-rmf-oper:node[Cisco-IOS-XR-infra-rmf-oper:node-id = ' + str(self.node_id) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.node_id is not None:
                    return True

                if self.active_reboot_reason is not None:
                    return True

                if self.err_log is not None:
                    return True

                if self.log is not None:
                    return True

                if self.redundancy is not None and self.redundancy._has_data():
                    return True

                if self.standby_reboot_reason is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rmf_oper as meta
                return meta._meta_table['Redundancy.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-rmf-oper:redundancy/Cisco-IOS-XR-infra-rmf-oper:nodes'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.node is not None:
                for child_ref in self.node:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rmf_oper as meta
            return meta._meta_table['Redundancy.Nodes']['meta_info']


    class Summary(object):
        """
        Redundancy Summary of Nodes
        
        .. attribute:: err_log
        
        	Error Log
        	**type**\:  str
        
        .. attribute:: red_pair
        
        	Redundancy Pair
        	**type**\: list of    :py:class:`RedPair <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rmf_oper.Redundancy.Summary.RedPair>`
        
        

        """

        _prefix = 'infra-rmf-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.err_log = None
            self.red_pair = YList()
            self.red_pair.parent = self
            self.red_pair.name = 'red_pair'


        class RedPair(object):
            """
            Redundancy Pair
            
            .. attribute:: active
            
            	Active node name R/S/I
            	**type**\:  str
            
            .. attribute:: groupinfo
            
            	groupinfo
            	**type**\: list of    :py:class:`Groupinfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rmf_oper.Redundancy.Summary.RedPair.Groupinfo>`
            
            .. attribute:: ha_state
            
            	High Availability state Ready/Not Ready
            	**type**\:  str
            
            .. attribute:: nsr_state
            
            	NSR state Configured/Not Configured
            	**type**\:  str
            
            .. attribute:: standby
            
            	Standby node name R/S/I
            	**type**\:  str
            
            

            """

            _prefix = 'infra-rmf-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.active = None
                self.groupinfo = YList()
                self.groupinfo.parent = self
                self.groupinfo.name = 'groupinfo'
                self.ha_state = None
                self.nsr_state = None
                self.standby = None


            class Groupinfo(object):
                """
                groupinfo
                
                .. attribute:: active
                
                	Active
                	**type**\:  str
                
                .. attribute:: ha_state
                
                	HAState
                	**type**\:  str
                
                .. attribute:: nsr_state
                
                	NSRState
                	**type**\:  str
                
                .. attribute:: standby
                
                	Standby
                	**type**\:  str
                
                

                """

                _prefix = 'infra-rmf-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.active = None
                    self.ha_state = None
                    self.nsr_state = None
                    self.standby = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-infra-rmf-oper:redundancy/Cisco-IOS-XR-infra-rmf-oper:summary/Cisco-IOS-XR-infra-rmf-oper:red-pair/Cisco-IOS-XR-infra-rmf-oper:groupinfo'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.active is not None:
                        return True

                    if self.ha_state is not None:
                        return True

                    if self.nsr_state is not None:
                        return True

                    if self.standby is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rmf_oper as meta
                    return meta._meta_table['Redundancy.Summary.RedPair.Groupinfo']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-infra-rmf-oper:redundancy/Cisco-IOS-XR-infra-rmf-oper:summary/Cisco-IOS-XR-infra-rmf-oper:red-pair'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.active is not None:
                    return True

                if self.groupinfo is not None:
                    for child_ref in self.groupinfo:
                        if child_ref._has_data():
                            return True

                if self.ha_state is not None:
                    return True

                if self.nsr_state is not None:
                    return True

                if self.standby is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rmf_oper as meta
                return meta._meta_table['Redundancy.Summary.RedPair']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-rmf-oper:redundancy/Cisco-IOS-XR-infra-rmf-oper:summary'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.err_log is not None:
                return True

            if self.red_pair is not None:
                for child_ref in self.red_pair:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rmf_oper as meta
            return meta._meta_table['Redundancy.Summary']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-infra-rmf-oper:redundancy'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.nodes is not None and self.nodes._has_data():
            return True

        if self.summary is not None and self.summary._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rmf_oper as meta
        return meta._meta_table['Redundancy']['meta_info']


