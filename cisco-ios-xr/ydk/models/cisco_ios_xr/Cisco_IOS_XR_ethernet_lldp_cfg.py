""" Cisco_IOS_XR_ethernet_lldp_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ethernet\-lldp package configuration.

This module contains definitions
for the following management objects\:
  lldp\: Enable LLDP, or configure global LLDP subcommands

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg
module with configuration data.

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Lldp(Entity):
    """
    Enable LLDP, or configure global LLDP subcommands
    
    .. attribute:: tlv_select
    
    	Selection of LLDP TLVs to disable
    	**type**\:  :py:class:`TlvSelect <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_cfg.Lldp.TlvSelect>`
    
    	**presence node**\: True
    
    .. attribute:: holdtime
    
    	Length  of time  (in sec) that receiver must keep this packet
    	**type**\: int
    
    	**range:** 0..65535
    
    .. attribute:: extended_show_width
    
    	Enable or disable LLDP Show LLDP Neighbor Extended Width
    	**type**\: bool
    
    	**default value**\: false
    
    .. attribute:: enable_subintf
    
    	Enable or disable LLDP on Sub\-interfaces as well globally
    	**type**\: bool
    
    	**default value**\: false
    
    .. attribute:: enable_mgmtintf
    
    	Enable or disable LLDP on Mgmt interfaces as well globally
    	**type**\: bool
    
    	**default value**\: false
    
    .. attribute:: timer
    
    	Specify the rate at which LLDP packets are sent (in sec)
    	**type**\: int
    
    	**range:** 5..65534
    
    	**default value**\: 30
    
    .. attribute:: reinit
    
    	Delay (in sec) for LLDP initialization on any interface
    	**type**\: int
    
    	**range:** 2..5
    
    	**default value**\: 2
    
    .. attribute:: enable
    
    	Enable or disable LLDP globally
    	**type**\: bool
    
    	**default value**\: false
    
    

    """

    _prefix = 'ethernet-lldp-cfg'
    _revision = '2017-05-01'

    def __init__(self):
        super(Lldp, self).__init__()
        self._top_entity = None

        self.yang_name = "lldp"
        self.yang_parent_name = "Cisco-IOS-XR-ethernet-lldp-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("tlv-select", ("tlv_select", Lldp.TlvSelect))])
        self._leafs = OrderedDict([
            ('holdtime', (YLeaf(YType.uint32, 'holdtime'), ['int'])),
            ('extended_show_width', (YLeaf(YType.boolean, 'extended-show-width'), ['bool'])),
            ('enable_subintf', (YLeaf(YType.boolean, 'enable-subintf'), ['bool'])),
            ('enable_mgmtintf', (YLeaf(YType.boolean, 'enable-mgmtintf'), ['bool'])),
            ('timer', (YLeaf(YType.uint32, 'timer'), ['int'])),
            ('reinit', (YLeaf(YType.uint32, 'reinit'), ['int'])),
            ('enable', (YLeaf(YType.boolean, 'enable'), ['bool'])),
        ])
        self.holdtime = None
        self.extended_show_width = None
        self.enable_subintf = None
        self.enable_mgmtintf = None
        self.timer = None
        self.reinit = None
        self.enable = None

        self.tlv_select = None
        self._children_name_map["tlv_select"] = "tlv-select"
        self._segment_path = lambda: "Cisco-IOS-XR-ethernet-lldp-cfg:lldp"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Lldp, ['holdtime', 'extended_show_width', 'enable_subintf', 'enable_mgmtintf', 'timer', 'reinit', 'enable'], name, value)


    class TlvSelect(Entity):
        """
        Selection of LLDP TLVs to disable
        
        .. attribute:: system_name
        
        	System Name TLV
        	**type**\:  :py:class:`SystemName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_cfg.Lldp.TlvSelect.SystemName>`
        
        .. attribute:: port_description
        
        	Port Description TLV
        	**type**\:  :py:class:`PortDescription <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_cfg.Lldp.TlvSelect.PortDescription>`
        
        .. attribute:: system_description
        
        	System Description TLV
        	**type**\:  :py:class:`SystemDescription <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_cfg.Lldp.TlvSelect.SystemDescription>`
        
        .. attribute:: system_capabilities
        
        	System Capabilities TLV
        	**type**\:  :py:class:`SystemCapabilities <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_cfg.Lldp.TlvSelect.SystemCapabilities>`
        
        .. attribute:: management_address
        
        	Management Address TLV
        	**type**\:  :py:class:`ManagementAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_cfg.Lldp.TlvSelect.ManagementAddress>`
        
        .. attribute:: tlv_select_enter
        
        	enter lldp tlv\-select submode
        	**type**\: bool
        
        	**mandatory**\: True
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'ethernet-lldp-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(Lldp.TlvSelect, self).__init__()

            self.yang_name = "tlv-select"
            self.yang_parent_name = "lldp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("system-name", ("system_name", Lldp.TlvSelect.SystemName)), ("port-description", ("port_description", Lldp.TlvSelect.PortDescription)), ("system-description", ("system_description", Lldp.TlvSelect.SystemDescription)), ("system-capabilities", ("system_capabilities", Lldp.TlvSelect.SystemCapabilities)), ("management-address", ("management_address", Lldp.TlvSelect.ManagementAddress))])
            self.is_presence_container = True
            self._leafs = OrderedDict([
                ('tlv_select_enter', (YLeaf(YType.boolean, 'tlv-select-enter'), ['bool'])),
            ])
            self.tlv_select_enter = None

            self.system_name = Lldp.TlvSelect.SystemName()
            self.system_name.parent = self
            self._children_name_map["system_name"] = "system-name"

            self.port_description = Lldp.TlvSelect.PortDescription()
            self.port_description.parent = self
            self._children_name_map["port_description"] = "port-description"

            self.system_description = Lldp.TlvSelect.SystemDescription()
            self.system_description.parent = self
            self._children_name_map["system_description"] = "system-description"

            self.system_capabilities = Lldp.TlvSelect.SystemCapabilities()
            self.system_capabilities.parent = self
            self._children_name_map["system_capabilities"] = "system-capabilities"

            self.management_address = Lldp.TlvSelect.ManagementAddress()
            self.management_address.parent = self
            self._children_name_map["management_address"] = "management-address"
            self._segment_path = lambda: "tlv-select"
            self._absolute_path = lambda: "Cisco-IOS-XR-ethernet-lldp-cfg:lldp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Lldp.TlvSelect, ['tlv_select_enter'], name, value)


        class SystemName(Entity):
            """
            System Name TLV
            
            .. attribute:: disable
            
            	disable System Name TLV
            	**type**\: bool
            
            	**default value**\: false
            
            

            """

            _prefix = 'ethernet-lldp-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(Lldp.TlvSelect.SystemName, self).__init__()

                self.yang_name = "system-name"
                self.yang_parent_name = "tlv-select"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('disable', (YLeaf(YType.boolean, 'disable'), ['bool'])),
                ])
                self.disable = None
                self._segment_path = lambda: "system-name"
                self._absolute_path = lambda: "Cisco-IOS-XR-ethernet-lldp-cfg:lldp/tlv-select/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Lldp.TlvSelect.SystemName, ['disable'], name, value)


        class PortDescription(Entity):
            """
            Port Description TLV
            
            .. attribute:: disable
            
            	disable Port Description TLV
            	**type**\: bool
            
            	**default value**\: false
            
            

            """

            _prefix = 'ethernet-lldp-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(Lldp.TlvSelect.PortDescription, self).__init__()

                self.yang_name = "port-description"
                self.yang_parent_name = "tlv-select"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('disable', (YLeaf(YType.boolean, 'disable'), ['bool'])),
                ])
                self.disable = None
                self._segment_path = lambda: "port-description"
                self._absolute_path = lambda: "Cisco-IOS-XR-ethernet-lldp-cfg:lldp/tlv-select/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Lldp.TlvSelect.PortDescription, ['disable'], name, value)


        class SystemDescription(Entity):
            """
            System Description TLV
            
            .. attribute:: disable
            
            	disable System Description TLV
            	**type**\: bool
            
            	**default value**\: false
            
            

            """

            _prefix = 'ethernet-lldp-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(Lldp.TlvSelect.SystemDescription, self).__init__()

                self.yang_name = "system-description"
                self.yang_parent_name = "tlv-select"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('disable', (YLeaf(YType.boolean, 'disable'), ['bool'])),
                ])
                self.disable = None
                self._segment_path = lambda: "system-description"
                self._absolute_path = lambda: "Cisco-IOS-XR-ethernet-lldp-cfg:lldp/tlv-select/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Lldp.TlvSelect.SystemDescription, ['disable'], name, value)


        class SystemCapabilities(Entity):
            """
            System Capabilities TLV
            
            .. attribute:: disable
            
            	disable System Capabilities TLV
            	**type**\: bool
            
            	**default value**\: false
            
            

            """

            _prefix = 'ethernet-lldp-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(Lldp.TlvSelect.SystemCapabilities, self).__init__()

                self.yang_name = "system-capabilities"
                self.yang_parent_name = "tlv-select"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('disable', (YLeaf(YType.boolean, 'disable'), ['bool'])),
                ])
                self.disable = None
                self._segment_path = lambda: "system-capabilities"
                self._absolute_path = lambda: "Cisco-IOS-XR-ethernet-lldp-cfg:lldp/tlv-select/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Lldp.TlvSelect.SystemCapabilities, ['disable'], name, value)


        class ManagementAddress(Entity):
            """
            Management Address TLV
            
            .. attribute:: disable
            
            	disable Management Address TLV
            	**type**\: bool
            
            	**default value**\: false
            
            

            """

            _prefix = 'ethernet-lldp-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(Lldp.TlvSelect.ManagementAddress, self).__init__()

                self.yang_name = "management-address"
                self.yang_parent_name = "tlv-select"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('disable', (YLeaf(YType.boolean, 'disable'), ['bool'])),
                ])
                self.disable = None
                self._segment_path = lambda: "management-address"
                self._absolute_path = lambda: "Cisco-IOS-XR-ethernet-lldp-cfg:lldp/tlv-select/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Lldp.TlvSelect.ManagementAddress, ['disable'], name, value)

    def clone_ptr(self):
        self._top_entity = Lldp()
        return self._top_entity

