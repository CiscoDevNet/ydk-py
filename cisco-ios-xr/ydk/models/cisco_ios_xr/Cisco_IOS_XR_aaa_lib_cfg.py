""" Cisco_IOS_XR_aaa_lib_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR aaa\-lib package configuration.

This module contains definitions
for the following management objects\:
  aaa\: Authentication, Authorization and Accounting

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Aaa(Entity):
    """
    Authentication, Authorization and Accounting
    
    .. attribute:: aaa_dot1x
    
    	AAA Dot1x
    	**type**\:   :py:class:`AaaDot1X <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.AaaDot1X>`
    
    .. attribute:: aaa_mobile
    
    	AAA Mobile
    	**type**\:   :py:class:`AaaMobile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.AaaMobile>`
    
    .. attribute:: aaa_subscriber
    
    	AAA subscriber
    	**type**\:   :py:class:`AaaSubscriber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.AaaSubscriber>`
    
    .. attribute:: accounting_update
    
    	Configuration related to 'update' accounting
    	**type**\:   :py:class:`AccountingUpdate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.AccountingUpdate>`
    
    	**presence node**\: True
    
    .. attribute:: accountings
    
    	AAA accounting
    	**type**\:   :py:class:`Accountings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Accountings>`
    
    .. attribute:: authentications
    
    	AAA authentication
    	**type**\:   :py:class:`Authentications <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Authentications>`
    
    .. attribute:: authorizations
    
    	AAA authorization
    	**type**\:   :py:class:`Authorizations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Authorizations>`
    
    .. attribute:: banner
    
    	AAA banner
    	**type**\:   :py:class:`Banner <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Banner>`
    
    .. attribute:: default_taskgroup
    
    	This class is used for setting the default taskgroup to be used for remote server authentication
    	**type**\:  str
    
    .. attribute:: diameter
    
    	Diameter base protocol
    	**type**\:   :py:class:`Diameter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Diameter>`
    
    .. attribute:: radius
    
    	Remote Access Dial\-In User Service
    	**type**\:   :py:class:`Radius <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius>`
    
    .. attribute:: radius_attribute
    
    	AAA RADIUS attribute configurations
    	**type**\:   :py:class:`RadiusAttribute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.RadiusAttribute>`
    
    .. attribute:: server_groups
    
    	AAA group definitions
    	**type**\:   :py:class:`ServerGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups>`
    
    .. attribute:: tacacs
    
    	Modify TACACS+ query parameters
    	**type**\:   :py:class:`Tacacs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Tacacs>`
    
    .. attribute:: taskgroups
    
    	Specify a taskgroup to inherit from
    	**type**\:   :py:class:`Taskgroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Taskgroups>`
    
    .. attribute:: usergroups
    
    	Specify a Usergroup to inherit from
    	**type**\:   :py:class:`Usergroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Usergroups>`
    
    .. attribute:: usernames
    
    	Configure local usernames
    	**type**\:   :py:class:`Usernames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Usernames>`
    
    

    """

    _prefix = 'aaa-lib-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(Aaa, self).__init__()
        self._top_entity = None

        self.yang_name = "aaa"
        self.yang_parent_name = "Cisco-IOS-XR-aaa-lib-cfg"

        self.default_taskgroup = YLeaf(YType.str, "Cisco-IOS-XR-aaa-locald-cfg:default-taskgroup")

        self.aaa_dot1x = Aaa.AaaDot1X()
        self.aaa_dot1x.parent = self
        self._children_name_map["aaa_dot1x"] = "aaa-dot1x"
        self._children_yang_names.add("aaa-dot1x")

        self.aaa_mobile = Aaa.AaaMobile()
        self.aaa_mobile.parent = self
        self._children_name_map["aaa_mobile"] = "aaa-mobile"
        self._children_yang_names.add("aaa-mobile")

        self.aaa_subscriber = Aaa.AaaSubscriber()
        self.aaa_subscriber.parent = self
        self._children_name_map["aaa_subscriber"] = "aaa-subscriber"
        self._children_yang_names.add("aaa-subscriber")

        self.accounting_update = None
        self._children_name_map["accounting_update"] = "accounting-update"
        self._children_yang_names.add("accounting-update")

        self.accountings = Aaa.Accountings()
        self.accountings.parent = self
        self._children_name_map["accountings"] = "accountings"
        self._children_yang_names.add("accountings")

        self.authentications = Aaa.Authentications()
        self.authentications.parent = self
        self._children_name_map["authentications"] = "authentications"
        self._children_yang_names.add("authentications")

        self.authorizations = Aaa.Authorizations()
        self.authorizations.parent = self
        self._children_name_map["authorizations"] = "authorizations"
        self._children_yang_names.add("authorizations")

        self.banner = Aaa.Banner()
        self.banner.parent = self
        self._children_name_map["banner"] = "banner"
        self._children_yang_names.add("banner")

        self.diameter = Aaa.Diameter()
        self.diameter.parent = self
        self._children_name_map["diameter"] = "diameter"
        self._children_yang_names.add("diameter")

        self.radius = Aaa.Radius()
        self.radius.parent = self
        self._children_name_map["radius"] = "radius"
        self._children_yang_names.add("radius")

        self.radius_attribute = Aaa.RadiusAttribute()
        self.radius_attribute.parent = self
        self._children_name_map["radius_attribute"] = "radius-attribute"
        self._children_yang_names.add("radius-attribute")

        self.server_groups = Aaa.ServerGroups()
        self.server_groups.parent = self
        self._children_name_map["server_groups"] = "server-groups"
        self._children_yang_names.add("server-groups")

        self.tacacs = Aaa.Tacacs()
        self.tacacs.parent = self
        self._children_name_map["tacacs"] = "tacacs"
        self._children_yang_names.add("tacacs")

        self.taskgroups = Aaa.Taskgroups()
        self.taskgroups.parent = self
        self._children_name_map["taskgroups"] = "taskgroups"
        self._children_yang_names.add("taskgroups")

        self.usergroups = Aaa.Usergroups()
        self.usergroups.parent = self
        self._children_name_map["usergroups"] = "usergroups"
        self._children_yang_names.add("usergroups")

        self.usernames = Aaa.Usernames()
        self.usernames.parent = self
        self._children_name_map["usernames"] = "usernames"
        self._children_yang_names.add("usernames")

    def __setattr__(self, name, value):
        self._check_monkey_patching_error(name, value)
        with _handle_type_error():
            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                    "Please use list append or extend method."
                                    .format(value))
            if isinstance(value, Enum.YLeaf):
                value = value.name
            if name in ("default_taskgroup") and name in self.__dict__:
                if isinstance(value, YLeaf):
                    self.__dict__[name].set(value.get())
                elif isinstance(value, YLeafList):
                    super(Aaa, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(Aaa, self).__setattr__(name, value)


    class Accountings(Entity):
        """
        AAA accounting
        
        .. attribute:: accounting
        
        	Configurations related to accounting
        	**type**\: list of    :py:class:`Accounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Accountings.Accounting>`
        
        

        """

        _prefix = 'aaa-lib-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Aaa.Accountings, self).__init__()

            self.yang_name = "accountings"
            self.yang_parent_name = "aaa"

            self.accounting = YList(self)

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
                        super(Aaa.Accountings, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Aaa.Accountings, self).__setattr__(name, value)


        class Accounting(Entity):
            """
            Configurations related to accounting
            
            .. attribute:: type  <key>
            
            	exec\:Account exec sessions, commands\: Account CLI commands
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: listname  <key>
            
            	Named accounting list
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: broadcast
            
            	Broadcast
            	**type**\:   :py:class:`AaaAccountingBroadcast <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes.AaaAccountingBroadcast>`
            
            .. attribute:: method1
            
            	Method Type
            	**type**\:   :py:class:`AaaMethod <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes.AaaMethod>`
            
            .. attribute:: method2
            
            	Method Type
            	**type**\:   :py:class:`AaaMethod <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes.AaaMethod>`
            
            .. attribute:: method3
            
            	Method Type
            	**type**\:   :py:class:`AaaMethod <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes.AaaMethod>`
            
            .. attribute:: method4
            
            	Method Type
            	**type**\:   :py:class:`AaaMethod <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes.AaaMethod>`
            
            .. attribute:: rp_failover
            
            	rpfailover
            	**type**\:   :py:class:`AaaAccountingRpFailover <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes.AaaAccountingRpFailover>`
            
            .. attribute:: server_group_name1
            
            	Server group name
            	**type**\:  str
            
            .. attribute:: server_group_name2
            
            	Server group name
            	**type**\:  str
            
            .. attribute:: server_group_name3
            
            	Server group name
            	**type**\:  str
            
            .. attribute:: server_group_name4
            
            	Server group name
            	**type**\:  str
            
            .. attribute:: type_xr
            
            	Stop only/Start Stop
            	**type**\:   :py:class:`AaaAccounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes.AaaAccounting>`
            
            

            """

            _prefix = 'aaa-lib-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Accountings.Accounting, self).__init__()

                self.yang_name = "accounting"
                self.yang_parent_name = "accountings"

                self.type = YLeaf(YType.str, "type")

                self.listname = YLeaf(YType.str, "listname")

                self.broadcast = YLeaf(YType.enumeration, "broadcast")

                self.method1 = YLeaf(YType.enumeration, "method1")

                self.method2 = YLeaf(YType.enumeration, "method2")

                self.method3 = YLeaf(YType.enumeration, "method3")

                self.method4 = YLeaf(YType.enumeration, "method4")

                self.rp_failover = YLeaf(YType.enumeration, "rp-failover")

                self.server_group_name1 = YLeaf(YType.str, "server-group-name1")

                self.server_group_name2 = YLeaf(YType.str, "server-group-name2")

                self.server_group_name3 = YLeaf(YType.str, "server-group-name3")

                self.server_group_name4 = YLeaf(YType.str, "server-group-name4")

                self.type_xr = YLeaf(YType.enumeration, "type-xr")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("type",
                                "listname",
                                "broadcast",
                                "method1",
                                "method2",
                                "method3",
                                "method4",
                                "rp_failover",
                                "server_group_name1",
                                "server_group_name2",
                                "server_group_name3",
                                "server_group_name4",
                                "type_xr") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Aaa.Accountings.Accounting, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Aaa.Accountings.Accounting, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.type.is_set or
                    self.listname.is_set or
                    self.broadcast.is_set or
                    self.method1.is_set or
                    self.method2.is_set or
                    self.method3.is_set or
                    self.method4.is_set or
                    self.rp_failover.is_set or
                    self.server_group_name1.is_set or
                    self.server_group_name2.is_set or
                    self.server_group_name3.is_set or
                    self.server_group_name4.is_set or
                    self.type_xr.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.type.yfilter != YFilter.not_set or
                    self.listname.yfilter != YFilter.not_set or
                    self.broadcast.yfilter != YFilter.not_set or
                    self.method1.yfilter != YFilter.not_set or
                    self.method2.yfilter != YFilter.not_set or
                    self.method3.yfilter != YFilter.not_set or
                    self.method4.yfilter != YFilter.not_set or
                    self.rp_failover.yfilter != YFilter.not_set or
                    self.server_group_name1.yfilter != YFilter.not_set or
                    self.server_group_name2.yfilter != YFilter.not_set or
                    self.server_group_name3.yfilter != YFilter.not_set or
                    self.server_group_name4.yfilter != YFilter.not_set or
                    self.type_xr.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "accounting" + "[type='" + self.type.get() + "']" + "[listname='" + self.listname.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/accountings/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.type.get_name_leafdata())
                if (self.listname.is_set or self.listname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.listname.get_name_leafdata())
                if (self.broadcast.is_set or self.broadcast.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.broadcast.get_name_leafdata())
                if (self.method1.is_set or self.method1.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.method1.get_name_leafdata())
                if (self.method2.is_set or self.method2.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.method2.get_name_leafdata())
                if (self.method3.is_set or self.method3.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.method3.get_name_leafdata())
                if (self.method4.is_set or self.method4.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.method4.get_name_leafdata())
                if (self.rp_failover.is_set or self.rp_failover.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rp_failover.get_name_leafdata())
                if (self.server_group_name1.is_set or self.server_group_name1.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.server_group_name1.get_name_leafdata())
                if (self.server_group_name2.is_set or self.server_group_name2.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.server_group_name2.get_name_leafdata())
                if (self.server_group_name3.is_set or self.server_group_name3.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.server_group_name3.get_name_leafdata())
                if (self.server_group_name4.is_set or self.server_group_name4.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.server_group_name4.get_name_leafdata())
                if (self.type_xr.is_set or self.type_xr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.type_xr.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "type" or name == "listname" or name == "broadcast" or name == "method1" or name == "method2" or name == "method3" or name == "method4" or name == "rp-failover" or name == "server-group-name1" or name == "server-group-name2" or name == "server-group-name3" or name == "server-group-name4" or name == "type-xr"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "type"):
                    self.type = value
                    self.type.value_namespace = name_space
                    self.type.value_namespace_prefix = name_space_prefix
                if(value_path == "listname"):
                    self.listname = value
                    self.listname.value_namespace = name_space
                    self.listname.value_namespace_prefix = name_space_prefix
                if(value_path == "broadcast"):
                    self.broadcast = value
                    self.broadcast.value_namespace = name_space
                    self.broadcast.value_namespace_prefix = name_space_prefix
                if(value_path == "method1"):
                    self.method1 = value
                    self.method1.value_namespace = name_space
                    self.method1.value_namespace_prefix = name_space_prefix
                if(value_path == "method2"):
                    self.method2 = value
                    self.method2.value_namespace = name_space
                    self.method2.value_namespace_prefix = name_space_prefix
                if(value_path == "method3"):
                    self.method3 = value
                    self.method3.value_namespace = name_space
                    self.method3.value_namespace_prefix = name_space_prefix
                if(value_path == "method4"):
                    self.method4 = value
                    self.method4.value_namespace = name_space
                    self.method4.value_namespace_prefix = name_space_prefix
                if(value_path == "rp-failover"):
                    self.rp_failover = value
                    self.rp_failover.value_namespace = name_space
                    self.rp_failover.value_namespace_prefix = name_space_prefix
                if(value_path == "server-group-name1"):
                    self.server_group_name1 = value
                    self.server_group_name1.value_namespace = name_space
                    self.server_group_name1.value_namespace_prefix = name_space_prefix
                if(value_path == "server-group-name2"):
                    self.server_group_name2 = value
                    self.server_group_name2.value_namespace = name_space
                    self.server_group_name2.value_namespace_prefix = name_space_prefix
                if(value_path == "server-group-name3"):
                    self.server_group_name3 = value
                    self.server_group_name3.value_namespace = name_space
                    self.server_group_name3.value_namespace_prefix = name_space_prefix
                if(value_path == "server-group-name4"):
                    self.server_group_name4 = value
                    self.server_group_name4.value_namespace = name_space
                    self.server_group_name4.value_namespace_prefix = name_space_prefix
                if(value_path == "type-xr"):
                    self.type_xr = value
                    self.type_xr.value_namespace = name_space
                    self.type_xr.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.accounting:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.accounting:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "accountings" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "accounting"):
                for c in self.accounting:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Aaa.Accountings.Accounting()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.accounting.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "accounting"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Authorizations(Entity):
        """
        AAA authorization
        
        .. attribute:: authorization
        
        	Configurations related to authorization
        	**type**\: list of    :py:class:`Authorization <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Authorizations.Authorization>`
        
        

        """

        _prefix = 'aaa-lib-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Aaa.Authorizations, self).__init__()

            self.yang_name = "authorizations"
            self.yang_parent_name = "aaa"

            self.authorization = YList(self)

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
                        super(Aaa.Authorizations, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Aaa.Authorizations, self).__setattr__(name, value)


        class Authorization(Entity):
            """
            Configurations related to authorization
            
            .. attribute:: type  <key>
            
            	network\: Authorize IKE requests, commands\: Authorize CLI commands
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: listname  <key>
            
            	List name for AAA authorization
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: method1
            
            	Method Type
            	**type**\:   :py:class:`AaaMethod <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes.AaaMethod>`
            
            .. attribute:: method2
            
            	Method Type
            	**type**\:   :py:class:`AaaMethod <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes.AaaMethod>`
            
            .. attribute:: method3
            
            	Method Type
            	**type**\:   :py:class:`AaaMethod <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes.AaaMethod>`
            
            .. attribute:: method4
            
            	Method Type
            	**type**\:   :py:class:`AaaMethod <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes.AaaMethod>`
            
            .. attribute:: server_group_name1
            
            	Server group name
            	**type**\:  str
            
            .. attribute:: server_group_name2
            
            	Server group name
            	**type**\:  str
            
            .. attribute:: server_group_name3
            
            	Server group name
            	**type**\:  str
            
            .. attribute:: server_group_name4
            
            	Server group name
            	**type**\:  str
            
            

            """

            _prefix = 'aaa-lib-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Authorizations.Authorization, self).__init__()

                self.yang_name = "authorization"
                self.yang_parent_name = "authorizations"

                self.type = YLeaf(YType.str, "type")

                self.listname = YLeaf(YType.str, "listname")

                self.method1 = YLeaf(YType.enumeration, "method1")

                self.method2 = YLeaf(YType.enumeration, "method2")

                self.method3 = YLeaf(YType.enumeration, "method3")

                self.method4 = YLeaf(YType.enumeration, "method4")

                self.server_group_name1 = YLeaf(YType.str, "server-group-name1")

                self.server_group_name2 = YLeaf(YType.str, "server-group-name2")

                self.server_group_name3 = YLeaf(YType.str, "server-group-name3")

                self.server_group_name4 = YLeaf(YType.str, "server-group-name4")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("type",
                                "listname",
                                "method1",
                                "method2",
                                "method3",
                                "method4",
                                "server_group_name1",
                                "server_group_name2",
                                "server_group_name3",
                                "server_group_name4") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Aaa.Authorizations.Authorization, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Aaa.Authorizations.Authorization, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.type.is_set or
                    self.listname.is_set or
                    self.method1.is_set or
                    self.method2.is_set or
                    self.method3.is_set or
                    self.method4.is_set or
                    self.server_group_name1.is_set or
                    self.server_group_name2.is_set or
                    self.server_group_name3.is_set or
                    self.server_group_name4.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.type.yfilter != YFilter.not_set or
                    self.listname.yfilter != YFilter.not_set or
                    self.method1.yfilter != YFilter.not_set or
                    self.method2.yfilter != YFilter.not_set or
                    self.method3.yfilter != YFilter.not_set or
                    self.method4.yfilter != YFilter.not_set or
                    self.server_group_name1.yfilter != YFilter.not_set or
                    self.server_group_name2.yfilter != YFilter.not_set or
                    self.server_group_name3.yfilter != YFilter.not_set or
                    self.server_group_name4.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "authorization" + "[type='" + self.type.get() + "']" + "[listname='" + self.listname.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/authorizations/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.type.get_name_leafdata())
                if (self.listname.is_set or self.listname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.listname.get_name_leafdata())
                if (self.method1.is_set or self.method1.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.method1.get_name_leafdata())
                if (self.method2.is_set or self.method2.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.method2.get_name_leafdata())
                if (self.method3.is_set or self.method3.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.method3.get_name_leafdata())
                if (self.method4.is_set or self.method4.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.method4.get_name_leafdata())
                if (self.server_group_name1.is_set or self.server_group_name1.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.server_group_name1.get_name_leafdata())
                if (self.server_group_name2.is_set or self.server_group_name2.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.server_group_name2.get_name_leafdata())
                if (self.server_group_name3.is_set or self.server_group_name3.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.server_group_name3.get_name_leafdata())
                if (self.server_group_name4.is_set or self.server_group_name4.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.server_group_name4.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "type" or name == "listname" or name == "method1" or name == "method2" or name == "method3" or name == "method4" or name == "server-group-name1" or name == "server-group-name2" or name == "server-group-name3" or name == "server-group-name4"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "type"):
                    self.type = value
                    self.type.value_namespace = name_space
                    self.type.value_namespace_prefix = name_space_prefix
                if(value_path == "listname"):
                    self.listname = value
                    self.listname.value_namespace = name_space
                    self.listname.value_namespace_prefix = name_space_prefix
                if(value_path == "method1"):
                    self.method1 = value
                    self.method1.value_namespace = name_space
                    self.method1.value_namespace_prefix = name_space_prefix
                if(value_path == "method2"):
                    self.method2 = value
                    self.method2.value_namespace = name_space
                    self.method2.value_namespace_prefix = name_space_prefix
                if(value_path == "method3"):
                    self.method3 = value
                    self.method3.value_namespace = name_space
                    self.method3.value_namespace_prefix = name_space_prefix
                if(value_path == "method4"):
                    self.method4 = value
                    self.method4.value_namespace = name_space
                    self.method4.value_namespace_prefix = name_space_prefix
                if(value_path == "server-group-name1"):
                    self.server_group_name1 = value
                    self.server_group_name1.value_namespace = name_space
                    self.server_group_name1.value_namespace_prefix = name_space_prefix
                if(value_path == "server-group-name2"):
                    self.server_group_name2 = value
                    self.server_group_name2.value_namespace = name_space
                    self.server_group_name2.value_namespace_prefix = name_space_prefix
                if(value_path == "server-group-name3"):
                    self.server_group_name3 = value
                    self.server_group_name3.value_namespace = name_space
                    self.server_group_name3.value_namespace_prefix = name_space_prefix
                if(value_path == "server-group-name4"):
                    self.server_group_name4 = value
                    self.server_group_name4.value_namespace = name_space
                    self.server_group_name4.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.authorization:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.authorization:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "authorizations" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "authorization"):
                for c in self.authorization:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Aaa.Authorizations.Authorization()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.authorization.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "authorization"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class AccountingUpdate(Entity):
        """
        Configuration related to 'update' accounting
        
        .. attribute:: periodic_interval
        
        	Periodic update interval in minutes
        	**type**\:  int
        
        	**range:** 0..35791394
        
        	**units**\: minute
        
        .. attribute:: type
        
        	newinfo/periodic
        	**type**\:   :py:class:`AaaAccountingUpdate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes.AaaAccountingUpdate>`
        
        	**mandatory**\: True
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'aaa-lib-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Aaa.AccountingUpdate, self).__init__()

            self.yang_name = "accounting-update"
            self.yang_parent_name = "aaa"
            self.is_presence_container = True

            self.periodic_interval = YLeaf(YType.uint32, "periodic-interval")

            self.type = YLeaf(YType.enumeration, "type")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("periodic_interval",
                            "type") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Aaa.AccountingUpdate, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Aaa.AccountingUpdate, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.periodic_interval.is_set or
                self.type.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.periodic_interval.yfilter != YFilter.not_set or
                self.type.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "accounting-update" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.periodic_interval.is_set or self.periodic_interval.yfilter != YFilter.not_set):
                leaf_name_data.append(self.periodic_interval.get_name_leafdata())
            if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                leaf_name_data.append(self.type.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "periodic-interval" or name == "type"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "periodic-interval"):
                self.periodic_interval = value
                self.periodic_interval.value_namespace = name_space
                self.periodic_interval.value_namespace_prefix = name_space_prefix
            if(value_path == "type"):
                self.type = value
                self.type.value_namespace = name_space
                self.type.value_namespace_prefix = name_space_prefix


    class Banner(Entity):
        """
        AAA banner
        
        .. attribute:: login
        
        	AAA login banner
        	**type**\:  str
        
        

        """

        _prefix = 'aaa-lib-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Aaa.Banner, self).__init__()

            self.yang_name = "banner"
            self.yang_parent_name = "aaa"

            self.login = YLeaf(YType.str, "login")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("login") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Aaa.Banner, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Aaa.Banner, self).__setattr__(name, value)

        def has_data(self):
            return self.login.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.login.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "banner" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.login.is_set or self.login.yfilter != YFilter.not_set):
                leaf_name_data.append(self.login.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "login"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "login"):
                self.login = value
                self.login.value_namespace = name_space
                self.login.value_namespace_prefix = name_space_prefix


    class Authentications(Entity):
        """
        AAA authentication
        
        .. attribute:: authentication
        
        	Configurations related to authentication
        	**type**\: list of    :py:class:`Authentication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Authentications.Authentication>`
        
        

        """

        _prefix = 'aaa-lib-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Aaa.Authentications, self).__init__()

            self.yang_name = "authentications"
            self.yang_parent_name = "aaa"

            self.authentication = YList(self)

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
                        super(Aaa.Authentications, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Aaa.Authentications, self).__setattr__(name, value)


        class Authentication(Entity):
            """
            Configurations related to authentication
            
            .. attribute:: type  <key>
            
            	login\: Authenticate login sessions, ppp\: Authenticate ppp sessions
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: listname  <key>
            
            	List name for AAA authentication
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: method1
            
            	Method Type
            	**type**\:   :py:class:`AaaMethod <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes.AaaMethod>`
            
            .. attribute:: method2
            
            	Method Type
            	**type**\:   :py:class:`AaaMethod <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes.AaaMethod>`
            
            .. attribute:: method3
            
            	Method Type
            	**type**\:   :py:class:`AaaMethod <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes.AaaMethod>`
            
            .. attribute:: method4
            
            	Method Type
            	**type**\:   :py:class:`AaaMethod <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes.AaaMethod>`
            
            .. attribute:: server_group_name1
            
            	Server group name
            	**type**\:  str
            
            .. attribute:: server_group_name2
            
            	Server group name
            	**type**\:  str
            
            .. attribute:: server_group_name3
            
            	Server group name
            	**type**\:  str
            
            .. attribute:: server_group_name4
            
            	Server group name
            	**type**\:  str
            
            

            """

            _prefix = 'aaa-lib-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Authentications.Authentication, self).__init__()

                self.yang_name = "authentication"
                self.yang_parent_name = "authentications"

                self.type = YLeaf(YType.str, "type")

                self.listname = YLeaf(YType.str, "listname")

                self.method1 = YLeaf(YType.enumeration, "method1")

                self.method2 = YLeaf(YType.enumeration, "method2")

                self.method3 = YLeaf(YType.enumeration, "method3")

                self.method4 = YLeaf(YType.enumeration, "method4")

                self.server_group_name1 = YLeaf(YType.str, "server-group-name1")

                self.server_group_name2 = YLeaf(YType.str, "server-group-name2")

                self.server_group_name3 = YLeaf(YType.str, "server-group-name3")

                self.server_group_name4 = YLeaf(YType.str, "server-group-name4")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("type",
                                "listname",
                                "method1",
                                "method2",
                                "method3",
                                "method4",
                                "server_group_name1",
                                "server_group_name2",
                                "server_group_name3",
                                "server_group_name4") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Aaa.Authentications.Authentication, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Aaa.Authentications.Authentication, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.type.is_set or
                    self.listname.is_set or
                    self.method1.is_set or
                    self.method2.is_set or
                    self.method3.is_set or
                    self.method4.is_set or
                    self.server_group_name1.is_set or
                    self.server_group_name2.is_set or
                    self.server_group_name3.is_set or
                    self.server_group_name4.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.type.yfilter != YFilter.not_set or
                    self.listname.yfilter != YFilter.not_set or
                    self.method1.yfilter != YFilter.not_set or
                    self.method2.yfilter != YFilter.not_set or
                    self.method3.yfilter != YFilter.not_set or
                    self.method4.yfilter != YFilter.not_set or
                    self.server_group_name1.yfilter != YFilter.not_set or
                    self.server_group_name2.yfilter != YFilter.not_set or
                    self.server_group_name3.yfilter != YFilter.not_set or
                    self.server_group_name4.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "authentication" + "[type='" + self.type.get() + "']" + "[listname='" + self.listname.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/authentications/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.type.get_name_leafdata())
                if (self.listname.is_set or self.listname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.listname.get_name_leafdata())
                if (self.method1.is_set or self.method1.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.method1.get_name_leafdata())
                if (self.method2.is_set or self.method2.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.method2.get_name_leafdata())
                if (self.method3.is_set or self.method3.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.method3.get_name_leafdata())
                if (self.method4.is_set or self.method4.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.method4.get_name_leafdata())
                if (self.server_group_name1.is_set or self.server_group_name1.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.server_group_name1.get_name_leafdata())
                if (self.server_group_name2.is_set or self.server_group_name2.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.server_group_name2.get_name_leafdata())
                if (self.server_group_name3.is_set or self.server_group_name3.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.server_group_name3.get_name_leafdata())
                if (self.server_group_name4.is_set or self.server_group_name4.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.server_group_name4.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "type" or name == "listname" or name == "method1" or name == "method2" or name == "method3" or name == "method4" or name == "server-group-name1" or name == "server-group-name2" or name == "server-group-name3" or name == "server-group-name4"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "type"):
                    self.type = value
                    self.type.value_namespace = name_space
                    self.type.value_namespace_prefix = name_space_prefix
                if(value_path == "listname"):
                    self.listname = value
                    self.listname.value_namespace = name_space
                    self.listname.value_namespace_prefix = name_space_prefix
                if(value_path == "method1"):
                    self.method1 = value
                    self.method1.value_namespace = name_space
                    self.method1.value_namespace_prefix = name_space_prefix
                if(value_path == "method2"):
                    self.method2 = value
                    self.method2.value_namespace = name_space
                    self.method2.value_namespace_prefix = name_space_prefix
                if(value_path == "method3"):
                    self.method3 = value
                    self.method3.value_namespace = name_space
                    self.method3.value_namespace_prefix = name_space_prefix
                if(value_path == "method4"):
                    self.method4 = value
                    self.method4.value_namespace = name_space
                    self.method4.value_namespace_prefix = name_space_prefix
                if(value_path == "server-group-name1"):
                    self.server_group_name1 = value
                    self.server_group_name1.value_namespace = name_space
                    self.server_group_name1.value_namespace_prefix = name_space_prefix
                if(value_path == "server-group-name2"):
                    self.server_group_name2 = value
                    self.server_group_name2.value_namespace = name_space
                    self.server_group_name2.value_namespace_prefix = name_space_prefix
                if(value_path == "server-group-name3"):
                    self.server_group_name3 = value
                    self.server_group_name3.value_namespace = name_space
                    self.server_group_name3.value_namespace_prefix = name_space_prefix
                if(value_path == "server-group-name4"):
                    self.server_group_name4 = value
                    self.server_group_name4.value_namespace = name_space
                    self.server_group_name4.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.authentication:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.authentication:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "authentications" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "authentication"):
                for c in self.authentication:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Aaa.Authentications.Authentication()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.authentication.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "authentication"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class AaaSubscriber(Entity):
        """
        AAA subscriber
        
        .. attribute:: accountings
        
        	AAA accounting
        	**type**\:   :py:class:`Accountings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.AaaSubscriber.Accountings>`
        
        .. attribute:: authentications
        
        	AAA authentication
        	**type**\:   :py:class:`Authentications <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.AaaSubscriber.Authentications>`
        
        .. attribute:: authorizations
        
        	AAA authorization
        	**type**\:   :py:class:`Authorizations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.AaaSubscriber.Authorizations>`
        
        .. attribute:: policy_if_authors
        
        	AAA authorization policy
        	**type**\:   :py:class:`PolicyIfAuthors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.AaaSubscriber.PolicyIfAuthors>`
        
        .. attribute:: prepaid_authors
        
        	AAA authorization prepaid
        	**type**\:   :py:class:`PrepaidAuthors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.AaaSubscriber.PrepaidAuthors>`
        
        .. attribute:: service_accounting
        
        	Set accounting parameters for Service
        	**type**\:   :py:class:`ServiceAccounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.AaaSubscriber.ServiceAccounting>`
        
        

        """

        _prefix = 'aaa-aaacore-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Aaa.AaaSubscriber, self).__init__()

            self.yang_name = "aaa-subscriber"
            self.yang_parent_name = "aaa"

            self.accountings = Aaa.AaaSubscriber.Accountings()
            self.accountings.parent = self
            self._children_name_map["accountings"] = "accountings"
            self._children_yang_names.add("accountings")

            self.authentications = Aaa.AaaSubscriber.Authentications()
            self.authentications.parent = self
            self._children_name_map["authentications"] = "authentications"
            self._children_yang_names.add("authentications")

            self.authorizations = Aaa.AaaSubscriber.Authorizations()
            self.authorizations.parent = self
            self._children_name_map["authorizations"] = "authorizations"
            self._children_yang_names.add("authorizations")

            self.policy_if_authors = Aaa.AaaSubscriber.PolicyIfAuthors()
            self.policy_if_authors.parent = self
            self._children_name_map["policy_if_authors"] = "policy-if-authors"
            self._children_yang_names.add("policy-if-authors")

            self.prepaid_authors = Aaa.AaaSubscriber.PrepaidAuthors()
            self.prepaid_authors.parent = self
            self._children_name_map["prepaid_authors"] = "prepaid-authors"
            self._children_yang_names.add("prepaid-authors")

            self.service_accounting = Aaa.AaaSubscriber.ServiceAccounting()
            self.service_accounting.parent = self
            self._children_name_map["service_accounting"] = "service-accounting"
            self._children_yang_names.add("service-accounting")


        class PolicyIfAuthors(Entity):
            """
            AAA authorization policy
            
            .. attribute:: policy_if_author
            
            	Configurations related to authorization
            	**type**\: list of    :py:class:`PolicyIfAuthor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.AaaSubscriber.PolicyIfAuthors.PolicyIfAuthor>`
            
            

            """

            _prefix = 'aaa-aaacore-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.AaaSubscriber.PolicyIfAuthors, self).__init__()

                self.yang_name = "policy-if-authors"
                self.yang_parent_name = "aaa-subscriber"

                self.policy_if_author = YList(self)

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
                            super(Aaa.AaaSubscriber.PolicyIfAuthors, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Aaa.AaaSubscriber.PolicyIfAuthors, self).__setattr__(name, value)


            class PolicyIfAuthor(Entity):
                """
                Configurations related to authorization
                
                .. attribute:: type  <key>
                
                	Set authorization lists
                	**type**\:  str
                
                	**pattern:** (subscriber)\|(service)\|(policy\-if)\|(prepaid)\|(dot1x)
                
                .. attribute:: listname  <key>
                
                	Named authorization list
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: method
                
                	Method Types
                	**type**\:  list of   :py:class:`AaaMethod <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes.AaaMethod>`
                
                .. attribute:: server_group_name
                
                	Server group names
                	**type**\:  list of str
                
                

                """

                _prefix = 'aaa-aaacore-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.AaaSubscriber.PolicyIfAuthors.PolicyIfAuthor, self).__init__()

                    self.yang_name = "policy-if-author"
                    self.yang_parent_name = "policy-if-authors"

                    self.type = YLeaf(YType.str, "type")

                    self.listname = YLeaf(YType.str, "listname")

                    self.method = YLeafList(YType.enumeration, "method")

                    self.server_group_name = YLeafList(YType.str, "server-group-name")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("type",
                                    "listname",
                                    "method",
                                    "server_group_name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Aaa.AaaSubscriber.PolicyIfAuthors.PolicyIfAuthor, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Aaa.AaaSubscriber.PolicyIfAuthors.PolicyIfAuthor, self).__setattr__(name, value)

                def has_data(self):
                    for leaf in self.method.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.server_group_name.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    return (
                        self.type.is_set or
                        self.listname.is_set)

                def has_operation(self):
                    for leaf in self.method.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.server_group_name.getYLeafs():
                        if (leaf.is_set):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.type.yfilter != YFilter.not_set or
                        self.listname.yfilter != YFilter.not_set or
                        self.method.yfilter != YFilter.not_set or
                        self.server_group_name.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "policy-if-author" + "[type='" + self.type.get() + "']" + "[listname='" + self.listname.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:aaa-subscriber/policy-if-authors/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.type.get_name_leafdata())
                    if (self.listname.is_set or self.listname.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.listname.get_name_leafdata())

                    leaf_name_data.extend(self.method.get_name_leafdata())

                    leaf_name_data.extend(self.server_group_name.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "type" or name == "listname" or name == "method" or name == "server-group-name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "type"):
                        self.type = value
                        self.type.value_namespace = name_space
                        self.type.value_namespace_prefix = name_space_prefix
                    if(value_path == "listname"):
                        self.listname = value
                        self.listname.value_namespace = name_space
                        self.listname.value_namespace_prefix = name_space_prefix
                    if(value_path == "method"):
                        self.method.append(value)
                    if(value_path == "server-group-name"):
                        self.server_group_name.append(value)

            def has_data(self):
                for c in self.policy_if_author:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.policy_if_author:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "policy-if-authors" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:aaa-subscriber/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "policy-if-author"):
                    for c in self.policy_if_author:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Aaa.AaaSubscriber.PolicyIfAuthors.PolicyIfAuthor()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.policy_if_author.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "policy-if-author"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class Accountings(Entity):
            """
            AAA accounting
            
            .. attribute:: accounting
            
            	Configurations related to accounting
            	**type**\: list of    :py:class:`Accounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.AaaSubscriber.Accountings.Accounting>`
            
            

            """

            _prefix = 'aaa-aaacore-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.AaaSubscriber.Accountings, self).__init__()

                self.yang_name = "accountings"
                self.yang_parent_name = "aaa-subscriber"

                self.accounting = YList(self)

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
                            super(Aaa.AaaSubscriber.Accountings, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Aaa.AaaSubscriber.Accountings, self).__setattr__(name, value)


            class Accounting(Entity):
                """
                Configurations related to accounting
                
                .. attribute:: type  <key>
                
                	Set accounting lists
                	**type**\:  str
                
                	**pattern:** (subscriber)\|(service)\|(policy\-if)\|(prepaid)\|(dot1x)
                
                .. attribute:: listname  <key>
                
                	Named accounting list
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: broadcast
                
                	Broadcast
                	**type**\:   :py:class:`AaaAccountingBroadcast <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes.AaaAccountingBroadcast>`
                
                	**mandatory**\: True
                
                .. attribute:: method
                
                	Method Types
                	**type**\:  list of   :py:class:`AaaMethod <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes.AaaMethod>`
                
                .. attribute:: server_group_name
                
                	Server group names
                	**type**\:  list of str
                
                

                """

                _prefix = 'aaa-aaacore-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.AaaSubscriber.Accountings.Accounting, self).__init__()

                    self.yang_name = "accounting"
                    self.yang_parent_name = "accountings"

                    self.type = YLeaf(YType.str, "type")

                    self.listname = YLeaf(YType.str, "listname")

                    self.broadcast = YLeaf(YType.enumeration, "broadcast")

                    self.method = YLeafList(YType.enumeration, "method")

                    self.server_group_name = YLeafList(YType.str, "server-group-name")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("type",
                                    "listname",
                                    "broadcast",
                                    "method",
                                    "server_group_name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Aaa.AaaSubscriber.Accountings.Accounting, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Aaa.AaaSubscriber.Accountings.Accounting, self).__setattr__(name, value)

                def has_data(self):
                    for leaf in self.method.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.server_group_name.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    return (
                        self.type.is_set or
                        self.listname.is_set or
                        self.broadcast.is_set)

                def has_operation(self):
                    for leaf in self.method.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.server_group_name.getYLeafs():
                        if (leaf.is_set):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.type.yfilter != YFilter.not_set or
                        self.listname.yfilter != YFilter.not_set or
                        self.broadcast.yfilter != YFilter.not_set or
                        self.method.yfilter != YFilter.not_set or
                        self.server_group_name.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "accounting" + "[type='" + self.type.get() + "']" + "[listname='" + self.listname.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:aaa-subscriber/accountings/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.type.get_name_leafdata())
                    if (self.listname.is_set or self.listname.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.listname.get_name_leafdata())
                    if (self.broadcast.is_set or self.broadcast.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.broadcast.get_name_leafdata())

                    leaf_name_data.extend(self.method.get_name_leafdata())

                    leaf_name_data.extend(self.server_group_name.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "type" or name == "listname" or name == "broadcast" or name == "method" or name == "server-group-name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "type"):
                        self.type = value
                        self.type.value_namespace = name_space
                        self.type.value_namespace_prefix = name_space_prefix
                    if(value_path == "listname"):
                        self.listname = value
                        self.listname.value_namespace = name_space
                        self.listname.value_namespace_prefix = name_space_prefix
                    if(value_path == "broadcast"):
                        self.broadcast = value
                        self.broadcast.value_namespace = name_space
                        self.broadcast.value_namespace_prefix = name_space_prefix
                    if(value_path == "method"):
                        self.method.append(value)
                    if(value_path == "server-group-name"):
                        self.server_group_name.append(value)

            def has_data(self):
                for c in self.accounting:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.accounting:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "accountings" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:aaa-subscriber/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "accounting"):
                    for c in self.accounting:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Aaa.AaaSubscriber.Accountings.Accounting()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.accounting.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "accounting"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class ServiceAccounting(Entity):
            """
            Set accounting parameters for Service
            
            .. attribute:: type
            
            	Send extended/brief service accounting records
            	**type**\:   :py:class:`AaaServiceAccounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_aaacore_cfg.AaaServiceAccounting>`
            
            

            """

            _prefix = 'aaa-aaacore-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.AaaSubscriber.ServiceAccounting, self).__init__()

                self.yang_name = "service-accounting"
                self.yang_parent_name = "aaa-subscriber"

                self.type = YLeaf(YType.enumeration, "type")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("type") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Aaa.AaaSubscriber.ServiceAccounting, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Aaa.AaaSubscriber.ServiceAccounting, self).__setattr__(name, value)

            def has_data(self):
                return self.type.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.type.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "service-accounting" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:aaa-subscriber/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.type.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "type"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "type"):
                    self.type = value
                    self.type.value_namespace = name_space
                    self.type.value_namespace_prefix = name_space_prefix


        class PrepaidAuthors(Entity):
            """
            AAA authorization prepaid
            
            .. attribute:: prepaid_author
            
            	Configurations related to authorization
            	**type**\: list of    :py:class:`PrepaidAuthor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.AaaSubscriber.PrepaidAuthors.PrepaidAuthor>`
            
            

            """

            _prefix = 'aaa-aaacore-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.AaaSubscriber.PrepaidAuthors, self).__init__()

                self.yang_name = "prepaid-authors"
                self.yang_parent_name = "aaa-subscriber"

                self.prepaid_author = YList(self)

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
                            super(Aaa.AaaSubscriber.PrepaidAuthors, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Aaa.AaaSubscriber.PrepaidAuthors, self).__setattr__(name, value)


            class PrepaidAuthor(Entity):
                """
                Configurations related to authorization
                
                .. attribute:: type  <key>
                
                	Set authorization lists
                	**type**\:  str
                
                	**pattern:** (subscriber)\|(service)\|(policy\-if)\|(prepaid)\|(dot1x)
                
                .. attribute:: listname  <key>
                
                	Named authorization list
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: method
                
                	Method Types
                	**type**\:  list of   :py:class:`AaaMethod <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes.AaaMethod>`
                
                .. attribute:: server_group_name
                
                	Server group names
                	**type**\:  list of str
                
                

                """

                _prefix = 'aaa-aaacore-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.AaaSubscriber.PrepaidAuthors.PrepaidAuthor, self).__init__()

                    self.yang_name = "prepaid-author"
                    self.yang_parent_name = "prepaid-authors"

                    self.type = YLeaf(YType.str, "type")

                    self.listname = YLeaf(YType.str, "listname")

                    self.method = YLeafList(YType.enumeration, "method")

                    self.server_group_name = YLeafList(YType.str, "server-group-name")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("type",
                                    "listname",
                                    "method",
                                    "server_group_name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Aaa.AaaSubscriber.PrepaidAuthors.PrepaidAuthor, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Aaa.AaaSubscriber.PrepaidAuthors.PrepaidAuthor, self).__setattr__(name, value)

                def has_data(self):
                    for leaf in self.method.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.server_group_name.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    return (
                        self.type.is_set or
                        self.listname.is_set)

                def has_operation(self):
                    for leaf in self.method.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.server_group_name.getYLeafs():
                        if (leaf.is_set):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.type.yfilter != YFilter.not_set or
                        self.listname.yfilter != YFilter.not_set or
                        self.method.yfilter != YFilter.not_set or
                        self.server_group_name.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "prepaid-author" + "[type='" + self.type.get() + "']" + "[listname='" + self.listname.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:aaa-subscriber/prepaid-authors/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.type.get_name_leafdata())
                    if (self.listname.is_set or self.listname.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.listname.get_name_leafdata())

                    leaf_name_data.extend(self.method.get_name_leafdata())

                    leaf_name_data.extend(self.server_group_name.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "type" or name == "listname" or name == "method" or name == "server-group-name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "type"):
                        self.type = value
                        self.type.value_namespace = name_space
                        self.type.value_namespace_prefix = name_space_prefix
                    if(value_path == "listname"):
                        self.listname = value
                        self.listname.value_namespace = name_space
                        self.listname.value_namespace_prefix = name_space_prefix
                    if(value_path == "method"):
                        self.method.append(value)
                    if(value_path == "server-group-name"):
                        self.server_group_name.append(value)

            def has_data(self):
                for c in self.prepaid_author:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.prepaid_author:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "prepaid-authors" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:aaa-subscriber/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "prepaid-author"):
                    for c in self.prepaid_author:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Aaa.AaaSubscriber.PrepaidAuthors.PrepaidAuthor()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.prepaid_author.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "prepaid-author"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class Authorizations(Entity):
            """
            AAA authorization
            
            .. attribute:: authorization
            
            	Configurations related to authorization
            	**type**\: list of    :py:class:`Authorization <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.AaaSubscriber.Authorizations.Authorization>`
            
            

            """

            _prefix = 'aaa-aaacore-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.AaaSubscriber.Authorizations, self).__init__()

                self.yang_name = "authorizations"
                self.yang_parent_name = "aaa-subscriber"

                self.authorization = YList(self)

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
                            super(Aaa.AaaSubscriber.Authorizations, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Aaa.AaaSubscriber.Authorizations, self).__setattr__(name, value)


            class Authorization(Entity):
                """
                Configurations related to authorization
                
                .. attribute:: type  <key>
                
                	Set authorization lists
                	**type**\:  str
                
                	**pattern:** (subscriber)\|(service)\|(policy\-if)\|(prepaid)\|(dot1x)
                
                .. attribute:: listname  <key>
                
                	Named authorization list
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: method
                
                	Method Types
                	**type**\:  list of   :py:class:`AaaMethod <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes.AaaMethod>`
                
                .. attribute:: server_group_name
                
                	Server group names
                	**type**\:  list of str
                
                

                """

                _prefix = 'aaa-aaacore-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.AaaSubscriber.Authorizations.Authorization, self).__init__()

                    self.yang_name = "authorization"
                    self.yang_parent_name = "authorizations"

                    self.type = YLeaf(YType.str, "type")

                    self.listname = YLeaf(YType.str, "listname")

                    self.method = YLeafList(YType.enumeration, "method")

                    self.server_group_name = YLeafList(YType.str, "server-group-name")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("type",
                                    "listname",
                                    "method",
                                    "server_group_name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Aaa.AaaSubscriber.Authorizations.Authorization, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Aaa.AaaSubscriber.Authorizations.Authorization, self).__setattr__(name, value)

                def has_data(self):
                    for leaf in self.method.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.server_group_name.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    return (
                        self.type.is_set or
                        self.listname.is_set)

                def has_operation(self):
                    for leaf in self.method.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.server_group_name.getYLeafs():
                        if (leaf.is_set):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.type.yfilter != YFilter.not_set or
                        self.listname.yfilter != YFilter.not_set or
                        self.method.yfilter != YFilter.not_set or
                        self.server_group_name.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "authorization" + "[type='" + self.type.get() + "']" + "[listname='" + self.listname.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:aaa-subscriber/authorizations/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.type.get_name_leafdata())
                    if (self.listname.is_set or self.listname.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.listname.get_name_leafdata())

                    leaf_name_data.extend(self.method.get_name_leafdata())

                    leaf_name_data.extend(self.server_group_name.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "type" or name == "listname" or name == "method" or name == "server-group-name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "type"):
                        self.type = value
                        self.type.value_namespace = name_space
                        self.type.value_namespace_prefix = name_space_prefix
                    if(value_path == "listname"):
                        self.listname = value
                        self.listname.value_namespace = name_space
                        self.listname.value_namespace_prefix = name_space_prefix
                    if(value_path == "method"):
                        self.method.append(value)
                    if(value_path == "server-group-name"):
                        self.server_group_name.append(value)

            def has_data(self):
                for c in self.authorization:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.authorization:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "authorizations" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:aaa-subscriber/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "authorization"):
                    for c in self.authorization:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Aaa.AaaSubscriber.Authorizations.Authorization()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.authorization.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "authorization"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class Authentications(Entity):
            """
            AAA authentication
            
            .. attribute:: authentication
            
            	Configurations related to authentication
            	**type**\: list of    :py:class:`Authentication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.AaaSubscriber.Authentications.Authentication>`
            
            

            """

            _prefix = 'aaa-aaacore-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.AaaSubscriber.Authentications, self).__init__()

                self.yang_name = "authentications"
                self.yang_parent_name = "aaa-subscriber"

                self.authentication = YList(self)

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
                            super(Aaa.AaaSubscriber.Authentications, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Aaa.AaaSubscriber.Authentications, self).__setattr__(name, value)


            class Authentication(Entity):
                """
                Configurations related to authentication
                
                .. attribute:: type  <key>
                
                	Set authentication lists
                	**type**\:  str
                
                	**pattern:** (subscriber)\|(service)\|(policy\-if)\|(prepaid)\|(dot1x)
                
                .. attribute:: listname  <key>
                
                	Named authentication list
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: method
                
                	Method Types
                	**type**\:  list of   :py:class:`AaaMethod <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes.AaaMethod>`
                
                .. attribute:: server_group_name
                
                	Server group names
                	**type**\:  list of str
                
                

                """

                _prefix = 'aaa-aaacore-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.AaaSubscriber.Authentications.Authentication, self).__init__()

                    self.yang_name = "authentication"
                    self.yang_parent_name = "authentications"

                    self.type = YLeaf(YType.str, "type")

                    self.listname = YLeaf(YType.str, "listname")

                    self.method = YLeafList(YType.enumeration, "method")

                    self.server_group_name = YLeafList(YType.str, "server-group-name")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("type",
                                    "listname",
                                    "method",
                                    "server_group_name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Aaa.AaaSubscriber.Authentications.Authentication, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Aaa.AaaSubscriber.Authentications.Authentication, self).__setattr__(name, value)

                def has_data(self):
                    for leaf in self.method.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.server_group_name.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    return (
                        self.type.is_set or
                        self.listname.is_set)

                def has_operation(self):
                    for leaf in self.method.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.server_group_name.getYLeafs():
                        if (leaf.is_set):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.type.yfilter != YFilter.not_set or
                        self.listname.yfilter != YFilter.not_set or
                        self.method.yfilter != YFilter.not_set or
                        self.server_group_name.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "authentication" + "[type='" + self.type.get() + "']" + "[listname='" + self.listname.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:aaa-subscriber/authentications/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.type.get_name_leafdata())
                    if (self.listname.is_set or self.listname.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.listname.get_name_leafdata())

                    leaf_name_data.extend(self.method.get_name_leafdata())

                    leaf_name_data.extend(self.server_group_name.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "type" or name == "listname" or name == "method" or name == "server-group-name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "type"):
                        self.type = value
                        self.type.value_namespace = name_space
                        self.type.value_namespace_prefix = name_space_prefix
                    if(value_path == "listname"):
                        self.listname = value
                        self.listname.value_namespace = name_space
                        self.listname.value_namespace_prefix = name_space_prefix
                    if(value_path == "method"):
                        self.method.append(value)
                    if(value_path == "server-group-name"):
                        self.server_group_name.append(value)

            def has_data(self):
                for c in self.authentication:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.authentication:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "authentications" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:aaa-subscriber/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "authentication"):
                    for c in self.authentication:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Aaa.AaaSubscriber.Authentications.Authentication()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.authentication.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "authentication"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                (self.accountings is not None and self.accountings.has_data()) or
                (self.authentications is not None and self.authentications.has_data()) or
                (self.authorizations is not None and self.authorizations.has_data()) or
                (self.policy_if_authors is not None and self.policy_if_authors.has_data()) or
                (self.prepaid_authors is not None and self.prepaid_authors.has_data()) or
                (self.service_accounting is not None and self.service_accounting.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.accountings is not None and self.accountings.has_operation()) or
                (self.authentications is not None and self.authentications.has_operation()) or
                (self.authorizations is not None and self.authorizations.has_operation()) or
                (self.policy_if_authors is not None and self.policy_if_authors.has_operation()) or
                (self.prepaid_authors is not None and self.prepaid_authors.has_operation()) or
                (self.service_accounting is not None and self.service_accounting.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "Cisco-IOS-XR-aaa-aaacore-cfg:aaa-subscriber" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "accountings"):
                if (self.accountings is None):
                    self.accountings = Aaa.AaaSubscriber.Accountings()
                    self.accountings.parent = self
                    self._children_name_map["accountings"] = "accountings"
                return self.accountings

            if (child_yang_name == "authentications"):
                if (self.authentications is None):
                    self.authentications = Aaa.AaaSubscriber.Authentications()
                    self.authentications.parent = self
                    self._children_name_map["authentications"] = "authentications"
                return self.authentications

            if (child_yang_name == "authorizations"):
                if (self.authorizations is None):
                    self.authorizations = Aaa.AaaSubscriber.Authorizations()
                    self.authorizations.parent = self
                    self._children_name_map["authorizations"] = "authorizations"
                return self.authorizations

            if (child_yang_name == "policy-if-authors"):
                if (self.policy_if_authors is None):
                    self.policy_if_authors = Aaa.AaaSubscriber.PolicyIfAuthors()
                    self.policy_if_authors.parent = self
                    self._children_name_map["policy_if_authors"] = "policy-if-authors"
                return self.policy_if_authors

            if (child_yang_name == "prepaid-authors"):
                if (self.prepaid_authors is None):
                    self.prepaid_authors = Aaa.AaaSubscriber.PrepaidAuthors()
                    self.prepaid_authors.parent = self
                    self._children_name_map["prepaid_authors"] = "prepaid-authors"
                return self.prepaid_authors

            if (child_yang_name == "service-accounting"):
                if (self.service_accounting is None):
                    self.service_accounting = Aaa.AaaSubscriber.ServiceAccounting()
                    self.service_accounting.parent = self
                    self._children_name_map["service_accounting"] = "service-accounting"
                return self.service_accounting

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "accountings" or name == "authentications" or name == "authorizations" or name == "policy-if-authors" or name == "prepaid-authors" or name == "service-accounting"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class AaaMobile(Entity):
        """
        AAA Mobile
        
        .. attribute:: mobiles
        
        	AAA Mobile Accounting
        	**type**\:   :py:class:`Mobiles <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.AaaMobile.Mobiles>`
        
        

        """

        _prefix = 'aaa-aaacore-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Aaa.AaaMobile, self).__init__()

            self.yang_name = "aaa-mobile"
            self.yang_parent_name = "aaa"

            self.mobiles = Aaa.AaaMobile.Mobiles()
            self.mobiles.parent = self
            self._children_name_map["mobiles"] = "mobiles"
            self._children_yang_names.add("mobiles")


        class Mobiles(Entity):
            """
            AAA Mobile Accounting
            
            .. attribute:: mobile
            
            	Configurations related to accounting
            	**type**\: list of    :py:class:`Mobile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.AaaMobile.Mobiles.Mobile>`
            
            

            """

            _prefix = 'aaa-aaacore-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.AaaMobile.Mobiles, self).__init__()

                self.yang_name = "mobiles"
                self.yang_parent_name = "aaa-mobile"

                self.mobile = YList(self)

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
                            super(Aaa.AaaMobile.Mobiles, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Aaa.AaaMobile.Mobiles, self).__setattr__(name, value)


            class Mobile(Entity):
                """
                Configurations related to accounting
                
                .. attribute:: listname  <key>
                
                	Named accounting list
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: broadcast
                
                	Broadcast
                	**type**\:   :py:class:`AaaAccountingBroadcast <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes.AaaAccountingBroadcast>`
                
                	**mandatory**\: True
                
                .. attribute:: method
                
                	Method Types
                	**type**\:  list of   :py:class:`AaaMethod <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes.AaaMethod>`
                
                .. attribute:: server_group_name
                
                	Server group names
                	**type**\:  list of str
                
                

                """

                _prefix = 'aaa-aaacore-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.AaaMobile.Mobiles.Mobile, self).__init__()

                    self.yang_name = "mobile"
                    self.yang_parent_name = "mobiles"

                    self.listname = YLeaf(YType.str, "listname")

                    self.broadcast = YLeaf(YType.enumeration, "broadcast")

                    self.method = YLeafList(YType.enumeration, "method")

                    self.server_group_name = YLeafList(YType.str, "server-group-name")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("listname",
                                    "broadcast",
                                    "method",
                                    "server_group_name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Aaa.AaaMobile.Mobiles.Mobile, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Aaa.AaaMobile.Mobiles.Mobile, self).__setattr__(name, value)

                def has_data(self):
                    for leaf in self.method.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.server_group_name.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    return (
                        self.listname.is_set or
                        self.broadcast.is_set)

                def has_operation(self):
                    for leaf in self.method.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.server_group_name.getYLeafs():
                        if (leaf.is_set):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.listname.yfilter != YFilter.not_set or
                        self.broadcast.yfilter != YFilter.not_set or
                        self.method.yfilter != YFilter.not_set or
                        self.server_group_name.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "mobile" + "[listname='" + self.listname.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:aaa-mobile/mobiles/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.listname.is_set or self.listname.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.listname.get_name_leafdata())
                    if (self.broadcast.is_set or self.broadcast.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.broadcast.get_name_leafdata())

                    leaf_name_data.extend(self.method.get_name_leafdata())

                    leaf_name_data.extend(self.server_group_name.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "listname" or name == "broadcast" or name == "method" or name == "server-group-name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "listname"):
                        self.listname = value
                        self.listname.value_namespace = name_space
                        self.listname.value_namespace_prefix = name_space_prefix
                    if(value_path == "broadcast"):
                        self.broadcast = value
                        self.broadcast.value_namespace = name_space
                        self.broadcast.value_namespace_prefix = name_space_prefix
                    if(value_path == "method"):
                        self.method.append(value)
                    if(value_path == "server-group-name"):
                        self.server_group_name.append(value)

            def has_data(self):
                for c in self.mobile:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.mobile:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "mobiles" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:aaa-mobile/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "mobile"):
                    for c in self.mobile:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Aaa.AaaMobile.Mobiles.Mobile()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.mobile.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "mobile"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (self.mobiles is not None and self.mobiles.has_data())

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.mobiles is not None and self.mobiles.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "Cisco-IOS-XR-aaa-aaacore-cfg:aaa-mobile" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "mobiles"):
                if (self.mobiles is None):
                    self.mobiles = Aaa.AaaMobile.Mobiles()
                    self.mobiles.parent = self
                    self._children_name_map["mobiles"] = "mobiles"
                return self.mobiles

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "mobiles"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class AaaDot1X(Entity):
        """
        AAA Dot1x
        
        .. attribute:: authentications
        
        	AAA authentication
        	**type**\:   :py:class:`Authentications <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.AaaDot1X.Authentications>`
        
        

        """

        _prefix = 'aaa-aaacore-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Aaa.AaaDot1X, self).__init__()

            self.yang_name = "aaa-dot1x"
            self.yang_parent_name = "aaa"

            self.authentications = Aaa.AaaDot1X.Authentications()
            self.authentications.parent = self
            self._children_name_map["authentications"] = "authentications"
            self._children_yang_names.add("authentications")


        class Authentications(Entity):
            """
            AAA authentication
            
            .. attribute:: authentication
            
            	Configurations related to authentication
            	**type**\: list of    :py:class:`Authentication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.AaaDot1X.Authentications.Authentication>`
            
            

            """

            _prefix = 'aaa-aaacore-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.AaaDot1X.Authentications, self).__init__()

                self.yang_name = "authentications"
                self.yang_parent_name = "aaa-dot1x"

                self.authentication = YList(self)

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
                            super(Aaa.AaaDot1X.Authentications, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Aaa.AaaDot1X.Authentications, self).__setattr__(name, value)


            class Authentication(Entity):
                """
                Configurations related to authentication
                
                .. attribute:: type  <key>
                
                	Set authentication lists
                	**type**\:  str
                
                	**pattern:** (subscriber)\|(service)\|(policy\-if)\|(prepaid)\|(dot1x)
                
                .. attribute:: listname  <key>
                
                	Named authentication list
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: method
                
                	Method Types
                	**type**\:  list of   :py:class:`AaaMethod <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes.AaaMethod>`
                
                .. attribute:: server_group_name
                
                	Server group names
                	**type**\:  list of str
                
                

                """

                _prefix = 'aaa-aaacore-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.AaaDot1X.Authentications.Authentication, self).__init__()

                    self.yang_name = "authentication"
                    self.yang_parent_name = "authentications"

                    self.type = YLeaf(YType.str, "type")

                    self.listname = YLeaf(YType.str, "listname")

                    self.method = YLeafList(YType.enumeration, "method")

                    self.server_group_name = YLeafList(YType.str, "server-group-name")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("type",
                                    "listname",
                                    "method",
                                    "server_group_name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Aaa.AaaDot1X.Authentications.Authentication, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Aaa.AaaDot1X.Authentications.Authentication, self).__setattr__(name, value)

                def has_data(self):
                    for leaf in self.method.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.server_group_name.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    return (
                        self.type.is_set or
                        self.listname.is_set)

                def has_operation(self):
                    for leaf in self.method.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.server_group_name.getYLeafs():
                        if (leaf.is_set):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.type.yfilter != YFilter.not_set or
                        self.listname.yfilter != YFilter.not_set or
                        self.method.yfilter != YFilter.not_set or
                        self.server_group_name.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "authentication" + "[type='" + self.type.get() + "']" + "[listname='" + self.listname.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:aaa-dot1x/authentications/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.type.get_name_leafdata())
                    if (self.listname.is_set or self.listname.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.listname.get_name_leafdata())

                    leaf_name_data.extend(self.method.get_name_leafdata())

                    leaf_name_data.extend(self.server_group_name.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "type" or name == "listname" or name == "method" or name == "server-group-name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "type"):
                        self.type = value
                        self.type.value_namespace = name_space
                        self.type.value_namespace_prefix = name_space_prefix
                    if(value_path == "listname"):
                        self.listname = value
                        self.listname.value_namespace = name_space
                        self.listname.value_namespace_prefix = name_space_prefix
                    if(value_path == "method"):
                        self.method.append(value)
                    if(value_path == "server-group-name"):
                        self.server_group_name.append(value)

            def has_data(self):
                for c in self.authentication:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.authentication:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "authentications" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:aaa-dot1x/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "authentication"):
                    for c in self.authentication:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Aaa.AaaDot1X.Authentications.Authentication()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.authentication.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "authentication"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (self.authentications is not None and self.authentications.has_data())

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.authentications is not None and self.authentications.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "Cisco-IOS-XR-aaa-aaacore-cfg:aaa-dot1x" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "authentications"):
                if (self.authentications is None):
                    self.authentications = Aaa.AaaDot1X.Authentications()
                    self.authentications.parent = self
                    self._children_name_map["authentications"] = "authentications"
                return self.authentications

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "authentications"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class RadiusAttribute(Entity):
        """
        AAA RADIUS attribute configurations
        
        .. attribute:: called_station
        
        	AAA called station id attribute
        	**type**\:   :py:class:`CalledStation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.RadiusAttribute.CalledStation>`
        
        .. attribute:: calling_station
        
        	AAA calling station id attribute
        	**type**\:   :py:class:`CallingStation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.RadiusAttribute.CallingStation>`
        
        .. attribute:: format_others
        
        	AAA nas\-port\-id attribute format
        	**type**\:   :py:class:`FormatOthers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.RadiusAttribute.FormatOthers>`
        
        .. attribute:: nas_port
        
        	AAA nas\-port\-id attribute
        	**type**\:   :py:class:`NasPort <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.RadiusAttribute.NasPort>`
        
        .. attribute:: nas_port_id
        
        	AAA nas\-port\-id attribute
        	**type**\:   :py:class:`NasPortId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.RadiusAttribute.NasPortId>`
        
        

        """

        _prefix = 'aaa-aaacore-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Aaa.RadiusAttribute, self).__init__()

            self.yang_name = "radius-attribute"
            self.yang_parent_name = "aaa"

            self.called_station = Aaa.RadiusAttribute.CalledStation()
            self.called_station.parent = self
            self._children_name_map["called_station"] = "called-station"
            self._children_yang_names.add("called-station")

            self.calling_station = Aaa.RadiusAttribute.CallingStation()
            self.calling_station.parent = self
            self._children_name_map["calling_station"] = "calling-station"
            self._children_yang_names.add("calling-station")

            self.format_others = Aaa.RadiusAttribute.FormatOthers()
            self.format_others.parent = self
            self._children_name_map["format_others"] = "format-others"
            self._children_yang_names.add("format-others")

            self.nas_port = Aaa.RadiusAttribute.NasPort()
            self.nas_port.parent = self
            self._children_name_map["nas_port"] = "nas-port"
            self._children_yang_names.add("nas-port")

            self.nas_port_id = Aaa.RadiusAttribute.NasPortId()
            self.nas_port_id.parent = self
            self._children_name_map["nas_port_id"] = "nas-port-id"
            self._children_yang_names.add("nas-port-id")


        class NasPortId(Entity):
            """
            AAA nas\-port\-id attribute
            
            .. attribute:: formats
            
            	AAA nas\-port\-id attribute format
            	**type**\:   :py:class:`Formats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.RadiusAttribute.NasPortId.Formats>`
            
            

            """

            _prefix = 'aaa-aaacore-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.RadiusAttribute.NasPortId, self).__init__()

                self.yang_name = "nas-port-id"
                self.yang_parent_name = "radius-attribute"

                self.formats = Aaa.RadiusAttribute.NasPortId.Formats()
                self.formats.parent = self
                self._children_name_map["formats"] = "formats"
                self._children_yang_names.add("formats")


            class Formats(Entity):
                """
                AAA nas\-port\-id attribute format
                
                .. attribute:: format
                
                	nas\-port\-id attribute format
                	**type**\: list of    :py:class:`Format <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.RadiusAttribute.NasPortId.Formats.Format>`
                
                

                """

                _prefix = 'aaa-aaacore-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.RadiusAttribute.NasPortId.Formats, self).__init__()

                    self.yang_name = "formats"
                    self.yang_parent_name = "nas-port-id"

                    self.format = YList(self)

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
                                super(Aaa.RadiusAttribute.NasPortId.Formats, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Aaa.RadiusAttribute.NasPortId.Formats, self).__setattr__(name, value)


                class Format(Entity):
                    """
                    nas\-port\-id attribute format
                    
                    .. attribute:: type  <key>
                    
                    	Nas\-Port\-Type value to apply format name on
                    	**type**\:  int
                    
                    	**range:** 0..45
                    
                    .. attribute:: format_name
                    
                    	AAA nas\-port attribute format
                    	**type**\:  str
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'aaa-aaacore-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Aaa.RadiusAttribute.NasPortId.Formats.Format, self).__init__()

                        self.yang_name = "format"
                        self.yang_parent_name = "formats"

                        self.type = YLeaf(YType.uint32, "type")

                        self.format_name = YLeaf(YType.str, "format-name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("type",
                                        "format_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Aaa.RadiusAttribute.NasPortId.Formats.Format, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Aaa.RadiusAttribute.NasPortId.Formats.Format, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.type.is_set or
                            self.format_name.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.type.yfilter != YFilter.not_set or
                            self.format_name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "format" + "[type='" + self.type.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:radius-attribute/nas-port-id/formats/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.type.get_name_leafdata())
                        if (self.format_name.is_set or self.format_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.format_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "type" or name == "format-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "type"):
                            self.type = value
                            self.type.value_namespace = name_space
                            self.type.value_namespace_prefix = name_space_prefix
                        if(value_path == "format-name"):
                            self.format_name = value
                            self.format_name.value_namespace = name_space
                            self.format_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.format:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.format:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "formats" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:radius-attribute/nas-port-id/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "format"):
                        for c in self.format:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Aaa.RadiusAttribute.NasPortId.Formats.Format()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.format.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "format"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (self.formats is not None and self.formats.has_data())

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.formats is not None and self.formats.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "nas-port-id" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:radius-attribute/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "formats"):
                    if (self.formats is None):
                        self.formats = Aaa.RadiusAttribute.NasPortId.Formats()
                        self.formats.parent = self
                        self._children_name_map["formats"] = "formats"
                    return self.formats

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "formats"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class CallingStation(Entity):
            """
            AAA calling station id attribute
            
            .. attribute:: formats
            
            	AAA nas\-port\-id attribute format
            	**type**\:   :py:class:`Formats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.RadiusAttribute.CallingStation.Formats>`
            
            

            """

            _prefix = 'aaa-aaacore-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.RadiusAttribute.CallingStation, self).__init__()

                self.yang_name = "calling-station"
                self.yang_parent_name = "radius-attribute"

                self.formats = Aaa.RadiusAttribute.CallingStation.Formats()
                self.formats.parent = self
                self._children_name_map["formats"] = "formats"
                self._children_yang_names.add("formats")


            class Formats(Entity):
                """
                AAA nas\-port\-id attribute format
                
                .. attribute:: format
                
                	nas\-port\-id attribute format
                	**type**\: list of    :py:class:`Format <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.RadiusAttribute.CallingStation.Formats.Format>`
                
                

                """

                _prefix = 'aaa-aaacore-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.RadiusAttribute.CallingStation.Formats, self).__init__()

                    self.yang_name = "formats"
                    self.yang_parent_name = "calling-station"

                    self.format = YList(self)

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
                                super(Aaa.RadiusAttribute.CallingStation.Formats, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Aaa.RadiusAttribute.CallingStation.Formats, self).__setattr__(name, value)


                class Format(Entity):
                    """
                    nas\-port\-id attribute format
                    
                    .. attribute:: type  <key>
                    
                    	Nas\-Port\-Type value to apply format name on
                    	**type**\:  int
                    
                    	**range:** 0..45
                    
                    .. attribute:: format_name
                    
                    	AAA nas\-port attribute format
                    	**type**\:  str
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'aaa-aaacore-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Aaa.RadiusAttribute.CallingStation.Formats.Format, self).__init__()

                        self.yang_name = "format"
                        self.yang_parent_name = "formats"

                        self.type = YLeaf(YType.uint32, "type")

                        self.format_name = YLeaf(YType.str, "format-name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("type",
                                        "format_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Aaa.RadiusAttribute.CallingStation.Formats.Format, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Aaa.RadiusAttribute.CallingStation.Formats.Format, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.type.is_set or
                            self.format_name.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.type.yfilter != YFilter.not_set or
                            self.format_name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "format" + "[type='" + self.type.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:radius-attribute/calling-station/formats/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.type.get_name_leafdata())
                        if (self.format_name.is_set or self.format_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.format_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "type" or name == "format-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "type"):
                            self.type = value
                            self.type.value_namespace = name_space
                            self.type.value_namespace_prefix = name_space_prefix
                        if(value_path == "format-name"):
                            self.format_name = value
                            self.format_name.value_namespace = name_space
                            self.format_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.format:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.format:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "formats" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:radius-attribute/calling-station/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "format"):
                        for c in self.format:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Aaa.RadiusAttribute.CallingStation.Formats.Format()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.format.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "format"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (self.formats is not None and self.formats.has_data())

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.formats is not None and self.formats.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "calling-station" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:radius-attribute/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "formats"):
                    if (self.formats is None):
                        self.formats = Aaa.RadiusAttribute.CallingStation.Formats()
                        self.formats.parent = self
                        self._children_name_map["formats"] = "formats"
                    return self.formats

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "formats"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class CalledStation(Entity):
            """
            AAA called station id attribute
            
            .. attribute:: formats
            
            	AAA nas\-port\-id attribute format
            	**type**\:   :py:class:`Formats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.RadiusAttribute.CalledStation.Formats>`
            
            

            """

            _prefix = 'aaa-aaacore-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.RadiusAttribute.CalledStation, self).__init__()

                self.yang_name = "called-station"
                self.yang_parent_name = "radius-attribute"

                self.formats = Aaa.RadiusAttribute.CalledStation.Formats()
                self.formats.parent = self
                self._children_name_map["formats"] = "formats"
                self._children_yang_names.add("formats")


            class Formats(Entity):
                """
                AAA nas\-port\-id attribute format
                
                .. attribute:: format
                
                	nas\-port\-id attribute format
                	**type**\: list of    :py:class:`Format <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.RadiusAttribute.CalledStation.Formats.Format>`
                
                

                """

                _prefix = 'aaa-aaacore-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.RadiusAttribute.CalledStation.Formats, self).__init__()

                    self.yang_name = "formats"
                    self.yang_parent_name = "called-station"

                    self.format = YList(self)

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
                                super(Aaa.RadiusAttribute.CalledStation.Formats, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Aaa.RadiusAttribute.CalledStation.Formats, self).__setattr__(name, value)


                class Format(Entity):
                    """
                    nas\-port\-id attribute format
                    
                    .. attribute:: type  <key>
                    
                    	Nas\-Port\-Type value to apply format name on
                    	**type**\:  int
                    
                    	**range:** 0..45
                    
                    .. attribute:: format_name
                    
                    	AAA nas\-port attribute format
                    	**type**\:  str
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'aaa-aaacore-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Aaa.RadiusAttribute.CalledStation.Formats.Format, self).__init__()

                        self.yang_name = "format"
                        self.yang_parent_name = "formats"

                        self.type = YLeaf(YType.uint32, "type")

                        self.format_name = YLeaf(YType.str, "format-name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("type",
                                        "format_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Aaa.RadiusAttribute.CalledStation.Formats.Format, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Aaa.RadiusAttribute.CalledStation.Formats.Format, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.type.is_set or
                            self.format_name.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.type.yfilter != YFilter.not_set or
                            self.format_name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "format" + "[type='" + self.type.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:radius-attribute/called-station/formats/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.type.get_name_leafdata())
                        if (self.format_name.is_set or self.format_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.format_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "type" or name == "format-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "type"):
                            self.type = value
                            self.type.value_namespace = name_space
                            self.type.value_namespace_prefix = name_space_prefix
                        if(value_path == "format-name"):
                            self.format_name = value
                            self.format_name.value_namespace = name_space
                            self.format_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.format:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.format:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "formats" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:radius-attribute/called-station/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "format"):
                        for c in self.format:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Aaa.RadiusAttribute.CalledStation.Formats.Format()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.format.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "format"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (self.formats is not None and self.formats.has_data())

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.formats is not None and self.formats.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "called-station" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:radius-attribute/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "formats"):
                    if (self.formats is None):
                        self.formats = Aaa.RadiusAttribute.CalledStation.Formats()
                        self.formats.parent = self
                        self._children_name_map["formats"] = "formats"
                    return self.formats

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "formats"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class NasPort(Entity):
            """
            AAA nas\-port\-id attribute
            
            .. attribute:: format_extendeds
            
            	AAA nas\-port\-id attribute format
            	**type**\:   :py:class:`FormatExtendeds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.RadiusAttribute.NasPort.FormatExtendeds>`
            
            

            """

            _prefix = 'aaa-aaacore-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.RadiusAttribute.NasPort, self).__init__()

                self.yang_name = "nas-port"
                self.yang_parent_name = "radius-attribute"

                self.format_extendeds = Aaa.RadiusAttribute.NasPort.FormatExtendeds()
                self.format_extendeds.parent = self
                self._children_name_map["format_extendeds"] = "format-extendeds"
                self._children_yang_names.add("format-extendeds")


            class FormatExtendeds(Entity):
                """
                AAA nas\-port\-id attribute format
                
                .. attribute:: format_extended
                
                	nas\-port\-id extended attribute
                	**type**\: list of    :py:class:`FormatExtended <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.RadiusAttribute.NasPort.FormatExtendeds.FormatExtended>`
                
                

                """

                _prefix = 'aaa-aaacore-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.RadiusAttribute.NasPort.FormatExtendeds, self).__init__()

                    self.yang_name = "format-extendeds"
                    self.yang_parent_name = "nas-port"

                    self.format_extended = YList(self)

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
                                super(Aaa.RadiusAttribute.NasPort.FormatExtendeds, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Aaa.RadiusAttribute.NasPort.FormatExtendeds, self).__setattr__(name, value)


                class FormatExtended(Entity):
                    """
                    nas\-port\-id extended attribute
                    
                    .. attribute:: value  <key>
                    
                    	format type
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: type  <key>
                    
                    	AAA nas\-port attribute format
                    	**type**\:  int
                    
                    	**range:** 0..45
                    
                    .. attribute:: format_identifier
                    
                    	A 32 character string representing the format to be used
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    

                    """

                    _prefix = 'aaa-aaacore-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Aaa.RadiusAttribute.NasPort.FormatExtendeds.FormatExtended, self).__init__()

                        self.yang_name = "format-extended"
                        self.yang_parent_name = "format-extendeds"

                        self.value = YLeaf(YType.str, "value")

                        self.type = YLeaf(YType.uint32, "type")

                        self.format_identifier = YLeaf(YType.str, "format-identifier")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("value",
                                        "type",
                                        "format_identifier") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Aaa.RadiusAttribute.NasPort.FormatExtendeds.FormatExtended, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Aaa.RadiusAttribute.NasPort.FormatExtendeds.FormatExtended, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.value.is_set or
                            self.type.is_set or
                            self.format_identifier.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.value.yfilter != YFilter.not_set or
                            self.type.yfilter != YFilter.not_set or
                            self.format_identifier.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "format-extended" + "[value='" + self.value.get() + "']" + "[type='" + self.type.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:radius-attribute/nas-port/format-extendeds/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.value.is_set or self.value.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.value.get_name_leafdata())
                        if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.type.get_name_leafdata())
                        if (self.format_identifier.is_set or self.format_identifier.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.format_identifier.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "value" or name == "type" or name == "format-identifier"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "value"):
                            self.value = value
                            self.value.value_namespace = name_space
                            self.value.value_namespace_prefix = name_space_prefix
                        if(value_path == "type"):
                            self.type = value
                            self.type.value_namespace = name_space
                            self.type.value_namespace_prefix = name_space_prefix
                        if(value_path == "format-identifier"):
                            self.format_identifier = value
                            self.format_identifier.value_namespace = name_space
                            self.format_identifier.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.format_extended:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.format_extended:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "format-extendeds" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:radius-attribute/nas-port/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "format-extended"):
                        for c in self.format_extended:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Aaa.RadiusAttribute.NasPort.FormatExtendeds.FormatExtended()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.format_extended.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "format-extended"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (self.format_extendeds is not None and self.format_extendeds.has_data())

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.format_extendeds is not None and self.format_extendeds.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "nas-port" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:radius-attribute/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "format-extendeds"):
                    if (self.format_extendeds is None):
                        self.format_extendeds = Aaa.RadiusAttribute.NasPort.FormatExtendeds()
                        self.format_extendeds.parent = self
                        self._children_name_map["format_extendeds"] = "format-extendeds"
                    return self.format_extendeds

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "format-extendeds"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class FormatOthers(Entity):
            """
            AAA nas\-port\-id attribute format
            
            .. attribute:: format_other
            
            	Other configs
            	**type**\: list of    :py:class:`FormatOther <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.RadiusAttribute.FormatOthers.FormatOther>`
            
            

            """

            _prefix = 'aaa-aaacore-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.RadiusAttribute.FormatOthers, self).__init__()

                self.yang_name = "format-others"
                self.yang_parent_name = "radius-attribute"

                self.format_other = YList(self)

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
                            super(Aaa.RadiusAttribute.FormatOthers, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Aaa.RadiusAttribute.FormatOthers, self).__setattr__(name, value)


            class FormatOther(Entity):
                """
                Other configs
                
                .. attribute:: nas_port_type_name  <key>
                
                	Nas\-Port\-Type value to apply format name on
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: attribute_config1
                
                	Argument1
                	**type**\:  str
                
                .. attribute:: attribute_config10
                
                	Argument10
                	**type**\:  str
                
                .. attribute:: attribute_config11
                
                	Argument11
                	**type**\:  str
                
                .. attribute:: attribute_config12
                
                	Argument12
                	**type**\:  str
                
                .. attribute:: attribute_config13
                
                	Argument13
                	**type**\:  str
                
                .. attribute:: attribute_config14
                
                	Argument14
                	**type**\:  str
                
                .. attribute:: attribute_config15
                
                	Argument15
                	**type**\:  str
                
                .. attribute:: attribute_config16
                
                	Argument16
                	**type**\:  str
                
                .. attribute:: attribute_config17
                
                	Argument17
                	**type**\:  str
                
                .. attribute:: attribute_config18
                
                	Argument18
                	**type**\:  str
                
                .. attribute:: attribute_config19
                
                	Argument19
                	**type**\:  int
                
                	**range:** 1..253
                
                .. attribute:: attribute_config2
                
                	Argument2
                	**type**\:  str
                
                .. attribute:: attribute_config3
                
                	Argument3
                	**type**\:  str
                
                .. attribute:: attribute_config4
                
                	Argument4
                	**type**\:  str
                
                .. attribute:: attribute_config5
                
                	Argument5
                	**type**\:  str
                
                .. attribute:: attribute_config6
                
                	Argument6
                	**type**\:  str
                
                .. attribute:: attribute_config7
                
                	Argument7
                	**type**\:  str
                
                .. attribute:: attribute_config8
                
                	Argument8
                	**type**\:  str
                
                .. attribute:: attribute_config9
                
                	Argument9
                	**type**\:  str
                
                

                """

                _prefix = 'aaa-aaacore-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.RadiusAttribute.FormatOthers.FormatOther, self).__init__()

                    self.yang_name = "format-other"
                    self.yang_parent_name = "format-others"

                    self.nas_port_type_name = YLeaf(YType.str, "nas-port-type-name")

                    self.attribute_config1 = YLeaf(YType.str, "attribute-config1")

                    self.attribute_config10 = YLeaf(YType.str, "attribute-config10")

                    self.attribute_config11 = YLeaf(YType.str, "attribute-config11")

                    self.attribute_config12 = YLeaf(YType.str, "attribute-config12")

                    self.attribute_config13 = YLeaf(YType.str, "attribute-config13")

                    self.attribute_config14 = YLeaf(YType.str, "attribute-config14")

                    self.attribute_config15 = YLeaf(YType.str, "attribute-config15")

                    self.attribute_config16 = YLeaf(YType.str, "attribute-config16")

                    self.attribute_config17 = YLeaf(YType.str, "attribute-config17")

                    self.attribute_config18 = YLeaf(YType.str, "attribute-config18")

                    self.attribute_config19 = YLeaf(YType.uint32, "attribute-config19")

                    self.attribute_config2 = YLeaf(YType.str, "attribute-config2")

                    self.attribute_config3 = YLeaf(YType.str, "attribute-config3")

                    self.attribute_config4 = YLeaf(YType.str, "attribute-config4")

                    self.attribute_config5 = YLeaf(YType.str, "attribute-config5")

                    self.attribute_config6 = YLeaf(YType.str, "attribute-config6")

                    self.attribute_config7 = YLeaf(YType.str, "attribute-config7")

                    self.attribute_config8 = YLeaf(YType.str, "attribute-config8")

                    self.attribute_config9 = YLeaf(YType.str, "attribute-config9")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("nas_port_type_name",
                                    "attribute_config1",
                                    "attribute_config10",
                                    "attribute_config11",
                                    "attribute_config12",
                                    "attribute_config13",
                                    "attribute_config14",
                                    "attribute_config15",
                                    "attribute_config16",
                                    "attribute_config17",
                                    "attribute_config18",
                                    "attribute_config19",
                                    "attribute_config2",
                                    "attribute_config3",
                                    "attribute_config4",
                                    "attribute_config5",
                                    "attribute_config6",
                                    "attribute_config7",
                                    "attribute_config8",
                                    "attribute_config9") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Aaa.RadiusAttribute.FormatOthers.FormatOther, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Aaa.RadiusAttribute.FormatOthers.FormatOther, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.nas_port_type_name.is_set or
                        self.attribute_config1.is_set or
                        self.attribute_config10.is_set or
                        self.attribute_config11.is_set or
                        self.attribute_config12.is_set or
                        self.attribute_config13.is_set or
                        self.attribute_config14.is_set or
                        self.attribute_config15.is_set or
                        self.attribute_config16.is_set or
                        self.attribute_config17.is_set or
                        self.attribute_config18.is_set or
                        self.attribute_config19.is_set or
                        self.attribute_config2.is_set or
                        self.attribute_config3.is_set or
                        self.attribute_config4.is_set or
                        self.attribute_config5.is_set or
                        self.attribute_config6.is_set or
                        self.attribute_config7.is_set or
                        self.attribute_config8.is_set or
                        self.attribute_config9.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.nas_port_type_name.yfilter != YFilter.not_set or
                        self.attribute_config1.yfilter != YFilter.not_set or
                        self.attribute_config10.yfilter != YFilter.not_set or
                        self.attribute_config11.yfilter != YFilter.not_set or
                        self.attribute_config12.yfilter != YFilter.not_set or
                        self.attribute_config13.yfilter != YFilter.not_set or
                        self.attribute_config14.yfilter != YFilter.not_set or
                        self.attribute_config15.yfilter != YFilter.not_set or
                        self.attribute_config16.yfilter != YFilter.not_set or
                        self.attribute_config17.yfilter != YFilter.not_set or
                        self.attribute_config18.yfilter != YFilter.not_set or
                        self.attribute_config19.yfilter != YFilter.not_set or
                        self.attribute_config2.yfilter != YFilter.not_set or
                        self.attribute_config3.yfilter != YFilter.not_set or
                        self.attribute_config4.yfilter != YFilter.not_set or
                        self.attribute_config5.yfilter != YFilter.not_set or
                        self.attribute_config6.yfilter != YFilter.not_set or
                        self.attribute_config7.yfilter != YFilter.not_set or
                        self.attribute_config8.yfilter != YFilter.not_set or
                        self.attribute_config9.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "format-other" + "[nas-port-type-name='" + self.nas_port_type_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:radius-attribute/format-others/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.nas_port_type_name.is_set or self.nas_port_type_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.nas_port_type_name.get_name_leafdata())
                    if (self.attribute_config1.is_set or self.attribute_config1.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.attribute_config1.get_name_leafdata())
                    if (self.attribute_config10.is_set or self.attribute_config10.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.attribute_config10.get_name_leafdata())
                    if (self.attribute_config11.is_set or self.attribute_config11.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.attribute_config11.get_name_leafdata())
                    if (self.attribute_config12.is_set or self.attribute_config12.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.attribute_config12.get_name_leafdata())
                    if (self.attribute_config13.is_set or self.attribute_config13.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.attribute_config13.get_name_leafdata())
                    if (self.attribute_config14.is_set or self.attribute_config14.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.attribute_config14.get_name_leafdata())
                    if (self.attribute_config15.is_set or self.attribute_config15.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.attribute_config15.get_name_leafdata())
                    if (self.attribute_config16.is_set or self.attribute_config16.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.attribute_config16.get_name_leafdata())
                    if (self.attribute_config17.is_set or self.attribute_config17.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.attribute_config17.get_name_leafdata())
                    if (self.attribute_config18.is_set or self.attribute_config18.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.attribute_config18.get_name_leafdata())
                    if (self.attribute_config19.is_set or self.attribute_config19.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.attribute_config19.get_name_leafdata())
                    if (self.attribute_config2.is_set or self.attribute_config2.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.attribute_config2.get_name_leafdata())
                    if (self.attribute_config3.is_set or self.attribute_config3.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.attribute_config3.get_name_leafdata())
                    if (self.attribute_config4.is_set or self.attribute_config4.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.attribute_config4.get_name_leafdata())
                    if (self.attribute_config5.is_set or self.attribute_config5.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.attribute_config5.get_name_leafdata())
                    if (self.attribute_config6.is_set or self.attribute_config6.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.attribute_config6.get_name_leafdata())
                    if (self.attribute_config7.is_set or self.attribute_config7.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.attribute_config7.get_name_leafdata())
                    if (self.attribute_config8.is_set or self.attribute_config8.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.attribute_config8.get_name_leafdata())
                    if (self.attribute_config9.is_set or self.attribute_config9.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.attribute_config9.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "nas-port-type-name" or name == "attribute-config1" or name == "attribute-config10" or name == "attribute-config11" or name == "attribute-config12" or name == "attribute-config13" or name == "attribute-config14" or name == "attribute-config15" or name == "attribute-config16" or name == "attribute-config17" or name == "attribute-config18" or name == "attribute-config19" or name == "attribute-config2" or name == "attribute-config3" or name == "attribute-config4" or name == "attribute-config5" or name == "attribute-config6" or name == "attribute-config7" or name == "attribute-config8" or name == "attribute-config9"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "nas-port-type-name"):
                        self.nas_port_type_name = value
                        self.nas_port_type_name.value_namespace = name_space
                        self.nas_port_type_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "attribute-config1"):
                        self.attribute_config1 = value
                        self.attribute_config1.value_namespace = name_space
                        self.attribute_config1.value_namespace_prefix = name_space_prefix
                    if(value_path == "attribute-config10"):
                        self.attribute_config10 = value
                        self.attribute_config10.value_namespace = name_space
                        self.attribute_config10.value_namespace_prefix = name_space_prefix
                    if(value_path == "attribute-config11"):
                        self.attribute_config11 = value
                        self.attribute_config11.value_namespace = name_space
                        self.attribute_config11.value_namespace_prefix = name_space_prefix
                    if(value_path == "attribute-config12"):
                        self.attribute_config12 = value
                        self.attribute_config12.value_namespace = name_space
                        self.attribute_config12.value_namespace_prefix = name_space_prefix
                    if(value_path == "attribute-config13"):
                        self.attribute_config13 = value
                        self.attribute_config13.value_namespace = name_space
                        self.attribute_config13.value_namespace_prefix = name_space_prefix
                    if(value_path == "attribute-config14"):
                        self.attribute_config14 = value
                        self.attribute_config14.value_namespace = name_space
                        self.attribute_config14.value_namespace_prefix = name_space_prefix
                    if(value_path == "attribute-config15"):
                        self.attribute_config15 = value
                        self.attribute_config15.value_namespace = name_space
                        self.attribute_config15.value_namespace_prefix = name_space_prefix
                    if(value_path == "attribute-config16"):
                        self.attribute_config16 = value
                        self.attribute_config16.value_namespace = name_space
                        self.attribute_config16.value_namespace_prefix = name_space_prefix
                    if(value_path == "attribute-config17"):
                        self.attribute_config17 = value
                        self.attribute_config17.value_namespace = name_space
                        self.attribute_config17.value_namespace_prefix = name_space_prefix
                    if(value_path == "attribute-config18"):
                        self.attribute_config18 = value
                        self.attribute_config18.value_namespace = name_space
                        self.attribute_config18.value_namespace_prefix = name_space_prefix
                    if(value_path == "attribute-config19"):
                        self.attribute_config19 = value
                        self.attribute_config19.value_namespace = name_space
                        self.attribute_config19.value_namespace_prefix = name_space_prefix
                    if(value_path == "attribute-config2"):
                        self.attribute_config2 = value
                        self.attribute_config2.value_namespace = name_space
                        self.attribute_config2.value_namespace_prefix = name_space_prefix
                    if(value_path == "attribute-config3"):
                        self.attribute_config3 = value
                        self.attribute_config3.value_namespace = name_space
                        self.attribute_config3.value_namespace_prefix = name_space_prefix
                    if(value_path == "attribute-config4"):
                        self.attribute_config4 = value
                        self.attribute_config4.value_namespace = name_space
                        self.attribute_config4.value_namespace_prefix = name_space_prefix
                    if(value_path == "attribute-config5"):
                        self.attribute_config5 = value
                        self.attribute_config5.value_namespace = name_space
                        self.attribute_config5.value_namespace_prefix = name_space_prefix
                    if(value_path == "attribute-config6"):
                        self.attribute_config6 = value
                        self.attribute_config6.value_namespace = name_space
                        self.attribute_config6.value_namespace_prefix = name_space_prefix
                    if(value_path == "attribute-config7"):
                        self.attribute_config7 = value
                        self.attribute_config7.value_namespace = name_space
                        self.attribute_config7.value_namespace_prefix = name_space_prefix
                    if(value_path == "attribute-config8"):
                        self.attribute_config8 = value
                        self.attribute_config8.value_namespace = name_space
                        self.attribute_config8.value_namespace_prefix = name_space_prefix
                    if(value_path == "attribute-config9"):
                        self.attribute_config9 = value
                        self.attribute_config9.value_namespace = name_space
                        self.attribute_config9.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.format_other:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.format_other:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "format-others" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:radius-attribute/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "format-other"):
                    for c in self.format_other:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Aaa.RadiusAttribute.FormatOthers.FormatOther()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.format_other.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "format-other"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                (self.called_station is not None and self.called_station.has_data()) or
                (self.calling_station is not None and self.calling_station.has_data()) or
                (self.format_others is not None and self.format_others.has_data()) or
                (self.nas_port is not None and self.nas_port.has_data()) or
                (self.nas_port_id is not None and self.nas_port_id.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.called_station is not None and self.called_station.has_operation()) or
                (self.calling_station is not None and self.calling_station.has_operation()) or
                (self.format_others is not None and self.format_others.has_operation()) or
                (self.nas_port is not None and self.nas_port.has_operation()) or
                (self.nas_port_id is not None and self.nas_port_id.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "Cisco-IOS-XR-aaa-aaacore-cfg:radius-attribute" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "called-station"):
                if (self.called_station is None):
                    self.called_station = Aaa.RadiusAttribute.CalledStation()
                    self.called_station.parent = self
                    self._children_name_map["called_station"] = "called-station"
                return self.called_station

            if (child_yang_name == "calling-station"):
                if (self.calling_station is None):
                    self.calling_station = Aaa.RadiusAttribute.CallingStation()
                    self.calling_station.parent = self
                    self._children_name_map["calling_station"] = "calling-station"
                return self.calling_station

            if (child_yang_name == "format-others"):
                if (self.format_others is None):
                    self.format_others = Aaa.RadiusAttribute.FormatOthers()
                    self.format_others.parent = self
                    self._children_name_map["format_others"] = "format-others"
                return self.format_others

            if (child_yang_name == "nas-port"):
                if (self.nas_port is None):
                    self.nas_port = Aaa.RadiusAttribute.NasPort()
                    self.nas_port.parent = self
                    self._children_name_map["nas_port"] = "nas-port"
                return self.nas_port

            if (child_yang_name == "nas-port-id"):
                if (self.nas_port_id is None):
                    self.nas_port_id = Aaa.RadiusAttribute.NasPortId()
                    self.nas_port_id.parent = self
                    self._children_name_map["nas_port_id"] = "nas-port-id"
                return self.nas_port_id

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "called-station" or name == "calling-station" or name == "format-others" or name == "nas-port" or name == "nas-port-id"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class ServerGroups(Entity):
        """
        AAA group definitions
        
        .. attribute:: diameter_server_groups
        
        	DIAMETER server group definition
        	**type**\:   :py:class:`DiameterServerGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.DiameterServerGroups>`
        
        .. attribute:: radius_server_groups
        
        	RADIUS server group definition
        	**type**\:   :py:class:`RadiusServerGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.RadiusServerGroups>`
        
        .. attribute:: tacacs_server_groups
        
        	TACACS+ server\-group definition
        	**type**\:   :py:class:`TacacsServerGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.TacacsServerGroups>`
        
        

        """

        _prefix = 'aaa-locald-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Aaa.ServerGroups, self).__init__()

            self.yang_name = "server-groups"
            self.yang_parent_name = "aaa"

            self.diameter_server_groups = Aaa.ServerGroups.DiameterServerGroups()
            self.diameter_server_groups.parent = self
            self._children_name_map["diameter_server_groups"] = "diameter-server-groups"
            self._children_yang_names.add("diameter-server-groups")

            self.radius_server_groups = Aaa.ServerGroups.RadiusServerGroups()
            self.radius_server_groups.parent = self
            self._children_name_map["radius_server_groups"] = "radius-server-groups"
            self._children_yang_names.add("radius-server-groups")

            self.tacacs_server_groups = Aaa.ServerGroups.TacacsServerGroups()
            self.tacacs_server_groups.parent = self
            self._children_name_map["tacacs_server_groups"] = "tacacs-server-groups"
            self._children_yang_names.add("tacacs-server-groups")


        class DiameterServerGroups(Entity):
            """
            DIAMETER server group definition
            
            .. attribute:: diameter_server_group
            
            	DIAMETER server group name
            	**type**\: list of    :py:class:`DiameterServerGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.DiameterServerGroups.DiameterServerGroup>`
            
            

            """

            _prefix = 'aaa-diameter-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.ServerGroups.DiameterServerGroups, self).__init__()

                self.yang_name = "diameter-server-groups"
                self.yang_parent_name = "server-groups"

                self.diameter_server_group = YList(self)

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
                            super(Aaa.ServerGroups.DiameterServerGroups, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Aaa.ServerGroups.DiameterServerGroups, self).__setattr__(name, value)


            class DiameterServerGroup(Entity):
                """
                DIAMETER server group name
                
                .. attribute:: server_group_name  <key>
                
                	DIAMETER server group name
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: servers
                
                	List of DIAMETER servers present in the group
                	**type**\:   :py:class:`Servers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.DiameterServerGroups.DiameterServerGroup.Servers>`
                
                

                """

                _prefix = 'aaa-diameter-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.ServerGroups.DiameterServerGroups.DiameterServerGroup, self).__init__()

                    self.yang_name = "diameter-server-group"
                    self.yang_parent_name = "diameter-server-groups"

                    self.server_group_name = YLeaf(YType.str, "server-group-name")

                    self.servers = Aaa.ServerGroups.DiameterServerGroups.DiameterServerGroup.Servers()
                    self.servers.parent = self
                    self._children_name_map["servers"] = "servers"
                    self._children_yang_names.add("servers")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("server_group_name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Aaa.ServerGroups.DiameterServerGroups.DiameterServerGroup, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Aaa.ServerGroups.DiameterServerGroups.DiameterServerGroup, self).__setattr__(name, value)


                class Servers(Entity):
                    """
                    List of DIAMETER servers present in the group
                    
                    .. attribute:: server
                    
                    	A server to include in the server group
                    	**type**\: list of    :py:class:`Server <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.DiameterServerGroups.DiameterServerGroup.Servers.Server>`
                    
                    

                    """

                    _prefix = 'aaa-diameter-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Aaa.ServerGroups.DiameterServerGroups.DiameterServerGroup.Servers, self).__init__()

                        self.yang_name = "servers"
                        self.yang_parent_name = "diameter-server-group"

                        self.server = YList(self)

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
                                    super(Aaa.ServerGroups.DiameterServerGroups.DiameterServerGroup.Servers, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Aaa.ServerGroups.DiameterServerGroups.DiameterServerGroup.Servers, self).__setattr__(name, value)


                    class Server(Entity):
                        """
                        A server to include in the server group
                        
                        .. attribute:: ordering_index  <key>
                        
                        	This is used to sort the servers in the order of precedence
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: peer_name  <key>
                        
                        	Name for the diameter peer configuration
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        

                        """

                        _prefix = 'aaa-diameter-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Aaa.ServerGroups.DiameterServerGroups.DiameterServerGroup.Servers.Server, self).__init__()

                            self.yang_name = "server"
                            self.yang_parent_name = "servers"

                            self.ordering_index = YLeaf(YType.int32, "ordering-index")

                            self.peer_name = YLeaf(YType.str, "peer-name")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("ordering_index",
                                            "peer_name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Aaa.ServerGroups.DiameterServerGroups.DiameterServerGroup.Servers.Server, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Aaa.ServerGroups.DiameterServerGroups.DiameterServerGroup.Servers.Server, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.ordering_index.is_set or
                                self.peer_name.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.ordering_index.yfilter != YFilter.not_set or
                                self.peer_name.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "server" + "[ordering-index='" + self.ordering_index.get() + "']" + "[peer-name='" + self.peer_name.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.ordering_index.is_set or self.ordering_index.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ordering_index.get_name_leafdata())
                            if (self.peer_name.is_set or self.peer_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.peer_name.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "ordering-index" or name == "peer-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "ordering-index"):
                                self.ordering_index = value
                                self.ordering_index.value_namespace = name_space
                                self.ordering_index.value_namespace_prefix = name_space_prefix
                            if(value_path == "peer-name"):
                                self.peer_name = value
                                self.peer_name.value_namespace = name_space
                                self.peer_name.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.server:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.server:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "servers" + path_buffer

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

                        if (child_yang_name == "server"):
                            for c in self.server:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Aaa.ServerGroups.DiameterServerGroups.DiameterServerGroup.Servers.Server()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.server.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "server"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        self.server_group_name.is_set or
                        (self.servers is not None and self.servers.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.server_group_name.yfilter != YFilter.not_set or
                        (self.servers is not None and self.servers.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "diameter-server-group" + "[server-group-name='" + self.server_group_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-locald-cfg:server-groups/Cisco-IOS-XR-aaa-diameter-cfg:diameter-server-groups/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.server_group_name.is_set or self.server_group_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.server_group_name.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "servers"):
                        if (self.servers is None):
                            self.servers = Aaa.ServerGroups.DiameterServerGroups.DiameterServerGroup.Servers()
                            self.servers.parent = self
                            self._children_name_map["servers"] = "servers"
                        return self.servers

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "servers" or name == "server-group-name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "server-group-name"):
                        self.server_group_name = value
                        self.server_group_name.value_namespace = name_space
                        self.server_group_name.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.diameter_server_group:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.diameter_server_group:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "Cisco-IOS-XR-aaa-diameter-cfg:diameter-server-groups" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-locald-cfg:server-groups/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "diameter-server-group"):
                    for c in self.diameter_server_group:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Aaa.ServerGroups.DiameterServerGroups.DiameterServerGroup()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.diameter_server_group.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "diameter-server-group"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class RadiusServerGroups(Entity):
            """
            RADIUS server group definition
            
            .. attribute:: radius_server_group
            
            	RADIUS server group name
            	**type**\: list of    :py:class:`RadiusServerGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup>`
            
            

            """

            _prefix = 'aaa-protocol-radius-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.ServerGroups.RadiusServerGroups, self).__init__()

                self.yang_name = "radius-server-groups"
                self.yang_parent_name = "server-groups"

                self.radius_server_group = YList(self)

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
                            super(Aaa.ServerGroups.RadiusServerGroups, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Aaa.ServerGroups.RadiusServerGroups, self).__setattr__(name, value)


            class RadiusServerGroup(Entity):
                """
                RADIUS server group name
                
                .. attribute:: server_group_name  <key>
                
                	RADIUS server group name
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: accounting
                
                	List of filters in server group
                	**type**\:   :py:class:`Accounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Accounting>`
                
                .. attribute:: authorization
                
                	List of filters in server group
                	**type**\:   :py:class:`Authorization <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Authorization>`
                
                .. attribute:: dead_time
                
                	This indicates the length of time (in minutes) for which RADIUS servers present in this group remain marked as dead
                	**type**\:  int
                
                	**range:** 1..1440
                
                	**units**\: minute
                
                .. attribute:: load_balance
                
                	Radius load\-balancing options
                	**type**\:   :py:class:`LoadBalance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.LoadBalance>`
                
                .. attribute:: private_servers
                
                	List of private RADIUS servers present in the group
                	**type**\:   :py:class:`PrivateServers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.PrivateServers>`
                
                .. attribute:: server_group_throttle
                
                	Radius throttling options
                	**type**\:   :py:class:`ServerGroupThrottle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.ServerGroupThrottle>`
                
                .. attribute:: servers
                
                	List of RADIUS servers present in the group
                	**type**\:   :py:class:`Servers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Servers>`
                
                .. attribute:: source_interface
                
                	Specify interface for source address in RADIUS packets
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: vrf
                
                	Specify VRF name of RADIUS group
                	**type**\:  str
                
                

                """

                _prefix = 'aaa-protocol-radius-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup, self).__init__()

                    self.yang_name = "radius-server-group"
                    self.yang_parent_name = "radius-server-groups"

                    self.server_group_name = YLeaf(YType.str, "server-group-name")

                    self.dead_time = YLeaf(YType.uint32, "dead-time")

                    self.source_interface = YLeaf(YType.str, "source-interface")

                    self.vrf = YLeaf(YType.str, "vrf")

                    self.accounting = Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Accounting()
                    self.accounting.parent = self
                    self._children_name_map["accounting"] = "accounting"
                    self._children_yang_names.add("accounting")

                    self.authorization = Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Authorization()
                    self.authorization.parent = self
                    self._children_name_map["authorization"] = "authorization"
                    self._children_yang_names.add("authorization")

                    self.load_balance = Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.LoadBalance()
                    self.load_balance.parent = self
                    self._children_name_map["load_balance"] = "load-balance"
                    self._children_yang_names.add("load-balance")

                    self.private_servers = Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.PrivateServers()
                    self.private_servers.parent = self
                    self._children_name_map["private_servers"] = "private-servers"
                    self._children_yang_names.add("private-servers")

                    self.server_group_throttle = Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.ServerGroupThrottle()
                    self.server_group_throttle.parent = self
                    self._children_name_map["server_group_throttle"] = "server-group-throttle"
                    self._children_yang_names.add("server-group-throttle")

                    self.servers = Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Servers()
                    self.servers.parent = self
                    self._children_name_map["servers"] = "servers"
                    self._children_yang_names.add("servers")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("server_group_name",
                                    "dead_time",
                                    "source_interface",
                                    "vrf") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup, self).__setattr__(name, value)


                class Accounting(Entity):
                    """
                    List of filters in server group
                    
                    .. attribute:: reply
                    
                    	Specify a filter in server group
                    	**type**\:   :py:class:`Reply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Accounting.Reply>`
                    
                    .. attribute:: request
                    
                    	Specify a filter in server group
                    	**type**\:   :py:class:`Request <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Accounting.Request>`
                    
                    

                    """

                    _prefix = 'aaa-protocol-radius-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Accounting, self).__init__()

                        self.yang_name = "accounting"
                        self.yang_parent_name = "radius-server-group"

                        self.reply = Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Accounting.Reply()
                        self.reply.parent = self
                        self._children_name_map["reply"] = "reply"
                        self._children_yang_names.add("reply")

                        self.request = Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Accounting.Request()
                        self.request.parent = self
                        self._children_name_map["request"] = "request"
                        self._children_yang_names.add("request")


                    class Request(Entity):
                        """
                        Specify a filter in server group
                        
                        .. attribute:: action
                        
                        	Specify the attribute list type accept or reject
                        	**type**\:   :py:class:`AaaAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg.AaaAction>`
                        
                        .. attribute:: attribute_list_name
                        
                        	Name of RADIUS attribute list
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'aaa-protocol-radius-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Accounting.Request, self).__init__()

                            self.yang_name = "request"
                            self.yang_parent_name = "accounting"

                            self.action = YLeaf(YType.enumeration, "action")

                            self.attribute_list_name = YLeaf(YType.str, "attribute-list-name")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("action",
                                            "attribute_list_name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Accounting.Request, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Accounting.Request, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.action.is_set or
                                self.attribute_list_name.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.action.yfilter != YFilter.not_set or
                                self.attribute_list_name.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "request" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.action.is_set or self.action.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.action.get_name_leafdata())
                            if (self.attribute_list_name.is_set or self.attribute_list_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.attribute_list_name.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "action" or name == "attribute-list-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "action"):
                                self.action = value
                                self.action.value_namespace = name_space
                                self.action.value_namespace_prefix = name_space_prefix
                            if(value_path == "attribute-list-name"):
                                self.attribute_list_name = value
                                self.attribute_list_name.value_namespace = name_space
                                self.attribute_list_name.value_namespace_prefix = name_space_prefix


                    class Reply(Entity):
                        """
                        Specify a filter in server group
                        
                        .. attribute:: action
                        
                        	Specify the attribute list type accept or reject
                        	**type**\:   :py:class:`AaaAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg.AaaAction>`
                        
                        .. attribute:: attribute_list_name
                        
                        	Name of RADIUS attribute list
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'aaa-protocol-radius-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Accounting.Reply, self).__init__()

                            self.yang_name = "reply"
                            self.yang_parent_name = "accounting"

                            self.action = YLeaf(YType.enumeration, "action")

                            self.attribute_list_name = YLeaf(YType.str, "attribute-list-name")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("action",
                                            "attribute_list_name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Accounting.Reply, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Accounting.Reply, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.action.is_set or
                                self.attribute_list_name.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.action.yfilter != YFilter.not_set or
                                self.attribute_list_name.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "reply" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.action.is_set or self.action.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.action.get_name_leafdata())
                            if (self.attribute_list_name.is_set or self.attribute_list_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.attribute_list_name.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "action" or name == "attribute-list-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "action"):
                                self.action = value
                                self.action.value_namespace = name_space
                                self.action.value_namespace_prefix = name_space_prefix
                            if(value_path == "attribute-list-name"):
                                self.attribute_list_name = value
                                self.attribute_list_name.value_namespace = name_space
                                self.attribute_list_name.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            (self.reply is not None and self.reply.has_data()) or
                            (self.request is not None and self.request.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.reply is not None and self.reply.has_operation()) or
                            (self.request is not None and self.request.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "accounting" + path_buffer

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

                        if (child_yang_name == "reply"):
                            if (self.reply is None):
                                self.reply = Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Accounting.Reply()
                                self.reply.parent = self
                                self._children_name_map["reply"] = "reply"
                            return self.reply

                        if (child_yang_name == "request"):
                            if (self.request is None):
                                self.request = Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Accounting.Request()
                                self.request.parent = self
                                self._children_name_map["request"] = "request"
                            return self.request

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "reply" or name == "request"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class Servers(Entity):
                    """
                    List of RADIUS servers present in the group
                    
                    .. attribute:: server
                    
                    	A server to include in the server group
                    	**type**\: list of    :py:class:`Server <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Servers.Server>`
                    
                    

                    """

                    _prefix = 'aaa-protocol-radius-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Servers, self).__init__()

                        self.yang_name = "servers"
                        self.yang_parent_name = "radius-server-group"

                        self.server = YList(self)

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
                                    super(Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Servers, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Servers, self).__setattr__(name, value)


                    class Server(Entity):
                        """
                        A server to include in the server group
                        
                        .. attribute:: ordering_index  <key>
                        
                        	This is used to sort the servers in the order of precedence
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: ip_address  <key>
                        
                        	IP address of RADIUS server
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: auth_port_number  <key>
                        
                        	Authentication Port number (standard port 1645)
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: acct_port_number  <key>
                        
                        	Accounting Port number (standard port 1646)
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        

                        """

                        _prefix = 'aaa-protocol-radius-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Servers.Server, self).__init__()

                            self.yang_name = "server"
                            self.yang_parent_name = "servers"

                            self.ordering_index = YLeaf(YType.int32, "ordering-index")

                            self.ip_address = YLeaf(YType.str, "ip-address")

                            self.auth_port_number = YLeaf(YType.uint16, "auth-port-number")

                            self.acct_port_number = YLeaf(YType.uint16, "acct-port-number")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("ordering_index",
                                            "ip_address",
                                            "auth_port_number",
                                            "acct_port_number") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Servers.Server, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Servers.Server, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.ordering_index.is_set or
                                self.ip_address.is_set or
                                self.auth_port_number.is_set or
                                self.acct_port_number.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.ordering_index.yfilter != YFilter.not_set or
                                self.ip_address.yfilter != YFilter.not_set or
                                self.auth_port_number.yfilter != YFilter.not_set or
                                self.acct_port_number.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "server" + "[ordering-index='" + self.ordering_index.get() + "']" + "[ip-address='" + self.ip_address.get() + "']" + "[auth-port-number='" + self.auth_port_number.get() + "']" + "[acct-port-number='" + self.acct_port_number.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.ordering_index.is_set or self.ordering_index.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ordering_index.get_name_leafdata())
                            if (self.ip_address.is_set or self.ip_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ip_address.get_name_leafdata())
                            if (self.auth_port_number.is_set or self.auth_port_number.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.auth_port_number.get_name_leafdata())
                            if (self.acct_port_number.is_set or self.acct_port_number.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.acct_port_number.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "ordering-index" or name == "ip-address" or name == "auth-port-number" or name == "acct-port-number"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "ordering-index"):
                                self.ordering_index = value
                                self.ordering_index.value_namespace = name_space
                                self.ordering_index.value_namespace_prefix = name_space_prefix
                            if(value_path == "ip-address"):
                                self.ip_address = value
                                self.ip_address.value_namespace = name_space
                                self.ip_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "auth-port-number"):
                                self.auth_port_number = value
                                self.auth_port_number.value_namespace = name_space
                                self.auth_port_number.value_namespace_prefix = name_space_prefix
                            if(value_path == "acct-port-number"):
                                self.acct_port_number = value
                                self.acct_port_number.value_namespace = name_space
                                self.acct_port_number.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.server:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.server:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "servers" + path_buffer

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

                        if (child_yang_name == "server"):
                            for c in self.server:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Servers.Server()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.server.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "server"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class PrivateServers(Entity):
                    """
                    List of private RADIUS servers present in the
                    group
                    
                    .. attribute:: private_server
                    
                    	A private server to include in the server group
                    	**type**\: list of    :py:class:`PrivateServer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.PrivateServers.PrivateServer>`
                    
                    

                    """

                    _prefix = 'aaa-protocol-radius-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.PrivateServers, self).__init__()

                        self.yang_name = "private-servers"
                        self.yang_parent_name = "radius-server-group"

                        self.private_server = YList(self)

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
                                    super(Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.PrivateServers, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.PrivateServers, self).__setattr__(name, value)


                    class PrivateServer(Entity):
                        """
                        A private server to include in the server
                        group
                        
                        .. attribute:: ordering_index  <key>
                        
                        	This is used to sort the servers in the order of precedence
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: ip_address  <key>
                        
                        	IP address of RADIUS server
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: auth_port_number  <key>
                        
                        	Authentication Port number (standard port 1645)
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: acct_port_number  <key>
                        
                        	Accounting Port number (standard port 1646)
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: idle_time
                        
                        	Idle time for the radius Server
                        	**type**\:  int
                        
                        	**range:** 1..60
                        
                        	**default value**\: 5
                        
                        .. attribute:: ignore_accounting_port
                        
                        	Ignore Accounting port
                        	**type**\:  bool
                        
                        .. attribute:: ignore_auth_port
                        
                        	Ignore authentication Port
                        	**type**\:  bool
                        
                        .. attribute:: private_key
                        
                        	RADIUS encryption key
                        	**type**\:  str
                        
                        	**pattern:** (!.+)\|([^!].+)
                        
                        .. attribute:: private_retransmit
                        
                        	Number of times to retransmit a request to the RADIUS server
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        	**default value**\: 3
                        
                        .. attribute:: private_timeout
                        
                        	Time to wait for a RADIUS server to reply
                        	**type**\:  int
                        
                        	**range:** 1..1000
                        
                        	**default value**\: 5
                        
                        .. attribute:: username
                        
                        	Username to be tested for automated testing
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'aaa-protocol-radius-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.PrivateServers.PrivateServer, self).__init__()

                            self.yang_name = "private-server"
                            self.yang_parent_name = "private-servers"

                            self.ordering_index = YLeaf(YType.int32, "ordering-index")

                            self.ip_address = YLeaf(YType.str, "ip-address")

                            self.auth_port_number = YLeaf(YType.uint16, "auth-port-number")

                            self.acct_port_number = YLeaf(YType.uint16, "acct-port-number")

                            self.idle_time = YLeaf(YType.uint32, "idle-time")

                            self.ignore_accounting_port = YLeaf(YType.boolean, "ignore-accounting-port")

                            self.ignore_auth_port = YLeaf(YType.boolean, "ignore-auth-port")

                            self.private_key = YLeaf(YType.str, "private-key")

                            self.private_retransmit = YLeaf(YType.uint32, "private-retransmit")

                            self.private_timeout = YLeaf(YType.uint32, "private-timeout")

                            self.username = YLeaf(YType.str, "username")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("ordering_index",
                                            "ip_address",
                                            "auth_port_number",
                                            "acct_port_number",
                                            "idle_time",
                                            "ignore_accounting_port",
                                            "ignore_auth_port",
                                            "private_key",
                                            "private_retransmit",
                                            "private_timeout",
                                            "username") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.PrivateServers.PrivateServer, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.PrivateServers.PrivateServer, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.ordering_index.is_set or
                                self.ip_address.is_set or
                                self.auth_port_number.is_set or
                                self.acct_port_number.is_set or
                                self.idle_time.is_set or
                                self.ignore_accounting_port.is_set or
                                self.ignore_auth_port.is_set or
                                self.private_key.is_set or
                                self.private_retransmit.is_set or
                                self.private_timeout.is_set or
                                self.username.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.ordering_index.yfilter != YFilter.not_set or
                                self.ip_address.yfilter != YFilter.not_set or
                                self.auth_port_number.yfilter != YFilter.not_set or
                                self.acct_port_number.yfilter != YFilter.not_set or
                                self.idle_time.yfilter != YFilter.not_set or
                                self.ignore_accounting_port.yfilter != YFilter.not_set or
                                self.ignore_auth_port.yfilter != YFilter.not_set or
                                self.private_key.yfilter != YFilter.not_set or
                                self.private_retransmit.yfilter != YFilter.not_set or
                                self.private_timeout.yfilter != YFilter.not_set or
                                self.username.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "private-server" + "[ordering-index='" + self.ordering_index.get() + "']" + "[ip-address='" + self.ip_address.get() + "']" + "[auth-port-number='" + self.auth_port_number.get() + "']" + "[acct-port-number='" + self.acct_port_number.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.ordering_index.is_set or self.ordering_index.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ordering_index.get_name_leafdata())
                            if (self.ip_address.is_set or self.ip_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ip_address.get_name_leafdata())
                            if (self.auth_port_number.is_set or self.auth_port_number.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.auth_port_number.get_name_leafdata())
                            if (self.acct_port_number.is_set or self.acct_port_number.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.acct_port_number.get_name_leafdata())
                            if (self.idle_time.is_set or self.idle_time.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.idle_time.get_name_leafdata())
                            if (self.ignore_accounting_port.is_set or self.ignore_accounting_port.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ignore_accounting_port.get_name_leafdata())
                            if (self.ignore_auth_port.is_set or self.ignore_auth_port.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ignore_auth_port.get_name_leafdata())
                            if (self.private_key.is_set or self.private_key.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.private_key.get_name_leafdata())
                            if (self.private_retransmit.is_set or self.private_retransmit.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.private_retransmit.get_name_leafdata())
                            if (self.private_timeout.is_set or self.private_timeout.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.private_timeout.get_name_leafdata())
                            if (self.username.is_set or self.username.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.username.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "ordering-index" or name == "ip-address" or name == "auth-port-number" or name == "acct-port-number" or name == "idle-time" or name == "ignore-accounting-port" or name == "ignore-auth-port" or name == "private-key" or name == "private-retransmit" or name == "private-timeout" or name == "username"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "ordering-index"):
                                self.ordering_index = value
                                self.ordering_index.value_namespace = name_space
                                self.ordering_index.value_namespace_prefix = name_space_prefix
                            if(value_path == "ip-address"):
                                self.ip_address = value
                                self.ip_address.value_namespace = name_space
                                self.ip_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "auth-port-number"):
                                self.auth_port_number = value
                                self.auth_port_number.value_namespace = name_space
                                self.auth_port_number.value_namespace_prefix = name_space_prefix
                            if(value_path == "acct-port-number"):
                                self.acct_port_number = value
                                self.acct_port_number.value_namespace = name_space
                                self.acct_port_number.value_namespace_prefix = name_space_prefix
                            if(value_path == "idle-time"):
                                self.idle_time = value
                                self.idle_time.value_namespace = name_space
                                self.idle_time.value_namespace_prefix = name_space_prefix
                            if(value_path == "ignore-accounting-port"):
                                self.ignore_accounting_port = value
                                self.ignore_accounting_port.value_namespace = name_space
                                self.ignore_accounting_port.value_namespace_prefix = name_space_prefix
                            if(value_path == "ignore-auth-port"):
                                self.ignore_auth_port = value
                                self.ignore_auth_port.value_namespace = name_space
                                self.ignore_auth_port.value_namespace_prefix = name_space_prefix
                            if(value_path == "private-key"):
                                self.private_key = value
                                self.private_key.value_namespace = name_space
                                self.private_key.value_namespace_prefix = name_space_prefix
                            if(value_path == "private-retransmit"):
                                self.private_retransmit = value
                                self.private_retransmit.value_namespace = name_space
                                self.private_retransmit.value_namespace_prefix = name_space_prefix
                            if(value_path == "private-timeout"):
                                self.private_timeout = value
                                self.private_timeout.value_namespace = name_space
                                self.private_timeout.value_namespace_prefix = name_space_prefix
                            if(value_path == "username"):
                                self.username = value
                                self.username.value_namespace = name_space
                                self.username.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.private_server:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.private_server:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "private-servers" + path_buffer

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

                        if (child_yang_name == "private-server"):
                            for c in self.private_server:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.PrivateServers.PrivateServer()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.private_server.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "private-server"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class ServerGroupThrottle(Entity):
                    """
                    Radius throttling options
                    
                    .. attribute:: access
                    
                    	To flow control the number of access requests sent to a radius server
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    	**default value**\: 0
                    
                    .. attribute:: access_timeout
                    
                    	Specify the number of timeouts exceeding which a throttled access request is dropped
                    	**type**\:  int
                    
                    	**range:** 1..10
                    
                    	**default value**\: 3
                    
                    .. attribute:: accounting
                    
                    	To flow control the number of accounting requests sent to a radius server
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    	**default value**\: 0
                    
                    

                    """

                    _prefix = 'aaa-protocol-radius-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.ServerGroupThrottle, self).__init__()

                        self.yang_name = "server-group-throttle"
                        self.yang_parent_name = "radius-server-group"

                        self.access = YLeaf(YType.uint32, "access")

                        self.access_timeout = YLeaf(YType.uint32, "access-timeout")

                        self.accounting = YLeaf(YType.uint32, "accounting")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("access",
                                        "access_timeout",
                                        "accounting") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.ServerGroupThrottle, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.ServerGroupThrottle, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.access.is_set or
                            self.access_timeout.is_set or
                            self.accounting.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.access.yfilter != YFilter.not_set or
                            self.access_timeout.yfilter != YFilter.not_set or
                            self.accounting.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "server-group-throttle" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.access.is_set or self.access.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.access.get_name_leafdata())
                        if (self.access_timeout.is_set or self.access_timeout.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.access_timeout.get_name_leafdata())
                        if (self.accounting.is_set or self.accounting.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.accounting.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "access" or name == "access-timeout" or name == "accounting"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "access"):
                            self.access = value
                            self.access.value_namespace = name_space
                            self.access.value_namespace_prefix = name_space_prefix
                        if(value_path == "access-timeout"):
                            self.access_timeout = value
                            self.access_timeout.value_namespace = name_space
                            self.access_timeout.value_namespace_prefix = name_space_prefix
                        if(value_path == "accounting"):
                            self.accounting = value
                            self.accounting.value_namespace = name_space
                            self.accounting.value_namespace_prefix = name_space_prefix


                class LoadBalance(Entity):
                    """
                    Radius load\-balancing options
                    
                    .. attribute:: method
                    
                    	Method by which the next host will be picked
                    	**type**\:   :py:class:`Method <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.LoadBalance.Method>`
                    
                    

                    """

                    _prefix = 'aaa-protocol-radius-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.LoadBalance, self).__init__()

                        self.yang_name = "load-balance"
                        self.yang_parent_name = "radius-server-group"

                        self.method = Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.LoadBalance.Method()
                        self.method.parent = self
                        self._children_name_map["method"] = "method"
                        self._children_yang_names.add("method")


                    class Method(Entity):
                        """
                        Method by which the next host will be picked
                        
                        .. attribute:: name
                        
                        	Batch size for selection of the server
                        	**type**\:   :py:class:`Name <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.LoadBalance.Method.Name>`
                        
                        

                        """

                        _prefix = 'aaa-protocol-radius-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.LoadBalance.Method, self).__init__()

                            self.yang_name = "method"
                            self.yang_parent_name = "load-balance"

                            self.name = Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.LoadBalance.Method.Name()
                            self.name.parent = self
                            self._children_name_map["name"] = "name"
                            self._children_yang_names.add("name")


                        class Name(Entity):
                            """
                            Batch size for selection of the server
                            
                            .. attribute:: batch_size
                            
                            	Batch size for selection of the server
                            	**type**\:  int
                            
                            	**range:** 1..1500
                            
                            	**default value**\: 25
                            
                            .. attribute:: ignore_preferred_server
                            
                            	Disable preferred server for this Server Group
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**default value**\: 1
                            
                            .. attribute:: least_outstanding
                            
                            	Pick the server with the least transactions outstanding
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**default value**\: 4
                            
                            

                            """

                            _prefix = 'aaa-protocol-radius-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.LoadBalance.Method.Name, self).__init__()

                                self.yang_name = "name"
                                self.yang_parent_name = "method"

                                self.batch_size = YLeaf(YType.uint32, "batch-size")

                                self.ignore_preferred_server = YLeaf(YType.int32, "ignore-preferred-server")

                                self.least_outstanding = YLeaf(YType.int32, "least-outstanding")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("batch_size",
                                                "ignore_preferred_server",
                                                "least_outstanding") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.LoadBalance.Method.Name, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.LoadBalance.Method.Name, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.batch_size.is_set or
                                    self.ignore_preferred_server.is_set or
                                    self.least_outstanding.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.batch_size.yfilter != YFilter.not_set or
                                    self.ignore_preferred_server.yfilter != YFilter.not_set or
                                    self.least_outstanding.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "name" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.batch_size.is_set or self.batch_size.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.batch_size.get_name_leafdata())
                                if (self.ignore_preferred_server.is_set or self.ignore_preferred_server.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ignore_preferred_server.get_name_leafdata())
                                if (self.least_outstanding.is_set or self.least_outstanding.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.least_outstanding.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "batch-size" or name == "ignore-preferred-server" or name == "least-outstanding"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "batch-size"):
                                    self.batch_size = value
                                    self.batch_size.value_namespace = name_space
                                    self.batch_size.value_namespace_prefix = name_space_prefix
                                if(value_path == "ignore-preferred-server"):
                                    self.ignore_preferred_server = value
                                    self.ignore_preferred_server.value_namespace = name_space
                                    self.ignore_preferred_server.value_namespace_prefix = name_space_prefix
                                if(value_path == "least-outstanding"):
                                    self.least_outstanding = value
                                    self.least_outstanding.value_namespace = name_space
                                    self.least_outstanding.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (self.name is not None and self.name.has_data())

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                (self.name is not None and self.name.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "method" + path_buffer

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

                            if (child_yang_name == "name"):
                                if (self.name is None):
                                    self.name = Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.LoadBalance.Method.Name()
                                    self.name.parent = self
                                    self._children_name_map["name"] = "name"
                                return self.name

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (self.method is not None and self.method.has_data())

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.method is not None and self.method.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "load-balance" + path_buffer

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

                        if (child_yang_name == "method"):
                            if (self.method is None):
                                self.method = Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.LoadBalance.Method()
                                self.method.parent = self
                                self._children_name_map["method"] = "method"
                            return self.method

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "method"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class Authorization(Entity):
                    """
                    List of filters in server group
                    
                    .. attribute:: reply
                    
                    	Specify a filter in server group
                    	**type**\:   :py:class:`Reply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Authorization.Reply>`
                    
                    .. attribute:: request
                    
                    	Specify a filter in server group
                    	**type**\:   :py:class:`Request <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Authorization.Request>`
                    
                    

                    """

                    _prefix = 'aaa-protocol-radius-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Authorization, self).__init__()

                        self.yang_name = "authorization"
                        self.yang_parent_name = "radius-server-group"

                        self.reply = Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Authorization.Reply()
                        self.reply.parent = self
                        self._children_name_map["reply"] = "reply"
                        self._children_yang_names.add("reply")

                        self.request = Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Authorization.Request()
                        self.request.parent = self
                        self._children_name_map["request"] = "request"
                        self._children_yang_names.add("request")


                    class Request(Entity):
                        """
                        Specify a filter in server group
                        
                        .. attribute:: action
                        
                        	Specify the attribute list type accept or reject
                        	**type**\:   :py:class:`AaaAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg.AaaAction>`
                        
                        .. attribute:: attribute_list_name
                        
                        	Name of RADIUS attribute list
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'aaa-protocol-radius-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Authorization.Request, self).__init__()

                            self.yang_name = "request"
                            self.yang_parent_name = "authorization"

                            self.action = YLeaf(YType.enumeration, "action")

                            self.attribute_list_name = YLeaf(YType.str, "attribute-list-name")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("action",
                                            "attribute_list_name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Authorization.Request, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Authorization.Request, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.action.is_set or
                                self.attribute_list_name.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.action.yfilter != YFilter.not_set or
                                self.attribute_list_name.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "request" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.action.is_set or self.action.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.action.get_name_leafdata())
                            if (self.attribute_list_name.is_set or self.attribute_list_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.attribute_list_name.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "action" or name == "attribute-list-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "action"):
                                self.action = value
                                self.action.value_namespace = name_space
                                self.action.value_namespace_prefix = name_space_prefix
                            if(value_path == "attribute-list-name"):
                                self.attribute_list_name = value
                                self.attribute_list_name.value_namespace = name_space
                                self.attribute_list_name.value_namespace_prefix = name_space_prefix


                    class Reply(Entity):
                        """
                        Specify a filter in server group
                        
                        .. attribute:: action
                        
                        	Specify the attribute list type accept or reject
                        	**type**\:   :py:class:`AaaAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg.AaaAction>`
                        
                        .. attribute:: attribute_list_name
                        
                        	Name of RADIUS attribute list
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'aaa-protocol-radius-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Authorization.Reply, self).__init__()

                            self.yang_name = "reply"
                            self.yang_parent_name = "authorization"

                            self.action = YLeaf(YType.enumeration, "action")

                            self.attribute_list_name = YLeaf(YType.str, "attribute-list-name")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("action",
                                            "attribute_list_name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Authorization.Reply, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Authorization.Reply, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.action.is_set or
                                self.attribute_list_name.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.action.yfilter != YFilter.not_set or
                                self.attribute_list_name.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "reply" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.action.is_set or self.action.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.action.get_name_leafdata())
                            if (self.attribute_list_name.is_set or self.attribute_list_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.attribute_list_name.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "action" or name == "attribute-list-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "action"):
                                self.action = value
                                self.action.value_namespace = name_space
                                self.action.value_namespace_prefix = name_space_prefix
                            if(value_path == "attribute-list-name"):
                                self.attribute_list_name = value
                                self.attribute_list_name.value_namespace = name_space
                                self.attribute_list_name.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            (self.reply is not None and self.reply.has_data()) or
                            (self.request is not None and self.request.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.reply is not None and self.reply.has_operation()) or
                            (self.request is not None and self.request.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "authorization" + path_buffer

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

                        if (child_yang_name == "reply"):
                            if (self.reply is None):
                                self.reply = Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Authorization.Reply()
                                self.reply.parent = self
                                self._children_name_map["reply"] = "reply"
                            return self.reply

                        if (child_yang_name == "request"):
                            if (self.request is None):
                                self.request = Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Authorization.Request()
                                self.request.parent = self
                                self._children_name_map["request"] = "request"
                            return self.request

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "reply" or name == "request"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        self.server_group_name.is_set or
                        self.dead_time.is_set or
                        self.source_interface.is_set or
                        self.vrf.is_set or
                        (self.accounting is not None and self.accounting.has_data()) or
                        (self.authorization is not None and self.authorization.has_data()) or
                        (self.load_balance is not None and self.load_balance.has_data()) or
                        (self.private_servers is not None and self.private_servers.has_data()) or
                        (self.server_group_throttle is not None and self.server_group_throttle.has_data()) or
                        (self.servers is not None and self.servers.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.server_group_name.yfilter != YFilter.not_set or
                        self.dead_time.yfilter != YFilter.not_set or
                        self.source_interface.yfilter != YFilter.not_set or
                        self.vrf.yfilter != YFilter.not_set or
                        (self.accounting is not None and self.accounting.has_operation()) or
                        (self.authorization is not None and self.authorization.has_operation()) or
                        (self.load_balance is not None and self.load_balance.has_operation()) or
                        (self.private_servers is not None and self.private_servers.has_operation()) or
                        (self.server_group_throttle is not None and self.server_group_throttle.has_operation()) or
                        (self.servers is not None and self.servers.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "radius-server-group" + "[server-group-name='" + self.server_group_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-locald-cfg:server-groups/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius-server-groups/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.server_group_name.is_set or self.server_group_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.server_group_name.get_name_leafdata())
                    if (self.dead_time.is_set or self.dead_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.dead_time.get_name_leafdata())
                    if (self.source_interface.is_set or self.source_interface.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.source_interface.get_name_leafdata())
                    if (self.vrf.is_set or self.vrf.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.vrf.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "accounting"):
                        if (self.accounting is None):
                            self.accounting = Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Accounting()
                            self.accounting.parent = self
                            self._children_name_map["accounting"] = "accounting"
                        return self.accounting

                    if (child_yang_name == "authorization"):
                        if (self.authorization is None):
                            self.authorization = Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Authorization()
                            self.authorization.parent = self
                            self._children_name_map["authorization"] = "authorization"
                        return self.authorization

                    if (child_yang_name == "load-balance"):
                        if (self.load_balance is None):
                            self.load_balance = Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.LoadBalance()
                            self.load_balance.parent = self
                            self._children_name_map["load_balance"] = "load-balance"
                        return self.load_balance

                    if (child_yang_name == "private-servers"):
                        if (self.private_servers is None):
                            self.private_servers = Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.PrivateServers()
                            self.private_servers.parent = self
                            self._children_name_map["private_servers"] = "private-servers"
                        return self.private_servers

                    if (child_yang_name == "server-group-throttle"):
                        if (self.server_group_throttle is None):
                            self.server_group_throttle = Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.ServerGroupThrottle()
                            self.server_group_throttle.parent = self
                            self._children_name_map["server_group_throttle"] = "server-group-throttle"
                        return self.server_group_throttle

                    if (child_yang_name == "servers"):
                        if (self.servers is None):
                            self.servers = Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Servers()
                            self.servers.parent = self
                            self._children_name_map["servers"] = "servers"
                        return self.servers

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "accounting" or name == "authorization" or name == "load-balance" or name == "private-servers" or name == "server-group-throttle" or name == "servers" or name == "server-group-name" or name == "dead-time" or name == "source-interface" or name == "vrf"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "server-group-name"):
                        self.server_group_name = value
                        self.server_group_name.value_namespace = name_space
                        self.server_group_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "dead-time"):
                        self.dead_time = value
                        self.dead_time.value_namespace = name_space
                        self.dead_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "source-interface"):
                        self.source_interface = value
                        self.source_interface.value_namespace = name_space
                        self.source_interface.value_namespace_prefix = name_space_prefix
                    if(value_path == "vrf"):
                        self.vrf = value
                        self.vrf.value_namespace = name_space
                        self.vrf.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.radius_server_group:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.radius_server_group:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "Cisco-IOS-XR-aaa-protocol-radius-cfg:radius-server-groups" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-locald-cfg:server-groups/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "radius-server-group"):
                    for c in self.radius_server_group:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.radius_server_group.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "radius-server-group"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class TacacsServerGroups(Entity):
            """
            TACACS+ server\-group definition
            
            .. attribute:: tacacs_server_group
            
            	TACACS+ Server group name
            	**type**\: list of    :py:class:`TacacsServerGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup>`
            
            

            """

            _prefix = 'aaa-tacacs-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.ServerGroups.TacacsServerGroups, self).__init__()

                self.yang_name = "tacacs-server-groups"
                self.yang_parent_name = "server-groups"

                self.tacacs_server_group = YList(self)

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
                            super(Aaa.ServerGroups.TacacsServerGroups, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Aaa.ServerGroups.TacacsServerGroups, self).__setattr__(name, value)


            class TacacsServerGroup(Entity):
                """
                TACACS+ Server group name
                
                .. attribute:: server_group_name  <key>
                
                	TACACS+ Server group name
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: private_servers
                
                	List of private TACACS servers present in the group
                	**type**\:   :py:class:`PrivateServers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.PrivateServers>`
                
                .. attribute:: servers
                
                	Specify a TACACS+ server
                	**type**\:   :py:class:`Servers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.Servers>`
                
                .. attribute:: vrf
                
                	Specify VRF name of TACACS group
                	**type**\:  str
                
                

                """

                _prefix = 'aaa-tacacs-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup, self).__init__()

                    self.yang_name = "tacacs-server-group"
                    self.yang_parent_name = "tacacs-server-groups"

                    self.server_group_name = YLeaf(YType.str, "server-group-name")

                    self.vrf = YLeaf(YType.str, "vrf")

                    self.private_servers = Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.PrivateServers()
                    self.private_servers.parent = self
                    self._children_name_map["private_servers"] = "private-servers"
                    self._children_yang_names.add("private-servers")

                    self.servers = Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.Servers()
                    self.servers.parent = self
                    self._children_name_map["servers"] = "servers"
                    self._children_yang_names.add("servers")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("server_group_name",
                                    "vrf") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup, self).__setattr__(name, value)


                class Servers(Entity):
                    """
                    Specify a TACACS+ server
                    
                    .. attribute:: server
                    
                    	A server to include in the server group
                    	**type**\: list of    :py:class:`Server <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.Servers.Server>`
                    
                    

                    """

                    _prefix = 'aaa-tacacs-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.Servers, self).__init__()

                        self.yang_name = "servers"
                        self.yang_parent_name = "tacacs-server-group"

                        self.server = YList(self)

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
                                    super(Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.Servers, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.Servers, self).__setattr__(name, value)


                    class Server(Entity):
                        """
                        A server to include in the server group
                        
                        .. attribute:: ordering_index  <key>
                        
                        	This is used to sort the servers in the order of precedence
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: ip_address  <key>
                        
                        	IP address of TACACS+ server
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        

                        """

                        _prefix = 'aaa-tacacs-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.Servers.Server, self).__init__()

                            self.yang_name = "server"
                            self.yang_parent_name = "servers"

                            self.ordering_index = YLeaf(YType.int32, "ordering-index")

                            self.ip_address = YLeaf(YType.str, "ip-address")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("ordering_index",
                                            "ip_address") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.Servers.Server, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.Servers.Server, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.ordering_index.is_set or
                                self.ip_address.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.ordering_index.yfilter != YFilter.not_set or
                                self.ip_address.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "server" + "[ordering-index='" + self.ordering_index.get() + "']" + "[ip-address='" + self.ip_address.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.ordering_index.is_set or self.ordering_index.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ordering_index.get_name_leafdata())
                            if (self.ip_address.is_set or self.ip_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ip_address.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "ordering-index" or name == "ip-address"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "ordering-index"):
                                self.ordering_index = value
                                self.ordering_index.value_namespace = name_space
                                self.ordering_index.value_namespace_prefix = name_space_prefix
                            if(value_path == "ip-address"):
                                self.ip_address = value
                                self.ip_address.value_namespace = name_space
                                self.ip_address.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.server:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.server:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "servers" + path_buffer

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

                        if (child_yang_name == "server"):
                            for c in self.server:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.Servers.Server()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.server.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "server"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class PrivateServers(Entity):
                    """
                    List of private TACACS servers present in the
                    group
                    
                    .. attribute:: private_server
                    
                    	A private server to include in the server group
                    	**type**\: list of    :py:class:`PrivateServer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.PrivateServers.PrivateServer>`
                    
                    

                    """

                    _prefix = 'aaa-tacacs-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.PrivateServers, self).__init__()

                        self.yang_name = "private-servers"
                        self.yang_parent_name = "tacacs-server-group"

                        self.private_server = YList(self)

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
                                    super(Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.PrivateServers, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.PrivateServers, self).__setattr__(name, value)


                    class PrivateServer(Entity):
                        """
                        A private server to include in the server
                        group
                        
                        .. attribute:: ordering_index  <key>
                        
                        	This is used to sort the servers in the order of precedence
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: ip_address  <key>
                        
                        	IP address of TACACS+ server
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: port_number  <key>
                        
                        	Port number (standard 49)
                        	**type**\:  int
                        
                        	**range:** 1..65535
                        
                        .. attribute:: key
                        
                        	Set TACACS+ encryption key
                        	**type**\:  str
                        
                        	**pattern:** (!.+)\|([^!].+)
                        
                        .. attribute:: timeout
                        
                        	Time to wait for a TACACS+ server to reply
                        	**type**\:  int
                        
                        	**range:** 1..1000
                        
                        	**default value**\: 5
                        
                        

                        """

                        _prefix = 'aaa-tacacs-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.PrivateServers.PrivateServer, self).__init__()

                            self.yang_name = "private-server"
                            self.yang_parent_name = "private-servers"

                            self.ordering_index = YLeaf(YType.int32, "ordering-index")

                            self.ip_address = YLeaf(YType.str, "ip-address")

                            self.port_number = YLeaf(YType.uint32, "port-number")

                            self.key = YLeaf(YType.str, "key")

                            self.timeout = YLeaf(YType.uint32, "timeout")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("ordering_index",
                                            "ip_address",
                                            "port_number",
                                            "key",
                                            "timeout") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.PrivateServers.PrivateServer, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.PrivateServers.PrivateServer, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.ordering_index.is_set or
                                self.ip_address.is_set or
                                self.port_number.is_set or
                                self.key.is_set or
                                self.timeout.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.ordering_index.yfilter != YFilter.not_set or
                                self.ip_address.yfilter != YFilter.not_set or
                                self.port_number.yfilter != YFilter.not_set or
                                self.key.yfilter != YFilter.not_set or
                                self.timeout.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "private-server" + "[ordering-index='" + self.ordering_index.get() + "']" + "[ip-address='" + self.ip_address.get() + "']" + "[port-number='" + self.port_number.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.ordering_index.is_set or self.ordering_index.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ordering_index.get_name_leafdata())
                            if (self.ip_address.is_set or self.ip_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ip_address.get_name_leafdata())
                            if (self.port_number.is_set or self.port_number.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.port_number.get_name_leafdata())
                            if (self.key.is_set or self.key.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.key.get_name_leafdata())
                            if (self.timeout.is_set or self.timeout.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.timeout.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "ordering-index" or name == "ip-address" or name == "port-number" or name == "key" or name == "timeout"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "ordering-index"):
                                self.ordering_index = value
                                self.ordering_index.value_namespace = name_space
                                self.ordering_index.value_namespace_prefix = name_space_prefix
                            if(value_path == "ip-address"):
                                self.ip_address = value
                                self.ip_address.value_namespace = name_space
                                self.ip_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "port-number"):
                                self.port_number = value
                                self.port_number.value_namespace = name_space
                                self.port_number.value_namespace_prefix = name_space_prefix
                            if(value_path == "key"):
                                self.key = value
                                self.key.value_namespace = name_space
                                self.key.value_namespace_prefix = name_space_prefix
                            if(value_path == "timeout"):
                                self.timeout = value
                                self.timeout.value_namespace = name_space
                                self.timeout.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.private_server:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.private_server:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "private-servers" + path_buffer

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

                        if (child_yang_name == "private-server"):
                            for c in self.private_server:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.PrivateServers.PrivateServer()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.private_server.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "private-server"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        self.server_group_name.is_set or
                        self.vrf.is_set or
                        (self.private_servers is not None and self.private_servers.has_data()) or
                        (self.servers is not None and self.servers.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.server_group_name.yfilter != YFilter.not_set or
                        self.vrf.yfilter != YFilter.not_set or
                        (self.private_servers is not None and self.private_servers.has_operation()) or
                        (self.servers is not None and self.servers.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "tacacs-server-group" + "[server-group-name='" + self.server_group_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-locald-cfg:server-groups/Cisco-IOS-XR-aaa-tacacs-cfg:tacacs-server-groups/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.server_group_name.is_set or self.server_group_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.server_group_name.get_name_leafdata())
                    if (self.vrf.is_set or self.vrf.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.vrf.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "private-servers"):
                        if (self.private_servers is None):
                            self.private_servers = Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.PrivateServers()
                            self.private_servers.parent = self
                            self._children_name_map["private_servers"] = "private-servers"
                        return self.private_servers

                    if (child_yang_name == "servers"):
                        if (self.servers is None):
                            self.servers = Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.Servers()
                            self.servers.parent = self
                            self._children_name_map["servers"] = "servers"
                        return self.servers

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "private-servers" or name == "servers" or name == "server-group-name" or name == "vrf"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "server-group-name"):
                        self.server_group_name = value
                        self.server_group_name.value_namespace = name_space
                        self.server_group_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "vrf"):
                        self.vrf = value
                        self.vrf.value_namespace = name_space
                        self.vrf.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.tacacs_server_group:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.tacacs_server_group:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "Cisco-IOS-XR-aaa-tacacs-cfg:tacacs-server-groups" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-locald-cfg:server-groups/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "tacacs-server-group"):
                    for c in self.tacacs_server_group:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.tacacs_server_group.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "tacacs-server-group"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                (self.diameter_server_groups is not None and self.diameter_server_groups.has_data()) or
                (self.radius_server_groups is not None and self.radius_server_groups.has_data()) or
                (self.tacacs_server_groups is not None and self.tacacs_server_groups.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.diameter_server_groups is not None and self.diameter_server_groups.has_operation()) or
                (self.radius_server_groups is not None and self.radius_server_groups.has_operation()) or
                (self.tacacs_server_groups is not None and self.tacacs_server_groups.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "Cisco-IOS-XR-aaa-locald-cfg:server-groups" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "diameter-server-groups"):
                if (self.diameter_server_groups is None):
                    self.diameter_server_groups = Aaa.ServerGroups.DiameterServerGroups()
                    self.diameter_server_groups.parent = self
                    self._children_name_map["diameter_server_groups"] = "diameter-server-groups"
                return self.diameter_server_groups

            if (child_yang_name == "radius-server-groups"):
                if (self.radius_server_groups is None):
                    self.radius_server_groups = Aaa.ServerGroups.RadiusServerGroups()
                    self.radius_server_groups.parent = self
                    self._children_name_map["radius_server_groups"] = "radius-server-groups"
                return self.radius_server_groups

            if (child_yang_name == "tacacs-server-groups"):
                if (self.tacacs_server_groups is None):
                    self.tacacs_server_groups = Aaa.ServerGroups.TacacsServerGroups()
                    self.tacacs_server_groups.parent = self
                    self._children_name_map["tacacs_server_groups"] = "tacacs-server-groups"
                return self.tacacs_server_groups

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "diameter-server-groups" or name == "radius-server-groups" or name == "tacacs-server-groups"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Usernames(Entity):
        """
        Configure local usernames
        
        .. attribute:: username
        
        	Local username
        	**type**\: list of    :py:class:`Username <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Usernames.Username>`
        
        

        """

        _prefix = 'aaa-locald-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Aaa.Usernames, self).__init__()

            self.yang_name = "usernames"
            self.yang_parent_name = "aaa"

            self.username = YList(self)

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
                        super(Aaa.Usernames, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Aaa.Usernames, self).__setattr__(name, value)


        class Username(Entity):
            """
            Local username
            
            .. attribute:: ordering_index  <key>
            
            	This is used to sort the users in the order of precedence
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: name  <key>
            
            	Username
            	**type**\:  str
            
            .. attribute:: password
            
            	Specify the password for the user
            	**type**\:  str
            
            	**pattern:** (!.+)\|([^!].+)
            
            .. attribute:: secret
            
            	Specify the secret for the user
            	**type**\:  str
            
            	**pattern:** (!.+)\|([^!].+)
            
            .. attribute:: usergroup_under_usernames
            
            	Specify the usergroup to which this user belongs
            	**type**\:   :py:class:`UsergroupUnderUsernames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Usernames.Username.UsergroupUnderUsernames>`
            
            

            """

            _prefix = 'aaa-locald-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Usernames.Username, self).__init__()

                self.yang_name = "username"
                self.yang_parent_name = "usernames"

                self.ordering_index = YLeaf(YType.int32, "ordering-index")

                self.name = YLeaf(YType.str, "name")

                self.password = YLeaf(YType.str, "password")

                self.secret = YLeaf(YType.str, "secret")

                self.usergroup_under_usernames = Aaa.Usernames.Username.UsergroupUnderUsernames()
                self.usergroup_under_usernames.parent = self
                self._children_name_map["usergroup_under_usernames"] = "usergroup-under-usernames"
                self._children_yang_names.add("usergroup-under-usernames")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ordering_index",
                                "name",
                                "password",
                                "secret") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Aaa.Usernames.Username, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Aaa.Usernames.Username, self).__setattr__(name, value)


            class UsergroupUnderUsernames(Entity):
                """
                Specify the usergroup to which this user
                belongs
                
                .. attribute:: usergroup_under_username
                
                	Name of the usergroup
                	**type**\: list of    :py:class:`UsergroupUnderUsername <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Usernames.Username.UsergroupUnderUsernames.UsergroupUnderUsername>`
                
                

                """

                _prefix = 'aaa-locald-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.Usernames.Username.UsergroupUnderUsernames, self).__init__()

                    self.yang_name = "usergroup-under-usernames"
                    self.yang_parent_name = "username"

                    self.usergroup_under_username = YList(self)

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
                                super(Aaa.Usernames.Username.UsergroupUnderUsernames, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Aaa.Usernames.Username.UsergroupUnderUsernames, self).__setattr__(name, value)


                class UsergroupUnderUsername(Entity):
                    """
                    Name of the usergroup
                    
                    .. attribute:: name  <key>
                    
                    	Name of the usergroup
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    

                    """

                    _prefix = 'aaa-locald-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Aaa.Usernames.Username.UsergroupUnderUsernames.UsergroupUnderUsername, self).__init__()

                        self.yang_name = "usergroup-under-username"
                        self.yang_parent_name = "usergroup-under-usernames"

                        self.name = YLeaf(YType.str, "name")

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
                                    super(Aaa.Usernames.Username.UsergroupUnderUsernames.UsergroupUnderUsername, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Aaa.Usernames.Username.UsergroupUnderUsernames.UsergroupUnderUsername, self).__setattr__(name, value)

                    def has_data(self):
                        return self.name.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "usergroup-under-username" + "[name='" + self.name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
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

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "name"):
                            self.name = value
                            self.name.value_namespace = name_space
                            self.name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.usergroup_under_username:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.usergroup_under_username:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "usergroup-under-usernames" + path_buffer

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

                    if (child_yang_name == "usergroup-under-username"):
                        for c in self.usergroup_under_username:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Aaa.Usernames.Username.UsergroupUnderUsernames.UsergroupUnderUsername()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.usergroup_under_username.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "usergroup-under-username"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.ordering_index.is_set or
                    self.name.is_set or
                    self.password.is_set or
                    self.secret.is_set or
                    (self.usergroup_under_usernames is not None and self.usergroup_under_usernames.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ordering_index.yfilter != YFilter.not_set or
                    self.name.yfilter != YFilter.not_set or
                    self.password.yfilter != YFilter.not_set or
                    self.secret.yfilter != YFilter.not_set or
                    (self.usergroup_under_usernames is not None and self.usergroup_under_usernames.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "username" + "[ordering-index='" + self.ordering_index.get() + "']" + "[name='" + self.name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-locald-cfg:usernames/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ordering_index.is_set or self.ordering_index.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ordering_index.get_name_leafdata())
                if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.name.get_name_leafdata())
                if (self.password.is_set or self.password.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.password.get_name_leafdata())
                if (self.secret.is_set or self.secret.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.secret.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "usergroup-under-usernames"):
                    if (self.usergroup_under_usernames is None):
                        self.usergroup_under_usernames = Aaa.Usernames.Username.UsergroupUnderUsernames()
                        self.usergroup_under_usernames.parent = self
                        self._children_name_map["usergroup_under_usernames"] = "usergroup-under-usernames"
                    return self.usergroup_under_usernames

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "usergroup-under-usernames" or name == "ordering-index" or name == "name" or name == "password" or name == "secret"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ordering-index"):
                    self.ordering_index = value
                    self.ordering_index.value_namespace = name_space
                    self.ordering_index.value_namespace_prefix = name_space_prefix
                if(value_path == "name"):
                    self.name = value
                    self.name.value_namespace = name_space
                    self.name.value_namespace_prefix = name_space_prefix
                if(value_path == "password"):
                    self.password = value
                    self.password.value_namespace = name_space
                    self.password.value_namespace_prefix = name_space_prefix
                if(value_path == "secret"):
                    self.secret = value
                    self.secret.value_namespace = name_space
                    self.secret.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.username:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.username:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "Cisco-IOS-XR-aaa-locald-cfg:usernames" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "username"):
                for c in self.username:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Aaa.Usernames.Username()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.username.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "username"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Taskgroups(Entity):
        """
        Specify a taskgroup to inherit from
        
        .. attribute:: taskgroup
        
        	Taskgroup name
        	**type**\: list of    :py:class:`Taskgroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Taskgroups.Taskgroup>`
        
        

        """

        _prefix = 'aaa-locald-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Aaa.Taskgroups, self).__init__()

            self.yang_name = "taskgroups"
            self.yang_parent_name = "aaa"

            self.taskgroup = YList(self)

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
                        super(Aaa.Taskgroups, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Aaa.Taskgroups, self).__setattr__(name, value)


        class Taskgroup(Entity):
            """
            Taskgroup name
            
            .. attribute:: name  <key>
            
            	Taskgroup name
            	**type**\:  str
            
            .. attribute:: description
            
            	Description for the task group
            	**type**\:  str
            
            .. attribute:: taskgroup_under_taskgroups
            
            	Specify a taskgroup to inherit from
            	**type**\:   :py:class:`TaskgroupUnderTaskgroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Taskgroups.Taskgroup.TaskgroupUnderTaskgroups>`
            
            .. attribute:: tasks
            
            	Specify task IDs to be part of this group
            	**type**\:   :py:class:`Tasks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Taskgroups.Taskgroup.Tasks>`
            
            

            """

            _prefix = 'aaa-locald-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Taskgroups.Taskgroup, self).__init__()

                self.yang_name = "taskgroup"
                self.yang_parent_name = "taskgroups"

                self.name = YLeaf(YType.str, "name")

                self.description = YLeaf(YType.str, "description")

                self.taskgroup_under_taskgroups = Aaa.Taskgroups.Taskgroup.TaskgroupUnderTaskgroups()
                self.taskgroup_under_taskgroups.parent = self
                self._children_name_map["taskgroup_under_taskgroups"] = "taskgroup-under-taskgroups"
                self._children_yang_names.add("taskgroup-under-taskgroups")

                self.tasks = Aaa.Taskgroups.Taskgroup.Tasks()
                self.tasks.parent = self
                self._children_name_map["tasks"] = "tasks"
                self._children_yang_names.add("tasks")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("name",
                                "description") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Aaa.Taskgroups.Taskgroup, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Aaa.Taskgroups.Taskgroup, self).__setattr__(name, value)


            class TaskgroupUnderTaskgroups(Entity):
                """
                Specify a taskgroup to inherit from
                
                .. attribute:: taskgroup_under_taskgroup
                
                	Name of the task group to include
                	**type**\: list of    :py:class:`TaskgroupUnderTaskgroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Taskgroups.Taskgroup.TaskgroupUnderTaskgroups.TaskgroupUnderTaskgroup>`
                
                

                """

                _prefix = 'aaa-locald-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.Taskgroups.Taskgroup.TaskgroupUnderTaskgroups, self).__init__()

                    self.yang_name = "taskgroup-under-taskgroups"
                    self.yang_parent_name = "taskgroup"

                    self.taskgroup_under_taskgroup = YList(self)

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
                                super(Aaa.Taskgroups.Taskgroup.TaskgroupUnderTaskgroups, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Aaa.Taskgroups.Taskgroup.TaskgroupUnderTaskgroups, self).__setattr__(name, value)


                class TaskgroupUnderTaskgroup(Entity):
                    """
                    Name of the task group to include
                    
                    .. attribute:: name  <key>
                    
                    	Name of the task group to include
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    

                    """

                    _prefix = 'aaa-locald-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Aaa.Taskgroups.Taskgroup.TaskgroupUnderTaskgroups.TaskgroupUnderTaskgroup, self).__init__()

                        self.yang_name = "taskgroup-under-taskgroup"
                        self.yang_parent_name = "taskgroup-under-taskgroups"

                        self.name = YLeaf(YType.str, "name")

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
                                    super(Aaa.Taskgroups.Taskgroup.TaskgroupUnderTaskgroups.TaskgroupUnderTaskgroup, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Aaa.Taskgroups.Taskgroup.TaskgroupUnderTaskgroups.TaskgroupUnderTaskgroup, self).__setattr__(name, value)

                    def has_data(self):
                        return self.name.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "taskgroup-under-taskgroup" + "[name='" + self.name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
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

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "name"):
                            self.name = value
                            self.name.value_namespace = name_space
                            self.name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.taskgroup_under_taskgroup:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.taskgroup_under_taskgroup:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "taskgroup-under-taskgroups" + path_buffer

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

                    if (child_yang_name == "taskgroup-under-taskgroup"):
                        for c in self.taskgroup_under_taskgroup:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Aaa.Taskgroups.Taskgroup.TaskgroupUnderTaskgroups.TaskgroupUnderTaskgroup()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.taskgroup_under_taskgroup.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "taskgroup-under-taskgroup"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Tasks(Entity):
                """
                Specify task IDs to be part of this group
                
                .. attribute:: task
                
                	Task ID to be included
                	**type**\: list of    :py:class:`Task <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Taskgroups.Taskgroup.Tasks.Task>`
                
                

                """

                _prefix = 'aaa-locald-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.Taskgroups.Taskgroup.Tasks, self).__init__()

                    self.yang_name = "tasks"
                    self.yang_parent_name = "taskgroup"

                    self.task = YList(self)

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
                                super(Aaa.Taskgroups.Taskgroup.Tasks, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Aaa.Taskgroups.Taskgroup.Tasks, self).__setattr__(name, value)


                class Task(Entity):
                    """
                    Task ID to be included
                    
                    .. attribute:: type  <key>
                    
                    	This specifies the operation permitted for this task eg\: read/write/execute/debug
                    	**type**\:   :py:class:`AaaLocaldTaskClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_cfg.AaaLocaldTaskClass>`
                    
                    .. attribute:: task_id  <key>
                    
                    	Task ID to which permission is to be granted (please use class AllTasks to get a list of valid task IDs)
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'aaa-locald-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Aaa.Taskgroups.Taskgroup.Tasks.Task, self).__init__()

                        self.yang_name = "task"
                        self.yang_parent_name = "tasks"

                        self.type = YLeaf(YType.enumeration, "type")

                        self.task_id = YLeaf(YType.str, "task-id")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("type",
                                        "task_id") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Aaa.Taskgroups.Taskgroup.Tasks.Task, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Aaa.Taskgroups.Taskgroup.Tasks.Task, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.type.is_set or
                            self.task_id.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.type.yfilter != YFilter.not_set or
                            self.task_id.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "task" + "[type='" + self.type.get() + "']" + "[task-id='" + self.task_id.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.type.get_name_leafdata())
                        if (self.task_id.is_set or self.task_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.task_id.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "type" or name == "task-id"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "type"):
                            self.type = value
                            self.type.value_namespace = name_space
                            self.type.value_namespace_prefix = name_space_prefix
                        if(value_path == "task-id"):
                            self.task_id = value
                            self.task_id.value_namespace = name_space
                            self.task_id.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.task:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.task:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "tasks" + path_buffer

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

                    if (child_yang_name == "task"):
                        for c in self.task:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Aaa.Taskgroups.Taskgroup.Tasks.Task()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.task.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "task"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.name.is_set or
                    self.description.is_set or
                    (self.taskgroup_under_taskgroups is not None and self.taskgroup_under_taskgroups.has_data()) or
                    (self.tasks is not None and self.tasks.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.name.yfilter != YFilter.not_set or
                    self.description.yfilter != YFilter.not_set or
                    (self.taskgroup_under_taskgroups is not None and self.taskgroup_under_taskgroups.has_operation()) or
                    (self.tasks is not None and self.tasks.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "taskgroup" + "[name='" + self.name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-locald-cfg:taskgroups/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.name.get_name_leafdata())
                if (self.description.is_set or self.description.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.description.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "taskgroup-under-taskgroups"):
                    if (self.taskgroup_under_taskgroups is None):
                        self.taskgroup_under_taskgroups = Aaa.Taskgroups.Taskgroup.TaskgroupUnderTaskgroups()
                        self.taskgroup_under_taskgroups.parent = self
                        self._children_name_map["taskgroup_under_taskgroups"] = "taskgroup-under-taskgroups"
                    return self.taskgroup_under_taskgroups

                if (child_yang_name == "tasks"):
                    if (self.tasks is None):
                        self.tasks = Aaa.Taskgroups.Taskgroup.Tasks()
                        self.tasks.parent = self
                        self._children_name_map["tasks"] = "tasks"
                    return self.tasks

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "taskgroup-under-taskgroups" or name == "tasks" or name == "name" or name == "description"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "name"):
                    self.name = value
                    self.name.value_namespace = name_space
                    self.name.value_namespace_prefix = name_space_prefix
                if(value_path == "description"):
                    self.description = value
                    self.description.value_namespace = name_space
                    self.description.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.taskgroup:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.taskgroup:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "Cisco-IOS-XR-aaa-locald-cfg:taskgroups" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "taskgroup"):
                for c in self.taskgroup:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Aaa.Taskgroups.Taskgroup()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.taskgroup.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "taskgroup"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Usergroups(Entity):
        """
        Specify a Usergroup to inherit from
        
        .. attribute:: usergroup
        
        	Usergroup name
        	**type**\: list of    :py:class:`Usergroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Usergroups.Usergroup>`
        
        

        """

        _prefix = 'aaa-locald-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Aaa.Usergroups, self).__init__()

            self.yang_name = "usergroups"
            self.yang_parent_name = "aaa"

            self.usergroup = YList(self)

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
                        super(Aaa.Usergroups, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Aaa.Usergroups, self).__setattr__(name, value)


        class Usergroup(Entity):
            """
            Usergroup name
            
            .. attribute:: name  <key>
            
            	Usergroup name
            	**type**\:  str
            
            .. attribute:: description
            
            	Description for the user group
            	**type**\:  str
            
            .. attribute:: taskgroup_under_usergroups
            
            	Task group associated with this group
            	**type**\:   :py:class:`TaskgroupUnderUsergroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Usergroups.Usergroup.TaskgroupUnderUsergroups>`
            
            .. attribute:: usergroup_under_usergroups
            
            	User group to be inherited by this group
            	**type**\:   :py:class:`UsergroupUnderUsergroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Usergroups.Usergroup.UsergroupUnderUsergroups>`
            
            

            """

            _prefix = 'aaa-locald-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Usergroups.Usergroup, self).__init__()

                self.yang_name = "usergroup"
                self.yang_parent_name = "usergroups"

                self.name = YLeaf(YType.str, "name")

                self.description = YLeaf(YType.str, "description")

                self.taskgroup_under_usergroups = Aaa.Usergroups.Usergroup.TaskgroupUnderUsergroups()
                self.taskgroup_under_usergroups.parent = self
                self._children_name_map["taskgroup_under_usergroups"] = "taskgroup-under-usergroups"
                self._children_yang_names.add("taskgroup-under-usergroups")

                self.usergroup_under_usergroups = Aaa.Usergroups.Usergroup.UsergroupUnderUsergroups()
                self.usergroup_under_usergroups.parent = self
                self._children_name_map["usergroup_under_usergroups"] = "usergroup-under-usergroups"
                self._children_yang_names.add("usergroup-under-usergroups")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("name",
                                "description") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Aaa.Usergroups.Usergroup, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Aaa.Usergroups.Usergroup, self).__setattr__(name, value)


            class TaskgroupUnderUsergroups(Entity):
                """
                Task group associated with this group
                
                .. attribute:: taskgroup_under_usergroup
                
                	Name of the task group
                	**type**\: list of    :py:class:`TaskgroupUnderUsergroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Usergroups.Usergroup.TaskgroupUnderUsergroups.TaskgroupUnderUsergroup>`
                
                

                """

                _prefix = 'aaa-locald-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.Usergroups.Usergroup.TaskgroupUnderUsergroups, self).__init__()

                    self.yang_name = "taskgroup-under-usergroups"
                    self.yang_parent_name = "usergroup"

                    self.taskgroup_under_usergroup = YList(self)

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
                                super(Aaa.Usergroups.Usergroup.TaskgroupUnderUsergroups, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Aaa.Usergroups.Usergroup.TaskgroupUnderUsergroups, self).__setattr__(name, value)


                class TaskgroupUnderUsergroup(Entity):
                    """
                    Name of the task group
                    
                    .. attribute:: name  <key>
                    
                    	Name of the task group
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    

                    """

                    _prefix = 'aaa-locald-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Aaa.Usergroups.Usergroup.TaskgroupUnderUsergroups.TaskgroupUnderUsergroup, self).__init__()

                        self.yang_name = "taskgroup-under-usergroup"
                        self.yang_parent_name = "taskgroup-under-usergroups"

                        self.name = YLeaf(YType.str, "name")

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
                                    super(Aaa.Usergroups.Usergroup.TaskgroupUnderUsergroups.TaskgroupUnderUsergroup, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Aaa.Usergroups.Usergroup.TaskgroupUnderUsergroups.TaskgroupUnderUsergroup, self).__setattr__(name, value)

                    def has_data(self):
                        return self.name.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "taskgroup-under-usergroup" + "[name='" + self.name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
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

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "name"):
                            self.name = value
                            self.name.value_namespace = name_space
                            self.name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.taskgroup_under_usergroup:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.taskgroup_under_usergroup:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "taskgroup-under-usergroups" + path_buffer

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

                    if (child_yang_name == "taskgroup-under-usergroup"):
                        for c in self.taskgroup_under_usergroup:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Aaa.Usergroups.Usergroup.TaskgroupUnderUsergroups.TaskgroupUnderUsergroup()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.taskgroup_under_usergroup.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "taskgroup-under-usergroup"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class UsergroupUnderUsergroups(Entity):
                """
                User group to be inherited by this group
                
                .. attribute:: usergroup_under_usergroup
                
                	Name of the user group
                	**type**\: list of    :py:class:`UsergroupUnderUsergroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Usergroups.Usergroup.UsergroupUnderUsergroups.UsergroupUnderUsergroup>`
                
                

                """

                _prefix = 'aaa-locald-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.Usergroups.Usergroup.UsergroupUnderUsergroups, self).__init__()

                    self.yang_name = "usergroup-under-usergroups"
                    self.yang_parent_name = "usergroup"

                    self.usergroup_under_usergroup = YList(self)

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
                                super(Aaa.Usergroups.Usergroup.UsergroupUnderUsergroups, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Aaa.Usergroups.Usergroup.UsergroupUnderUsergroups, self).__setattr__(name, value)


                class UsergroupUnderUsergroup(Entity):
                    """
                    Name of the user group
                    
                    .. attribute:: name  <key>
                    
                    	Name of the user group
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    

                    """

                    _prefix = 'aaa-locald-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Aaa.Usergroups.Usergroup.UsergroupUnderUsergroups.UsergroupUnderUsergroup, self).__init__()

                        self.yang_name = "usergroup-under-usergroup"
                        self.yang_parent_name = "usergroup-under-usergroups"

                        self.name = YLeaf(YType.str, "name")

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
                                    super(Aaa.Usergroups.Usergroup.UsergroupUnderUsergroups.UsergroupUnderUsergroup, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Aaa.Usergroups.Usergroup.UsergroupUnderUsergroups.UsergroupUnderUsergroup, self).__setattr__(name, value)

                    def has_data(self):
                        return self.name.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "usergroup-under-usergroup" + "[name='" + self.name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
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

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "name"):
                            self.name = value
                            self.name.value_namespace = name_space
                            self.name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.usergroup_under_usergroup:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.usergroup_under_usergroup:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "usergroup-under-usergroups" + path_buffer

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

                    if (child_yang_name == "usergroup-under-usergroup"):
                        for c in self.usergroup_under_usergroup:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Aaa.Usergroups.Usergroup.UsergroupUnderUsergroups.UsergroupUnderUsergroup()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.usergroup_under_usergroup.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "usergroup-under-usergroup"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.name.is_set or
                    self.description.is_set or
                    (self.taskgroup_under_usergroups is not None and self.taskgroup_under_usergroups.has_data()) or
                    (self.usergroup_under_usergroups is not None and self.usergroup_under_usergroups.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.name.yfilter != YFilter.not_set or
                    self.description.yfilter != YFilter.not_set or
                    (self.taskgroup_under_usergroups is not None and self.taskgroup_under_usergroups.has_operation()) or
                    (self.usergroup_under_usergroups is not None and self.usergroup_under_usergroups.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "usergroup" + "[name='" + self.name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-locald-cfg:usergroups/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.name.get_name_leafdata())
                if (self.description.is_set or self.description.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.description.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "taskgroup-under-usergroups"):
                    if (self.taskgroup_under_usergroups is None):
                        self.taskgroup_under_usergroups = Aaa.Usergroups.Usergroup.TaskgroupUnderUsergroups()
                        self.taskgroup_under_usergroups.parent = self
                        self._children_name_map["taskgroup_under_usergroups"] = "taskgroup-under-usergroups"
                    return self.taskgroup_under_usergroups

                if (child_yang_name == "usergroup-under-usergroups"):
                    if (self.usergroup_under_usergroups is None):
                        self.usergroup_under_usergroups = Aaa.Usergroups.Usergroup.UsergroupUnderUsergroups()
                        self.usergroup_under_usergroups.parent = self
                        self._children_name_map["usergroup_under_usergroups"] = "usergroup-under-usergroups"
                    return self.usergroup_under_usergroups

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "taskgroup-under-usergroups" or name == "usergroup-under-usergroups" or name == "name" or name == "description"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "name"):
                    self.name = value
                    self.name.value_namespace = name_space
                    self.name.value_namespace_prefix = name_space_prefix
                if(value_path == "description"):
                    self.description = value
                    self.description.value_namespace = name_space
                    self.description.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.usergroup:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.usergroup:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "Cisco-IOS-XR-aaa-locald-cfg:usergroups" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "usergroup"):
                for c in self.usergroup:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Aaa.Usergroups.Usergroup()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.usergroup.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "usergroup"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Diameter(Entity):
        """
        Diameter base protocol
        
        .. attribute:: diameter_timer
        
        	Timers used for the peer
        	**type**\:   :py:class:`DiameterTimer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Diameter.DiameterTimer>`
        
        .. attribute:: diameter_tls
        
        	TLS sub commands
        	**type**\:   :py:class:`DiameterTls <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Diameter.DiameterTls>`
        
        .. attribute:: diams
        
        	Attribute list configuration for test command
        	**type**\:   :py:class:`Diams <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Diameter.Diams>`
        
        .. attribute:: gx
        
        	Start diameter policy\-if
        	**type**\:   :py:class:`Gx <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Diameter.Gx>`
        
        .. attribute:: gy
        
        	Start diameter policy\-if
        	**type**\:   :py:class:`Gy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Diameter.Gy>`
        
        .. attribute:: nas
        
        	Start diameter Nas
        	**type**\:   :py:class:`Nas <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Diameter.Nas>`
        
        .. attribute:: origin
        
        	Origin sub commands
        	**type**\:   :py:class:`Origin <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Diameter.Origin>`
        
        .. attribute:: peers
        
        	List of diameter peers
        	**type**\:   :py:class:`Peers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Diameter.Peers>`
        
        .. attribute:: source_interface
        
        	Specify interface for source address in DIAMETER packets
        	**type**\:  str
        
        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
        
        .. attribute:: vendor
        
        	Vendor specific
        	**type**\:   :py:class:`Vendor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Diameter.Vendor>`
        
        

        """

        _prefix = 'aaa-diameter-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Aaa.Diameter, self).__init__()

            self.yang_name = "diameter"
            self.yang_parent_name = "aaa"

            self.source_interface = YLeaf(YType.str, "source-interface")

            self.diameter_timer = Aaa.Diameter.DiameterTimer()
            self.diameter_timer.parent = self
            self._children_name_map["diameter_timer"] = "diameter-timer"
            self._children_yang_names.add("diameter-timer")

            self.diameter_tls = Aaa.Diameter.DiameterTls()
            self.diameter_tls.parent = self
            self._children_name_map["diameter_tls"] = "diameter-tls"
            self._children_yang_names.add("diameter-tls")

            self.diams = Aaa.Diameter.Diams()
            self.diams.parent = self
            self._children_name_map["diams"] = "diams"
            self._children_yang_names.add("diams")

            self.gx = Aaa.Diameter.Gx()
            self.gx.parent = self
            self._children_name_map["gx"] = "gx"
            self._children_yang_names.add("gx")

            self.gy = Aaa.Diameter.Gy()
            self.gy.parent = self
            self._children_name_map["gy"] = "gy"
            self._children_yang_names.add("gy")

            self.nas = Aaa.Diameter.Nas()
            self.nas.parent = self
            self._children_name_map["nas"] = "nas"
            self._children_yang_names.add("nas")

            self.origin = Aaa.Diameter.Origin()
            self.origin.parent = self
            self._children_name_map["origin"] = "origin"
            self._children_yang_names.add("origin")

            self.peers = Aaa.Diameter.Peers()
            self.peers.parent = self
            self._children_name_map["peers"] = "peers"
            self._children_yang_names.add("peers")

            self.vendor = Aaa.Diameter.Vendor()
            self.vendor.parent = self
            self._children_name_map["vendor"] = "vendor"
            self._children_yang_names.add("vendor")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("source_interface") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Aaa.Diameter, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Aaa.Diameter, self).__setattr__(name, value)


        class Gy(Entity):
            """
            Start diameter policy\-if
            
            .. attribute:: dest_host
            
            	Destination Host name in FQDN format
            	**type**\:  str
            
            .. attribute:: retransmit
            
            	Set retransmit count
            	**type**\:  int
            
            	**range:** 1..10
            
            .. attribute:: tx_timer
            
            	Transaction timer value
            	**type**\:  int
            
            	**range:** 1..1000
            
            

            """

            _prefix = 'aaa-diameter-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Diameter.Gy, self).__init__()

                self.yang_name = "gy"
                self.yang_parent_name = "diameter"

                self.dest_host = YLeaf(YType.str, "dest-host")

                self.retransmit = YLeaf(YType.uint32, "retransmit")

                self.tx_timer = YLeaf(YType.uint32, "tx-timer")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("dest_host",
                                "retransmit",
                                "tx_timer") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Aaa.Diameter.Gy, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Aaa.Diameter.Gy, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.dest_host.is_set or
                    self.retransmit.is_set or
                    self.tx_timer.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.dest_host.yfilter != YFilter.not_set or
                    self.retransmit.yfilter != YFilter.not_set or
                    self.tx_timer.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "gy" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-diameter-cfg:diameter/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.dest_host.is_set or self.dest_host.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dest_host.get_name_leafdata())
                if (self.retransmit.is_set or self.retransmit.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.retransmit.get_name_leafdata())
                if (self.tx_timer.is_set or self.tx_timer.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tx_timer.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "dest-host" or name == "retransmit" or name == "tx-timer"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "dest-host"):
                    self.dest_host = value
                    self.dest_host.value_namespace = name_space
                    self.dest_host.value_namespace_prefix = name_space_prefix
                if(value_path == "retransmit"):
                    self.retransmit = value
                    self.retransmit.value_namespace = name_space
                    self.retransmit.value_namespace_prefix = name_space_prefix
                if(value_path == "tx-timer"):
                    self.tx_timer = value
                    self.tx_timer.value_namespace = name_space
                    self.tx_timer.value_namespace_prefix = name_space_prefix


        class Origin(Entity):
            """
            Origin sub commands
            
            .. attribute:: host
            
            	Host name in FQDN format
            	**type**\:  str
            
            .. attribute:: realm
            
            	Origin Realm String
            	**type**\:  str
            
            

            """

            _prefix = 'aaa-diameter-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Diameter.Origin, self).__init__()

                self.yang_name = "origin"
                self.yang_parent_name = "diameter"

                self.host = YLeaf(YType.str, "host")

                self.realm = YLeaf(YType.str, "realm")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("host",
                                "realm") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Aaa.Diameter.Origin, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Aaa.Diameter.Origin, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.host.is_set or
                    self.realm.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.host.yfilter != YFilter.not_set or
                    self.realm.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "origin" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-diameter-cfg:diameter/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.host.is_set or self.host.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.host.get_name_leafdata())
                if (self.realm.is_set or self.realm.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.realm.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "host" or name == "realm"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "host"):
                    self.host = value
                    self.host.value_namespace = name_space
                    self.host.value_namespace_prefix = name_space_prefix
                if(value_path == "realm"):
                    self.realm = value
                    self.realm.value_namespace = name_space
                    self.realm.value_namespace_prefix = name_space_prefix


        class Nas(Entity):
            """
            Start diameter Nas
            
            .. attribute:: dest_host
            
            	Destination Host name in FQDN format
            	**type**\:  str
            
            

            """

            _prefix = 'aaa-diameter-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Diameter.Nas, self).__init__()

                self.yang_name = "nas"
                self.yang_parent_name = "diameter"

                self.dest_host = YLeaf(YType.str, "dest-host")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("dest_host") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Aaa.Diameter.Nas, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Aaa.Diameter.Nas, self).__setattr__(name, value)

            def has_data(self):
                return self.dest_host.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.dest_host.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "nas" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-diameter-cfg:diameter/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.dest_host.is_set or self.dest_host.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dest_host.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "dest-host"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "dest-host"):
                    self.dest_host = value
                    self.dest_host.value_namespace = name_space
                    self.dest_host.value_namespace_prefix = name_space_prefix


        class DiameterTls(Entity):
            """
            TLS sub commands
            
            .. attribute:: trustpoint
            
            	Trustpoint label to be used
            	**type**\:  str
            
            

            """

            _prefix = 'aaa-diameter-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Diameter.DiameterTls, self).__init__()

                self.yang_name = "diameter-tls"
                self.yang_parent_name = "diameter"

                self.trustpoint = YLeaf(YType.str, "trustpoint")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("trustpoint") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Aaa.Diameter.DiameterTls, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Aaa.Diameter.DiameterTls, self).__setattr__(name, value)

            def has_data(self):
                return self.trustpoint.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.trustpoint.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "diameter-tls" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-diameter-cfg:diameter/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.trustpoint.is_set or self.trustpoint.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.trustpoint.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "trustpoint"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "trustpoint"):
                    self.trustpoint = value
                    self.trustpoint.value_namespace = name_space
                    self.trustpoint.value_namespace_prefix = name_space_prefix


        class Peers(Entity):
            """
            List of diameter peers
            
            .. attribute:: peer
            
            	Diameter peer instance
            	**type**\: list of    :py:class:`Peer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Diameter.Peers.Peer>`
            
            

            """

            _prefix = 'aaa-diameter-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Diameter.Peers, self).__init__()

                self.yang_name = "peers"
                self.yang_parent_name = "diameter"

                self.peer = YList(self)

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
                            super(Aaa.Diameter.Peers, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Aaa.Diameter.Peers, self).__setattr__(name, value)


            class Peer(Entity):
                """
                Diameter peer instance
                
                .. attribute:: peer_name  <key>
                
                	Name for the diameter peer configuration
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: host_destination
                
                	Destination host information
                	**type**\:  str
                
                .. attribute:: ipv4_address
                
                	IPv4 address of diameter server
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ipv6_address
                
                	IPv6 address of diameter server
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: peer_timer
                
                	Timers used for the peer
                	**type**\:   :py:class:`PeerTimer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Diameter.Peers.Peer.PeerTimer>`
                
                .. attribute:: peer_type
                
                	Peer Type
                	**type**\:   :py:class:`PeerType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Diameter.Peers.Peer.PeerType>`
                
                .. attribute:: realm_destination
                
                	Realm to which the peer belongs to
                	**type**\:  str
                
                .. attribute:: source_interface
                
                	Specify interface for source address in DIAMETER packets
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: tcp_transport
                
                	Specify a Diameter transport protocol
                	**type**\:  int
                
                	**range:** 1..65535
                
                .. attribute:: tls_transport
                
                	Specify a Diameter security type
                	**type**\:  int
                
                	**range:** 0..1
                
                .. attribute:: vrf_ip
                
                	VRF the peer belongs to
                	**type**\:  str
                
                

                """

                _prefix = 'aaa-diameter-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.Diameter.Peers.Peer, self).__init__()

                    self.yang_name = "peer"
                    self.yang_parent_name = "peers"

                    self.peer_name = YLeaf(YType.str, "peer-name")

                    self.host_destination = YLeaf(YType.str, "host-destination")

                    self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                    self.ipv6_address = YLeaf(YType.str, "ipv6-address")

                    self.realm_destination = YLeaf(YType.str, "realm-destination")

                    self.source_interface = YLeaf(YType.str, "source-interface")

                    self.tcp_transport = YLeaf(YType.uint32, "tcp-transport")

                    self.tls_transport = YLeaf(YType.uint32, "tls-transport")

                    self.vrf_ip = YLeaf(YType.str, "vrf-ip")

                    self.peer_timer = Aaa.Diameter.Peers.Peer.PeerTimer()
                    self.peer_timer.parent = self
                    self._children_name_map["peer_timer"] = "peer-timer"
                    self._children_yang_names.add("peer-timer")

                    self.peer_type = Aaa.Diameter.Peers.Peer.PeerType()
                    self.peer_type.parent = self
                    self._children_name_map["peer_type"] = "peer-type"
                    self._children_yang_names.add("peer-type")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("peer_name",
                                    "host_destination",
                                    "ipv4_address",
                                    "ipv6_address",
                                    "realm_destination",
                                    "source_interface",
                                    "tcp_transport",
                                    "tls_transport",
                                    "vrf_ip") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Aaa.Diameter.Peers.Peer, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Aaa.Diameter.Peers.Peer, self).__setattr__(name, value)


                class PeerTimer(Entity):
                    """
                    Timers used for the peer
                    
                    .. attribute:: connection
                    
                    	Timer value in seconds
                    	**type**\:  int
                    
                    	**range:** 1..1000
                    
                    	**default value**\: 5
                    
                    .. attribute:: transaction
                    
                    	Timer value in seconds
                    	**type**\:  int
                    
                    	**range:** 1..1000
                    
                    	**default value**\: 5
                    
                    .. attribute:: watchdog
                    
                    	Timer value in seconds
                    	**type**\:  int
                    
                    	**range:** 1..1000
                    
                    	**default value**\: 5
                    
                    

                    """

                    _prefix = 'aaa-diameter-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Aaa.Diameter.Peers.Peer.PeerTimer, self).__init__()

                        self.yang_name = "peer-timer"
                        self.yang_parent_name = "peer"

                        self.connection = YLeaf(YType.uint32, "connection")

                        self.transaction = YLeaf(YType.uint32, "transaction")

                        self.watchdog = YLeaf(YType.uint32, "watchdog")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("connection",
                                        "transaction",
                                        "watchdog") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Aaa.Diameter.Peers.Peer.PeerTimer, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Aaa.Diameter.Peers.Peer.PeerTimer, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.connection.is_set or
                            self.transaction.is_set or
                            self.watchdog.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.connection.yfilter != YFilter.not_set or
                            self.transaction.yfilter != YFilter.not_set or
                            self.watchdog.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "peer-timer" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.connection.is_set or self.connection.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.connection.get_name_leafdata())
                        if (self.transaction.is_set or self.transaction.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.transaction.get_name_leafdata())
                        if (self.watchdog.is_set or self.watchdog.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.watchdog.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "connection" or name == "transaction" or name == "watchdog"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "connection"):
                            self.connection = value
                            self.connection.value_namespace = name_space
                            self.connection.value_namespace_prefix = name_space_prefix
                        if(value_path == "transaction"):
                            self.transaction = value
                            self.transaction.value_namespace = name_space
                            self.transaction.value_namespace_prefix = name_space_prefix
                        if(value_path == "watchdog"):
                            self.watchdog = value
                            self.watchdog.value_namespace = name_space
                            self.watchdog.value_namespace_prefix = name_space_prefix


                class PeerType(Entity):
                    """
                    Peer Type
                    
                    .. attribute:: server
                    
                    	Enabled or disabled
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'aaa-diameter-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Aaa.Diameter.Peers.Peer.PeerType, self).__init__()

                        self.yang_name = "peer-type"
                        self.yang_parent_name = "peer"

                        self.server = YLeaf(YType.boolean, "server")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("server") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Aaa.Diameter.Peers.Peer.PeerType, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Aaa.Diameter.Peers.Peer.PeerType, self).__setattr__(name, value)

                    def has_data(self):
                        return self.server.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.server.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "peer-type" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.server.is_set or self.server.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.server.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "server"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "server"):
                            self.server = value
                            self.server.value_namespace = name_space
                            self.server.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.peer_name.is_set or
                        self.host_destination.is_set or
                        self.ipv4_address.is_set or
                        self.ipv6_address.is_set or
                        self.realm_destination.is_set or
                        self.source_interface.is_set or
                        self.tcp_transport.is_set or
                        self.tls_transport.is_set or
                        self.vrf_ip.is_set or
                        (self.peer_timer is not None and self.peer_timer.has_data()) or
                        (self.peer_type is not None and self.peer_type.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.peer_name.yfilter != YFilter.not_set or
                        self.host_destination.yfilter != YFilter.not_set or
                        self.ipv4_address.yfilter != YFilter.not_set or
                        self.ipv6_address.yfilter != YFilter.not_set or
                        self.realm_destination.yfilter != YFilter.not_set or
                        self.source_interface.yfilter != YFilter.not_set or
                        self.tcp_transport.yfilter != YFilter.not_set or
                        self.tls_transport.yfilter != YFilter.not_set or
                        self.vrf_ip.yfilter != YFilter.not_set or
                        (self.peer_timer is not None and self.peer_timer.has_operation()) or
                        (self.peer_type is not None and self.peer_type.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "peer" + "[peer-name='" + self.peer_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-diameter-cfg:diameter/peers/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.peer_name.is_set or self.peer_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.peer_name.get_name_leafdata())
                    if (self.host_destination.is_set or self.host_destination.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.host_destination.get_name_leafdata())
                    if (self.ipv4_address.is_set or self.ipv4_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ipv4_address.get_name_leafdata())
                    if (self.ipv6_address.is_set or self.ipv6_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ipv6_address.get_name_leafdata())
                    if (self.realm_destination.is_set or self.realm_destination.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.realm_destination.get_name_leafdata())
                    if (self.source_interface.is_set or self.source_interface.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.source_interface.get_name_leafdata())
                    if (self.tcp_transport.is_set or self.tcp_transport.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tcp_transport.get_name_leafdata())
                    if (self.tls_transport.is_set or self.tls_transport.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tls_transport.get_name_leafdata())
                    if (self.vrf_ip.is_set or self.vrf_ip.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.vrf_ip.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "peer-timer"):
                        if (self.peer_timer is None):
                            self.peer_timer = Aaa.Diameter.Peers.Peer.PeerTimer()
                            self.peer_timer.parent = self
                            self._children_name_map["peer_timer"] = "peer-timer"
                        return self.peer_timer

                    if (child_yang_name == "peer-type"):
                        if (self.peer_type is None):
                            self.peer_type = Aaa.Diameter.Peers.Peer.PeerType()
                            self.peer_type.parent = self
                            self._children_name_map["peer_type"] = "peer-type"
                        return self.peer_type

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "peer-timer" or name == "peer-type" or name == "peer-name" or name == "host-destination" or name == "ipv4-address" or name == "ipv6-address" or name == "realm-destination" or name == "source-interface" or name == "tcp-transport" or name == "tls-transport" or name == "vrf-ip"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "peer-name"):
                        self.peer_name = value
                        self.peer_name.value_namespace = name_space
                        self.peer_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "host-destination"):
                        self.host_destination = value
                        self.host_destination.value_namespace = name_space
                        self.host_destination.value_namespace_prefix = name_space_prefix
                    if(value_path == "ipv4-address"):
                        self.ipv4_address = value
                        self.ipv4_address.value_namespace = name_space
                        self.ipv4_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "ipv6-address"):
                        self.ipv6_address = value
                        self.ipv6_address.value_namespace = name_space
                        self.ipv6_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "realm-destination"):
                        self.realm_destination = value
                        self.realm_destination.value_namespace = name_space
                        self.realm_destination.value_namespace_prefix = name_space_prefix
                    if(value_path == "source-interface"):
                        self.source_interface = value
                        self.source_interface.value_namespace = name_space
                        self.source_interface.value_namespace_prefix = name_space_prefix
                    if(value_path == "tcp-transport"):
                        self.tcp_transport = value
                        self.tcp_transport.value_namespace = name_space
                        self.tcp_transport.value_namespace_prefix = name_space_prefix
                    if(value_path == "tls-transport"):
                        self.tls_transport = value
                        self.tls_transport.value_namespace = name_space
                        self.tls_transport.value_namespace_prefix = name_space_prefix
                    if(value_path == "vrf-ip"):
                        self.vrf_ip = value
                        self.vrf_ip.value_namespace = name_space
                        self.vrf_ip.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.peer:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.peer:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "peers" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-diameter-cfg:diameter/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "peer"):
                    for c in self.peer:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Aaa.Diameter.Peers.Peer()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.peer.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "peer"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class Diams(Entity):
            """
            Attribute list configuration for test command
            
            .. attribute:: diam
            
            	attribute list configuration
            	**type**\: list of    :py:class:`Diam <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Diameter.Diams.Diam>`
            
            

            """

            _prefix = 'aaa-diameter-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Diameter.Diams, self).__init__()

                self.yang_name = "diams"
                self.yang_parent_name = "diameter"

                self.diam = YList(self)

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
                            super(Aaa.Diameter.Diams, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Aaa.Diameter.Diams, self).__setattr__(name, value)


            class Diam(Entity):
                """
                attribute list configuration
                
                .. attribute:: list_id  <key>
                
                	attribute list number
                	**type**\:  int
                
                	**range:** 0..99
                
                .. attribute:: diam_attr_defs
                
                	Specify an attribute definition
                	**type**\:   :py:class:`DiamAttrDefs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Diameter.Diams.Diam.DiamAttrDefs>`
                
                

                """

                _prefix = 'aaa-diameter-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.Diameter.Diams.Diam, self).__init__()

                    self.yang_name = "diam"
                    self.yang_parent_name = "diams"

                    self.list_id = YLeaf(YType.uint32, "list-id")

                    self.diam_attr_defs = Aaa.Diameter.Diams.Diam.DiamAttrDefs()
                    self.diam_attr_defs.parent = self
                    self._children_name_map["diam_attr_defs"] = "diam-attr-defs"
                    self._children_yang_names.add("diam-attr-defs")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("list_id") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Aaa.Diameter.Diams.Diam, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Aaa.Diameter.Diams.Diam, self).__setattr__(name, value)


                class DiamAttrDefs(Entity):
                    """
                    Specify an attribute definition
                    
                    .. attribute:: diam_attr_def
                    
                    	vendor id
                    	**type**\: list of    :py:class:`DiamAttrDef <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Diameter.Diams.Diam.DiamAttrDefs.DiamAttrDef>`
                    
                    

                    """

                    _prefix = 'aaa-diameter-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Aaa.Diameter.Diams.Diam.DiamAttrDefs, self).__init__()

                        self.yang_name = "diam-attr-defs"
                        self.yang_parent_name = "diam"

                        self.diam_attr_def = YList(self)

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
                                    super(Aaa.Diameter.Diams.Diam.DiamAttrDefs, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Aaa.Diameter.Diams.Diam.DiamAttrDefs, self).__setattr__(name, value)


                    class DiamAttrDef(Entity):
                        """
                        vendor id
                        
                        .. attribute:: vendor_id  <key>
                        
                        	value for vendor id
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: attribute_id  <key>
                        
                        	enter attribute id
                        	**type**\:  int
                        
                        	**range:** 1..65535
                        
                        .. attribute:: diam_attr_value
                        
                        	attr subcommands
                        	**type**\:   :py:class:`DiamAttrValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Diameter.Diams.Diam.DiamAttrDefs.DiamAttrDef.DiamAttrValue>`
                        
                        

                        """

                        _prefix = 'aaa-diameter-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Aaa.Diameter.Diams.Diam.DiamAttrDefs.DiamAttrDef, self).__init__()

                            self.yang_name = "diam-attr-def"
                            self.yang_parent_name = "diam-attr-defs"

                            self.vendor_id = YLeaf(YType.uint32, "vendor-id")

                            self.attribute_id = YLeaf(YType.uint32, "attribute-id")

                            self.diam_attr_value = Aaa.Diameter.Diams.Diam.DiamAttrDefs.DiamAttrDef.DiamAttrValue()
                            self.diam_attr_value.parent = self
                            self._children_name_map["diam_attr_value"] = "diam-attr-value"
                            self._children_yang_names.add("diam-attr-value")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("vendor_id",
                                            "attribute_id") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Aaa.Diameter.Diams.Diam.DiamAttrDefs.DiamAttrDef, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Aaa.Diameter.Diams.Diam.DiamAttrDefs.DiamAttrDef, self).__setattr__(name, value)


                        class DiamAttrValue(Entity):
                            """
                            attr subcommands
                            
                            .. attribute:: data_type
                            
                            	Dataypte of attribute
                            	**type**\:  int
                            
                            	**range:** 0..23
                            
                            .. attribute:: mandatory
                            
                            	Is mandatory?
                            	**type**\:  int
                            
                            	**range:** 0..1
                            
                            .. attribute:: type_binary
                            
                            	Binary type
                            	**type**\:  str
                            
                            .. attribute:: type_boolean
                            
                            	Boolean type
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: type_enum
                            
                            	Enumeration type
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: type_grouped
                            
                            	Grouped attribute
                            	**type**\:  int
                            
                            	**range:** 0..99
                            
                            .. attribute:: type_identity
                            
                            	Diameter\-identity type
                            	**type**\:  str
                            
                            .. attribute:: type_ipv4_address
                            
                            	IPv4 address type
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: type_string
                            
                            	String type
                            	**type**\:  str
                            
                            .. attribute:: type_ulong
                            
                            	Numeric type
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'aaa-diameter-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Aaa.Diameter.Diams.Diam.DiamAttrDefs.DiamAttrDef.DiamAttrValue, self).__init__()

                                self.yang_name = "diam-attr-value"
                                self.yang_parent_name = "diam-attr-def"

                                self.data_type = YLeaf(YType.uint32, "data-type")

                                self.mandatory = YLeaf(YType.uint32, "mandatory")

                                self.type_binary = YLeaf(YType.str, "type-binary")

                                self.type_boolean = YLeaf(YType.uint32, "type-boolean")

                                self.type_enum = YLeaf(YType.uint32, "type-enum")

                                self.type_grouped = YLeaf(YType.uint32, "type-grouped")

                                self.type_identity = YLeaf(YType.str, "type-identity")

                                self.type_ipv4_address = YLeaf(YType.str, "type-ipv4-address")

                                self.type_string = YLeaf(YType.str, "type-string")

                                self.type_ulong = YLeaf(YType.uint32, "type-ulong")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("data_type",
                                                "mandatory",
                                                "type_binary",
                                                "type_boolean",
                                                "type_enum",
                                                "type_grouped",
                                                "type_identity",
                                                "type_ipv4_address",
                                                "type_string",
                                                "type_ulong") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Aaa.Diameter.Diams.Diam.DiamAttrDefs.DiamAttrDef.DiamAttrValue, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Aaa.Diameter.Diams.Diam.DiamAttrDefs.DiamAttrDef.DiamAttrValue, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.data_type.is_set or
                                    self.mandatory.is_set or
                                    self.type_binary.is_set or
                                    self.type_boolean.is_set or
                                    self.type_enum.is_set or
                                    self.type_grouped.is_set or
                                    self.type_identity.is_set or
                                    self.type_ipv4_address.is_set or
                                    self.type_string.is_set or
                                    self.type_ulong.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.data_type.yfilter != YFilter.not_set or
                                    self.mandatory.yfilter != YFilter.not_set or
                                    self.type_binary.yfilter != YFilter.not_set or
                                    self.type_boolean.yfilter != YFilter.not_set or
                                    self.type_enum.yfilter != YFilter.not_set or
                                    self.type_grouped.yfilter != YFilter.not_set or
                                    self.type_identity.yfilter != YFilter.not_set or
                                    self.type_ipv4_address.yfilter != YFilter.not_set or
                                    self.type_string.yfilter != YFilter.not_set or
                                    self.type_ulong.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "diam-attr-value" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.data_type.is_set or self.data_type.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.data_type.get_name_leafdata())
                                if (self.mandatory.is_set or self.mandatory.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.mandatory.get_name_leafdata())
                                if (self.type_binary.is_set or self.type_binary.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.type_binary.get_name_leafdata())
                                if (self.type_boolean.is_set or self.type_boolean.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.type_boolean.get_name_leafdata())
                                if (self.type_enum.is_set or self.type_enum.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.type_enum.get_name_leafdata())
                                if (self.type_grouped.is_set or self.type_grouped.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.type_grouped.get_name_leafdata())
                                if (self.type_identity.is_set or self.type_identity.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.type_identity.get_name_leafdata())
                                if (self.type_ipv4_address.is_set or self.type_ipv4_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.type_ipv4_address.get_name_leafdata())
                                if (self.type_string.is_set or self.type_string.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.type_string.get_name_leafdata())
                                if (self.type_ulong.is_set or self.type_ulong.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.type_ulong.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "data-type" or name == "mandatory" or name == "type-binary" or name == "type-boolean" or name == "type-enum" or name == "type-grouped" or name == "type-identity" or name == "type-ipv4-address" or name == "type-string" or name == "type-ulong"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "data-type"):
                                    self.data_type = value
                                    self.data_type.value_namespace = name_space
                                    self.data_type.value_namespace_prefix = name_space_prefix
                                if(value_path == "mandatory"):
                                    self.mandatory = value
                                    self.mandatory.value_namespace = name_space
                                    self.mandatory.value_namespace_prefix = name_space_prefix
                                if(value_path == "type-binary"):
                                    self.type_binary = value
                                    self.type_binary.value_namespace = name_space
                                    self.type_binary.value_namespace_prefix = name_space_prefix
                                if(value_path == "type-boolean"):
                                    self.type_boolean = value
                                    self.type_boolean.value_namespace = name_space
                                    self.type_boolean.value_namespace_prefix = name_space_prefix
                                if(value_path == "type-enum"):
                                    self.type_enum = value
                                    self.type_enum.value_namespace = name_space
                                    self.type_enum.value_namespace_prefix = name_space_prefix
                                if(value_path == "type-grouped"):
                                    self.type_grouped = value
                                    self.type_grouped.value_namespace = name_space
                                    self.type_grouped.value_namespace_prefix = name_space_prefix
                                if(value_path == "type-identity"):
                                    self.type_identity = value
                                    self.type_identity.value_namespace = name_space
                                    self.type_identity.value_namespace_prefix = name_space_prefix
                                if(value_path == "type-ipv4-address"):
                                    self.type_ipv4_address = value
                                    self.type_ipv4_address.value_namespace = name_space
                                    self.type_ipv4_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "type-string"):
                                    self.type_string = value
                                    self.type_string.value_namespace = name_space
                                    self.type_string.value_namespace_prefix = name_space_prefix
                                if(value_path == "type-ulong"):
                                    self.type_ulong = value
                                    self.type_ulong.value_namespace = name_space
                                    self.type_ulong.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.vendor_id.is_set or
                                self.attribute_id.is_set or
                                (self.diam_attr_value is not None and self.diam_attr_value.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.vendor_id.yfilter != YFilter.not_set or
                                self.attribute_id.yfilter != YFilter.not_set or
                                (self.diam_attr_value is not None and self.diam_attr_value.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "diam-attr-def" + "[vendor-id='" + self.vendor_id.get() + "']" + "[attribute-id='" + self.attribute_id.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.vendor_id.is_set or self.vendor_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.vendor_id.get_name_leafdata())
                            if (self.attribute_id.is_set or self.attribute_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.attribute_id.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "diam-attr-value"):
                                if (self.diam_attr_value is None):
                                    self.diam_attr_value = Aaa.Diameter.Diams.Diam.DiamAttrDefs.DiamAttrDef.DiamAttrValue()
                                    self.diam_attr_value.parent = self
                                    self._children_name_map["diam_attr_value"] = "diam-attr-value"
                                return self.diam_attr_value

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "diam-attr-value" or name == "vendor-id" or name == "attribute-id"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "vendor-id"):
                                self.vendor_id = value
                                self.vendor_id.value_namespace = name_space
                                self.vendor_id.value_namespace_prefix = name_space_prefix
                            if(value_path == "attribute-id"):
                                self.attribute_id = value
                                self.attribute_id.value_namespace = name_space
                                self.attribute_id.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.diam_attr_def:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.diam_attr_def:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "diam-attr-defs" + path_buffer

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

                        if (child_yang_name == "diam-attr-def"):
                            for c in self.diam_attr_def:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Aaa.Diameter.Diams.Diam.DiamAttrDefs.DiamAttrDef()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.diam_attr_def.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "diam-attr-def"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        self.list_id.is_set or
                        (self.diam_attr_defs is not None and self.diam_attr_defs.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.list_id.yfilter != YFilter.not_set or
                        (self.diam_attr_defs is not None and self.diam_attr_defs.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "diam" + "[list-id='" + self.list_id.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-diameter-cfg:diameter/diams/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.list_id.is_set or self.list_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.list_id.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "diam-attr-defs"):
                        if (self.diam_attr_defs is None):
                            self.diam_attr_defs = Aaa.Diameter.Diams.Diam.DiamAttrDefs()
                            self.diam_attr_defs.parent = self
                            self._children_name_map["diam_attr_defs"] = "diam-attr-defs"
                        return self.diam_attr_defs

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "diam-attr-defs" or name == "list-id"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "list-id"):
                        self.list_id = value
                        self.list_id.value_namespace = name_space
                        self.list_id.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.diam:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.diam:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "diams" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-diameter-cfg:diameter/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "diam"):
                    for c in self.diam:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Aaa.Diameter.Diams.Diam()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.diam.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "diam"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class Gx(Entity):
            """
            Start diameter policy\-if
            
            .. attribute:: dest_host
            
            	Destination Host name in FQDN format
            	**type**\:  str
            
            .. attribute:: retransmit
            
            	Set retransmit count
            	**type**\:  int
            
            	**range:** 1..10
            
            .. attribute:: tx_timer
            
            	Transaction timer value
            	**type**\:  int
            
            	**range:** 1..1000
            
            

            """

            _prefix = 'aaa-diameter-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Diameter.Gx, self).__init__()

                self.yang_name = "gx"
                self.yang_parent_name = "diameter"

                self.dest_host = YLeaf(YType.str, "dest-host")

                self.retransmit = YLeaf(YType.uint32, "retransmit")

                self.tx_timer = YLeaf(YType.uint32, "tx-timer")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("dest_host",
                                "retransmit",
                                "tx_timer") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Aaa.Diameter.Gx, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Aaa.Diameter.Gx, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.dest_host.is_set or
                    self.retransmit.is_set or
                    self.tx_timer.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.dest_host.yfilter != YFilter.not_set or
                    self.retransmit.yfilter != YFilter.not_set or
                    self.tx_timer.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "gx" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-diameter-cfg:diameter/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.dest_host.is_set or self.dest_host.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dest_host.get_name_leafdata())
                if (self.retransmit.is_set or self.retransmit.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.retransmit.get_name_leafdata())
                if (self.tx_timer.is_set or self.tx_timer.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tx_timer.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "dest-host" or name == "retransmit" or name == "tx-timer"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "dest-host"):
                    self.dest_host = value
                    self.dest_host.value_namespace = name_space
                    self.dest_host.value_namespace_prefix = name_space_prefix
                if(value_path == "retransmit"):
                    self.retransmit = value
                    self.retransmit.value_namespace = name_space
                    self.retransmit.value_namespace_prefix = name_space_prefix
                if(value_path == "tx-timer"):
                    self.tx_timer = value
                    self.tx_timer.value_namespace = name_space
                    self.tx_timer.value_namespace_prefix = name_space_prefix


        class DiameterTimer(Entity):
            """
            Timers used for the peer
            
            .. attribute:: connection
            
            	Timer value in seconds
            	**type**\:  int
            
            	**range:** 1..1000
            
            .. attribute:: transaction
            
            	Timer value in seconds
            	**type**\:  int
            
            	**range:** 1..1000
            
            .. attribute:: watchdog
            
            	Timer value in seconds
            	**type**\:  int
            
            	**range:** 1..1000
            
            

            """

            _prefix = 'aaa-diameter-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Diameter.DiameterTimer, self).__init__()

                self.yang_name = "diameter-timer"
                self.yang_parent_name = "diameter"

                self.connection = YLeaf(YType.uint32, "connection")

                self.transaction = YLeaf(YType.uint32, "transaction")

                self.watchdog = YLeaf(YType.uint32, "watchdog")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("connection",
                                "transaction",
                                "watchdog") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Aaa.Diameter.DiameterTimer, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Aaa.Diameter.DiameterTimer, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.connection.is_set or
                    self.transaction.is_set or
                    self.watchdog.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.connection.yfilter != YFilter.not_set or
                    self.transaction.yfilter != YFilter.not_set or
                    self.watchdog.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "diameter-timer" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-diameter-cfg:diameter/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.connection.is_set or self.connection.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.connection.get_name_leafdata())
                if (self.transaction.is_set or self.transaction.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.transaction.get_name_leafdata())
                if (self.watchdog.is_set or self.watchdog.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.watchdog.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "connection" or name == "transaction" or name == "watchdog"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "connection"):
                    self.connection = value
                    self.connection.value_namespace = name_space
                    self.connection.value_namespace_prefix = name_space_prefix
                if(value_path == "transaction"):
                    self.transaction = value
                    self.transaction.value_namespace = name_space
                    self.transaction.value_namespace_prefix = name_space_prefix
                if(value_path == "watchdog"):
                    self.watchdog = value
                    self.watchdog.value_namespace = name_space
                    self.watchdog.value_namespace_prefix = name_space_prefix


        class Vendor(Entity):
            """
            Vendor specific
            
            .. attribute:: supported
            
            	Supported vendors
            	**type**\:   :py:class:`Supported <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Diameter.Vendor.Supported>`
            
            

            """

            _prefix = 'aaa-diameter-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Diameter.Vendor, self).__init__()

                self.yang_name = "vendor"
                self.yang_parent_name = "diameter"

                self.supported = Aaa.Diameter.Vendor.Supported()
                self.supported.parent = self
                self._children_name_map["supported"] = "supported"
                self._children_yang_names.add("supported")


            class Supported(Entity):
                """
                Supported vendors
                
                .. attribute:: cisco
                
                	Cisco attribute support
                	**type**\:  bool
                
                .. attribute:: etsi
                
                	Etsi attribute support
                	**type**\:  bool
                
                .. attribute:: threegpp
                
                	3GPP attribute support
                	**type**\:  bool
                
                .. attribute:: vodafone
                
                	Vodafone attribute support
                	**type**\:  bool
                
                

                """

                _prefix = 'aaa-diameter-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.Diameter.Vendor.Supported, self).__init__()

                    self.yang_name = "supported"
                    self.yang_parent_name = "vendor"

                    self.cisco = YLeaf(YType.boolean, "cisco")

                    self.etsi = YLeaf(YType.boolean, "etsi")

                    self.threegpp = YLeaf(YType.boolean, "threegpp")

                    self.vodafone = YLeaf(YType.boolean, "vodafone")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("cisco",
                                    "etsi",
                                    "threegpp",
                                    "vodafone") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Aaa.Diameter.Vendor.Supported, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Aaa.Diameter.Vendor.Supported, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.cisco.is_set or
                        self.etsi.is_set or
                        self.threegpp.is_set or
                        self.vodafone.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.cisco.yfilter != YFilter.not_set or
                        self.etsi.yfilter != YFilter.not_set or
                        self.threegpp.yfilter != YFilter.not_set or
                        self.vodafone.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "supported" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-diameter-cfg:diameter/vendor/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.cisco.is_set or self.cisco.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.cisco.get_name_leafdata())
                    if (self.etsi.is_set or self.etsi.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.etsi.get_name_leafdata())
                    if (self.threegpp.is_set or self.threegpp.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.threegpp.get_name_leafdata())
                    if (self.vodafone.is_set or self.vodafone.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.vodafone.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "cisco" or name == "etsi" or name == "threegpp" or name == "vodafone"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "cisco"):
                        self.cisco = value
                        self.cisco.value_namespace = name_space
                        self.cisco.value_namespace_prefix = name_space_prefix
                    if(value_path == "etsi"):
                        self.etsi = value
                        self.etsi.value_namespace = name_space
                        self.etsi.value_namespace_prefix = name_space_prefix
                    if(value_path == "threegpp"):
                        self.threegpp = value
                        self.threegpp.value_namespace = name_space
                        self.threegpp.value_namespace_prefix = name_space_prefix
                    if(value_path == "vodafone"):
                        self.vodafone = value
                        self.vodafone.value_namespace = name_space
                        self.vodafone.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (self.supported is not None and self.supported.has_data())

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.supported is not None and self.supported.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "vendor" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-diameter-cfg:diameter/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "supported"):
                    if (self.supported is None):
                        self.supported = Aaa.Diameter.Vendor.Supported()
                        self.supported.parent = self
                        self._children_name_map["supported"] = "supported"
                    return self.supported

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "supported"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                self.source_interface.is_set or
                (self.diameter_timer is not None and self.diameter_timer.has_data()) or
                (self.diameter_tls is not None and self.diameter_tls.has_data()) or
                (self.diams is not None and self.diams.has_data()) or
                (self.gx is not None and self.gx.has_data()) or
                (self.gy is not None and self.gy.has_data()) or
                (self.nas is not None and self.nas.has_data()) or
                (self.origin is not None and self.origin.has_data()) or
                (self.peers is not None and self.peers.has_data()) or
                (self.vendor is not None and self.vendor.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.source_interface.yfilter != YFilter.not_set or
                (self.diameter_timer is not None and self.diameter_timer.has_operation()) or
                (self.diameter_tls is not None and self.diameter_tls.has_operation()) or
                (self.diams is not None and self.diams.has_operation()) or
                (self.gx is not None and self.gx.has_operation()) or
                (self.gy is not None and self.gy.has_operation()) or
                (self.nas is not None and self.nas.has_operation()) or
                (self.origin is not None and self.origin.has_operation()) or
                (self.peers is not None and self.peers.has_operation()) or
                (self.vendor is not None and self.vendor.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "Cisco-IOS-XR-aaa-diameter-cfg:diameter" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.source_interface.is_set or self.source_interface.yfilter != YFilter.not_set):
                leaf_name_data.append(self.source_interface.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "diameter-timer"):
                if (self.diameter_timer is None):
                    self.diameter_timer = Aaa.Diameter.DiameterTimer()
                    self.diameter_timer.parent = self
                    self._children_name_map["diameter_timer"] = "diameter-timer"
                return self.diameter_timer

            if (child_yang_name == "diameter-tls"):
                if (self.diameter_tls is None):
                    self.diameter_tls = Aaa.Diameter.DiameterTls()
                    self.diameter_tls.parent = self
                    self._children_name_map["diameter_tls"] = "diameter-tls"
                return self.diameter_tls

            if (child_yang_name == "diams"):
                if (self.diams is None):
                    self.diams = Aaa.Diameter.Diams()
                    self.diams.parent = self
                    self._children_name_map["diams"] = "diams"
                return self.diams

            if (child_yang_name == "gx"):
                if (self.gx is None):
                    self.gx = Aaa.Diameter.Gx()
                    self.gx.parent = self
                    self._children_name_map["gx"] = "gx"
                return self.gx

            if (child_yang_name == "gy"):
                if (self.gy is None):
                    self.gy = Aaa.Diameter.Gy()
                    self.gy.parent = self
                    self._children_name_map["gy"] = "gy"
                return self.gy

            if (child_yang_name == "nas"):
                if (self.nas is None):
                    self.nas = Aaa.Diameter.Nas()
                    self.nas.parent = self
                    self._children_name_map["nas"] = "nas"
                return self.nas

            if (child_yang_name == "origin"):
                if (self.origin is None):
                    self.origin = Aaa.Diameter.Origin()
                    self.origin.parent = self
                    self._children_name_map["origin"] = "origin"
                return self.origin

            if (child_yang_name == "peers"):
                if (self.peers is None):
                    self.peers = Aaa.Diameter.Peers()
                    self.peers.parent = self
                    self._children_name_map["peers"] = "peers"
                return self.peers

            if (child_yang_name == "vendor"):
                if (self.vendor is None):
                    self.vendor = Aaa.Diameter.Vendor()
                    self.vendor.parent = self
                    self._children_name_map["vendor"] = "vendor"
                return self.vendor

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "diameter-timer" or name == "diameter-tls" or name == "diams" or name == "gx" or name == "gy" or name == "nas" or name == "origin" or name == "peers" or name == "vendor" or name == "source-interface"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "source-interface"):
                self.source_interface = value
                self.source_interface.value_namespace = name_space
                self.source_interface.value_namespace_prefix = name_space_prefix


    class Radius(Entity):
        """
        Remote Access Dial\-In User Service
        
        .. attribute:: attributes
        
        	Table of attribute list
        	**type**\:   :py:class:`Attributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.Attributes>`
        
        .. attribute:: dead_criteria
        
        	RADIUS server dead criteria
        	**type**\:   :py:class:`DeadCriteria <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.DeadCriteria>`
        
        .. attribute:: dead_time
        
        	This indicates the length of time (in minutes) for which a RADIUS server remains marked as dead
        	**type**\:  int
        
        	**range:** 1..1440
        
        	**units**\: minute
        
        .. attribute:: disallow
        
        	disallow null\-username
        	**type**\:   :py:class:`Disallow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.Disallow>`
        
        .. attribute:: dynamic_authorization
        
        	RADIUS dynamic authorization
        	**type**\:   :py:class:`DynamicAuthorization <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.DynamicAuthorization>`
        
        .. attribute:: hosts
        
        	List of RADIUS servers
        	**type**\:   :py:class:`Hosts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.Hosts>`
        
        .. attribute:: idle_time
        
        	Idle time for RADIUS server
        	**type**\:  int
        
        	**range:** 1..1000
        
        	**default value**\: 5
        
        .. attribute:: ignore_accounting_port
        
        	Time to wait for a RADIUS server to reply
        	**type**\:  bool
        
        .. attribute:: ignore_auth_port
        
        	Time to wait for a RADIUS server to reply
        	**type**\:  bool
        
        .. attribute:: ipv4
        
        	IPv4 configuration
        	**type**\:   :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.Ipv4>`
        
        .. attribute:: ipv6
        
        	IPv6 configuration
        	**type**\:   :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.Ipv6>`
        
        .. attribute:: key
        
        	RADIUS encryption key
        	**type**\:  str
        
        	**pattern:** (!.+)\|([^!].+)
        
        .. attribute:: load_balance_options
        
        	Radius load\-balancing options
        	**type**\:   :py:class:`LoadBalanceOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.LoadBalanceOptions>`
        
        .. attribute:: radius_attribute
        
        	attribute
        	**type**\:   :py:class:`RadiusAttribute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.RadiusAttribute>`
        
        .. attribute:: retransmit
        
        	Number of times to retransmit a request to the RADIUS server(0\-Disable)
        	**type**\:  int
        
        	**range:** 0..100
        
        	**default value**\: 3
        
        .. attribute:: source_port
        
        	Source port
        	**type**\:   :py:class:`SourcePort <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.SourcePort>`
        
        .. attribute:: throttle
        
        	Radius throttling options
        	**type**\:   :py:class:`Throttle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.Throttle>`
        
        .. attribute:: timeout
        
        	Time to wait for a RADIUS server to reply
        	**type**\:  int
        
        	**range:** 1..1000
        
        	**default value**\: 5
        
        .. attribute:: username
        
        	Username to be tested for automated testing
        	**type**\:  str
        
        .. attribute:: vrfs
        
        	List of VRFs
        	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.Vrfs>`
        
        .. attribute:: vsa
        
        	Unknown VSA (Vendor Specific Attribute) ignore configuration for RADIUS server
        	**type**\:   :py:class:`Vsa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.Vsa>`
        
        

        """

        _prefix = 'aaa-protocol-radius-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Aaa.Radius, self).__init__()

            self.yang_name = "radius"
            self.yang_parent_name = "aaa"

            self.dead_time = YLeaf(YType.uint32, "dead-time")

            self.idle_time = YLeaf(YType.uint32, "idle-time")

            self.ignore_accounting_port = YLeaf(YType.boolean, "ignore-accounting-port")

            self.ignore_auth_port = YLeaf(YType.boolean, "ignore-auth-port")

            self.key = YLeaf(YType.str, "key")

            self.retransmit = YLeaf(YType.uint32, "retransmit")

            self.timeout = YLeaf(YType.uint32, "timeout")

            self.username = YLeaf(YType.str, "username")

            self.attributes = Aaa.Radius.Attributes()
            self.attributes.parent = self
            self._children_name_map["attributes"] = "attributes"
            self._children_yang_names.add("attributes")

            self.dead_criteria = Aaa.Radius.DeadCriteria()
            self.dead_criteria.parent = self
            self._children_name_map["dead_criteria"] = "dead-criteria"
            self._children_yang_names.add("dead-criteria")

            self.disallow = Aaa.Radius.Disallow()
            self.disallow.parent = self
            self._children_name_map["disallow"] = "disallow"
            self._children_yang_names.add("disallow")

            self.dynamic_authorization = Aaa.Radius.DynamicAuthorization()
            self.dynamic_authorization.parent = self
            self._children_name_map["dynamic_authorization"] = "dynamic-authorization"
            self._children_yang_names.add("dynamic-authorization")

            self.hosts = Aaa.Radius.Hosts()
            self.hosts.parent = self
            self._children_name_map["hosts"] = "hosts"
            self._children_yang_names.add("hosts")

            self.ipv4 = Aaa.Radius.Ipv4()
            self.ipv4.parent = self
            self._children_name_map["ipv4"] = "ipv4"
            self._children_yang_names.add("ipv4")

            self.ipv6 = Aaa.Radius.Ipv6()
            self.ipv6.parent = self
            self._children_name_map["ipv6"] = "ipv6"
            self._children_yang_names.add("ipv6")

            self.load_balance_options = Aaa.Radius.LoadBalanceOptions()
            self.load_balance_options.parent = self
            self._children_name_map["load_balance_options"] = "load-balance-options"
            self._children_yang_names.add("load-balance-options")

            self.radius_attribute = Aaa.Radius.RadiusAttribute()
            self.radius_attribute.parent = self
            self._children_name_map["radius_attribute"] = "radius-attribute"
            self._children_yang_names.add("radius-attribute")

            self.source_port = Aaa.Radius.SourcePort()
            self.source_port.parent = self
            self._children_name_map["source_port"] = "source-port"
            self._children_yang_names.add("source-port")

            self.throttle = Aaa.Radius.Throttle()
            self.throttle.parent = self
            self._children_name_map["throttle"] = "throttle"
            self._children_yang_names.add("throttle")

            self.vrfs = Aaa.Radius.Vrfs()
            self.vrfs.parent = self
            self._children_name_map["vrfs"] = "vrfs"
            self._children_yang_names.add("vrfs")

            self.vsa = Aaa.Radius.Vsa()
            self.vsa.parent = self
            self._children_name_map["vsa"] = "vsa"
            self._children_yang_names.add("vsa")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("dead_time",
                            "idle_time",
                            "ignore_accounting_port",
                            "ignore_auth_port",
                            "key",
                            "retransmit",
                            "timeout",
                            "username") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Aaa.Radius, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Aaa.Radius, self).__setattr__(name, value)


        class Hosts(Entity):
            """
            List of RADIUS servers
            
            .. attribute:: host
            
            	Instance of a RADIUS server
            	**type**\: list of    :py:class:`Host <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.Hosts.Host>`
            
            

            """

            _prefix = 'aaa-protocol-radius-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Radius.Hosts, self).__init__()

                self.yang_name = "hosts"
                self.yang_parent_name = "radius"

                self.host = YList(self)

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
                            super(Aaa.Radius.Hosts, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Aaa.Radius.Hosts, self).__setattr__(name, value)


            class Host(Entity):
                """
                Instance of a RADIUS server
                
                .. attribute:: ordering_index  <key>
                
                	This is used to sort the servers in the order of precedence
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: ip_address  <key>
                
                	IP address of RADIUS server
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                
                ----
                .. attribute:: auth_port_number  <key>
                
                	Authentication Port number (standard port 1645)
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: acct_port_number  <key>
                
                	Accounting Port number (standard port 1646)
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: host_key
                
                	RADIUS encryption key
                	**type**\:  str
                
                	**pattern:** (!.+)\|([^!].+)
                
                .. attribute:: host_retransmit
                
                	Number of times to retransmit a request to the RADIUS server
                	**type**\:  int
                
                	**range:** 1..100
                
                	**default value**\: 3
                
                .. attribute:: host_timeout
                
                	Time to wait for a RADIUS server to reply
                	**type**\:  int
                
                	**range:** 1..1000
                
                	**default value**\: 5
                
                .. attribute:: idle_time
                
                	Idle time for RADIUS server
                	**type**\:  int
                
                	**range:** 1..1000
                
                	**default value**\: 5
                
                .. attribute:: ignore_accounting_port
                
                	Time to wait for a RADIUS server to reply
                	**type**\:  bool
                
                .. attribute:: ignore_auth_port
                
                	Time to wait for a RADIUS server to reply
                	**type**\:  bool
                
                .. attribute:: username
                
                	Username to be tested for automated testing
                	**type**\:  str
                
                

                """

                _prefix = 'aaa-protocol-radius-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.Radius.Hosts.Host, self).__init__()

                    self.yang_name = "host"
                    self.yang_parent_name = "hosts"

                    self.ordering_index = YLeaf(YType.int32, "ordering-index")

                    self.ip_address = YLeaf(YType.str, "ip-address")

                    self.auth_port_number = YLeaf(YType.uint16, "auth-port-number")

                    self.acct_port_number = YLeaf(YType.uint16, "acct-port-number")

                    self.host_key = YLeaf(YType.str, "host-key")

                    self.host_retransmit = YLeaf(YType.uint32, "host-retransmit")

                    self.host_timeout = YLeaf(YType.uint32, "host-timeout")

                    self.idle_time = YLeaf(YType.uint32, "idle-time")

                    self.ignore_accounting_port = YLeaf(YType.boolean, "ignore-accounting-port")

                    self.ignore_auth_port = YLeaf(YType.boolean, "ignore-auth-port")

                    self.username = YLeaf(YType.str, "username")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("ordering_index",
                                    "ip_address",
                                    "auth_port_number",
                                    "acct_port_number",
                                    "host_key",
                                    "host_retransmit",
                                    "host_timeout",
                                    "idle_time",
                                    "ignore_accounting_port",
                                    "ignore_auth_port",
                                    "username") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Aaa.Radius.Hosts.Host, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Aaa.Radius.Hosts.Host, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.ordering_index.is_set or
                        self.ip_address.is_set or
                        self.auth_port_number.is_set or
                        self.acct_port_number.is_set or
                        self.host_key.is_set or
                        self.host_retransmit.is_set or
                        self.host_timeout.is_set or
                        self.idle_time.is_set or
                        self.ignore_accounting_port.is_set or
                        self.ignore_auth_port.is_set or
                        self.username.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.ordering_index.yfilter != YFilter.not_set or
                        self.ip_address.yfilter != YFilter.not_set or
                        self.auth_port_number.yfilter != YFilter.not_set or
                        self.acct_port_number.yfilter != YFilter.not_set or
                        self.host_key.yfilter != YFilter.not_set or
                        self.host_retransmit.yfilter != YFilter.not_set or
                        self.host_timeout.yfilter != YFilter.not_set or
                        self.idle_time.yfilter != YFilter.not_set or
                        self.ignore_accounting_port.yfilter != YFilter.not_set or
                        self.ignore_auth_port.yfilter != YFilter.not_set or
                        self.username.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "host" + "[ordering-index='" + self.ordering_index.get() + "']" + "[ip-address='" + self.ip_address.get() + "']" + "[auth-port-number='" + self.auth_port_number.get() + "']" + "[acct-port-number='" + self.acct_port_number.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/hosts/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.ordering_index.is_set or self.ordering_index.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ordering_index.get_name_leafdata())
                    if (self.ip_address.is_set or self.ip_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ip_address.get_name_leafdata())
                    if (self.auth_port_number.is_set or self.auth_port_number.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.auth_port_number.get_name_leafdata())
                    if (self.acct_port_number.is_set or self.acct_port_number.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.acct_port_number.get_name_leafdata())
                    if (self.host_key.is_set or self.host_key.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.host_key.get_name_leafdata())
                    if (self.host_retransmit.is_set or self.host_retransmit.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.host_retransmit.get_name_leafdata())
                    if (self.host_timeout.is_set or self.host_timeout.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.host_timeout.get_name_leafdata())
                    if (self.idle_time.is_set or self.idle_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.idle_time.get_name_leafdata())
                    if (self.ignore_accounting_port.is_set or self.ignore_accounting_port.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ignore_accounting_port.get_name_leafdata())
                    if (self.ignore_auth_port.is_set or self.ignore_auth_port.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ignore_auth_port.get_name_leafdata())
                    if (self.username.is_set or self.username.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.username.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "ordering-index" or name == "ip-address" or name == "auth-port-number" or name == "acct-port-number" or name == "host-key" or name == "host-retransmit" or name == "host-timeout" or name == "idle-time" or name == "ignore-accounting-port" or name == "ignore-auth-port" or name == "username"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "ordering-index"):
                        self.ordering_index = value
                        self.ordering_index.value_namespace = name_space
                        self.ordering_index.value_namespace_prefix = name_space_prefix
                    if(value_path == "ip-address"):
                        self.ip_address = value
                        self.ip_address.value_namespace = name_space
                        self.ip_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "auth-port-number"):
                        self.auth_port_number = value
                        self.auth_port_number.value_namespace = name_space
                        self.auth_port_number.value_namespace_prefix = name_space_prefix
                    if(value_path == "acct-port-number"):
                        self.acct_port_number = value
                        self.acct_port_number.value_namespace = name_space
                        self.acct_port_number.value_namespace_prefix = name_space_prefix
                    if(value_path == "host-key"):
                        self.host_key = value
                        self.host_key.value_namespace = name_space
                        self.host_key.value_namespace_prefix = name_space_prefix
                    if(value_path == "host-retransmit"):
                        self.host_retransmit = value
                        self.host_retransmit.value_namespace = name_space
                        self.host_retransmit.value_namespace_prefix = name_space_prefix
                    if(value_path == "host-timeout"):
                        self.host_timeout = value
                        self.host_timeout.value_namespace = name_space
                        self.host_timeout.value_namespace_prefix = name_space_prefix
                    if(value_path == "idle-time"):
                        self.idle_time = value
                        self.idle_time.value_namespace = name_space
                        self.idle_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "ignore-accounting-port"):
                        self.ignore_accounting_port = value
                        self.ignore_accounting_port.value_namespace = name_space
                        self.ignore_accounting_port.value_namespace_prefix = name_space_prefix
                    if(value_path == "ignore-auth-port"):
                        self.ignore_auth_port = value
                        self.ignore_auth_port.value_namespace = name_space
                        self.ignore_auth_port.value_namespace_prefix = name_space_prefix
                    if(value_path == "username"):
                        self.username = value
                        self.username.value_namespace = name_space
                        self.username.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.host:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.host:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "hosts" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "host"):
                    for c in self.host:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Aaa.Radius.Hosts.Host()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.host.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "host"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class DeadCriteria(Entity):
            """
            RADIUS server dead criteria
            
            .. attribute:: time
            
            	The minimum amount of time which must elapse since the router last received a valid RADIUS packet from the server prior to marking it dead
            	**type**\:  int
            
            	**range:** 1..120
            
            .. attribute:: tries
            
            	The number of consecutive timeouts the router must experience in order to mark the server as dead. All transmissions, including the initial transmit and all retransmits, will be counted
            	**type**\:  int
            
            	**range:** 1..100
            
            

            """

            _prefix = 'aaa-protocol-radius-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Radius.DeadCriteria, self).__init__()

                self.yang_name = "dead-criteria"
                self.yang_parent_name = "radius"

                self.time = YLeaf(YType.uint32, "time")

                self.tries = YLeaf(YType.uint32, "tries")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("time",
                                "tries") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Aaa.Radius.DeadCriteria, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Aaa.Radius.DeadCriteria, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.time.is_set or
                    self.tries.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.time.yfilter != YFilter.not_set or
                    self.tries.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "dead-criteria" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.time.is_set or self.time.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.time.get_name_leafdata())
                if (self.tries.is_set or self.tries.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tries.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "time" or name == "tries"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "time"):
                    self.time = value
                    self.time.value_namespace = name_space
                    self.time.value_namespace_prefix = name_space_prefix
                if(value_path == "tries"):
                    self.tries = value
                    self.tries.value_namespace = name_space
                    self.tries.value_namespace_prefix = name_space_prefix


        class Disallow(Entity):
            """
            disallow null\-username
            
            .. attribute:: null_username
            
            	Disallow null\-username
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            

            """

            _prefix = 'aaa-protocol-radius-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Radius.Disallow, self).__init__()

                self.yang_name = "disallow"
                self.yang_parent_name = "radius"

                self.null_username = YLeaf(YType.int32, "null-username")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("null_username") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Aaa.Radius.Disallow, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Aaa.Radius.Disallow, self).__setattr__(name, value)

            def has_data(self):
                return self.null_username.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.null_username.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "disallow" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.null_username.is_set or self.null_username.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.null_username.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "null-username"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "null-username"):
                    self.null_username = value
                    self.null_username.value_namespace = name_space
                    self.null_username.value_namespace_prefix = name_space_prefix


        class Ipv6(Entity):
            """
            IPv6 configuration
            
            .. attribute:: dscp
            
            	Specify the DSCP value
            	**type**\: one of the below types:
            
            	**type**\:   :py:class:`AaaDscpValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg.AaaDscpValue>`
            
            
            ----
            	**type**\:  int
            
            	**range:** 0..63
            
            
            ----
            

            """

            _prefix = 'aaa-protocol-radius-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Radius.Ipv6, self).__init__()

                self.yang_name = "ipv6"
                self.yang_parent_name = "radius"

                self.dscp = YLeaf(YType.str, "dscp")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("dscp") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Aaa.Radius.Ipv6, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Aaa.Radius.Ipv6, self).__setattr__(name, value)

            def has_data(self):
                return self.dscp.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.dscp.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ipv6" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.dscp.is_set or self.dscp.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dscp.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "dscp"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "dscp"):
                    self.dscp = value
                    self.dscp.value_namespace = name_space
                    self.dscp.value_namespace_prefix = name_space_prefix


        class DynamicAuthorization(Entity):
            """
            RADIUS dynamic authorization
            
            .. attribute:: authentication_type
            
            	RADIUS  dynamic  authorization  type
            	**type**\:   :py:class:`AaaAuthentication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg.AaaAuthentication>`
            
            .. attribute:: clients
            
            	Client data
            	**type**\:   :py:class:`Clients <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.DynamicAuthorization.Clients>`
            
            .. attribute:: ignore
            
            	Ignore option for server key or session key
            	**type**\:   :py:class:`AaaSelectKey <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg.AaaSelectKey>`
            
            .. attribute:: port
            
            	Specify the COA server port to listen on
            	**type**\:  int
            
            	**range:** 1000..5000
            
            .. attribute:: server_key
            
            	RADIUS CoA client encryption key
            	**type**\:  str
            
            	**pattern:** (!.+)\|([^!].+)
            
            

            """

            _prefix = 'aaa-protocol-radius-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Radius.DynamicAuthorization, self).__init__()

                self.yang_name = "dynamic-authorization"
                self.yang_parent_name = "radius"

                self.authentication_type = YLeaf(YType.enumeration, "authentication-type")

                self.ignore = YLeaf(YType.enumeration, "ignore")

                self.port = YLeaf(YType.uint32, "port")

                self.server_key = YLeaf(YType.str, "server-key")

                self.clients = Aaa.Radius.DynamicAuthorization.Clients()
                self.clients.parent = self
                self._children_name_map["clients"] = "clients"
                self._children_yang_names.add("clients")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("authentication_type",
                                "ignore",
                                "port",
                                "server_key") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Aaa.Radius.DynamicAuthorization, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Aaa.Radius.DynamicAuthorization, self).__setattr__(name, value)


            class Clients(Entity):
                """
                Client data
                
                .. attribute:: client
                
                	Client data
                	**type**\: list of    :py:class:`Client <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.DynamicAuthorization.Clients.Client>`
                
                .. attribute:: client_vrf_name
                
                	Client data
                	**type**\: list of    :py:class:`ClientVrfName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.DynamicAuthorization.Clients.ClientVrfName>`
                
                

                """

                _prefix = 'aaa-protocol-radius-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.Radius.DynamicAuthorization.Clients, self).__init__()

                    self.yang_name = "clients"
                    self.yang_parent_name = "dynamic-authorization"

                    self.client = YList(self)
                    self.client_vrf_name = YList(self)

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
                                super(Aaa.Radius.DynamicAuthorization.Clients, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Aaa.Radius.DynamicAuthorization.Clients, self).__setattr__(name, value)


                class Client(Entity):
                    """
                    Client data
                    
                    .. attribute:: ip_address  <key>
                    
                    	IP address of COA client
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    .. attribute:: server_key
                    
                    	RADIUS CoA client encryption key
                    	**type**\:  str
                    
                    	**pattern:** (!.+)\|([^!].+)
                    
                    

                    """

                    _prefix = 'aaa-protocol-radius-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Aaa.Radius.DynamicAuthorization.Clients.Client, self).__init__()

                        self.yang_name = "client"
                        self.yang_parent_name = "clients"

                        self.ip_address = YLeaf(YType.str, "ip-address")

                        self.server_key = YLeaf(YType.str, "server-key")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("ip_address",
                                        "server_key") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Aaa.Radius.DynamicAuthorization.Clients.Client, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Aaa.Radius.DynamicAuthorization.Clients.Client, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.ip_address.is_set or
                            self.server_key.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.ip_address.yfilter != YFilter.not_set or
                            self.server_key.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "client" + "[ip-address='" + self.ip_address.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/dynamic-authorization/clients/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.ip_address.is_set or self.ip_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ip_address.get_name_leafdata())
                        if (self.server_key.is_set or self.server_key.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.server_key.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "ip-address" or name == "server-key"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "ip-address"):
                            self.ip_address = value
                            self.ip_address.value_namespace = name_space
                            self.ip_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "server-key"):
                            self.server_key = value
                            self.server_key.value_namespace = name_space
                            self.server_key.value_namespace_prefix = name_space_prefix


                class ClientVrfName(Entity):
                    """
                    Client data
                    
                    .. attribute:: vrf_name  <key>
                    
                    	VRF name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: ip_address  <key>
                    
                    	IP address of COA client
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    .. attribute:: server_key
                    
                    	RADIUS CoA client encryption key
                    	**type**\:  str
                    
                    	**pattern:** (!.+)\|([^!].+)
                    
                    

                    """

                    _prefix = 'aaa-protocol-radius-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Aaa.Radius.DynamicAuthorization.Clients.ClientVrfName, self).__init__()

                        self.yang_name = "client-vrf-name"
                        self.yang_parent_name = "clients"

                        self.vrf_name = YLeaf(YType.str, "vrf-name")

                        self.ip_address = YLeaf(YType.str, "ip-address")

                        self.server_key = YLeaf(YType.str, "server-key")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("vrf_name",
                                        "ip_address",
                                        "server_key") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Aaa.Radius.DynamicAuthorization.Clients.ClientVrfName, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Aaa.Radius.DynamicAuthorization.Clients.ClientVrfName, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.vrf_name.is_set or
                            self.ip_address.is_set or
                            self.server_key.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.vrf_name.yfilter != YFilter.not_set or
                            self.ip_address.yfilter != YFilter.not_set or
                            self.server_key.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "client-vrf-name" + "[vrf-name='" + self.vrf_name.get() + "']" + "[ip-address='" + self.ip_address.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/dynamic-authorization/clients/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vrf_name.get_name_leafdata())
                        if (self.ip_address.is_set or self.ip_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ip_address.get_name_leafdata())
                        if (self.server_key.is_set or self.server_key.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.server_key.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "vrf-name" or name == "ip-address" or name == "server-key"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "vrf-name"):
                            self.vrf_name = value
                            self.vrf_name.value_namespace = name_space
                            self.vrf_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "ip-address"):
                            self.ip_address = value
                            self.ip_address.value_namespace = name_space
                            self.ip_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "server-key"):
                            self.server_key = value
                            self.server_key.value_namespace = name_space
                            self.server_key.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.client:
                        if (c.has_data()):
                            return True
                    for c in self.client_vrf_name:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.client:
                        if (c.has_operation()):
                            return True
                    for c in self.client_vrf_name:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "clients" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/dynamic-authorization/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "client"):
                        for c in self.client:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Aaa.Radius.DynamicAuthorization.Clients.Client()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.client.append(c)
                        return c

                    if (child_yang_name == "client-vrf-name"):
                        for c in self.client_vrf_name:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Aaa.Radius.DynamicAuthorization.Clients.ClientVrfName()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.client_vrf_name.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "client" or name == "client-vrf-name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.authentication_type.is_set or
                    self.ignore.is_set or
                    self.port.is_set or
                    self.server_key.is_set or
                    (self.clients is not None and self.clients.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.authentication_type.yfilter != YFilter.not_set or
                    self.ignore.yfilter != YFilter.not_set or
                    self.port.yfilter != YFilter.not_set or
                    self.server_key.yfilter != YFilter.not_set or
                    (self.clients is not None and self.clients.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "dynamic-authorization" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.authentication_type.is_set or self.authentication_type.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.authentication_type.get_name_leafdata())
                if (self.ignore.is_set or self.ignore.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ignore.get_name_leafdata())
                if (self.port.is_set or self.port.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.port.get_name_leafdata())
                if (self.server_key.is_set or self.server_key.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.server_key.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "clients"):
                    if (self.clients is None):
                        self.clients = Aaa.Radius.DynamicAuthorization.Clients()
                        self.clients.parent = self
                        self._children_name_map["clients"] = "clients"
                    return self.clients

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "clients" or name == "authentication-type" or name == "ignore" or name == "port" or name == "server-key"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "authentication-type"):
                    self.authentication_type = value
                    self.authentication_type.value_namespace = name_space
                    self.authentication_type.value_namespace_prefix = name_space_prefix
                if(value_path == "ignore"):
                    self.ignore = value
                    self.ignore.value_namespace = name_space
                    self.ignore.value_namespace_prefix = name_space_prefix
                if(value_path == "port"):
                    self.port = value
                    self.port.value_namespace = name_space
                    self.port.value_namespace_prefix = name_space_prefix
                if(value_path == "server-key"):
                    self.server_key = value
                    self.server_key.value_namespace = name_space
                    self.server_key.value_namespace_prefix = name_space_prefix


        class LoadBalanceOptions(Entity):
            """
            Radius load\-balancing options
            
            .. attribute:: load_balance_method
            
            	Method by which the next host will be picked
            	**type**\:   :py:class:`LoadBalanceMethod <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.LoadBalanceOptions.LoadBalanceMethod>`
            
            

            """

            _prefix = 'aaa-protocol-radius-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Radius.LoadBalanceOptions, self).__init__()

                self.yang_name = "load-balance-options"
                self.yang_parent_name = "radius"

                self.load_balance_method = Aaa.Radius.LoadBalanceOptions.LoadBalanceMethod()
                self.load_balance_method.parent = self
                self._children_name_map["load_balance_method"] = "load-balance-method"
                self._children_yang_names.add("load-balance-method")


            class LoadBalanceMethod(Entity):
                """
                Method by which the next host will be picked
                
                .. attribute:: batch_size
                
                	Batch size for selection of the server
                	**type**\:   :py:class:`BatchSize <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.LoadBalanceOptions.LoadBalanceMethod.BatchSize>`
                
                

                """

                _prefix = 'aaa-protocol-radius-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.Radius.LoadBalanceOptions.LoadBalanceMethod, self).__init__()

                    self.yang_name = "load-balance-method"
                    self.yang_parent_name = "load-balance-options"

                    self.batch_size = Aaa.Radius.LoadBalanceOptions.LoadBalanceMethod.BatchSize()
                    self.batch_size.parent = self
                    self._children_name_map["batch_size"] = "batch-size"
                    self._children_yang_names.add("batch-size")


                class BatchSize(Entity):
                    """
                    Batch size for selection of the server
                    
                    .. attribute:: batch_size
                    
                    	Batch size for selection of the server
                    	**type**\:  int
                    
                    	**range:** 1..1500
                    
                    	**default value**\: 25
                    
                    .. attribute:: ignore_preferred_server
                    
                    	Disable preferred server for this Server Group
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**default value**\: 1
                    
                    

                    """

                    _prefix = 'aaa-protocol-radius-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Aaa.Radius.LoadBalanceOptions.LoadBalanceMethod.BatchSize, self).__init__()

                        self.yang_name = "batch-size"
                        self.yang_parent_name = "load-balance-method"

                        self.batch_size = YLeaf(YType.uint32, "batch-size")

                        self.ignore_preferred_server = YLeaf(YType.int32, "ignore-preferred-server")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("batch_size",
                                        "ignore_preferred_server") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Aaa.Radius.LoadBalanceOptions.LoadBalanceMethod.BatchSize, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Aaa.Radius.LoadBalanceOptions.LoadBalanceMethod.BatchSize, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.batch_size.is_set or
                            self.ignore_preferred_server.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.batch_size.yfilter != YFilter.not_set or
                            self.ignore_preferred_server.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "batch-size" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/load-balance-options/load-balance-method/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.batch_size.is_set or self.batch_size.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.batch_size.get_name_leafdata())
                        if (self.ignore_preferred_server.is_set or self.ignore_preferred_server.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ignore_preferred_server.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "batch-size" or name == "ignore-preferred-server"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "batch-size"):
                            self.batch_size = value
                            self.batch_size.value_namespace = name_space
                            self.batch_size.value_namespace_prefix = name_space_prefix
                        if(value_path == "ignore-preferred-server"):
                            self.ignore_preferred_server = value
                            self.ignore_preferred_server.value_namespace = name_space
                            self.ignore_preferred_server.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (self.batch_size is not None and self.batch_size.has_data())

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.batch_size is not None and self.batch_size.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "load-balance-method" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/load-balance-options/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "batch-size"):
                        if (self.batch_size is None):
                            self.batch_size = Aaa.Radius.LoadBalanceOptions.LoadBalanceMethod.BatchSize()
                            self.batch_size.parent = self
                            self._children_name_map["batch_size"] = "batch-size"
                        return self.batch_size

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "batch-size"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (self.load_balance_method is not None and self.load_balance_method.has_data())

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.load_balance_method is not None and self.load_balance_method.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "load-balance-options" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "load-balance-method"):
                    if (self.load_balance_method is None):
                        self.load_balance_method = Aaa.Radius.LoadBalanceOptions.LoadBalanceMethod()
                        self.load_balance_method.parent = self
                        self._children_name_map["load_balance_method"] = "load-balance-method"
                    return self.load_balance_method

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "load-balance-method"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class Vrfs(Entity):
            """
            List of VRFs
            
            .. attribute:: vrf
            
            	A VRF
            	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.Vrfs.Vrf>`
            
            

            """

            _prefix = 'aaa-protocol-radius-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Radius.Vrfs, self).__init__()

                self.yang_name = "vrfs"
                self.yang_parent_name = "radius"

                self.vrf = YList(self)

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
                            super(Aaa.Radius.Vrfs, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Aaa.Radius.Vrfs, self).__setattr__(name, value)


            class Vrf(Entity):
                """
                A VRF
                
                .. attribute:: vrf_name  <key>
                
                	VRF name. Specify 'default' for defalut VRF
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: source_interface
                
                	Specify interface for source address in RADIUS packets
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                

                """

                _prefix = 'aaa-protocol-radius-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.Radius.Vrfs.Vrf, self).__init__()

                    self.yang_name = "vrf"
                    self.yang_parent_name = "vrfs"

                    self.vrf_name = YLeaf(YType.str, "vrf-name")

                    self.source_interface = YLeaf(YType.str, "source-interface")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("vrf_name",
                                    "source_interface") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Aaa.Radius.Vrfs.Vrf, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Aaa.Radius.Vrfs.Vrf, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.vrf_name.is_set or
                        self.source_interface.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.vrf_name.yfilter != YFilter.not_set or
                        self.source_interface.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "vrf" + "[vrf-name='" + self.vrf_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/vrfs/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.vrf_name.get_name_leafdata())
                    if (self.source_interface.is_set or self.source_interface.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.source_interface.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "vrf-name" or name == "source-interface"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "vrf-name"):
                        self.vrf_name = value
                        self.vrf_name.value_namespace = name_space
                        self.vrf_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "source-interface"):
                        self.source_interface = value
                        self.source_interface.value_namespace = name_space
                        self.source_interface.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.vrf:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.vrf:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "vrfs" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "vrf"):
                    for c in self.vrf:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Aaa.Radius.Vrfs.Vrf()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.vrf.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "vrf"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class Throttle(Entity):
            """
            Radius throttling options
            
            .. attribute:: access
            
            	To flow control the number of access requests sent to a radius server
            	**type**\:  int
            
            	**range:** 0..65535
            
            	**default value**\: 0
            
            .. attribute:: access_timeout
            
            	Specify the number of timeouts exceeding which a throttled access request is dropped
            	**type**\:  int
            
            	**range:** 1..10
            
            	**default value**\: 3
            
            .. attribute:: accounting
            
            	To flow control the number of accounting requests sent to a radius server
            	**type**\:  int
            
            	**range:** 0..65535
            
            	**default value**\: 0
            
            

            """

            _prefix = 'aaa-protocol-radius-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Radius.Throttle, self).__init__()

                self.yang_name = "throttle"
                self.yang_parent_name = "radius"

                self.access = YLeaf(YType.uint32, "access")

                self.access_timeout = YLeaf(YType.uint32, "access-timeout")

                self.accounting = YLeaf(YType.uint32, "accounting")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("access",
                                "access_timeout",
                                "accounting") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Aaa.Radius.Throttle, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Aaa.Radius.Throttle, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.access.is_set or
                    self.access_timeout.is_set or
                    self.accounting.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.access.yfilter != YFilter.not_set or
                    self.access_timeout.yfilter != YFilter.not_set or
                    self.accounting.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "throttle" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.access.is_set or self.access.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.access.get_name_leafdata())
                if (self.access_timeout.is_set or self.access_timeout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.access_timeout.get_name_leafdata())
                if (self.accounting.is_set or self.accounting.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.accounting.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "access" or name == "access-timeout" or name == "accounting"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "access"):
                    self.access = value
                    self.access.value_namespace = name_space
                    self.access.value_namespace_prefix = name_space_prefix
                if(value_path == "access-timeout"):
                    self.access_timeout = value
                    self.access_timeout.value_namespace = name_space
                    self.access_timeout.value_namespace_prefix = name_space_prefix
                if(value_path == "accounting"):
                    self.accounting = value
                    self.accounting.value_namespace = name_space
                    self.accounting.value_namespace_prefix = name_space_prefix


        class Vsa(Entity):
            """
            Unknown VSA (Vendor Specific Attribute) ignore
            configuration for RADIUS server
            
            .. attribute:: attribute
            
            	Vendor Specific Attribute
            	**type**\:   :py:class:`Attribute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.Vsa.Attribute>`
            
            

            """

            _prefix = 'aaa-protocol-radius-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Radius.Vsa, self).__init__()

                self.yang_name = "vsa"
                self.yang_parent_name = "radius"

                self.attribute = Aaa.Radius.Vsa.Attribute()
                self.attribute.parent = self
                self._children_name_map["attribute"] = "attribute"
                self._children_yang_names.add("attribute")


            class Attribute(Entity):
                """
                Vendor Specific Attribute
                
                .. attribute:: ignore
                
                	Ignore the VSA
                	**type**\:   :py:class:`Ignore <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.Vsa.Attribute.Ignore>`
                
                

                """

                _prefix = 'aaa-protocol-radius-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.Radius.Vsa.Attribute, self).__init__()

                    self.yang_name = "attribute"
                    self.yang_parent_name = "vsa"

                    self.ignore = Aaa.Radius.Vsa.Attribute.Ignore()
                    self.ignore.parent = self
                    self._children_name_map["ignore"] = "ignore"
                    self._children_yang_names.add("ignore")


                class Ignore(Entity):
                    """
                    Ignore the VSA
                    
                    .. attribute:: unknown
                    
                    	Ignore the VSA and no prefix will reject the unknown VSA
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'aaa-protocol-radius-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Aaa.Radius.Vsa.Attribute.Ignore, self).__init__()

                        self.yang_name = "ignore"
                        self.yang_parent_name = "attribute"

                        self.unknown = YLeaf(YType.empty, "unknown")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("unknown") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Aaa.Radius.Vsa.Attribute.Ignore, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Aaa.Radius.Vsa.Attribute.Ignore, self).__setattr__(name, value)

                    def has_data(self):
                        return self.unknown.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.unknown.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ignore" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/vsa/attribute/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.unknown.is_set or self.unknown.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.unknown.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "unknown"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "unknown"):
                            self.unknown = value
                            self.unknown.value_namespace = name_space
                            self.unknown.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (self.ignore is not None and self.ignore.has_data())

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.ignore is not None and self.ignore.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "attribute" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/vsa/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "ignore"):
                        if (self.ignore is None):
                            self.ignore = Aaa.Radius.Vsa.Attribute.Ignore()
                            self.ignore.parent = self
                            self._children_name_map["ignore"] = "ignore"
                        return self.ignore

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "ignore"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (self.attribute is not None and self.attribute.has_data())

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.attribute is not None and self.attribute.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "vsa" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "attribute"):
                    if (self.attribute is None):
                        self.attribute = Aaa.Radius.Vsa.Attribute()
                        self.attribute.parent = self
                        self._children_name_map["attribute"] = "attribute"
                    return self.attribute

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "attribute"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class Ipv4(Entity):
            """
            IPv4 configuration
            
            .. attribute:: dscp
            
            	Specify the DSCP value
            	**type**\: one of the below types:
            
            	**type**\:   :py:class:`AaaDscpValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg.AaaDscpValue>`
            
            
            ----
            	**type**\:  int
            
            	**range:** 0..63
            
            
            ----
            

            """

            _prefix = 'aaa-protocol-radius-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Radius.Ipv4, self).__init__()

                self.yang_name = "ipv4"
                self.yang_parent_name = "radius"

                self.dscp = YLeaf(YType.str, "dscp")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("dscp") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Aaa.Radius.Ipv4, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Aaa.Radius.Ipv4, self).__setattr__(name, value)

            def has_data(self):
                return self.dscp.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.dscp.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ipv4" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.dscp.is_set or self.dscp.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dscp.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "dscp"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "dscp"):
                    self.dscp = value
                    self.dscp.value_namespace = name_space
                    self.dscp.value_namespace_prefix = name_space_prefix


        class RadiusAttribute(Entity):
            """
            attribute
            
            .. attribute:: acct_multi_session_id
            
            	Acct\-Session\-Id attribute(44)
            	**type**\:   :py:class:`AcctMultiSessionId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.RadiusAttribute.AcctMultiSessionId>`
            
            .. attribute:: acct_session_id
            
            	Acct\-Session\-Id attribute(44)
            	**type**\:   :py:class:`AcctSessionId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.RadiusAttribute.AcctSessionId>`
            
            .. attribute:: filter_id_11
            
            	Filter\-Id attribute configuration
            	**type**\:   :py:class:`FilterId11 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.RadiusAttribute.FilterId11>`
            
            

            """

            _prefix = 'aaa-protocol-radius-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Radius.RadiusAttribute, self).__init__()

                self.yang_name = "radius-attribute"
                self.yang_parent_name = "radius"

                self.acct_multi_session_id = Aaa.Radius.RadiusAttribute.AcctMultiSessionId()
                self.acct_multi_session_id.parent = self
                self._children_name_map["acct_multi_session_id"] = "acct-multi-session-id"
                self._children_yang_names.add("acct-multi-session-id")

                self.acct_session_id = Aaa.Radius.RadiusAttribute.AcctSessionId()
                self.acct_session_id.parent = self
                self._children_name_map["acct_session_id"] = "acct-session-id"
                self._children_yang_names.add("acct-session-id")

                self.filter_id_11 = Aaa.Radius.RadiusAttribute.FilterId11()
                self.filter_id_11.parent = self
                self._children_name_map["filter_id_11"] = "filter-id-11"
                self._children_yang_names.add("filter-id-11")


            class FilterId11(Entity):
                """
                Filter\-Id attribute configuration
                
                .. attribute:: defaults
                
                	Set the attribute default direction
                	**type**\:   :py:class:`Defaults <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.RadiusAttribute.FilterId11.Defaults>`
                
                

                """

                _prefix = 'aaa-protocol-radius-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.Radius.RadiusAttribute.FilterId11, self).__init__()

                    self.yang_name = "filter-id-11"
                    self.yang_parent_name = "radius-attribute"

                    self.defaults = Aaa.Radius.RadiusAttribute.FilterId11.Defaults()
                    self.defaults.parent = self
                    self._children_name_map["defaults"] = "defaults"
                    self._children_yang_names.add("defaults")


                class Defaults(Entity):
                    """
                    Set the attribute default direction
                    
                    .. attribute:: direction
                    
                    	Filtering is applied to ingress(inbound)/egress(outbound) packets only
                    	**type**\:   :py:class:`AaaDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg.AaaDirection>`
                    
                    

                    """

                    _prefix = 'aaa-protocol-radius-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Aaa.Radius.RadiusAttribute.FilterId11.Defaults, self).__init__()

                        self.yang_name = "defaults"
                        self.yang_parent_name = "filter-id-11"

                        self.direction = YLeaf(YType.enumeration, "direction")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("direction") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Aaa.Radius.RadiusAttribute.FilterId11.Defaults, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Aaa.Radius.RadiusAttribute.FilterId11.Defaults, self).__setattr__(name, value)

                    def has_data(self):
                        return self.direction.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.direction.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "defaults" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/radius-attribute/filter-id-11/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.direction.is_set or self.direction.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.direction.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "direction"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "direction"):
                            self.direction = value
                            self.direction.value_namespace = name_space
                            self.direction.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (self.defaults is not None and self.defaults.has_data())

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.defaults is not None and self.defaults.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "filter-id-11" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/radius-attribute/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "defaults"):
                        if (self.defaults is None):
                            self.defaults = Aaa.Radius.RadiusAttribute.FilterId11.Defaults()
                            self.defaults.parent = self
                            self._children_name_map["defaults"] = "defaults"
                        return self.defaults

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "defaults"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class AcctMultiSessionId(Entity):
                """
                Acct\-Session\-Id attribute(44)
                
                .. attribute:: include_parent_session_id
                
                	Prepend Acct\-Session\-Id attribute with Nas\-Port\-Id
                	**type**\:   :py:class:`IncludeParentSessionId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.RadiusAttribute.AcctMultiSessionId.IncludeParentSessionId>`
                
                

                """

                _prefix = 'aaa-protocol-radius-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.Radius.RadiusAttribute.AcctMultiSessionId, self).__init__()

                    self.yang_name = "acct-multi-session-id"
                    self.yang_parent_name = "radius-attribute"

                    self.include_parent_session_id = Aaa.Radius.RadiusAttribute.AcctMultiSessionId.IncludeParentSessionId()
                    self.include_parent_session_id.parent = self
                    self._children_name_map["include_parent_session_id"] = "include-parent-session-id"
                    self._children_yang_names.add("include-parent-session-id")


                class IncludeParentSessionId(Entity):
                    """
                    Prepend Acct\-Session\-Id attribute with
                    Nas\-Port\-Id
                    
                    .. attribute:: config
                    
                    	false/true
                    	**type**\:   :py:class:`AaaConfig <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg.AaaConfig>`
                    
                    

                    """

                    _prefix = 'aaa-protocol-radius-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Aaa.Radius.RadiusAttribute.AcctMultiSessionId.IncludeParentSessionId, self).__init__()

                        self.yang_name = "include-parent-session-id"
                        self.yang_parent_name = "acct-multi-session-id"

                        self.config = YLeaf(YType.enumeration, "config")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("config") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Aaa.Radius.RadiusAttribute.AcctMultiSessionId.IncludeParentSessionId, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Aaa.Radius.RadiusAttribute.AcctMultiSessionId.IncludeParentSessionId, self).__setattr__(name, value)

                    def has_data(self):
                        return self.config.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.config.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "include-parent-session-id" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/radius-attribute/acct-multi-session-id/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.config.is_set or self.config.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.config.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "config"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "config"):
                            self.config = value
                            self.config.value_namespace = name_space
                            self.config.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (self.include_parent_session_id is not None and self.include_parent_session_id.has_data())

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.include_parent_session_id is not None and self.include_parent_session_id.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "acct-multi-session-id" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/radius-attribute/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "include-parent-session-id"):
                        if (self.include_parent_session_id is None):
                            self.include_parent_session_id = Aaa.Radius.RadiusAttribute.AcctMultiSessionId.IncludeParentSessionId()
                            self.include_parent_session_id.parent = self
                            self._children_name_map["include_parent_session_id"] = "include-parent-session-id"
                        return self.include_parent_session_id

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "include-parent-session-id"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class AcctSessionId(Entity):
                """
                Acct\-Session\-Id attribute(44)
                
                .. attribute:: prepend_nas_port_id
                
                	Prepend Acct\-Session\-Id attribute with Nas\-Port\-Id
                	**type**\:   :py:class:`PrependNasPortId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.RadiusAttribute.AcctSessionId.PrependNasPortId>`
                
                

                """

                _prefix = 'aaa-protocol-radius-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.Radius.RadiusAttribute.AcctSessionId, self).__init__()

                    self.yang_name = "acct-session-id"
                    self.yang_parent_name = "radius-attribute"

                    self.prepend_nas_port_id = Aaa.Radius.RadiusAttribute.AcctSessionId.PrependNasPortId()
                    self.prepend_nas_port_id.parent = self
                    self._children_name_map["prepend_nas_port_id"] = "prepend-nas-port-id"
                    self._children_yang_names.add("prepend-nas-port-id")


                class PrependNasPortId(Entity):
                    """
                    Prepend Acct\-Session\-Id attribute with
                    Nas\-Port\-Id
                    
                    .. attribute:: config
                    
                    	false/true
                    	**type**\:   :py:class:`AaaConfig <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg.AaaConfig>`
                    
                    

                    """

                    _prefix = 'aaa-protocol-radius-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Aaa.Radius.RadiusAttribute.AcctSessionId.PrependNasPortId, self).__init__()

                        self.yang_name = "prepend-nas-port-id"
                        self.yang_parent_name = "acct-session-id"

                        self.config = YLeaf(YType.enumeration, "config")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("config") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Aaa.Radius.RadiusAttribute.AcctSessionId.PrependNasPortId, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Aaa.Radius.RadiusAttribute.AcctSessionId.PrependNasPortId, self).__setattr__(name, value)

                    def has_data(self):
                        return self.config.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.config.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "prepend-nas-port-id" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/radius-attribute/acct-session-id/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.config.is_set or self.config.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.config.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "config"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "config"):
                            self.config = value
                            self.config.value_namespace = name_space
                            self.config.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (self.prepend_nas_port_id is not None and self.prepend_nas_port_id.has_data())

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.prepend_nas_port_id is not None and self.prepend_nas_port_id.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "acct-session-id" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/radius-attribute/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "prepend-nas-port-id"):
                        if (self.prepend_nas_port_id is None):
                            self.prepend_nas_port_id = Aaa.Radius.RadiusAttribute.AcctSessionId.PrependNasPortId()
                            self.prepend_nas_port_id.parent = self
                            self._children_name_map["prepend_nas_port_id"] = "prepend-nas-port-id"
                        return self.prepend_nas_port_id

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "prepend-nas-port-id"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    (self.acct_multi_session_id is not None and self.acct_multi_session_id.has_data()) or
                    (self.acct_session_id is not None and self.acct_session_id.has_data()) or
                    (self.filter_id_11 is not None and self.filter_id_11.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.acct_multi_session_id is not None and self.acct_multi_session_id.has_operation()) or
                    (self.acct_session_id is not None and self.acct_session_id.has_operation()) or
                    (self.filter_id_11 is not None and self.filter_id_11.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "radius-attribute" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "acct-multi-session-id"):
                    if (self.acct_multi_session_id is None):
                        self.acct_multi_session_id = Aaa.Radius.RadiusAttribute.AcctMultiSessionId()
                        self.acct_multi_session_id.parent = self
                        self._children_name_map["acct_multi_session_id"] = "acct-multi-session-id"
                    return self.acct_multi_session_id

                if (child_yang_name == "acct-session-id"):
                    if (self.acct_session_id is None):
                        self.acct_session_id = Aaa.Radius.RadiusAttribute.AcctSessionId()
                        self.acct_session_id.parent = self
                        self._children_name_map["acct_session_id"] = "acct-session-id"
                    return self.acct_session_id

                if (child_yang_name == "filter-id-11"):
                    if (self.filter_id_11 is None):
                        self.filter_id_11 = Aaa.Radius.RadiusAttribute.FilterId11()
                        self.filter_id_11.parent = self
                        self._children_name_map["filter_id_11"] = "filter-id-11"
                    return self.filter_id_11

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "acct-multi-session-id" or name == "acct-session-id" or name == "filter-id-11"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class Attributes(Entity):
            """
            Table of attribute list
            
            .. attribute:: attribute
            
            	Attribute list name
            	**type**\: list of    :py:class:`Attribute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.Attributes.Attribute>`
            
            

            """

            _prefix = 'aaa-protocol-radius-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Radius.Attributes, self).__init__()

                self.yang_name = "attributes"
                self.yang_parent_name = "radius"

                self.attribute = YList(self)

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
                            super(Aaa.Radius.Attributes, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Aaa.Radius.Attributes, self).__setattr__(name, value)


            class Attribute(Entity):
                """
                Attribute list name
                
                .. attribute:: attribute_list_name  <key>
                
                	Attribute list name
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: attribute
                
                	Specify RADIUS attribute
                	**type**\:  str
                
                

                """

                _prefix = 'aaa-protocol-radius-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.Radius.Attributes.Attribute, self).__init__()

                    self.yang_name = "attribute"
                    self.yang_parent_name = "attributes"

                    self.attribute_list_name = YLeaf(YType.str, "attribute-list-name")

                    self.attribute = YLeaf(YType.str, "attribute")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("attribute_list_name",
                                    "attribute") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Aaa.Radius.Attributes.Attribute, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Aaa.Radius.Attributes.Attribute, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.attribute_list_name.is_set or
                        self.attribute.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.attribute_list_name.yfilter != YFilter.not_set or
                        self.attribute.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "attribute" + "[attribute-list-name='" + self.attribute_list_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/attributes/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.attribute_list_name.is_set or self.attribute_list_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.attribute_list_name.get_name_leafdata())
                    if (self.attribute.is_set or self.attribute.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.attribute.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "attribute-list-name" or name == "attribute"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "attribute-list-name"):
                        self.attribute_list_name = value
                        self.attribute_list_name.value_namespace = name_space
                        self.attribute_list_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "attribute"):
                        self.attribute = value
                        self.attribute.value_namespace = name_space
                        self.attribute.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.attribute:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.attribute:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "attributes" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "attribute"):
                    for c in self.attribute:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Aaa.Radius.Attributes.Attribute()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.attribute.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "attribute"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class SourcePort(Entity):
            """
            Source port
            
            .. attribute:: extended
            
            	Enable source\-port extend 
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'aaa-protocol-radius-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Radius.SourcePort, self).__init__()

                self.yang_name = "source-port"
                self.yang_parent_name = "radius"

                self.extended = YLeaf(YType.empty, "extended")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("extended") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Aaa.Radius.SourcePort, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Aaa.Radius.SourcePort, self).__setattr__(name, value)

            def has_data(self):
                return self.extended.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.extended.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "source-port" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.extended.is_set or self.extended.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.extended.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "extended"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "extended"):
                    self.extended = value
                    self.extended.value_namespace = name_space
                    self.extended.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (
                self.dead_time.is_set or
                self.idle_time.is_set or
                self.ignore_accounting_port.is_set or
                self.ignore_auth_port.is_set or
                self.key.is_set or
                self.retransmit.is_set or
                self.timeout.is_set or
                self.username.is_set or
                (self.attributes is not None and self.attributes.has_data()) or
                (self.dead_criteria is not None and self.dead_criteria.has_data()) or
                (self.disallow is not None and self.disallow.has_data()) or
                (self.dynamic_authorization is not None and self.dynamic_authorization.has_data()) or
                (self.hosts is not None and self.hosts.has_data()) or
                (self.ipv4 is not None and self.ipv4.has_data()) or
                (self.ipv6 is not None and self.ipv6.has_data()) or
                (self.load_balance_options is not None and self.load_balance_options.has_data()) or
                (self.radius_attribute is not None and self.radius_attribute.has_data()) or
                (self.source_port is not None and self.source_port.has_data()) or
                (self.throttle is not None and self.throttle.has_data()) or
                (self.vrfs is not None and self.vrfs.has_data()) or
                (self.vsa is not None and self.vsa.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.dead_time.yfilter != YFilter.not_set or
                self.idle_time.yfilter != YFilter.not_set or
                self.ignore_accounting_port.yfilter != YFilter.not_set or
                self.ignore_auth_port.yfilter != YFilter.not_set or
                self.key.yfilter != YFilter.not_set or
                self.retransmit.yfilter != YFilter.not_set or
                self.timeout.yfilter != YFilter.not_set or
                self.username.yfilter != YFilter.not_set or
                (self.attributes is not None and self.attributes.has_operation()) or
                (self.dead_criteria is not None and self.dead_criteria.has_operation()) or
                (self.disallow is not None and self.disallow.has_operation()) or
                (self.dynamic_authorization is not None and self.dynamic_authorization.has_operation()) or
                (self.hosts is not None and self.hosts.has_operation()) or
                (self.ipv4 is not None and self.ipv4.has_operation()) or
                (self.ipv6 is not None and self.ipv6.has_operation()) or
                (self.load_balance_options is not None and self.load_balance_options.has_operation()) or
                (self.radius_attribute is not None and self.radius_attribute.has_operation()) or
                (self.source_port is not None and self.source_port.has_operation()) or
                (self.throttle is not None and self.throttle.has_operation()) or
                (self.vrfs is not None and self.vrfs.has_operation()) or
                (self.vsa is not None and self.vsa.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "Cisco-IOS-XR-aaa-protocol-radius-cfg:radius" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.dead_time.is_set or self.dead_time.yfilter != YFilter.not_set):
                leaf_name_data.append(self.dead_time.get_name_leafdata())
            if (self.idle_time.is_set or self.idle_time.yfilter != YFilter.not_set):
                leaf_name_data.append(self.idle_time.get_name_leafdata())
            if (self.ignore_accounting_port.is_set or self.ignore_accounting_port.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ignore_accounting_port.get_name_leafdata())
            if (self.ignore_auth_port.is_set or self.ignore_auth_port.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ignore_auth_port.get_name_leafdata())
            if (self.key.is_set or self.key.yfilter != YFilter.not_set):
                leaf_name_data.append(self.key.get_name_leafdata())
            if (self.retransmit.is_set or self.retransmit.yfilter != YFilter.not_set):
                leaf_name_data.append(self.retransmit.get_name_leafdata())
            if (self.timeout.is_set or self.timeout.yfilter != YFilter.not_set):
                leaf_name_data.append(self.timeout.get_name_leafdata())
            if (self.username.is_set or self.username.yfilter != YFilter.not_set):
                leaf_name_data.append(self.username.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "attributes"):
                if (self.attributes is None):
                    self.attributes = Aaa.Radius.Attributes()
                    self.attributes.parent = self
                    self._children_name_map["attributes"] = "attributes"
                return self.attributes

            if (child_yang_name == "dead-criteria"):
                if (self.dead_criteria is None):
                    self.dead_criteria = Aaa.Radius.DeadCriteria()
                    self.dead_criteria.parent = self
                    self._children_name_map["dead_criteria"] = "dead-criteria"
                return self.dead_criteria

            if (child_yang_name == "disallow"):
                if (self.disallow is None):
                    self.disallow = Aaa.Radius.Disallow()
                    self.disallow.parent = self
                    self._children_name_map["disallow"] = "disallow"
                return self.disallow

            if (child_yang_name == "dynamic-authorization"):
                if (self.dynamic_authorization is None):
                    self.dynamic_authorization = Aaa.Radius.DynamicAuthorization()
                    self.dynamic_authorization.parent = self
                    self._children_name_map["dynamic_authorization"] = "dynamic-authorization"
                return self.dynamic_authorization

            if (child_yang_name == "hosts"):
                if (self.hosts is None):
                    self.hosts = Aaa.Radius.Hosts()
                    self.hosts.parent = self
                    self._children_name_map["hosts"] = "hosts"
                return self.hosts

            if (child_yang_name == "ipv4"):
                if (self.ipv4 is None):
                    self.ipv4 = Aaa.Radius.Ipv4()
                    self.ipv4.parent = self
                    self._children_name_map["ipv4"] = "ipv4"
                return self.ipv4

            if (child_yang_name == "ipv6"):
                if (self.ipv6 is None):
                    self.ipv6 = Aaa.Radius.Ipv6()
                    self.ipv6.parent = self
                    self._children_name_map["ipv6"] = "ipv6"
                return self.ipv6

            if (child_yang_name == "load-balance-options"):
                if (self.load_balance_options is None):
                    self.load_balance_options = Aaa.Radius.LoadBalanceOptions()
                    self.load_balance_options.parent = self
                    self._children_name_map["load_balance_options"] = "load-balance-options"
                return self.load_balance_options

            if (child_yang_name == "radius-attribute"):
                if (self.radius_attribute is None):
                    self.radius_attribute = Aaa.Radius.RadiusAttribute()
                    self.radius_attribute.parent = self
                    self._children_name_map["radius_attribute"] = "radius-attribute"
                return self.radius_attribute

            if (child_yang_name == "source-port"):
                if (self.source_port is None):
                    self.source_port = Aaa.Radius.SourcePort()
                    self.source_port.parent = self
                    self._children_name_map["source_port"] = "source-port"
                return self.source_port

            if (child_yang_name == "throttle"):
                if (self.throttle is None):
                    self.throttle = Aaa.Radius.Throttle()
                    self.throttle.parent = self
                    self._children_name_map["throttle"] = "throttle"
                return self.throttle

            if (child_yang_name == "vrfs"):
                if (self.vrfs is None):
                    self.vrfs = Aaa.Radius.Vrfs()
                    self.vrfs.parent = self
                    self._children_name_map["vrfs"] = "vrfs"
                return self.vrfs

            if (child_yang_name == "vsa"):
                if (self.vsa is None):
                    self.vsa = Aaa.Radius.Vsa()
                    self.vsa.parent = self
                    self._children_name_map["vsa"] = "vsa"
                return self.vsa

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "attributes" or name == "dead-criteria" or name == "disallow" or name == "dynamic-authorization" or name == "hosts" or name == "ipv4" or name == "ipv6" or name == "load-balance-options" or name == "radius-attribute" or name == "source-port" or name == "throttle" or name == "vrfs" or name == "vsa" or name == "dead-time" or name == "idle-time" or name == "ignore-accounting-port" or name == "ignore-auth-port" or name == "key" or name == "retransmit" or name == "timeout" or name == "username"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "dead-time"):
                self.dead_time = value
                self.dead_time.value_namespace = name_space
                self.dead_time.value_namespace_prefix = name_space_prefix
            if(value_path == "idle-time"):
                self.idle_time = value
                self.idle_time.value_namespace = name_space
                self.idle_time.value_namespace_prefix = name_space_prefix
            if(value_path == "ignore-accounting-port"):
                self.ignore_accounting_port = value
                self.ignore_accounting_port.value_namespace = name_space
                self.ignore_accounting_port.value_namespace_prefix = name_space_prefix
            if(value_path == "ignore-auth-port"):
                self.ignore_auth_port = value
                self.ignore_auth_port.value_namespace = name_space
                self.ignore_auth_port.value_namespace_prefix = name_space_prefix
            if(value_path == "key"):
                self.key = value
                self.key.value_namespace = name_space
                self.key.value_namespace_prefix = name_space_prefix
            if(value_path == "retransmit"):
                self.retransmit = value
                self.retransmit.value_namespace = name_space
                self.retransmit.value_namespace_prefix = name_space_prefix
            if(value_path == "timeout"):
                self.timeout = value
                self.timeout.value_namespace = name_space
                self.timeout.value_namespace_prefix = name_space_prefix
            if(value_path == "username"):
                self.username = value
                self.username.value_namespace = name_space
                self.username.value_namespace_prefix = name_space_prefix


    class Tacacs(Entity):
        """
        Modify TACACS+ query parameters
        
        .. attribute:: hosts
        
        	Specify a TACACS+ server
        	**type**\:   :py:class:`Hosts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Tacacs.Hosts>`
        
        .. attribute:: ipv4
        
        	IPv4 configuration
        	**type**\:   :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Tacacs.Ipv4>`
        
        .. attribute:: ipv6
        
        	IPv6 configuration
        	**type**\:   :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Tacacs.Ipv6>`
        
        .. attribute:: key
        
        	Set TACACS+ encryption key
        	**type**\:  str
        
        	**pattern:** (!.+)\|([^!].+)
        
        .. attribute:: single_connect
        
        	Use a single connection for all sessions for a given TACACS+ server
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: timeout
        
        	Time to wait for a TACACS+ server to reply
        	**type**\:  int
        
        	**range:** 1..1000
        
        	**default value**\: 5
        
        .. attribute:: vrfs
        
        	List of VRFs
        	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Tacacs.Vrfs>`
        
        

        """

        _prefix = 'aaa-tacacs-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Aaa.Tacacs, self).__init__()

            self.yang_name = "tacacs"
            self.yang_parent_name = "aaa"

            self.key = YLeaf(YType.str, "key")

            self.single_connect = YLeaf(YType.boolean, "single-connect")

            self.timeout = YLeaf(YType.uint32, "timeout")

            self.hosts = Aaa.Tacacs.Hosts()
            self.hosts.parent = self
            self._children_name_map["hosts"] = "hosts"
            self._children_yang_names.add("hosts")

            self.ipv4 = Aaa.Tacacs.Ipv4()
            self.ipv4.parent = self
            self._children_name_map["ipv4"] = "ipv4"
            self._children_yang_names.add("ipv4")

            self.ipv6 = Aaa.Tacacs.Ipv6()
            self.ipv6.parent = self
            self._children_name_map["ipv6"] = "ipv6"
            self._children_yang_names.add("ipv6")

            self.vrfs = Aaa.Tacacs.Vrfs()
            self.vrfs.parent = self
            self._children_name_map["vrfs"] = "vrfs"
            self._children_yang_names.add("vrfs")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("key",
                            "single_connect",
                            "timeout") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Aaa.Tacacs, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Aaa.Tacacs, self).__setattr__(name, value)


        class Ipv6(Entity):
            """
            IPv6 configuration
            
            .. attribute:: dscp
            
            	Specify the DSCP value
            	**type**\: one of the below types:
            
            	**type**\:   :py:class:`TacacsDscpValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_tacacs_cfg.TacacsDscpValue>`
            
            
            ----
            	**type**\:  int
            
            	**range:** 0..63
            
            
            ----
            

            """

            _prefix = 'aaa-tacacs-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Tacacs.Ipv6, self).__init__()

                self.yang_name = "ipv6"
                self.yang_parent_name = "tacacs"

                self.dscp = YLeaf(YType.str, "dscp")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("dscp") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Aaa.Tacacs.Ipv6, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Aaa.Tacacs.Ipv6, self).__setattr__(name, value)

            def has_data(self):
                return self.dscp.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.dscp.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ipv6" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-tacacs-cfg:tacacs/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.dscp.is_set or self.dscp.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dscp.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "dscp"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "dscp"):
                    self.dscp = value
                    self.dscp.value_namespace = name_space
                    self.dscp.value_namespace_prefix = name_space_prefix


        class Hosts(Entity):
            """
            Specify a TACACS+ server
            
            .. attribute:: host
            
            	One of the TACACS+ servers
            	**type**\: list of    :py:class:`Host <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Tacacs.Hosts.Host>`
            
            

            """

            _prefix = 'aaa-tacacs-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Tacacs.Hosts, self).__init__()

                self.yang_name = "hosts"
                self.yang_parent_name = "tacacs"

                self.host = YList(self)

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
                            super(Aaa.Tacacs.Hosts, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Aaa.Tacacs.Hosts, self).__setattr__(name, value)


            class Host(Entity):
                """
                One of the TACACS+ servers
                
                .. attribute:: ordering_index  <key>
                
                	This is used to sort the servers in the order of precedence
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: ip_address  <key>
                
                	IP address of TACACS+ server
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                
                ----
                .. attribute:: port_number  <key>
                
                	Port number (standard 49)
                	**type**\:  int
                
                	**range:** 1..65535
                
                .. attribute:: key
                
                	Set TACACS+ encryption key
                	**type**\:  str
                
                	**pattern:** (!.+)\|([^!].+)
                
                .. attribute:: single_connect
                
                	Use a single connection for all sessions for a given TACACS+ server
                	**type**\:  bool
                
                	**default value**\: false
                
                .. attribute:: timeout
                
                	Time to wait for a TACACS+ server to reply
                	**type**\:  int
                
                	**range:** 1..1000
                
                	**default value**\: 5
                
                

                """

                _prefix = 'aaa-tacacs-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.Tacacs.Hosts.Host, self).__init__()

                    self.yang_name = "host"
                    self.yang_parent_name = "hosts"

                    self.ordering_index = YLeaf(YType.int32, "ordering-index")

                    self.ip_address = YLeaf(YType.str, "ip-address")

                    self.port_number = YLeaf(YType.uint32, "port-number")

                    self.key = YLeaf(YType.str, "key")

                    self.single_connect = YLeaf(YType.boolean, "single-connect")

                    self.timeout = YLeaf(YType.uint32, "timeout")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("ordering_index",
                                    "ip_address",
                                    "port_number",
                                    "key",
                                    "single_connect",
                                    "timeout") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Aaa.Tacacs.Hosts.Host, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Aaa.Tacacs.Hosts.Host, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.ordering_index.is_set or
                        self.ip_address.is_set or
                        self.port_number.is_set or
                        self.key.is_set or
                        self.single_connect.is_set or
                        self.timeout.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.ordering_index.yfilter != YFilter.not_set or
                        self.ip_address.yfilter != YFilter.not_set or
                        self.port_number.yfilter != YFilter.not_set or
                        self.key.yfilter != YFilter.not_set or
                        self.single_connect.yfilter != YFilter.not_set or
                        self.timeout.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "host" + "[ordering-index='" + self.ordering_index.get() + "']" + "[ip-address='" + self.ip_address.get() + "']" + "[port-number='" + self.port_number.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-tacacs-cfg:tacacs/hosts/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.ordering_index.is_set or self.ordering_index.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ordering_index.get_name_leafdata())
                    if (self.ip_address.is_set or self.ip_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ip_address.get_name_leafdata())
                    if (self.port_number.is_set or self.port_number.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.port_number.get_name_leafdata())
                    if (self.key.is_set or self.key.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.key.get_name_leafdata())
                    if (self.single_connect.is_set or self.single_connect.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.single_connect.get_name_leafdata())
                    if (self.timeout.is_set or self.timeout.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.timeout.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "ordering-index" or name == "ip-address" or name == "port-number" or name == "key" or name == "single-connect" or name == "timeout"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "ordering-index"):
                        self.ordering_index = value
                        self.ordering_index.value_namespace = name_space
                        self.ordering_index.value_namespace_prefix = name_space_prefix
                    if(value_path == "ip-address"):
                        self.ip_address = value
                        self.ip_address.value_namespace = name_space
                        self.ip_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "port-number"):
                        self.port_number = value
                        self.port_number.value_namespace = name_space
                        self.port_number.value_namespace_prefix = name_space_prefix
                    if(value_path == "key"):
                        self.key = value
                        self.key.value_namespace = name_space
                        self.key.value_namespace_prefix = name_space_prefix
                    if(value_path == "single-connect"):
                        self.single_connect = value
                        self.single_connect.value_namespace = name_space
                        self.single_connect.value_namespace_prefix = name_space_prefix
                    if(value_path == "timeout"):
                        self.timeout = value
                        self.timeout.value_namespace = name_space
                        self.timeout.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.host:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.host:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "hosts" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-tacacs-cfg:tacacs/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "host"):
                    for c in self.host:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Aaa.Tacacs.Hosts.Host()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.host.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "host"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class Ipv4(Entity):
            """
            IPv4 configuration
            
            .. attribute:: dscp
            
            	Specify the DSCP value
            	**type**\: one of the below types:
            
            	**type**\:   :py:class:`TacacsDscpValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_tacacs_cfg.TacacsDscpValue>`
            
            
            ----
            	**type**\:  int
            
            	**range:** 0..63
            
            
            ----
            

            """

            _prefix = 'aaa-tacacs-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Tacacs.Ipv4, self).__init__()

                self.yang_name = "ipv4"
                self.yang_parent_name = "tacacs"

                self.dscp = YLeaf(YType.str, "dscp")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("dscp") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Aaa.Tacacs.Ipv4, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Aaa.Tacacs.Ipv4, self).__setattr__(name, value)

            def has_data(self):
                return self.dscp.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.dscp.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ipv4" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-tacacs-cfg:tacacs/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.dscp.is_set or self.dscp.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dscp.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "dscp"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "dscp"):
                    self.dscp = value
                    self.dscp.value_namespace = name_space
                    self.dscp.value_namespace_prefix = name_space_prefix


        class Vrfs(Entity):
            """
            List of VRFs
            
            .. attribute:: vrf
            
            	A VRF
            	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Tacacs.Vrfs.Vrf>`
            
            

            """

            _prefix = 'aaa-tacacs-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Tacacs.Vrfs, self).__init__()

                self.yang_name = "vrfs"
                self.yang_parent_name = "tacacs"

                self.vrf = YList(self)

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
                            super(Aaa.Tacacs.Vrfs, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Aaa.Tacacs.Vrfs, self).__setattr__(name, value)


            class Vrf(Entity):
                """
                A VRF
                
                .. attribute:: vrf_name  <key>
                
                	VRF name. Specify 'default' for default VRF
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: source_interface
                
                	Specify interface for source address in TACACS+ packets
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                

                """

                _prefix = 'aaa-tacacs-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.Tacacs.Vrfs.Vrf, self).__init__()

                    self.yang_name = "vrf"
                    self.yang_parent_name = "vrfs"

                    self.vrf_name = YLeaf(YType.str, "vrf-name")

                    self.source_interface = YLeaf(YType.str, "source-interface")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("vrf_name",
                                    "source_interface") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Aaa.Tacacs.Vrfs.Vrf, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Aaa.Tacacs.Vrfs.Vrf, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.vrf_name.is_set or
                        self.source_interface.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.vrf_name.yfilter != YFilter.not_set or
                        self.source_interface.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "vrf" + "[vrf-name='" + self.vrf_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-tacacs-cfg:tacacs/vrfs/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.vrf_name.get_name_leafdata())
                    if (self.source_interface.is_set or self.source_interface.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.source_interface.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "vrf-name" or name == "source-interface"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "vrf-name"):
                        self.vrf_name = value
                        self.vrf_name.value_namespace = name_space
                        self.vrf_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "source-interface"):
                        self.source_interface = value
                        self.source_interface.value_namespace = name_space
                        self.source_interface.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.vrf:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.vrf:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "vrfs" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-tacacs-cfg:tacacs/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "vrf"):
                    for c in self.vrf:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Aaa.Tacacs.Vrfs.Vrf()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.vrf.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "vrf"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                self.key.is_set or
                self.single_connect.is_set or
                self.timeout.is_set or
                (self.hosts is not None and self.hosts.has_data()) or
                (self.ipv4 is not None and self.ipv4.has_data()) or
                (self.ipv6 is not None and self.ipv6.has_data()) or
                (self.vrfs is not None and self.vrfs.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.key.yfilter != YFilter.not_set or
                self.single_connect.yfilter != YFilter.not_set or
                self.timeout.yfilter != YFilter.not_set or
                (self.hosts is not None and self.hosts.has_operation()) or
                (self.ipv4 is not None and self.ipv4.has_operation()) or
                (self.ipv6 is not None and self.ipv6.has_operation()) or
                (self.vrfs is not None and self.vrfs.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "Cisco-IOS-XR-aaa-tacacs-cfg:tacacs" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.key.is_set or self.key.yfilter != YFilter.not_set):
                leaf_name_data.append(self.key.get_name_leafdata())
            if (self.single_connect.is_set or self.single_connect.yfilter != YFilter.not_set):
                leaf_name_data.append(self.single_connect.get_name_leafdata())
            if (self.timeout.is_set or self.timeout.yfilter != YFilter.not_set):
                leaf_name_data.append(self.timeout.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "hosts"):
                if (self.hosts is None):
                    self.hosts = Aaa.Tacacs.Hosts()
                    self.hosts.parent = self
                    self._children_name_map["hosts"] = "hosts"
                return self.hosts

            if (child_yang_name == "ipv4"):
                if (self.ipv4 is None):
                    self.ipv4 = Aaa.Tacacs.Ipv4()
                    self.ipv4.parent = self
                    self._children_name_map["ipv4"] = "ipv4"
                return self.ipv4

            if (child_yang_name == "ipv6"):
                if (self.ipv6 is None):
                    self.ipv6 = Aaa.Tacacs.Ipv6()
                    self.ipv6.parent = self
                    self._children_name_map["ipv6"] = "ipv6"
                return self.ipv6

            if (child_yang_name == "vrfs"):
                if (self.vrfs is None):
                    self.vrfs = Aaa.Tacacs.Vrfs()
                    self.vrfs.parent = self
                    self._children_name_map["vrfs"] = "vrfs"
                return self.vrfs

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "hosts" or name == "ipv4" or name == "ipv6" or name == "vrfs" or name == "key" or name == "single-connect" or name == "timeout"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "key"):
                self.key = value
                self.key.value_namespace = name_space
                self.key.value_namespace_prefix = name_space_prefix
            if(value_path == "single-connect"):
                self.single_connect = value
                self.single_connect.value_namespace = name_space
                self.single_connect.value_namespace_prefix = name_space_prefix
            if(value_path == "timeout"):
                self.timeout = value
                self.timeout.value_namespace = name_space
                self.timeout.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (
            self.default_taskgroup.is_set or
            (self.aaa_dot1x is not None and self.aaa_dot1x.has_data()) or
            (self.aaa_mobile is not None and self.aaa_mobile.has_data()) or
            (self.aaa_subscriber is not None and self.aaa_subscriber.has_data()) or
            (self.accountings is not None and self.accountings.has_data()) or
            (self.authentications is not None and self.authentications.has_data()) or
            (self.authorizations is not None and self.authorizations.has_data()) or
            (self.banner is not None and self.banner.has_data()) or
            (self.diameter is not None and self.diameter.has_data()) or
            (self.radius is not None and self.radius.has_data()) or
            (self.radius_attribute is not None and self.radius_attribute.has_data()) or
            (self.server_groups is not None and self.server_groups.has_data()) or
            (self.tacacs is not None and self.tacacs.has_data()) or
            (self.taskgroups is not None and self.taskgroups.has_data()) or
            (self.usergroups is not None and self.usergroups.has_data()) or
            (self.usernames is not None and self.usernames.has_data()) or
            (self.accounting_update is not None))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            self.default_taskgroup.yfilter != YFilter.not_set or
            (self.aaa_dot1x is not None and self.aaa_dot1x.has_operation()) or
            (self.aaa_mobile is not None and self.aaa_mobile.has_operation()) or
            (self.aaa_subscriber is not None and self.aaa_subscriber.has_operation()) or
            (self.accounting_update is not None and self.accounting_update.has_operation()) or
            (self.accountings is not None and self.accountings.has_operation()) or
            (self.authentications is not None and self.authentications.has_operation()) or
            (self.authorizations is not None and self.authorizations.has_operation()) or
            (self.banner is not None and self.banner.has_operation()) or
            (self.diameter is not None and self.diameter.has_operation()) or
            (self.radius is not None and self.radius.has_operation()) or
            (self.radius_attribute is not None and self.radius_attribute.has_operation()) or
            (self.server_groups is not None and self.server_groups.has_operation()) or
            (self.tacacs is not None and self.tacacs.has_operation()) or
            (self.taskgroups is not None and self.taskgroups.has_operation()) or
            (self.usergroups is not None and self.usergroups.has_operation()) or
            (self.usernames is not None and self.usernames.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-aaa-lib-cfg:aaa" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()
        if (self.default_taskgroup.is_set or self.default_taskgroup.yfilter != YFilter.not_set):
            leaf_name_data.append(self.default_taskgroup.get_name_leafdata())

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "aaa-dot1x"):
            if (self.aaa_dot1x is None):
                self.aaa_dot1x = Aaa.AaaDot1X()
                self.aaa_dot1x.parent = self
                self._children_name_map["aaa_dot1x"] = "aaa-dot1x"
            return self.aaa_dot1x

        if (child_yang_name == "aaa-mobile"):
            if (self.aaa_mobile is None):
                self.aaa_mobile = Aaa.AaaMobile()
                self.aaa_mobile.parent = self
                self._children_name_map["aaa_mobile"] = "aaa-mobile"
            return self.aaa_mobile

        if (child_yang_name == "aaa-subscriber"):
            if (self.aaa_subscriber is None):
                self.aaa_subscriber = Aaa.AaaSubscriber()
                self.aaa_subscriber.parent = self
                self._children_name_map["aaa_subscriber"] = "aaa-subscriber"
            return self.aaa_subscriber

        if (child_yang_name == "accounting-update"):
            if (self.accounting_update is None):
                self.accounting_update = Aaa.AccountingUpdate()
                self.accounting_update.parent = self
                self._children_name_map["accounting_update"] = "accounting-update"
            return self.accounting_update

        if (child_yang_name == "accountings"):
            if (self.accountings is None):
                self.accountings = Aaa.Accountings()
                self.accountings.parent = self
                self._children_name_map["accountings"] = "accountings"
            return self.accountings

        if (child_yang_name == "authentications"):
            if (self.authentications is None):
                self.authentications = Aaa.Authentications()
                self.authentications.parent = self
                self._children_name_map["authentications"] = "authentications"
            return self.authentications

        if (child_yang_name == "authorizations"):
            if (self.authorizations is None):
                self.authorizations = Aaa.Authorizations()
                self.authorizations.parent = self
                self._children_name_map["authorizations"] = "authorizations"
            return self.authorizations

        if (child_yang_name == "banner"):
            if (self.banner is None):
                self.banner = Aaa.Banner()
                self.banner.parent = self
                self._children_name_map["banner"] = "banner"
            return self.banner

        if (child_yang_name == "diameter"):
            if (self.diameter is None):
                self.diameter = Aaa.Diameter()
                self.diameter.parent = self
                self._children_name_map["diameter"] = "diameter"
            return self.diameter

        if (child_yang_name == "radius"):
            if (self.radius is None):
                self.radius = Aaa.Radius()
                self.radius.parent = self
                self._children_name_map["radius"] = "radius"
            return self.radius

        if (child_yang_name == "radius-attribute"):
            if (self.radius_attribute is None):
                self.radius_attribute = Aaa.RadiusAttribute()
                self.radius_attribute.parent = self
                self._children_name_map["radius_attribute"] = "radius-attribute"
            return self.radius_attribute

        if (child_yang_name == "server-groups"):
            if (self.server_groups is None):
                self.server_groups = Aaa.ServerGroups()
                self.server_groups.parent = self
                self._children_name_map["server_groups"] = "server-groups"
            return self.server_groups

        if (child_yang_name == "tacacs"):
            if (self.tacacs is None):
                self.tacacs = Aaa.Tacacs()
                self.tacacs.parent = self
                self._children_name_map["tacacs"] = "tacacs"
            return self.tacacs

        if (child_yang_name == "taskgroups"):
            if (self.taskgroups is None):
                self.taskgroups = Aaa.Taskgroups()
                self.taskgroups.parent = self
                self._children_name_map["taskgroups"] = "taskgroups"
            return self.taskgroups

        if (child_yang_name == "usergroups"):
            if (self.usergroups is None):
                self.usergroups = Aaa.Usergroups()
                self.usergroups.parent = self
                self._children_name_map["usergroups"] = "usergroups"
            return self.usergroups

        if (child_yang_name == "usernames"):
            if (self.usernames is None):
                self.usernames = Aaa.Usernames()
                self.usernames.parent = self
                self._children_name_map["usernames"] = "usernames"
            return self.usernames

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "aaa-dot1x" or name == "aaa-mobile" or name == "aaa-subscriber" or name == "accounting-update" or name == "accountings" or name == "authentications" or name == "authorizations" or name == "banner" or name == "diameter" or name == "radius" or name == "radius-attribute" or name == "server-groups" or name == "tacacs" or name == "taskgroups" or name == "usergroups" or name == "usernames" or name == "default-taskgroup"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        if(value_path == "default-taskgroup"):
            self.default_taskgroup = value
            self.default_taskgroup.value_namespace = name_space
            self.default_taskgroup.value_namespace_prefix = name_space_prefix

    def clone_ptr(self):
        self._top_entity = Aaa()
        return self._top_entity

