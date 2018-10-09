""" Cisco_IOS_XR_sysadmin_sdr_mgr 

This module contains definitions
for the Calvados model objects.

This module contains a collection of YANG
definitions for Cisco IOS\-XR SysAdmin configuration.

This module defines the SDR\-SM support config for SDR

Copyright(c) 2011\-2017 by Cisco Systems, Inc.
All rights reserved.

Copyright (c) 2012\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CardType(Enum):
    """
    CardType (Enum Class)

    The List of supported Card Types

    .. data:: RP = 0

    .. data:: LC = 1

    .. data:: CC = 2

    """

    RP = Enum.YLeaf(0, "RP")

    LC = Enum.YLeaf(1, "LC")

    CC = Enum.YLeaf(2, "CC")


class VmReloadReason(Enum):
    """
    VmReloadReason (Enum Class)

    The List of vm reload reasons

    .. data:: CARD_OFFLINE = 0

    .. data:: CARD_SHUTDOWN = 1

    .. data:: ALL_VM_RELOAD = 2

    .. data:: VM_REQUESTED_GRACEFUL_RELOAD = 3

    .. data:: VM_REQUESTED_UNGRACEFUL_RELOAD = 4

    .. data:: SDR_CLI_REQUESTED = 5

    .. data:: SDR_VCPU_VMEM_CHANGED = 6

    .. data:: SDR_HEARTBEAT_FAILURE = 7

    .. data:: FIRST_BOOT = 8

    .. data:: SMU = 9

    .. data:: REASON_UNKNOWN = 10

    """

    CARD_OFFLINE = Enum.YLeaf(0, "CARD_OFFLINE")

    CARD_SHUTDOWN = Enum.YLeaf(1, "CARD_SHUTDOWN")

    ALL_VM_RELOAD = Enum.YLeaf(2, "ALL_VM_RELOAD")

    VM_REQUESTED_GRACEFUL_RELOAD = Enum.YLeaf(3, "VM_REQUESTED_GRACEFUL_RELOAD")

    VM_REQUESTED_UNGRACEFUL_RELOAD = Enum.YLeaf(4, "VM_REQUESTED_UNGRACEFUL_RELOAD")

    SDR_CLI_REQUESTED = Enum.YLeaf(5, "SDR_CLI_REQUESTED")

    SDR_VCPU_VMEM_CHANGED = Enum.YLeaf(6, "SDR_VCPU_VMEM_CHANGED")

    SDR_HEARTBEAT_FAILURE = Enum.YLeaf(7, "SDR_HEARTBEAT_FAILURE")

    FIRST_BOOT = Enum.YLeaf(8, "FIRST_BOOT")

    SMU = Enum.YLeaf(9, "SMU")

    REASON_UNKNOWN = Enum.YLeaf(10, "REASON_UNKNOWN")



class SdrConfig(Entity):
    """
    
    
    .. attribute:: sdr
    
    	Add/Edit a Secure Domain Router by name
    	**type**\: list of  		 :py:class:`Sdr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdr_mgr.SdrConfig.Sdr>`
    
    

    """

    _prefix = 'calvados_sdr'
    _revision = '2018-05-15'

    def __init__(self):
        super(SdrConfig, self).__init__()
        self._top_entity = None

        self.yang_name = "sdr-config"
        self.yang_parent_name = "Cisco-IOS-XR-sysadmin-sdr-mgr"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("sdr", ("sdr", SdrConfig.Sdr))])
        self._leafs = OrderedDict()

        self.sdr = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-sdr-mgr:sdr-config"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(SdrConfig, [], name, value)


    class Sdr(Entity):
        """
        Add/Edit a Secure Domain Router by name
        
        .. attribute:: name  (key)
        
        	Name of the Secure Domain Router , 30 max characters
        	**type**\: str
        
        	**pattern:** [a\-zA\-Z0\-9\_\-]{1,30}
        
        .. attribute:: initial_image
        
        	List of the initial image and packages for the Secure Domain Router
        	**type**\: str
        
        .. attribute:: lead_down_delta
        
        	Amount of time between lead down to declare SDR down
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: pairing_mode
        
        	Setting for pairing mode
        	**type**\:  :py:class:`PairingMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdr_mgr.SdrConfig.Sdr.PairingMode>`
        
        .. attribute:: issu
        
        	ISSU flag. Once disabled, ISSU won't be performed for this SDR
        	**type**\:  :py:class:`Issu <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdr_mgr.SdrConfig.Sdr.Issu>`
        
        .. attribute:: resources
        
        	Edit resources for a Secure Domain Router
        	**type**\:  :py:class:`Resources <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdr_mgr.SdrConfig.Sdr.Resources>`
        
        .. attribute:: location
        
        	Enter list of nodes' location to add to this LR
        	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdr_mgr.SdrConfig.Sdr.Location>`
        
        .. attribute:: action
        
        	
        	**type**\:  :py:class:`Action <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdr_mgr.SdrConfig.Sdr.Action>`
        
        .. attribute:: detail
        
        	
        	**type**\:  :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdr_mgr.SdrConfig.Sdr.Detail>`
        
        .. attribute:: reboot_history
        
        	
        	**type**\:  :py:class:`RebootHistory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdr_mgr.SdrConfig.Sdr.RebootHistory>`
        
        .. attribute:: nodes
        
        	
        	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdr_mgr.SdrConfig.Sdr.Nodes>`
        
        .. attribute:: pairing2
        
        	
        	**type**\:  :py:class:`Pairing2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdr_mgr.SdrConfig.Sdr.Pairing2>`
        
        .. attribute:: pairing
        
        	Add/Edit a RP Pairing by name
        	**type**\: list of  		 :py:class:`Pairing <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdr_mgr.SdrConfig.Sdr.Pairing>`
        
        

        """

        _prefix = 'calvados_sdr'
        _revision = '2018-05-15'

        def __init__(self):
            super(SdrConfig.Sdr, self).__init__()

            self.yang_name = "sdr"
            self.yang_parent_name = "sdr-config"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['name']
            self._child_classes = OrderedDict([("resources", ("resources", SdrConfig.Sdr.Resources)), ("location", ("location", SdrConfig.Sdr.Location)), ("Action", ("action", SdrConfig.Sdr.Action)), ("detail", ("detail", SdrConfig.Sdr.Detail)), ("reboot-history", ("reboot_history", SdrConfig.Sdr.RebootHistory)), ("nodes", ("nodes", SdrConfig.Sdr.Nodes)), ("pairing2", ("pairing2", SdrConfig.Sdr.Pairing2)), ("pairing", ("pairing", SdrConfig.Sdr.Pairing))])
            self._leafs = OrderedDict([
                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                ('initial_image', (YLeaf(YType.str, 'initial-image'), ['str'])),
                ('lead_down_delta', (YLeaf(YType.uint32, 'lead_down_delta'), ['int'])),
                ('pairing_mode', (YLeaf(YType.enumeration, 'pairing-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdr_mgr', 'SdrConfig', 'Sdr.PairingMode')])),
                ('issu', (YLeaf(YType.enumeration, 'issu'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdr_mgr', 'SdrConfig', 'Sdr.Issu')])),
            ])
            self.name = None
            self.initial_image = None
            self.lead_down_delta = None
            self.pairing_mode = None
            self.issu = None

            self.resources = SdrConfig.Sdr.Resources()
            self.resources.parent = self
            self._children_name_map["resources"] = "resources"

            self.action = SdrConfig.Sdr.Action()
            self.action.parent = self
            self._children_name_map["action"] = "Action"

            self.detail = SdrConfig.Sdr.Detail()
            self.detail.parent = self
            self._children_name_map["detail"] = "detail"

            self.reboot_history = SdrConfig.Sdr.RebootHistory()
            self.reboot_history.parent = self
            self._children_name_map["reboot_history"] = "reboot-history"

            self.nodes = SdrConfig.Sdr.Nodes()
            self.nodes.parent = self
            self._children_name_map["nodes"] = "nodes"

            self.pairing2 = SdrConfig.Sdr.Pairing2()
            self.pairing2.parent = self
            self._children_name_map["pairing2"] = "pairing2"

            self.location = YList(self)
            self.pairing = YList(self)
            self._segment_path = lambda: "sdr" + "[name='" + str(self.name) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-sdr-mgr:sdr-config/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(SdrConfig.Sdr, ['name', 'initial_image', 'lead_down_delta', 'pairing_mode', 'issu'], name, value)

        class Issu(Enum):
            """
            Issu (Enum Class)

            ISSU flag. Once disabled, ISSU won't be performed for this SDR.

            .. data:: disable = 0

            """

            disable = Enum.YLeaf(0, "disable")


        class PairingMode(Enum):
            """
            PairingMode (Enum Class)

            Setting for pairing mode

            .. data:: intra_rack = 0

            .. data:: inter_rack = 1

            """

            intra_rack = Enum.YLeaf(0, "intra-rack")

            inter_rack = Enum.YLeaf(1, "inter-rack")



        class Resources(Entity):
            """
            Edit resources for a Secure Domain Router
            
            .. attribute:: fgid
            
            	Fgids for a Secure Domain Router
            	**type**\: int
            
            	**range:** 25000..524288
            
            .. attribute:: mgmt_ext_vlan
            
            	Management External VLAN for Secure Domain Router
            	**type**\: int
            
            	**range:** 2..4094
            
            .. attribute:: card_type
            
            	
            	**type**\: list of  		 :py:class:`CardType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdr_mgr.SdrConfig.Sdr.Resources.CardType>`
            
            .. attribute:: disk_space_size
            
            	Edit disk space size for a Secure Domain Router, unit in [MB]
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'calvados_sdr'
            _revision = '2018-05-15'

            def __init__(self):
                super(SdrConfig.Sdr.Resources, self).__init__()

                self.yang_name = "resources"
                self.yang_parent_name = "sdr"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("card-type", ("card_type", SdrConfig.Sdr.Resources.CardType))])
                self._leafs = OrderedDict([
                    ('fgid', (YLeaf(YType.uint32, 'fgid'), ['int'])),
                    ('mgmt_ext_vlan', (YLeaf(YType.uint32, 'mgmt_ext_vlan'), ['int'])),
                    ('disk_space_size', (YLeaf(YType.uint32, 'disk-space-size'), ['int'])),
                ])
                self.fgid = None
                self.mgmt_ext_vlan = None
                self.disk_space_size = None

                self.card_type = YList(self)
                self._segment_path = lambda: "resources"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(SdrConfig.Sdr.Resources, ['fgid', 'mgmt_ext_vlan', 'disk_space_size'], name, value)


            class CardType(Entity):
                """
                
                
                .. attribute:: type  (key)
                
                	Card Type
                	**type**\:  :py:class:`CardType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdr_mgr.CardType>`
                
                .. attribute:: vm_memory
                
                	VM Memory Size in units of [GB]
                	**type**\: int
                
                	**range:** 1..128
                
                .. attribute:: vm_cpu
                
                	VM Number of CPUs
                	**type**\: int
                
                	**range:** 1..128
                
                

                """

                _prefix = 'calvados_sdr'
                _revision = '2018-05-15'

                def __init__(self):
                    super(SdrConfig.Sdr.Resources.CardType, self).__init__()

                    self.yang_name = "card-type"
                    self.yang_parent_name = "resources"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['type']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdr_mgr', 'CardType', '')])),
                        ('vm_memory', (YLeaf(YType.uint32, 'vm-memory'), ['int'])),
                        ('vm_cpu', (YLeaf(YType.uint32, 'vm-cpu'), ['int'])),
                    ])
                    self.type = None
                    self.vm_memory = None
                    self.vm_cpu = None
                    self._segment_path = lambda: "card-type" + "[type='" + str(self.type) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(SdrConfig.Sdr.Resources.CardType, ['type', 'vm_memory', 'vm_cpu'], name, value)


        class Location(Entity):
            """
            Enter list of nodes' location to add to this LR
            
            .. attribute:: node_location  (key)
            
            	Enter location or all
            	**type**\: str
            
            	**pattern:** ((0?[0\-9]\|1[1\-5]\|[bB]\\d)/(([rR][pP]\|[lL][cC]\|[cC][bB])?\\d{1,2}))(/[cC][pP][uU]0)?\|all
            
            

            """

            _prefix = 'calvados_sdr'
            _revision = '2018-05-15'

            def __init__(self):
                super(SdrConfig.Sdr.Location, self).__init__()

                self.yang_name = "location"
                self.yang_parent_name = "sdr"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = ['node_location']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('node_location', (YLeaf(YType.str, 'node-location'), ['str'])),
                ])
                self.node_location = None
                self._segment_path = lambda: "location" + "[node-location='" + str(self.node_location) + "']"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(SdrConfig.Sdr.Location, ['node_location'], name, value)


        class Action(Entity):
            """
            
            
            .. attribute:: location
            
            	
            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdr_mgr.SdrConfig.Sdr.Action.Location>`
            
            

            """

            _prefix = 'calvados_sdr'
            _revision = '2018-05-15'

            def __init__(self):
                super(SdrConfig.Sdr.Action, self).__init__()

                self.yang_name = "Action"
                self.yang_parent_name = "sdr"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("location", ("location", SdrConfig.Sdr.Action.Location))])
                self._leafs = OrderedDict()

                self.location = YList(self)
                self._segment_path = lambda: "Action"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(SdrConfig.Sdr.Action, [], name, value)


            class Location(Entity):
                """
                
                
                .. attribute:: node_location  (key)
                
                	Enter location or all
                	**type**\: str
                
                	**pattern:** ((0?[0\-9]\|1[1\-5]\|[bB]\\d)/((([rR]([sS]){0,1}[pP])\|[cC][bB])?\\d{1,2})/[V][M](0?[0\-9]\|1[1\-5]))?\|all
                
                

                """

                _prefix = 'calvados_sdr'
                _revision = '2018-05-15'

                def __init__(self):
                    super(SdrConfig.Sdr.Action.Location, self).__init__()

                    self.yang_name = "location"
                    self.yang_parent_name = "Action"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['node_location']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('node_location', (YLeaf(YType.str, 'node-location'), ['str'])),
                    ])
                    self.node_location = None
                    self._segment_path = lambda: "location" + "[node-location='" + str(self.node_location) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(SdrConfig.Sdr.Action.Location, ['node_location'], name, value)


        class Detail(Entity):
            """
            
            
            .. attribute:: location
            
            	
            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdr_mgr.SdrConfig.Sdr.Detail.Location>`
            
            

            """

            _prefix = 'calvados_sdr'
            _revision = '2018-05-15'

            def __init__(self):
                super(SdrConfig.Sdr.Detail, self).__init__()

                self.yang_name = "detail"
                self.yang_parent_name = "sdr"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("location", ("location", SdrConfig.Sdr.Detail.Location))])
                self._leafs = OrderedDict()

                self.location = YList(self)
                self._segment_path = lambda: "detail"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(SdrConfig.Sdr.Detail, [], name, value)


            class Location(Entity):
                """
                
                
                .. attribute:: node_location  (key)
                
                	
                	**type**\: str
                
                	**pattern:** ((0?[0\-9]\|1[1\-5]\|[bB]\\d)/((([rR]([sS]){0,1}[pP])\|[cC][bB])?\\d{1,2})/[V][M](0?[0\-9]\|1[1\-5]))?
                
                .. attribute:: sdr_id
                
                	
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: ip_addr
                
                	IP address of VM
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: mac_address
                
                	MAC address of VM
                	**type**\: str
                
                .. attribute:: boot_part
                
                	
                	**type**\: str
                
                .. attribute:: data_part
                
                	
                	**type**\: str
                
                .. attribute:: big_disk
                
                	
                	**type**\: str
                
                .. attribute:: vm_id
                
                	
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: vmcpu
                
                	
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: vmmemory
                
                	
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: card_type
                
                	
                	**type**\: str
                
                .. attribute:: card_serial
                
                	
                	**type**\: str
                
                .. attribute:: rack_type
                
                	
                	**type**\: str
                
                .. attribute:: chassis_serial
                
                	
                	**type**\: str
                
                .. attribute:: hw_version
                
                	
                	**type**\: str
                
                .. attribute:: mgmt_ext_vlan
                
                	
                	**type**\: str
                
                .. attribute:: state
                
                	State of VM
                	**type**\: str
                
                .. attribute:: start_time
                
                	
                	**type**\: str
                
                .. attribute:: reboot_count
                
                	Number of times rebooted since first boot
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: rh_count
                
                	Number of times rebooted since lasr card reload
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: reboot_hist1
                
                	
                	**type**\: list of  		 :py:class:`RebootHist1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdr_mgr.SdrConfig.Sdr.Detail.Location.RebootHist1>`
                
                

                """

                _prefix = 'calvados_sdr'
                _revision = '2018-05-15'

                def __init__(self):
                    super(SdrConfig.Sdr.Detail.Location, self).__init__()

                    self.yang_name = "location"
                    self.yang_parent_name = "detail"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['node_location']
                    self._child_classes = OrderedDict([("reboot_hist1", ("reboot_hist1", SdrConfig.Sdr.Detail.Location.RebootHist1))])
                    self._leafs = OrderedDict([
                        ('node_location', (YLeaf(YType.str, 'node-location'), ['str'])),
                        ('sdr_id', (YLeaf(YType.uint32, 'sdr-id'), ['int'])),
                        ('ip_addr', (YLeaf(YType.str, 'ip-addr'), ['str','str'])),
                        ('mac_address', (YLeaf(YType.str, 'mac-address'), ['str'])),
                        ('boot_part', (YLeaf(YType.str, 'boot_part'), ['str'])),
                        ('data_part', (YLeaf(YType.str, 'data_part'), ['str'])),
                        ('big_disk', (YLeaf(YType.str, 'big_disk'), ['str'])),
                        ('vm_id', (YLeaf(YType.uint32, 'vm_id'), ['int'])),
                        ('vmcpu', (YLeaf(YType.uint32, 'vmcpu'), ['int'])),
                        ('vmmemory', (YLeaf(YType.uint32, 'vmmemory'), ['int'])),
                        ('card_type', (YLeaf(YType.str, 'card-type'), ['str'])),
                        ('card_serial', (YLeaf(YType.str, 'card_serial'), ['str'])),
                        ('rack_type', (YLeaf(YType.str, 'rack-type'), ['str'])),
                        ('chassis_serial', (YLeaf(YType.str, 'chassis_serial'), ['str'])),
                        ('hw_version', (YLeaf(YType.str, 'hw_version'), ['str'])),
                        ('mgmt_ext_vlan', (YLeaf(YType.str, 'mgmt_ext_vlan'), ['str'])),
                        ('state', (YLeaf(YType.str, 'state'), ['str'])),
                        ('start_time', (YLeaf(YType.str, 'start-time'), ['str'])),
                        ('reboot_count', (YLeaf(YType.uint32, 'reboot_count'), ['int'])),
                        ('rh_count', (YLeaf(YType.uint32, 'rh_count'), ['int'])),
                    ])
                    self.node_location = None
                    self.sdr_id = None
                    self.ip_addr = None
                    self.mac_address = None
                    self.boot_part = None
                    self.data_part = None
                    self.big_disk = None
                    self.vm_id = None
                    self.vmcpu = None
                    self.vmmemory = None
                    self.card_type = None
                    self.card_serial = None
                    self.rack_type = None
                    self.chassis_serial = None
                    self.hw_version = None
                    self.mgmt_ext_vlan = None
                    self.state = None
                    self.start_time = None
                    self.reboot_count = None
                    self.rh_count = None

                    self.reboot_hist1 = YList(self)
                    self._segment_path = lambda: "location" + "[node-location='" + str(self.node_location) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(SdrConfig.Sdr.Detail.Location, ['node_location', 'sdr_id', 'ip_addr', 'mac_address', 'boot_part', 'data_part', 'big_disk', 'vm_id', 'vmcpu', 'vmmemory', 'card_type', 'card_serial', 'rack_type', 'chassis_serial', 'hw_version', 'mgmt_ext_vlan', 'state', 'start_time', 'reboot_count', 'rh_count'], name, value)


                class RebootHist1(Entity):
                    """
                    
                    
                    .. attribute:: count  (key)
                    
                    	
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: time
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: reason
                    
                    	Reason for reload
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'calvados_sdr'
                    _revision = '2018-05-15'

                    def __init__(self):
                        super(SdrConfig.Sdr.Detail.Location.RebootHist1, self).__init__()

                        self.yang_name = "reboot_hist1"
                        self.yang_parent_name = "location"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['count']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                            ('time', (YLeaf(YType.str, 'Time'), ['str'])),
                            ('reason', (YLeaf(YType.str, 'Reason'), ['str'])),
                        ])
                        self.count = None
                        self.time = None
                        self.reason = None
                        self._segment_path = lambda: "reboot_hist1" + "[count='" + str(self.count) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(SdrConfig.Sdr.Detail.Location.RebootHist1, ['count', 'time', 'reason'], name, value)


        class RebootHistory(Entity):
            """
            
            
            .. attribute:: reverse
            
            	
            	**type**\:  :py:class:`Reverse <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdr_mgr.SdrConfig.Sdr.RebootHistory.Reverse>`
            
            .. attribute:: default_disp
            
            	
            	**type**\:  :py:class:`DefaultDisp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdr_mgr.SdrConfig.Sdr.RebootHistory.DefaultDisp>`
            
            

            """

            _prefix = 'calvados_sdr'
            _revision = '2018-05-15'

            def __init__(self):
                super(SdrConfig.Sdr.RebootHistory, self).__init__()

                self.yang_name = "reboot-history"
                self.yang_parent_name = "sdr"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("reverse", ("reverse", SdrConfig.Sdr.RebootHistory.Reverse)), ("default-disp", ("default_disp", SdrConfig.Sdr.RebootHistory.DefaultDisp))])
                self._leafs = OrderedDict()

                self.reverse = SdrConfig.Sdr.RebootHistory.Reverse()
                self.reverse.parent = self
                self._children_name_map["reverse"] = "reverse"

                self.default_disp = SdrConfig.Sdr.RebootHistory.DefaultDisp()
                self.default_disp.parent = self
                self._children_name_map["default_disp"] = "default-disp"
                self._segment_path = lambda: "reboot-history"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(SdrConfig.Sdr.RebootHistory, [], name, value)


            class Reverse(Entity):
                """
                
                
                .. attribute:: location
                
                	
                	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdr_mgr.SdrConfig.Sdr.RebootHistory.Reverse.Location>`
                
                

                """

                _prefix = 'calvados_sdr'
                _revision = '2018-05-15'

                def __init__(self):
                    super(SdrConfig.Sdr.RebootHistory.Reverse, self).__init__()

                    self.yang_name = "reverse"
                    self.yang_parent_name = "reboot-history"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("location", ("location", SdrConfig.Sdr.RebootHistory.Reverse.Location))])
                    self._leafs = OrderedDict()

                    self.location = YList(self)
                    self._segment_path = lambda: "reverse"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(SdrConfig.Sdr.RebootHistory.Reverse, [], name, value)


                class Location(Entity):
                    """
                    
                    
                    .. attribute:: node_location  (key)
                    
                    	
                    	**type**\: str
                    
                    	**pattern:** ((0?[0\-9]\|1[1\-5]\|[bB]\\d)/((([rR]([sS]){0,1}[pP])\|[cC][bB])?\\d{1,2})/[V][M](0?[0\-9]\|1[1\-5]))?
                    
                    .. attribute:: reboot_count
                    
                    	Number of times rebooted since first boot
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rh_count
                    
                    	Number of times rebooted since last card reload
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: reboot_hist2
                    
                    	
                    	**type**\: list of  		 :py:class:`RebootHist2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdr_mgr.SdrConfig.Sdr.RebootHistory.Reverse.Location.RebootHist2>`
                    
                    

                    """

                    _prefix = 'calvados_sdr'
                    _revision = '2018-05-15'

                    def __init__(self):
                        super(SdrConfig.Sdr.RebootHistory.Reverse.Location, self).__init__()

                        self.yang_name = "location"
                        self.yang_parent_name = "reverse"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['node_location']
                        self._child_classes = OrderedDict([("reboot_hist2", ("reboot_hist2", SdrConfig.Sdr.RebootHistory.Reverse.Location.RebootHist2))])
                        self._leafs = OrderedDict([
                            ('node_location', (YLeaf(YType.str, 'node-location'), ['str'])),
                            ('reboot_count', (YLeaf(YType.uint32, 'reboot_count'), ['int'])),
                            ('rh_count', (YLeaf(YType.uint32, 'rh_count'), ['int'])),
                        ])
                        self.node_location = None
                        self.reboot_count = None
                        self.rh_count = None

                        self.reboot_hist2 = YList(self)
                        self._segment_path = lambda: "location" + "[node-location='" + str(self.node_location) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(SdrConfig.Sdr.RebootHistory.Reverse.Location, ['node_location', 'reboot_count', 'rh_count'], name, value)


                    class RebootHist2(Entity):
                        """
                        
                        
                        .. attribute:: count  (key)
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: time
                        
                        	
                        	**type**\: str
                        
                        .. attribute:: reason
                        
                        	Reason for reload
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'calvados_sdr'
                        _revision = '2018-05-15'

                        def __init__(self):
                            super(SdrConfig.Sdr.RebootHistory.Reverse.Location.RebootHist2, self).__init__()

                            self.yang_name = "reboot_hist2"
                            self.yang_parent_name = "location"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['count']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                                ('time', (YLeaf(YType.str, 'Time'), ['str'])),
                                ('reason', (YLeaf(YType.str, 'Reason'), ['str'])),
                            ])
                            self.count = None
                            self.time = None
                            self.reason = None
                            self._segment_path = lambda: "reboot_hist2" + "[count='" + str(self.count) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(SdrConfig.Sdr.RebootHistory.Reverse.Location.RebootHist2, ['count', 'time', 'reason'], name, value)


            class DefaultDisp(Entity):
                """
                
                
                .. attribute:: location
                
                	
                	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdr_mgr.SdrConfig.Sdr.RebootHistory.DefaultDisp.Location>`
                
                

                """

                _prefix = 'calvados_sdr'
                _revision = '2018-05-15'

                def __init__(self):
                    super(SdrConfig.Sdr.RebootHistory.DefaultDisp, self).__init__()

                    self.yang_name = "default-disp"
                    self.yang_parent_name = "reboot-history"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("location", ("location", SdrConfig.Sdr.RebootHistory.DefaultDisp.Location))])
                    self._leafs = OrderedDict()

                    self.location = YList(self)
                    self._segment_path = lambda: "default-disp"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(SdrConfig.Sdr.RebootHistory.DefaultDisp, [], name, value)


                class Location(Entity):
                    """
                    
                    
                    .. attribute:: node_location  (key)
                    
                    	
                    	**type**\: str
                    
                    	**pattern:** ((0?[0\-9]\|1[1\-5]\|[bB]\\d)/((([rR]([sS]){0,1}[pP])\|[cC][bB])?\\d{1,2})/[V][M](0?[0\-9]\|1[1\-5]))?
                    
                    .. attribute:: reboot_count
                    
                    	Number of times rebooted since first boot
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rh_count
                    
                    	Number of times rebooted since last card reload
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: reboot_hist2
                    
                    	
                    	**type**\: list of  		 :py:class:`RebootHist2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdr_mgr.SdrConfig.Sdr.RebootHistory.DefaultDisp.Location.RebootHist2>`
                    
                    

                    """

                    _prefix = 'calvados_sdr'
                    _revision = '2018-05-15'

                    def __init__(self):
                        super(SdrConfig.Sdr.RebootHistory.DefaultDisp.Location, self).__init__()

                        self.yang_name = "location"
                        self.yang_parent_name = "default-disp"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['node_location']
                        self._child_classes = OrderedDict([("reboot_hist2", ("reboot_hist2", SdrConfig.Sdr.RebootHistory.DefaultDisp.Location.RebootHist2))])
                        self._leafs = OrderedDict([
                            ('node_location', (YLeaf(YType.str, 'node-location'), ['str'])),
                            ('reboot_count', (YLeaf(YType.uint32, 'reboot_count'), ['int'])),
                            ('rh_count', (YLeaf(YType.uint32, 'rh_count'), ['int'])),
                        ])
                        self.node_location = None
                        self.reboot_count = None
                        self.rh_count = None

                        self.reboot_hist2 = YList(self)
                        self._segment_path = lambda: "location" + "[node-location='" + str(self.node_location) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(SdrConfig.Sdr.RebootHistory.DefaultDisp.Location, ['node_location', 'reboot_count', 'rh_count'], name, value)


                    class RebootHist2(Entity):
                        """
                        
                        
                        .. attribute:: count  (key)
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: time
                        
                        	
                        	**type**\: str
                        
                        .. attribute:: reason
                        
                        	Reason for reload
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'calvados_sdr'
                        _revision = '2018-05-15'

                        def __init__(self):
                            super(SdrConfig.Sdr.RebootHistory.DefaultDisp.Location.RebootHist2, self).__init__()

                            self.yang_name = "reboot_hist2"
                            self.yang_parent_name = "location"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['count']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                                ('time', (YLeaf(YType.str, 'Time'), ['str'])),
                                ('reason', (YLeaf(YType.str, 'Reason'), ['str'])),
                            ])
                            self.count = None
                            self.time = None
                            self.reason = None
                            self._segment_path = lambda: "reboot_hist2" + "[count='" + str(self.count) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(SdrConfig.Sdr.RebootHistory.DefaultDisp.Location.RebootHist2, ['count', 'time', 'reason'], name, value)


        class Nodes(Entity):
            """
            
            
            .. attribute:: location
            
            	
            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdr_mgr.SdrConfig.Sdr.Nodes.Location>`
            
            

            """

            _prefix = 'calvados_sdr'
            _revision = '2018-05-15'

            def __init__(self):
                super(SdrConfig.Sdr.Nodes, self).__init__()

                self.yang_name = "nodes"
                self.yang_parent_name = "sdr"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("location", ("location", SdrConfig.Sdr.Nodes.Location))])
                self._leafs = OrderedDict()

                self.location = YList(self)
                self._segment_path = lambda: "nodes"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(SdrConfig.Sdr.Nodes, [], name, value)


            class Location(Entity):
                """
                
                
                .. attribute:: node_location  (key)
                
                	
                	**type**\: str
                
                	**pattern:** ((0?[0\-9]\|1[1\-5]\|[bB]\\d)/((([rR]([sS]){0,1}[pP])\|[cC][bB])?\\d{1,2})/[V][M](0?[0\-9]\|1[1\-5]))?
                
                .. attribute:: sdr_id
                
                	
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: ip_addr
                
                	IP address of VM
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: mac_address
                
                	MAC address of VM
                	**type**\: str
                
                .. attribute:: state
                
                	State of VM
                	**type**\: str
                
                .. attribute:: start_time
                
                	
                	**type**\: str
                
                .. attribute:: reload_reason
                
                	Reason for last reload
                	**type**\: str
                
                .. attribute:: reboot_count
                
                	Number of times rebooted since first boot
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: rh_count
                
                	Number of times rebooted since first boot
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'calvados_sdr'
                _revision = '2018-05-15'

                def __init__(self):
                    super(SdrConfig.Sdr.Nodes.Location, self).__init__()

                    self.yang_name = "location"
                    self.yang_parent_name = "nodes"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['node_location']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('node_location', (YLeaf(YType.str, 'node-location'), ['str'])),
                        ('sdr_id', (YLeaf(YType.uint32, 'sdr-id'), ['int'])),
                        ('ip_addr', (YLeaf(YType.str, 'ip-addr'), ['str','str'])),
                        ('mac_address', (YLeaf(YType.str, 'mac-address'), ['str'])),
                        ('state', (YLeaf(YType.str, 'state'), ['str'])),
                        ('start_time', (YLeaf(YType.str, 'start-time'), ['str'])),
                        ('reload_reason', (YLeaf(YType.str, 'reload_reason'), ['str'])),
                        ('reboot_count', (YLeaf(YType.uint32, 'reboot_count'), ['int'])),
                        ('rh_count', (YLeaf(YType.uint32, 'rh_count'), ['int'])),
                    ])
                    self.node_location = None
                    self.sdr_id = None
                    self.ip_addr = None
                    self.mac_address = None
                    self.state = None
                    self.start_time = None
                    self.reload_reason = None
                    self.reboot_count = None
                    self.rh_count = None
                    self._segment_path = lambda: "location" + "[node-location='" + str(self.node_location) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(SdrConfig.Sdr.Nodes.Location, ['node_location', 'sdr_id', 'ip_addr', 'mac_address', 'state', 'start_time', 'reload_reason', 'reboot_count', 'rh_count'], name, value)


        class Pairing2(Entity):
            """
            
            
            .. attribute:: pairing_mode
            
            	Mode of Pairing
            	**type**\: str
            
            .. attribute:: sdrlead
            
            	
            	**type**\:  :py:class:`Sdrlead <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdr_mgr.SdrConfig.Sdr.Pairing2.Sdrlead>`
            
            .. attribute:: pairing
            
            	
            	**type**\: list of  		 :py:class:`Pairing <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdr_mgr.SdrConfig.Sdr.Pairing2.Pairing>`
            
            

            """

            _prefix = 'calvados_sdr'
            _revision = '2018-05-15'

            def __init__(self):
                super(SdrConfig.Sdr.Pairing2, self).__init__()

                self.yang_name = "pairing2"
                self.yang_parent_name = "sdr"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("sdrlead", ("sdrlead", SdrConfig.Sdr.Pairing2.Sdrlead)), ("pairing", ("pairing", SdrConfig.Sdr.Pairing2.Pairing))])
                self._leafs = OrderedDict([
                    ('pairing_mode', (YLeaf(YType.str, 'pairing-mode'), ['str'])),
                ])
                self.pairing_mode = None

                self.sdrlead = SdrConfig.Sdr.Pairing2.Sdrlead()
                self.sdrlead.parent = self
                self._children_name_map["sdrlead"] = "sdrlead"

                self.pairing = YList(self)
                self._segment_path = lambda: "pairing2"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(SdrConfig.Sdr.Pairing2, ['pairing_mode'], name, value)


            class Sdrlead(Entity):
                """
                
                
                .. attribute:: rp1
                
                	
                	**type**\: str
                
                .. attribute:: rp2
                
                	
                	**type**\: str
                
                

                """

                _prefix = 'calvados_sdr'
                _revision = '2018-05-15'

                def __init__(self):
                    super(SdrConfig.Sdr.Pairing2.Sdrlead, self).__init__()

                    self.yang_name = "sdrlead"
                    self.yang_parent_name = "pairing2"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('rp1', (YLeaf(YType.str, 'rp1'), ['str'])),
                        ('rp2', (YLeaf(YType.str, 'rp2'), ['str'])),
                    ])
                    self.rp1 = None
                    self.rp2 = None
                    self._segment_path = lambda: "sdrlead"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(SdrConfig.Sdr.Pairing2.Sdrlead, ['rp1', 'rp2'], name, value)


            class Pairing(Entity):
                """
                
                
                .. attribute:: name  (key)
                
                	
                	**type**\: str
                
                .. attribute:: rp1
                
                	
                	**type**\: str
                
                .. attribute:: rp2
                
                	
                	**type**\: str
                
                

                """

                _prefix = 'calvados_sdr'
                _revision = '2018-05-15'

                def __init__(self):
                    super(SdrConfig.Sdr.Pairing2.Pairing, self).__init__()

                    self.yang_name = "pairing"
                    self.yang_parent_name = "pairing2"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['name']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                        ('rp1', (YLeaf(YType.str, 'rp1'), ['str'])),
                        ('rp2', (YLeaf(YType.str, 'rp2'), ['str'])),
                    ])
                    self.name = None
                    self.rp1 = None
                    self.rp2 = None
                    self._segment_path = lambda: "pairing" + "[name='" + str(self.name) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(SdrConfig.Sdr.Pairing2.Pairing, ['name', 'rp1', 'rp2'], name, value)


        class Pairing(Entity):
            """
            Add/Edit a RP Pairing by name
            
            .. attribute:: name  (key)
            
            	
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9\_\-]{1,64}
            
            .. attribute:: rp1
            
            	Enter RP Node location
            	**type**\: str
            
            	**pattern:** ((0?[0\-9]\|1[1\-5]\|[bB]\\d)/(([rR][pP]\|[cC][bB])\\d{1,2}))(/[cC][pP][uU]0)?
            
            	**mandatory**\: True
            
            .. attribute:: rp2
            
            	Enter RP Node location
            	**type**\: str
            
            	**pattern:** ((0?[0\-9]\|1[1\-5]\|[bB]\\d)/(([rR][pP]\|[cC][bB])\\d{1,2}))(/[cC][pP][uU]0)?
            
            	**mandatory**\: True
            
            

            """

            _prefix = 'calvados_sdr'
            _revision = '2018-05-15'

            def __init__(self):
                super(SdrConfig.Sdr.Pairing, self).__init__()

                self.yang_name = "pairing"
                self.yang_parent_name = "sdr"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = ['name']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                    ('rp1', (YLeaf(YType.str, 'rp1'), ['str'])),
                    ('rp2', (YLeaf(YType.str, 'rp2'), ['str'])),
                ])
                self.name = None
                self.rp1 = None
                self.rp2 = None
                self._segment_path = lambda: "pairing" + "[name='" + str(self.name) + "']"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(SdrConfig.Sdr.Pairing, ['name', 'rp1', 'rp2'], name, value)

    def clone_ptr(self):
        self._top_entity = SdrConfig()
        return self._top_entity

class SdrManager(Entity):
    """
    
    
    .. attribute:: sdr_mgr
    
    	
    	**type**\:  :py:class:`SdrMgr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdr_mgr.SdrManager.SdrMgr>`
    
    

    """

    _prefix = 'calvados_sdr'
    _revision = '2018-05-15'

    def __init__(self):
        super(SdrManager, self).__init__()
        self._top_entity = None

        self.yang_name = "sdr-manager"
        self.yang_parent_name = "Cisco-IOS-XR-sysadmin-sdr-mgr"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("sdr_mgr", ("sdr_mgr", SdrManager.SdrMgr))])
        self._leafs = OrderedDict()

        self.sdr_mgr = SdrManager.SdrMgr()
        self.sdr_mgr.parent = self
        self._children_name_map["sdr_mgr"] = "sdr_mgr"
        self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-sdr-mgr:sdr-manager"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(SdrManager, [], name, value)


    class SdrMgr(Entity):
        """
        
        
        .. attribute:: trace
        
        	show traceable processes
        	**type**\: list of  		 :py:class:`Trace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdr_mgr.SdrManager.SdrMgr.Trace>`
        
        

        """

        _prefix = 'calvados_sdr'
        _revision = '2018-05-15'

        def __init__(self):
            super(SdrManager.SdrMgr, self).__init__()

            self.yang_name = "sdr_mgr"
            self.yang_parent_name = "sdr-manager"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("trace", ("trace", SdrManager.SdrMgr.Trace))])
            self._leafs = OrderedDict()

            self.trace = YList(self)
            self._segment_path = lambda: "sdr_mgr"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-sdr-mgr:sdr-manager/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(SdrManager.SdrMgr, [], name, value)


        class Trace(Entity):
            """
            show traceable processes
            
            .. attribute:: buffer  (key)
            
            	
            	**type**\: str
            
            .. attribute:: location
            
            	
            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdr_mgr.SdrManager.SdrMgr.Trace.Location>`
            
            

            """

            _prefix = 'calvados_sdr'
            _revision = '2018-05-15'

            def __init__(self):
                super(SdrManager.SdrMgr.Trace, self).__init__()

                self.yang_name = "trace"
                self.yang_parent_name = "sdr_mgr"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['buffer']
                self._child_classes = OrderedDict([("location", ("location", SdrManager.SdrMgr.Trace.Location))])
                self._leafs = OrderedDict([
                    ('buffer', (YLeaf(YType.str, 'buffer'), ['str'])),
                ])
                self.buffer = None

                self.location = YList(self)
                self._segment_path = lambda: "trace" + "[buffer='" + str(self.buffer) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-sdr-mgr:sdr-manager/sdr_mgr/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(SdrManager.SdrMgr.Trace, [u'buffer'], name, value)


            class Location(Entity):
                """
                
                
                .. attribute:: location_name  (key)
                
                	
                	**type**\: str
                
                .. attribute:: all_options
                
                	
                	**type**\: list of  		 :py:class:`AllOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdr_mgr.SdrManager.SdrMgr.Trace.Location.AllOptions>`
                
                

                """

                _prefix = 'calvados_sdr'
                _revision = '2018-05-15'

                def __init__(self):
                    super(SdrManager.SdrMgr.Trace.Location, self).__init__()

                    self.yang_name = "location"
                    self.yang_parent_name = "trace"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['location_name']
                    self._child_classes = OrderedDict([("all-options", ("all_options", SdrManager.SdrMgr.Trace.Location.AllOptions))])
                    self._leafs = OrderedDict([
                        ('location_name', (YLeaf(YType.str, 'location_name'), ['str'])),
                    ])
                    self.location_name = None

                    self.all_options = YList(self)
                    self._segment_path = lambda: "location" + "[location_name='" + str(self.location_name) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(SdrManager.SdrMgr.Trace.Location, [u'location_name'], name, value)


                class AllOptions(Entity):
                    """
                    
                    
                    .. attribute:: option  (key)
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: trace_blocks
                    
                    	
                    	**type**\: list of  		 :py:class:`TraceBlocks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdr_mgr.SdrManager.SdrMgr.Trace.Location.AllOptions.TraceBlocks>`
                    
                    

                    """

                    _prefix = 'calvados_sdr'
                    _revision = '2018-05-15'

                    def __init__(self):
                        super(SdrManager.SdrMgr.Trace.Location.AllOptions, self).__init__()

                        self.yang_name = "all-options"
                        self.yang_parent_name = "location"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['option']
                        self._child_classes = OrderedDict([("trace-blocks", ("trace_blocks", SdrManager.SdrMgr.Trace.Location.AllOptions.TraceBlocks))])
                        self._leafs = OrderedDict([
                            ('option', (YLeaf(YType.str, 'option'), ['str'])),
                        ])
                        self.option = None

                        self.trace_blocks = YList(self)
                        self._segment_path = lambda: "all-options" + "[option='" + str(self.option) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(SdrManager.SdrMgr.Trace.Location.AllOptions, [u'option'], name, value)


                    class TraceBlocks(Entity):
                        """
                        
                        
                        .. attribute:: data
                        
                        	Trace output block
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'calvados_sdr'
                        _revision = '2018-05-15'

                        def __init__(self):
                            super(SdrManager.SdrMgr.Trace.Location.AllOptions.TraceBlocks, self).__init__()

                            self.yang_name = "trace-blocks"
                            self.yang_parent_name = "all-options"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('data', (YLeaf(YType.str, 'data'), ['str'])),
                            ])
                            self.data = None
                            self._segment_path = lambda: "trace-blocks"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(SdrManager.SdrMgr.Trace.Location.AllOptions.TraceBlocks, [u'data'], name, value)

    def clone_ptr(self):
        self._top_entity = SdrManager()
        return self._top_entity

class SdrOperation(Entity):
    """
    
    
    .. attribute:: sdr
    
    	SDR
    	**type**\: list of  		 :py:class:`Sdr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdr_mgr.SdrOperation.Sdr>`
    
    

    """

    _prefix = 'calvados_sdr'
    _revision = '2018-05-15'

    def __init__(self):
        super(SdrOperation, self).__init__()
        self._top_entity = None

        self.yang_name = "sdr-operation"
        self.yang_parent_name = "Cisco-IOS-XR-sysadmin-sdr-mgr"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("sdr", ("sdr", SdrOperation.Sdr))])
        self._leafs = OrderedDict()

        self.sdr = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-sdr-mgr:sdr-operation"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(SdrOperation, [], name, value)


    class Sdr(Entity):
        """
        SDR
        
        .. attribute:: name  (key)
        
        	Name of the Secure Domain Router, 30 max characters
        	**type**\: str
        
        	**pattern:** [a\-zA\-Z0\-9\_\-]{1,30}
        
        .. attribute:: nodes
        
        	
        	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdr_mgr.SdrOperation.Sdr.Nodes>`
        
        

        """

        _prefix = 'calvados_sdr'
        _revision = '2018-05-15'

        def __init__(self):
            super(SdrOperation.Sdr, self).__init__()

            self.yang_name = "sdr"
            self.yang_parent_name = "sdr-operation"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['name']
            self._child_classes = OrderedDict([("nodes", ("nodes", SdrOperation.Sdr.Nodes))])
            self._leafs = OrderedDict([
                ('name', (YLeaf(YType.str, 'name'), ['str'])),
            ])
            self.name = None

            self.nodes = SdrOperation.Sdr.Nodes()
            self.nodes.parent = self
            self._children_name_map["nodes"] = "nodes"
            self._segment_path = lambda: "sdr" + "[name='" + str(self.name) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-sdr-mgr:sdr-operation/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(SdrOperation.Sdr, ['name'], name, value)


        class Nodes(Entity):
            """
            
            
            .. attribute:: location
            
            	
            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdr_mgr.SdrOperation.Sdr.Nodes.Location>`
            
            

            """

            _prefix = 'calvados_sdr'
            _revision = '2018-05-15'

            def __init__(self):
                super(SdrOperation.Sdr.Nodes, self).__init__()

                self.yang_name = "nodes"
                self.yang_parent_name = "sdr"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("location", ("location", SdrOperation.Sdr.Nodes.Location))])
                self._leafs = OrderedDict()

                self.location = YList(self)
                self._segment_path = lambda: "nodes"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(SdrOperation.Sdr.Nodes, [], name, value)


            class Location(Entity):
                """
                
                
                .. attribute:: node_location  (key)
                
                	
                	**type**\: str
                
                .. attribute:: node_type  (key)
                
                	
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: progress
                
                	Progress of Operation
                	**type**\: str
                
                .. attribute:: state
                
                	State of Operation
                	**type**\: str
                
                

                """

                _prefix = 'calvados_sdr'
                _revision = '2018-05-15'

                def __init__(self):
                    super(SdrOperation.Sdr.Nodes.Location, self).__init__()

                    self.yang_name = "location"
                    self.yang_parent_name = "nodes"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['node_location','node_type']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('node_location', (YLeaf(YType.str, 'node-location'), ['str'])),
                        ('node_type', (YLeaf(YType.uint32, 'node-type'), ['int'])),
                        ('progress', (YLeaf(YType.str, 'progress'), ['str'])),
                        ('state', (YLeaf(YType.str, 'state'), ['str'])),
                    ])
                    self.node_location = None
                    self.node_type = None
                    self.progress = None
                    self.state = None
                    self._segment_path = lambda: "location" + "[node-location='" + str(self.node_location) + "']" + "[node-type='" + str(self.node_type) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(SdrOperation.Sdr.Nodes.Location, ['node_location', 'node_type', 'progress', 'state'], name, value)

    def clone_ptr(self):
        self._top_entity = SdrOperation()
        return self._top_entity

class PrivateSdr(Entity):
    """
    
    
    .. attribute:: sdr_name
    
    	
    	**type**\: list of  		 :py:class:`SdrName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdr_mgr.PrivateSdr.SdrName>`
    
    

    """

    _prefix = 'calvados_sdr'
    _revision = '2018-05-15'

    def __init__(self):
        super(PrivateSdr, self).__init__()
        self._top_entity = None

        self.yang_name = "private-sdr"
        self.yang_parent_name = "Cisco-IOS-XR-sysadmin-sdr-mgr"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("sdr-name", ("sdr_name", PrivateSdr.SdrName))])
        self._leafs = OrderedDict()

        self.sdr_name = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-sdr-mgr:private-sdr"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(PrivateSdr, [], name, value)


    class SdrName(Entity):
        """
        
        
        .. attribute:: name  (key)
        
        	
        	**type**\: str
        
        .. attribute:: id
        
        	
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: lead_rack0
        
        	
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: lead_rack1
        
        	
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: pairing
        
        	
        	**type**\: list of  		 :py:class:`Pairing <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdr_mgr.PrivateSdr.SdrName.Pairing>`
        
        

        """

        _prefix = 'calvados_sdr'
        _revision = '2018-05-15'

        def __init__(self):
            super(PrivateSdr.SdrName, self).__init__()

            self.yang_name = "sdr-name"
            self.yang_parent_name = "private-sdr"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['name']
            self._child_classes = OrderedDict([("pairing", ("pairing", PrivateSdr.SdrName.Pairing))])
            self._leafs = OrderedDict([
                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                ('id', (YLeaf(YType.uint32, 'id'), ['int'])),
                ('lead_rack0', (YLeaf(YType.uint32, 'lead_rack0'), ['int'])),
                ('lead_rack1', (YLeaf(YType.uint32, 'lead_rack1'), ['int'])),
            ])
            self.name = None
            self.id = None
            self.lead_rack0 = None
            self.lead_rack1 = None

            self.pairing = YList(self)
            self._segment_path = lambda: "sdr-name" + "[name='" + str(self.name) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-sdr-mgr:private-sdr/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(PrivateSdr.SdrName, ['name', 'id', 'lead_rack0', 'lead_rack1'], name, value)


        class Pairing(Entity):
            """
            
            
            .. attribute:: num  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: second_exist
            
            	
            	**type**\: bool
            
            .. attribute:: rp1_rack
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rp1_slot
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rp2_rack
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rp2_slot
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'calvados_sdr'
            _revision = '2018-05-15'

            def __init__(self):
                super(PrivateSdr.SdrName.Pairing, self).__init__()

                self.yang_name = "pairing"
                self.yang_parent_name = "sdr-name"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = ['num']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('num', (YLeaf(YType.uint32, 'num'), ['int'])),
                    ('second_exist', (YLeaf(YType.boolean, 'second_exist'), ['bool'])),
                    ('rp1_rack', (YLeaf(YType.uint32, 'rp1_rack'), ['int'])),
                    ('rp1_slot', (YLeaf(YType.uint32, 'rp1_slot'), ['int'])),
                    ('rp2_rack', (YLeaf(YType.uint32, 'rp2_rack'), ['int'])),
                    ('rp2_slot', (YLeaf(YType.uint32, 'rp2_slot'), ['int'])),
                ])
                self.num = None
                self.second_exist = None
                self.rp1_rack = None
                self.rp1_slot = None
                self.rp2_rack = None
                self.rp2_slot = None
                self._segment_path = lambda: "pairing" + "[num='" + str(self.num) + "']"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PrivateSdr.SdrName.Pairing, ['num', 'second_exist', 'rp1_rack', 'rp1_slot', 'rp2_rack', 'rp2_slot'], name, value)

    def clone_ptr(self):
        self._top_entity = PrivateSdr()
        return self._top_entity

