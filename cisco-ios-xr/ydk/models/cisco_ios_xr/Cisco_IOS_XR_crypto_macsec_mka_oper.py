""" Cisco_IOS_XR_crypto_macsec_mka_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR crypto\-macsec\-mka package operational data.

This module contains definitions
for the following management objects\:
  macsec\: Macsec operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Macsec(Entity):
    """
    Macsec operational data
    
    .. attribute:: mka
    
    	MKA Data
    	**type**\:   :py:class:`Mka <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_oper.Macsec.Mka>`
    
    

    """

    _prefix = 'crypto-macsec-mka-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Macsec, self).__init__()
        self._top_entity = None

        self.yang_name = "macsec"
        self.yang_parent_name = "Cisco-IOS-XR-crypto-macsec-mka-oper"

        self.mka = Macsec.Mka()
        self.mka.parent = self
        self._children_name_map["mka"] = "mka"
        self._children_yang_names.add("mka")


    class Mka(Entity):
        """
        MKA Data
        
        .. attribute:: interfaces
        
        	MKA Data
        	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_oper.Macsec.Mka.Interfaces>`
        
        

        """

        _prefix = 'crypto-macsec-mka-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Macsec.Mka, self).__init__()

            self.yang_name = "mka"
            self.yang_parent_name = "macsec"

            self.interfaces = Macsec.Mka.Interfaces()
            self.interfaces.parent = self
            self._children_name_map["interfaces"] = "interfaces"
            self._children_yang_names.add("interfaces")


        class Interfaces(Entity):
            """
            MKA Data
            
            .. attribute:: interface
            
            	MKA Data for the Interface
            	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_oper.Macsec.Mka.Interfaces.Interface>`
            
            

            """

            _prefix = 'crypto-macsec-mka-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Macsec.Mka.Interfaces, self).__init__()

                self.yang_name = "interfaces"
                self.yang_parent_name = "mka"

                self.interface = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in () and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Macsec.Mka.Interfaces, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Macsec.Mka.Interfaces, self).__setattr__(name, value)


            class Interface(Entity):
                """
                MKA Data for the Interface
                
                .. attribute:: name  <key>
                
                	Interface Name
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: session
                
                	MKA Session Data
                	**type**\:   :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_oper.Macsec.Mka.Interfaces.Interface.Session>`
                
                

                """

                _prefix = 'crypto-macsec-mka-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Macsec.Mka.Interfaces.Interface, self).__init__()

                    self.yang_name = "interface"
                    self.yang_parent_name = "interfaces"

                    self.name = YLeaf(YType.str, "name")

                    self.session = Macsec.Mka.Interfaces.Interface.Session()
                    self.session.parent = self
                    self._children_name_map["session"] = "session"
                    self._children_yang_names.add("session")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Macsec.Mka.Interfaces.Interface, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Macsec.Mka.Interfaces.Interface, self).__setattr__(name, value)


                class Session(Entity):
                    """
                    MKA Session Data
                    
                    .. attribute:: ca
                    
                    	CA List for a Session
                    	**type**\: list of    :py:class:`Ca <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_oper.Macsec.Mka.Interfaces.Interface.Session.Ca>`
                    
                    .. attribute:: session_summary
                    
                    	Session summary
                    	**type**\:   :py:class:`SessionSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_oper.Macsec.Mka.Interfaces.Interface.Session.SessionSummary>`
                    
                    .. attribute:: vp
                    
                    	Virtual Pointer Info
                    	**type**\:   :py:class:`Vp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_oper.Macsec.Mka.Interfaces.Interface.Session.Vp>`
                    
                    

                    """

                    _prefix = 'crypto-macsec-mka-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Macsec.Mka.Interfaces.Interface.Session, self).__init__()

                        self.yang_name = "session"
                        self.yang_parent_name = "interface"

                        self.session_summary = Macsec.Mka.Interfaces.Interface.Session.SessionSummary()
                        self.session_summary.parent = self
                        self._children_name_map["session_summary"] = "session-summary"
                        self._children_yang_names.add("session-summary")

                        self.vp = Macsec.Mka.Interfaces.Interface.Session.Vp()
                        self.vp.parent = self
                        self._children_name_map["vp"] = "vp"
                        self._children_yang_names.add("vp")

                        self.ca = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in () and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Macsec.Mka.Interfaces.Interface.Session, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Macsec.Mka.Interfaces.Interface.Session, self).__setattr__(name, value)


                    class SessionSummary(Entity):
                        """
                        Session summary
                        
                        .. attribute:: algo_agility
                        
                        	Alogorithm Agility
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: capability
                        
                        	MACSec Capability
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: cipher_str
                        
                        	Cipher String
                        	**type**\:  str
                        
                        .. attribute:: confidentiality_offset
                        
                        	Confidentiality Offset
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: delay_protection
                        
                        	Delay Protect
                        	**type**\:  bool
                        
                        .. attribute:: include_icv_indicator
                        
                        	IncludeICVIndicator
                        	**type**\:  bool
                        
                        .. attribute:: inherited_policy
                        
                        	Is Inherited Policy
                        	**type**\:  bool
                        
                        .. attribute:: inner_tag
                        
                        	VLAN Inner TAG
                        	**type**\:   :py:class:`InnerTag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_oper.Macsec.Mka.Interfaces.Interface.Session.SessionSummary.InnerTag>`
                        
                        .. attribute:: interface_name
                        
                        	macsec configured interface
                        	**type**\:  str
                        
                        .. attribute:: mac_sec_desired
                        
                        	MACSec Desired
                        	**type**\:  bool
                        
                        .. attribute:: my_mac
                        
                        	My MAC
                        	**type**\:  str
                        
                        .. attribute:: outer_tag
                        
                        	VLAN Outer TAG
                        	**type**\:   :py:class:`OuterTag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_oper.Macsec.Mka.Interfaces.Interface.Session.SessionSummary.OuterTag>`
                        
                        .. attribute:: policy
                        
                        	Policy Name
                        	**type**\:  str
                        
                        .. attribute:: priority
                        
                        	Key Server Priority
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: replay_protect
                        
                        	Replay Protect
                        	**type**\:  bool
                        
                        .. attribute:: window_size
                        
                        	Replay Window Size
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'crypto-macsec-mka-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Macsec.Mka.Interfaces.Interface.Session.SessionSummary, self).__init__()

                            self.yang_name = "session-summary"
                            self.yang_parent_name = "session"

                            self.algo_agility = YLeaf(YType.uint32, "algo-agility")

                            self.capability = YLeaf(YType.uint32, "capability")

                            self.cipher_str = YLeaf(YType.str, "cipher-str")

                            self.confidentiality_offset = YLeaf(YType.uint32, "confidentiality-offset")

                            self.delay_protection = YLeaf(YType.boolean, "delay-protection")

                            self.include_icv_indicator = YLeaf(YType.boolean, "include-icv-indicator")

                            self.inherited_policy = YLeaf(YType.boolean, "inherited-policy")

                            self.interface_name = YLeaf(YType.str, "interface-name")

                            self.mac_sec_desired = YLeaf(YType.boolean, "mac-sec-desired")

                            self.my_mac = YLeaf(YType.str, "my-mac")

                            self.policy = YLeaf(YType.str, "policy")

                            self.priority = YLeaf(YType.uint32, "priority")

                            self.replay_protect = YLeaf(YType.boolean, "replay-protect")

                            self.window_size = YLeaf(YType.uint32, "window-size")

                            self.inner_tag = Macsec.Mka.Interfaces.Interface.Session.SessionSummary.InnerTag()
                            self.inner_tag.parent = self
                            self._children_name_map["inner_tag"] = "inner-tag"
                            self._children_yang_names.add("inner-tag")

                            self.outer_tag = Macsec.Mka.Interfaces.Interface.Session.SessionSummary.OuterTag()
                            self.outer_tag.parent = self
                            self._children_name_map["outer_tag"] = "outer-tag"
                            self._children_yang_names.add("outer-tag")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("algo_agility",
                                            "capability",
                                            "cipher_str",
                                            "confidentiality_offset",
                                            "delay_protection",
                                            "include_icv_indicator",
                                            "inherited_policy",
                                            "interface_name",
                                            "mac_sec_desired",
                                            "my_mac",
                                            "policy",
                                            "priority",
                                            "replay_protect",
                                            "window_size") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Macsec.Mka.Interfaces.Interface.Session.SessionSummary, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Macsec.Mka.Interfaces.Interface.Session.SessionSummary, self).__setattr__(name, value)


                        class OuterTag(Entity):
                            """
                            VLAN Outer TAG
                            
                            .. attribute:: cfi
                            
                            	cfi
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: etype
                            
                            	etype
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: priority
                            
                            	priority
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: vlan_id
                            
                            	vlan id
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'crypto-macsec-mka-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Macsec.Mka.Interfaces.Interface.Session.SessionSummary.OuterTag, self).__init__()

                                self.yang_name = "outer-tag"
                                self.yang_parent_name = "session-summary"

                                self.cfi = YLeaf(YType.uint8, "cfi")

                                self.etype = YLeaf(YType.uint16, "etype")

                                self.priority = YLeaf(YType.uint8, "priority")

                                self.vlan_id = YLeaf(YType.uint16, "vlan-id")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("cfi",
                                                "etype",
                                                "priority",
                                                "vlan_id") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Macsec.Mka.Interfaces.Interface.Session.SessionSummary.OuterTag, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Macsec.Mka.Interfaces.Interface.Session.SessionSummary.OuterTag, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.cfi.is_set or
                                    self.etype.is_set or
                                    self.priority.is_set or
                                    self.vlan_id.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.cfi.yfilter != YFilter.not_set or
                                    self.etype.yfilter != YFilter.not_set or
                                    self.priority.yfilter != YFilter.not_set or
                                    self.vlan_id.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "outer-tag" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.cfi.is_set or self.cfi.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.cfi.get_name_leafdata())
                                if (self.etype.is_set or self.etype.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.etype.get_name_leafdata())
                                if (self.priority.is_set or self.priority.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.priority.get_name_leafdata())
                                if (self.vlan_id.is_set or self.vlan_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.vlan_id.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "cfi" or name == "etype" or name == "priority" or name == "vlan-id"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "cfi"):
                                    self.cfi = value
                                    self.cfi.value_namespace = name_space
                                    self.cfi.value_namespace_prefix = name_space_prefix
                                if(value_path == "etype"):
                                    self.etype = value
                                    self.etype.value_namespace = name_space
                                    self.etype.value_namespace_prefix = name_space_prefix
                                if(value_path == "priority"):
                                    self.priority = value
                                    self.priority.value_namespace = name_space
                                    self.priority.value_namespace_prefix = name_space_prefix
                                if(value_path == "vlan-id"):
                                    self.vlan_id = value
                                    self.vlan_id.value_namespace = name_space
                                    self.vlan_id.value_namespace_prefix = name_space_prefix


                        class InnerTag(Entity):
                            """
                            VLAN Inner TAG
                            
                            .. attribute:: cfi
                            
                            	cfi
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: etype
                            
                            	etype
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: priority
                            
                            	priority
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: vlan_id
                            
                            	vlan id
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'crypto-macsec-mka-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Macsec.Mka.Interfaces.Interface.Session.SessionSummary.InnerTag, self).__init__()

                                self.yang_name = "inner-tag"
                                self.yang_parent_name = "session-summary"

                                self.cfi = YLeaf(YType.uint8, "cfi")

                                self.etype = YLeaf(YType.uint16, "etype")

                                self.priority = YLeaf(YType.uint8, "priority")

                                self.vlan_id = YLeaf(YType.uint16, "vlan-id")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("cfi",
                                                "etype",
                                                "priority",
                                                "vlan_id") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Macsec.Mka.Interfaces.Interface.Session.SessionSummary.InnerTag, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Macsec.Mka.Interfaces.Interface.Session.SessionSummary.InnerTag, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.cfi.is_set or
                                    self.etype.is_set or
                                    self.priority.is_set or
                                    self.vlan_id.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.cfi.yfilter != YFilter.not_set or
                                    self.etype.yfilter != YFilter.not_set or
                                    self.priority.yfilter != YFilter.not_set or
                                    self.vlan_id.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "inner-tag" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.cfi.is_set or self.cfi.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.cfi.get_name_leafdata())
                                if (self.etype.is_set or self.etype.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.etype.get_name_leafdata())
                                if (self.priority.is_set or self.priority.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.priority.get_name_leafdata())
                                if (self.vlan_id.is_set or self.vlan_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.vlan_id.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "cfi" or name == "etype" or name == "priority" or name == "vlan-id"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "cfi"):
                                    self.cfi = value
                                    self.cfi.value_namespace = name_space
                                    self.cfi.value_namespace_prefix = name_space_prefix
                                if(value_path == "etype"):
                                    self.etype = value
                                    self.etype.value_namespace = name_space
                                    self.etype.value_namespace_prefix = name_space_prefix
                                if(value_path == "priority"):
                                    self.priority = value
                                    self.priority.value_namespace = name_space
                                    self.priority.value_namespace_prefix = name_space_prefix
                                if(value_path == "vlan-id"):
                                    self.vlan_id = value
                                    self.vlan_id.value_namespace = name_space
                                    self.vlan_id.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.algo_agility.is_set or
                                self.capability.is_set or
                                self.cipher_str.is_set or
                                self.confidentiality_offset.is_set or
                                self.delay_protection.is_set or
                                self.include_icv_indicator.is_set or
                                self.inherited_policy.is_set or
                                self.interface_name.is_set or
                                self.mac_sec_desired.is_set or
                                self.my_mac.is_set or
                                self.policy.is_set or
                                self.priority.is_set or
                                self.replay_protect.is_set or
                                self.window_size.is_set or
                                (self.inner_tag is not None and self.inner_tag.has_data()) or
                                (self.outer_tag is not None and self.outer_tag.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.algo_agility.yfilter != YFilter.not_set or
                                self.capability.yfilter != YFilter.not_set or
                                self.cipher_str.yfilter != YFilter.not_set or
                                self.confidentiality_offset.yfilter != YFilter.not_set or
                                self.delay_protection.yfilter != YFilter.not_set or
                                self.include_icv_indicator.yfilter != YFilter.not_set or
                                self.inherited_policy.yfilter != YFilter.not_set or
                                self.interface_name.yfilter != YFilter.not_set or
                                self.mac_sec_desired.yfilter != YFilter.not_set or
                                self.my_mac.yfilter != YFilter.not_set or
                                self.policy.yfilter != YFilter.not_set or
                                self.priority.yfilter != YFilter.not_set or
                                self.replay_protect.yfilter != YFilter.not_set or
                                self.window_size.yfilter != YFilter.not_set or
                                (self.inner_tag is not None and self.inner_tag.has_operation()) or
                                (self.outer_tag is not None and self.outer_tag.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "session-summary" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.algo_agility.is_set or self.algo_agility.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.algo_agility.get_name_leafdata())
                            if (self.capability.is_set or self.capability.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.capability.get_name_leafdata())
                            if (self.cipher_str.is_set or self.cipher_str.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.cipher_str.get_name_leafdata())
                            if (self.confidentiality_offset.is_set or self.confidentiality_offset.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.confidentiality_offset.get_name_leafdata())
                            if (self.delay_protection.is_set or self.delay_protection.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.delay_protection.get_name_leafdata())
                            if (self.include_icv_indicator.is_set or self.include_icv_indicator.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.include_icv_indicator.get_name_leafdata())
                            if (self.inherited_policy.is_set or self.inherited_policy.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.inherited_policy.get_name_leafdata())
                            if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.interface_name.get_name_leafdata())
                            if (self.mac_sec_desired.is_set or self.mac_sec_desired.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.mac_sec_desired.get_name_leafdata())
                            if (self.my_mac.is_set or self.my_mac.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.my_mac.get_name_leafdata())
                            if (self.policy.is_set or self.policy.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.policy.get_name_leafdata())
                            if (self.priority.is_set or self.priority.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.priority.get_name_leafdata())
                            if (self.replay_protect.is_set or self.replay_protect.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.replay_protect.get_name_leafdata())
                            if (self.window_size.is_set or self.window_size.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.window_size.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "inner-tag"):
                                if (self.inner_tag is None):
                                    self.inner_tag = Macsec.Mka.Interfaces.Interface.Session.SessionSummary.InnerTag()
                                    self.inner_tag.parent = self
                                    self._children_name_map["inner_tag"] = "inner-tag"
                                return self.inner_tag

                            if (child_yang_name == "outer-tag"):
                                if (self.outer_tag is None):
                                    self.outer_tag = Macsec.Mka.Interfaces.Interface.Session.SessionSummary.OuterTag()
                                    self.outer_tag.parent = self
                                    self._children_name_map["outer_tag"] = "outer-tag"
                                return self.outer_tag

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "inner-tag" or name == "outer-tag" or name == "algo-agility" or name == "capability" or name == "cipher-str" or name == "confidentiality-offset" or name == "delay-protection" or name == "include-icv-indicator" or name == "inherited-policy" or name == "interface-name" or name == "mac-sec-desired" or name == "my-mac" or name == "policy" or name == "priority" or name == "replay-protect" or name == "window-size"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "algo-agility"):
                                self.algo_agility = value
                                self.algo_agility.value_namespace = name_space
                                self.algo_agility.value_namespace_prefix = name_space_prefix
                            if(value_path == "capability"):
                                self.capability = value
                                self.capability.value_namespace = name_space
                                self.capability.value_namespace_prefix = name_space_prefix
                            if(value_path == "cipher-str"):
                                self.cipher_str = value
                                self.cipher_str.value_namespace = name_space
                                self.cipher_str.value_namespace_prefix = name_space_prefix
                            if(value_path == "confidentiality-offset"):
                                self.confidentiality_offset = value
                                self.confidentiality_offset.value_namespace = name_space
                                self.confidentiality_offset.value_namespace_prefix = name_space_prefix
                            if(value_path == "delay-protection"):
                                self.delay_protection = value
                                self.delay_protection.value_namespace = name_space
                                self.delay_protection.value_namespace_prefix = name_space_prefix
                            if(value_path == "include-icv-indicator"):
                                self.include_icv_indicator = value
                                self.include_icv_indicator.value_namespace = name_space
                                self.include_icv_indicator.value_namespace_prefix = name_space_prefix
                            if(value_path == "inherited-policy"):
                                self.inherited_policy = value
                                self.inherited_policy.value_namespace = name_space
                                self.inherited_policy.value_namespace_prefix = name_space_prefix
                            if(value_path == "interface-name"):
                                self.interface_name = value
                                self.interface_name.value_namespace = name_space
                                self.interface_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "mac-sec-desired"):
                                self.mac_sec_desired = value
                                self.mac_sec_desired.value_namespace = name_space
                                self.mac_sec_desired.value_namespace_prefix = name_space_prefix
                            if(value_path == "my-mac"):
                                self.my_mac = value
                                self.my_mac.value_namespace = name_space
                                self.my_mac.value_namespace_prefix = name_space_prefix
                            if(value_path == "policy"):
                                self.policy = value
                                self.policy.value_namespace = name_space
                                self.policy.value_namespace_prefix = name_space_prefix
                            if(value_path == "priority"):
                                self.priority = value
                                self.priority.value_namespace = name_space
                                self.priority.value_namespace_prefix = name_space_prefix
                            if(value_path == "replay-protect"):
                                self.replay_protect = value
                                self.replay_protect.value_namespace = name_space
                                self.replay_protect.value_namespace_prefix = name_space_prefix
                            if(value_path == "window-size"):
                                self.window_size = value
                                self.window_size.value_namespace = name_space
                                self.window_size.value_namespace_prefix = name_space_prefix


                    class Vp(Entity):
                        """
                        Virtual Pointer Info
                        
                        .. attribute:: cipher_suite
                        
                        	SAK Cipher Suite
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: latest_an
                        
                        	Latest SAK AN
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: latest_ki
                        
                        	Latest SAK KI
                        	**type**\:  str
                        
                        .. attribute:: latest_kn
                        
                        	Latest SAK KN
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: latest_rx
                        
                        	Latest Rx status
                        	**type**\:  bool
                        
                        .. attribute:: latest_tx
                        
                        	Latest Tx status
                        	**type**\:  bool
                        
                        .. attribute:: my_sci
                        
                        	Local SCI(MAC)
                        	**type**\:  str
                        
                        .. attribute:: old_an
                        
                        	Old SAK AN
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: old_ki
                        
                        	Old SAK KI
                        	**type**\:  str
                        
                        .. attribute:: old_kn
                        
                        	Old SAK KN
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: old_rx
                        
                        	Old Rx status
                        	**type**\:  bool
                        
                        .. attribute:: old_tx
                        
                        	Old Tx status
                        	**type**\:  bool
                        
                        .. attribute:: retire_time
                        
                        	SAK Retire time
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ssci
                        
                        	SSCI of the Local TxSC
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: time_to_sak_rekey
                        
                        	Next SAK Rekey time in Sec
                        	**type**\:  str
                        
                        .. attribute:: virtual_port_id
                        
                        	Virtual Port ID
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: wait_time
                        
                        	SAK Transmit Wait Time
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'crypto-macsec-mka-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Macsec.Mka.Interfaces.Interface.Session.Vp, self).__init__()

                            self.yang_name = "vp"
                            self.yang_parent_name = "session"

                            self.cipher_suite = YLeaf(YType.uint32, "cipher-suite")

                            self.latest_an = YLeaf(YType.uint32, "latest-an")

                            self.latest_ki = YLeaf(YType.str, "latest-ki")

                            self.latest_kn = YLeaf(YType.uint32, "latest-kn")

                            self.latest_rx = YLeaf(YType.boolean, "latest-rx")

                            self.latest_tx = YLeaf(YType.boolean, "latest-tx")

                            self.my_sci = YLeaf(YType.str, "my-sci")

                            self.old_an = YLeaf(YType.uint32, "old-an")

                            self.old_ki = YLeaf(YType.str, "old-ki")

                            self.old_kn = YLeaf(YType.uint32, "old-kn")

                            self.old_rx = YLeaf(YType.boolean, "old-rx")

                            self.old_tx = YLeaf(YType.boolean, "old-tx")

                            self.retire_time = YLeaf(YType.uint32, "retire-time")

                            self.ssci = YLeaf(YType.uint32, "ssci")

                            self.time_to_sak_rekey = YLeaf(YType.str, "time-to-sak-rekey")

                            self.virtual_port_id = YLeaf(YType.uint32, "virtual-port-id")

                            self.wait_time = YLeaf(YType.uint32, "wait-time")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("cipher_suite",
                                            "latest_an",
                                            "latest_ki",
                                            "latest_kn",
                                            "latest_rx",
                                            "latest_tx",
                                            "my_sci",
                                            "old_an",
                                            "old_ki",
                                            "old_kn",
                                            "old_rx",
                                            "old_tx",
                                            "retire_time",
                                            "ssci",
                                            "time_to_sak_rekey",
                                            "virtual_port_id",
                                            "wait_time") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Macsec.Mka.Interfaces.Interface.Session.Vp, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Macsec.Mka.Interfaces.Interface.Session.Vp, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.cipher_suite.is_set or
                                self.latest_an.is_set or
                                self.latest_ki.is_set or
                                self.latest_kn.is_set or
                                self.latest_rx.is_set or
                                self.latest_tx.is_set or
                                self.my_sci.is_set or
                                self.old_an.is_set or
                                self.old_ki.is_set or
                                self.old_kn.is_set or
                                self.old_rx.is_set or
                                self.old_tx.is_set or
                                self.retire_time.is_set or
                                self.ssci.is_set or
                                self.time_to_sak_rekey.is_set or
                                self.virtual_port_id.is_set or
                                self.wait_time.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.cipher_suite.yfilter != YFilter.not_set or
                                self.latest_an.yfilter != YFilter.not_set or
                                self.latest_ki.yfilter != YFilter.not_set or
                                self.latest_kn.yfilter != YFilter.not_set or
                                self.latest_rx.yfilter != YFilter.not_set or
                                self.latest_tx.yfilter != YFilter.not_set or
                                self.my_sci.yfilter != YFilter.not_set or
                                self.old_an.yfilter != YFilter.not_set or
                                self.old_ki.yfilter != YFilter.not_set or
                                self.old_kn.yfilter != YFilter.not_set or
                                self.old_rx.yfilter != YFilter.not_set or
                                self.old_tx.yfilter != YFilter.not_set or
                                self.retire_time.yfilter != YFilter.not_set or
                                self.ssci.yfilter != YFilter.not_set or
                                self.time_to_sak_rekey.yfilter != YFilter.not_set or
                                self.virtual_port_id.yfilter != YFilter.not_set or
                                self.wait_time.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "vp" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.cipher_suite.is_set or self.cipher_suite.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.cipher_suite.get_name_leafdata())
                            if (self.latest_an.is_set or self.latest_an.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.latest_an.get_name_leafdata())
                            if (self.latest_ki.is_set or self.latest_ki.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.latest_ki.get_name_leafdata())
                            if (self.latest_kn.is_set or self.latest_kn.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.latest_kn.get_name_leafdata())
                            if (self.latest_rx.is_set or self.latest_rx.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.latest_rx.get_name_leafdata())
                            if (self.latest_tx.is_set or self.latest_tx.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.latest_tx.get_name_leafdata())
                            if (self.my_sci.is_set or self.my_sci.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.my_sci.get_name_leafdata())
                            if (self.old_an.is_set or self.old_an.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.old_an.get_name_leafdata())
                            if (self.old_ki.is_set or self.old_ki.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.old_ki.get_name_leafdata())
                            if (self.old_kn.is_set or self.old_kn.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.old_kn.get_name_leafdata())
                            if (self.old_rx.is_set or self.old_rx.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.old_rx.get_name_leafdata())
                            if (self.old_tx.is_set or self.old_tx.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.old_tx.get_name_leafdata())
                            if (self.retire_time.is_set or self.retire_time.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.retire_time.get_name_leafdata())
                            if (self.ssci.is_set or self.ssci.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ssci.get_name_leafdata())
                            if (self.time_to_sak_rekey.is_set or self.time_to_sak_rekey.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.time_to_sak_rekey.get_name_leafdata())
                            if (self.virtual_port_id.is_set or self.virtual_port_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.virtual_port_id.get_name_leafdata())
                            if (self.wait_time.is_set or self.wait_time.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.wait_time.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "cipher-suite" or name == "latest-an" or name == "latest-ki" or name == "latest-kn" or name == "latest-rx" or name == "latest-tx" or name == "my-sci" or name == "old-an" or name == "old-ki" or name == "old-kn" or name == "old-rx" or name == "old-tx" or name == "retire-time" or name == "ssci" or name == "time-to-sak-rekey" or name == "virtual-port-id" or name == "wait-time"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "cipher-suite"):
                                self.cipher_suite = value
                                self.cipher_suite.value_namespace = name_space
                                self.cipher_suite.value_namespace_prefix = name_space_prefix
                            if(value_path == "latest-an"):
                                self.latest_an = value
                                self.latest_an.value_namespace = name_space
                                self.latest_an.value_namespace_prefix = name_space_prefix
                            if(value_path == "latest-ki"):
                                self.latest_ki = value
                                self.latest_ki.value_namespace = name_space
                                self.latest_ki.value_namespace_prefix = name_space_prefix
                            if(value_path == "latest-kn"):
                                self.latest_kn = value
                                self.latest_kn.value_namespace = name_space
                                self.latest_kn.value_namespace_prefix = name_space_prefix
                            if(value_path == "latest-rx"):
                                self.latest_rx = value
                                self.latest_rx.value_namespace = name_space
                                self.latest_rx.value_namespace_prefix = name_space_prefix
                            if(value_path == "latest-tx"):
                                self.latest_tx = value
                                self.latest_tx.value_namespace = name_space
                                self.latest_tx.value_namespace_prefix = name_space_prefix
                            if(value_path == "my-sci"):
                                self.my_sci = value
                                self.my_sci.value_namespace = name_space
                                self.my_sci.value_namespace_prefix = name_space_prefix
                            if(value_path == "old-an"):
                                self.old_an = value
                                self.old_an.value_namespace = name_space
                                self.old_an.value_namespace_prefix = name_space_prefix
                            if(value_path == "old-ki"):
                                self.old_ki = value
                                self.old_ki.value_namespace = name_space
                                self.old_ki.value_namespace_prefix = name_space_prefix
                            if(value_path == "old-kn"):
                                self.old_kn = value
                                self.old_kn.value_namespace = name_space
                                self.old_kn.value_namespace_prefix = name_space_prefix
                            if(value_path == "old-rx"):
                                self.old_rx = value
                                self.old_rx.value_namespace = name_space
                                self.old_rx.value_namespace_prefix = name_space_prefix
                            if(value_path == "old-tx"):
                                self.old_tx = value
                                self.old_tx.value_namespace = name_space
                                self.old_tx.value_namespace_prefix = name_space_prefix
                            if(value_path == "retire-time"):
                                self.retire_time = value
                                self.retire_time.value_namespace = name_space
                                self.retire_time.value_namespace_prefix = name_space_prefix
                            if(value_path == "ssci"):
                                self.ssci = value
                                self.ssci.value_namespace = name_space
                                self.ssci.value_namespace_prefix = name_space_prefix
                            if(value_path == "time-to-sak-rekey"):
                                self.time_to_sak_rekey = value
                                self.time_to_sak_rekey.value_namespace = name_space
                                self.time_to_sak_rekey.value_namespace_prefix = name_space_prefix
                            if(value_path == "virtual-port-id"):
                                self.virtual_port_id = value
                                self.virtual_port_id.value_namespace = name_space
                                self.virtual_port_id.value_namespace_prefix = name_space_prefix
                            if(value_path == "wait-time"):
                                self.wait_time = value
                                self.wait_time.value_namespace = name_space
                                self.wait_time.value_namespace_prefix = name_space_prefix


                    class Ca(Entity):
                        """
                        CA List for a Session
                        
                        .. attribute:: authentication_mode
                        
                        	CA Authentication Mode \:PRIMARY\-PSK/FALLBACK\-PSK/EAP
                        	**type**\:  str
                        
                        .. attribute:: authenticator
                        
                        	authenticator
                        	**type**\:  bool
                        
                        .. attribute:: ckn
                        
                        	CKN
                        	**type**\:  str
                        
                        .. attribute:: dormant_peer
                        
                        	Dormant Peer List
                        	**type**\: list of    :py:class:`DormantPeer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_oper.Macsec.Mka.Interfaces.Interface.Session.Ca.DormantPeer>`
                        
                        .. attribute:: first_ca
                        
                        	Is First CA
                        	**type**\:  bool
                        
                        .. attribute:: is_key_server
                        
                        	Is Key Server
                        	**type**\:  bool
                        
                        .. attribute:: key_chain
                        
                        	Key Chain name
                        	**type**\:  str
                        
                        .. attribute:: live_peer
                        
                        	Live Peer List
                        	**type**\: list of    :py:class:`LivePeer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_oper.Macsec.Mka.Interfaces.Interface.Session.Ca.LivePeer>`
                        
                        .. attribute:: my_mi
                        
                        	Member Identifier
                        	**type**\:  str
                        
                        .. attribute:: my_mn
                        
                        	Message Number
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: num_live_peers
                        
                        	Number of Live Peers
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: num_live_peers_responded
                        
                        	Number of Live Peers responded
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: peer_sci
                        
                        	Peer SCI(MAC)
                        	**type**\:  str
                        
                        .. attribute:: potential_peer
                        
                        	Potential Peer List
                        	**type**\: list of    :py:class:`PotentialPeer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_oper.Macsec.Mka.Interfaces.Interface.Session.Ca.PotentialPeer>`
                        
                        .. attribute:: status
                        
                        	Session Status [Secured/Not Secured]
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: status_description
                        
                        	Status Description
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'crypto-macsec-mka-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Macsec.Mka.Interfaces.Interface.Session.Ca, self).__init__()

                            self.yang_name = "ca"
                            self.yang_parent_name = "session"

                            self.authentication_mode = YLeaf(YType.str, "authentication-mode")

                            self.authenticator = YLeaf(YType.boolean, "authenticator")

                            self.ckn = YLeaf(YType.str, "ckn")

                            self.first_ca = YLeaf(YType.boolean, "first-ca")

                            self.is_key_server = YLeaf(YType.boolean, "is-key-server")

                            self.key_chain = YLeaf(YType.str, "key-chain")

                            self.my_mi = YLeaf(YType.str, "my-mi")

                            self.my_mn = YLeaf(YType.uint32, "my-mn")

                            self.num_live_peers = YLeaf(YType.uint32, "num-live-peers")

                            self.num_live_peers_responded = YLeaf(YType.uint32, "num-live-peers-responded")

                            self.peer_sci = YLeaf(YType.str, "peer-sci")

                            self.status = YLeaf(YType.uint32, "status")

                            self.status_description = YLeaf(YType.str, "status-description")

                            self.dormant_peer = YList(self)
                            self.live_peer = YList(self)
                            self.potential_peer = YList(self)

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("authentication_mode",
                                            "authenticator",
                                            "ckn",
                                            "first_ca",
                                            "is_key_server",
                                            "key_chain",
                                            "my_mi",
                                            "my_mn",
                                            "num_live_peers",
                                            "num_live_peers_responded",
                                            "peer_sci",
                                            "status",
                                            "status_description") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Macsec.Mka.Interfaces.Interface.Session.Ca, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Macsec.Mka.Interfaces.Interface.Session.Ca, self).__setattr__(name, value)


                        class LivePeer(Entity):
                            """
                            Live Peer List
                            
                            .. attribute:: mi
                            
                            	Member ID
                            	**type**\:  str
                            
                            .. attribute:: mn
                            
                            	Message Number
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: priority
                            
                            	KS Priority
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: sci
                            
                            	Rx SCI
                            	**type**\:  str
                            
                            .. attribute:: ssci
                            
                            	Peer SSCI
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'crypto-macsec-mka-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Macsec.Mka.Interfaces.Interface.Session.Ca.LivePeer, self).__init__()

                                self.yang_name = "live-peer"
                                self.yang_parent_name = "ca"

                                self.mi = YLeaf(YType.str, "mi")

                                self.mn = YLeaf(YType.uint32, "mn")

                                self.priority = YLeaf(YType.uint32, "priority")

                                self.sci = YLeaf(YType.str, "sci")

                                self.ssci = YLeaf(YType.uint32, "ssci")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("mi",
                                                "mn",
                                                "priority",
                                                "sci",
                                                "ssci") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Macsec.Mka.Interfaces.Interface.Session.Ca.LivePeer, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Macsec.Mka.Interfaces.Interface.Session.Ca.LivePeer, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.mi.is_set or
                                    self.mn.is_set or
                                    self.priority.is_set or
                                    self.sci.is_set or
                                    self.ssci.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.mi.yfilter != YFilter.not_set or
                                    self.mn.yfilter != YFilter.not_set or
                                    self.priority.yfilter != YFilter.not_set or
                                    self.sci.yfilter != YFilter.not_set or
                                    self.ssci.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "live-peer" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.mi.is_set or self.mi.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.mi.get_name_leafdata())
                                if (self.mn.is_set or self.mn.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.mn.get_name_leafdata())
                                if (self.priority.is_set or self.priority.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.priority.get_name_leafdata())
                                if (self.sci.is_set or self.sci.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.sci.get_name_leafdata())
                                if (self.ssci.is_set or self.ssci.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ssci.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "mi" or name == "mn" or name == "priority" or name == "sci" or name == "ssci"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "mi"):
                                    self.mi = value
                                    self.mi.value_namespace = name_space
                                    self.mi.value_namespace_prefix = name_space_prefix
                                if(value_path == "mn"):
                                    self.mn = value
                                    self.mn.value_namespace = name_space
                                    self.mn.value_namespace_prefix = name_space_prefix
                                if(value_path == "priority"):
                                    self.priority = value
                                    self.priority.value_namespace = name_space
                                    self.priority.value_namespace_prefix = name_space_prefix
                                if(value_path == "sci"):
                                    self.sci = value
                                    self.sci.value_namespace = name_space
                                    self.sci.value_namespace_prefix = name_space_prefix
                                if(value_path == "ssci"):
                                    self.ssci = value
                                    self.ssci.value_namespace = name_space
                                    self.ssci.value_namespace_prefix = name_space_prefix


                        class PotentialPeer(Entity):
                            """
                            Potential Peer List
                            
                            .. attribute:: mi
                            
                            	Member ID
                            	**type**\:  str
                            
                            .. attribute:: mn
                            
                            	Message Number
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: priority
                            
                            	KS Priority
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: sci
                            
                            	Rx SCI
                            	**type**\:  str
                            
                            .. attribute:: ssci
                            
                            	Peer SSCI
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'crypto-macsec-mka-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Macsec.Mka.Interfaces.Interface.Session.Ca.PotentialPeer, self).__init__()

                                self.yang_name = "potential-peer"
                                self.yang_parent_name = "ca"

                                self.mi = YLeaf(YType.str, "mi")

                                self.mn = YLeaf(YType.uint32, "mn")

                                self.priority = YLeaf(YType.uint32, "priority")

                                self.sci = YLeaf(YType.str, "sci")

                                self.ssci = YLeaf(YType.uint32, "ssci")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("mi",
                                                "mn",
                                                "priority",
                                                "sci",
                                                "ssci") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Macsec.Mka.Interfaces.Interface.Session.Ca.PotentialPeer, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Macsec.Mka.Interfaces.Interface.Session.Ca.PotentialPeer, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.mi.is_set or
                                    self.mn.is_set or
                                    self.priority.is_set or
                                    self.sci.is_set or
                                    self.ssci.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.mi.yfilter != YFilter.not_set or
                                    self.mn.yfilter != YFilter.not_set or
                                    self.priority.yfilter != YFilter.not_set or
                                    self.sci.yfilter != YFilter.not_set or
                                    self.ssci.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "potential-peer" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.mi.is_set or self.mi.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.mi.get_name_leafdata())
                                if (self.mn.is_set or self.mn.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.mn.get_name_leafdata())
                                if (self.priority.is_set or self.priority.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.priority.get_name_leafdata())
                                if (self.sci.is_set or self.sci.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.sci.get_name_leafdata())
                                if (self.ssci.is_set or self.ssci.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ssci.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "mi" or name == "mn" or name == "priority" or name == "sci" or name == "ssci"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "mi"):
                                    self.mi = value
                                    self.mi.value_namespace = name_space
                                    self.mi.value_namespace_prefix = name_space_prefix
                                if(value_path == "mn"):
                                    self.mn = value
                                    self.mn.value_namespace = name_space
                                    self.mn.value_namespace_prefix = name_space_prefix
                                if(value_path == "priority"):
                                    self.priority = value
                                    self.priority.value_namespace = name_space
                                    self.priority.value_namespace_prefix = name_space_prefix
                                if(value_path == "sci"):
                                    self.sci = value
                                    self.sci.value_namespace = name_space
                                    self.sci.value_namespace_prefix = name_space_prefix
                                if(value_path == "ssci"):
                                    self.ssci = value
                                    self.ssci.value_namespace = name_space
                                    self.ssci.value_namespace_prefix = name_space_prefix


                        class DormantPeer(Entity):
                            """
                            Dormant Peer List
                            
                            .. attribute:: mi
                            
                            	Member ID
                            	**type**\:  str
                            
                            .. attribute:: mn
                            
                            	Message Number
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: priority
                            
                            	KS Priority
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: sci
                            
                            	Rx SCI
                            	**type**\:  str
                            
                            .. attribute:: ssci
                            
                            	Peer SSCI
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'crypto-macsec-mka-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Macsec.Mka.Interfaces.Interface.Session.Ca.DormantPeer, self).__init__()

                                self.yang_name = "dormant-peer"
                                self.yang_parent_name = "ca"

                                self.mi = YLeaf(YType.str, "mi")

                                self.mn = YLeaf(YType.uint32, "mn")

                                self.priority = YLeaf(YType.uint32, "priority")

                                self.sci = YLeaf(YType.str, "sci")

                                self.ssci = YLeaf(YType.uint32, "ssci")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("mi",
                                                "mn",
                                                "priority",
                                                "sci",
                                                "ssci") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Macsec.Mka.Interfaces.Interface.Session.Ca.DormantPeer, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Macsec.Mka.Interfaces.Interface.Session.Ca.DormantPeer, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.mi.is_set or
                                    self.mn.is_set or
                                    self.priority.is_set or
                                    self.sci.is_set or
                                    self.ssci.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.mi.yfilter != YFilter.not_set or
                                    self.mn.yfilter != YFilter.not_set or
                                    self.priority.yfilter != YFilter.not_set or
                                    self.sci.yfilter != YFilter.not_set or
                                    self.ssci.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "dormant-peer" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.mi.is_set or self.mi.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.mi.get_name_leafdata())
                                if (self.mn.is_set or self.mn.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.mn.get_name_leafdata())
                                if (self.priority.is_set or self.priority.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.priority.get_name_leafdata())
                                if (self.sci.is_set or self.sci.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.sci.get_name_leafdata())
                                if (self.ssci.is_set or self.ssci.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ssci.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "mi" or name == "mn" or name == "priority" or name == "sci" or name == "ssci"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "mi"):
                                    self.mi = value
                                    self.mi.value_namespace = name_space
                                    self.mi.value_namespace_prefix = name_space_prefix
                                if(value_path == "mn"):
                                    self.mn = value
                                    self.mn.value_namespace = name_space
                                    self.mn.value_namespace_prefix = name_space_prefix
                                if(value_path == "priority"):
                                    self.priority = value
                                    self.priority.value_namespace = name_space
                                    self.priority.value_namespace_prefix = name_space_prefix
                                if(value_path == "sci"):
                                    self.sci = value
                                    self.sci.value_namespace = name_space
                                    self.sci.value_namespace_prefix = name_space_prefix
                                if(value_path == "ssci"):
                                    self.ssci = value
                                    self.ssci.value_namespace = name_space
                                    self.ssci.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.dormant_peer:
                                if (c.has_data()):
                                    return True
                            for c in self.live_peer:
                                if (c.has_data()):
                                    return True
                            for c in self.potential_peer:
                                if (c.has_data()):
                                    return True
                            return (
                                self.authentication_mode.is_set or
                                self.authenticator.is_set or
                                self.ckn.is_set or
                                self.first_ca.is_set or
                                self.is_key_server.is_set or
                                self.key_chain.is_set or
                                self.my_mi.is_set or
                                self.my_mn.is_set or
                                self.num_live_peers.is_set or
                                self.num_live_peers_responded.is_set or
                                self.peer_sci.is_set or
                                self.status.is_set or
                                self.status_description.is_set)

                        def has_operation(self):
                            for c in self.dormant_peer:
                                if (c.has_operation()):
                                    return True
                            for c in self.live_peer:
                                if (c.has_operation()):
                                    return True
                            for c in self.potential_peer:
                                if (c.has_operation()):
                                    return True
                            return (
                                self.yfilter != YFilter.not_set or
                                self.authentication_mode.yfilter != YFilter.not_set or
                                self.authenticator.yfilter != YFilter.not_set or
                                self.ckn.yfilter != YFilter.not_set or
                                self.first_ca.yfilter != YFilter.not_set or
                                self.is_key_server.yfilter != YFilter.not_set or
                                self.key_chain.yfilter != YFilter.not_set or
                                self.my_mi.yfilter != YFilter.not_set or
                                self.my_mn.yfilter != YFilter.not_set or
                                self.num_live_peers.yfilter != YFilter.not_set or
                                self.num_live_peers_responded.yfilter != YFilter.not_set or
                                self.peer_sci.yfilter != YFilter.not_set or
                                self.status.yfilter != YFilter.not_set or
                                self.status_description.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "ca" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.authentication_mode.is_set or self.authentication_mode.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.authentication_mode.get_name_leafdata())
                            if (self.authenticator.is_set or self.authenticator.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.authenticator.get_name_leafdata())
                            if (self.ckn.is_set or self.ckn.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ckn.get_name_leafdata())
                            if (self.first_ca.is_set or self.first_ca.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.first_ca.get_name_leafdata())
                            if (self.is_key_server.is_set or self.is_key_server.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_key_server.get_name_leafdata())
                            if (self.key_chain.is_set or self.key_chain.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.key_chain.get_name_leafdata())
                            if (self.my_mi.is_set or self.my_mi.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.my_mi.get_name_leafdata())
                            if (self.my_mn.is_set or self.my_mn.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.my_mn.get_name_leafdata())
                            if (self.num_live_peers.is_set or self.num_live_peers.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.num_live_peers.get_name_leafdata())
                            if (self.num_live_peers_responded.is_set or self.num_live_peers_responded.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.num_live_peers_responded.get_name_leafdata())
                            if (self.peer_sci.is_set or self.peer_sci.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.peer_sci.get_name_leafdata())
                            if (self.status.is_set or self.status.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.status.get_name_leafdata())
                            if (self.status_description.is_set or self.status_description.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.status_description.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "dormant-peer"):
                                for c in self.dormant_peer:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Macsec.Mka.Interfaces.Interface.Session.Ca.DormantPeer()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.dormant_peer.append(c)
                                return c

                            if (child_yang_name == "live-peer"):
                                for c in self.live_peer:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Macsec.Mka.Interfaces.Interface.Session.Ca.LivePeer()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.live_peer.append(c)
                                return c

                            if (child_yang_name == "potential-peer"):
                                for c in self.potential_peer:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Macsec.Mka.Interfaces.Interface.Session.Ca.PotentialPeer()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.potential_peer.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "dormant-peer" or name == "live-peer" or name == "potential-peer" or name == "authentication-mode" or name == "authenticator" or name == "ckn" or name == "first-ca" or name == "is-key-server" or name == "key-chain" or name == "my-mi" or name == "my-mn" or name == "num-live-peers" or name == "num-live-peers-responded" or name == "peer-sci" or name == "status" or name == "status-description"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "authentication-mode"):
                                self.authentication_mode = value
                                self.authentication_mode.value_namespace = name_space
                                self.authentication_mode.value_namespace_prefix = name_space_prefix
                            if(value_path == "authenticator"):
                                self.authenticator = value
                                self.authenticator.value_namespace = name_space
                                self.authenticator.value_namespace_prefix = name_space_prefix
                            if(value_path == "ckn"):
                                self.ckn = value
                                self.ckn.value_namespace = name_space
                                self.ckn.value_namespace_prefix = name_space_prefix
                            if(value_path == "first-ca"):
                                self.first_ca = value
                                self.first_ca.value_namespace = name_space
                                self.first_ca.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-key-server"):
                                self.is_key_server = value
                                self.is_key_server.value_namespace = name_space
                                self.is_key_server.value_namespace_prefix = name_space_prefix
                            if(value_path == "key-chain"):
                                self.key_chain = value
                                self.key_chain.value_namespace = name_space
                                self.key_chain.value_namespace_prefix = name_space_prefix
                            if(value_path == "my-mi"):
                                self.my_mi = value
                                self.my_mi.value_namespace = name_space
                                self.my_mi.value_namespace_prefix = name_space_prefix
                            if(value_path == "my-mn"):
                                self.my_mn = value
                                self.my_mn.value_namespace = name_space
                                self.my_mn.value_namespace_prefix = name_space_prefix
                            if(value_path == "num-live-peers"):
                                self.num_live_peers = value
                                self.num_live_peers.value_namespace = name_space
                                self.num_live_peers.value_namespace_prefix = name_space_prefix
                            if(value_path == "num-live-peers-responded"):
                                self.num_live_peers_responded = value
                                self.num_live_peers_responded.value_namespace = name_space
                                self.num_live_peers_responded.value_namespace_prefix = name_space_prefix
                            if(value_path == "peer-sci"):
                                self.peer_sci = value
                                self.peer_sci.value_namespace = name_space
                                self.peer_sci.value_namespace_prefix = name_space_prefix
                            if(value_path == "status"):
                                self.status = value
                                self.status.value_namespace = name_space
                                self.status.value_namespace_prefix = name_space_prefix
                            if(value_path == "status-description"):
                                self.status_description = value
                                self.status_description.value_namespace = name_space
                                self.status_description.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.ca:
                            if (c.has_data()):
                                return True
                        return (
                            (self.session_summary is not None and self.session_summary.has_data()) or
                            (self.vp is not None and self.vp.has_data()))

                    def has_operation(self):
                        for c in self.ca:
                            if (c.has_operation()):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.session_summary is not None and self.session_summary.has_operation()) or
                            (self.vp is not None and self.vp.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "session" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "ca"):
                            for c in self.ca:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Macsec.Mka.Interfaces.Interface.Session.Ca()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.ca.append(c)
                            return c

                        if (child_yang_name == "session-summary"):
                            if (self.session_summary is None):
                                self.session_summary = Macsec.Mka.Interfaces.Interface.Session.SessionSummary()
                                self.session_summary.parent = self
                                self._children_name_map["session_summary"] = "session-summary"
                            return self.session_summary

                        if (child_yang_name == "vp"):
                            if (self.vp is None):
                                self.vp = Macsec.Mka.Interfaces.Interface.Session.Vp()
                                self.vp.parent = self
                                self._children_name_map["vp"] = "vp"
                            return self.vp

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "ca" or name == "session-summary" or name == "vp"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        self.name.is_set or
                        (self.session is not None and self.session.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.name.yfilter != YFilter.not_set or
                        (self.session is not None and self.session.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "interface" + "[name='" + self.name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-crypto-macsec-mka-oper:macsec/mka/interfaces/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.name.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "session"):
                        if (self.session is None):
                            self.session = Macsec.Mka.Interfaces.Interface.Session()
                            self.session.parent = self
                            self._children_name_map["session"] = "session"
                        return self.session

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "session" or name == "name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "name"):
                        self.name = value
                        self.name.value_namespace = name_space
                        self.name.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.interface:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.interface:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "interfaces" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-crypto-macsec-mka-oper:macsec/mka/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "interface"):
                    for c in self.interface:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Macsec.Mka.Interfaces.Interface()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.interface.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "interface"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (self.interfaces is not None and self.interfaces.has_data())

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.interfaces is not None and self.interfaces.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "mka" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-crypto-macsec-mka-oper:macsec/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "interfaces"):
                if (self.interfaces is None):
                    self.interfaces = Macsec.Mka.Interfaces()
                    self.interfaces.parent = self
                    self._children_name_map["interfaces"] = "interfaces"
                return self.interfaces

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "interfaces"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.mka is not None and self.mka.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.mka is not None and self.mka.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-crypto-macsec-mka-oper:macsec" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "mka"):
            if (self.mka is None):
                self.mka = Macsec.Mka()
                self.mka.parent = self
                self._children_name_map["mka"] = "mka"
            return self.mka

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "mka"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Macsec()
        return self._top_entity

