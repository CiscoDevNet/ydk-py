""" ietf_syslog_types 

This module contains a collection of YANG type definitions for 
SYSLOG.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Severity(Enum):
    """
    Severity

    The definitions for Syslog message severity as per RFC 5424.

    .. data:: emergency = 0

    	Emergency Level Msg

    .. data:: alert = 1

    	Alert Level Msg

    .. data:: critical = 2

    	Critical Level Msg

    .. data:: error = 3

    	Error Level Msg

    .. data:: warning = 4

    	Warning Level Msg

    .. data:: notice = 5

    	Notification Level Msg

    .. data:: info = 6

    	Informational Level Msg

    .. data:: debug = 7

    	Debugging Level Msg

    """

    emergency = Enum.YLeaf(0, "emergency")

    alert = Enum.YLeaf(1, "alert")

    critical = Enum.YLeaf(2, "critical")

    error = Enum.YLeaf(3, "error")

    warning = Enum.YLeaf(4, "warning")

    notice = Enum.YLeaf(5, "notice")

    info = Enum.YLeaf(6, "info")

    debug = Enum.YLeaf(7, "debug")



class SyslogFacility(Identity):
    """
    The base identity to represent syslog facilities
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self):
        super(SyslogFacility, self).__init__("urn:ietf:params:xml:ns:yang:ietf-syslog-types", "ietf-syslog-types", "ietf-syslog-types:syslog-facility")


class Ftp(Identity):
    """
    The facility for the FTP daemon as defined in RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self):
        super(Ftp, self).__init__("urn:ietf:params:xml:ns:yang:ietf-syslog-types", "ietf-syslog-types", "ietf-syslog-types:ftp")


class Auth(Identity):
    """
    The facility for security/authorization messages as defined 
    in RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self):
        super(Auth, self).__init__("urn:ietf:params:xml:ns:yang:ietf-syslog-types", "ietf-syslog-types", "ietf-syslog-types:auth")


class User(Identity):
    """
    The facility for user\-level messages as defined in RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self):
        super(User, self).__init__("urn:ietf:params:xml:ns:yang:ietf-syslog-types", "ietf-syslog-types", "ietf-syslog-types:user")


class Local5(Identity):
    """
    The facility for local use 5 messages as defined in 
    RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self):
        super(Local5, self).__init__("urn:ietf:params:xml:ns:yang:ietf-syslog-types", "ietf-syslog-types", "ietf-syslog-types:local5")


class Local0(Identity):
    """
    The facility for local use 0 messages as defined in 
    RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self):
        super(Local0, self).__init__("urn:ietf:params:xml:ns:yang:ietf-syslog-types", "ietf-syslog-types", "ietf-syslog-types:local0")


class Console(Identity):
    """
    The facility for log alert messages as defined in RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self):
        super(Console, self).__init__("urn:ietf:params:xml:ns:yang:ietf-syslog-types", "ietf-syslog-types", "ietf-syslog-types:console")


class Local3(Identity):
    """
    The facility for local use 3 messages as defined in 
    RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self):
        super(Local3, self).__init__("urn:ietf:params:xml:ns:yang:ietf-syslog-types", "ietf-syslog-types", "ietf-syslog-types:local3")


class Lpr(Identity):
    """
    The facility for the line printer subsystem as defined in 
    RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self):
        super(Lpr, self).__init__("urn:ietf:params:xml:ns:yang:ietf-syslog-types", "ietf-syslog-types", "ietf-syslog-types:lpr")


class Syslog(Identity):
    """
    The facility for messages generated internally by syslogd 
    facility as defined in RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self):
        super(Syslog, self).__init__("urn:ietf:params:xml:ns:yang:ietf-syslog-types", "ietf-syslog-types", "ietf-syslog-types:syslog")


class Local4(Identity):
    """
    The facility for local use 4 messages as defined in 
    RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self):
        super(Local4, self).__init__("urn:ietf:params:xml:ns:yang:ietf-syslog-types", "ietf-syslog-types", "ietf-syslog-types:local4")


class Cron(Identity):
    """
    The facility for the clock daemon as defined in RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self):
        super(Cron, self).__init__("urn:ietf:params:xml:ns:yang:ietf-syslog-types", "ietf-syslog-types", "ietf-syslog-types:cron")


class Kern(Identity):
    """
    The facility for kernel messages as defined in RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self):
        super(Kern, self).__init__("urn:ietf:params:xml:ns:yang:ietf-syslog-types", "ietf-syslog-types", "ietf-syslog-types:kern")


class Daemon(Identity):
    """
    The facility for the system daemons as defined in RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self):
        super(Daemon, self).__init__("urn:ietf:params:xml:ns:yang:ietf-syslog-types", "ietf-syslog-types", "ietf-syslog-types:daemon")


class Mail(Identity):
    """
    The facility for the mail system as defined in RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self):
        super(Mail, self).__init__("urn:ietf:params:xml:ns:yang:ietf-syslog-types", "ietf-syslog-types", "ietf-syslog-types:mail")


class Local2(Identity):
    """
    The facility for local use 2 messages as defined in 
    RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self):
        super(Local2, self).__init__("urn:ietf:params:xml:ns:yang:ietf-syslog-types", "ietf-syslog-types", "ietf-syslog-types:local2")


class News(Identity):
    """
    The facility for the network news subsystem as defined in 
    RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self):
        super(News, self).__init__("urn:ietf:params:xml:ns:yang:ietf-syslog-types", "ietf-syslog-types", "ietf-syslog-types:news")


class Local7(Identity):
    """
    The facility for local use 7 messages as defined in 
    RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self):
        super(Local7, self).__init__("urn:ietf:params:xml:ns:yang:ietf-syslog-types", "ietf-syslog-types", "ietf-syslog-types:local7")


class Local1(Identity):
    """
    The facility for local use 1 messages as defined in 
    RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self):
        super(Local1, self).__init__("urn:ietf:params:xml:ns:yang:ietf-syslog-types", "ietf-syslog-types", "ietf-syslog-types:local1")


class Cron2(Identity):
    """
    The facility for the second clock daemon as defined in 
    RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self):
        super(Cron2, self).__init__("urn:ietf:params:xml:ns:yang:ietf-syslog-types", "ietf-syslog-types", "ietf-syslog-types:cron2")


class Authpriv(Identity):
    """
    The facility for privileged security/authorization messages 
    as defined in RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self):
        super(Authpriv, self).__init__("urn:ietf:params:xml:ns:yang:ietf-syslog-types", "ietf-syslog-types", "ietf-syslog-types:authpriv")


class Uucp(Identity):
    """
    The facility for the UUCP subsystem as defined in RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self):
        super(Uucp, self).__init__("urn:ietf:params:xml:ns:yang:ietf-syslog-types", "ietf-syslog-types", "ietf-syslog-types:uucp")


class Local6(Identity):
    """
    The facility for local use 6 messages as defined in 
    RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self):
        super(Local6, self).__init__("urn:ietf:params:xml:ns:yang:ietf-syslog-types", "ietf-syslog-types", "ietf-syslog-types:local6")


class Ntp(Identity):
    """
    The facility for the NTP subsystem as defined in RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self):
        super(Ntp, self).__init__("urn:ietf:params:xml:ns:yang:ietf-syslog-types", "ietf-syslog-types", "ietf-syslog-types:ntp")


class Audit(Identity):
    """
    The facility for log audit messages as defined in RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self):
        super(Audit, self).__init__("urn:ietf:params:xml:ns:yang:ietf-syslog-types", "ietf-syslog-types", "ietf-syslog-types:audit")


