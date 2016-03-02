""" CISCO_FIREWALL_TC 

This MIB module defines textual conventions that
are commonly used in modeling management information 
pertaining to configuration, status and activity
of firewalls.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class CFWApplicationProtocol_Enum(Enum):
    """
    CFWApplicationProtocol_Enum

    This type denotes the application (OSI Layer 7)
    protocol/service corresponding to a firewall session
    or a connection.
    
    Description of constants of this type
    
    'none'
        Denotes the semantics of 'not applicable'.
    
    'other'
        Denotes any protocol not listed.

    """

    NONE = 1

    OTHER = 2

    FTP = 3

    TELNET = 4

    SMTP = 5

    HTTP = 6

    TACACS = 7

    DNS = 8

    SQLNET = 9

    HTTPS = 10

    TFTP = 11

    GOPHER = 12

    FINGER = 13

    KERBEROS = 14

    POP2 = 15

    POP3 = 16

    SUNRPC = 17

    MSRPC = 18

    NNTP = 19

    SNMP = 20

    IMAP = 21

    LDAP = 22

    EXEC = 23

    LOGIN = 24

    SHELL = 25

    MSSQL = 26

    SYBASESQL = 27

    NFS = 28

    LOTUSNOTE = 29

    H323 = 30

    CUSEEME = 31

    REALMEDIA = 32

    NETSHOW = 33

    STREAMWORKS = 34

    VDOLIVE = 35

    SAP = 36

    SIP = 37

    MGCP = 38

    RTSP = 39

    SKINNY = 40

    GTPV0 = 41

    GTPV1 = 42

    ECHO = 43

    DISCARD = 44

    DAYTIME = 45

    NETSTAT = 46

    SSH = 47

    TIME = 48

    TACACSDS = 49

    BOOTPS = 50

    BOOTPC = 51

    DNSIX = 52

    RTELNET = 53

    IDENT = 54

    SQLSERV = 55

    NTP = 56

    PWDGEN = 57

    CISCOFNA = 58

    CISCOTNA = 59

    CISCOSYS = 60

    NETBIOSNS = 61

    NETBIOSDGM = 62

    NETBIOSSSN = 63

    SQLSRV = 64

    SNMPTRAP = 65

    RSVD = 66

    SEND = 67

    XDMCP = 68

    BGP = 69

    IRC = 70

    QMTP = 71

    IPX = 72

    DBASE = 73

    IMAP3 = 74

    RSVPTUNNEL = 75

    HPCOLLECTOR = 76

    HPMANAGEDNODE = 77

    HPALARMMGR = 78

    MICROSOFTDS = 79

    CREATIVESERVER = 80

    CREATIVEPARTNR = 81

    APPLEQTC = 82

    IGMPV3LITE = 83

    ISAKMP = 84

    BIFF = 85

    WHO = 86

    SYSLOG = 87

    ROUTER = 88

    NCP = 89

    TIMED = 90

    IRCSERV = 91

    UUCP = 92

    SYSLOGCONN = 93

    SSHELL = 94

    LDAPS = 95

    DHCPFAILOVER = 96

    MSEXCHROUTING = 97

    ENTRUSTSVCS = 98

    ENTRUSTSVCHANDLER = 99

    CISCOTDP = 100

    WEBSTER = 101

    GDOI = 102

    ISCSI = 103

    CDDBP = 104

    FTPS = 105

    TELNETS = 106

    IMAPS = 107

    IRCS = 108

    POP3S = 109

    SOCKS = 110

    KAZAA = 111

    MSSQLM = 112

    MSSNA = 113

    WINS = 114

    ICA = 115

    ORASRV = 116

    RDBDBSDISP = 117

    VQP = 118

    ICABROWSER = 119

    KERMIT = 120

    RSVPENCAP = 121

    L2TP = 122

    PPTP = 123

    H323GATESTAT = 124

    RWINSOCK = 125

    RADIUS = 126

    HSRP = 127

    NET8CMAN = 128

    ORACLEEMVP = 129

    ORACLENAMES = 130

    ORACLE = 131

    CISCOSVCS = 132

    CISCONETMGMT = 133

    STUN = 134

    TRRSRB = 135

    DDNSV3 = 136

    ACESVR = 137

    GIOP = 138

    TTC = 139

    IPASS = 140

    CLP = 141

    CITRIXIMACLIENT = 142

    SMS = 143

    CITRIX = 144

    REALSECURE = 145

    LOTUSMTAP = 146

    CIFS = 147

    MSDOTNETSTER = 148

    TARANTELLA = 149

    FCIPPORT = 150

    SSP = 151

    ISCSITARGET = 152

    MYSQL = 153

    MSCLUSTERNET = 154

    LDAPADMIN = 155

    IEEE80211IAPP = 156

    OEMAGENT = 157

    RTCPMPORT = 158

    DBCONTROLAGENT = 159

    IPSECMSFT = 160

    SIPTLS = 161

    AIM = 162

    PCANYWHEREDATA = 163

    PCANYWHERESTAT = 164

    X11 = 165

    IRCU = 166

    N2H2SERVER = 167

    H323CALLSIGALT = 168

    YAHOOMSGR = 169

    MSNMSGR = 170


    @staticmethod
    def _meta_info():
        from ydk.models.firewall._meta import _CISCO_FIREWALL_TC as meta
        return meta._meta_table['CFWApplicationProtocol_Enum']


class CFWNetworkProtocol_Enum(Enum):
    """
    CFWNetworkProtocol_Enum

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

    """

    NONE = 1

    OTHER = 2

    IP = 3

    ICMP = 4

    GRE = 5

    UDP = 6

    TCP = 7


    @staticmethod
    def _meta_info():
        from ydk.models.firewall._meta import _CISCO_FIREWALL_TC as meta
        return meta._meta_table['CFWNetworkProtocol_Enum']


class CFWPolicyTargetType_Enum(Enum):
    """
    CFWPolicyTargetType_Enum

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

    """

    ALL = 1

    OTHER = 2

    INTERFACE = 3

    ZONE = 4

    ZONEPAIR = 5

    USER = 6

    USERGROUP = 7

    CONTEXT = 8


    @staticmethod
    def _meta_info():
        from ydk.models.firewall._meta import _CISCO_FIREWALL_TC as meta
        return meta._meta_table['CFWPolicyTargetType_Enum']


class CFWUrlServerStatus_Enum(Enum):
    """
    CFWUrlServerStatus_Enum

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

    """

    ONLINE = 1

    OFFLINE = 2

    INDETERMINATE = 3


    @staticmethod
    def _meta_info():
        from ydk.models.firewall._meta import _CISCO_FIREWALL_TC as meta
        return meta._meta_table['CFWUrlServerStatus_Enum']


class CFWUrlfVendorId_Enum(Enum):
    """
    CFWUrlfVendorId_Enum

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

    """

    OTHER = 1

    WEBSENSE = 2

    N2H2 = 3


    @staticmethod
    def _meta_info():
        from ydk.models.firewall._meta import _CISCO_FIREWALL_TC as meta
        return meta._meta_table['CFWUrlfVendorId_Enum']



