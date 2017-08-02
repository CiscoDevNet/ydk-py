""" Cisco_IOS_XR_iedge4710_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR iedge4710 package configuration.

This module contains definitions
for the following management objects\:
  subscriber\-manager\: iEdge subscriber manager configuration
  subscriber\-featurette\: subscriber featurette
  iedge\-license\-manager\: iedge license manager
  sub\-manager\: sub manager

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg
module with configuration data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class SubscriberManager(Entity):
    """
    iEdge subscriber manager configuration
    
    .. attribute:: accounting
    
    	iEdge accounting feature
    	**type**\:   :py:class:`Accounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg.SubscriberManager.Accounting>`
    
    .. attribute:: srg
    
    	SRG specific config
    	**type**\:   :py:class:`Srg <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg.SubscriberManager.Srg>`
    
    

    """

    _prefix = 'iedge4710-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(SubscriberManager, self).__init__()
        self._top_entity = None

        self.yang_name = "subscriber-manager"
        self.yang_parent_name = "Cisco-IOS-XR-iedge4710-cfg"

        self.accounting = SubscriberManager.Accounting()
        self.accounting.parent = self
        self._children_name_map["accounting"] = "accounting"
        self._children_yang_names.add("accounting")

        self.srg = SubscriberManager.Srg()
        self.srg.parent = self
        self._children_name_map["srg"] = "srg"
        self._children_yang_names.add("srg")


    class Accounting(Entity):
        """
        iEdge accounting feature
        
        .. attribute:: interim
        
        	interim accounting related
        	**type**\:   :py:class:`Interim <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg.SubscriberManager.Accounting.Interim>`
        
        .. attribute:: send_stop
        
        	Accounting send stop feature
        	**type**\:   :py:class:`SendStop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg.SubscriberManager.Accounting.SendStop>`
        
        

        """

        _prefix = 'iedge4710-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(SubscriberManager.Accounting, self).__init__()

            self.yang_name = "accounting"
            self.yang_parent_name = "subscriber-manager"

            self.interim = SubscriberManager.Accounting.Interim()
            self.interim.parent = self
            self._children_name_map["interim"] = "interim"
            self._children_yang_names.add("interim")

            self.send_stop = SubscriberManager.Accounting.SendStop()
            self.send_stop.parent = self
            self._children_name_map["send_stop"] = "send-stop"
            self._children_yang_names.add("send-stop")


        class SendStop(Entity):
            """
            Accounting send stop feature
            
            .. attribute:: setup_failure
            
            	Set up failure feature
            	**type**\:  str
            
            

            """

            _prefix = 'iedge4710-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(SubscriberManager.Accounting.SendStop, self).__init__()

                self.yang_name = "send-stop"
                self.yang_parent_name = "accounting"

                self.setup_failure = YLeaf(YType.str, "setup-failure")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("setup_failure") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(SubscriberManager.Accounting.SendStop, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(SubscriberManager.Accounting.SendStop, self).__setattr__(name, value)

            def has_data(self):
                return self.setup_failure.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.setup_failure.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "send-stop" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-iedge4710-cfg:subscriber-manager/accounting/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.setup_failure.is_set or self.setup_failure.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.setup_failure.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "setup-failure"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "setup-failure"):
                    self.setup_failure = value
                    self.setup_failure.value_namespace = name_space
                    self.setup_failure.value_namespace_prefix = name_space_prefix


        class Interim(Entity):
            """
            interim accounting related
            
            .. attribute:: variation
            
            	variation of first session or service interim record from configured timeout
            	**type**\:   :py:class:`Variation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg.SubscriberManager.Accounting.Interim.Variation>`
            
            

            """

            _prefix = 'iedge4710-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(SubscriberManager.Accounting.Interim, self).__init__()

                self.yang_name = "interim"
                self.yang_parent_name = "accounting"

                self.variation = SubscriberManager.Accounting.Interim.Variation()
                self.variation.parent = self
                self._children_name_map["variation"] = "variation"
                self._children_yang_names.add("variation")


            class Variation(Entity):
                """
                variation of first session or service interim
                record from configured timeout
                
                .. attribute:: maximum_percentage_variation
                
                	maximum percentage variation (maximum absolute variation is 15 minutes)
                	**type**\:  int
                
                	**range:** 0..50
                
                	**units**\: percentage
                
                

                """

                _prefix = 'iedge4710-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(SubscriberManager.Accounting.Interim.Variation, self).__init__()

                    self.yang_name = "variation"
                    self.yang_parent_name = "interim"

                    self.maximum_percentage_variation = YLeaf(YType.uint32, "maximum-percentage-variation")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("maximum_percentage_variation") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(SubscriberManager.Accounting.Interim.Variation, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(SubscriberManager.Accounting.Interim.Variation, self).__setattr__(name, value)

                def has_data(self):
                    return self.maximum_percentage_variation.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.maximum_percentage_variation.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "variation" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-iedge4710-cfg:subscriber-manager/accounting/interim/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.maximum_percentage_variation.is_set or self.maximum_percentage_variation.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.maximum_percentage_variation.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "maximum-percentage-variation"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "maximum-percentage-variation"):
                        self.maximum_percentage_variation = value
                        self.maximum_percentage_variation.value_namespace = name_space
                        self.maximum_percentage_variation.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (self.variation is not None and self.variation.has_data())

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.variation is not None and self.variation.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "interim" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-iedge4710-cfg:subscriber-manager/accounting/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "variation"):
                    if (self.variation is None):
                        self.variation = SubscriberManager.Accounting.Interim.Variation()
                        self.variation.parent = self
                        self._children_name_map["variation"] = "variation"
                    return self.variation

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "variation"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                (self.interim is not None and self.interim.has_data()) or
                (self.send_stop is not None and self.send_stop.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.interim is not None and self.interim.has_operation()) or
                (self.send_stop is not None and self.send_stop.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "accounting" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-iedge4710-cfg:subscriber-manager/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "interim"):
                if (self.interim is None):
                    self.interim = SubscriberManager.Accounting.Interim()
                    self.interim.parent = self
                    self._children_name_map["interim"] = "interim"
                return self.interim

            if (child_yang_name == "send-stop"):
                if (self.send_stop is None):
                    self.send_stop = SubscriberManager.Accounting.SendStop()
                    self.send_stop.parent = self
                    self._children_name_map["send_stop"] = "send-stop"
                return self.send_stop

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "interim" or name == "send-stop"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Srg(Entity):
        """
        SRG specific config
        
        .. attribute:: sync_account_session_id
        
        	sync account session id from master to slave
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'iedge4710-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(SubscriberManager.Srg, self).__init__()

            self.yang_name = "srg"
            self.yang_parent_name = "subscriber-manager"

            self.sync_account_session_id = YLeaf(YType.empty, "sync-account-session-id")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("sync_account_session_id") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(SubscriberManager.Srg, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(SubscriberManager.Srg, self).__setattr__(name, value)

        def has_data(self):
            return self.sync_account_session_id.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.sync_account_session_id.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "srg" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-iedge4710-cfg:subscriber-manager/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.sync_account_session_id.is_set or self.sync_account_session_id.yfilter != YFilter.not_set):
                leaf_name_data.append(self.sync_account_session_id.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "sync-account-session-id"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "sync-account-session-id"):
                self.sync_account_session_id = value
                self.sync_account_session_id.value_namespace = name_space
                self.sync_account_session_id.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (
            (self.accounting is not None and self.accounting.has_data()) or
            (self.srg is not None and self.srg.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.accounting is not None and self.accounting.has_operation()) or
            (self.srg is not None and self.srg.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-iedge4710-cfg:subscriber-manager" + path_buffer

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

        if (child_yang_name == "accounting"):
            if (self.accounting is None):
                self.accounting = SubscriberManager.Accounting()
                self.accounting.parent = self
                self._children_name_map["accounting"] = "accounting"
            return self.accounting

        if (child_yang_name == "srg"):
            if (self.srg is None):
                self.srg = SubscriberManager.Srg()
                self.srg.parent = self
                self._children_name_map["srg"] = "srg"
            return self.srg

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "accounting" or name == "srg"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = SubscriberManager()
        return self._top_entity

class SubscriberFeaturette(Entity):
    """
    subscriber featurette
    
    .. attribute:: identity_change
    
    	enable identity change processing
    	**type**\: list of    :py:class:`IdentityChange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg.SubscriberFeaturette.IdentityChange>`
    
    

    """

    _prefix = 'iedge4710-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(SubscriberFeaturette, self).__init__()
        self._top_entity = None

        self.yang_name = "subscriber-featurette"
        self.yang_parent_name = "Cisco-IOS-XR-iedge4710-cfg"

        self.identity_change = YList(self)

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
                    super(SubscriberFeaturette, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(SubscriberFeaturette, self).__setattr__(name, value)


    class IdentityChange(Entity):
        """
        enable identity change processing
        
        .. attribute:: identity_change  <key>
        
        	identity change
        	**type**\:  str
        
        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
        
        .. attribute:: enable
        
        	instance of identity\-change
        	**type**\:  int
        
        	**range:** \-2147483648..2147483647
        
        

        """

        _prefix = 'iedge4710-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(SubscriberFeaturette.IdentityChange, self).__init__()

            self.yang_name = "identity-change"
            self.yang_parent_name = "subscriber-featurette"

            self.identity_change = YLeaf(YType.str, "identity-change")

            self.enable = YLeaf(YType.int32, "enable")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("identity_change",
                            "enable") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(SubscriberFeaturette.IdentityChange, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(SubscriberFeaturette.IdentityChange, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.identity_change.is_set or
                self.enable.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.identity_change.yfilter != YFilter.not_set or
                self.enable.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "identity-change" + "[identity-change='" + self.identity_change.get() + "']" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-iedge4710-cfg:subscriber-featurette/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.identity_change.is_set or self.identity_change.yfilter != YFilter.not_set):
                leaf_name_data.append(self.identity_change.get_name_leafdata())
            if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                leaf_name_data.append(self.enable.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "identity-change" or name == "enable"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "identity-change"):
                self.identity_change = value
                self.identity_change.value_namespace = name_space
                self.identity_change.value_namespace_prefix = name_space_prefix
            if(value_path == "enable"):
                self.enable = value
                self.enable.value_namespace = name_space
                self.enable.value_namespace_prefix = name_space_prefix

    def has_data(self):
        for c in self.identity_change:
            if (c.has_data()):
                return True
        return False

    def has_operation(self):
        for c in self.identity_change:
            if (c.has_operation()):
                return True
        return self.yfilter != YFilter.not_set

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-iedge4710-cfg:subscriber-featurette" + path_buffer

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

        if (child_yang_name == "identity-change"):
            for c in self.identity_change:
                segment = c.get_segment_path()
                if (segment_path == segment):
                    return c
            c = SubscriberFeaturette.IdentityChange()
            c.parent = self
            local_reference_key = "ydk::seg::%s" % segment_path
            self._local_refs[local_reference_key] = c
            self.identity_change.append(c)
            return c

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "identity-change"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = SubscriberFeaturette()
        return self._top_entity

class IedgeLicenseManager(Entity):
    """
    iedge license manager
    
    .. attribute:: node
    
    	Location. For eg., 0/1/CPU0
    	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg.IedgeLicenseManager.Node>`
    
    

    """

    _prefix = 'iedge4710-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(IedgeLicenseManager, self).__init__()
        self._top_entity = None

        self.yang_name = "iedge-license-manager"
        self.yang_parent_name = "Cisco-IOS-XR-iedge4710-cfg"

        self.node = YList(self)

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
                    super(IedgeLicenseManager, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(IedgeLicenseManager, self).__setattr__(name, value)


    class Node(Entity):
        """
        Location. For eg., 0/1/CPU0
        
        .. attribute:: node_name  <key>
        
        	The node id to filter on. For eg., 0/1/CPU0
        	**type**\:  str
        
        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
        
        .. attribute:: session_limit
        
        	Session limit configured on linecard
        	**type**\:  int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: session_threshold
        
        	Session threshold configured on linecard
        	**type**\:  int
        
        	**range:** \-2147483648..2147483647
        
        

        """

        _prefix = 'iedge4710-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(IedgeLicenseManager.Node, self).__init__()

            self.yang_name = "node"
            self.yang_parent_name = "iedge-license-manager"

            self.node_name = YLeaf(YType.str, "node-name")

            self.session_limit = YLeaf(YType.int32, "session-limit")

            self.session_threshold = YLeaf(YType.int32, "session-threshold")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("node_name",
                            "session_limit",
                            "session_threshold") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(IedgeLicenseManager.Node, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(IedgeLicenseManager.Node, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.node_name.is_set or
                self.session_limit.is_set or
                self.session_threshold.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.node_name.yfilter != YFilter.not_set or
                self.session_limit.yfilter != YFilter.not_set or
                self.session_threshold.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "node" + "[node-name='" + self.node_name.get() + "']" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-iedge4710-cfg:iedge-license-manager/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.node_name.is_set or self.node_name.yfilter != YFilter.not_set):
                leaf_name_data.append(self.node_name.get_name_leafdata())
            if (self.session_limit.is_set or self.session_limit.yfilter != YFilter.not_set):
                leaf_name_data.append(self.session_limit.get_name_leafdata())
            if (self.session_threshold.is_set or self.session_threshold.yfilter != YFilter.not_set):
                leaf_name_data.append(self.session_threshold.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "node-name" or name == "session-limit" or name == "session-threshold"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "node-name"):
                self.node_name = value
                self.node_name.value_namespace = name_space
                self.node_name.value_namespace_prefix = name_space_prefix
            if(value_path == "session-limit"):
                self.session_limit = value
                self.session_limit.value_namespace = name_space
                self.session_limit.value_namespace_prefix = name_space_prefix
            if(value_path == "session-threshold"):
                self.session_threshold = value
                self.session_threshold.value_namespace = name_space
                self.session_threshold.value_namespace_prefix = name_space_prefix

    def has_data(self):
        for c in self.node:
            if (c.has_data()):
                return True
        return False

    def has_operation(self):
        for c in self.node:
            if (c.has_operation()):
                return True
        return self.yfilter != YFilter.not_set

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-iedge4710-cfg:iedge-license-manager" + path_buffer

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

        if (child_yang_name == "node"):
            for c in self.node:
                segment = c.get_segment_path()
                if (segment_path == segment):
                    return c
            c = IedgeLicenseManager.Node()
            c.parent = self
            local_reference_key = "ydk::seg::%s" % segment_path
            self._local_refs[local_reference_key] = c
            self.node.append(c)
            return c

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "node"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = IedgeLicenseManager()
        return self._top_entity

class SubManager(Entity):
    """
    sub manager
    
    .. attribute:: location
    
    	Select location
    	**type**\: list of    :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg.SubManager.Location>`
    
    

    """

    _prefix = 'iedge4710-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(SubManager, self).__init__()
        self._top_entity = None

        self.yang_name = "sub-manager"
        self.yang_parent_name = "Cisco-IOS-XR-iedge4710-cfg"

        self.location = YList(self)

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
                    super(SubManager, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(SubManager, self).__setattr__(name, value)


    class Location(Entity):
        """
        Select location
        
        .. attribute:: location1  <key>
        
        	Specify location
        	**type**\:  str
        
        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
        
        .. attribute:: history
        
        	Disable history for subscriber manager
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: trace
        
        	Subscriber manager trace
        	**type**\:   :py:class:`Trace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg.SubManager.Location.Trace>`
        
        

        """

        _prefix = 'iedge4710-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(SubManager.Location, self).__init__()

            self.yang_name = "location"
            self.yang_parent_name = "sub-manager"

            self.location1 = YLeaf(YType.str, "location1")

            self.history = YLeaf(YType.empty, "history")

            self.trace = SubManager.Location.Trace()
            self.trace.parent = self
            self._children_name_map["trace"] = "trace"
            self._children_yang_names.add("trace")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("location1",
                            "history") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(SubManager.Location, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(SubManager.Location, self).__setattr__(name, value)


        class Trace(Entity):
            """
            Subscriber manager trace
            
            .. attribute:: trace_level
            
            	Subscriber manager trace level
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            

            """

            _prefix = 'iedge4710-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(SubManager.Location.Trace, self).__init__()

                self.yang_name = "trace"
                self.yang_parent_name = "location"

                self.trace_level = YLeaf(YType.int32, "trace-level")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("trace_level") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(SubManager.Location.Trace, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(SubManager.Location.Trace, self).__setattr__(name, value)

            def has_data(self):
                return self.trace_level.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.trace_level.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "trace" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.trace_level.is_set or self.trace_level.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.trace_level.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "trace-level"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "trace-level"):
                    self.trace_level = value
                    self.trace_level.value_namespace = name_space
                    self.trace_level.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (
                self.location1.is_set or
                self.history.is_set or
                (self.trace is not None and self.trace.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.location1.yfilter != YFilter.not_set or
                self.history.yfilter != YFilter.not_set or
                (self.trace is not None and self.trace.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "location" + "[location1='" + self.location1.get() + "']" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-iedge4710-cfg:sub-manager/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.location1.is_set or self.location1.yfilter != YFilter.not_set):
                leaf_name_data.append(self.location1.get_name_leafdata())
            if (self.history.is_set or self.history.yfilter != YFilter.not_set):
                leaf_name_data.append(self.history.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "trace"):
                if (self.trace is None):
                    self.trace = SubManager.Location.Trace()
                    self.trace.parent = self
                    self._children_name_map["trace"] = "trace"
                return self.trace

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "trace" or name == "location1" or name == "history"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "location1"):
                self.location1 = value
                self.location1.value_namespace = name_space
                self.location1.value_namespace_prefix = name_space_prefix
            if(value_path == "history"):
                self.history = value
                self.history.value_namespace = name_space
                self.history.value_namespace_prefix = name_space_prefix

    def has_data(self):
        for c in self.location:
            if (c.has_data()):
                return True
        return False

    def has_operation(self):
        for c in self.location:
            if (c.has_operation()):
                return True
        return self.yfilter != YFilter.not_set

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-iedge4710-cfg:sub-manager" + path_buffer

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

        if (child_yang_name == "location"):
            for c in self.location:
                segment = c.get_segment_path()
                if (segment_path == segment):
                    return c
            c = SubManager.Location()
            c.parent = self
            local_reference_key = "ydk::seg::%s" % segment_path
            self._local_refs[local_reference_key] = c
            self.location.append(c)
            return c

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "location"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = SubManager()
        return self._top_entity

