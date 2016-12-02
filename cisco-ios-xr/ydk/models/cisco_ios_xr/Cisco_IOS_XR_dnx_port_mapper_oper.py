""" Cisco_IOS_XR_dnx_port_mapper_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR dnx\-port\-mapper package operational data.

This module contains definitions
for the following management objects\:
  oor\: DPA operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class Oor(object):
    """
    DPA operational data
    
    .. attribute:: nodes
    
    	OOR data for available nodes
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_port_mapper_oper.Oor.Nodes>`
    
    

    """

    _prefix = 'dnx-port-mapper-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.nodes = Oor.Nodes()
        self.nodes.parent = self


    class Nodes(object):
        """
        OOR data for available nodes
        
        .. attribute:: node
        
        	DPA operational data for a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_port_mapper_oper.Oor.Nodes.Node>`
        
        

        """

        _prefix = 'dnx-port-mapper-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
            """
            DPA operational data for a particular node
            
            .. attribute:: node_name  <key>
            
            	Node ID
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: bundle_interface_details
            
            	OOR Bundle Interface Detail
            	**type**\:   :py:class:`BundleInterfaceDetails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_port_mapper_oper.Oor.Nodes.Node.BundleInterfaceDetails>`
            
            .. attribute:: interface_details
            
            	OOR Interface Detail
            	**type**\:   :py:class:`InterfaceDetails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_port_mapper_oper.Oor.Nodes.Node.InterfaceDetails>`
            
            .. attribute:: interface_summary_datas
            
            	OOR Per Interface Summary
            	**type**\:   :py:class:`InterfaceSummaryDatas <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_port_mapper_oper.Oor.Nodes.Node.InterfaceSummaryDatas>`
            
            .. attribute:: oor_summary
            
            	OOR Summary
            	**type**\:   :py:class:`OorSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_port_mapper_oper.Oor.Nodes.Node.OorSummary>`
            
            

            """

            _prefix = 'dnx-port-mapper-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.node_name = None
                self.bundle_interface_details = Oor.Nodes.Node.BundleInterfaceDetails()
                self.bundle_interface_details.parent = self
                self.interface_details = Oor.Nodes.Node.InterfaceDetails()
                self.interface_details.parent = self
                self.interface_summary_datas = Oor.Nodes.Node.InterfaceSummaryDatas()
                self.interface_summary_datas.parent = self
                self.oor_summary = Oor.Nodes.Node.OorSummary()
                self.oor_summary.parent = self


            class BundleInterfaceDetails(object):
                """
                OOR Bundle Interface Detail
                
                .. attribute:: bundle_interface_detail
                
                	OOR Data for particular Bundle interface
                	**type**\: list of    :py:class:`BundleInterfaceDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_port_mapper_oper.Oor.Nodes.Node.BundleInterfaceDetails.BundleInterfaceDetail>`
                
                

                """

                _prefix = 'dnx-port-mapper-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.bundle_interface_detail = YList()
                    self.bundle_interface_detail.parent = self
                    self.bundle_interface_detail.name = 'bundle_interface_detail'


                class BundleInterfaceDetail(object):
                    """
                    OOR Data for particular Bundle interface
                    
                    .. attribute:: interface  <key>
                    
                    	Interface Name
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: interface_state
                    
                    	Current state of the interface
                    	**type**\:  str
                    
                    .. attribute:: member
                    
                    	Member details
                    	**type**\: list of    :py:class:`Member <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_port_mapper_oper.Oor.Nodes.Node.BundleInterfaceDetails.BundleInterfaceDetail.Member>`
                    
                    .. attribute:: time_stamp
                    
                    	Timestamp
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'dnx-port-mapper-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.interface = None
                        self.interface_state = None
                        self.member = YList()
                        self.member.parent = self
                        self.member.name = 'member'
                        self.time_stamp = None


                    class Member(object):
                        """
                        Member details
                        
                        .. attribute:: hardware_resource
                        
                        	Type of harware resoruce
                        	**type**\:  str
                        
                        .. attribute:: interface_name
                        
                        	Name of the interface
                        	**type**\:  str
                        
                        .. attribute:: interface_status
                        
                        	The current state of the interface
                        	**type**\:  str
                        
                        .. attribute:: npu_id
                        
                        	Npuid of the interface
                        	**type**\:  str
                        
                        .. attribute:: time_stamp
                        
                        	Timestamp
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'dnx-port-mapper-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.hardware_resource = None
                            self.interface_name = None
                            self.interface_status = None
                            self.npu_id = None
                            self.time_stamp = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-dnx-port-mapper-oper:member'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.hardware_resource is not None:
                                return True

                            if self.interface_name is not None:
                                return True

                            if self.interface_status is not None:
                                return True

                            if self.npu_id is not None:
                                return True

                            if self.time_stamp is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dnx_port_mapper_oper as meta
                            return meta._meta_table['Oor.Nodes.Node.BundleInterfaceDetails.BundleInterfaceDetail.Member']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.interface is None:
                            raise YPYModelError('Key property interface is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-dnx-port-mapper-oper:bundle-interface-detail[Cisco-IOS-XR-dnx-port-mapper-oper:interface = ' + str(self.interface) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.interface is not None:
                            return True

                        if self.interface_state is not None:
                            return True

                        if self.member is not None:
                            for child_ref in self.member:
                                if child_ref._has_data():
                                    return True

                        if self.time_stamp is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dnx_port_mapper_oper as meta
                        return meta._meta_table['Oor.Nodes.Node.BundleInterfaceDetails.BundleInterfaceDetail']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-dnx-port-mapper-oper:bundle-interface-details'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.bundle_interface_detail is not None:
                        for child_ref in self.bundle_interface_detail:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dnx_port_mapper_oper as meta
                    return meta._meta_table['Oor.Nodes.Node.BundleInterfaceDetails']['meta_info']


            class InterfaceDetails(object):
                """
                OOR Interface Detail
                
                .. attribute:: interface_detail
                
                	OOR Data for particular interface
                	**type**\: list of    :py:class:`InterfaceDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_port_mapper_oper.Oor.Nodes.Node.InterfaceDetails.InterfaceDetail>`
                
                

                """

                _prefix = 'dnx-port-mapper-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.interface_detail = YList()
                    self.interface_detail.parent = self
                    self.interface_detail.name = 'interface_detail'


                class InterfaceDetail(object):
                    """
                    OOR Data for particular interface
                    
                    .. attribute:: interface  <key>
                    
                    	Interface Name
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: hardware_resource
                    
                    	Type of harware resoruce
                    	**type**\:  str
                    
                    .. attribute:: interface_name
                    
                    	Name of the interface
                    	**type**\:  str
                    
                    .. attribute:: interface_status
                    
                    	The current state of the interface
                    	**type**\:  str
                    
                    .. attribute:: npu_id
                    
                    	Npuid of the interface
                    	**type**\:  str
                    
                    .. attribute:: time_stamp
                    
                    	Timestamp
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'dnx-port-mapper-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.interface = None
                        self.hardware_resource = None
                        self.interface_name = None
                        self.interface_status = None
                        self.npu_id = None
                        self.time_stamp = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.interface is None:
                            raise YPYModelError('Key property interface is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-dnx-port-mapper-oper:interface-detail[Cisco-IOS-XR-dnx-port-mapper-oper:interface = ' + str(self.interface) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.interface is not None:
                            return True

                        if self.hardware_resource is not None:
                            return True

                        if self.interface_name is not None:
                            return True

                        if self.interface_status is not None:
                            return True

                        if self.npu_id is not None:
                            return True

                        if self.time_stamp is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dnx_port_mapper_oper as meta
                        return meta._meta_table['Oor.Nodes.Node.InterfaceDetails.InterfaceDetail']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-dnx-port-mapper-oper:interface-details'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.interface_detail is not None:
                        for child_ref in self.interface_detail:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dnx_port_mapper_oper as meta
                    return meta._meta_table['Oor.Nodes.Node.InterfaceDetails']['meta_info']


            class InterfaceSummaryDatas(object):
                """
                OOR Per Interface Summary
                
                .. attribute:: interface_summary_data
                
                	OOR Data for particular interface
                	**type**\: list of    :py:class:`InterfaceSummaryData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_port_mapper_oper.Oor.Nodes.Node.InterfaceSummaryDatas.InterfaceSummaryData>`
                
                

                """

                _prefix = 'dnx-port-mapper-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.interface_summary_data = YList()
                    self.interface_summary_data.parent = self
                    self.interface_summary_data.name = 'interface_summary_data'


                class InterfaceSummaryData(object):
                    """
                    OOR Data for particular interface
                    
                    .. attribute:: interface  <key>
                    
                    	Interface Number
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: hardware_resource
                    
                    	Type of harware resoruce
                    	**type**\:  str
                    
                    .. attribute:: interface_name
                    
                    	Name of the interface
                    	**type**\:  str
                    
                    .. attribute:: interface_status
                    
                    	The current state of the interface
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'dnx-port-mapper-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.interface = None
                        self.hardware_resource = None
                        self.interface_name = None
                        self.interface_status = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.interface is None:
                            raise YPYModelError('Key property interface is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-dnx-port-mapper-oper:interface-summary-data[Cisco-IOS-XR-dnx-port-mapper-oper:interface = ' + str(self.interface) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.interface is not None:
                            return True

                        if self.hardware_resource is not None:
                            return True

                        if self.interface_name is not None:
                            return True

                        if self.interface_status is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dnx_port_mapper_oper as meta
                        return meta._meta_table['Oor.Nodes.Node.InterfaceSummaryDatas.InterfaceSummaryData']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-dnx-port-mapper-oper:interface-summary-datas'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.interface_summary_data is not None:
                        for child_ref in self.interface_summary_data:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dnx_port_mapper_oper as meta
                    return meta._meta_table['Oor.Nodes.Node.InterfaceSummaryDatas']['meta_info']


            class OorSummary(object):
                """
                OOR Summary
                
                .. attribute:: green
                
                	interfaces in green state
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: red
                
                	interfaces in red state
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: yel_low
                
                	interfaces in yellow state
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'dnx-port-mapper-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.green = None
                    self.red = None
                    self.yel_low = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-dnx-port-mapper-oper:oor-summary'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.green is not None:
                        return True

                    if self.red is not None:
                        return True

                    if self.yel_low is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dnx_port_mapper_oper as meta
                    return meta._meta_table['Oor.Nodes.Node.OorSummary']['meta_info']

            @property
            def _common_path(self):
                if self.node_name is None:
                    raise YPYModelError('Key property node_name is None')

                return '/Cisco-IOS-XR-dnx-port-mapper-oper:oor/Cisco-IOS-XR-dnx-port-mapper-oper:nodes/Cisco-IOS-XR-dnx-port-mapper-oper:node[Cisco-IOS-XR-dnx-port-mapper-oper:node-name = ' + str(self.node_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.node_name is not None:
                    return True

                if self.bundle_interface_details is not None and self.bundle_interface_details._has_data():
                    return True

                if self.interface_details is not None and self.interface_details._has_data():
                    return True

                if self.interface_summary_datas is not None and self.interface_summary_datas._has_data():
                    return True

                if self.oor_summary is not None and self.oor_summary._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dnx_port_mapper_oper as meta
                return meta._meta_table['Oor.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-dnx-port-mapper-oper:oor/Cisco-IOS-XR-dnx-port-mapper-oper:nodes'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.node is not None:
                for child_ref in self.node:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dnx_port_mapper_oper as meta
            return meta._meta_table['Oor.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-dnx-port-mapper-oper:oor'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.nodes is not None and self.nodes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dnx_port_mapper_oper as meta
        return meta._meta_table['Oor']['meta_info']


