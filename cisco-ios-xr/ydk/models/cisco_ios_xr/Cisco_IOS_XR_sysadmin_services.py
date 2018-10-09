""" Cisco_IOS_XR_sysadmin_services 

This module contains definitions
for the Calvados model objects.

This module contains a collection of YANG
definitions for Cisco IOS\-XR SysAdmin configuration.

This module defines the services offered in the
sysadmin plane.

Copyright(c) 2016 by Cisco Systems, Inc.
All rights reserved.

Copyright (c) 2012\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Service(Entity):
    """
    
    
    .. attribute:: cli
    
    	
    	**type**\:  :py:class:`Cli <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_services.Service.Cli>`
    
    

    """

    _prefix = 'calvados_services'
    _revision = '2016-11-10'

    def __init__(self):
        super(Service, self).__init__()
        self._top_entity = None

        self.yang_name = "service"
        self.yang_parent_name = "Cisco-IOS-XR-sysadmin-services"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("cli", ("cli", Service.Cli))])
        self._leafs = OrderedDict()

        self.cli = Service.Cli()
        self.cli.parent = self
        self._children_name_map["cli"] = "cli"
        self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-services:service"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Service, [], name, value)


    class Cli(Entity):
        """
        
        
        .. attribute:: interactive
        
        	
        	**type**\:  :py:class:`Interactive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_services.Service.Cli.Interactive>`
        
        

        """

        _prefix = 'calvados_services'
        _revision = '2016-11-10'

        def __init__(self):
            super(Service.Cli, self).__init__()

            self.yang_name = "cli"
            self.yang_parent_name = "service"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("interactive", ("interactive", Service.Cli.Interactive))])
            self._leafs = OrderedDict()

            self.interactive = Service.Cli.Interactive()
            self.interactive.parent = self
            self._children_name_map["interactive"] = "interactive"
            self._segment_path = lambda: "cli"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-services:service/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Service.Cli, [], name, value)


        class Interactive(Entity):
            """
            
            
            .. attribute:: enabled
            
            	
            	**type**\: bool
            
            	**default value**\: true
            
            

            """

            _prefix = 'calvados_services'
            _revision = '2016-11-10'

            def __init__(self):
                super(Service.Cli.Interactive, self).__init__()

                self.yang_name = "interactive"
                self.yang_parent_name = "cli"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('enabled', (YLeaf(YType.boolean, 'enabled'), ['bool'])),
                ])
                self.enabled = None
                self._segment_path = lambda: "interactive"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-services:service/cli/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Service.Cli.Interactive, ['enabled'], name, value)

    def clone_ptr(self):
        self._top_entity = Service()
        return self._top_entity

