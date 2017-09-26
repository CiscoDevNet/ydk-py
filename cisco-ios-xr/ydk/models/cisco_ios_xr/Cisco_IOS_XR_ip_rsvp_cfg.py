""" Cisco_IOS_XR_ip_rsvp_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-rsvp package configuration.

This module contains definitions
for the following management objects\:
  rsvp\: Global RSVP configuration commands

This YANG module augments the
  Cisco\-IOS\-XR\-snmp\-agent\-cfg
module with configuration data.

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class RsvpBc0(Enum):
    """
    RsvpBc0

    Rsvp bc0

    .. data:: bc0 = 1

    	Keyword is bc0

    .. data:: global_pool = 2

    	Keyword is global-pool

    .. data:: not_specified = 3

    	Keyword is not specified

    """

    bc0 = Enum.YLeaf(1, "bc0")

    global_pool = Enum.YLeaf(2, "global-pool")

    not_specified = Enum.YLeaf(3, "not-specified")


class RsvpBc1(Enum):
    """
    RsvpBc1

    Rsvp bc1

    .. data:: bc1 = 1

    	Keyword is bc1

    .. data:: sub_pool = 2

    	Keyword is sub-pool

    """

    bc1 = Enum.YLeaf(1, "bc1")

    sub_pool = Enum.YLeaf(2, "sub-pool")


class RsvpBwCfg(Enum):
    """
    RsvpBwCfg

    Rsvp bw cfg

    .. data:: absolute = 0

    	Configuration is in absolute bandwidth values

    .. data:: percentage = 1

    	Configuration is in percentage of physical

    	bandwidth values

    """

    absolute = Enum.YLeaf(0, "absolute")

    percentage = Enum.YLeaf(1, "percentage")


class RsvpRdm(Enum):
    """
    RsvpRdm

    Rsvp rdm

    .. data:: rdm = 1

    	RDM Keyword Specified

    .. data:: not_specified = 2

    	RDM Keyword Not Specified

    .. data:: use_default_bandwidth = 3

    	Use Default Bandwidth - 75% Link Bandwidth

    """

    rdm = Enum.YLeaf(1, "rdm")

    not_specified = Enum.YLeaf(2, "not-specified")

    use_default_bandwidth = Enum.YLeaf(3, "use-default-bandwidth")



class Rsvp(Entity):
    """
    Global RSVP configuration commands
    
    .. attribute:: authentication
    
    	Configure RSVP authentication
    	**type**\:   :py:class:`Authentication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Authentication>`
    
    .. attribute:: controllers
    
    	Controller table
    	**type**\:   :py:class:`Controllers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Controllers>`
    
    .. attribute:: global_bandwidth
    
    	Configure Global Bandwidth Parameters
    	**type**\:   :py:class:`GlobalBandwidth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.GlobalBandwidth>`
    
    .. attribute:: global_logging
    
    	Global Logging
    	**type**\:   :py:class:`GlobalLogging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.GlobalLogging>`
    
    .. attribute:: interfaces
    
    	Interface table
    	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Interfaces>`
    
    .. attribute:: neighbors
    
    	RSVP Neighbor Table
    	**type**\:   :py:class:`Neighbors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Neighbors>`
    
    .. attribute:: signalling
    
    	Configure Global RSVP signalling parameters
    	**type**\:   :py:class:`Signalling <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Signalling>`
    
    

    """

    _prefix = 'ip-rsvp-cfg'
    _revision = '2017-05-01'

    def __init__(self):
        super(Rsvp, self).__init__()
        self._top_entity = None

        self.yang_name = "rsvp"
        self.yang_parent_name = "Cisco-IOS-XR-ip-rsvp-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"authentication" : ("authentication", Rsvp.Authentication), "controllers" : ("controllers", Rsvp.Controllers), "global-bandwidth" : ("global_bandwidth", Rsvp.GlobalBandwidth), "global-logging" : ("global_logging", Rsvp.GlobalLogging), "interfaces" : ("interfaces", Rsvp.Interfaces), "neighbors" : ("neighbors", Rsvp.Neighbors), "signalling" : ("signalling", Rsvp.Signalling)}
        self._child_list_classes = {}

        self.authentication = Rsvp.Authentication()
        self.authentication.parent = self
        self._children_name_map["authentication"] = "authentication"
        self._children_yang_names.add("authentication")

        self.controllers = Rsvp.Controllers()
        self.controllers.parent = self
        self._children_name_map["controllers"] = "controllers"
        self._children_yang_names.add("controllers")

        self.global_bandwidth = Rsvp.GlobalBandwidth()
        self.global_bandwidth.parent = self
        self._children_name_map["global_bandwidth"] = "global-bandwidth"
        self._children_yang_names.add("global-bandwidth")

        self.global_logging = Rsvp.GlobalLogging()
        self.global_logging.parent = self
        self._children_name_map["global_logging"] = "global-logging"
        self._children_yang_names.add("global-logging")

        self.interfaces = Rsvp.Interfaces()
        self.interfaces.parent = self
        self._children_name_map["interfaces"] = "interfaces"
        self._children_yang_names.add("interfaces")

        self.neighbors = Rsvp.Neighbors()
        self.neighbors.parent = self
        self._children_name_map["neighbors"] = "neighbors"
        self._children_yang_names.add("neighbors")

        self.signalling = Rsvp.Signalling()
        self.signalling.parent = self
        self._children_name_map["signalling"] = "signalling"
        self._children_yang_names.add("signalling")
        self._segment_path = lambda: "Cisco-IOS-XR-ip-rsvp-cfg:rsvp"


    class Authentication(Entity):
        """
        Configure RSVP authentication
        
        .. attribute:: enable
        
        	Enable or disable RSVP authentication
        	**type**\:  bool
        
        .. attribute:: key_chain
        
        	Key chain to authenticate RSVP signalling messages
        	**type**\:  str
        
        	**length:** 1..32
        
        .. attribute:: life_time
        
        	Life time (in seconds) for each security association
        	**type**\:  int
        
        	**range:** 30..86400
        
        	**units**\: second
        
        .. attribute:: window_size
        
        	Window\-size to limit number of out\-of\-order messages
        	**type**\:  int
        
        	**range:** 1..64
        
        

        """

        _prefix = 'ip-rsvp-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(Rsvp.Authentication, self).__init__()

            self.yang_name = "authentication"
            self.yang_parent_name = "rsvp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.enable = YLeaf(YType.boolean, "enable")

            self.key_chain = YLeaf(YType.str, "key-chain")

            self.life_time = YLeaf(YType.uint32, "life-time")

            self.window_size = YLeaf(YType.uint32, "window-size")
            self._segment_path = lambda: "authentication"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-rsvp-cfg:rsvp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Rsvp.Authentication, ['enable', 'key_chain', 'life_time', 'window_size'], name, value)


    class Controllers(Entity):
        """
        Controller table
        
        .. attribute:: controller
        
        	Controller configuration
        	**type**\: list of    :py:class:`Controller <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Controllers.Controller>`
        
        

        """

        _prefix = 'ip-rsvp-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(Rsvp.Controllers, self).__init__()

            self.yang_name = "controllers"
            self.yang_parent_name = "rsvp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"controller" : ("controller", Rsvp.Controllers.Controller)}

            self.controller = YList(self)
            self._segment_path = lambda: "controllers"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-rsvp-cfg:rsvp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Rsvp.Controllers, [], name, value)


        class Controller(Entity):
            """
            Controller configuration
            
            .. attribute:: controller_name  <key>
            
            	Name of controller
            	**type**\:  str
            
            	**pattern:** [a\-zA\-Z0\-9./\-]+
            
            .. attribute:: cntl_signalling
            
            	Configure RSVP signalling parameters
            	**type**\:   :py:class:`CntlSignalling <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Controllers.Controller.CntlSignalling>`
            
            .. attribute:: enable
            
            	Enable RSVP on an interface
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'ip-rsvp-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(Rsvp.Controllers.Controller, self).__init__()

                self.yang_name = "controller"
                self.yang_parent_name = "controllers"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"cntl-signalling" : ("cntl_signalling", Rsvp.Controllers.Controller.CntlSignalling)}
                self._child_list_classes = {}

                self.controller_name = YLeaf(YType.str, "controller-name")

                self.enable = YLeaf(YType.empty, "enable")

                self.cntl_signalling = Rsvp.Controllers.Controller.CntlSignalling()
                self.cntl_signalling.parent = self
                self._children_name_map["cntl_signalling"] = "cntl-signalling"
                self._children_yang_names.add("cntl-signalling")
                self._segment_path = lambda: "controller" + "[controller-name='" + self.controller_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-rsvp-cfg:rsvp/controllers/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Rsvp.Controllers.Controller, ['controller_name', 'enable'], name, value)


            class CntlSignalling(Entity):
                """
                Configure RSVP signalling parameters
                
                .. attribute:: out_of_band
                
                	Configure RSVP out\-of\-band signalling parameters
                	**type**\:   :py:class:`OutOfBand <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Controllers.Controller.CntlSignalling.OutOfBand>`
                
                

                """

                _prefix = 'ip-rsvp-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Rsvp.Controllers.Controller.CntlSignalling, self).__init__()

                    self.yang_name = "cntl-signalling"
                    self.yang_parent_name = "controller"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"out-of-band" : ("out_of_band", Rsvp.Controllers.Controller.CntlSignalling.OutOfBand)}
                    self._child_list_classes = {}

                    self.out_of_band = Rsvp.Controllers.Controller.CntlSignalling.OutOfBand()
                    self.out_of_band.parent = self
                    self._children_name_map["out_of_band"] = "out-of-band"
                    self._children_yang_names.add("out-of-band")
                    self._segment_path = lambda: "cntl-signalling"


                class OutOfBand(Entity):
                    """
                    Configure RSVP out\-of\-band signalling parameters
                    
                    .. attribute:: missed_messages
                    
                    	Configure max number of consecutive missed messages for state expiry for out\-of\-band tunnels
                    	**type**\:  int
                    
                    	**range:** 1..110000
                    
                    	**default value**\: 38000
                    
                    .. attribute:: refresh_interval
                    
                    	Configure interval between successive refreshes for out\-of\-band tunnels
                    	**type**\:  int
                    
                    	**range:** 180..86400
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'ip-rsvp-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Rsvp.Controllers.Controller.CntlSignalling.OutOfBand, self).__init__()

                        self.yang_name = "out-of-band"
                        self.yang_parent_name = "cntl-signalling"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.missed_messages = YLeaf(YType.uint32, "missed-messages")

                        self.refresh_interval = YLeaf(YType.uint32, "refresh-interval")
                        self._segment_path = lambda: "out-of-band"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Rsvp.Controllers.Controller.CntlSignalling.OutOfBand, ['missed_messages', 'refresh_interval'], name, value)


    class GlobalBandwidth(Entity):
        """
        Configure Global Bandwidth Parameters
        
        .. attribute:: default_interface_percent
        
        	Configure Global RSVP signalling parameters
        	**type**\:   :py:class:`DefaultInterfacePercent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.GlobalBandwidth.DefaultInterfacePercent>`
        
        

        """

        _prefix = 'ip-rsvp-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(Rsvp.GlobalBandwidth, self).__init__()

            self.yang_name = "global-bandwidth"
            self.yang_parent_name = "rsvp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"default-interface-percent" : ("default_interface_percent", Rsvp.GlobalBandwidth.DefaultInterfacePercent)}
            self._child_list_classes = {}

            self.default_interface_percent = Rsvp.GlobalBandwidth.DefaultInterfacePercent()
            self.default_interface_percent.parent = self
            self._children_name_map["default_interface_percent"] = "default-interface-percent"
            self._children_yang_names.add("default-interface-percent")
            self._segment_path = lambda: "global-bandwidth"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-rsvp-cfg:rsvp/%s" % self._segment_path()


        class DefaultInterfacePercent(Entity):
            """
            Configure Global RSVP signalling parameters
            
            .. attribute:: mam
            
            	Configure global default MAM I/F percent bandwidth parameters
            	**type**\:   :py:class:`Mam <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.GlobalBandwidth.DefaultInterfacePercent.Mam>`
            
            .. attribute:: rdm
            
            	Configure global default RDM I/F percent bandwidth parameters
            	**type**\:   :py:class:`Rdm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.GlobalBandwidth.DefaultInterfacePercent.Rdm>`
            
            

            """

            _prefix = 'ip-rsvp-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(Rsvp.GlobalBandwidth.DefaultInterfacePercent, self).__init__()

                self.yang_name = "default-interface-percent"
                self.yang_parent_name = "global-bandwidth"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"mam" : ("mam", Rsvp.GlobalBandwidth.DefaultInterfacePercent.Mam), "rdm" : ("rdm", Rsvp.GlobalBandwidth.DefaultInterfacePercent.Rdm)}
                self._child_list_classes = {}

                self.mam = Rsvp.GlobalBandwidth.DefaultInterfacePercent.Mam()
                self.mam.parent = self
                self._children_name_map["mam"] = "mam"
                self._children_yang_names.add("mam")

                self.rdm = Rsvp.GlobalBandwidth.DefaultInterfacePercent.Rdm()
                self.rdm.parent = self
                self._children_name_map["rdm"] = "rdm"
                self._children_yang_names.add("rdm")
                self._segment_path = lambda: "default-interface-percent"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-rsvp-cfg:rsvp/global-bandwidth/%s" % self._segment_path()


            class Mam(Entity):
                """
                Configure global default MAM I/F percent
                bandwidth parameters
                
                .. attribute:: bc0_percent
                
                	Default BC0 pool I/F % B/W 
                	**type**\:  int
                
                	**range:** 0..10000
                
                .. attribute:: bc1_percent
                
                	Default BC1 pool I/F % B/W 
                	**type**\:  int
                
                	**range:** 0..10000
                
                .. attribute:: max_res_percent
                
                	Default maximum reservable I/F % B/W 
                	**type**\:  int
                
                	**range:** 0..10000
                
                

                """

                _prefix = 'ip-rsvp-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Rsvp.GlobalBandwidth.DefaultInterfacePercent.Mam, self).__init__()

                    self.yang_name = "mam"
                    self.yang_parent_name = "default-interface-percent"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.bc0_percent = YLeaf(YType.uint32, "bc0-percent")

                    self.bc1_percent = YLeaf(YType.uint32, "bc1-percent")

                    self.max_res_percent = YLeaf(YType.uint32, "max-res-percent")
                    self._segment_path = lambda: "mam"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-rsvp-cfg:rsvp/global-bandwidth/default-interface-percent/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Rsvp.GlobalBandwidth.DefaultInterfacePercent.Mam, ['bc0_percent', 'bc1_percent', 'max_res_percent'], name, value)


            class Rdm(Entity):
                """
                Configure global default RDM I/F percent
                bandwidth parameters
                
                .. attribute:: bc0_percent
                
                	Default BC0 pool I/F % B/W 
                	**type**\:  int
                
                	**range:** 0..10000
                
                .. attribute:: bc1_percent
                
                	Default BC1 pool I/F % B/W 
                	**type**\:  int
                
                	**range:** 0..10000
                
                

                """

                _prefix = 'ip-rsvp-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Rsvp.GlobalBandwidth.DefaultInterfacePercent.Rdm, self).__init__()

                    self.yang_name = "rdm"
                    self.yang_parent_name = "default-interface-percent"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.bc0_percent = YLeaf(YType.uint32, "bc0-percent")

                    self.bc1_percent = YLeaf(YType.uint32, "bc1-percent")
                    self._segment_path = lambda: "rdm"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-rsvp-cfg:rsvp/global-bandwidth/default-interface-percent/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Rsvp.GlobalBandwidth.DefaultInterfacePercent.Rdm, ['bc0_percent', 'bc1_percent'], name, value)


    class GlobalLogging(Entity):
        """
        Global Logging
        
        .. attribute:: log_issu_status
        
        	Enable ISSU Status Logging
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: log_nsr_status
        
        	Enable NSR Status Logging
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'ip-rsvp-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(Rsvp.GlobalLogging, self).__init__()

            self.yang_name = "global-logging"
            self.yang_parent_name = "rsvp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.log_issu_status = YLeaf(YType.empty, "log-issu-status")

            self.log_nsr_status = YLeaf(YType.empty, "log-nsr-status")
            self._segment_path = lambda: "global-logging"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-rsvp-cfg:rsvp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Rsvp.GlobalLogging, ['log_issu_status', 'log_nsr_status'], name, value)


    class Interfaces(Entity):
        """
        Interface table
        
        .. attribute:: interface
        
        	Interface configuration
        	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Interfaces.Interface>`
        
        

        """

        _prefix = 'ip-rsvp-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(Rsvp.Interfaces, self).__init__()

            self.yang_name = "interfaces"
            self.yang_parent_name = "rsvp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"interface" : ("interface", Rsvp.Interfaces.Interface)}

            self.interface = YList(self)
            self._segment_path = lambda: "interfaces"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-rsvp-cfg:rsvp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Rsvp.Interfaces, [], name, value)


        class Interface(Entity):
            """
            Interface configuration
            
            .. attribute:: name  <key>
            
            	Name of interface
            	**type**\:  str
            
            	**pattern:** [a\-zA\-Z0\-9./\-]+
            
            .. attribute:: authentication
            
            	Configure RSVP authentication
            	**type**\:   :py:class:`Authentication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Interfaces.Interface.Authentication>`
            
            .. attribute:: bandwidth
            
            	Configure Bandwidth
            	**type**\:   :py:class:`Bandwidth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Interfaces.Interface.Bandwidth>`
            
            .. attribute:: enable
            
            	Enable RSVP on an interface
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: if_signalling
            
            	Configure RSVP signalling parameters
            	**type**\:   :py:class:`IfSignalling <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Interfaces.Interface.IfSignalling>`
            
            

            """

            _prefix = 'ip-rsvp-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(Rsvp.Interfaces.Interface, self).__init__()

                self.yang_name = "interface"
                self.yang_parent_name = "interfaces"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"authentication" : ("authentication", Rsvp.Interfaces.Interface.Authentication), "bandwidth" : ("bandwidth", Rsvp.Interfaces.Interface.Bandwidth), "if-signalling" : ("if_signalling", Rsvp.Interfaces.Interface.IfSignalling)}
                self._child_list_classes = {}

                self.name = YLeaf(YType.str, "name")

                self.enable = YLeaf(YType.empty, "enable")

                self.authentication = Rsvp.Interfaces.Interface.Authentication()
                self.authentication.parent = self
                self._children_name_map["authentication"] = "authentication"
                self._children_yang_names.add("authentication")

                self.bandwidth = Rsvp.Interfaces.Interface.Bandwidth()
                self.bandwidth.parent = self
                self._children_name_map["bandwidth"] = "bandwidth"
                self._children_yang_names.add("bandwidth")

                self.if_signalling = Rsvp.Interfaces.Interface.IfSignalling()
                self.if_signalling.parent = self
                self._children_name_map["if_signalling"] = "if-signalling"
                self._children_yang_names.add("if-signalling")
                self._segment_path = lambda: "interface" + "[name='" + self.name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-rsvp-cfg:rsvp/interfaces/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Rsvp.Interfaces.Interface, ['name', 'enable'], name, value)


            class Authentication(Entity):
                """
                Configure RSVP authentication
                
                .. attribute:: enable
                
                	Enable or disable RSVP authentication
                	**type**\:  bool
                
                .. attribute:: key_chain
                
                	Key chain to authenticate RSVP signalling messages
                	**type**\:  str
                
                	**length:** 1..32
                
                .. attribute:: life_time
                
                	Life time (in seconds) for each security association
                	**type**\:  int
                
                	**range:** 30..86400
                
                	**units**\: second
                
                .. attribute:: window_size
                
                	Window\-size to limit number of out\-of\-order messages
                	**type**\:  int
                
                	**range:** 1..64
                
                

                """

                _prefix = 'ip-rsvp-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Rsvp.Interfaces.Interface.Authentication, self).__init__()

                    self.yang_name = "authentication"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.enable = YLeaf(YType.boolean, "enable")

                    self.key_chain = YLeaf(YType.str, "key-chain")

                    self.life_time = YLeaf(YType.uint32, "life-time")

                    self.window_size = YLeaf(YType.uint32, "window-size")
                    self._segment_path = lambda: "authentication"

                def __setattr__(self, name, value):
                    self._perform_setattr(Rsvp.Interfaces.Interface.Authentication, ['enable', 'key_chain', 'life_time', 'window_size'], name, value)


            class Bandwidth(Entity):
                """
                Configure Bandwidth
                
                .. attribute:: mam
                
                	Configure MAM bandwidth parameters
                	**type**\:   :py:class:`Mam <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Interfaces.Interface.Bandwidth.Mam>`
                
                .. attribute:: rdm
                
                	Configure RDM bandwidth parameters
                	**type**\:   :py:class:`Rdm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Interfaces.Interface.Bandwidth.Rdm>`
                
                

                """

                _prefix = 'ip-rsvp-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Rsvp.Interfaces.Interface.Bandwidth, self).__init__()

                    self.yang_name = "bandwidth"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"mam" : ("mam", Rsvp.Interfaces.Interface.Bandwidth.Mam), "rdm" : ("rdm", Rsvp.Interfaces.Interface.Bandwidth.Rdm)}
                    self._child_list_classes = {}

                    self.mam = Rsvp.Interfaces.Interface.Bandwidth.Mam()
                    self.mam.parent = self
                    self._children_name_map["mam"] = "mam"
                    self._children_yang_names.add("mam")

                    self.rdm = Rsvp.Interfaces.Interface.Bandwidth.Rdm()
                    self.rdm.parent = self
                    self._children_name_map["rdm"] = "rdm"
                    self._children_yang_names.add("rdm")
                    self._segment_path = lambda: "bandwidth"


                class Mam(Entity):
                    """
                    Configure MAM bandwidth parameters
                    
                    .. attribute:: bandwidth_mode
                    
                    	Absolute or Percentage bandwidth mode
                    	**type**\:   :py:class:`RsvpBwCfg <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.RsvpBwCfg>`
                    
                    	**units**\: percentage
                    
                    .. attribute:: bc0_bandwidth
                    
                    	Reservable bandwidth in BC0 (Kbps or percent of physical bandwidth)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: bc1_bandwidth
                    
                    	Reservable bandwidth in BC1 (Kbps or percent of physical bandwidth)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: max_resv_bandwidth
                    
                    	Maximum reservable bandwidth (Kbps or percent of physical bandwidth)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: max_resv_flow
                    
                    	Largest reservable flow (Kbps or percent of physical bandwidth)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ip-rsvp-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Rsvp.Interfaces.Interface.Bandwidth.Mam, self).__init__()

                        self.yang_name = "mam"
                        self.yang_parent_name = "bandwidth"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.bandwidth_mode = YLeaf(YType.enumeration, "bandwidth-mode")

                        self.bc0_bandwidth = YLeaf(YType.uint32, "bc0-bandwidth")

                        self.bc1_bandwidth = YLeaf(YType.uint32, "bc1-bandwidth")

                        self.max_resv_bandwidth = YLeaf(YType.uint32, "max-resv-bandwidth")

                        self.max_resv_flow = YLeaf(YType.uint32, "max-resv-flow")
                        self._segment_path = lambda: "mam"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Rsvp.Interfaces.Interface.Bandwidth.Mam, ['bandwidth_mode', 'bc0_bandwidth', 'bc1_bandwidth', 'max_resv_bandwidth', 'max_resv_flow'], name, value)


                class Rdm(Entity):
                    """
                    Configure RDM bandwidth parameters
                    
                    .. attribute:: bandwidth_mode
                    
                    	Absolute or Percentage bandwidth mode
                    	**type**\:   :py:class:`RsvpBwCfg <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.RsvpBwCfg>`
                    
                    	**units**\: percentage
                    
                    .. attribute:: bc0_bandwidth
                    
                    	Reservable bandwidth in BC0 (Kbps or percent of physical bandwidth)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: bc0_keyword
                    
                    	Set requests should always use BC0
                    	**type**\:   :py:class:`RsvpBc0 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.RsvpBc0>`
                    
                    .. attribute:: bc1_bandwidth
                    
                    	Reservable bandwidth in BC1 (Kbps or percent of physical bandwidth)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: bc1_keyword
                    
                    	Set requests should always use BC1
                    	**type**\:   :py:class:`RsvpBc1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.RsvpBc1>`
                    
                    .. attribute:: max_resv_flow
                    
                    	Largest reservable flow (Kbps or percent of physical bandwidth)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rdm_keyword
                    
                    	Set requests should always use RDM
                    	**type**\:   :py:class:`RsvpRdm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.RsvpRdm>`
                    
                    

                    """

                    _prefix = 'ip-rsvp-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Rsvp.Interfaces.Interface.Bandwidth.Rdm, self).__init__()

                        self.yang_name = "rdm"
                        self.yang_parent_name = "bandwidth"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.bandwidth_mode = YLeaf(YType.enumeration, "bandwidth-mode")

                        self.bc0_bandwidth = YLeaf(YType.uint32, "bc0-bandwidth")

                        self.bc0_keyword = YLeaf(YType.enumeration, "bc0-keyword")

                        self.bc1_bandwidth = YLeaf(YType.uint32, "bc1-bandwidth")

                        self.bc1_keyword = YLeaf(YType.enumeration, "bc1-keyword")

                        self.max_resv_flow = YLeaf(YType.uint32, "max-resv-flow")

                        self.rdm_keyword = YLeaf(YType.enumeration, "rdm-keyword")
                        self._segment_path = lambda: "rdm"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Rsvp.Interfaces.Interface.Bandwidth.Rdm, ['bandwidth_mode', 'bc0_bandwidth', 'bc0_keyword', 'bc1_bandwidth', 'bc1_keyword', 'max_resv_flow', 'rdm_keyword'], name, value)


            class IfSignalling(Entity):
                """
                Configure RSVP signalling parameters
                
                .. attribute:: dscp
                
                	Differentiated Services Code Point (DSCP)
                	**type**\:  int
                
                	**range:** 0..63
                
                .. attribute:: hello_graceful_restart_if_based
                
                	Enable IF\-based Hello adjacency on a RSVP interface
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: interval_rate
                
                	Configure number of messages to be sent per interval
                	**type**\:   :py:class:`IntervalRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Interfaces.Interface.IfSignalling.IntervalRate>`
                
                .. attribute:: missed_messages
                
                	Configure max number of consecutive missed messages for state expiry
                	**type**\:  int
                
                	**range:** 1..8
                
                	**default value**\: 4
                
                .. attribute:: out_of_band
                
                	Configure RSVP out\-of\-band signalling parameters
                	**type**\:   :py:class:`OutOfBand <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Interfaces.Interface.IfSignalling.OutOfBand>`
                
                .. attribute:: pacing
                
                	Enable rate\-limiting on the interface
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: refresh_interval
                
                	Configure interval between successive refreshes
                	**type**\:  int
                
                	**range:** 10..180
                
                	**units**\: second
                
                	**default value**\: 45
                
                .. attribute:: refresh_reduction
                
                	Configure RSVP Refresh Reduction parameters
                	**type**\:   :py:class:`RefreshReduction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Interfaces.Interface.IfSignalling.RefreshReduction>`
                
                

                """

                _prefix = 'ip-rsvp-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Rsvp.Interfaces.Interface.IfSignalling, self).__init__()

                    self.yang_name = "if-signalling"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"interval-rate" : ("interval_rate", Rsvp.Interfaces.Interface.IfSignalling.IntervalRate), "out-of-band" : ("out_of_band", Rsvp.Interfaces.Interface.IfSignalling.OutOfBand), "refresh-reduction" : ("refresh_reduction", Rsvp.Interfaces.Interface.IfSignalling.RefreshReduction)}
                    self._child_list_classes = {}

                    self.dscp = YLeaf(YType.uint32, "dscp")

                    self.hello_graceful_restart_if_based = YLeaf(YType.empty, "hello-graceful-restart-if-based")

                    self.missed_messages = YLeaf(YType.uint32, "missed-messages")

                    self.pacing = YLeaf(YType.empty, "pacing")

                    self.refresh_interval = YLeaf(YType.uint32, "refresh-interval")

                    self.interval_rate = Rsvp.Interfaces.Interface.IfSignalling.IntervalRate()
                    self.interval_rate.parent = self
                    self._children_name_map["interval_rate"] = "interval-rate"
                    self._children_yang_names.add("interval-rate")

                    self.out_of_band = Rsvp.Interfaces.Interface.IfSignalling.OutOfBand()
                    self.out_of_band.parent = self
                    self._children_name_map["out_of_band"] = "out-of-band"
                    self._children_yang_names.add("out-of-band")

                    self.refresh_reduction = Rsvp.Interfaces.Interface.IfSignalling.RefreshReduction()
                    self.refresh_reduction.parent = self
                    self._children_name_map["refresh_reduction"] = "refresh-reduction"
                    self._children_yang_names.add("refresh-reduction")
                    self._segment_path = lambda: "if-signalling"

                def __setattr__(self, name, value):
                    self._perform_setattr(Rsvp.Interfaces.Interface.IfSignalling, ['dscp', 'hello_graceful_restart_if_based', 'missed_messages', 'pacing', 'refresh_interval'], name, value)


                class IntervalRate(Entity):
                    """
                    Configure number of messages to be sent per
                    interval
                    
                    .. attribute:: interval_size
                    
                    	Size of an interval (milliseconds)
                    	**type**\:  int
                    
                    	**range:** 250..2000
                    
                    	**units**\: millisecond
                    
                    	**default value**\: 1000
                    
                    .. attribute:: messages_per_interval
                    
                    	Number of messages to be sent per interval
                    	**type**\:  int
                    
                    	**range:** 1..500
                    
                    	**default value**\: 100
                    
                    

                    """

                    _prefix = 'ip-rsvp-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Rsvp.Interfaces.Interface.IfSignalling.IntervalRate, self).__init__()

                        self.yang_name = "interval-rate"
                        self.yang_parent_name = "if-signalling"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.interval_size = YLeaf(YType.uint32, "interval-size")

                        self.messages_per_interval = YLeaf(YType.uint32, "messages-per-interval")
                        self._segment_path = lambda: "interval-rate"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Rsvp.Interfaces.Interface.IfSignalling.IntervalRate, ['interval_size', 'messages_per_interval'], name, value)


                class OutOfBand(Entity):
                    """
                    Configure RSVP out\-of\-band signalling parameters
                    
                    .. attribute:: missed_messages
                    
                    	Configure max number of consecutive missed messages for state expiry for out\-of\-band tunnels
                    	**type**\:  int
                    
                    	**range:** 1..110000
                    
                    	**default value**\: 38000
                    
                    .. attribute:: refresh_interval
                    
                    	Configure interval between successive refreshes for out\-of\-band tunnels
                    	**type**\:  int
                    
                    	**range:** 180..86400
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'ip-rsvp-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Rsvp.Interfaces.Interface.IfSignalling.OutOfBand, self).__init__()

                        self.yang_name = "out-of-band"
                        self.yang_parent_name = "if-signalling"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.missed_messages = YLeaf(YType.uint32, "missed-messages")

                        self.refresh_interval = YLeaf(YType.uint32, "refresh-interval")
                        self._segment_path = lambda: "out-of-band"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Rsvp.Interfaces.Interface.IfSignalling.OutOfBand, ['missed_messages', 'refresh_interval'], name, value)


                class RefreshReduction(Entity):
                    """
                    Configure RSVP Refresh Reduction parameters
                    
                    .. attribute:: bundle_message_max_size
                    
                    	Configure maximum size of a single RSVP Bundle message
                    	**type**\:  int
                    
                    	**range:** 512..65000
                    
                    	**units**\: byte
                    
                    	**default value**\: 4096
                    
                    .. attribute:: disable
                    
                    	Disable refresh reduction
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: reliable_ack_hold_time
                    
                    	Configure hold time for sending RSVP ACK message(s)
                    	**type**\:  int
                    
                    	**range:** 100..5000
                    
                    	**units**\: millisecond
                    
                    	**default value**\: 400
                    
                    .. attribute:: reliable_ack_max_size
                    
                    	Configure max size of a single RSVP ACK message
                    	**type**\:  int
                    
                    	**range:** 20..65000
                    
                    	**units**\: byte
                    
                    	**default value**\: 4096
                    
                    .. attribute:: reliable_retransmit_time
                    
                    	Configure min delay to wait for an ACK before a retransmit
                    	**type**\:  int
                    
                    	**range:** 100..10000
                    
                    	**units**\: millisecond
                    
                    	**default value**\: 2100
                    
                    .. attribute:: reliable_s_refresh
                    
                    	Configure use of reliable messaging for summary refresh
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: summary_max_size
                    
                    	Configure max size of a single RSVP summary refresh message
                    	**type**\:  int
                    
                    	**range:** 20..65000
                    
                    	**units**\: byte
                    
                    	**default value**\: 4096
                    
                    

                    """

                    _prefix = 'ip-rsvp-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Rsvp.Interfaces.Interface.IfSignalling.RefreshReduction, self).__init__()

                        self.yang_name = "refresh-reduction"
                        self.yang_parent_name = "if-signalling"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.bundle_message_max_size = YLeaf(YType.uint32, "bundle-message-max-size")

                        self.disable = YLeaf(YType.empty, "disable")

                        self.reliable_ack_hold_time = YLeaf(YType.uint32, "reliable-ack-hold-time")

                        self.reliable_ack_max_size = YLeaf(YType.uint32, "reliable-ack-max-size")

                        self.reliable_retransmit_time = YLeaf(YType.uint32, "reliable-retransmit-time")

                        self.reliable_s_refresh = YLeaf(YType.empty, "reliable-s-refresh")

                        self.summary_max_size = YLeaf(YType.uint32, "summary-max-size")
                        self._segment_path = lambda: "refresh-reduction"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Rsvp.Interfaces.Interface.IfSignalling.RefreshReduction, ['bundle_message_max_size', 'disable', 'reliable_ack_hold_time', 'reliable_ack_max_size', 'reliable_retransmit_time', 'reliable_s_refresh', 'summary_max_size'], name, value)


    class Neighbors(Entity):
        """
        RSVP Neighbor Table
        
        .. attribute:: neighbor
        
        	RSVP neighbor configuration
        	**type**\: list of    :py:class:`Neighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Neighbors.Neighbor>`
        
        

        """

        _prefix = 'ip-rsvp-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(Rsvp.Neighbors, self).__init__()

            self.yang_name = "neighbors"
            self.yang_parent_name = "rsvp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"neighbor" : ("neighbor", Rsvp.Neighbors.Neighbor)}

            self.neighbor = YList(self)
            self._segment_path = lambda: "neighbors"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-rsvp-cfg:rsvp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Rsvp.Neighbors, [], name, value)


        class Neighbor(Entity):
            """
            RSVP neighbor configuration
            
            .. attribute:: neighbor  <key>
            
            	Neighbor IP address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: authentication
            
            	Configure RSVP authentication
            	**type**\:   :py:class:`Authentication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Neighbors.Neighbor.Authentication>`
            
            

            """

            _prefix = 'ip-rsvp-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(Rsvp.Neighbors.Neighbor, self).__init__()

                self.yang_name = "neighbor"
                self.yang_parent_name = "neighbors"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"authentication" : ("authentication", Rsvp.Neighbors.Neighbor.Authentication)}
                self._child_list_classes = {}

                self.neighbor = YLeaf(YType.str, "neighbor")

                self.authentication = Rsvp.Neighbors.Neighbor.Authentication()
                self.authentication.parent = self
                self._children_name_map["authentication"] = "authentication"
                self._children_yang_names.add("authentication")
                self._segment_path = lambda: "neighbor" + "[neighbor='" + self.neighbor.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-rsvp-cfg:rsvp/neighbors/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Rsvp.Neighbors.Neighbor, ['neighbor'], name, value)


            class Authentication(Entity):
                """
                Configure RSVP authentication
                
                .. attribute:: enable
                
                	Enable or disable RSVP authentication
                	**type**\:  bool
                
                .. attribute:: key_chain
                
                	Key chain to authenticate RSVP signalling messages
                	**type**\:  str
                
                	**length:** 1..32
                
                .. attribute:: life_time
                
                	Life time (in seconds) for each security association
                	**type**\:  int
                
                	**range:** 30..86400
                
                	**units**\: second
                
                .. attribute:: window_size
                
                	Window\-size to limit number of out\-of\-order messages
                	**type**\:  int
                
                	**range:** 1..64
                
                

                """

                _prefix = 'ip-rsvp-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Rsvp.Neighbors.Neighbor.Authentication, self).__init__()

                    self.yang_name = "authentication"
                    self.yang_parent_name = "neighbor"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.enable = YLeaf(YType.boolean, "enable")

                    self.key_chain = YLeaf(YType.str, "key-chain")

                    self.life_time = YLeaf(YType.uint32, "life-time")

                    self.window_size = YLeaf(YType.uint32, "window-size")
                    self._segment_path = lambda: "authentication"

                def __setattr__(self, name, value):
                    self._perform_setattr(Rsvp.Neighbors.Neighbor.Authentication, ['enable', 'key_chain', 'life_time', 'window_size'], name, value)


    class Signalling(Entity):
        """
        Configure Global RSVP signalling parameters
        
        .. attribute:: checksum
        
        	RSVP message checksum computation
        	**type**\:   :py:class:`Checksum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Signalling.Checksum>`
        
        .. attribute:: global_out_of_band
        
        	Configure out\-of\-band signalling parameters
        	**type**\:   :py:class:`GlobalOutOfBand <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Signalling.GlobalOutOfBand>`
        
        .. attribute:: graceful_restart
        
        	Configure RSVP Graceful\-Restart parameters
        	**type**\:   :py:class:`GracefulRestart <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Signalling.GracefulRestart>`
        
        .. attribute:: hello_graceful_restart_interval
        
        	Configure interval between successive Hello messages
        	**type**\:  int
        
        	**range:** 3000..30000
        
        	**units**\: millisecond
        
        	**default value**\: 5000
        
        .. attribute:: hello_graceful_restart_misses
        
        	Configure max number of consecutive missed Hello messages
        	**type**\:  int
        
        	**range:** 1..10
        
        	**default value**\: 3
        
        .. attribute:: pesr
        
        	Sending Path Error with State\-Removal flag
        	**type**\:   :py:class:`Pesr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Signalling.Pesr>`
        
        .. attribute:: prefix_filtering
        
        	Configure prefix filtering parameters
        	**type**\:   :py:class:`PrefixFiltering <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Signalling.PrefixFiltering>`
        
        

        """

        _prefix = 'ip-rsvp-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(Rsvp.Signalling, self).__init__()

            self.yang_name = "signalling"
            self.yang_parent_name = "rsvp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"checksum" : ("checksum", Rsvp.Signalling.Checksum), "global-out-of-band" : ("global_out_of_band", Rsvp.Signalling.GlobalOutOfBand), "graceful-restart" : ("graceful_restart", Rsvp.Signalling.GracefulRestart), "pesr" : ("pesr", Rsvp.Signalling.Pesr), "prefix-filtering" : ("prefix_filtering", Rsvp.Signalling.PrefixFiltering)}
            self._child_list_classes = {}

            self.hello_graceful_restart_interval = YLeaf(YType.uint32, "hello-graceful-restart-interval")

            self.hello_graceful_restart_misses = YLeaf(YType.uint32, "hello-graceful-restart-misses")

            self.checksum = Rsvp.Signalling.Checksum()
            self.checksum.parent = self
            self._children_name_map["checksum"] = "checksum"
            self._children_yang_names.add("checksum")

            self.global_out_of_band = Rsvp.Signalling.GlobalOutOfBand()
            self.global_out_of_band.parent = self
            self._children_name_map["global_out_of_band"] = "global-out-of-band"
            self._children_yang_names.add("global-out-of-band")

            self.graceful_restart = Rsvp.Signalling.GracefulRestart()
            self.graceful_restart.parent = self
            self._children_name_map["graceful_restart"] = "graceful-restart"
            self._children_yang_names.add("graceful-restart")

            self.pesr = Rsvp.Signalling.Pesr()
            self.pesr.parent = self
            self._children_name_map["pesr"] = "pesr"
            self._children_yang_names.add("pesr")

            self.prefix_filtering = Rsvp.Signalling.PrefixFiltering()
            self.prefix_filtering.parent = self
            self._children_name_map["prefix_filtering"] = "prefix-filtering"
            self._children_yang_names.add("prefix-filtering")
            self._segment_path = lambda: "signalling"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-rsvp-cfg:rsvp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Rsvp.Signalling, ['hello_graceful_restart_interval', 'hello_graceful_restart_misses'], name, value)


        class Checksum(Entity):
            """
            RSVP message checksum computation
            
            .. attribute:: disable
            
            	Disable RSVP message checksum computation
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'ip-rsvp-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(Rsvp.Signalling.Checksum, self).__init__()

                self.yang_name = "checksum"
                self.yang_parent_name = "signalling"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.disable = YLeaf(YType.empty, "disable")
                self._segment_path = lambda: "checksum"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-rsvp-cfg:rsvp/signalling/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Rsvp.Signalling.Checksum, ['disable'], name, value)


        class GlobalOutOfBand(Entity):
            """
            Configure out\-of\-band signalling parameters
            
            .. attribute:: vrf
            
            	VRF used for out\-of\-band control signalling
            	**type**\:  str
            
            	**length:** 1..32
            
            

            """

            _prefix = 'ip-rsvp-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(Rsvp.Signalling.GlobalOutOfBand, self).__init__()

                self.yang_name = "global-out-of-band"
                self.yang_parent_name = "signalling"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.vrf = YLeaf(YType.str, "vrf")
                self._segment_path = lambda: "global-out-of-band"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-rsvp-cfg:rsvp/signalling/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Rsvp.Signalling.GlobalOutOfBand, ['vrf'], name, value)


        class GracefulRestart(Entity):
            """
            Configure RSVP Graceful\-Restart parameters
            
            .. attribute:: enable
            
            	Enable RSVP graceful restart
            	**type**\:  bool
            
            .. attribute:: lsp_class_type
            
            	Send LSP's ctype for recovery and suggested label
            	**type**\:   :py:class:`LspClassType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Signalling.GracefulRestart.LspClassType>`
            
            .. attribute:: recovery_time
            
            	Graceful restart recovery time (seconds)
            	**type**\:  int
            
            	**range:** 0..3600
            
            	**units**\: second
            
            	**default value**\: 120
            
            .. attribute:: restart_time
            
            	Graceful restart time (seconds)
            	**type**\:  int
            
            	**range:** 60..3600
            
            	**units**\: second
            
            	**default value**\: 120
            
            

            """

            _prefix = 'ip-rsvp-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(Rsvp.Signalling.GracefulRestart, self).__init__()

                self.yang_name = "graceful-restart"
                self.yang_parent_name = "signalling"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"lsp-class-type" : ("lsp_class_type", Rsvp.Signalling.GracefulRestart.LspClassType)}
                self._child_list_classes = {}

                self.enable = YLeaf(YType.boolean, "enable")

                self.recovery_time = YLeaf(YType.uint32, "recovery-time")

                self.restart_time = YLeaf(YType.uint32, "restart-time")

                self.lsp_class_type = Rsvp.Signalling.GracefulRestart.LspClassType()
                self.lsp_class_type.parent = self
                self._children_name_map["lsp_class_type"] = "lsp-class-type"
                self._children_yang_names.add("lsp-class-type")
                self._segment_path = lambda: "graceful-restart"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-rsvp-cfg:rsvp/signalling/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Rsvp.Signalling.GracefulRestart, ['enable', 'recovery_time', 'restart_time'], name, value)


            class LspClassType(Entity):
                """
                Send LSP's ctype for recovery and suggested
                label
                
                .. attribute:: enable
                
                	Send LSP's ctype for recovery and suggested label
                	**type**\:  bool
                
                

                """

                _prefix = 'ip-rsvp-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Rsvp.Signalling.GracefulRestart.LspClassType, self).__init__()

                    self.yang_name = "lsp-class-type"
                    self.yang_parent_name = "graceful-restart"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.enable = YLeaf(YType.boolean, "enable")
                    self._segment_path = lambda: "lsp-class-type"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-rsvp-cfg:rsvp/signalling/graceful-restart/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Rsvp.Signalling.GracefulRestart.LspClassType, ['enable'], name, value)


        class Pesr(Entity):
            """
            Sending Path Error with State\-Removal flag
            
            .. attribute:: disable
            
            	Disable RSVP PESR
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'ip-rsvp-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(Rsvp.Signalling.Pesr, self).__init__()

                self.yang_name = "pesr"
                self.yang_parent_name = "signalling"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.disable = YLeaf(YType.empty, "disable")
                self._segment_path = lambda: "pesr"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-rsvp-cfg:rsvp/signalling/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Rsvp.Signalling.Pesr, ['disable'], name, value)


        class PrefixFiltering(Entity):
            """
            Configure prefix filtering parameters
            
            .. attribute:: acl
            
            	Configure an ACL to perform prefix filtering of RSVP Router Alert messages
            	**type**\:  str
            
            	**length:** 1..65
            
            .. attribute:: default_deny_action
            
            	Configure RSVP behaviour for scenarios where ACL match yields a default (implicit) deny
            	**type**\:   :py:class:`DefaultDenyAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Signalling.PrefixFiltering.DefaultDenyAction>`
            
            

            """

            _prefix = 'ip-rsvp-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(Rsvp.Signalling.PrefixFiltering, self).__init__()

                self.yang_name = "prefix-filtering"
                self.yang_parent_name = "signalling"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"default-deny-action" : ("default_deny_action", Rsvp.Signalling.PrefixFiltering.DefaultDenyAction)}
                self._child_list_classes = {}

                self.acl = YLeaf(YType.str, "acl")

                self.default_deny_action = Rsvp.Signalling.PrefixFiltering.DefaultDenyAction()
                self.default_deny_action.parent = self
                self._children_name_map["default_deny_action"] = "default-deny-action"
                self._children_yang_names.add("default-deny-action")
                self._segment_path = lambda: "prefix-filtering"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-rsvp-cfg:rsvp/signalling/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Rsvp.Signalling.PrefixFiltering, ['acl'], name, value)


            class DefaultDenyAction(Entity):
                """
                Configure RSVP behaviour for scenarios where
                ACL match yields a default (implicit) deny
                
                .. attribute:: drop
                
                	Configure RSVP to drop packets when ACL match yields a default (implicit) deny
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'ip-rsvp-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Rsvp.Signalling.PrefixFiltering.DefaultDenyAction, self).__init__()

                    self.yang_name = "default-deny-action"
                    self.yang_parent_name = "prefix-filtering"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.drop = YLeaf(YType.empty, "drop")
                    self._segment_path = lambda: "default-deny-action"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-rsvp-cfg:rsvp/signalling/prefix-filtering/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Rsvp.Signalling.PrefixFiltering.DefaultDenyAction, ['drop'], name, value)

    def clone_ptr(self):
        self._top_entity = Rsvp()
        return self._top_entity

