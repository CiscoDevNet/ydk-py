""" Cisco_IOS_XR_infra_objmgr_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-objmgr package operational data.

This module contains definitions
for the following management objects\:
  object\-group\: Object\-group operational data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class EndPort(Enum):
    """
    EndPort (Enum Class)

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
    Port (Enum Class)

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
    PortOperator (Enum Class)

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
    StartPort (Enum Class)

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
    
    .. attribute:: port
    
    	Port object group
    	**type**\:  :py:class:`Port <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Port>`
    
    .. attribute:: network
    
    	Network object group
    	**type**\:  :py:class:`Network <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Network>`
    
    

    """

    _prefix = 'infra-objmgr-oper'
    _revision = '2017-05-01'

    def __init__(self):
        super(ObjectGroup, self).__init__()
        self._top_entity = None

        self.yang_name = "object-group"
        self.yang_parent_name = "Cisco-IOS-XR-infra-objmgr-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("port", ("port", ObjectGroup.Port)), ("network", ("network", ObjectGroup.Network))])
        self._leafs = OrderedDict()

        self.port = ObjectGroup.Port()
        self.port.parent = self
        self._children_name_map["port"] = "port"

        self.network = ObjectGroup.Network()
        self.network.parent = self
        self._children_name_map["network"] = "network"
        self._segment_path = lambda: "Cisco-IOS-XR-infra-objmgr-oper:object-group"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(ObjectGroup, [], name, value)


    class Port(Entity):
        """
        Port object group
        
        .. attribute:: objects
        
        	Table of Object
        	**type**\:  :py:class:`Objects <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Port.Objects>`
        
        

        """

        _prefix = 'infra-objmgr-oper'
        _revision = '2017-05-01'

        def __init__(self):
            super(ObjectGroup.Port, self).__init__()

            self.yang_name = "port"
            self.yang_parent_name = "object-group"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("objects", ("objects", ObjectGroup.Port.Objects))])
            self._leafs = OrderedDict()

            self.objects = ObjectGroup.Port.Objects()
            self.objects.parent = self
            self._children_name_map["objects"] = "objects"
            self._segment_path = lambda: "port"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-objmgr-oper:object-group/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ObjectGroup.Port, [], name, value)


        class Objects(Entity):
            """
            Table of Object
            
            .. attribute:: object
            
            	Port object group
            	**type**\: list of  		 :py:class:`Object <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Port.Objects.Object>`
            
            

            """

            _prefix = 'infra-objmgr-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(ObjectGroup.Port.Objects, self).__init__()

                self.yang_name = "objects"
                self.yang_parent_name = "port"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("object", ("object", ObjectGroup.Port.Objects.Object))])
                self._leafs = OrderedDict()

                self.object = YList(self)
                self._segment_path = lambda: "objects"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-objmgr-oper:object-group/port/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ObjectGroup.Port.Objects, [], name, value)


            class Object(Entity):
                """
                Port object group
                
                .. attribute:: object_name  (key)
                
                	Port object group name
                	**type**\: str
                
                	**length:** 1..64
                
                .. attribute:: nested_groups
                
                	Table of NestedGroup
                	**type**\:  :py:class:`NestedGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Port.Objects.Object.NestedGroups>`
                
                .. attribute:: operators
                
                	Table of Operator
                	**type**\:  :py:class:`Operators <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Port.Objects.Object.Operators>`
                
                .. attribute:: port_ranges
                
                	Table of PortRange
                	**type**\:  :py:class:`PortRanges <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Port.Objects.Object.PortRanges>`
                
                .. attribute:: parent_groups
                
                	Table of ParentGroup
                	**type**\:  :py:class:`ParentGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Port.Objects.Object.ParentGroups>`
                
                

                """

                _prefix = 'infra-objmgr-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(ObjectGroup.Port.Objects.Object, self).__init__()

                    self.yang_name = "object"
                    self.yang_parent_name = "objects"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['object_name']
                    self._child_classes = OrderedDict([("nested-groups", ("nested_groups", ObjectGroup.Port.Objects.Object.NestedGroups)), ("operators", ("operators", ObjectGroup.Port.Objects.Object.Operators)), ("port-ranges", ("port_ranges", ObjectGroup.Port.Objects.Object.PortRanges)), ("parent-groups", ("parent_groups", ObjectGroup.Port.Objects.Object.ParentGroups))])
                    self._leafs = OrderedDict([
                        ('object_name', (YLeaf(YType.str, 'object-name'), ['str'])),
                    ])
                    self.object_name = None

                    self.nested_groups = ObjectGroup.Port.Objects.Object.NestedGroups()
                    self.nested_groups.parent = self
                    self._children_name_map["nested_groups"] = "nested-groups"

                    self.operators = ObjectGroup.Port.Objects.Object.Operators()
                    self.operators.parent = self
                    self._children_name_map["operators"] = "operators"

                    self.port_ranges = ObjectGroup.Port.Objects.Object.PortRanges()
                    self.port_ranges.parent = self
                    self._children_name_map["port_ranges"] = "port-ranges"

                    self.parent_groups = ObjectGroup.Port.Objects.Object.ParentGroups()
                    self.parent_groups.parent = self
                    self._children_name_map["parent_groups"] = "parent-groups"
                    self._segment_path = lambda: "object" + "[object-name='" + str(self.object_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-infra-objmgr-oper:object-group/port/objects/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ObjectGroup.Port.Objects.Object, ['object_name'], name, value)


                class NestedGroups(Entity):
                    """
                    Table of NestedGroup
                    
                    .. attribute:: nested_group
                    
                    	nested object group
                    	**type**\: list of  		 :py:class:`NestedGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Port.Objects.Object.NestedGroups.NestedGroup>`
                    
                    

                    """

                    _prefix = 'infra-objmgr-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(ObjectGroup.Port.Objects.Object.NestedGroups, self).__init__()

                        self.yang_name = "nested-groups"
                        self.yang_parent_name = "object"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("nested-group", ("nested_group", ObjectGroup.Port.Objects.Object.NestedGroups.NestedGroup))])
                        self._leafs = OrderedDict()

                        self.nested_group = YList(self)
                        self._segment_path = lambda: "nested-groups"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectGroup.Port.Objects.Object.NestedGroups, [], name, value)


                    class NestedGroup(Entity):
                        """
                        nested object group
                        
                        .. attribute:: nested_group_name  (key)
                        
                        	Nested object group
                        	**type**\: str
                        
                        	**length:** 1..64
                        
                        .. attribute:: nested_group_name_xr
                        
                        	Nested group
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'infra-objmgr-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(ObjectGroup.Port.Objects.Object.NestedGroups.NestedGroup, self).__init__()

                            self.yang_name = "nested-group"
                            self.yang_parent_name = "nested-groups"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['nested_group_name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('nested_group_name', (YLeaf(YType.str, 'nested-group-name'), ['str'])),
                                ('nested_group_name_xr', (YLeaf(YType.str, 'nested-group-name-xr'), ['str'])),
                            ])
                            self.nested_group_name = None
                            self.nested_group_name_xr = None
                            self._segment_path = lambda: "nested-group" + "[nested-group-name='" + str(self.nested_group_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(ObjectGroup.Port.Objects.Object.NestedGroups.NestedGroup, ['nested_group_name', 'nested_group_name_xr'], name, value)


                class Operators(Entity):
                    """
                    Table of Operator
                    
                    .. attribute:: operator
                    
                    	op class
                    	**type**\: list of  		 :py:class:`Operator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Port.Objects.Object.Operators.Operator>`
                    
                    

                    """

                    _prefix = 'infra-objmgr-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(ObjectGroup.Port.Objects.Object.Operators, self).__init__()

                        self.yang_name = "operators"
                        self.yang_parent_name = "object"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("operator", ("operator", ObjectGroup.Port.Objects.Object.Operators.Operator))])
                        self._leafs = OrderedDict()

                        self.operator = YList(self)
                        self._segment_path = lambda: "operators"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectGroup.Port.Objects.Object.Operators, [], name, value)


                    class Operator(Entity):
                        """
                        op class
                        
                        .. attribute:: operator_type
                        
                        	operation for ports
                        	**type**\:  :py:class:`PortOperator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.PortOperator>`
                        
                        .. attribute:: port
                        
                        	Port number
                        	**type**\: union of the below types:
                        
                        		**type**\:  :py:class:`Port <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.Port>`
                        
                        		**type**\: int
                        
                        			**range:** 0..65535
                        
                        .. attribute:: operator_type_xr
                        
                        	Operator
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: port_xr
                        
                        	Port
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'infra-objmgr-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(ObjectGroup.Port.Objects.Object.Operators.Operator, self).__init__()

                            self.yang_name = "operator"
                            self.yang_parent_name = "operators"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('operator_type', (YLeaf(YType.enumeration, 'operator-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper', 'PortOperator', '')])),
                                ('port', (YLeaf(YType.str, 'port'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper', 'Port', ''),'int'])),
                                ('operator_type_xr', (YLeaf(YType.uint32, 'operator-type-xr'), ['int'])),
                                ('port_xr', (YLeaf(YType.uint32, 'port-xr'), ['int'])),
                            ])
                            self.operator_type = None
                            self.port = None
                            self.operator_type_xr = None
                            self.port_xr = None
                            self._segment_path = lambda: "operator"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(ObjectGroup.Port.Objects.Object.Operators.Operator, ['operator_type', 'port', 'operator_type_xr', 'port_xr'], name, value)


                class PortRanges(Entity):
                    """
                    Table of PortRange
                    
                    .. attribute:: port_range
                    
                    	Match only packets on a given port range
                    	**type**\: list of  		 :py:class:`PortRange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Port.Objects.Object.PortRanges.PortRange>`
                    
                    

                    """

                    _prefix = 'infra-objmgr-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(ObjectGroup.Port.Objects.Object.PortRanges, self).__init__()

                        self.yang_name = "port-ranges"
                        self.yang_parent_name = "object"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("port-range", ("port_range", ObjectGroup.Port.Objects.Object.PortRanges.PortRange))])
                        self._leafs = OrderedDict()

                        self.port_range = YList(self)
                        self._segment_path = lambda: "port-ranges"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectGroup.Port.Objects.Object.PortRanges, [], name, value)


                    class PortRange(Entity):
                        """
                        Match only packets on a given port range
                        
                        .. attribute:: start_port
                        
                        	Start port number
                        	**type**\: union of the below types:
                        
                        		**type**\:  :py:class:`StartPort <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.StartPort>`
                        
                        		**type**\: int
                        
                        			**range:** 0..65535
                        
                        .. attribute:: end_port
                        
                        	End port number
                        	**type**\: union of the below types:
                        
                        		**type**\:  :py:class:`EndPort <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.EndPort>`
                        
                        		**type**\: int
                        
                        			**range:** 0..65535
                        
                        .. attribute:: start_port_xr
                        
                        	Port start address
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_port_xr
                        
                        	Port end address
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'infra-objmgr-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(ObjectGroup.Port.Objects.Object.PortRanges.PortRange, self).__init__()

                            self.yang_name = "port-range"
                            self.yang_parent_name = "port-ranges"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('start_port', (YLeaf(YType.str, 'start-port'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper', 'StartPort', ''),'int'])),
                                ('end_port', (YLeaf(YType.str, 'end-port'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper', 'EndPort', ''),'int'])),
                                ('start_port_xr', (YLeaf(YType.uint32, 'start-port-xr'), ['int'])),
                                ('end_port_xr', (YLeaf(YType.uint32, 'end-port-xr'), ['int'])),
                            ])
                            self.start_port = None
                            self.end_port = None
                            self.start_port_xr = None
                            self.end_port_xr = None
                            self._segment_path = lambda: "port-range"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(ObjectGroup.Port.Objects.Object.PortRanges.PortRange, ['start_port', 'end_port', 'start_port_xr', 'end_port_xr'], name, value)


                class ParentGroups(Entity):
                    """
                    Table of ParentGroup
                    
                    .. attribute:: parent_group
                    
                    	Parent object group
                    	**type**\: list of  		 :py:class:`ParentGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Port.Objects.Object.ParentGroups.ParentGroup>`
                    
                    

                    """

                    _prefix = 'infra-objmgr-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(ObjectGroup.Port.Objects.Object.ParentGroups, self).__init__()

                        self.yang_name = "parent-groups"
                        self.yang_parent_name = "object"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("parent-group", ("parent_group", ObjectGroup.Port.Objects.Object.ParentGroups.ParentGroup))])
                        self._leafs = OrderedDict()

                        self.parent_group = YList(self)
                        self._segment_path = lambda: "parent-groups"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectGroup.Port.Objects.Object.ParentGroups, [], name, value)


                    class ParentGroup(Entity):
                        """
                        Parent object group
                        
                        .. attribute:: parent_group_name  (key)
                        
                        	Nested object group
                        	**type**\: str
                        
                        	**length:** 1..64
                        
                        .. attribute:: parent_name
                        
                        	Parent node
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'infra-objmgr-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(ObjectGroup.Port.Objects.Object.ParentGroups.ParentGroup, self).__init__()

                            self.yang_name = "parent-group"
                            self.yang_parent_name = "parent-groups"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['parent_group_name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('parent_group_name', (YLeaf(YType.str, 'parent-group-name'), ['str'])),
                                ('parent_name', (YLeaf(YType.str, 'parent-name'), ['str'])),
                            ])
                            self.parent_group_name = None
                            self.parent_name = None
                            self._segment_path = lambda: "parent-group" + "[parent-group-name='" + str(self.parent_group_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(ObjectGroup.Port.Objects.Object.ParentGroups.ParentGroup, ['parent_group_name', 'parent_name'], name, value)


    class Network(Entity):
        """
        Network object group
        
        .. attribute:: ipv6
        
        	IPv6 object group
        	**type**\:  :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Network.Ipv6>`
        
        .. attribute:: ipv4
        
        	IPv4 object group
        	**type**\:  :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Network.Ipv4>`
        
        

        """

        _prefix = 'infra-objmgr-oper'
        _revision = '2017-05-01'

        def __init__(self):
            super(ObjectGroup.Network, self).__init__()

            self.yang_name = "network"
            self.yang_parent_name = "object-group"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ipv6", ("ipv6", ObjectGroup.Network.Ipv6)), ("ipv4", ("ipv4", ObjectGroup.Network.Ipv4))])
            self._leafs = OrderedDict()

            self.ipv6 = ObjectGroup.Network.Ipv6()
            self.ipv6.parent = self
            self._children_name_map["ipv6"] = "ipv6"

            self.ipv4 = ObjectGroup.Network.Ipv4()
            self.ipv4.parent = self
            self._children_name_map["ipv4"] = "ipv4"
            self._segment_path = lambda: "network"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-objmgr-oper:object-group/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ObjectGroup.Network, [], name, value)


        class Ipv6(Entity):
            """
            IPv6 object group
            
            .. attribute:: objects
            
            	Table of Object
            	**type**\:  :py:class:`Objects <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Network.Ipv6.Objects>`
            
            

            """

            _prefix = 'infra-objmgr-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(ObjectGroup.Network.Ipv6, self).__init__()

                self.yang_name = "ipv6"
                self.yang_parent_name = "network"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("objects", ("objects", ObjectGroup.Network.Ipv6.Objects))])
                self._leafs = OrderedDict()

                self.objects = ObjectGroup.Network.Ipv6.Objects()
                self.objects.parent = self
                self._children_name_map["objects"] = "objects"
                self._segment_path = lambda: "ipv6"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-objmgr-oper:object-group/network/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ObjectGroup.Network.Ipv6, [], name, value)


            class Objects(Entity):
                """
                Table of Object
                
                .. attribute:: object
                
                	IPv6 object group
                	**type**\: list of  		 :py:class:`Object <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Network.Ipv6.Objects.Object>`
                
                

                """

                _prefix = 'infra-objmgr-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(ObjectGroup.Network.Ipv6.Objects, self).__init__()

                    self.yang_name = "objects"
                    self.yang_parent_name = "ipv6"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("object", ("object", ObjectGroup.Network.Ipv6.Objects.Object))])
                    self._leafs = OrderedDict()

                    self.object = YList(self)
                    self._segment_path = lambda: "objects"
                    self._absolute_path = lambda: "Cisco-IOS-XR-infra-objmgr-oper:object-group/network/ipv6/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ObjectGroup.Network.Ipv6.Objects, [], name, value)


                class Object(Entity):
                    """
                    IPv6 object group
                    
                    .. attribute:: object_name  (key)
                    
                    	IPv6 object group name \- maximum 64 characters
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    .. attribute:: nested_groups
                    
                    	Table of NestedGroup
                    	**type**\:  :py:class:`NestedGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Network.Ipv6.Objects.Object.NestedGroups>`
                    
                    .. attribute:: addresses
                    
                    	Table of Address
                    	**type**\:  :py:class:`Addresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Network.Ipv6.Objects.Object.Addresses>`
                    
                    .. attribute:: address_ranges
                    
                    	Table of AddressRange
                    	**type**\:  :py:class:`AddressRanges <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Network.Ipv6.Objects.Object.AddressRanges>`
                    
                    .. attribute:: parent_groups
                    
                    	Table of parent object group
                    	**type**\:  :py:class:`ParentGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Network.Ipv6.Objects.Object.ParentGroups>`
                    
                    .. attribute:: hosts
                    
                    	Table of Host
                    	**type**\:  :py:class:`Hosts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Network.Ipv6.Objects.Object.Hosts>`
                    
                    

                    """

                    _prefix = 'infra-objmgr-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(ObjectGroup.Network.Ipv6.Objects.Object, self).__init__()

                        self.yang_name = "object"
                        self.yang_parent_name = "objects"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['object_name']
                        self._child_classes = OrderedDict([("nested-groups", ("nested_groups", ObjectGroup.Network.Ipv6.Objects.Object.NestedGroups)), ("addresses", ("addresses", ObjectGroup.Network.Ipv6.Objects.Object.Addresses)), ("address-ranges", ("address_ranges", ObjectGroup.Network.Ipv6.Objects.Object.AddressRanges)), ("parent-groups", ("parent_groups", ObjectGroup.Network.Ipv6.Objects.Object.ParentGroups)), ("hosts", ("hosts", ObjectGroup.Network.Ipv6.Objects.Object.Hosts))])
                        self._leafs = OrderedDict([
                            ('object_name', (YLeaf(YType.str, 'object-name'), ['str'])),
                        ])
                        self.object_name = None

                        self.nested_groups = ObjectGroup.Network.Ipv6.Objects.Object.NestedGroups()
                        self.nested_groups.parent = self
                        self._children_name_map["nested_groups"] = "nested-groups"

                        self.addresses = ObjectGroup.Network.Ipv6.Objects.Object.Addresses()
                        self.addresses.parent = self
                        self._children_name_map["addresses"] = "addresses"

                        self.address_ranges = ObjectGroup.Network.Ipv6.Objects.Object.AddressRanges()
                        self.address_ranges.parent = self
                        self._children_name_map["address_ranges"] = "address-ranges"

                        self.parent_groups = ObjectGroup.Network.Ipv6.Objects.Object.ParentGroups()
                        self.parent_groups.parent = self
                        self._children_name_map["parent_groups"] = "parent-groups"

                        self.hosts = ObjectGroup.Network.Ipv6.Objects.Object.Hosts()
                        self.hosts.parent = self
                        self._children_name_map["hosts"] = "hosts"
                        self._segment_path = lambda: "object" + "[object-name='" + str(self.object_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-infra-objmgr-oper:object-group/network/ipv6/objects/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectGroup.Network.Ipv6.Objects.Object, ['object_name'], name, value)


                    class NestedGroups(Entity):
                        """
                        Table of NestedGroup
                        
                        .. attribute:: nested_group
                        
                        	nested object group
                        	**type**\: list of  		 :py:class:`NestedGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Network.Ipv6.Objects.Object.NestedGroups.NestedGroup>`
                        
                        

                        """

                        _prefix = 'infra-objmgr-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(ObjectGroup.Network.Ipv6.Objects.Object.NestedGroups, self).__init__()

                            self.yang_name = "nested-groups"
                            self.yang_parent_name = "object"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("nested-group", ("nested_group", ObjectGroup.Network.Ipv6.Objects.Object.NestedGroups.NestedGroup))])
                            self._leafs = OrderedDict()

                            self.nested_group = YList(self)
                            self._segment_path = lambda: "nested-groups"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(ObjectGroup.Network.Ipv6.Objects.Object.NestedGroups, [], name, value)


                        class NestedGroup(Entity):
                            """
                            nested object group
                            
                            .. attribute:: nested_group_name  (key)
                            
                            	Enter the name of a nested object group
                            	**type**\: str
                            
                            	**length:** 1..64
                            
                            .. attribute:: nested_group_name_xr
                            
                            	Nested group
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'infra-objmgr-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(ObjectGroup.Network.Ipv6.Objects.Object.NestedGroups.NestedGroup, self).__init__()

                                self.yang_name = "nested-group"
                                self.yang_parent_name = "nested-groups"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['nested_group_name']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('nested_group_name', (YLeaf(YType.str, 'nested-group-name'), ['str'])),
                                    ('nested_group_name_xr', (YLeaf(YType.str, 'nested-group-name-xr'), ['str'])),
                                ])
                                self.nested_group_name = None
                                self.nested_group_name_xr = None
                                self._segment_path = lambda: "nested-group" + "[nested-group-name='" + str(self.nested_group_name) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(ObjectGroup.Network.Ipv6.Objects.Object.NestedGroups.NestedGroup, ['nested_group_name', 'nested_group_name_xr'], name, value)


                    class Addresses(Entity):
                        """
                        Table of Address
                        
                        .. attribute:: address
                        
                        	IPv6 address
                        	**type**\: list of  		 :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Network.Ipv6.Objects.Object.Addresses.Address>`
                        
                        

                        """

                        _prefix = 'infra-objmgr-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(ObjectGroup.Network.Ipv6.Objects.Object.Addresses, self).__init__()

                            self.yang_name = "addresses"
                            self.yang_parent_name = "object"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("address", ("address", ObjectGroup.Network.Ipv6.Objects.Object.Addresses.Address))])
                            self._leafs = OrderedDict()

                            self.address = YList(self)
                            self._segment_path = lambda: "addresses"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(ObjectGroup.Network.Ipv6.Objects.Object.Addresses, [], name, value)


                        class Address(Entity):
                            """
                            IPv6 address
                            
                            .. attribute:: prefix
                            
                            	IPv6 prefix x\:x\:\:x/y
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: prefix_length
                            
                            	Prefix of the IP Address
                            	**type**\: int
                            
                            	**range:** 0..128
                            
                            .. attribute:: prefix_xr
                            
                            	IPv4 Address
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: prefix_length_xr
                            
                            	Prefix length
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'infra-objmgr-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(ObjectGroup.Network.Ipv6.Objects.Object.Addresses.Address, self).__init__()

                                self.yang_name = "address"
                                self.yang_parent_name = "addresses"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('prefix', (YLeaf(YType.str, 'prefix'), ['str'])),
                                    ('prefix_length', (YLeaf(YType.uint8, 'prefix-length'), ['int'])),
                                    ('prefix_xr', (YLeaf(YType.str, 'prefix-xr'), ['str'])),
                                    ('prefix_length_xr', (YLeaf(YType.uint32, 'prefix-length-xr'), ['int'])),
                                ])
                                self.prefix = None
                                self.prefix_length = None
                                self.prefix_xr = None
                                self.prefix_length_xr = None
                                self._segment_path = lambda: "address"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(ObjectGroup.Network.Ipv6.Objects.Object.Addresses.Address, ['prefix', 'prefix_length', 'prefix_xr', 'prefix_length_xr'], name, value)


                    class AddressRanges(Entity):
                        """
                        Table of AddressRange
                        
                        .. attribute:: address_range
                        
                        	Range of host addresses
                        	**type**\: list of  		 :py:class:`AddressRange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Network.Ipv6.Objects.Object.AddressRanges.AddressRange>`
                        
                        

                        """

                        _prefix = 'infra-objmgr-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(ObjectGroup.Network.Ipv6.Objects.Object.AddressRanges, self).__init__()

                            self.yang_name = "address-ranges"
                            self.yang_parent_name = "object"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("address-range", ("address_range", ObjectGroup.Network.Ipv6.Objects.Object.AddressRanges.AddressRange))])
                            self._leafs = OrderedDict()

                            self.address_range = YList(self)
                            self._segment_path = lambda: "address-ranges"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(ObjectGroup.Network.Ipv6.Objects.Object.AddressRanges, [], name, value)


                        class AddressRange(Entity):
                            """
                            Range of host addresses
                            
                            .. attribute:: start_address
                            
                            	IPv6 address
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: end_address
                            
                            	IPv6 address
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: start_address_xr
                            
                            	Range start address
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: end_address_xr
                            
                            	Range end address
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-objmgr-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(ObjectGroup.Network.Ipv6.Objects.Object.AddressRanges.AddressRange, self).__init__()

                                self.yang_name = "address-range"
                                self.yang_parent_name = "address-ranges"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('start_address', (YLeaf(YType.str, 'start-address'), ['str'])),
                                    ('end_address', (YLeaf(YType.str, 'end-address'), ['str'])),
                                    ('start_address_xr', (YLeaf(YType.str, 'start-address-xr'), ['str'])),
                                    ('end_address_xr', (YLeaf(YType.str, 'end-address-xr'), ['str'])),
                                ])
                                self.start_address = None
                                self.end_address = None
                                self.start_address_xr = None
                                self.end_address_xr = None
                                self._segment_path = lambda: "address-range"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(ObjectGroup.Network.Ipv6.Objects.Object.AddressRanges.AddressRange, ['start_address', 'end_address', 'start_address_xr', 'end_address_xr'], name, value)


                    class ParentGroups(Entity):
                        """
                        Table of parent object group
                        
                        .. attribute:: parent_group
                        
                        	Parent object group
                        	**type**\: list of  		 :py:class:`ParentGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Network.Ipv6.Objects.Object.ParentGroups.ParentGroup>`
                        
                        

                        """

                        _prefix = 'infra-objmgr-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(ObjectGroup.Network.Ipv6.Objects.Object.ParentGroups, self).__init__()

                            self.yang_name = "parent-groups"
                            self.yang_parent_name = "object"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("parent-group", ("parent_group", ObjectGroup.Network.Ipv6.Objects.Object.ParentGroups.ParentGroup))])
                            self._leafs = OrderedDict()

                            self.parent_group = YList(self)
                            self._segment_path = lambda: "parent-groups"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(ObjectGroup.Network.Ipv6.Objects.Object.ParentGroups, [], name, value)


                        class ParentGroup(Entity):
                            """
                            Parent object group
                            
                            .. attribute:: parent_group_name  (key)
                            
                            	Nested object group
                            	**type**\: str
                            
                            	**length:** 1..64
                            
                            .. attribute:: parent_name
                            
                            	Parent node
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'infra-objmgr-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(ObjectGroup.Network.Ipv6.Objects.Object.ParentGroups.ParentGroup, self).__init__()

                                self.yang_name = "parent-group"
                                self.yang_parent_name = "parent-groups"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['parent_group_name']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('parent_group_name', (YLeaf(YType.str, 'parent-group-name'), ['str'])),
                                    ('parent_name', (YLeaf(YType.str, 'parent-name'), ['str'])),
                                ])
                                self.parent_group_name = None
                                self.parent_name = None
                                self._segment_path = lambda: "parent-group" + "[parent-group-name='" + str(self.parent_group_name) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(ObjectGroup.Network.Ipv6.Objects.Object.ParentGroups.ParentGroup, ['parent_group_name', 'parent_name'], name, value)


                    class Hosts(Entity):
                        """
                        Table of Host
                        
                        .. attribute:: host
                        
                        	A single host address
                        	**type**\: list of  		 :py:class:`Host <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Network.Ipv6.Objects.Object.Hosts.Host>`
                        
                        

                        """

                        _prefix = 'infra-objmgr-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(ObjectGroup.Network.Ipv6.Objects.Object.Hosts, self).__init__()

                            self.yang_name = "hosts"
                            self.yang_parent_name = "object"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("host", ("host", ObjectGroup.Network.Ipv6.Objects.Object.Hosts.Host))])
                            self._leafs = OrderedDict()

                            self.host = YList(self)
                            self._segment_path = lambda: "hosts"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(ObjectGroup.Network.Ipv6.Objects.Object.Hosts, [], name, value)


                        class Host(Entity):
                            """
                            A single host address
                            
                            .. attribute:: host_address  (key)
                            
                            	host ipv6 address
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: host_address_xr
                            
                            	Host address
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-objmgr-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(ObjectGroup.Network.Ipv6.Objects.Object.Hosts.Host, self).__init__()

                                self.yang_name = "host"
                                self.yang_parent_name = "hosts"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['host_address']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('host_address', (YLeaf(YType.str, 'host-address'), ['str'])),
                                    ('host_address_xr', (YLeaf(YType.str, 'host-address-xr'), ['str'])),
                                ])
                                self.host_address = None
                                self.host_address_xr = None
                                self._segment_path = lambda: "host" + "[host-address='" + str(self.host_address) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(ObjectGroup.Network.Ipv6.Objects.Object.Hosts.Host, ['host_address', 'host_address_xr'], name, value)


        class Ipv4(Entity):
            """
            IPv4 object group
            
            .. attribute:: objects
            
            	Table of Object
            	**type**\:  :py:class:`Objects <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Network.Ipv4.Objects>`
            
            

            """

            _prefix = 'infra-objmgr-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(ObjectGroup.Network.Ipv4, self).__init__()

                self.yang_name = "ipv4"
                self.yang_parent_name = "network"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("objects", ("objects", ObjectGroup.Network.Ipv4.Objects))])
                self._leafs = OrderedDict()

                self.objects = ObjectGroup.Network.Ipv4.Objects()
                self.objects.parent = self
                self._children_name_map["objects"] = "objects"
                self._segment_path = lambda: "ipv4"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-objmgr-oper:object-group/network/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ObjectGroup.Network.Ipv4, [], name, value)


            class Objects(Entity):
                """
                Table of Object
                
                .. attribute:: object
                
                	IPv4 object group
                	**type**\: list of  		 :py:class:`Object <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Network.Ipv4.Objects.Object>`
                
                

                """

                _prefix = 'infra-objmgr-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(ObjectGroup.Network.Ipv4.Objects, self).__init__()

                    self.yang_name = "objects"
                    self.yang_parent_name = "ipv4"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("object", ("object", ObjectGroup.Network.Ipv4.Objects.Object))])
                    self._leafs = OrderedDict()

                    self.object = YList(self)
                    self._segment_path = lambda: "objects"
                    self._absolute_path = lambda: "Cisco-IOS-XR-infra-objmgr-oper:object-group/network/ipv4/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ObjectGroup.Network.Ipv4.Objects, [], name, value)


                class Object(Entity):
                    """
                    IPv4 object group
                    
                    .. attribute:: object_name  (key)
                    
                    	IPv4 object group name \- maximum 64 characters
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    .. attribute:: nested_groups
                    
                    	Table of NestedGroup
                    	**type**\:  :py:class:`NestedGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Network.Ipv4.Objects.Object.NestedGroups>`
                    
                    .. attribute:: addresses
                    
                    	Table of Address
                    	**type**\:  :py:class:`Addresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Network.Ipv4.Objects.Object.Addresses>`
                    
                    .. attribute:: address_ranges
                    
                    	Table of AddressRange
                    	**type**\:  :py:class:`AddressRanges <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Network.Ipv4.Objects.Object.AddressRanges>`
                    
                    .. attribute:: parent_groups
                    
                    	Table of parent object group
                    	**type**\:  :py:class:`ParentGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Network.Ipv4.Objects.Object.ParentGroups>`
                    
                    .. attribute:: hosts
                    
                    	Table of Host
                    	**type**\:  :py:class:`Hosts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Network.Ipv4.Objects.Object.Hosts>`
                    
                    

                    """

                    _prefix = 'infra-objmgr-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(ObjectGroup.Network.Ipv4.Objects.Object, self).__init__()

                        self.yang_name = "object"
                        self.yang_parent_name = "objects"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['object_name']
                        self._child_classes = OrderedDict([("nested-groups", ("nested_groups", ObjectGroup.Network.Ipv4.Objects.Object.NestedGroups)), ("addresses", ("addresses", ObjectGroup.Network.Ipv4.Objects.Object.Addresses)), ("address-ranges", ("address_ranges", ObjectGroup.Network.Ipv4.Objects.Object.AddressRanges)), ("parent-groups", ("parent_groups", ObjectGroup.Network.Ipv4.Objects.Object.ParentGroups)), ("hosts", ("hosts", ObjectGroup.Network.Ipv4.Objects.Object.Hosts))])
                        self._leafs = OrderedDict([
                            ('object_name', (YLeaf(YType.str, 'object-name'), ['str'])),
                        ])
                        self.object_name = None

                        self.nested_groups = ObjectGroup.Network.Ipv4.Objects.Object.NestedGroups()
                        self.nested_groups.parent = self
                        self._children_name_map["nested_groups"] = "nested-groups"

                        self.addresses = ObjectGroup.Network.Ipv4.Objects.Object.Addresses()
                        self.addresses.parent = self
                        self._children_name_map["addresses"] = "addresses"

                        self.address_ranges = ObjectGroup.Network.Ipv4.Objects.Object.AddressRanges()
                        self.address_ranges.parent = self
                        self._children_name_map["address_ranges"] = "address-ranges"

                        self.parent_groups = ObjectGroup.Network.Ipv4.Objects.Object.ParentGroups()
                        self.parent_groups.parent = self
                        self._children_name_map["parent_groups"] = "parent-groups"

                        self.hosts = ObjectGroup.Network.Ipv4.Objects.Object.Hosts()
                        self.hosts.parent = self
                        self._children_name_map["hosts"] = "hosts"
                        self._segment_path = lambda: "object" + "[object-name='" + str(self.object_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-infra-objmgr-oper:object-group/network/ipv4/objects/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectGroup.Network.Ipv4.Objects.Object, ['object_name'], name, value)


                    class NestedGroups(Entity):
                        """
                        Table of NestedGroup
                        
                        .. attribute:: nested_group
                        
                        	Nested object group
                        	**type**\: list of  		 :py:class:`NestedGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Network.Ipv4.Objects.Object.NestedGroups.NestedGroup>`
                        
                        

                        """

                        _prefix = 'infra-objmgr-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(ObjectGroup.Network.Ipv4.Objects.Object.NestedGroups, self).__init__()

                            self.yang_name = "nested-groups"
                            self.yang_parent_name = "object"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("nested-group", ("nested_group", ObjectGroup.Network.Ipv4.Objects.Object.NestedGroups.NestedGroup))])
                            self._leafs = OrderedDict()

                            self.nested_group = YList(self)
                            self._segment_path = lambda: "nested-groups"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(ObjectGroup.Network.Ipv4.Objects.Object.NestedGroups, [], name, value)


                        class NestedGroup(Entity):
                            """
                            Nested object group
                            
                            .. attribute:: nested_group_name  (key)
                            
                            	Nested object group
                            	**type**\: str
                            
                            	**length:** 1..64
                            
                            .. attribute:: nested_group_name_xr
                            
                            	Nested group
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'infra-objmgr-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(ObjectGroup.Network.Ipv4.Objects.Object.NestedGroups.NestedGroup, self).__init__()

                                self.yang_name = "nested-group"
                                self.yang_parent_name = "nested-groups"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['nested_group_name']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('nested_group_name', (YLeaf(YType.str, 'nested-group-name'), ['str'])),
                                    ('nested_group_name_xr', (YLeaf(YType.str, 'nested-group-name-xr'), ['str'])),
                                ])
                                self.nested_group_name = None
                                self.nested_group_name_xr = None
                                self._segment_path = lambda: "nested-group" + "[nested-group-name='" + str(self.nested_group_name) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(ObjectGroup.Network.Ipv4.Objects.Object.NestedGroups.NestedGroup, ['nested_group_name', 'nested_group_name_xr'], name, value)


                    class Addresses(Entity):
                        """
                        Table of Address
                        
                        .. attribute:: address
                        
                        	IPv4 address
                        	**type**\: list of  		 :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Network.Ipv4.Objects.Object.Addresses.Address>`
                        
                        

                        """

                        _prefix = 'infra-objmgr-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(ObjectGroup.Network.Ipv4.Objects.Object.Addresses, self).__init__()

                            self.yang_name = "addresses"
                            self.yang_parent_name = "object"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("address", ("address", ObjectGroup.Network.Ipv4.Objects.Object.Addresses.Address))])
                            self._leafs = OrderedDict()

                            self.address = YList(self)
                            self._segment_path = lambda: "addresses"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(ObjectGroup.Network.Ipv4.Objects.Object.Addresses, [], name, value)


                        class Address(Entity):
                            """
                            IPv4 address
                            
                            .. attribute:: prefix
                            
                            	IPv4 address/prefix
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: prefix_length
                            
                            	Prefix of the IP Address
                            	**type**\: int
                            
                            	**range:** 0..32
                            
                            .. attribute:: prefix_xr
                            
                            	IPv4 Address
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: prefix_length_xr
                            
                            	Prefix length
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'infra-objmgr-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(ObjectGroup.Network.Ipv4.Objects.Object.Addresses.Address, self).__init__()

                                self.yang_name = "address"
                                self.yang_parent_name = "addresses"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('prefix', (YLeaf(YType.str, 'prefix'), ['str'])),
                                    ('prefix_length', (YLeaf(YType.uint8, 'prefix-length'), ['int'])),
                                    ('prefix_xr', (YLeaf(YType.str, 'prefix-xr'), ['str'])),
                                    ('prefix_length_xr', (YLeaf(YType.uint32, 'prefix-length-xr'), ['int'])),
                                ])
                                self.prefix = None
                                self.prefix_length = None
                                self.prefix_xr = None
                                self.prefix_length_xr = None
                                self._segment_path = lambda: "address"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(ObjectGroup.Network.Ipv4.Objects.Object.Addresses.Address, ['prefix', 'prefix_length', 'prefix_xr', 'prefix_length_xr'], name, value)


                    class AddressRanges(Entity):
                        """
                        Table of AddressRange
                        
                        .. attribute:: address_range
                        
                        	Range of host addresses
                        	**type**\: list of  		 :py:class:`AddressRange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Network.Ipv4.Objects.Object.AddressRanges.AddressRange>`
                        
                        

                        """

                        _prefix = 'infra-objmgr-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(ObjectGroup.Network.Ipv4.Objects.Object.AddressRanges, self).__init__()

                            self.yang_name = "address-ranges"
                            self.yang_parent_name = "object"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("address-range", ("address_range", ObjectGroup.Network.Ipv4.Objects.Object.AddressRanges.AddressRange))])
                            self._leafs = OrderedDict()

                            self.address_range = YList(self)
                            self._segment_path = lambda: "address-ranges"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(ObjectGroup.Network.Ipv4.Objects.Object.AddressRanges, [], name, value)


                        class AddressRange(Entity):
                            """
                            Range of host addresses
                            
                            .. attribute:: start_address
                            
                            	IPv4 address
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: end_address
                            
                            	IPv4 address
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: start_address_xr
                            
                            	Range start address
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: end_address_xr
                            
                            	Range end address
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-objmgr-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(ObjectGroup.Network.Ipv4.Objects.Object.AddressRanges.AddressRange, self).__init__()

                                self.yang_name = "address-range"
                                self.yang_parent_name = "address-ranges"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('start_address', (YLeaf(YType.str, 'start-address'), ['str'])),
                                    ('end_address', (YLeaf(YType.str, 'end-address'), ['str'])),
                                    ('start_address_xr', (YLeaf(YType.str, 'start-address-xr'), ['str'])),
                                    ('end_address_xr', (YLeaf(YType.str, 'end-address-xr'), ['str'])),
                                ])
                                self.start_address = None
                                self.end_address = None
                                self.start_address_xr = None
                                self.end_address_xr = None
                                self._segment_path = lambda: "address-range"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(ObjectGroup.Network.Ipv4.Objects.Object.AddressRanges.AddressRange, ['start_address', 'end_address', 'start_address_xr', 'end_address_xr'], name, value)


                    class ParentGroups(Entity):
                        """
                        Table of parent object group
                        
                        .. attribute:: parent_group
                        
                        	Parent object group
                        	**type**\: list of  		 :py:class:`ParentGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Network.Ipv4.Objects.Object.ParentGroups.ParentGroup>`
                        
                        

                        """

                        _prefix = 'infra-objmgr-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(ObjectGroup.Network.Ipv4.Objects.Object.ParentGroups, self).__init__()

                            self.yang_name = "parent-groups"
                            self.yang_parent_name = "object"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("parent-group", ("parent_group", ObjectGroup.Network.Ipv4.Objects.Object.ParentGroups.ParentGroup))])
                            self._leafs = OrderedDict()

                            self.parent_group = YList(self)
                            self._segment_path = lambda: "parent-groups"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(ObjectGroup.Network.Ipv4.Objects.Object.ParentGroups, [], name, value)


                        class ParentGroup(Entity):
                            """
                            Parent object group
                            
                            .. attribute:: parent_group_name  (key)
                            
                            	Nested object group
                            	**type**\: str
                            
                            	**length:** 1..64
                            
                            .. attribute:: parent_name
                            
                            	Parent node
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'infra-objmgr-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(ObjectGroup.Network.Ipv4.Objects.Object.ParentGroups.ParentGroup, self).__init__()

                                self.yang_name = "parent-group"
                                self.yang_parent_name = "parent-groups"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['parent_group_name']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('parent_group_name', (YLeaf(YType.str, 'parent-group-name'), ['str'])),
                                    ('parent_name', (YLeaf(YType.str, 'parent-name'), ['str'])),
                                ])
                                self.parent_group_name = None
                                self.parent_name = None
                                self._segment_path = lambda: "parent-group" + "[parent-group-name='" + str(self.parent_group_name) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(ObjectGroup.Network.Ipv4.Objects.Object.ParentGroups.ParentGroup, ['parent_group_name', 'parent_name'], name, value)


                    class Hosts(Entity):
                        """
                        Table of Host
                        
                        .. attribute:: host
                        
                        	A single host address
                        	**type**\: list of  		 :py:class:`Host <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Network.Ipv4.Objects.Object.Hosts.Host>`
                        
                        

                        """

                        _prefix = 'infra-objmgr-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(ObjectGroup.Network.Ipv4.Objects.Object.Hosts, self).__init__()

                            self.yang_name = "hosts"
                            self.yang_parent_name = "object"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("host", ("host", ObjectGroup.Network.Ipv4.Objects.Object.Hosts.Host))])
                            self._leafs = OrderedDict()

                            self.host = YList(self)
                            self._segment_path = lambda: "hosts"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(ObjectGroup.Network.Ipv4.Objects.Object.Hosts, [], name, value)


                        class Host(Entity):
                            """
                            A single host address
                            
                            .. attribute:: host_address  (key)
                            
                            	Host ipv4 address
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: host_address_xr
                            
                            	Host address
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-objmgr-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(ObjectGroup.Network.Ipv4.Objects.Object.Hosts.Host, self).__init__()

                                self.yang_name = "host"
                                self.yang_parent_name = "hosts"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['host_address']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('host_address', (YLeaf(YType.str, 'host-address'), ['str'])),
                                    ('host_address_xr', (YLeaf(YType.str, 'host-address-xr'), ['str'])),
                                ])
                                self.host_address = None
                                self.host_address_xr = None
                                self._segment_path = lambda: "host" + "[host-address='" + str(self.host_address) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(ObjectGroup.Network.Ipv4.Objects.Object.Hosts.Host, ['host_address', 'host_address_xr'], name, value)

    def clone_ptr(self):
        self._top_entity = ObjectGroup()
        return self._top_entity

