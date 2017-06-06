""" CISCO_FIREWALL_TC 

This MIB module defines textual conventions that
are commonly used in modeling management information 
pertaining to configuration, status and activity
of firewalls.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class CfwapplicationprotocolEnum(Enum):
    """
    CfwapplicationprotocolEnum

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

    none = 1

    other = 2

    ftp = 3

    telnet = 4

    smtp = 5

    http = 6

    tacacs = 7

    dns = 8

    sqlnet = 9

    https = 10

    tftp = 11

    gopher = 12

    finger = 13

    kerberos = 14

    pop2 = 15

    pop3 = 16

    sunRpc = 17

    msRpc = 18

    nntp = 19

    snmp = 20

    imap = 21

    ldap = 22

    exec_ = 23

    login = 24

    shell = 25

    msSql = 26

    sybaseSql = 27

    nfs = 28

    lotusnote = 29

    h323 = 30

    cuseeme = 31

    realmedia = 32

    netshow = 33

    streamworks = 34

    vdolive = 35

    sap = 36

    sip = 37

    mgcp = 38

    rtsp = 39

    skinny = 40

    gtpV0 = 41

    gtpV1 = 42

    echo = 43

    discard = 44

    daytime = 45

    netstat = 46

    ssh = 47

    time = 48

    tacacsDs = 49

    bootps = 50

    bootpc = 51

    dnsix = 52

    rtelnet = 53

    ident = 54

    sqlServ = 55

    ntp = 56

    pwdgen = 57

    ciscoFna = 58

    ciscoTna = 59

    ciscoSys = 60

    netbiosNs = 61

    netbiosDgm = 62

    netbiosSsn = 63

    sqlSrv = 64

    snmpTrap = 65

    rsvd = 66

    send = 67

    xdmcp = 68

    bgp = 69

    irc = 70

    qmtp = 71

    ipx = 72

    dbase = 73

    imap3 = 74

    rsvpTunnel = 75

    hpCollector = 76

    hpManagedNode = 77

    hpAlarmMgr = 78

    microsoftDs = 79

    creativeServer = 80

    creativePartnr = 81

    appleQtc = 82

    igmpV3Lite = 83

    isakmp = 84

    biff = 85

    who = 86

    syslog = 87

    router = 88

    ncp = 89

    timed = 90

    ircServ = 91

    uucp = 92

    syslogConn = 93

    sshell = 94

    ldaps = 95

    dhcpFailover = 96

    msexchRouting = 97

    entrustSvcs = 98

    entrustSvcHandler = 99

    ciscoTdp = 100

    webster = 101

    gdoi = 102

    iscsi = 103

    cddbp = 104

    ftps = 105

    telnets = 106

    imaps = 107

    ircs = 108

    pop3s = 109

    socks = 110

    kazaa = 111

    msSqlM = 112

    msSna = 113

    wins = 114

    ica = 115

    orasrv = 116

    rdbDbsDisp = 117

    vqp = 118

    icabrowser = 119

    kermit = 120

    rsvpEncap = 121

    l2tp = 122

    pptp = 123

    h323Gatestat = 124

    rWinsock = 125

    radius = 126

    hsrp = 127

    net8Cman = 128

    oracleEmVp = 129

    oracleNames = 130

    oracle = 131

    ciscoSvcs = 132

    ciscoNetMgmt = 133

    stun = 134

    trRsrb = 135

    ddnsV3 = 136

    aceSvr = 137

    giop = 138

    ttc = 139

    ipass = 140

    clp = 141

    citrixImaClient = 142

    sms = 143

    citrix = 144

    realSecure = 145

    lotusMtap = 146

    cifs = 147

    msDotnetster = 148

    tarantella = 149

    fcipPort = 150

    ssp = 151

    iscsiTarget = 152

    mySql = 153

    msClusterNet = 154

    ldapAdmin = 155

    ieee80211Iapp = 156

    oemAgent = 157

    rtcPmPort = 158

    dbControlAgent = 159

    ipsecMsft = 160

    sipTls = 161

    aim = 162

    pcAnyWhereData = 163

    pcAnyWhereStat = 164

    x11 = 165

    ircu = 166

    n2h2Server = 167

    h323CallSigAlt = 168

    yahooMsgr = 169

    msnMsgr = 170


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_FIREWALL_TC as meta
        return meta._meta_table['CfwapplicationprotocolEnum']


class CfwnetworkprotocolEnum(Enum):
    """
    CfwnetworkprotocolEnum

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

    none = 1

    other = 2

    ip = 3

    icmp = 4

    gre = 5

    udp = 6

    tcp = 7


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_FIREWALL_TC as meta
        return meta._meta_table['CfwnetworkprotocolEnum']


class CfwpolicytargettypeEnum(Enum):
    """
    CfwpolicytargettypeEnum

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

    all = 1

    other = 2

    interface = 3

    zone = 4

    zonepair = 5

    user = 6

    usergroup = 7

    context = 8


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_FIREWALL_TC as meta
        return meta._meta_table['CfwpolicytargettypeEnum']


class CfwurlfvendoridEnum(Enum):
    """
    CfwurlfvendoridEnum

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

    other = 1

    websense = 2

    n2h2 = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_FIREWALL_TC as meta
        return meta._meta_table['CfwurlfvendoridEnum']


class CfwurlserverstatusEnum(Enum):
    """
    CfwurlserverstatusEnum

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

    online = 1

    offline = 2

    indeterminate = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_FIREWALL_TC as meta
        return meta._meta_table['CfwurlserverstatusEnum']



