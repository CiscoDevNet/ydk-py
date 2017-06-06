""" Cisco_IOS_XR_ethernet_lldp_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ethernet\-lldp package configuration.

This module contains definitions
for the following management objects\:
  lldp\: Enable LLDP, or configure global LLDP subcommands

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg
module with configuration data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class Lldp(object):
    """
    Enable LLDP, or configure global LLDP subcommands
    
    .. attribute:: enable
    
    	Enable or disable LLDP globally
    	**type**\:  bool
    
    	**default value**\: false
    
    .. attribute:: enable_subintf
    
    	Enable or disable LLDP on Sub\-interfaces as well globally
    	**type**\:  bool
    
    	**default value**\: false
    
    .. attribute:: extended_show_width
    
    	Enable or disable LLDP Show LLDP Neighbor Extended Width
    	**type**\:  bool
    
    	**default value**\: false
    
    .. attribute:: holdtime
    
    	Length  of time  (in sec) that receiver must keep this packet
    	**type**\:  int
    
    	**range:** 0..65535
    
    .. attribute:: reinit
    
    	Delay (in sec) for LLDP initialization on any interface
    	**type**\:  int
    
    	**range:** 2..5
    
    	**default value**\: 2
    
    .. attribute:: timer
    
    	Specify the rate at which LLDP packets are sent (in sec)
    	**type**\:  int
    
    	**range:** 5..65534
    
    	**default value**\: 30
    
    .. attribute:: tlv_select
    
    	Selection of LLDP TLVs to disable
    	**type**\:   :py:class:`TlvSelect <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_cfg.Lldp.TlvSelect>`
    
    	**presence node**\: True
    
    

    """

    _prefix = 'ethernet-lldp-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.enable = None
        self.enable_subintf = None
        self.extended_show_width = None
        self.holdtime = None
        self.reinit = None
        self.timer = None
        self.tlv_select = None


    class TlvSelect(object):
        """
        Selection of LLDP TLVs to disable
        
        .. attribute:: management_address
        
        	Management Address TLV
        	**type**\:   :py:class:`ManagementAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_cfg.Lldp.TlvSelect.ManagementAddress>`
        
        .. attribute:: port_description
        
        	Port Description TLV
        	**type**\:   :py:class:`PortDescription <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_cfg.Lldp.TlvSelect.PortDescription>`
        
        .. attribute:: system_capabilities
        
        	System Capabilities TLV
        	**type**\:   :py:class:`SystemCapabilities <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_cfg.Lldp.TlvSelect.SystemCapabilities>`
        
        .. attribute:: system_description
        
        	System Description TLV
        	**type**\:   :py:class:`SystemDescription <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_cfg.Lldp.TlvSelect.SystemDescription>`
        
        .. attribute:: system_name
        
        	System Name TLV
        	**type**\:   :py:class:`SystemName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_cfg.Lldp.TlvSelect.SystemName>`
        
        .. attribute:: tlv_select_enter
        
        	enter lldp tlv\-select submode
        	**type**\:  bool
        
        	**mandatory**\: True
        
        .. attribute:: _is_presence
        
        	Is present if this instance represents presence container else not
        	**type**\: bool
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'ethernet-lldp-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self._is_presence = True
            self.management_address = Lldp.TlvSelect.ManagementAddress()
            self.management_address.parent = self
            self.port_description = Lldp.TlvSelect.PortDescription()
            self.port_description.parent = self
            self.system_capabilities = Lldp.TlvSelect.SystemCapabilities()
            self.system_capabilities.parent = self
            self.system_description = Lldp.TlvSelect.SystemDescription()
            self.system_description.parent = self
            self.system_name = Lldp.TlvSelect.SystemName()
            self.system_name.parent = self
            self.tlv_select_enter = None


        class SystemName(object):
            """
            System Name TLV
            
            .. attribute:: disable
            
            	disable System Name TLV
            	**type**\:  bool
            
            	**default value**\: false
            
            

            """

            _prefix = 'ethernet-lldp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.disable = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ethernet-lldp-cfg:lldp/Cisco-IOS-XR-ethernet-lldp-cfg:tlv-select/Cisco-IOS-XR-ethernet-lldp-cfg:system-name'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.disable is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_lldp_cfg as meta
                return meta._meta_table['Lldp.TlvSelect.SystemName']['meta_info']


        class PortDescription(object):
            """
            Port Description TLV
            
            .. attribute:: disable
            
            	disable Port Description TLV
            	**type**\:  bool
            
            	**default value**\: false
            
            

            """

            _prefix = 'ethernet-lldp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.disable = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ethernet-lldp-cfg:lldp/Cisco-IOS-XR-ethernet-lldp-cfg:tlv-select/Cisco-IOS-XR-ethernet-lldp-cfg:port-description'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.disable is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_lldp_cfg as meta
                return meta._meta_table['Lldp.TlvSelect.PortDescription']['meta_info']


        class SystemDescription(object):
            """
            System Description TLV
            
            .. attribute:: disable
            
            	disable System Description TLV
            	**type**\:  bool
            
            	**default value**\: false
            
            

            """

            _prefix = 'ethernet-lldp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.disable = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ethernet-lldp-cfg:lldp/Cisco-IOS-XR-ethernet-lldp-cfg:tlv-select/Cisco-IOS-XR-ethernet-lldp-cfg:system-description'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.disable is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_lldp_cfg as meta
                return meta._meta_table['Lldp.TlvSelect.SystemDescription']['meta_info']


        class SystemCapabilities(object):
            """
            System Capabilities TLV
            
            .. attribute:: disable
            
            	disable System Capabilities TLV
            	**type**\:  bool
            
            	**default value**\: false
            
            

            """

            _prefix = 'ethernet-lldp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.disable = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ethernet-lldp-cfg:lldp/Cisco-IOS-XR-ethernet-lldp-cfg:tlv-select/Cisco-IOS-XR-ethernet-lldp-cfg:system-capabilities'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.disable is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_lldp_cfg as meta
                return meta._meta_table['Lldp.TlvSelect.SystemCapabilities']['meta_info']


        class ManagementAddress(object):
            """
            Management Address TLV
            
            .. attribute:: disable
            
            	disable Management Address TLV
            	**type**\:  bool
            
            	**default value**\: false
            
            

            """

            _prefix = 'ethernet-lldp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.disable = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ethernet-lldp-cfg:lldp/Cisco-IOS-XR-ethernet-lldp-cfg:tlv-select/Cisco-IOS-XR-ethernet-lldp-cfg:management-address'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.disable is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_lldp_cfg as meta
                return meta._meta_table['Lldp.TlvSelect.ManagementAddress']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ethernet-lldp-cfg:lldp/Cisco-IOS-XR-ethernet-lldp-cfg:tlv-select'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self._is_presence:
                return True
            if self.management_address is not None and self.management_address._has_data():
                return True

            if self.port_description is not None and self.port_description._has_data():
                return True

            if self.system_capabilities is not None and self.system_capabilities._has_data():
                return True

            if self.system_description is not None and self.system_description._has_data():
                return True

            if self.system_name is not None and self.system_name._has_data():
                return True

            if self.tlv_select_enter is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_lldp_cfg as meta
            return meta._meta_table['Lldp.TlvSelect']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ethernet-lldp-cfg:lldp'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.enable is not None:
            return True

        if self.enable_subintf is not None:
            return True

        if self.extended_show_width is not None:
            return True

        if self.holdtime is not None:
            return True

        if self.reinit is not None:
            return True

        if self.timer is not None:
            return True

        if self.tlv_select is not None and self.tlv_select._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_lldp_cfg as meta
        return meta._meta_table['Lldp']['meta_info']


