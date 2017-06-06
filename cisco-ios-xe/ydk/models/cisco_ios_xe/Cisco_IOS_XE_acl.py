""" Cisco_IOS_XE_acl 

Cisco XE Native Access Control List (ACL) Yang model.
Copyright (c) 2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class AclPortTypeEnum(Enum):
    """
    AclPortTypeEnum

    .. data:: biff = 0

    .. data:: bootpc = 1

    .. data:: bootps = 2

    .. data:: discard = 3

    .. data:: dnsix = 4

    .. data:: domain = 5

    .. data:: echo = 6

    .. data:: isakmp = 7

    .. data:: mobile_ip = 8

    .. data:: nameserver = 9

    .. data:: netbios_dgm = 10

    .. data:: netbios_ns = 11

    .. data:: netbios_ss = 12

    .. data:: non500_isakmp = 13

    .. data:: ntp = 14

    .. data:: pim_auto_rp = 15

    .. data:: rip = 16

    .. data:: ripv6 = 17

    .. data:: snmp = 18

    .. data:: snmptrap = 19

    .. data:: sunrpc = 20

    .. data:: syslog = 21

    .. data:: tacacs = 22

    .. data:: talk = 23

    .. data:: tftp = 24

    .. data:: time = 25

    .. data:: who = 26

    .. data:: xdmcp = 27

    .. data:: bgp = 28

    .. data:: chargen = 29

    .. data:: cmd = 30

    .. data:: connectedapps_plain = 31

    .. data:: connectedapps_tls = 32

    .. data:: daytime = 33

    .. data:: exec_ = 34

    .. data:: finger = 35

    .. data:: ftp = 36

    .. data:: ftp_data = 37

    .. data:: gopher = 38

    .. data:: hostname = 39

    .. data:: ident = 40

    .. data:: irc = 41

    .. data:: klogin = 42

    .. data:: kshell = 43

    .. data:: login = 44

    .. data:: lpd = 45

    .. data:: msrpc = 46

    .. data:: nntp = 47

    .. data:: pop2 = 48

    .. data:: pop3 = 49

    .. data:: smtp = 50

    .. data:: telnet = 51

    .. data:: uucp = 52

    .. data:: whois = 53

    .. data:: www = 54

    """

    biff = 0

    bootpc = 1

    bootps = 2

    discard = 3

    dnsix = 4

    domain = 5

    echo = 6

    isakmp = 7

    mobile_ip = 8

    nameserver = 9

    netbios_dgm = 10

    netbios_ns = 11

    netbios_ss = 12

    non500_isakmp = 13

    ntp = 14

    pim_auto_rp = 15

    rip = 16

    ripv6 = 17

    snmp = 18

    snmptrap = 19

    sunrpc = 20

    syslog = 21

    tacacs = 22

    talk = 23

    tftp = 24

    time = 25

    who = 26

    xdmcp = 27

    bgp = 28

    chargen = 29

    cmd = 30

    connectedapps_plain = 31

    connectedapps_tls = 32

    daytime = 33

    exec_ = 34

    finger = 35

    ftp = 36

    ftp_data = 37

    gopher = 38

    hostname = 39

    ident = 40

    irc = 41

    klogin = 42

    kshell = 43

    login = 44

    lpd = 45

    msrpc = 46

    nntp = 47

    pop2 = 48

    pop3 = 49

    smtp = 50

    telnet = 51

    uucp = 52

    whois = 53

    www = 54


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_acl as meta
        return meta._meta_table['AclPortTypeEnum']



