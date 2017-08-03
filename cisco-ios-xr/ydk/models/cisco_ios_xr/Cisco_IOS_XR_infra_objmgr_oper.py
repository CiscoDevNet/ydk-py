""" Cisco_IOS_XR_infra_objmgr_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-objmgr package operational data.

This module contains definitions
for the following management objects\:
  object\-group\: Object\-group operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class EndPort(Enum):
    """
    EndPort

    End port

    .. data:: echo = 7

    	Echo (7)

    .. data:: discard = 9

    	Discard (9)

    .. data:: daytime = 13

    	Daytime (13)

    .. data:: chargen = 19

    	Character generator (19)

    .. data:: ftp_data = 20

    	FTP data connections (used infrequently, 20)

    .. data:: ftp = 21

    	File Transfer Protocol (21)

    .. data:: ssh = 22

    	Secure Shell (22)

    .. data:: telnet = 23

    	Telnet (23)

    .. data:: smtp = 25

    	Simple Mail Transport Protocol (25)

    .. data:: time = 37

    	Time (37)

    .. data:: nicname = 43

    	Nicname (43)

    .. data:: tacacs = 49

    	TAC Access Control System (49)

    .. data:: domain = 53

    	Domain Name Service (53)

    .. data:: gopher = 70

    	Gopher (70)

    .. data:: finger = 79

    	Finger (79)

    .. data:: www = 80

    	World Wide Web (HTTP, 80)

    .. data:: host_name = 101

    	NIC hostname server (101)

    .. data:: pop2 = 109

    	Post Office Protocol v2 (109)

    .. data:: pop3 = 110

    	Post Office Protocol v3 (110)

    .. data:: sun_rpc = 111

    	Sun Remote Procedure Call (111)

    .. data:: ident = 113

    	Ident Protocol (113)

    .. data:: nntp = 119

    	Network News Transport Protocol (119)

    .. data:: bgp = 179

    	Border Gateway Protocol (179)

    .. data:: irc = 194

    	Internet Relay Chat (194)

    .. data:: pim_auto_rp = 496

    	PIM Auto-RP (496)

    .. data:: exec_ = 512

    	Exec (rsh, 512)

    .. data:: login = 513

    	Login (rlogin, 513)

    .. data:: cmd = 514

    	Remote commands (rcmd, 514)

    .. data:: lpd = 515

    	Printer service (515)

    .. data:: uucp = 540

    	Unix-to-Unix Copy Program (540)

    .. data:: klogin = 543

    	Kerberos login (543)

    .. data:: kshell = 544

    	Kerberos shell (544)

    .. data:: talk = 517

    	Talk (517)

    .. data:: ldp = 646

    	LDP session connection attempts (MPLS, 646)

    """

    echo = Enum.YLeaf(7, "echo")

    discard = Enum.YLeaf(9, "discard")

    daytime = Enum.YLeaf(13, "daytime")

    chargen = Enum.YLeaf(19, "chargen")

    ftp_data = Enum.YLeaf(20, "ftp-data")

    ftp = Enum.YLeaf(21, "ftp")

    ssh = Enum.YLeaf(22, "ssh")

    telnet = Enum.YLeaf(23, "telnet")

    smtp = Enum.YLeaf(25, "smtp")

    time = Enum.YLeaf(37, "time")

    nicname = Enum.YLeaf(43, "nicname")

    tacacs = Enum.YLeaf(49, "tacacs")

    domain = Enum.YLeaf(53, "domain")

    gopher = Enum.YLeaf(70, "gopher")

    finger = Enum.YLeaf(79, "finger")

    www = Enum.YLeaf(80, "www")

    host_name = Enum.YLeaf(101, "host-name")

    pop2 = Enum.YLeaf(109, "pop2")

    pop3 = Enum.YLeaf(110, "pop3")

    sun_rpc = Enum.YLeaf(111, "sun-rpc")

    ident = Enum.YLeaf(113, "ident")

    nntp = Enum.YLeaf(119, "nntp")

    bgp = Enum.YLeaf(179, "bgp")

    irc = Enum.YLeaf(194, "irc")

    pim_auto_rp = Enum.YLeaf(496, "pim-auto-rp")

    exec_ = Enum.YLeaf(512, "exec")

    login = Enum.YLeaf(513, "login")

    cmd = Enum.YLeaf(514, "cmd")

    lpd = Enum.YLeaf(515, "lpd")

    uucp = Enum.YLeaf(540, "uucp")

    klogin = Enum.YLeaf(543, "klogin")

    kshell = Enum.YLeaf(544, "kshell")

    talk = Enum.YLeaf(517, "talk")

    ldp = Enum.YLeaf(646, "ldp")


class Port(Enum):
    """
    Port

    Port

    .. data:: echo = 7

    	Echo (7)

    .. data:: discard = 9

    	Discard (9)

    .. data:: daytime = 13

    	Daytime (13)

    .. data:: chargen = 19

    	Character generator (19)

    .. data:: ftp_data = 20

    	FTP data connections (used infrequently, 20)

    .. data:: ftp = 21

    	File Transfer Protocol (21)

    .. data:: ssh = 22

    	Secure Shell (22)

    .. data:: telnet = 23

    	Telnet (23)

    .. data:: smtp = 25

    	Simple Mail Transport Protocol (25)

    .. data:: time = 37

    	Time (37)

    .. data:: nicname = 43

    	Nicname (43)

    .. data:: tacacs = 49

    	TAC Access Control System (49)

    .. data:: domain = 53

    	Domain Name Service (53)

    .. data:: gopher = 70

    	Gopher (70)

    .. data:: finger = 79

    	Finger (79)

    .. data:: www = 80

    	World Wide Web (HTTP, 80)

    .. data:: host_name = 101

    	NIC hostname server (101)

    .. data:: pop2 = 109

    	Post Office Protocol v2 (109)

    .. data:: pop3 = 110

    	Post Office Protocol v3 (110)

    .. data:: sun_rpc = 111

    	Sun Remote Procedure Call (111)

    .. data:: ident = 113

    	Ident Protocol (113)

    .. data:: nntp = 119

    	Network News Transport Protocol (119)

    .. data:: bgp = 179

    	Border Gateway Protocol (179)

    .. data:: irc = 194

    	Internet Relay Chat (194)

    .. data:: pim_auto_rp = 496

    	PIM Auto-RP (496)

    .. data:: exec_ = 512

    	Exec (rsh, 512)

    .. data:: login = 513

    	Login (rlogin, 513)

    .. data:: cmd = 514

    	Remote commands (rcmd, 514)

    .. data:: lpd = 515

    	Printer service (515)

    .. data:: uucp = 540

    	Unix-to-Unix Copy Program (540)

    .. data:: klogin = 543

    	Kerberos login (543)

    .. data:: kshell = 544

    	Kerberos shell (544)

    .. data:: talk = 517

    	Talk (517)

    .. data:: ldp = 646

    	LDP session connection attempts (MPLS, 646)

    """

    echo = Enum.YLeaf(7, "echo")

    discard = Enum.YLeaf(9, "discard")

    daytime = Enum.YLeaf(13, "daytime")

    chargen = Enum.YLeaf(19, "chargen")

    ftp_data = Enum.YLeaf(20, "ftp-data")

    ftp = Enum.YLeaf(21, "ftp")

    ssh = Enum.YLeaf(22, "ssh")

    telnet = Enum.YLeaf(23, "telnet")

    smtp = Enum.YLeaf(25, "smtp")

    time = Enum.YLeaf(37, "time")

    nicname = Enum.YLeaf(43, "nicname")

    tacacs = Enum.YLeaf(49, "tacacs")

    domain = Enum.YLeaf(53, "domain")

    gopher = Enum.YLeaf(70, "gopher")

    finger = Enum.YLeaf(79, "finger")

    www = Enum.YLeaf(80, "www")

    host_name = Enum.YLeaf(101, "host-name")

    pop2 = Enum.YLeaf(109, "pop2")

    pop3 = Enum.YLeaf(110, "pop3")

    sun_rpc = Enum.YLeaf(111, "sun-rpc")

    ident = Enum.YLeaf(113, "ident")

    nntp = Enum.YLeaf(119, "nntp")

    bgp = Enum.YLeaf(179, "bgp")

    irc = Enum.YLeaf(194, "irc")

    pim_auto_rp = Enum.YLeaf(496, "pim-auto-rp")

    exec_ = Enum.YLeaf(512, "exec")

    login = Enum.YLeaf(513, "login")

    cmd = Enum.YLeaf(514, "cmd")

    lpd = Enum.YLeaf(515, "lpd")

    uucp = Enum.YLeaf(540, "uucp")

    klogin = Enum.YLeaf(543, "klogin")

    kshell = Enum.YLeaf(544, "kshell")

    talk = Enum.YLeaf(517, "talk")

    ldp = Enum.YLeaf(646, "ldp")


class PortOperator(Enum):
    """
    PortOperator

    Port operator

    .. data:: equal = 0

    	Match packets on ports equal to entered port

    	number

    .. data:: not_equal = 1

    	Match packets on ports not equal to entered

    	port number

    .. data:: greater_than = 2

    	Match packets on ports greater than entered

    	port number

    .. data:: less_than = 3

    	Match packets on ports less than entered port

    	number

    """

    equal = Enum.YLeaf(0, "equal")

    not_equal = Enum.YLeaf(1, "not-equal")

    greater_than = Enum.YLeaf(2, "greater-than")

    less_than = Enum.YLeaf(3, "less-than")


class StartPort(Enum):
    """
    StartPort

    Start port

    .. data:: echo = 7

    	Echo (7)

    .. data:: discard = 9

    	Discard (9)

    .. data:: daytime = 13

    	Daytime (13)

    .. data:: chargen = 19

    	Character generator (19)

    .. data:: ftp_data = 20

    	FTP data connections (used infrequently, 20)

    .. data:: ftp = 21

    	File Transfer Protocol (21)

    .. data:: ssh = 22

    	Secure Shell (22)

    .. data:: telnet = 23

    	Telnet (23)

    .. data:: smtp = 25

    	Simple Mail Transport Protocol (25)

    .. data:: time = 37

    	Time (37)

    .. data:: nicname = 43

    	Nicname (43)

    .. data:: tacacs = 49

    	TAC Access Control System (49)

    .. data:: domain = 53

    	Domain Name Service (53)

    .. data:: gopher = 70

    	Gopher (70)

    .. data:: finger = 79

    	Finger (79)

    .. data:: www = 80

    	World Wide Web (HTTP, 80)

    .. data:: host_name = 101

    	NIC hostname server (101)

    .. data:: pop2 = 109

    	Post Office Protocol v2 (109)

    .. data:: pop3 = 110

    	Post Office Protocol v3 (110)

    .. data:: sun_rpc = 111

    	Sun Remote Procedure Call (111)

    .. data:: ident = 113

    	Ident Protocol (113)

    .. data:: nntp = 119

    	Network News Transport Protocol (119)

    .. data:: bgp = 179

    	Border Gateway Protocol (179)

    .. data:: irc = 194

    	Internet Relay Chat (194)

    .. data:: pim_auto_rp = 496

    	PIM Auto-RP (496)

    .. data:: exec_ = 512

    	Exec (rsh, 512)

    .. data:: login = 513

    	Login (rlogin, 513)

    .. data:: cmd = 514

    	Remote commands (rcmd, 514)

    .. data:: lpd = 515

    	Printer service (515)

    .. data:: uucp = 540

    	Unix-to-Unix Copy Program (540)

    .. data:: klogin = 543

    	Kerberos login (543)

    .. data:: kshell = 544

    	Kerberos shell (544)

    .. data:: talk = 517

    	Talk (517)

    .. data:: ldp = 646

    	LDP session connection attempts (MPLS, 646)

    """

    echo = Enum.YLeaf(7, "echo")

    discard = Enum.YLeaf(9, "discard")

    daytime = Enum.YLeaf(13, "daytime")

    chargen = Enum.YLeaf(19, "chargen")

    ftp_data = Enum.YLeaf(20, "ftp-data")

    ftp = Enum.YLeaf(21, "ftp")

    ssh = Enum.YLeaf(22, "ssh")

    telnet = Enum.YLeaf(23, "telnet")

    smtp = Enum.YLeaf(25, "smtp")

    time = Enum.YLeaf(37, "time")

    nicname = Enum.YLeaf(43, "nicname")

    tacacs = Enum.YLeaf(49, "tacacs")

    domain = Enum.YLeaf(53, "domain")

    gopher = Enum.YLeaf(70, "gopher")

    finger = Enum.YLeaf(79, "finger")

    www = Enum.YLeaf(80, "www")

    host_name = Enum.YLeaf(101, "host-name")

    pop2 = Enum.YLeaf(109, "pop2")

    pop3 = Enum.YLeaf(110, "pop3")

    sun_rpc = Enum.YLeaf(111, "sun-rpc")

    ident = Enum.YLeaf(113, "ident")

    nntp = Enum.YLeaf(119, "nntp")

    bgp = Enum.YLeaf(179, "bgp")

    irc = Enum.YLeaf(194, "irc")

    pim_auto_rp = Enum.YLeaf(496, "pim-auto-rp")

    exec_ = Enum.YLeaf(512, "exec")

    login = Enum.YLeaf(513, "login")

    cmd = Enum.YLeaf(514, "cmd")

    lpd = Enum.YLeaf(515, "lpd")

    uucp = Enum.YLeaf(540, "uucp")

    klogin = Enum.YLeaf(543, "klogin")

    kshell = Enum.YLeaf(544, "kshell")

    talk = Enum.YLeaf(517, "talk")

    ldp = Enum.YLeaf(646, "ldp")



class ObjectGroup(Entity):
    """
    Object\-group operational data
    
    .. attribute:: network
    
    	Network object group
    	**type**\:   :py:class:`Network <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Network>`
    
    .. attribute:: port
    
    	Port object group
    	**type**\:   :py:class:`Port <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Port>`
    
    

    """

    _prefix = 'infra-objmgr-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(ObjectGroup, self).__init__()
        self._top_entity = None

        self.yang_name = "object-group"
        self.yang_parent_name = "Cisco-IOS-XR-infra-objmgr-oper"

        self.network = ObjectGroup.Network()
        self.network.parent = self
        self._children_name_map["network"] = "network"
        self._children_yang_names.add("network")

        self.port = ObjectGroup.Port()
        self.port.parent = self
        self._children_name_map["port"] = "port"
        self._children_yang_names.add("port")


    class Port(Entity):
        """
        Port object group
        
        .. attribute:: objects
        
        	Table of Object
        	**type**\:   :py:class:`Objects <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Port.Objects>`
        
        

        """

        _prefix = 'infra-objmgr-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(ObjectGroup.Port, self).__init__()

            self.yang_name = "port"
            self.yang_parent_name = "object-group"

            self.objects = ObjectGroup.Port.Objects()
            self.objects.parent = self
            self._children_name_map["objects"] = "objects"
            self._children_yang_names.add("objects")


        class Objects(Entity):
            """
            Table of Object
            
            .. attribute:: object
            
            	Port object group
            	**type**\: list of    :py:class:`Object <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Port.Objects.Object>`
            
            

            """

            _prefix = 'infra-objmgr-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(ObjectGroup.Port.Objects, self).__init__()

                self.yang_name = "objects"
                self.yang_parent_name = "port"

                self.object = YList(self)

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
                            super(ObjectGroup.Port.Objects, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(ObjectGroup.Port.Objects, self).__setattr__(name, value)


            class Object(Entity):
                """
                Port object group
                
                .. attribute:: object_name  <key>
                
                	Port object group name
                	**type**\:  str
                
                	**length:** 1..64
                
                .. attribute:: nested_groups
                
                	Table of NestedGroup
                	**type**\:   :py:class:`NestedGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Port.Objects.Object.NestedGroups>`
                
                .. attribute:: operators
                
                	Table of Operator
                	**type**\:   :py:class:`Operators <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Port.Objects.Object.Operators>`
                
                .. attribute:: parent_groups
                
                	Table of ParentGroup
                	**type**\:   :py:class:`ParentGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Port.Objects.Object.ParentGroups>`
                
                .. attribute:: port_ranges
                
                	Table of PortRange
                	**type**\:   :py:class:`PortRanges <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Port.Objects.Object.PortRanges>`
                
                

                """

                _prefix = 'infra-objmgr-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ObjectGroup.Port.Objects.Object, self).__init__()

                    self.yang_name = "object"
                    self.yang_parent_name = "objects"

                    self.object_name = YLeaf(YType.str, "object-name")

                    self.nested_groups = ObjectGroup.Port.Objects.Object.NestedGroups()
                    self.nested_groups.parent = self
                    self._children_name_map["nested_groups"] = "nested-groups"
                    self._children_yang_names.add("nested-groups")

                    self.operators = ObjectGroup.Port.Objects.Object.Operators()
                    self.operators.parent = self
                    self._children_name_map["operators"] = "operators"
                    self._children_yang_names.add("operators")

                    self.parent_groups = ObjectGroup.Port.Objects.Object.ParentGroups()
                    self.parent_groups.parent = self
                    self._children_name_map["parent_groups"] = "parent-groups"
                    self._children_yang_names.add("parent-groups")

                    self.port_ranges = ObjectGroup.Port.Objects.Object.PortRanges()
                    self.port_ranges.parent = self
                    self._children_name_map["port_ranges"] = "port-ranges"
                    self._children_yang_names.add("port-ranges")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("object_name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(ObjectGroup.Port.Objects.Object, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ObjectGroup.Port.Objects.Object, self).__setattr__(name, value)


                class NestedGroups(Entity):
                    """
                    Table of NestedGroup
                    
                    .. attribute:: nested_group
                    
                    	nested object group
                    	**type**\: list of    :py:class:`NestedGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Port.Objects.Object.NestedGroups.NestedGroup>`
                    
                    

                    """

                    _prefix = 'infra-objmgr-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ObjectGroup.Port.Objects.Object.NestedGroups, self).__init__()

                        self.yang_name = "nested-groups"
                        self.yang_parent_name = "object"

                        self.nested_group = YList(self)

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
                                    super(ObjectGroup.Port.Objects.Object.NestedGroups, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ObjectGroup.Port.Objects.Object.NestedGroups, self).__setattr__(name, value)


                    class NestedGroup(Entity):
                        """
                        nested object group
                        
                        .. attribute:: nested_group_name  <key>
                        
                        	Nested object group
                        	**type**\:  str
                        
                        	**length:** 1..64
                        
                        .. attribute:: nested_group_name_xr
                        
                        	Nested group
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'infra-objmgr-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(ObjectGroup.Port.Objects.Object.NestedGroups.NestedGroup, self).__init__()

                            self.yang_name = "nested-group"
                            self.yang_parent_name = "nested-groups"

                            self.nested_group_name = YLeaf(YType.str, "nested-group-name")

                            self.nested_group_name_xr = YLeaf(YType.str, "nested-group-name-xr")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("nested_group_name",
                                            "nested_group_name_xr") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(ObjectGroup.Port.Objects.Object.NestedGroups.NestedGroup, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(ObjectGroup.Port.Objects.Object.NestedGroups.NestedGroup, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.nested_group_name.is_set or
                                self.nested_group_name_xr.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.nested_group_name.yfilter != YFilter.not_set or
                                self.nested_group_name_xr.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "nested-group" + "[nested-group-name='" + self.nested_group_name.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.nested_group_name.is_set or self.nested_group_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.nested_group_name.get_name_leafdata())
                            if (self.nested_group_name_xr.is_set or self.nested_group_name_xr.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.nested_group_name_xr.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "nested-group-name" or name == "nested-group-name-xr"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "nested-group-name"):
                                self.nested_group_name = value
                                self.nested_group_name.value_namespace = name_space
                                self.nested_group_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "nested-group-name-xr"):
                                self.nested_group_name_xr = value
                                self.nested_group_name_xr.value_namespace = name_space
                                self.nested_group_name_xr.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.nested_group:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.nested_group:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "nested-groups" + path_buffer

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

                        if (child_yang_name == "nested-group"):
                            for c in self.nested_group:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = ObjectGroup.Port.Objects.Object.NestedGroups.NestedGroup()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.nested_group.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "nested-group"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class Operators(Entity):
                    """
                    Table of Operator
                    
                    .. attribute:: operator
                    
                    	op class
                    	**type**\: list of    :py:class:`Operator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Port.Objects.Object.Operators.Operator>`
                    
                    

                    """

                    _prefix = 'infra-objmgr-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ObjectGroup.Port.Objects.Object.Operators, self).__init__()

                        self.yang_name = "operators"
                        self.yang_parent_name = "object"

                        self.operator = YList(self)

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
                                    super(ObjectGroup.Port.Objects.Object.Operators, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ObjectGroup.Port.Objects.Object.Operators, self).__setattr__(name, value)


                    class Operator(Entity):
                        """
                        op class
                        
                        .. attribute:: operator_type
                        
                        	operation for ports
                        	**type**\:   :py:class:`PortOperator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.PortOperator>`
                        
                        .. attribute:: operator_type_xr
                        
                        	Operator
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: port
                        
                        	Port number
                        	**type**\: one of the below types:
                        
                        	**type**\:   :py:class:`Port <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.Port>`
                        
                        
                        ----
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        
                        ----
                        .. attribute:: port_xr
                        
                        	Port
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'infra-objmgr-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(ObjectGroup.Port.Objects.Object.Operators.Operator, self).__init__()

                            self.yang_name = "operator"
                            self.yang_parent_name = "operators"

                            self.operator_type = YLeaf(YType.enumeration, "operator-type")

                            self.operator_type_xr = YLeaf(YType.uint32, "operator-type-xr")

                            self.port = YLeaf(YType.str, "port")

                            self.port_xr = YLeaf(YType.uint32, "port-xr")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("operator_type",
                                            "operator_type_xr",
                                            "port",
                                            "port_xr") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(ObjectGroup.Port.Objects.Object.Operators.Operator, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(ObjectGroup.Port.Objects.Object.Operators.Operator, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.operator_type.is_set or
                                self.operator_type_xr.is_set or
                                self.port.is_set or
                                self.port_xr.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.operator_type.yfilter != YFilter.not_set or
                                self.operator_type_xr.yfilter != YFilter.not_set or
                                self.port.yfilter != YFilter.not_set or
                                self.port_xr.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "operator" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.operator_type.is_set or self.operator_type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.operator_type.get_name_leafdata())
                            if (self.operator_type_xr.is_set or self.operator_type_xr.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.operator_type_xr.get_name_leafdata())
                            if (self.port.is_set or self.port.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.port.get_name_leafdata())
                            if (self.port_xr.is_set or self.port_xr.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.port_xr.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "operator-type" or name == "operator-type-xr" or name == "port" or name == "port-xr"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "operator-type"):
                                self.operator_type = value
                                self.operator_type.value_namespace = name_space
                                self.operator_type.value_namespace_prefix = name_space_prefix
                            if(value_path == "operator-type-xr"):
                                self.operator_type_xr = value
                                self.operator_type_xr.value_namespace = name_space
                                self.operator_type_xr.value_namespace_prefix = name_space_prefix
                            if(value_path == "port"):
                                self.port = value
                                self.port.value_namespace = name_space
                                self.port.value_namespace_prefix = name_space_prefix
                            if(value_path == "port-xr"):
                                self.port_xr = value
                                self.port_xr.value_namespace = name_space
                                self.port_xr.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.operator:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.operator:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "operators" + path_buffer

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

                        if (child_yang_name == "operator"):
                            for c in self.operator:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = ObjectGroup.Port.Objects.Object.Operators.Operator()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.operator.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "operator"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class PortRanges(Entity):
                    """
                    Table of PortRange
                    
                    .. attribute:: port_range
                    
                    	Match only packets on a given port range
                    	**type**\: list of    :py:class:`PortRange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Port.Objects.Object.PortRanges.PortRange>`
                    
                    

                    """

                    _prefix = 'infra-objmgr-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ObjectGroup.Port.Objects.Object.PortRanges, self).__init__()

                        self.yang_name = "port-ranges"
                        self.yang_parent_name = "object"

                        self.port_range = YList(self)

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
                                    super(ObjectGroup.Port.Objects.Object.PortRanges, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ObjectGroup.Port.Objects.Object.PortRanges, self).__setattr__(name, value)


                    class PortRange(Entity):
                        """
                        Match only packets on a given port range
                        
                        .. attribute:: end_port
                        
                        	End port number
                        	**type**\: one of the below types:
                        
                        	**type**\:   :py:class:`EndPort <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.EndPort>`
                        
                        
                        ----
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        
                        ----
                        .. attribute:: end_port_xr
                        
                        	Port end address
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: start_port
                        
                        	Start port number
                        	**type**\: one of the below types:
                        
                        	**type**\:   :py:class:`StartPort <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.StartPort>`
                        
                        
                        ----
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        
                        ----
                        .. attribute:: start_port_xr
                        
                        	Port start address
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'infra-objmgr-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(ObjectGroup.Port.Objects.Object.PortRanges.PortRange, self).__init__()

                            self.yang_name = "port-range"
                            self.yang_parent_name = "port-ranges"

                            self.end_port = YLeaf(YType.str, "end-port")

                            self.end_port_xr = YLeaf(YType.uint32, "end-port-xr")

                            self.start_port = YLeaf(YType.str, "start-port")

                            self.start_port_xr = YLeaf(YType.uint32, "start-port-xr")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("end_port",
                                            "end_port_xr",
                                            "start_port",
                                            "start_port_xr") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(ObjectGroup.Port.Objects.Object.PortRanges.PortRange, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(ObjectGroup.Port.Objects.Object.PortRanges.PortRange, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.end_port.is_set or
                                self.end_port_xr.is_set or
                                self.start_port.is_set or
                                self.start_port_xr.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.end_port.yfilter != YFilter.not_set or
                                self.end_port_xr.yfilter != YFilter.not_set or
                                self.start_port.yfilter != YFilter.not_set or
                                self.start_port_xr.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "port-range" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.end_port.is_set or self.end_port.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.end_port.get_name_leafdata())
                            if (self.end_port_xr.is_set or self.end_port_xr.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.end_port_xr.get_name_leafdata())
                            if (self.start_port.is_set or self.start_port.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.start_port.get_name_leafdata())
                            if (self.start_port_xr.is_set or self.start_port_xr.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.start_port_xr.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "end-port" or name == "end-port-xr" or name == "start-port" or name == "start-port-xr"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "end-port"):
                                self.end_port = value
                                self.end_port.value_namespace = name_space
                                self.end_port.value_namespace_prefix = name_space_prefix
                            if(value_path == "end-port-xr"):
                                self.end_port_xr = value
                                self.end_port_xr.value_namespace = name_space
                                self.end_port_xr.value_namespace_prefix = name_space_prefix
                            if(value_path == "start-port"):
                                self.start_port = value
                                self.start_port.value_namespace = name_space
                                self.start_port.value_namespace_prefix = name_space_prefix
                            if(value_path == "start-port-xr"):
                                self.start_port_xr = value
                                self.start_port_xr.value_namespace = name_space
                                self.start_port_xr.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.port_range:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.port_range:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "port-ranges" + path_buffer

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

                        if (child_yang_name == "port-range"):
                            for c in self.port_range:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = ObjectGroup.Port.Objects.Object.PortRanges.PortRange()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.port_range.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "port-range"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class ParentGroups(Entity):
                    """
                    Table of ParentGroup
                    
                    .. attribute:: parent_group
                    
                    	Parent object group
                    	**type**\: list of    :py:class:`ParentGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Port.Objects.Object.ParentGroups.ParentGroup>`
                    
                    

                    """

                    _prefix = 'infra-objmgr-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ObjectGroup.Port.Objects.Object.ParentGroups, self).__init__()

                        self.yang_name = "parent-groups"
                        self.yang_parent_name = "object"

                        self.parent_group = YList(self)

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
                                    super(ObjectGroup.Port.Objects.Object.ParentGroups, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ObjectGroup.Port.Objects.Object.ParentGroups, self).__setattr__(name, value)


                    class ParentGroup(Entity):
                        """
                        Parent object group
                        
                        .. attribute:: parent_group_name  <key>
                        
                        	Nested object group
                        	**type**\:  str
                        
                        	**length:** 1..64
                        
                        .. attribute:: parent_name
                        
                        	Parent node
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'infra-objmgr-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(ObjectGroup.Port.Objects.Object.ParentGroups.ParentGroup, self).__init__()

                            self.yang_name = "parent-group"
                            self.yang_parent_name = "parent-groups"

                            self.parent_group_name = YLeaf(YType.str, "parent-group-name")

                            self.parent_name = YLeaf(YType.str, "parent-name")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("parent_group_name",
                                            "parent_name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(ObjectGroup.Port.Objects.Object.ParentGroups.ParentGroup, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(ObjectGroup.Port.Objects.Object.ParentGroups.ParentGroup, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.parent_group_name.is_set or
                                self.parent_name.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.parent_group_name.yfilter != YFilter.not_set or
                                self.parent_name.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "parent-group" + "[parent-group-name='" + self.parent_group_name.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.parent_group_name.is_set or self.parent_group_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.parent_group_name.get_name_leafdata())
                            if (self.parent_name.is_set or self.parent_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.parent_name.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "parent-group-name" or name == "parent-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "parent-group-name"):
                                self.parent_group_name = value
                                self.parent_group_name.value_namespace = name_space
                                self.parent_group_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "parent-name"):
                                self.parent_name = value
                                self.parent_name.value_namespace = name_space
                                self.parent_name.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.parent_group:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.parent_group:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "parent-groups" + path_buffer

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

                        if (child_yang_name == "parent-group"):
                            for c in self.parent_group:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = ObjectGroup.Port.Objects.Object.ParentGroups.ParentGroup()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.parent_group.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "parent-group"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        self.object_name.is_set or
                        (self.nested_groups is not None and self.nested_groups.has_data()) or
                        (self.operators is not None and self.operators.has_data()) or
                        (self.parent_groups is not None and self.parent_groups.has_data()) or
                        (self.port_ranges is not None and self.port_ranges.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.object_name.yfilter != YFilter.not_set or
                        (self.nested_groups is not None and self.nested_groups.has_operation()) or
                        (self.operators is not None and self.operators.has_operation()) or
                        (self.parent_groups is not None and self.parent_groups.has_operation()) or
                        (self.port_ranges is not None and self.port_ranges.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "object" + "[object-name='" + self.object_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-infra-objmgr-oper:object-group/port/objects/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.object_name.is_set or self.object_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.object_name.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "nested-groups"):
                        if (self.nested_groups is None):
                            self.nested_groups = ObjectGroup.Port.Objects.Object.NestedGroups()
                            self.nested_groups.parent = self
                            self._children_name_map["nested_groups"] = "nested-groups"
                        return self.nested_groups

                    if (child_yang_name == "operators"):
                        if (self.operators is None):
                            self.operators = ObjectGroup.Port.Objects.Object.Operators()
                            self.operators.parent = self
                            self._children_name_map["operators"] = "operators"
                        return self.operators

                    if (child_yang_name == "parent-groups"):
                        if (self.parent_groups is None):
                            self.parent_groups = ObjectGroup.Port.Objects.Object.ParentGroups()
                            self.parent_groups.parent = self
                            self._children_name_map["parent_groups"] = "parent-groups"
                        return self.parent_groups

                    if (child_yang_name == "port-ranges"):
                        if (self.port_ranges is None):
                            self.port_ranges = ObjectGroup.Port.Objects.Object.PortRanges()
                            self.port_ranges.parent = self
                            self._children_name_map["port_ranges"] = "port-ranges"
                        return self.port_ranges

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "nested-groups" or name == "operators" or name == "parent-groups" or name == "port-ranges" or name == "object-name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "object-name"):
                        self.object_name = value
                        self.object_name.value_namespace = name_space
                        self.object_name.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.object:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.object:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "objects" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-objmgr-oper:object-group/port/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "object"):
                    for c in self.object:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = ObjectGroup.Port.Objects.Object()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.object.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "object"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (self.objects is not None and self.objects.has_data())

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.objects is not None and self.objects.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "port" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-objmgr-oper:object-group/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "objects"):
                if (self.objects is None):
                    self.objects = ObjectGroup.Port.Objects()
                    self.objects.parent = self
                    self._children_name_map["objects"] = "objects"
                return self.objects

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "objects"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Network(Entity):
        """
        Network object group
        
        .. attribute:: ipv4
        
        	IPv4 object group
        	**type**\:   :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Network.Ipv4>`
        
        .. attribute:: ipv6
        
        	IPv6 object group
        	**type**\:   :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Network.Ipv6>`
        
        

        """

        _prefix = 'infra-objmgr-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(ObjectGroup.Network, self).__init__()

            self.yang_name = "network"
            self.yang_parent_name = "object-group"

            self.ipv4 = ObjectGroup.Network.Ipv4()
            self.ipv4.parent = self
            self._children_name_map["ipv4"] = "ipv4"
            self._children_yang_names.add("ipv4")

            self.ipv6 = ObjectGroup.Network.Ipv6()
            self.ipv6.parent = self
            self._children_name_map["ipv6"] = "ipv6"
            self._children_yang_names.add("ipv6")


        class Ipv6(Entity):
            """
            IPv6 object group
            
            .. attribute:: objects
            
            	Table of Object
            	**type**\:   :py:class:`Objects <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Network.Ipv6.Objects>`
            
            

            """

            _prefix = 'infra-objmgr-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(ObjectGroup.Network.Ipv6, self).__init__()

                self.yang_name = "ipv6"
                self.yang_parent_name = "network"

                self.objects = ObjectGroup.Network.Ipv6.Objects()
                self.objects.parent = self
                self._children_name_map["objects"] = "objects"
                self._children_yang_names.add("objects")


            class Objects(Entity):
                """
                Table of Object
                
                .. attribute:: object
                
                	IPv6 object group
                	**type**\: list of    :py:class:`Object <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Network.Ipv6.Objects.Object>`
                
                

                """

                _prefix = 'infra-objmgr-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ObjectGroup.Network.Ipv6.Objects, self).__init__()

                    self.yang_name = "objects"
                    self.yang_parent_name = "ipv6"

                    self.object = YList(self)

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
                                super(ObjectGroup.Network.Ipv6.Objects, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ObjectGroup.Network.Ipv6.Objects, self).__setattr__(name, value)


                class Object(Entity):
                    """
                    IPv6 object group
                    
                    .. attribute:: object_name  <key>
                    
                    	IPv6 object group name \- maximum 64 characters
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    .. attribute:: address_ranges
                    
                    	Table of AddressRange
                    	**type**\:   :py:class:`AddressRanges <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Network.Ipv6.Objects.Object.AddressRanges>`
                    
                    .. attribute:: addresses
                    
                    	Table of Address
                    	**type**\:   :py:class:`Addresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Network.Ipv6.Objects.Object.Addresses>`
                    
                    .. attribute:: hosts
                    
                    	Table of Host
                    	**type**\:   :py:class:`Hosts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Network.Ipv6.Objects.Object.Hosts>`
                    
                    .. attribute:: nested_groups
                    
                    	Table of NestedGroup
                    	**type**\:   :py:class:`NestedGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Network.Ipv6.Objects.Object.NestedGroups>`
                    
                    .. attribute:: parent_groups
                    
                    	Table of parent object group
                    	**type**\:   :py:class:`ParentGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Network.Ipv6.Objects.Object.ParentGroups>`
                    
                    

                    """

                    _prefix = 'infra-objmgr-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ObjectGroup.Network.Ipv6.Objects.Object, self).__init__()

                        self.yang_name = "object"
                        self.yang_parent_name = "objects"

                        self.object_name = YLeaf(YType.str, "object-name")

                        self.address_ranges = ObjectGroup.Network.Ipv6.Objects.Object.AddressRanges()
                        self.address_ranges.parent = self
                        self._children_name_map["address_ranges"] = "address-ranges"
                        self._children_yang_names.add("address-ranges")

                        self.addresses = ObjectGroup.Network.Ipv6.Objects.Object.Addresses()
                        self.addresses.parent = self
                        self._children_name_map["addresses"] = "addresses"
                        self._children_yang_names.add("addresses")

                        self.hosts = ObjectGroup.Network.Ipv6.Objects.Object.Hosts()
                        self.hosts.parent = self
                        self._children_name_map["hosts"] = "hosts"
                        self._children_yang_names.add("hosts")

                        self.nested_groups = ObjectGroup.Network.Ipv6.Objects.Object.NestedGroups()
                        self.nested_groups.parent = self
                        self._children_name_map["nested_groups"] = "nested-groups"
                        self._children_yang_names.add("nested-groups")

                        self.parent_groups = ObjectGroup.Network.Ipv6.Objects.Object.ParentGroups()
                        self.parent_groups.parent = self
                        self._children_name_map["parent_groups"] = "parent-groups"
                        self._children_yang_names.add("parent-groups")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("object_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ObjectGroup.Network.Ipv6.Objects.Object, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ObjectGroup.Network.Ipv6.Objects.Object, self).__setattr__(name, value)


                    class NestedGroups(Entity):
                        """
                        Table of NestedGroup
                        
                        .. attribute:: nested_group
                        
                        	nested object group
                        	**type**\: list of    :py:class:`NestedGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Network.Ipv6.Objects.Object.NestedGroups.NestedGroup>`
                        
                        

                        """

                        _prefix = 'infra-objmgr-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(ObjectGroup.Network.Ipv6.Objects.Object.NestedGroups, self).__init__()

                            self.yang_name = "nested-groups"
                            self.yang_parent_name = "object"

                            self.nested_group = YList(self)

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
                                        super(ObjectGroup.Network.Ipv6.Objects.Object.NestedGroups, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(ObjectGroup.Network.Ipv6.Objects.Object.NestedGroups, self).__setattr__(name, value)


                        class NestedGroup(Entity):
                            """
                            nested object group
                            
                            .. attribute:: nested_group_name  <key>
                            
                            	Enter the name of a nested object group
                            	**type**\:  str
                            
                            	**length:** 1..64
                            
                            .. attribute:: nested_group_name_xr
                            
                            	Nested group
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'infra-objmgr-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(ObjectGroup.Network.Ipv6.Objects.Object.NestedGroups.NestedGroup, self).__init__()

                                self.yang_name = "nested-group"
                                self.yang_parent_name = "nested-groups"

                                self.nested_group_name = YLeaf(YType.str, "nested-group-name")

                                self.nested_group_name_xr = YLeaf(YType.str, "nested-group-name-xr")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("nested_group_name",
                                                "nested_group_name_xr") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(ObjectGroup.Network.Ipv6.Objects.Object.NestedGroups.NestedGroup, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(ObjectGroup.Network.Ipv6.Objects.Object.NestedGroups.NestedGroup, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.nested_group_name.is_set or
                                    self.nested_group_name_xr.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.nested_group_name.yfilter != YFilter.not_set or
                                    self.nested_group_name_xr.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "nested-group" + "[nested-group-name='" + self.nested_group_name.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.nested_group_name.is_set or self.nested_group_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.nested_group_name.get_name_leafdata())
                                if (self.nested_group_name_xr.is_set or self.nested_group_name_xr.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.nested_group_name_xr.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "nested-group-name" or name == "nested-group-name-xr"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "nested-group-name"):
                                    self.nested_group_name = value
                                    self.nested_group_name.value_namespace = name_space
                                    self.nested_group_name.value_namespace_prefix = name_space_prefix
                                if(value_path == "nested-group-name-xr"):
                                    self.nested_group_name_xr = value
                                    self.nested_group_name_xr.value_namespace = name_space
                                    self.nested_group_name_xr.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.nested_group:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.nested_group:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "nested-groups" + path_buffer

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

                            if (child_yang_name == "nested-group"):
                                for c in self.nested_group:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = ObjectGroup.Network.Ipv6.Objects.Object.NestedGroups.NestedGroup()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.nested_group.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "nested-group"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass


                    class Addresses(Entity):
                        """
                        Table of Address
                        
                        .. attribute:: address
                        
                        	IPv6 address
                        	**type**\: list of    :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Network.Ipv6.Objects.Object.Addresses.Address>`
                        
                        

                        """

                        _prefix = 'infra-objmgr-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(ObjectGroup.Network.Ipv6.Objects.Object.Addresses, self).__init__()

                            self.yang_name = "addresses"
                            self.yang_parent_name = "object"

                            self.address = YList(self)

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
                                        super(ObjectGroup.Network.Ipv6.Objects.Object.Addresses, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(ObjectGroup.Network.Ipv6.Objects.Object.Addresses, self).__setattr__(name, value)


                        class Address(Entity):
                            """
                            IPv6 address
                            
                            .. attribute:: prefix
                            
                            	IPv6 prefix x\:x\:\:x/y
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: prefix_length
                            
                            	Prefix of the IP Address
                            	**type**\:  int
                            
                            	**range:** 0..128
                            
                            .. attribute:: prefix_length_xr
                            
                            	Prefix length
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: prefix_xr
                            
                            	IPv4 Address
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-objmgr-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(ObjectGroup.Network.Ipv6.Objects.Object.Addresses.Address, self).__init__()

                                self.yang_name = "address"
                                self.yang_parent_name = "addresses"

                                self.prefix = YLeaf(YType.str, "prefix")

                                self.prefix_length = YLeaf(YType.uint8, "prefix-length")

                                self.prefix_length_xr = YLeaf(YType.uint32, "prefix-length-xr")

                                self.prefix_xr = YLeaf(YType.str, "prefix-xr")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("prefix",
                                                "prefix_length",
                                                "prefix_length_xr",
                                                "prefix_xr") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(ObjectGroup.Network.Ipv6.Objects.Object.Addresses.Address, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(ObjectGroup.Network.Ipv6.Objects.Object.Addresses.Address, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.prefix.is_set or
                                    self.prefix_length.is_set or
                                    self.prefix_length_xr.is_set or
                                    self.prefix_xr.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.prefix.yfilter != YFilter.not_set or
                                    self.prefix_length.yfilter != YFilter.not_set or
                                    self.prefix_length_xr.yfilter != YFilter.not_set or
                                    self.prefix_xr.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "address" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.prefix.is_set or self.prefix.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.prefix.get_name_leafdata())
                                if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.prefix_length.get_name_leafdata())
                                if (self.prefix_length_xr.is_set or self.prefix_length_xr.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.prefix_length_xr.get_name_leafdata())
                                if (self.prefix_xr.is_set or self.prefix_xr.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.prefix_xr.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "prefix" or name == "prefix-length" or name == "prefix-length-xr" or name == "prefix-xr"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "prefix"):
                                    self.prefix = value
                                    self.prefix.value_namespace = name_space
                                    self.prefix.value_namespace_prefix = name_space_prefix
                                if(value_path == "prefix-length"):
                                    self.prefix_length = value
                                    self.prefix_length.value_namespace = name_space
                                    self.prefix_length.value_namespace_prefix = name_space_prefix
                                if(value_path == "prefix-length-xr"):
                                    self.prefix_length_xr = value
                                    self.prefix_length_xr.value_namespace = name_space
                                    self.prefix_length_xr.value_namespace_prefix = name_space_prefix
                                if(value_path == "prefix-xr"):
                                    self.prefix_xr = value
                                    self.prefix_xr.value_namespace = name_space
                                    self.prefix_xr.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.address:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.address:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "addresses" + path_buffer

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

                            if (child_yang_name == "address"):
                                for c in self.address:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = ObjectGroup.Network.Ipv6.Objects.Object.Addresses.Address()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.address.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "address"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass


                    class AddressRanges(Entity):
                        """
                        Table of AddressRange
                        
                        .. attribute:: address_range
                        
                        	Range of host addresses
                        	**type**\: list of    :py:class:`AddressRange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Network.Ipv6.Objects.Object.AddressRanges.AddressRange>`
                        
                        

                        """

                        _prefix = 'infra-objmgr-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(ObjectGroup.Network.Ipv6.Objects.Object.AddressRanges, self).__init__()

                            self.yang_name = "address-ranges"
                            self.yang_parent_name = "object"

                            self.address_range = YList(self)

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
                                        super(ObjectGroup.Network.Ipv6.Objects.Object.AddressRanges, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(ObjectGroup.Network.Ipv6.Objects.Object.AddressRanges, self).__setattr__(name, value)


                        class AddressRange(Entity):
                            """
                            Range of host addresses
                            
                            .. attribute:: end_address
                            
                            	IPv6 address
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: end_address_xr
                            
                            	Range end address
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: start_address
                            
                            	IPv6 address
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: start_address_xr
                            
                            	Range start address
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-objmgr-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(ObjectGroup.Network.Ipv6.Objects.Object.AddressRanges.AddressRange, self).__init__()

                                self.yang_name = "address-range"
                                self.yang_parent_name = "address-ranges"

                                self.end_address = YLeaf(YType.str, "end-address")

                                self.end_address_xr = YLeaf(YType.str, "end-address-xr")

                                self.start_address = YLeaf(YType.str, "start-address")

                                self.start_address_xr = YLeaf(YType.str, "start-address-xr")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("end_address",
                                                "end_address_xr",
                                                "start_address",
                                                "start_address_xr") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(ObjectGroup.Network.Ipv6.Objects.Object.AddressRanges.AddressRange, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(ObjectGroup.Network.Ipv6.Objects.Object.AddressRanges.AddressRange, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.end_address.is_set or
                                    self.end_address_xr.is_set or
                                    self.start_address.is_set or
                                    self.start_address_xr.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.end_address.yfilter != YFilter.not_set or
                                    self.end_address_xr.yfilter != YFilter.not_set or
                                    self.start_address.yfilter != YFilter.not_set or
                                    self.start_address_xr.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "address-range" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.end_address.is_set or self.end_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.end_address.get_name_leafdata())
                                if (self.end_address_xr.is_set or self.end_address_xr.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.end_address_xr.get_name_leafdata())
                                if (self.start_address.is_set or self.start_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.start_address.get_name_leafdata())
                                if (self.start_address_xr.is_set or self.start_address_xr.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.start_address_xr.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "end-address" or name == "end-address-xr" or name == "start-address" or name == "start-address-xr"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "end-address"):
                                    self.end_address = value
                                    self.end_address.value_namespace = name_space
                                    self.end_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "end-address-xr"):
                                    self.end_address_xr = value
                                    self.end_address_xr.value_namespace = name_space
                                    self.end_address_xr.value_namespace_prefix = name_space_prefix
                                if(value_path == "start-address"):
                                    self.start_address = value
                                    self.start_address.value_namespace = name_space
                                    self.start_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "start-address-xr"):
                                    self.start_address_xr = value
                                    self.start_address_xr.value_namespace = name_space
                                    self.start_address_xr.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.address_range:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.address_range:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "address-ranges" + path_buffer

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

                            if (child_yang_name == "address-range"):
                                for c in self.address_range:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = ObjectGroup.Network.Ipv6.Objects.Object.AddressRanges.AddressRange()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.address_range.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "address-range"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass


                    class ParentGroups(Entity):
                        """
                        Table of parent object group
                        
                        .. attribute:: parent_group
                        
                        	Parent object group
                        	**type**\: list of    :py:class:`ParentGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Network.Ipv6.Objects.Object.ParentGroups.ParentGroup>`
                        
                        

                        """

                        _prefix = 'infra-objmgr-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(ObjectGroup.Network.Ipv6.Objects.Object.ParentGroups, self).__init__()

                            self.yang_name = "parent-groups"
                            self.yang_parent_name = "object"

                            self.parent_group = YList(self)

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
                                        super(ObjectGroup.Network.Ipv6.Objects.Object.ParentGroups, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(ObjectGroup.Network.Ipv6.Objects.Object.ParentGroups, self).__setattr__(name, value)


                        class ParentGroup(Entity):
                            """
                            Parent object group
                            
                            .. attribute:: parent_group_name  <key>
                            
                            	Nested object group
                            	**type**\:  str
                            
                            	**length:** 1..64
                            
                            .. attribute:: parent_name
                            
                            	Parent node
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'infra-objmgr-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(ObjectGroup.Network.Ipv6.Objects.Object.ParentGroups.ParentGroup, self).__init__()

                                self.yang_name = "parent-group"
                                self.yang_parent_name = "parent-groups"

                                self.parent_group_name = YLeaf(YType.str, "parent-group-name")

                                self.parent_name = YLeaf(YType.str, "parent-name")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("parent_group_name",
                                                "parent_name") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(ObjectGroup.Network.Ipv6.Objects.Object.ParentGroups.ParentGroup, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(ObjectGroup.Network.Ipv6.Objects.Object.ParentGroups.ParentGroup, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.parent_group_name.is_set or
                                    self.parent_name.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.parent_group_name.yfilter != YFilter.not_set or
                                    self.parent_name.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "parent-group" + "[parent-group-name='" + self.parent_group_name.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.parent_group_name.is_set or self.parent_group_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.parent_group_name.get_name_leafdata())
                                if (self.parent_name.is_set or self.parent_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.parent_name.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "parent-group-name" or name == "parent-name"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "parent-group-name"):
                                    self.parent_group_name = value
                                    self.parent_group_name.value_namespace = name_space
                                    self.parent_group_name.value_namespace_prefix = name_space_prefix
                                if(value_path == "parent-name"):
                                    self.parent_name = value
                                    self.parent_name.value_namespace = name_space
                                    self.parent_name.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.parent_group:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.parent_group:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "parent-groups" + path_buffer

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

                            if (child_yang_name == "parent-group"):
                                for c in self.parent_group:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = ObjectGroup.Network.Ipv6.Objects.Object.ParentGroups.ParentGroup()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.parent_group.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "parent-group"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass


                    class Hosts(Entity):
                        """
                        Table of Host
                        
                        .. attribute:: host
                        
                        	A single host address
                        	**type**\: list of    :py:class:`Host <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Network.Ipv6.Objects.Object.Hosts.Host>`
                        
                        

                        """

                        _prefix = 'infra-objmgr-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(ObjectGroup.Network.Ipv6.Objects.Object.Hosts, self).__init__()

                            self.yang_name = "hosts"
                            self.yang_parent_name = "object"

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
                                        super(ObjectGroup.Network.Ipv6.Objects.Object.Hosts, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(ObjectGroup.Network.Ipv6.Objects.Object.Hosts, self).__setattr__(name, value)


                        class Host(Entity):
                            """
                            A single host address
                            
                            .. attribute:: host_address  <key>
                            
                            	host ipv6 address
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: host_address_xr
                            
                            	Host address
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-objmgr-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(ObjectGroup.Network.Ipv6.Objects.Object.Hosts.Host, self).__init__()

                                self.yang_name = "host"
                                self.yang_parent_name = "hosts"

                                self.host_address = YLeaf(YType.str, "host-address")

                                self.host_address_xr = YLeaf(YType.str, "host-address-xr")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("host_address",
                                                "host_address_xr") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(ObjectGroup.Network.Ipv6.Objects.Object.Hosts.Host, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(ObjectGroup.Network.Ipv6.Objects.Object.Hosts.Host, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.host_address.is_set or
                                    self.host_address_xr.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.host_address.yfilter != YFilter.not_set or
                                    self.host_address_xr.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "host" + "[host-address='" + self.host_address.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.host_address.is_set or self.host_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.host_address.get_name_leafdata())
                                if (self.host_address_xr.is_set or self.host_address_xr.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.host_address_xr.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "host-address" or name == "host-address-xr"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "host-address"):
                                    self.host_address = value
                                    self.host_address.value_namespace = name_space
                                    self.host_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "host-address-xr"):
                                    self.host_address_xr = value
                                    self.host_address_xr.value_namespace = name_space
                                    self.host_address_xr.value_namespace_prefix = name_space_prefix

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

                            if (child_yang_name == "host"):
                                for c in self.host:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = ObjectGroup.Network.Ipv6.Objects.Object.Hosts.Host()
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

                    def has_data(self):
                        return (
                            self.object_name.is_set or
                            (self.address_ranges is not None and self.address_ranges.has_data()) or
                            (self.addresses is not None and self.addresses.has_data()) or
                            (self.hosts is not None and self.hosts.has_data()) or
                            (self.nested_groups is not None and self.nested_groups.has_data()) or
                            (self.parent_groups is not None and self.parent_groups.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.object_name.yfilter != YFilter.not_set or
                            (self.address_ranges is not None and self.address_ranges.has_operation()) or
                            (self.addresses is not None and self.addresses.has_operation()) or
                            (self.hosts is not None and self.hosts.has_operation()) or
                            (self.nested_groups is not None and self.nested_groups.has_operation()) or
                            (self.parent_groups is not None and self.parent_groups.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "object" + "[object-name='" + self.object_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-infra-objmgr-oper:object-group/network/ipv6/objects/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.object_name.is_set or self.object_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.object_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "address-ranges"):
                            if (self.address_ranges is None):
                                self.address_ranges = ObjectGroup.Network.Ipv6.Objects.Object.AddressRanges()
                                self.address_ranges.parent = self
                                self._children_name_map["address_ranges"] = "address-ranges"
                            return self.address_ranges

                        if (child_yang_name == "addresses"):
                            if (self.addresses is None):
                                self.addresses = ObjectGroup.Network.Ipv6.Objects.Object.Addresses()
                                self.addresses.parent = self
                                self._children_name_map["addresses"] = "addresses"
                            return self.addresses

                        if (child_yang_name == "hosts"):
                            if (self.hosts is None):
                                self.hosts = ObjectGroup.Network.Ipv6.Objects.Object.Hosts()
                                self.hosts.parent = self
                                self._children_name_map["hosts"] = "hosts"
                            return self.hosts

                        if (child_yang_name == "nested-groups"):
                            if (self.nested_groups is None):
                                self.nested_groups = ObjectGroup.Network.Ipv6.Objects.Object.NestedGroups()
                                self.nested_groups.parent = self
                                self._children_name_map["nested_groups"] = "nested-groups"
                            return self.nested_groups

                        if (child_yang_name == "parent-groups"):
                            if (self.parent_groups is None):
                                self.parent_groups = ObjectGroup.Network.Ipv6.Objects.Object.ParentGroups()
                                self.parent_groups.parent = self
                                self._children_name_map["parent_groups"] = "parent-groups"
                            return self.parent_groups

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "address-ranges" or name == "addresses" or name == "hosts" or name == "nested-groups" or name == "parent-groups" or name == "object-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "object-name"):
                            self.object_name = value
                            self.object_name.value_namespace = name_space
                            self.object_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.object:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.object:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "objects" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-infra-objmgr-oper:object-group/network/ipv6/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "object"):
                        for c in self.object:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = ObjectGroup.Network.Ipv6.Objects.Object()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.object.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "object"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (self.objects is not None and self.objects.has_data())

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.objects is not None and self.objects.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ipv6" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-objmgr-oper:object-group/network/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "objects"):
                    if (self.objects is None):
                        self.objects = ObjectGroup.Network.Ipv6.Objects()
                        self.objects.parent = self
                        self._children_name_map["objects"] = "objects"
                    return self.objects

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "objects"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class Ipv4(Entity):
            """
            IPv4 object group
            
            .. attribute:: objects
            
            	Table of Object
            	**type**\:   :py:class:`Objects <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Network.Ipv4.Objects>`
            
            

            """

            _prefix = 'infra-objmgr-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(ObjectGroup.Network.Ipv4, self).__init__()

                self.yang_name = "ipv4"
                self.yang_parent_name = "network"

                self.objects = ObjectGroup.Network.Ipv4.Objects()
                self.objects.parent = self
                self._children_name_map["objects"] = "objects"
                self._children_yang_names.add("objects")


            class Objects(Entity):
                """
                Table of Object
                
                .. attribute:: object
                
                	IPv4 object group
                	**type**\: list of    :py:class:`Object <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Network.Ipv4.Objects.Object>`
                
                

                """

                _prefix = 'infra-objmgr-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ObjectGroup.Network.Ipv4.Objects, self).__init__()

                    self.yang_name = "objects"
                    self.yang_parent_name = "ipv4"

                    self.object = YList(self)

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
                                super(ObjectGroup.Network.Ipv4.Objects, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ObjectGroup.Network.Ipv4.Objects, self).__setattr__(name, value)


                class Object(Entity):
                    """
                    IPv4 object group
                    
                    .. attribute:: object_name  <key>
                    
                    	IPv4 object group name \- maximum 64 characters
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    .. attribute:: address_ranges
                    
                    	Table of AddressRange
                    	**type**\:   :py:class:`AddressRanges <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Network.Ipv4.Objects.Object.AddressRanges>`
                    
                    .. attribute:: addresses
                    
                    	Table of Address
                    	**type**\:   :py:class:`Addresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Network.Ipv4.Objects.Object.Addresses>`
                    
                    .. attribute:: hosts
                    
                    	Table of Host
                    	**type**\:   :py:class:`Hosts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Network.Ipv4.Objects.Object.Hosts>`
                    
                    .. attribute:: nested_groups
                    
                    	Table of NestedGroup
                    	**type**\:   :py:class:`NestedGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Network.Ipv4.Objects.Object.NestedGroups>`
                    
                    .. attribute:: parent_groups
                    
                    	Table of parent object group
                    	**type**\:   :py:class:`ParentGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Network.Ipv4.Objects.Object.ParentGroups>`
                    
                    

                    """

                    _prefix = 'infra-objmgr-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ObjectGroup.Network.Ipv4.Objects.Object, self).__init__()

                        self.yang_name = "object"
                        self.yang_parent_name = "objects"

                        self.object_name = YLeaf(YType.str, "object-name")

                        self.address_ranges = ObjectGroup.Network.Ipv4.Objects.Object.AddressRanges()
                        self.address_ranges.parent = self
                        self._children_name_map["address_ranges"] = "address-ranges"
                        self._children_yang_names.add("address-ranges")

                        self.addresses = ObjectGroup.Network.Ipv4.Objects.Object.Addresses()
                        self.addresses.parent = self
                        self._children_name_map["addresses"] = "addresses"
                        self._children_yang_names.add("addresses")

                        self.hosts = ObjectGroup.Network.Ipv4.Objects.Object.Hosts()
                        self.hosts.parent = self
                        self._children_name_map["hosts"] = "hosts"
                        self._children_yang_names.add("hosts")

                        self.nested_groups = ObjectGroup.Network.Ipv4.Objects.Object.NestedGroups()
                        self.nested_groups.parent = self
                        self._children_name_map["nested_groups"] = "nested-groups"
                        self._children_yang_names.add("nested-groups")

                        self.parent_groups = ObjectGroup.Network.Ipv4.Objects.Object.ParentGroups()
                        self.parent_groups.parent = self
                        self._children_name_map["parent_groups"] = "parent-groups"
                        self._children_yang_names.add("parent-groups")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("object_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ObjectGroup.Network.Ipv4.Objects.Object, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ObjectGroup.Network.Ipv4.Objects.Object, self).__setattr__(name, value)


                    class NestedGroups(Entity):
                        """
                        Table of NestedGroup
                        
                        .. attribute:: nested_group
                        
                        	Nested object group
                        	**type**\: list of    :py:class:`NestedGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Network.Ipv4.Objects.Object.NestedGroups.NestedGroup>`
                        
                        

                        """

                        _prefix = 'infra-objmgr-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(ObjectGroup.Network.Ipv4.Objects.Object.NestedGroups, self).__init__()

                            self.yang_name = "nested-groups"
                            self.yang_parent_name = "object"

                            self.nested_group = YList(self)

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
                                        super(ObjectGroup.Network.Ipv4.Objects.Object.NestedGroups, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(ObjectGroup.Network.Ipv4.Objects.Object.NestedGroups, self).__setattr__(name, value)


                        class NestedGroup(Entity):
                            """
                            Nested object group
                            
                            .. attribute:: nested_group_name  <key>
                            
                            	Nested object group
                            	**type**\:  str
                            
                            	**length:** 1..64
                            
                            .. attribute:: nested_group_name_xr
                            
                            	Nested group
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'infra-objmgr-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(ObjectGroup.Network.Ipv4.Objects.Object.NestedGroups.NestedGroup, self).__init__()

                                self.yang_name = "nested-group"
                                self.yang_parent_name = "nested-groups"

                                self.nested_group_name = YLeaf(YType.str, "nested-group-name")

                                self.nested_group_name_xr = YLeaf(YType.str, "nested-group-name-xr")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("nested_group_name",
                                                "nested_group_name_xr") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(ObjectGroup.Network.Ipv4.Objects.Object.NestedGroups.NestedGroup, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(ObjectGroup.Network.Ipv4.Objects.Object.NestedGroups.NestedGroup, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.nested_group_name.is_set or
                                    self.nested_group_name_xr.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.nested_group_name.yfilter != YFilter.not_set or
                                    self.nested_group_name_xr.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "nested-group" + "[nested-group-name='" + self.nested_group_name.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.nested_group_name.is_set or self.nested_group_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.nested_group_name.get_name_leafdata())
                                if (self.nested_group_name_xr.is_set or self.nested_group_name_xr.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.nested_group_name_xr.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "nested-group-name" or name == "nested-group-name-xr"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "nested-group-name"):
                                    self.nested_group_name = value
                                    self.nested_group_name.value_namespace = name_space
                                    self.nested_group_name.value_namespace_prefix = name_space_prefix
                                if(value_path == "nested-group-name-xr"):
                                    self.nested_group_name_xr = value
                                    self.nested_group_name_xr.value_namespace = name_space
                                    self.nested_group_name_xr.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.nested_group:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.nested_group:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "nested-groups" + path_buffer

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

                            if (child_yang_name == "nested-group"):
                                for c in self.nested_group:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = ObjectGroup.Network.Ipv4.Objects.Object.NestedGroups.NestedGroup()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.nested_group.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "nested-group"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass


                    class Addresses(Entity):
                        """
                        Table of Address
                        
                        .. attribute:: address
                        
                        	IPv4 address
                        	**type**\: list of    :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Network.Ipv4.Objects.Object.Addresses.Address>`
                        
                        

                        """

                        _prefix = 'infra-objmgr-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(ObjectGroup.Network.Ipv4.Objects.Object.Addresses, self).__init__()

                            self.yang_name = "addresses"
                            self.yang_parent_name = "object"

                            self.address = YList(self)

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
                                        super(ObjectGroup.Network.Ipv4.Objects.Object.Addresses, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(ObjectGroup.Network.Ipv4.Objects.Object.Addresses, self).__setattr__(name, value)


                        class Address(Entity):
                            """
                            IPv4 address
                            
                            .. attribute:: prefix
                            
                            	IPv4 address/prefix
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: prefix_length
                            
                            	Prefix of the IP Address
                            	**type**\:  int
                            
                            	**range:** 0..32
                            
                            .. attribute:: prefix_length_xr
                            
                            	Prefix length
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: prefix_xr
                            
                            	IPv4 Address
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-objmgr-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(ObjectGroup.Network.Ipv4.Objects.Object.Addresses.Address, self).__init__()

                                self.yang_name = "address"
                                self.yang_parent_name = "addresses"

                                self.prefix = YLeaf(YType.str, "prefix")

                                self.prefix_length = YLeaf(YType.uint8, "prefix-length")

                                self.prefix_length_xr = YLeaf(YType.uint32, "prefix-length-xr")

                                self.prefix_xr = YLeaf(YType.str, "prefix-xr")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("prefix",
                                                "prefix_length",
                                                "prefix_length_xr",
                                                "prefix_xr") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(ObjectGroup.Network.Ipv4.Objects.Object.Addresses.Address, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(ObjectGroup.Network.Ipv4.Objects.Object.Addresses.Address, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.prefix.is_set or
                                    self.prefix_length.is_set or
                                    self.prefix_length_xr.is_set or
                                    self.prefix_xr.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.prefix.yfilter != YFilter.not_set or
                                    self.prefix_length.yfilter != YFilter.not_set or
                                    self.prefix_length_xr.yfilter != YFilter.not_set or
                                    self.prefix_xr.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "address" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.prefix.is_set or self.prefix.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.prefix.get_name_leafdata())
                                if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.prefix_length.get_name_leafdata())
                                if (self.prefix_length_xr.is_set or self.prefix_length_xr.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.prefix_length_xr.get_name_leafdata())
                                if (self.prefix_xr.is_set or self.prefix_xr.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.prefix_xr.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "prefix" or name == "prefix-length" or name == "prefix-length-xr" or name == "prefix-xr"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "prefix"):
                                    self.prefix = value
                                    self.prefix.value_namespace = name_space
                                    self.prefix.value_namespace_prefix = name_space_prefix
                                if(value_path == "prefix-length"):
                                    self.prefix_length = value
                                    self.prefix_length.value_namespace = name_space
                                    self.prefix_length.value_namespace_prefix = name_space_prefix
                                if(value_path == "prefix-length-xr"):
                                    self.prefix_length_xr = value
                                    self.prefix_length_xr.value_namespace = name_space
                                    self.prefix_length_xr.value_namespace_prefix = name_space_prefix
                                if(value_path == "prefix-xr"):
                                    self.prefix_xr = value
                                    self.prefix_xr.value_namespace = name_space
                                    self.prefix_xr.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.address:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.address:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "addresses" + path_buffer

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

                            if (child_yang_name == "address"):
                                for c in self.address:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = ObjectGroup.Network.Ipv4.Objects.Object.Addresses.Address()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.address.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "address"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass


                    class AddressRanges(Entity):
                        """
                        Table of AddressRange
                        
                        .. attribute:: address_range
                        
                        	Range of host addresses
                        	**type**\: list of    :py:class:`AddressRange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Network.Ipv4.Objects.Object.AddressRanges.AddressRange>`
                        
                        

                        """

                        _prefix = 'infra-objmgr-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(ObjectGroup.Network.Ipv4.Objects.Object.AddressRanges, self).__init__()

                            self.yang_name = "address-ranges"
                            self.yang_parent_name = "object"

                            self.address_range = YList(self)

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
                                        super(ObjectGroup.Network.Ipv4.Objects.Object.AddressRanges, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(ObjectGroup.Network.Ipv4.Objects.Object.AddressRanges, self).__setattr__(name, value)


                        class AddressRange(Entity):
                            """
                            Range of host addresses
                            
                            .. attribute:: end_address
                            
                            	IPv4 address
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: end_address_xr
                            
                            	Range end address
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: start_address
                            
                            	IPv4 address
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: start_address_xr
                            
                            	Range start address
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-objmgr-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(ObjectGroup.Network.Ipv4.Objects.Object.AddressRanges.AddressRange, self).__init__()

                                self.yang_name = "address-range"
                                self.yang_parent_name = "address-ranges"

                                self.end_address = YLeaf(YType.str, "end-address")

                                self.end_address_xr = YLeaf(YType.str, "end-address-xr")

                                self.start_address = YLeaf(YType.str, "start-address")

                                self.start_address_xr = YLeaf(YType.str, "start-address-xr")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("end_address",
                                                "end_address_xr",
                                                "start_address",
                                                "start_address_xr") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(ObjectGroup.Network.Ipv4.Objects.Object.AddressRanges.AddressRange, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(ObjectGroup.Network.Ipv4.Objects.Object.AddressRanges.AddressRange, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.end_address.is_set or
                                    self.end_address_xr.is_set or
                                    self.start_address.is_set or
                                    self.start_address_xr.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.end_address.yfilter != YFilter.not_set or
                                    self.end_address_xr.yfilter != YFilter.not_set or
                                    self.start_address.yfilter != YFilter.not_set or
                                    self.start_address_xr.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "address-range" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.end_address.is_set or self.end_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.end_address.get_name_leafdata())
                                if (self.end_address_xr.is_set or self.end_address_xr.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.end_address_xr.get_name_leafdata())
                                if (self.start_address.is_set or self.start_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.start_address.get_name_leafdata())
                                if (self.start_address_xr.is_set or self.start_address_xr.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.start_address_xr.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "end-address" or name == "end-address-xr" or name == "start-address" or name == "start-address-xr"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "end-address"):
                                    self.end_address = value
                                    self.end_address.value_namespace = name_space
                                    self.end_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "end-address-xr"):
                                    self.end_address_xr = value
                                    self.end_address_xr.value_namespace = name_space
                                    self.end_address_xr.value_namespace_prefix = name_space_prefix
                                if(value_path == "start-address"):
                                    self.start_address = value
                                    self.start_address.value_namespace = name_space
                                    self.start_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "start-address-xr"):
                                    self.start_address_xr = value
                                    self.start_address_xr.value_namespace = name_space
                                    self.start_address_xr.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.address_range:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.address_range:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "address-ranges" + path_buffer

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

                            if (child_yang_name == "address-range"):
                                for c in self.address_range:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = ObjectGroup.Network.Ipv4.Objects.Object.AddressRanges.AddressRange()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.address_range.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "address-range"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass


                    class ParentGroups(Entity):
                        """
                        Table of parent object group
                        
                        .. attribute:: parent_group
                        
                        	Parent object group
                        	**type**\: list of    :py:class:`ParentGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Network.Ipv4.Objects.Object.ParentGroups.ParentGroup>`
                        
                        

                        """

                        _prefix = 'infra-objmgr-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(ObjectGroup.Network.Ipv4.Objects.Object.ParentGroups, self).__init__()

                            self.yang_name = "parent-groups"
                            self.yang_parent_name = "object"

                            self.parent_group = YList(self)

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
                                        super(ObjectGroup.Network.Ipv4.Objects.Object.ParentGroups, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(ObjectGroup.Network.Ipv4.Objects.Object.ParentGroups, self).__setattr__(name, value)


                        class ParentGroup(Entity):
                            """
                            Parent object group
                            
                            .. attribute:: parent_group_name  <key>
                            
                            	Nested object group
                            	**type**\:  str
                            
                            	**length:** 1..64
                            
                            .. attribute:: parent_name
                            
                            	Parent node
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'infra-objmgr-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(ObjectGroup.Network.Ipv4.Objects.Object.ParentGroups.ParentGroup, self).__init__()

                                self.yang_name = "parent-group"
                                self.yang_parent_name = "parent-groups"

                                self.parent_group_name = YLeaf(YType.str, "parent-group-name")

                                self.parent_name = YLeaf(YType.str, "parent-name")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("parent_group_name",
                                                "parent_name") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(ObjectGroup.Network.Ipv4.Objects.Object.ParentGroups.ParentGroup, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(ObjectGroup.Network.Ipv4.Objects.Object.ParentGroups.ParentGroup, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.parent_group_name.is_set or
                                    self.parent_name.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.parent_group_name.yfilter != YFilter.not_set or
                                    self.parent_name.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "parent-group" + "[parent-group-name='" + self.parent_group_name.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.parent_group_name.is_set or self.parent_group_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.parent_group_name.get_name_leafdata())
                                if (self.parent_name.is_set or self.parent_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.parent_name.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "parent-group-name" or name == "parent-name"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "parent-group-name"):
                                    self.parent_group_name = value
                                    self.parent_group_name.value_namespace = name_space
                                    self.parent_group_name.value_namespace_prefix = name_space_prefix
                                if(value_path == "parent-name"):
                                    self.parent_name = value
                                    self.parent_name.value_namespace = name_space
                                    self.parent_name.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.parent_group:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.parent_group:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "parent-groups" + path_buffer

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

                            if (child_yang_name == "parent-group"):
                                for c in self.parent_group:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = ObjectGroup.Network.Ipv4.Objects.Object.ParentGroups.ParentGroup()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.parent_group.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "parent-group"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass


                    class Hosts(Entity):
                        """
                        Table of Host
                        
                        .. attribute:: host
                        
                        	A single host address
                        	**type**\: list of    :py:class:`Host <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Network.Ipv4.Objects.Object.Hosts.Host>`
                        
                        

                        """

                        _prefix = 'infra-objmgr-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(ObjectGroup.Network.Ipv4.Objects.Object.Hosts, self).__init__()

                            self.yang_name = "hosts"
                            self.yang_parent_name = "object"

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
                                        super(ObjectGroup.Network.Ipv4.Objects.Object.Hosts, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(ObjectGroup.Network.Ipv4.Objects.Object.Hosts, self).__setattr__(name, value)


                        class Host(Entity):
                            """
                            A single host address
                            
                            .. attribute:: host_address  <key>
                            
                            	Host ipv4 address
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: host_address_xr
                            
                            	Host address
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-objmgr-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(ObjectGroup.Network.Ipv4.Objects.Object.Hosts.Host, self).__init__()

                                self.yang_name = "host"
                                self.yang_parent_name = "hosts"

                                self.host_address = YLeaf(YType.str, "host-address")

                                self.host_address_xr = YLeaf(YType.str, "host-address-xr")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("host_address",
                                                "host_address_xr") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(ObjectGroup.Network.Ipv4.Objects.Object.Hosts.Host, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(ObjectGroup.Network.Ipv4.Objects.Object.Hosts.Host, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.host_address.is_set or
                                    self.host_address_xr.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.host_address.yfilter != YFilter.not_set or
                                    self.host_address_xr.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "host" + "[host-address='" + self.host_address.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.host_address.is_set or self.host_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.host_address.get_name_leafdata())
                                if (self.host_address_xr.is_set or self.host_address_xr.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.host_address_xr.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "host-address" or name == "host-address-xr"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "host-address"):
                                    self.host_address = value
                                    self.host_address.value_namespace = name_space
                                    self.host_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "host-address-xr"):
                                    self.host_address_xr = value
                                    self.host_address_xr.value_namespace = name_space
                                    self.host_address_xr.value_namespace_prefix = name_space_prefix

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

                            if (child_yang_name == "host"):
                                for c in self.host:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = ObjectGroup.Network.Ipv4.Objects.Object.Hosts.Host()
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

                    def has_data(self):
                        return (
                            self.object_name.is_set or
                            (self.address_ranges is not None and self.address_ranges.has_data()) or
                            (self.addresses is not None and self.addresses.has_data()) or
                            (self.hosts is not None and self.hosts.has_data()) or
                            (self.nested_groups is not None and self.nested_groups.has_data()) or
                            (self.parent_groups is not None and self.parent_groups.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.object_name.yfilter != YFilter.not_set or
                            (self.address_ranges is not None and self.address_ranges.has_operation()) or
                            (self.addresses is not None and self.addresses.has_operation()) or
                            (self.hosts is not None and self.hosts.has_operation()) or
                            (self.nested_groups is not None and self.nested_groups.has_operation()) or
                            (self.parent_groups is not None and self.parent_groups.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "object" + "[object-name='" + self.object_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-infra-objmgr-oper:object-group/network/ipv4/objects/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.object_name.is_set or self.object_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.object_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "address-ranges"):
                            if (self.address_ranges is None):
                                self.address_ranges = ObjectGroup.Network.Ipv4.Objects.Object.AddressRanges()
                                self.address_ranges.parent = self
                                self._children_name_map["address_ranges"] = "address-ranges"
                            return self.address_ranges

                        if (child_yang_name == "addresses"):
                            if (self.addresses is None):
                                self.addresses = ObjectGroup.Network.Ipv4.Objects.Object.Addresses()
                                self.addresses.parent = self
                                self._children_name_map["addresses"] = "addresses"
                            return self.addresses

                        if (child_yang_name == "hosts"):
                            if (self.hosts is None):
                                self.hosts = ObjectGroup.Network.Ipv4.Objects.Object.Hosts()
                                self.hosts.parent = self
                                self._children_name_map["hosts"] = "hosts"
                            return self.hosts

                        if (child_yang_name == "nested-groups"):
                            if (self.nested_groups is None):
                                self.nested_groups = ObjectGroup.Network.Ipv4.Objects.Object.NestedGroups()
                                self.nested_groups.parent = self
                                self._children_name_map["nested_groups"] = "nested-groups"
                            return self.nested_groups

                        if (child_yang_name == "parent-groups"):
                            if (self.parent_groups is None):
                                self.parent_groups = ObjectGroup.Network.Ipv4.Objects.Object.ParentGroups()
                                self.parent_groups.parent = self
                                self._children_name_map["parent_groups"] = "parent-groups"
                            return self.parent_groups

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "address-ranges" or name == "addresses" or name == "hosts" or name == "nested-groups" or name == "parent-groups" or name == "object-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "object-name"):
                            self.object_name = value
                            self.object_name.value_namespace = name_space
                            self.object_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.object:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.object:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "objects" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-infra-objmgr-oper:object-group/network/ipv4/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "object"):
                        for c in self.object:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = ObjectGroup.Network.Ipv4.Objects.Object()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.object.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "object"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (self.objects is not None and self.objects.has_data())

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.objects is not None and self.objects.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ipv4" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-objmgr-oper:object-group/network/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "objects"):
                    if (self.objects is None):
                        self.objects = ObjectGroup.Network.Ipv4.Objects()
                        self.objects.parent = self
                        self._children_name_map["objects"] = "objects"
                    return self.objects

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "objects"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                (self.ipv4 is not None and self.ipv4.has_data()) or
                (self.ipv6 is not None and self.ipv6.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.ipv4 is not None and self.ipv4.has_operation()) or
                (self.ipv6 is not None and self.ipv6.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "network" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-objmgr-oper:object-group/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ipv4"):
                if (self.ipv4 is None):
                    self.ipv4 = ObjectGroup.Network.Ipv4()
                    self.ipv4.parent = self
                    self._children_name_map["ipv4"] = "ipv4"
                return self.ipv4

            if (child_yang_name == "ipv6"):
                if (self.ipv6 is None):
                    self.ipv6 = ObjectGroup.Network.Ipv6()
                    self.ipv6.parent = self
                    self._children_name_map["ipv6"] = "ipv6"
                return self.ipv6

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ipv4" or name == "ipv6"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.network is not None and self.network.has_data()) or
            (self.port is not None and self.port.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.network is not None and self.network.has_operation()) or
            (self.port is not None and self.port.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-infra-objmgr-oper:object-group" + path_buffer

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

        if (child_yang_name == "network"):
            if (self.network is None):
                self.network = ObjectGroup.Network()
                self.network.parent = self
                self._children_name_map["network"] = "network"
            return self.network

        if (child_yang_name == "port"):
            if (self.port is None):
                self.port = ObjectGroup.Port()
                self.port.parent = self
                self._children_name_map["port"] = "port"
            return self.port

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "network" or name == "port"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = ObjectGroup()
        return self._top_entity

