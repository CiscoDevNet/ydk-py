""" CISCO_FIREWALL_TC 

This MIB module defines textual conventions that
are commonly used in modeling management information 
pertaining to configuration, status and activity
of firewalls.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Cfwapplicationprotocol(Enum):
    """
    Cfwapplicationprotocol

    This type denotes the application (OSI Layer 7)

    protocol/service corresponding to a firewall session

    or a connection.

    Description of constants of this type

    'none'

        Denotes the semantics of 'not applicable'.

    'other'

        Denotes any protocol not listed.

    .. data:: none = 1

    .. data:: other = 2

    .. data:: ftp = 3

    .. data:: telnet = 4

    .. data:: smtp = 5

    .. data:: http = 6

    .. data:: tacacs = 7

    .. data:: dns = 8

    .. data:: sqlnet = 9

    .. data:: https = 10

    .. data:: tftp = 11

    .. data:: gopher = 12

    .. data:: finger = 13

    .. data:: kerberos = 14

    .. data:: pop2 = 15

    .. data:: pop3 = 16

    .. data:: sunRpc = 17

    .. data:: msRpc = 18

    .. data:: nntp = 19

    .. data:: snmp = 20

    .. data:: imap = 21

    .. data:: ldap = 22

    .. data:: exec_ = 23

    .. data:: login = 24

    .. data:: shell = 25

    .. data:: msSql = 26

    .. data:: sybaseSql = 27

    .. data:: nfs = 28

    .. data:: lotusnote = 29

    .. data:: h323 = 30

    .. data:: cuseeme = 31

    .. data:: realmedia = 32

    .. data:: netshow = 33

    .. data:: streamworks = 34

    .. data:: vdolive = 35

    .. data:: sap = 36

    .. data:: sip = 37

    .. data:: mgcp = 38

    .. data:: rtsp = 39

    .. data:: skinny = 40

    .. data:: gtpV0 = 41

    .. data:: gtpV1 = 42

    .. data:: echo = 43

    .. data:: discard = 44

    .. data:: daytime = 45

    .. data:: netstat = 46

    .. data:: ssh = 47

    .. data:: time = 48

    .. data:: tacacsDs = 49

    .. data:: bootps = 50

    .. data:: bootpc = 51

    .. data:: dnsix = 52

    .. data:: rtelnet = 53

    .. data:: ident = 54

    .. data:: sqlServ = 55

    .. data:: ntp = 56

    .. data:: pwdgen = 57

    .. data:: ciscoFna = 58

    .. data:: ciscoTna = 59

    .. data:: ciscoSys = 60

    .. data:: netbiosNs = 61

    .. data:: netbiosDgm = 62

    .. data:: netbiosSsn = 63

    .. data:: sqlSrv = 64

    .. data:: snmpTrap = 65

    .. data:: rsvd = 66

    .. data:: send = 67

    .. data:: xdmcp = 68

    .. data:: bgp = 69

    .. data:: irc = 70

    .. data:: qmtp = 71

    .. data:: ipx = 72

    .. data:: dbase = 73

    .. data:: imap3 = 74

    .. data:: rsvpTunnel = 75

    .. data:: hpCollector = 76

    .. data:: hpManagedNode = 77

    .. data:: hpAlarmMgr = 78

    .. data:: microsoftDs = 79

    .. data:: creativeServer = 80

    .. data:: creativePartnr = 81

    .. data:: appleQtc = 82

    .. data:: igmpV3Lite = 83

    .. data:: isakmp = 84

    .. data:: biff = 85

    .. data:: who = 86

    .. data:: syslog = 87

    .. data:: router = 88

    .. data:: ncp = 89

    .. data:: timed = 90

    .. data:: ircServ = 91

    .. data:: uucp = 92

    .. data:: syslogConn = 93

    .. data:: sshell = 94

    .. data:: ldaps = 95

    .. data:: dhcpFailover = 96

    .. data:: msexchRouting = 97

    .. data:: entrustSvcs = 98

    .. data:: entrustSvcHandler = 99

    .. data:: ciscoTdp = 100

    .. data:: webster = 101

    .. data:: gdoi = 102

    .. data:: iscsi = 103

    .. data:: cddbp = 104

    .. data:: ftps = 105

    .. data:: telnets = 106

    .. data:: imaps = 107

    .. data:: ircs = 108

    .. data:: pop3s = 109

    .. data:: socks = 110

    .. data:: kazaa = 111

    .. data:: msSqlM = 112

    .. data:: msSna = 113

    .. data:: wins = 114

    .. data:: ica = 115

    .. data:: orasrv = 116

    .. data:: rdbDbsDisp = 117

    .. data:: vqp = 118

    .. data:: icabrowser = 119

    .. data:: kermit = 120

    .. data:: rsvpEncap = 121

    .. data:: l2tp = 122

    .. data:: pptp = 123

    .. data:: h323Gatestat = 124

    .. data:: rWinsock = 125

    .. data:: radius = 126

    .. data:: hsrp = 127

    .. data:: net8Cman = 128

    .. data:: oracleEmVp = 129

    .. data:: oracleNames = 130

    .. data:: oracle = 131

    .. data:: ciscoSvcs = 132

    .. data:: ciscoNetMgmt = 133

    .. data:: stun = 134

    .. data:: trRsrb = 135

    .. data:: ddnsV3 = 136

    .. data:: aceSvr = 137

    .. data:: giop = 138

    .. data:: ttc = 139

    .. data:: ipass = 140

    .. data:: clp = 141

    .. data:: citrixImaClient = 142

    .. data:: sms = 143

    .. data:: citrix = 144

    .. data:: realSecure = 145

    .. data:: lotusMtap = 146

    .. data:: cifs = 147

    .. data:: msDotnetster = 148

    .. data:: tarantella = 149

    .. data:: fcipPort = 150

    .. data:: ssp = 151

    .. data:: iscsiTarget = 152

    .. data:: mySql = 153

    .. data:: msClusterNet = 154

    .. data:: ldapAdmin = 155

    .. data:: ieee80211Iapp = 156

    .. data:: oemAgent = 157

    .. data:: rtcPmPort = 158

    .. data:: dbControlAgent = 159

    .. data:: ipsecMsft = 160

    .. data:: sipTls = 161

    .. data:: aim = 162

    .. data:: pcAnyWhereData = 163

    .. data:: pcAnyWhereStat = 164

    .. data:: x11 = 165

    .. data:: ircu = 166

    .. data:: n2h2Server = 167

    .. data:: h323CallSigAlt = 168

    .. data:: yahooMsgr = 169

    .. data:: msnMsgr = 170

    """

    none = Enum.YLeaf(1, "none")

    other = Enum.YLeaf(2, "other")

    ftp = Enum.YLeaf(3, "ftp")

    telnet = Enum.YLeaf(4, "telnet")

    smtp = Enum.YLeaf(5, "smtp")

    http = Enum.YLeaf(6, "http")

    tacacs = Enum.YLeaf(7, "tacacs")

    dns = Enum.YLeaf(8, "dns")

    sqlnet = Enum.YLeaf(9, "sqlnet")

    https = Enum.YLeaf(10, "https")

    tftp = Enum.YLeaf(11, "tftp")

    gopher = Enum.YLeaf(12, "gopher")

    finger = Enum.YLeaf(13, "finger")

    kerberos = Enum.YLeaf(14, "kerberos")

    pop2 = Enum.YLeaf(15, "pop2")

    pop3 = Enum.YLeaf(16, "pop3")

    sunRpc = Enum.YLeaf(17, "sunRpc")

    msRpc = Enum.YLeaf(18, "msRpc")

    nntp = Enum.YLeaf(19, "nntp")

    snmp = Enum.YLeaf(20, "snmp")

    imap = Enum.YLeaf(21, "imap")

    ldap = Enum.YLeaf(22, "ldap")

    exec_ = Enum.YLeaf(23, "exec")

    login = Enum.YLeaf(24, "login")

    shell = Enum.YLeaf(25, "shell")

    msSql = Enum.YLeaf(26, "msSql")

    sybaseSql = Enum.YLeaf(27, "sybaseSql")

    nfs = Enum.YLeaf(28, "nfs")

    lotusnote = Enum.YLeaf(29, "lotusnote")

    h323 = Enum.YLeaf(30, "h323")

    cuseeme = Enum.YLeaf(31, "cuseeme")

    realmedia = Enum.YLeaf(32, "realmedia")

    netshow = Enum.YLeaf(33, "netshow")

    streamworks = Enum.YLeaf(34, "streamworks")

    vdolive = Enum.YLeaf(35, "vdolive")

    sap = Enum.YLeaf(36, "sap")

    sip = Enum.YLeaf(37, "sip")

    mgcp = Enum.YLeaf(38, "mgcp")

    rtsp = Enum.YLeaf(39, "rtsp")

    skinny = Enum.YLeaf(40, "skinny")

    gtpV0 = Enum.YLeaf(41, "gtpV0")

    gtpV1 = Enum.YLeaf(42, "gtpV1")

    echo = Enum.YLeaf(43, "echo")

    discard = Enum.YLeaf(44, "discard")

    daytime = Enum.YLeaf(45, "daytime")

    netstat = Enum.YLeaf(46, "netstat")

    ssh = Enum.YLeaf(47, "ssh")

    time = Enum.YLeaf(48, "time")

    tacacsDs = Enum.YLeaf(49, "tacacsDs")

    bootps = Enum.YLeaf(50, "bootps")

    bootpc = Enum.YLeaf(51, "bootpc")

    dnsix = Enum.YLeaf(52, "dnsix")

    rtelnet = Enum.YLeaf(53, "rtelnet")

    ident = Enum.YLeaf(54, "ident")

    sqlServ = Enum.YLeaf(55, "sqlServ")

    ntp = Enum.YLeaf(56, "ntp")

    pwdgen = Enum.YLeaf(57, "pwdgen")

    ciscoFna = Enum.YLeaf(58, "ciscoFna")

    ciscoTna = Enum.YLeaf(59, "ciscoTna")

    ciscoSys = Enum.YLeaf(60, "ciscoSys")

    netbiosNs = Enum.YLeaf(61, "netbiosNs")

    netbiosDgm = Enum.YLeaf(62, "netbiosDgm")

    netbiosSsn = Enum.YLeaf(63, "netbiosSsn")

    sqlSrv = Enum.YLeaf(64, "sqlSrv")

    snmpTrap = Enum.YLeaf(65, "snmpTrap")

    rsvd = Enum.YLeaf(66, "rsvd")

    send = Enum.YLeaf(67, "send")

    xdmcp = Enum.YLeaf(68, "xdmcp")

    bgp = Enum.YLeaf(69, "bgp")

    irc = Enum.YLeaf(70, "irc")

    qmtp = Enum.YLeaf(71, "qmtp")

    ipx = Enum.YLeaf(72, "ipx")

    dbase = Enum.YLeaf(73, "dbase")

    imap3 = Enum.YLeaf(74, "imap3")

    rsvpTunnel = Enum.YLeaf(75, "rsvpTunnel")

    hpCollector = Enum.YLeaf(76, "hpCollector")

    hpManagedNode = Enum.YLeaf(77, "hpManagedNode")

    hpAlarmMgr = Enum.YLeaf(78, "hpAlarmMgr")

    microsoftDs = Enum.YLeaf(79, "microsoftDs")

    creativeServer = Enum.YLeaf(80, "creativeServer")

    creativePartnr = Enum.YLeaf(81, "creativePartnr")

    appleQtc = Enum.YLeaf(82, "appleQtc")

    igmpV3Lite = Enum.YLeaf(83, "igmpV3Lite")

    isakmp = Enum.YLeaf(84, "isakmp")

    biff = Enum.YLeaf(85, "biff")

    who = Enum.YLeaf(86, "who")

    syslog = Enum.YLeaf(87, "syslog")

    router = Enum.YLeaf(88, "router")

    ncp = Enum.YLeaf(89, "ncp")

    timed = Enum.YLeaf(90, "timed")

    ircServ = Enum.YLeaf(91, "ircServ")

    uucp = Enum.YLeaf(92, "uucp")

    syslogConn = Enum.YLeaf(93, "syslogConn")

    sshell = Enum.YLeaf(94, "sshell")

    ldaps = Enum.YLeaf(95, "ldaps")

    dhcpFailover = Enum.YLeaf(96, "dhcpFailover")

    msexchRouting = Enum.YLeaf(97, "msexchRouting")

    entrustSvcs = Enum.YLeaf(98, "entrustSvcs")

    entrustSvcHandler = Enum.YLeaf(99, "entrustSvcHandler")

    ciscoTdp = Enum.YLeaf(100, "ciscoTdp")

    webster = Enum.YLeaf(101, "webster")

    gdoi = Enum.YLeaf(102, "gdoi")

    iscsi = Enum.YLeaf(103, "iscsi")

    cddbp = Enum.YLeaf(104, "cddbp")

    ftps = Enum.YLeaf(105, "ftps")

    telnets = Enum.YLeaf(106, "telnets")

    imaps = Enum.YLeaf(107, "imaps")

    ircs = Enum.YLeaf(108, "ircs")

    pop3s = Enum.YLeaf(109, "pop3s")

    socks = Enum.YLeaf(110, "socks")

    kazaa = Enum.YLeaf(111, "kazaa")

    msSqlM = Enum.YLeaf(112, "msSqlM")

    msSna = Enum.YLeaf(113, "msSna")

    wins = Enum.YLeaf(114, "wins")

    ica = Enum.YLeaf(115, "ica")

    orasrv = Enum.YLeaf(116, "orasrv")

    rdbDbsDisp = Enum.YLeaf(117, "rdbDbsDisp")

    vqp = Enum.YLeaf(118, "vqp")

    icabrowser = Enum.YLeaf(119, "icabrowser")

    kermit = Enum.YLeaf(120, "kermit")

    rsvpEncap = Enum.YLeaf(121, "rsvpEncap")

    l2tp = Enum.YLeaf(122, "l2tp")

    pptp = Enum.YLeaf(123, "pptp")

    h323Gatestat = Enum.YLeaf(124, "h323Gatestat")

    rWinsock = Enum.YLeaf(125, "rWinsock")

    radius = Enum.YLeaf(126, "radius")

    hsrp = Enum.YLeaf(127, "hsrp")

    net8Cman = Enum.YLeaf(128, "net8Cman")

    oracleEmVp = Enum.YLeaf(129, "oracleEmVp")

    oracleNames = Enum.YLeaf(130, "oracleNames")

    oracle = Enum.YLeaf(131, "oracle")

    ciscoSvcs = Enum.YLeaf(132, "ciscoSvcs")

    ciscoNetMgmt = Enum.YLeaf(133, "ciscoNetMgmt")

    stun = Enum.YLeaf(134, "stun")

    trRsrb = Enum.YLeaf(135, "trRsrb")

    ddnsV3 = Enum.YLeaf(136, "ddnsV3")

    aceSvr = Enum.YLeaf(137, "aceSvr")

    giop = Enum.YLeaf(138, "giop")

    ttc = Enum.YLeaf(139, "ttc")

    ipass = Enum.YLeaf(140, "ipass")

    clp = Enum.YLeaf(141, "clp")

    citrixImaClient = Enum.YLeaf(142, "citrixImaClient")

    sms = Enum.YLeaf(143, "sms")

    citrix = Enum.YLeaf(144, "citrix")

    realSecure = Enum.YLeaf(145, "realSecure")

    lotusMtap = Enum.YLeaf(146, "lotusMtap")

    cifs = Enum.YLeaf(147, "cifs")

    msDotnetster = Enum.YLeaf(148, "msDotnetster")

    tarantella = Enum.YLeaf(149, "tarantella")

    fcipPort = Enum.YLeaf(150, "fcipPort")

    ssp = Enum.YLeaf(151, "ssp")

    iscsiTarget = Enum.YLeaf(152, "iscsiTarget")

    mySql = Enum.YLeaf(153, "mySql")

    msClusterNet = Enum.YLeaf(154, "msClusterNet")

    ldapAdmin = Enum.YLeaf(155, "ldapAdmin")

    ieee80211Iapp = Enum.YLeaf(156, "ieee80211Iapp")

    oemAgent = Enum.YLeaf(157, "oemAgent")

    rtcPmPort = Enum.YLeaf(158, "rtcPmPort")

    dbControlAgent = Enum.YLeaf(159, "dbControlAgent")

    ipsecMsft = Enum.YLeaf(160, "ipsecMsft")

    sipTls = Enum.YLeaf(161, "sipTls")

    aim = Enum.YLeaf(162, "aim")

    pcAnyWhereData = Enum.YLeaf(163, "pcAnyWhereData")

    pcAnyWhereStat = Enum.YLeaf(164, "pcAnyWhereStat")

    x11 = Enum.YLeaf(165, "x11")

    ircu = Enum.YLeaf(166, "ircu")

    n2h2Server = Enum.YLeaf(167, "n2h2Server")

    h323CallSigAlt = Enum.YLeaf(168, "h323CallSigAlt")

    yahooMsgr = Enum.YLeaf(169, "yahooMsgr")

    msnMsgr = Enum.YLeaf(170, "msnMsgr")


class Cfwnetworkprotocol(Enum):
    """
    Cfwnetworkprotocol

    This type denotes protocols operating at 

    layers 3 or 4 of Open System Interconnection (OSI)

    model.

    The following values are defined\:

    'none'

        Denotes the semantics of 'not applicable'.

    'other'

        Denotes any protocol not listed.

    'ip'

        Denotes Internet Protocol (IP).

    'icmp'

        Denotes Internet Control Message

        Protocol.

    'gre'

        Denotes Generic Route Encapsulation

        protocol.

    'udp'

        Denotes User Datagram Protocol.

    'tcp'

        Denotes Transmission Control Protocol.

    .. data:: none = 1

    .. data:: other = 2

    .. data:: ip = 3

    .. data:: icmp = 4

    .. data:: gre = 5

    .. data:: udp = 6

    .. data:: tcp = 7

    """

    none = Enum.YLeaf(1, "none")

    other = Enum.YLeaf(2, "other")

    ip = Enum.YLeaf(3, "ip")

    icmp = Enum.YLeaf(4, "icmp")

    gre = Enum.YLeaf(5, "gre")

    udp = Enum.YLeaf(6, "udp")

    tcp = Enum.YLeaf(7, "tcp")


class Cfwpolicytargettype(Enum):
    """
    Cfwpolicytargettype

    This type is used to represent the type of 

    a policy target.

    The following values are defined\:

    'all'

        Certain firewall implementations allow policies

        to be applied on all applicable targets. (Such

        policies are termed 'global'). The target type

        'all' denotes the set of all applicable

        targets.

    'other'

        Denotes an entity type that has yet not been

        classified in one of the other types. This

        value is useful in accomodating new target types

        before the textual convention is revised to 

        include them.

    'interface'

        The policy target is an interface of the managed 

        device.

    'zone'

        The policy target is a zone, where a zone is

        is a collection of interfaces of the managed 

        device.

    'zonepair'

        The policy target is a pair of zones.

    'user'

        Denotes the identity of a user who is 

        authorized to access the firewall itself or 

        the resources protected by the firewall.

    'usergroup'

        Denotes the identity of a user group.

        User group denotes a collection of user

        identities, as defined above.

    'context'

        Denotes a logical device defined in the managed

        device with a distinct management context. 

        Examples of such logical devices include

        virtual contexts defined by Firewall Service

        Module, virtual sensors defined by Intrusion

        Detection Service Module and Virtual Routing

        and Forwarding (VRFs) defined by IOS.

    .. data:: all = 1

    .. data:: other = 2

    .. data:: interface = 3

    .. data:: zone = 4

    .. data:: zonepair = 5

    .. data:: user = 6

    .. data:: usergroup = 7

    .. data:: context = 8

    """

    all = Enum.YLeaf(1, "all")

    other = Enum.YLeaf(2, "other")

    interface = Enum.YLeaf(3, "interface")

    zone = Enum.YLeaf(4, "zone")

    zonepair = Enum.YLeaf(5, "zonepair")

    user = Enum.YLeaf(6, "user")

    usergroup = Enum.YLeaf(7, "usergroup")

    context = Enum.YLeaf(8, "context")


class Cfwurlfvendorid(Enum):
    """
    Cfwurlfvendorid

    This type denotes the vendor of a URL filtering

    server which the firewall uses to implement URL

    filtering. 

    A URL filtering server provides a database of URLs

    with appropriate access restrictions (e.g., 

    deny or permit). Various security devices can make

    use of these filtering servers to provide URL filtering

    functionality to the users.

    The following values are defined\:

    'other' 

        Other type of URL filtering servers than those

        specified below.

    'websense'

        Websense URL filtering server. One of the products

        provided by Websense is a Web Filtering Server. 

        More information about Websense Web Filtering

        product can be found at http\://www.websense.com

    'n2h2'

        N2H2 URL filtering server. More information about

        N2H2 Filtering product can be found at

        http\://www.n2h2.com

    .. data:: other = 1

    .. data:: websense = 2

    .. data:: n2h2 = 3

    """

    other = Enum.YLeaf(1, "other")

    websense = Enum.YLeaf(2, "websense")

    n2h2 = Enum.YLeaf(3, "n2h2")


class Cfwurlserverstatus(Enum):
    """
    Cfwurlserverstatus

    This type denotes the status of the URL filtering 

    server which the firewall uses to implement URL

    filtering.

    The following values are defined\:

    'online' 

        Indicates that the Server is online

    'offline'

        Indicates that the Server is offline

    'indeterminate'

        Indicates that the Server status 

        cannot be determined

    .. data:: online = 1

    .. data:: offline = 2

    .. data:: indeterminate = 3

    """

    online = Enum.YLeaf(1, "online")

    offline = Enum.YLeaf(2, "offline")

    indeterminate = Enum.YLeaf(3, "indeterminate")



