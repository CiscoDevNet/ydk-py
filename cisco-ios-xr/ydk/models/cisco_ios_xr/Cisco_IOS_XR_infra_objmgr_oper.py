""" Cisco_IOS_XR_infra_objmgr_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-objmgr package operational data.

This module contains definitions
for the following management objects\:
  object\-group\: Object\-group operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class EndPortEnum(Enum):
    """
    EndPortEnum

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

    echo = 7

    discard = 9

    daytime = 13

    chargen = 19

    ftp_data = 20

    ftp = 21

    ssh = 22

    telnet = 23

    smtp = 25

    time = 37

    nicname = 43

    tacacs = 49

    domain = 53

    gopher = 70

    finger = 79

    www = 80

    host_name = 101

    pop2 = 109

    pop3 = 110

    sun_rpc = 111

    ident = 113

    nntp = 119

    bgp = 179

    irc = 194

    pim_auto_rp = 496

    exec_ = 512

    login = 513

    cmd = 514

    lpd = 515

    uucp = 540

    klogin = 543

    kshell = 544

    talk = 517

    ldp = 646


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_objmgr_oper as meta
        return meta._meta_table['EndPortEnum']


class PortEnum(Enum):
    """
    PortEnum

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

    echo = 7

    discard = 9

    daytime = 13

    chargen = 19

    ftp_data = 20

    ftp = 21

    ssh = 22

    telnet = 23

    smtp = 25

    time = 37

    nicname = 43

    tacacs = 49

    domain = 53

    gopher = 70

    finger = 79

    www = 80

    host_name = 101

    pop2 = 109

    pop3 = 110

    sun_rpc = 111

    ident = 113

    nntp = 119

    bgp = 179

    irc = 194

    pim_auto_rp = 496

    exec_ = 512

    login = 513

    cmd = 514

    lpd = 515

    uucp = 540

    klogin = 543

    kshell = 544

    talk = 517

    ldp = 646


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_objmgr_oper as meta
        return meta._meta_table['PortEnum']


class PortOperatorEnum(Enum):
    """
    PortOperatorEnum

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

    equal = 0

    not_equal = 1

    greater_than = 2

    less_than = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_objmgr_oper as meta
        return meta._meta_table['PortOperatorEnum']


class StartPortEnum(Enum):
    """
    StartPortEnum

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

    echo = 7

    discard = 9

    daytime = 13

    chargen = 19

    ftp_data = 20

    ftp = 21

    ssh = 22

    telnet = 23

    smtp = 25

    time = 37

    nicname = 43

    tacacs = 49

    domain = 53

    gopher = 70

    finger = 79

    www = 80

    host_name = 101

    pop2 = 109

    pop3 = 110

    sun_rpc = 111

    ident = 113

    nntp = 119

    bgp = 179

    irc = 194

    pim_auto_rp = 496

    exec_ = 512

    login = 513

    cmd = 514

    lpd = 515

    uucp = 540

    klogin = 543

    kshell = 544

    talk = 517

    ldp = 646


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_objmgr_oper as meta
        return meta._meta_table['StartPortEnum']



class ObjectGroup(object):
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
        self.network = ObjectGroup.Network()
        self.network.parent = self
        self.port = ObjectGroup.Port()
        self.port.parent = self


    class Port(object):
        """
        Port object group
        
        .. attribute:: objects
        
        	Table of Object
        	**type**\:   :py:class:`Objects <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Port.Objects>`
        
        

        """

        _prefix = 'infra-objmgr-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.objects = ObjectGroup.Port.Objects()
            self.objects.parent = self


        class Objects(object):
            """
            Table of Object
            
            .. attribute:: object
            
            	Port object group
            	**type**\: list of    :py:class:`Object <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Port.Objects.Object>`
            
            

            """

            _prefix = 'infra-objmgr-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.object = YList()
                self.object.parent = self
                self.object.name = 'object'


            class Object(object):
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
                    self.parent = None
                    self.object_name = None
                    self.nested_groups = ObjectGroup.Port.Objects.Object.NestedGroups()
                    self.nested_groups.parent = self
                    self.operators = ObjectGroup.Port.Objects.Object.Operators()
                    self.operators.parent = self
                    self.parent_groups = ObjectGroup.Port.Objects.Object.ParentGroups()
                    self.parent_groups.parent = self
                    self.port_ranges = ObjectGroup.Port.Objects.Object.PortRanges()
                    self.port_ranges.parent = self


                class NestedGroups(object):
                    """
                    Table of NestedGroup
                    
                    .. attribute:: nested_group
                    
                    	nested object group
                    	**type**\: list of    :py:class:`NestedGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Port.Objects.Object.NestedGroups.NestedGroup>`
                    
                    

                    """

                    _prefix = 'infra-objmgr-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.nested_group = YList()
                        self.nested_group.parent = self
                        self.nested_group.name = 'nested_group'


                    class NestedGroup(object):
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
                            self.parent = None
                            self.nested_group_name = None
                            self.nested_group_name_xr = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.nested_group_name is None:
                                raise YPYModelError('Key property nested_group_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-objmgr-oper:nested-group[Cisco-IOS-XR-infra-objmgr-oper:nested-group-name = ' + str(self.nested_group_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.nested_group_name is not None:
                                return True

                            if self.nested_group_name_xr is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_objmgr_oper as meta
                            return meta._meta_table['ObjectGroup.Port.Objects.Object.NestedGroups.NestedGroup']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-objmgr-oper:nested-groups'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.nested_group is not None:
                            for child_ref in self.nested_group:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_objmgr_oper as meta
                        return meta._meta_table['ObjectGroup.Port.Objects.Object.NestedGroups']['meta_info']


                class Operators(object):
                    """
                    Table of Operator
                    
                    .. attribute:: operator
                    
                    	op class
                    	**type**\: list of    :py:class:`Operator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Port.Objects.Object.Operators.Operator>`
                    
                    

                    """

                    _prefix = 'infra-objmgr-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.operator = YList()
                        self.operator.parent = self
                        self.operator.name = 'operator'


                    class Operator(object):
                        """
                        op class
                        
                        .. attribute:: operator_type
                        
                        	operation for ports
                        	**type**\:   :py:class:`PortOperatorEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.PortOperatorEnum>`
                        
                        .. attribute:: operator_type_xr
                        
                        	Operator
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: port
                        
                        	Port number
                        	**type**\: one of the below types:
                        
                        	**type**\:   :py:class:`PortEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.PortEnum>`
                        
                        
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
                            self.parent = None
                            self.operator_type = None
                            self.operator_type_xr = None
                            self.port = None
                            self.port_xr = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-objmgr-oper:operator'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.operator_type is not None:
                                return True

                            if self.operator_type_xr is not None:
                                return True

                            if self.port is not None:
                                return True

                            if self.port_xr is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_objmgr_oper as meta
                            return meta._meta_table['ObjectGroup.Port.Objects.Object.Operators.Operator']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-objmgr-oper:operators'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.operator is not None:
                            for child_ref in self.operator:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_objmgr_oper as meta
                        return meta._meta_table['ObjectGroup.Port.Objects.Object.Operators']['meta_info']


                class PortRanges(object):
                    """
                    Table of PortRange
                    
                    .. attribute:: port_range
                    
                    	Match only packets on a given port range
                    	**type**\: list of    :py:class:`PortRange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Port.Objects.Object.PortRanges.PortRange>`
                    
                    

                    """

                    _prefix = 'infra-objmgr-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.port_range = YList()
                        self.port_range.parent = self
                        self.port_range.name = 'port_range'


                    class PortRange(object):
                        """
                        Match only packets on a given port range
                        
                        .. attribute:: end_port
                        
                        	End port number
                        	**type**\: one of the below types:
                        
                        	**type**\:   :py:class:`EndPortEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.EndPortEnum>`
                        
                        
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
                        
                        	**type**\:   :py:class:`StartPortEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.StartPortEnum>`
                        
                        
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
                            self.parent = None
                            self.end_port = None
                            self.end_port_xr = None
                            self.start_port = None
                            self.start_port_xr = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-objmgr-oper:port-range'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.end_port is not None:
                                return True

                            if self.end_port_xr is not None:
                                return True

                            if self.start_port is not None:
                                return True

                            if self.start_port_xr is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_objmgr_oper as meta
                            return meta._meta_table['ObjectGroup.Port.Objects.Object.PortRanges.PortRange']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-objmgr-oper:port-ranges'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.port_range is not None:
                            for child_ref in self.port_range:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_objmgr_oper as meta
                        return meta._meta_table['ObjectGroup.Port.Objects.Object.PortRanges']['meta_info']


                class ParentGroups(object):
                    """
                    Table of ParentGroup
                    
                    .. attribute:: parent_group
                    
                    	Parent object group
                    	**type**\: list of    :py:class:`ParentGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Port.Objects.Object.ParentGroups.ParentGroup>`
                    
                    

                    """

                    _prefix = 'infra-objmgr-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.parent_group = YList()
                        self.parent_group.parent = self
                        self.parent_group.name = 'parent_group'


                    class ParentGroup(object):
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
                            self.parent = None
                            self.parent_group_name = None
                            self.parent_name = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.parent_group_name is None:
                                raise YPYModelError('Key property parent_group_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-objmgr-oper:parent-group[Cisco-IOS-XR-infra-objmgr-oper:parent-group-name = ' + str(self.parent_group_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.parent_group_name is not None:
                                return True

                            if self.parent_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_objmgr_oper as meta
                            return meta._meta_table['ObjectGroup.Port.Objects.Object.ParentGroups.ParentGroup']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-objmgr-oper:parent-groups'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.parent_group is not None:
                            for child_ref in self.parent_group:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_objmgr_oper as meta
                        return meta._meta_table['ObjectGroup.Port.Objects.Object.ParentGroups']['meta_info']

                @property
                def _common_path(self):
                    if self.object_name is None:
                        raise YPYModelError('Key property object_name is None')

                    return '/Cisco-IOS-XR-infra-objmgr-oper:object-group/Cisco-IOS-XR-infra-objmgr-oper:port/Cisco-IOS-XR-infra-objmgr-oper:objects/Cisco-IOS-XR-infra-objmgr-oper:object[Cisco-IOS-XR-infra-objmgr-oper:object-name = ' + str(self.object_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.object_name is not None:
                        return True

                    if self.nested_groups is not None and self.nested_groups._has_data():
                        return True

                    if self.operators is not None and self.operators._has_data():
                        return True

                    if self.parent_groups is not None and self.parent_groups._has_data():
                        return True

                    if self.port_ranges is not None and self.port_ranges._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_objmgr_oper as meta
                    return meta._meta_table['ObjectGroup.Port.Objects.Object']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-infra-objmgr-oper:object-group/Cisco-IOS-XR-infra-objmgr-oper:port/Cisco-IOS-XR-infra-objmgr-oper:objects'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.object is not None:
                    for child_ref in self.object:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_objmgr_oper as meta
                return meta._meta_table['ObjectGroup.Port.Objects']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-objmgr-oper:object-group/Cisco-IOS-XR-infra-objmgr-oper:port'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.objects is not None and self.objects._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_objmgr_oper as meta
            return meta._meta_table['ObjectGroup.Port']['meta_info']


    class Network(object):
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
            self.parent = None
            self.ipv4 = ObjectGroup.Network.Ipv4()
            self.ipv4.parent = self
            self.ipv6 = ObjectGroup.Network.Ipv6()
            self.ipv6.parent = self


        class Ipv6(object):
            """
            IPv6 object group
            
            .. attribute:: objects
            
            	Table of Object
            	**type**\:   :py:class:`Objects <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Network.Ipv6.Objects>`
            
            

            """

            _prefix = 'infra-objmgr-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.objects = ObjectGroup.Network.Ipv6.Objects()
                self.objects.parent = self


            class Objects(object):
                """
                Table of Object
                
                .. attribute:: object
                
                	IPv6 object group
                	**type**\: list of    :py:class:`Object <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Network.Ipv6.Objects.Object>`
                
                

                """

                _prefix = 'infra-objmgr-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.object = YList()
                    self.object.parent = self
                    self.object.name = 'object'


                class Object(object):
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
                        self.parent = None
                        self.object_name = None
                        self.address_ranges = ObjectGroup.Network.Ipv6.Objects.Object.AddressRanges()
                        self.address_ranges.parent = self
                        self.addresses = ObjectGroup.Network.Ipv6.Objects.Object.Addresses()
                        self.addresses.parent = self
                        self.hosts = ObjectGroup.Network.Ipv6.Objects.Object.Hosts()
                        self.hosts.parent = self
                        self.nested_groups = ObjectGroup.Network.Ipv6.Objects.Object.NestedGroups()
                        self.nested_groups.parent = self
                        self.parent_groups = ObjectGroup.Network.Ipv6.Objects.Object.ParentGroups()
                        self.parent_groups.parent = self


                    class NestedGroups(object):
                        """
                        Table of NestedGroup
                        
                        .. attribute:: nested_group
                        
                        	nested object group
                        	**type**\: list of    :py:class:`NestedGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Network.Ipv6.Objects.Object.NestedGroups.NestedGroup>`
                        
                        

                        """

                        _prefix = 'infra-objmgr-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.nested_group = YList()
                            self.nested_group.parent = self
                            self.nested_group.name = 'nested_group'


                        class NestedGroup(object):
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
                                self.parent = None
                                self.nested_group_name = None
                                self.nested_group_name_xr = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.nested_group_name is None:
                                    raise YPYModelError('Key property nested_group_name is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-objmgr-oper:nested-group[Cisco-IOS-XR-infra-objmgr-oper:nested-group-name = ' + str(self.nested_group_name) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.nested_group_name is not None:
                                    return True

                                if self.nested_group_name_xr is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_objmgr_oper as meta
                                return meta._meta_table['ObjectGroup.Network.Ipv6.Objects.Object.NestedGroups.NestedGroup']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-objmgr-oper:nested-groups'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.nested_group is not None:
                                for child_ref in self.nested_group:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_objmgr_oper as meta
                            return meta._meta_table['ObjectGroup.Network.Ipv6.Objects.Object.NestedGroups']['meta_info']


                    class Addresses(object):
                        """
                        Table of Address
                        
                        .. attribute:: address
                        
                        	IPv6 address
                        	**type**\: list of    :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Network.Ipv6.Objects.Object.Addresses.Address>`
                        
                        

                        """

                        _prefix = 'infra-objmgr-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.address = YList()
                            self.address.parent = self
                            self.address.name = 'address'


                        class Address(object):
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
                                self.parent = None
                                self.prefix = None
                                self.prefix_length = None
                                self.prefix_length_xr = None
                                self.prefix_xr = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-objmgr-oper:address'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.prefix is not None:
                                    return True

                                if self.prefix_length is not None:
                                    return True

                                if self.prefix_length_xr is not None:
                                    return True

                                if self.prefix_xr is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_objmgr_oper as meta
                                return meta._meta_table['ObjectGroup.Network.Ipv6.Objects.Object.Addresses.Address']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-objmgr-oper:addresses'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.address is not None:
                                for child_ref in self.address:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_objmgr_oper as meta
                            return meta._meta_table['ObjectGroup.Network.Ipv6.Objects.Object.Addresses']['meta_info']


                    class AddressRanges(object):
                        """
                        Table of AddressRange
                        
                        .. attribute:: address_range
                        
                        	Range of host addresses
                        	**type**\: list of    :py:class:`AddressRange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Network.Ipv6.Objects.Object.AddressRanges.AddressRange>`
                        
                        

                        """

                        _prefix = 'infra-objmgr-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.address_range = YList()
                            self.address_range.parent = self
                            self.address_range.name = 'address_range'


                        class AddressRange(object):
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
                                self.parent = None
                                self.end_address = None
                                self.end_address_xr = None
                                self.start_address = None
                                self.start_address_xr = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-objmgr-oper:address-range'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.end_address is not None:
                                    return True

                                if self.end_address_xr is not None:
                                    return True

                                if self.start_address is not None:
                                    return True

                                if self.start_address_xr is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_objmgr_oper as meta
                                return meta._meta_table['ObjectGroup.Network.Ipv6.Objects.Object.AddressRanges.AddressRange']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-objmgr-oper:address-ranges'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.address_range is not None:
                                for child_ref in self.address_range:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_objmgr_oper as meta
                            return meta._meta_table['ObjectGroup.Network.Ipv6.Objects.Object.AddressRanges']['meta_info']


                    class ParentGroups(object):
                        """
                        Table of parent object group
                        
                        .. attribute:: parent_group
                        
                        	Parent object group
                        	**type**\: list of    :py:class:`ParentGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Network.Ipv6.Objects.Object.ParentGroups.ParentGroup>`
                        
                        

                        """

                        _prefix = 'infra-objmgr-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.parent_group = YList()
                            self.parent_group.parent = self
                            self.parent_group.name = 'parent_group'


                        class ParentGroup(object):
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
                                self.parent = None
                                self.parent_group_name = None
                                self.parent_name = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.parent_group_name is None:
                                    raise YPYModelError('Key property parent_group_name is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-objmgr-oper:parent-group[Cisco-IOS-XR-infra-objmgr-oper:parent-group-name = ' + str(self.parent_group_name) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.parent_group_name is not None:
                                    return True

                                if self.parent_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_objmgr_oper as meta
                                return meta._meta_table['ObjectGroup.Network.Ipv6.Objects.Object.ParentGroups.ParentGroup']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-objmgr-oper:parent-groups'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.parent_group is not None:
                                for child_ref in self.parent_group:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_objmgr_oper as meta
                            return meta._meta_table['ObjectGroup.Network.Ipv6.Objects.Object.ParentGroups']['meta_info']


                    class Hosts(object):
                        """
                        Table of Host
                        
                        .. attribute:: host
                        
                        	A single host address
                        	**type**\: list of    :py:class:`Host <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Network.Ipv6.Objects.Object.Hosts.Host>`
                        
                        

                        """

                        _prefix = 'infra-objmgr-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.host = YList()
                            self.host.parent = self
                            self.host.name = 'host'


                        class Host(object):
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
                                self.parent = None
                                self.host_address = None
                                self.host_address_xr = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.host_address is None:
                                    raise YPYModelError('Key property host_address is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-objmgr-oper:host[Cisco-IOS-XR-infra-objmgr-oper:host-address = ' + str(self.host_address) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.host_address is not None:
                                    return True

                                if self.host_address_xr is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_objmgr_oper as meta
                                return meta._meta_table['ObjectGroup.Network.Ipv6.Objects.Object.Hosts.Host']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-objmgr-oper:hosts'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.host is not None:
                                for child_ref in self.host:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_objmgr_oper as meta
                            return meta._meta_table['ObjectGroup.Network.Ipv6.Objects.Object.Hosts']['meta_info']

                    @property
                    def _common_path(self):
                        if self.object_name is None:
                            raise YPYModelError('Key property object_name is None')

                        return '/Cisco-IOS-XR-infra-objmgr-oper:object-group/Cisco-IOS-XR-infra-objmgr-oper:network/Cisco-IOS-XR-infra-objmgr-oper:ipv6/Cisco-IOS-XR-infra-objmgr-oper:objects/Cisco-IOS-XR-infra-objmgr-oper:object[Cisco-IOS-XR-infra-objmgr-oper:object-name = ' + str(self.object_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.object_name is not None:
                            return True

                        if self.address_ranges is not None and self.address_ranges._has_data():
                            return True

                        if self.addresses is not None and self.addresses._has_data():
                            return True

                        if self.hosts is not None and self.hosts._has_data():
                            return True

                        if self.nested_groups is not None and self.nested_groups._has_data():
                            return True

                        if self.parent_groups is not None and self.parent_groups._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_objmgr_oper as meta
                        return meta._meta_table['ObjectGroup.Network.Ipv6.Objects.Object']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-infra-objmgr-oper:object-group/Cisco-IOS-XR-infra-objmgr-oper:network/Cisco-IOS-XR-infra-objmgr-oper:ipv6/Cisco-IOS-XR-infra-objmgr-oper:objects'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.object is not None:
                        for child_ref in self.object:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_objmgr_oper as meta
                    return meta._meta_table['ObjectGroup.Network.Ipv6.Objects']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-infra-objmgr-oper:object-group/Cisco-IOS-XR-infra-objmgr-oper:network/Cisco-IOS-XR-infra-objmgr-oper:ipv6'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.objects is not None and self.objects._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_objmgr_oper as meta
                return meta._meta_table['ObjectGroup.Network.Ipv6']['meta_info']


        class Ipv4(object):
            """
            IPv4 object group
            
            .. attribute:: objects
            
            	Table of Object
            	**type**\:   :py:class:`Objects <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Network.Ipv4.Objects>`
            
            

            """

            _prefix = 'infra-objmgr-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.objects = ObjectGroup.Network.Ipv4.Objects()
                self.objects.parent = self


            class Objects(object):
                """
                Table of Object
                
                .. attribute:: object
                
                	IPv4 object group
                	**type**\: list of    :py:class:`Object <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Network.Ipv4.Objects.Object>`
                
                

                """

                _prefix = 'infra-objmgr-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.object = YList()
                    self.object.parent = self
                    self.object.name = 'object'


                class Object(object):
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
                        self.parent = None
                        self.object_name = None
                        self.address_ranges = ObjectGroup.Network.Ipv4.Objects.Object.AddressRanges()
                        self.address_ranges.parent = self
                        self.addresses = ObjectGroup.Network.Ipv4.Objects.Object.Addresses()
                        self.addresses.parent = self
                        self.hosts = ObjectGroup.Network.Ipv4.Objects.Object.Hosts()
                        self.hosts.parent = self
                        self.nested_groups = ObjectGroup.Network.Ipv4.Objects.Object.NestedGroups()
                        self.nested_groups.parent = self
                        self.parent_groups = ObjectGroup.Network.Ipv4.Objects.Object.ParentGroups()
                        self.parent_groups.parent = self


                    class NestedGroups(object):
                        """
                        Table of NestedGroup
                        
                        .. attribute:: nested_group
                        
                        	Nested object group
                        	**type**\: list of    :py:class:`NestedGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Network.Ipv4.Objects.Object.NestedGroups.NestedGroup>`
                        
                        

                        """

                        _prefix = 'infra-objmgr-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.nested_group = YList()
                            self.nested_group.parent = self
                            self.nested_group.name = 'nested_group'


                        class NestedGroup(object):
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
                                self.parent = None
                                self.nested_group_name = None
                                self.nested_group_name_xr = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.nested_group_name is None:
                                    raise YPYModelError('Key property nested_group_name is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-objmgr-oper:nested-group[Cisco-IOS-XR-infra-objmgr-oper:nested-group-name = ' + str(self.nested_group_name) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.nested_group_name is not None:
                                    return True

                                if self.nested_group_name_xr is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_objmgr_oper as meta
                                return meta._meta_table['ObjectGroup.Network.Ipv4.Objects.Object.NestedGroups.NestedGroup']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-objmgr-oper:nested-groups'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.nested_group is not None:
                                for child_ref in self.nested_group:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_objmgr_oper as meta
                            return meta._meta_table['ObjectGroup.Network.Ipv4.Objects.Object.NestedGroups']['meta_info']


                    class Addresses(object):
                        """
                        Table of Address
                        
                        .. attribute:: address
                        
                        	IPv4 address
                        	**type**\: list of    :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Network.Ipv4.Objects.Object.Addresses.Address>`
                        
                        

                        """

                        _prefix = 'infra-objmgr-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.address = YList()
                            self.address.parent = self
                            self.address.name = 'address'


                        class Address(object):
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
                                self.parent = None
                                self.prefix = None
                                self.prefix_length = None
                                self.prefix_length_xr = None
                                self.prefix_xr = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-objmgr-oper:address'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.prefix is not None:
                                    return True

                                if self.prefix_length is not None:
                                    return True

                                if self.prefix_length_xr is not None:
                                    return True

                                if self.prefix_xr is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_objmgr_oper as meta
                                return meta._meta_table['ObjectGroup.Network.Ipv4.Objects.Object.Addresses.Address']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-objmgr-oper:addresses'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.address is not None:
                                for child_ref in self.address:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_objmgr_oper as meta
                            return meta._meta_table['ObjectGroup.Network.Ipv4.Objects.Object.Addresses']['meta_info']


                    class AddressRanges(object):
                        """
                        Table of AddressRange
                        
                        .. attribute:: address_range
                        
                        	Range of host addresses
                        	**type**\: list of    :py:class:`AddressRange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Network.Ipv4.Objects.Object.AddressRanges.AddressRange>`
                        
                        

                        """

                        _prefix = 'infra-objmgr-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.address_range = YList()
                            self.address_range.parent = self
                            self.address_range.name = 'address_range'


                        class AddressRange(object):
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
                                self.parent = None
                                self.end_address = None
                                self.end_address_xr = None
                                self.start_address = None
                                self.start_address_xr = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-objmgr-oper:address-range'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.end_address is not None:
                                    return True

                                if self.end_address_xr is not None:
                                    return True

                                if self.start_address is not None:
                                    return True

                                if self.start_address_xr is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_objmgr_oper as meta
                                return meta._meta_table['ObjectGroup.Network.Ipv4.Objects.Object.AddressRanges.AddressRange']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-objmgr-oper:address-ranges'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.address_range is not None:
                                for child_ref in self.address_range:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_objmgr_oper as meta
                            return meta._meta_table['ObjectGroup.Network.Ipv4.Objects.Object.AddressRanges']['meta_info']


                    class ParentGroups(object):
                        """
                        Table of parent object group
                        
                        .. attribute:: parent_group
                        
                        	Parent object group
                        	**type**\: list of    :py:class:`ParentGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Network.Ipv4.Objects.Object.ParentGroups.ParentGroup>`
                        
                        

                        """

                        _prefix = 'infra-objmgr-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.parent_group = YList()
                            self.parent_group.parent = self
                            self.parent_group.name = 'parent_group'


                        class ParentGroup(object):
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
                                self.parent = None
                                self.parent_group_name = None
                                self.parent_name = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.parent_group_name is None:
                                    raise YPYModelError('Key property parent_group_name is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-objmgr-oper:parent-group[Cisco-IOS-XR-infra-objmgr-oper:parent-group-name = ' + str(self.parent_group_name) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.parent_group_name is not None:
                                    return True

                                if self.parent_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_objmgr_oper as meta
                                return meta._meta_table['ObjectGroup.Network.Ipv4.Objects.Object.ParentGroups.ParentGroup']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-objmgr-oper:parent-groups'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.parent_group is not None:
                                for child_ref in self.parent_group:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_objmgr_oper as meta
                            return meta._meta_table['ObjectGroup.Network.Ipv4.Objects.Object.ParentGroups']['meta_info']


                    class Hosts(object):
                        """
                        Table of Host
                        
                        .. attribute:: host
                        
                        	A single host address
                        	**type**\: list of    :py:class:`Host <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper.ObjectGroup.Network.Ipv4.Objects.Object.Hosts.Host>`
                        
                        

                        """

                        _prefix = 'infra-objmgr-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.host = YList()
                            self.host.parent = self
                            self.host.name = 'host'


                        class Host(object):
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
                                self.parent = None
                                self.host_address = None
                                self.host_address_xr = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.host_address is None:
                                    raise YPYModelError('Key property host_address is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-objmgr-oper:host[Cisco-IOS-XR-infra-objmgr-oper:host-address = ' + str(self.host_address) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.host_address is not None:
                                    return True

                                if self.host_address_xr is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_objmgr_oper as meta
                                return meta._meta_table['ObjectGroup.Network.Ipv4.Objects.Object.Hosts.Host']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-objmgr-oper:hosts'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.host is not None:
                                for child_ref in self.host:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_objmgr_oper as meta
                            return meta._meta_table['ObjectGroup.Network.Ipv4.Objects.Object.Hosts']['meta_info']

                    @property
                    def _common_path(self):
                        if self.object_name is None:
                            raise YPYModelError('Key property object_name is None')

                        return '/Cisco-IOS-XR-infra-objmgr-oper:object-group/Cisco-IOS-XR-infra-objmgr-oper:network/Cisco-IOS-XR-infra-objmgr-oper:ipv4/Cisco-IOS-XR-infra-objmgr-oper:objects/Cisco-IOS-XR-infra-objmgr-oper:object[Cisco-IOS-XR-infra-objmgr-oper:object-name = ' + str(self.object_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.object_name is not None:
                            return True

                        if self.address_ranges is not None and self.address_ranges._has_data():
                            return True

                        if self.addresses is not None and self.addresses._has_data():
                            return True

                        if self.hosts is not None and self.hosts._has_data():
                            return True

                        if self.nested_groups is not None and self.nested_groups._has_data():
                            return True

                        if self.parent_groups is not None and self.parent_groups._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_objmgr_oper as meta
                        return meta._meta_table['ObjectGroup.Network.Ipv4.Objects.Object']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-infra-objmgr-oper:object-group/Cisco-IOS-XR-infra-objmgr-oper:network/Cisco-IOS-XR-infra-objmgr-oper:ipv4/Cisco-IOS-XR-infra-objmgr-oper:objects'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.object is not None:
                        for child_ref in self.object:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_objmgr_oper as meta
                    return meta._meta_table['ObjectGroup.Network.Ipv4.Objects']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-infra-objmgr-oper:object-group/Cisco-IOS-XR-infra-objmgr-oper:network/Cisco-IOS-XR-infra-objmgr-oper:ipv4'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.objects is not None and self.objects._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_objmgr_oper as meta
                return meta._meta_table['ObjectGroup.Network.Ipv4']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-objmgr-oper:object-group/Cisco-IOS-XR-infra-objmgr-oper:network'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ipv4 is not None and self.ipv4._has_data():
                return True

            if self.ipv6 is not None and self.ipv6._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_objmgr_oper as meta
            return meta._meta_table['ObjectGroup.Network']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-infra-objmgr-oper:object-group'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.network is not None and self.network._has_data():
            return True

        if self.port is not None and self.port._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_objmgr_oper as meta
        return meta._meta_table['ObjectGroup']['meta_info']


