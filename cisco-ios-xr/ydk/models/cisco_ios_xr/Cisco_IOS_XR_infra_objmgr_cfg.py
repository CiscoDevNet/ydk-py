""" Cisco_IOS_XR_infra_objmgr_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-objmgr package configuration.

This module contains definitions
for the following management objects\:
  object\-group\: Object\-group configuration

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
    Object\-group configuration
    
    .. attribute:: port
    
    	Port object group
    	**type**\:  :py:class:`Port <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg.ObjectGroup.Port>`
    
    .. attribute:: network
    
    	Network object group
    	**type**\:  :py:class:`Network <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg.ObjectGroup.Network>`
    
    

    """

    _prefix = 'infra-objmgr-cfg'
    _revision = '2017-05-01'

    def __init__(self):
        super(ObjectGroup, self).__init__()
        self._top_entity = None

        self.yang_name = "object-group"
        self.yang_parent_name = "Cisco-IOS-XR-infra-objmgr-cfg"
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
        self._segment_path = lambda: "Cisco-IOS-XR-infra-objmgr-cfg:object-group"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(ObjectGroup, [], name, value)


    class Port(Entity):
        """
        Port object group
        
        .. attribute:: udf_objects
        
        	Table of port objects groups
        	**type**\:  :py:class:`UdfObjects <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg.ObjectGroup.Port.UdfObjects>`
        
        

        """

        _prefix = 'infra-objmgr-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(ObjectGroup.Port, self).__init__()

            self.yang_name = "port"
            self.yang_parent_name = "object-group"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("udf-objects", ("udf_objects", ObjectGroup.Port.UdfObjects))])
            self._leafs = OrderedDict()

            self.udf_objects = ObjectGroup.Port.UdfObjects()
            self.udf_objects.parent = self
            self._children_name_map["udf_objects"] = "udf-objects"
            self._segment_path = lambda: "port"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-objmgr-cfg:object-group/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ObjectGroup.Port, [], name, value)


        class UdfObjects(Entity):
            """
            Table of port objects groups
            
            .. attribute:: udf_object
            
            	Port object group
            	**type**\: list of  		 :py:class:`UdfObject <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg.ObjectGroup.Port.UdfObjects.UdfObject>`
            
            

            """

            _prefix = 'infra-objmgr-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(ObjectGroup.Port.UdfObjects, self).__init__()

                self.yang_name = "udf-objects"
                self.yang_parent_name = "port"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("udf-object", ("udf_object", ObjectGroup.Port.UdfObjects.UdfObject))])
                self._leafs = OrderedDict()

                self.udf_object = YList(self)
                self._segment_path = lambda: "udf-objects"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-objmgr-cfg:object-group/port/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ObjectGroup.Port.UdfObjects, [], name, value)


            class UdfObject(Entity):
                """
                Port object group
                
                .. attribute:: object_name  (key)
                
                	Port object group name \- maximum 64 characters
                	**type**\: str
                
                	**length:** 1..64
                
                .. attribute:: operators
                
                	Table of port operators
                	**type**\:  :py:class:`Operators <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg.ObjectGroup.Port.UdfObjects.UdfObject.Operators>`
                
                .. attribute:: nested_groups
                
                	Table of nested port object groups
                	**type**\:  :py:class:`NestedGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg.ObjectGroup.Port.UdfObjects.UdfObject.NestedGroups>`
                
                .. attribute:: port_ranges
                
                	Table of port range addresses
                	**type**\:  :py:class:`PortRanges <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg.ObjectGroup.Port.UdfObjects.UdfObject.PortRanges>`
                
                .. attribute:: description
                
                	Up to 100 characters describing this object
                	**type**\: str
                
                	**length:** 1..100
                
                

                """

                _prefix = 'infra-objmgr-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(ObjectGroup.Port.UdfObjects.UdfObject, self).__init__()

                    self.yang_name = "udf-object"
                    self.yang_parent_name = "udf-objects"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['object_name']
                    self._child_classes = OrderedDict([("operators", ("operators", ObjectGroup.Port.UdfObjects.UdfObject.Operators)), ("nested-groups", ("nested_groups", ObjectGroup.Port.UdfObjects.UdfObject.NestedGroups)), ("port-ranges", ("port_ranges", ObjectGroup.Port.UdfObjects.UdfObject.PortRanges))])
                    self._leafs = OrderedDict([
                        ('object_name', (YLeaf(YType.str, 'object-name'), ['str'])),
                        ('description', (YLeaf(YType.str, 'description'), ['str'])),
                    ])
                    self.object_name = None
                    self.description = None

                    self.operators = ObjectGroup.Port.UdfObjects.UdfObject.Operators()
                    self.operators.parent = self
                    self._children_name_map["operators"] = "operators"

                    self.nested_groups = ObjectGroup.Port.UdfObjects.UdfObject.NestedGroups()
                    self.nested_groups.parent = self
                    self._children_name_map["nested_groups"] = "nested-groups"

                    self.port_ranges = ObjectGroup.Port.UdfObjects.UdfObject.PortRanges()
                    self.port_ranges.parent = self
                    self._children_name_map["port_ranges"] = "port-ranges"
                    self._segment_path = lambda: "udf-object" + "[object-name='" + str(self.object_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-infra-objmgr-cfg:object-group/port/udf-objects/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ObjectGroup.Port.UdfObjects.UdfObject, ['object_name', 'description'], name, value)


                class Operators(Entity):
                    """
                    Table of port operators
                    
                    .. attribute:: operator
                    
                    	op class
                    	**type**\: list of  		 :py:class:`Operator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg.ObjectGroup.Port.UdfObjects.UdfObject.Operators.Operator>`
                    
                    

                    """

                    _prefix = 'infra-objmgr-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(ObjectGroup.Port.UdfObjects.UdfObject.Operators, self).__init__()

                        self.yang_name = "operators"
                        self.yang_parent_name = "udf-object"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("operator", ("operator", ObjectGroup.Port.UdfObjects.UdfObject.Operators.Operator))])
                        self._leafs = OrderedDict()

                        self.operator = YList(self)
                        self._segment_path = lambda: "operators"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectGroup.Port.UdfObjects.UdfObject.Operators, [], name, value)


                    class Operator(Entity):
                        """
                        op class
                        
                        .. attribute:: operator_type  (key)
                        
                        	operation for ports
                        	**type**\:  :py:class:`PortOperator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg.PortOperator>`
                        
                        .. attribute:: port  (key)
                        
                        	Port number
                        	**type**\: union of the below types:
                        
                        		**type**\:  :py:class:`Port <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg.Port>`
                        
                        		**type**\: int
                        
                        			**range:** 0..65535
                        
                        

                        """

                        _prefix = 'infra-objmgr-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(ObjectGroup.Port.UdfObjects.UdfObject.Operators.Operator, self).__init__()

                            self.yang_name = "operator"
                            self.yang_parent_name = "operators"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['operator_type','port']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('operator_type', (YLeaf(YType.enumeration, 'operator-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg', 'PortOperator', '')])),
                                ('port', (YLeaf(YType.str, 'port'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg', 'Port', ''),'int'])),
                            ])
                            self.operator_type = None
                            self.port = None
                            self._segment_path = lambda: "operator" + "[operator-type='" + str(self.operator_type) + "']" + "[port='" + str(self.port) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(ObjectGroup.Port.UdfObjects.UdfObject.Operators.Operator, ['operator_type', 'port'], name, value)


                class NestedGroups(Entity):
                    """
                    Table of nested port object groups
                    
                    .. attribute:: nested_group
                    
                    	nested object group
                    	**type**\: list of  		 :py:class:`NestedGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg.ObjectGroup.Port.UdfObjects.UdfObject.NestedGroups.NestedGroup>`
                    
                    

                    """

                    _prefix = 'infra-objmgr-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(ObjectGroup.Port.UdfObjects.UdfObject.NestedGroups, self).__init__()

                        self.yang_name = "nested-groups"
                        self.yang_parent_name = "udf-object"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("nested-group", ("nested_group", ObjectGroup.Port.UdfObjects.UdfObject.NestedGroups.NestedGroup))])
                        self._leafs = OrderedDict()

                        self.nested_group = YList(self)
                        self._segment_path = lambda: "nested-groups"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectGroup.Port.UdfObjects.UdfObject.NestedGroups, [], name, value)


                    class NestedGroup(Entity):
                        """
                        nested object group
                        
                        .. attribute:: nested_group_name  (key)
                        
                        	Name of a nested object group
                        	**type**\: str
                        
                        	**length:** 1..64
                        
                        

                        """

                        _prefix = 'infra-objmgr-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(ObjectGroup.Port.UdfObjects.UdfObject.NestedGroups.NestedGroup, self).__init__()

                            self.yang_name = "nested-group"
                            self.yang_parent_name = "nested-groups"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['nested_group_name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('nested_group_name', (YLeaf(YType.str, 'nested-group-name'), ['str'])),
                            ])
                            self.nested_group_name = None
                            self._segment_path = lambda: "nested-group" + "[nested-group-name='" + str(self.nested_group_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(ObjectGroup.Port.UdfObjects.UdfObject.NestedGroups.NestedGroup, ['nested_group_name'], name, value)


                class PortRanges(Entity):
                    """
                    Table of port range addresses
                    
                    .. attribute:: port_range
                    
                    	Match only packets on a given port range
                    	**type**\: list of  		 :py:class:`PortRange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg.ObjectGroup.Port.UdfObjects.UdfObject.PortRanges.PortRange>`
                    
                    

                    """

                    _prefix = 'infra-objmgr-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(ObjectGroup.Port.UdfObjects.UdfObject.PortRanges, self).__init__()

                        self.yang_name = "port-ranges"
                        self.yang_parent_name = "udf-object"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("port-range", ("port_range", ObjectGroup.Port.UdfObjects.UdfObject.PortRanges.PortRange))])
                        self._leafs = OrderedDict()

                        self.port_range = YList(self)
                        self._segment_path = lambda: "port-ranges"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectGroup.Port.UdfObjects.UdfObject.PortRanges, [], name, value)


                    class PortRange(Entity):
                        """
                        Match only packets on a given port range
                        
                        .. attribute:: start_port  (key)
                        
                        	Port number
                        	**type**\: union of the below types:
                        
                        		**type**\:  :py:class:`StartPort <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg.StartPort>`
                        
                        		**type**\: int
                        
                        			**range:** 0..65535
                        
                        .. attribute:: end_port  (key)
                        
                        	Port number
                        	**type**\: union of the below types:
                        
                        		**type**\:  :py:class:`EndPort <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg.EndPort>`
                        
                        		**type**\: int
                        
                        			**range:** 0..65535
                        
                        

                        """

                        _prefix = 'infra-objmgr-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(ObjectGroup.Port.UdfObjects.UdfObject.PortRanges.PortRange, self).__init__()

                            self.yang_name = "port-range"
                            self.yang_parent_name = "port-ranges"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['start_port','end_port']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('start_port', (YLeaf(YType.str, 'start-port'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg', 'StartPort', ''),'int'])),
                                ('end_port', (YLeaf(YType.str, 'end-port'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg', 'EndPort', ''),'int'])),
                            ])
                            self.start_port = None
                            self.end_port = None
                            self._segment_path = lambda: "port-range" + "[start-port='" + str(self.start_port) + "']" + "[end-port='" + str(self.end_port) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(ObjectGroup.Port.UdfObjects.UdfObject.PortRanges.PortRange, ['start_port', 'end_port'], name, value)


    class Network(Entity):
        """
        Network object group
        
        .. attribute:: ipv6
        
        	IPv6 object group
        	**type**\:  :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg.ObjectGroup.Network.Ipv6>`
        
        .. attribute:: ipv4
        
        	IPv4 object group
        	**type**\:  :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg.ObjectGroup.Network.Ipv4>`
        
        

        """

        _prefix = 'infra-objmgr-cfg'
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
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-objmgr-cfg:object-group/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ObjectGroup.Network, [], name, value)


        class Ipv6(Entity):
            """
            IPv6 object group
            
            .. attribute:: udf_objects
            
            	Table of ipv6 object groups
            	**type**\:  :py:class:`UdfObjects <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg.ObjectGroup.Network.Ipv6.UdfObjects>`
            
            

            """

            _prefix = 'infra-objmgr-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(ObjectGroup.Network.Ipv6, self).__init__()

                self.yang_name = "ipv6"
                self.yang_parent_name = "network"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("udf-objects", ("udf_objects", ObjectGroup.Network.Ipv6.UdfObjects))])
                self._leafs = OrderedDict()

                self.udf_objects = ObjectGroup.Network.Ipv6.UdfObjects()
                self.udf_objects.parent = self
                self._children_name_map["udf_objects"] = "udf-objects"
                self._segment_path = lambda: "ipv6"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-objmgr-cfg:object-group/network/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ObjectGroup.Network.Ipv6, [], name, value)


            class UdfObjects(Entity):
                """
                Table of ipv6 object groups
                
                .. attribute:: udf_object
                
                	IPv6 object group
                	**type**\: list of  		 :py:class:`UdfObject <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg.ObjectGroup.Network.Ipv6.UdfObjects.UdfObject>`
                
                

                """

                _prefix = 'infra-objmgr-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(ObjectGroup.Network.Ipv6.UdfObjects, self).__init__()

                    self.yang_name = "udf-objects"
                    self.yang_parent_name = "ipv6"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("udf-object", ("udf_object", ObjectGroup.Network.Ipv6.UdfObjects.UdfObject))])
                    self._leafs = OrderedDict()

                    self.udf_object = YList(self)
                    self._segment_path = lambda: "udf-objects"
                    self._absolute_path = lambda: "Cisco-IOS-XR-infra-objmgr-cfg:object-group/network/ipv6/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ObjectGroup.Network.Ipv6.UdfObjects, [], name, value)


                class UdfObject(Entity):
                    """
                    IPv6 object group
                    
                    .. attribute:: object_name  (key)
                    
                    	IPv6 object group name \- maximum 64 characters
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    .. attribute:: nested_groups
                    
                    	Table of nested ipv6 object groups
                    	**type**\:  :py:class:`NestedGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg.ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.NestedGroups>`
                    
                    .. attribute:: address_ranges
                    
                    	Table of ipv6 address ranges
                    	**type**\:  :py:class:`AddressRanges <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg.ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.AddressRanges>`
                    
                    .. attribute:: addresses
                    
                    	Table of ipv6 addresses
                    	**type**\:  :py:class:`Addresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg.ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.Addresses>`
                    
                    .. attribute:: hosts
                    
                    	Table of ipv6 host addresses
                    	**type**\:  :py:class:`Hosts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg.ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.Hosts>`
                    
                    .. attribute:: description
                    
                    	Up to 100 characters describing this object
                    	**type**\: str
                    
                    	**length:** 1..100
                    
                    

                    """

                    _prefix = 'infra-objmgr-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(ObjectGroup.Network.Ipv6.UdfObjects.UdfObject, self).__init__()

                        self.yang_name = "udf-object"
                        self.yang_parent_name = "udf-objects"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['object_name']
                        self._child_classes = OrderedDict([("nested-groups", ("nested_groups", ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.NestedGroups)), ("address-ranges", ("address_ranges", ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.AddressRanges)), ("addresses", ("addresses", ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.Addresses)), ("hosts", ("hosts", ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.Hosts))])
                        self._leafs = OrderedDict([
                            ('object_name', (YLeaf(YType.str, 'object-name'), ['str'])),
                            ('description', (YLeaf(YType.str, 'description'), ['str'])),
                        ])
                        self.object_name = None
                        self.description = None

                        self.nested_groups = ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.NestedGroups()
                        self.nested_groups.parent = self
                        self._children_name_map["nested_groups"] = "nested-groups"

                        self.address_ranges = ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.AddressRanges()
                        self.address_ranges.parent = self
                        self._children_name_map["address_ranges"] = "address-ranges"

                        self.addresses = ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.Addresses()
                        self.addresses.parent = self
                        self._children_name_map["addresses"] = "addresses"

                        self.hosts = ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.Hosts()
                        self.hosts.parent = self
                        self._children_name_map["hosts"] = "hosts"
                        self._segment_path = lambda: "udf-object" + "[object-name='" + str(self.object_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-infra-objmgr-cfg:object-group/network/ipv6/udf-objects/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectGroup.Network.Ipv6.UdfObjects.UdfObject, ['object_name', 'description'], name, value)


                    class NestedGroups(Entity):
                        """
                        Table of nested ipv6 object groups
                        
                        .. attribute:: nested_group
                        
                        	nested object group
                        	**type**\: list of  		 :py:class:`NestedGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg.ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.NestedGroups.NestedGroup>`
                        
                        

                        """

                        _prefix = 'infra-objmgr-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.NestedGroups, self).__init__()

                            self.yang_name = "nested-groups"
                            self.yang_parent_name = "udf-object"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("nested-group", ("nested_group", ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.NestedGroups.NestedGroup))])
                            self._leafs = OrderedDict()

                            self.nested_group = YList(self)
                            self._segment_path = lambda: "nested-groups"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.NestedGroups, [], name, value)


                        class NestedGroup(Entity):
                            """
                            nested object group
                            
                            .. attribute:: nested_group_name  (key)
                            
                            	Enter the name of a nested object group
                            	**type**\: str
                            
                            	**length:** 1..64
                            
                            

                            """

                            _prefix = 'infra-objmgr-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.NestedGroups.NestedGroup, self).__init__()

                                self.yang_name = "nested-group"
                                self.yang_parent_name = "nested-groups"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['nested_group_name']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('nested_group_name', (YLeaf(YType.str, 'nested-group-name'), ['str'])),
                                ])
                                self.nested_group_name = None
                                self._segment_path = lambda: "nested-group" + "[nested-group-name='" + str(self.nested_group_name) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.NestedGroups.NestedGroup, ['nested_group_name'], name, value)


                    class AddressRanges(Entity):
                        """
                        Table of ipv6 address ranges
                        
                        .. attribute:: address_range
                        
                        	Range of host addresses
                        	**type**\: list of  		 :py:class:`AddressRange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg.ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.AddressRanges.AddressRange>`
                        
                        

                        """

                        _prefix = 'infra-objmgr-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.AddressRanges, self).__init__()

                            self.yang_name = "address-ranges"
                            self.yang_parent_name = "udf-object"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("address-range", ("address_range", ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.AddressRanges.AddressRange))])
                            self._leafs = OrderedDict()

                            self.address_range = YList(self)
                            self._segment_path = lambda: "address-ranges"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.AddressRanges, [], name, value)


                        class AddressRange(Entity):
                            """
                            Range of host addresses
                            
                            .. attribute:: start_address  (key)
                            
                            	IPv6 address
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: end_address  (key)
                            
                            	IPv6 address
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-objmgr-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.AddressRanges.AddressRange, self).__init__()

                                self.yang_name = "address-range"
                                self.yang_parent_name = "address-ranges"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['start_address','end_address']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('start_address', (YLeaf(YType.str, 'start-address'), ['str'])),
                                    ('end_address', (YLeaf(YType.str, 'end-address'), ['str'])),
                                ])
                                self.start_address = None
                                self.end_address = None
                                self._segment_path = lambda: "address-range" + "[start-address='" + str(self.start_address) + "']" + "[end-address='" + str(self.end_address) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.AddressRanges.AddressRange, ['start_address', 'end_address'], name, value)


                    class Addresses(Entity):
                        """
                        Table of ipv6 addresses
                        
                        .. attribute:: address
                        
                        	IPv6 address
                        	**type**\: list of  		 :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg.ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.Addresses.Address>`
                        
                        

                        """

                        _prefix = 'infra-objmgr-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.Addresses, self).__init__()

                            self.yang_name = "addresses"
                            self.yang_parent_name = "udf-object"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("address", ("address", ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.Addresses.Address))])
                            self._leafs = OrderedDict()

                            self.address = YList(self)
                            self._segment_path = lambda: "addresses"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.Addresses, [], name, value)


                        class Address(Entity):
                            """
                            IPv6 address
                            
                            .. attribute:: prefix  (key)
                            
                            	IPv6 prefix x\:x\:\:x/y
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: prefix_length  (key)
                            
                            	Prefix of the IP Address
                            	**type**\: int
                            
                            	**range:** 0..128
                            
                            

                            """

                            _prefix = 'infra-objmgr-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.Addresses.Address, self).__init__()

                                self.yang_name = "address"
                                self.yang_parent_name = "addresses"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['prefix','prefix_length']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('prefix', (YLeaf(YType.str, 'prefix'), ['str'])),
                                    ('prefix_length', (YLeaf(YType.uint8, 'prefix-length'), ['int'])),
                                ])
                                self.prefix = None
                                self.prefix_length = None
                                self._segment_path = lambda: "address" + "[prefix='" + str(self.prefix) + "']" + "[prefix-length='" + str(self.prefix_length) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.Addresses.Address, ['prefix', 'prefix_length'], name, value)


                    class Hosts(Entity):
                        """
                        Table of ipv6 host addresses
                        
                        .. attribute:: host
                        
                        	A single host address
                        	**type**\: list of  		 :py:class:`Host <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg.ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.Hosts.Host>`
                        
                        

                        """

                        _prefix = 'infra-objmgr-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.Hosts, self).__init__()

                            self.yang_name = "hosts"
                            self.yang_parent_name = "udf-object"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("host", ("host", ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.Hosts.Host))])
                            self._leafs = OrderedDict()

                            self.host = YList(self)
                            self._segment_path = lambda: "hosts"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.Hosts, [], name, value)


                        class Host(Entity):
                            """
                            A single host address
                            
                            .. attribute:: host_address  (key)
                            
                            	host ipv6 address
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-objmgr-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.Hosts.Host, self).__init__()

                                self.yang_name = "host"
                                self.yang_parent_name = "hosts"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['host_address']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('host_address', (YLeaf(YType.str, 'host-address'), ['str'])),
                                ])
                                self.host_address = None
                                self._segment_path = lambda: "host" + "[host-address='" + str(self.host_address) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.Hosts.Host, ['host_address'], name, value)


        class Ipv4(Entity):
            """
            IPv4 object group
            
            .. attribute:: udf_objects
            
            	Table of ipv4 object groups
            	**type**\:  :py:class:`UdfObjects <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg.ObjectGroup.Network.Ipv4.UdfObjects>`
            
            

            """

            _prefix = 'infra-objmgr-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(ObjectGroup.Network.Ipv4, self).__init__()

                self.yang_name = "ipv4"
                self.yang_parent_name = "network"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("udf-objects", ("udf_objects", ObjectGroup.Network.Ipv4.UdfObjects))])
                self._leafs = OrderedDict()

                self.udf_objects = ObjectGroup.Network.Ipv4.UdfObjects()
                self.udf_objects.parent = self
                self._children_name_map["udf_objects"] = "udf-objects"
                self._segment_path = lambda: "ipv4"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-objmgr-cfg:object-group/network/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ObjectGroup.Network.Ipv4, [], name, value)


            class UdfObjects(Entity):
                """
                Table of ipv4 object groups
                
                .. attribute:: udf_object
                
                	IPv4 object group
                	**type**\: list of  		 :py:class:`UdfObject <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg.ObjectGroup.Network.Ipv4.UdfObjects.UdfObject>`
                
                

                """

                _prefix = 'infra-objmgr-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(ObjectGroup.Network.Ipv4.UdfObjects, self).__init__()

                    self.yang_name = "udf-objects"
                    self.yang_parent_name = "ipv4"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("udf-object", ("udf_object", ObjectGroup.Network.Ipv4.UdfObjects.UdfObject))])
                    self._leafs = OrderedDict()

                    self.udf_object = YList(self)
                    self._segment_path = lambda: "udf-objects"
                    self._absolute_path = lambda: "Cisco-IOS-XR-infra-objmgr-cfg:object-group/network/ipv4/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ObjectGroup.Network.Ipv4.UdfObjects, [], name, value)


                class UdfObject(Entity):
                    """
                    IPv4 object group
                    
                    .. attribute:: object_name  (key)
                    
                    	IPv4 object group name \- maximum 64 characters
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    .. attribute:: nested_groups
                    
                    	Table of nested ipv4 object groups
                    	**type**\:  :py:class:`NestedGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg.ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.NestedGroups>`
                    
                    .. attribute:: address_ranges
                    
                    	Table of ipv4 host address ranges
                    	**type**\:  :py:class:`AddressRanges <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg.ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.AddressRanges>`
                    
                    .. attribute:: addresses
                    
                    	Table of addresses
                    	**type**\:  :py:class:`Addresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg.ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.Addresses>`
                    
                    .. attribute:: hosts
                    
                    	Table of host addresses
                    	**type**\:  :py:class:`Hosts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg.ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.Hosts>`
                    
                    .. attribute:: description
                    
                    	Up to 100 characters describing this object
                    	**type**\: str
                    
                    	**length:** 1..100
                    
                    

                    """

                    _prefix = 'infra-objmgr-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(ObjectGroup.Network.Ipv4.UdfObjects.UdfObject, self).__init__()

                        self.yang_name = "udf-object"
                        self.yang_parent_name = "udf-objects"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['object_name']
                        self._child_classes = OrderedDict([("nested-groups", ("nested_groups", ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.NestedGroups)), ("address-ranges", ("address_ranges", ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.AddressRanges)), ("addresses", ("addresses", ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.Addresses)), ("hosts", ("hosts", ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.Hosts))])
                        self._leafs = OrderedDict([
                            ('object_name', (YLeaf(YType.str, 'object-name'), ['str'])),
                            ('description', (YLeaf(YType.str, 'description'), ['str'])),
                        ])
                        self.object_name = None
                        self.description = None

                        self.nested_groups = ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.NestedGroups()
                        self.nested_groups.parent = self
                        self._children_name_map["nested_groups"] = "nested-groups"

                        self.address_ranges = ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.AddressRanges()
                        self.address_ranges.parent = self
                        self._children_name_map["address_ranges"] = "address-ranges"

                        self.addresses = ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.Addresses()
                        self.addresses.parent = self
                        self._children_name_map["addresses"] = "addresses"

                        self.hosts = ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.Hosts()
                        self.hosts.parent = self
                        self._children_name_map["hosts"] = "hosts"
                        self._segment_path = lambda: "udf-object" + "[object-name='" + str(self.object_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-infra-objmgr-cfg:object-group/network/ipv4/udf-objects/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectGroup.Network.Ipv4.UdfObjects.UdfObject, ['object_name', 'description'], name, value)


                    class NestedGroups(Entity):
                        """
                        Table of nested ipv4 object groups
                        
                        .. attribute:: nested_group
                        
                        	Nested object group
                        	**type**\: list of  		 :py:class:`NestedGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg.ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.NestedGroups.NestedGroup>`
                        
                        

                        """

                        _prefix = 'infra-objmgr-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.NestedGroups, self).__init__()

                            self.yang_name = "nested-groups"
                            self.yang_parent_name = "udf-object"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("nested-group", ("nested_group", ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.NestedGroups.NestedGroup))])
                            self._leafs = OrderedDict()

                            self.nested_group = YList(self)
                            self._segment_path = lambda: "nested-groups"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.NestedGroups, [], name, value)


                        class NestedGroup(Entity):
                            """
                            Nested object group
                            
                            .. attribute:: nested_group_name  (key)
                            
                            	Nested object group
                            	**type**\: str
                            
                            	**length:** 1..64
                            
                            

                            """

                            _prefix = 'infra-objmgr-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.NestedGroups.NestedGroup, self).__init__()

                                self.yang_name = "nested-group"
                                self.yang_parent_name = "nested-groups"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['nested_group_name']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('nested_group_name', (YLeaf(YType.str, 'nested-group-name'), ['str'])),
                                ])
                                self.nested_group_name = None
                                self._segment_path = lambda: "nested-group" + "[nested-group-name='" + str(self.nested_group_name) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.NestedGroups.NestedGroup, ['nested_group_name'], name, value)


                    class AddressRanges(Entity):
                        """
                        Table of ipv4 host address ranges
                        
                        .. attribute:: address_range
                        
                        	Range of host addresses
                        	**type**\: list of  		 :py:class:`AddressRange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg.ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.AddressRanges.AddressRange>`
                        
                        

                        """

                        _prefix = 'infra-objmgr-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.AddressRanges, self).__init__()

                            self.yang_name = "address-ranges"
                            self.yang_parent_name = "udf-object"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("address-range", ("address_range", ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.AddressRanges.AddressRange))])
                            self._leafs = OrderedDict()

                            self.address_range = YList(self)
                            self._segment_path = lambda: "address-ranges"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.AddressRanges, [], name, value)


                        class AddressRange(Entity):
                            """
                            Range of host addresses
                            
                            .. attribute:: start_address  (key)
                            
                            	IPv4 address
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: end_address  (key)
                            
                            	IPv4 address
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-objmgr-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.AddressRanges.AddressRange, self).__init__()

                                self.yang_name = "address-range"
                                self.yang_parent_name = "address-ranges"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['start_address','end_address']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('start_address', (YLeaf(YType.str, 'start-address'), ['str'])),
                                    ('end_address', (YLeaf(YType.str, 'end-address'), ['str'])),
                                ])
                                self.start_address = None
                                self.end_address = None
                                self._segment_path = lambda: "address-range" + "[start-address='" + str(self.start_address) + "']" + "[end-address='" + str(self.end_address) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.AddressRanges.AddressRange, ['start_address', 'end_address'], name, value)


                    class Addresses(Entity):
                        """
                        Table of addresses
                        
                        .. attribute:: address
                        
                        	IPv4 address
                        	**type**\: list of  		 :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg.ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.Addresses.Address>`
                        
                        

                        """

                        _prefix = 'infra-objmgr-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.Addresses, self).__init__()

                            self.yang_name = "addresses"
                            self.yang_parent_name = "udf-object"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("address", ("address", ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.Addresses.Address))])
                            self._leafs = OrderedDict()

                            self.address = YList(self)
                            self._segment_path = lambda: "addresses"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.Addresses, [], name, value)


                        class Address(Entity):
                            """
                            IPv4 address
                            
                            .. attribute:: prefix  (key)
                            
                            	IPv4 address/prefix
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: prefix_length  (key)
                            
                            	Prefix of the IP Address
                            	**type**\: int
                            
                            	**range:** 0..32
                            
                            

                            """

                            _prefix = 'infra-objmgr-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.Addresses.Address, self).__init__()

                                self.yang_name = "address"
                                self.yang_parent_name = "addresses"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['prefix','prefix_length']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('prefix', (YLeaf(YType.str, 'prefix'), ['str'])),
                                    ('prefix_length', (YLeaf(YType.uint8, 'prefix-length'), ['int'])),
                                ])
                                self.prefix = None
                                self.prefix_length = None
                                self._segment_path = lambda: "address" + "[prefix='" + str(self.prefix) + "']" + "[prefix-length='" + str(self.prefix_length) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.Addresses.Address, ['prefix', 'prefix_length'], name, value)


                    class Hosts(Entity):
                        """
                        Table of host addresses
                        
                        .. attribute:: host
                        
                        	A single host address
                        	**type**\: list of  		 :py:class:`Host <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg.ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.Hosts.Host>`
                        
                        

                        """

                        _prefix = 'infra-objmgr-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.Hosts, self).__init__()

                            self.yang_name = "hosts"
                            self.yang_parent_name = "udf-object"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("host", ("host", ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.Hosts.Host))])
                            self._leafs = OrderedDict()

                            self.host = YList(self)
                            self._segment_path = lambda: "hosts"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.Hosts, [], name, value)


                        class Host(Entity):
                            """
                            A single host address
                            
                            .. attribute:: host_address  (key)
                            
                            	Host ipv4 address
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-objmgr-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.Hosts.Host, self).__init__()

                                self.yang_name = "host"
                                self.yang_parent_name = "hosts"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['host_address']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('host_address', (YLeaf(YType.str, 'host-address'), ['str'])),
                                ])
                                self.host_address = None
                                self._segment_path = lambda: "host" + "[host-address='" + str(self.host_address) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.Hosts.Host, ['host_address'], name, value)

    def clone_ptr(self):
        self._top_entity = ObjectGroup()
        return self._top_entity

