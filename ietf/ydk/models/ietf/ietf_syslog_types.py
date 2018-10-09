""" ietf_syslog_types 

This module contains a collection of YANG type definitions for 
SYSLOG.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Severity(Enum):
    """
    Severity (Enum Class)

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

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:ietf-syslog-types", pref="ietf-syslog-types", tag="ietf-syslog-types:syslog-facility"):
        super(SyslogFacility, self).__init__(ns, pref, tag)


class Cron2(SyslogFacility):
    """
    The facility for the second clock daemon as defined in 
    RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:ietf-syslog-types", pref="ietf-syslog-types", tag="ietf-syslog-types:cron2"):
        super(Cron2, self).__init__(ns, pref, tag)


class Cron(SyslogFacility):
    """
    The facility for the clock daemon as defined in RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:ietf-syslog-types", pref="ietf-syslog-types", tag="ietf-syslog-types:cron"):
        super(Cron, self).__init__(ns, pref, tag)


class Syslog(SyslogFacility):
    """
    The facility for messages generated internally by syslogd 
    facility as defined in RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:ietf-syslog-types", pref="ietf-syslog-types", tag="ietf-syslog-types:syslog"):
        super(Syslog, self).__init__(ns, pref, tag)


class Local4(SyslogFacility):
    """
    The facility for local use 4 messages as defined in 
    RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:ietf-syslog-types", pref="ietf-syslog-types", tag="ietf-syslog-types:local4"):
        super(Local4, self).__init__(ns, pref, tag)


class Ftp(SyslogFacility):
    """
    The facility for the FTP daemon as defined in RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:ietf-syslog-types", pref="ietf-syslog-types", tag="ietf-syslog-types:ftp"):
        super(Ftp, self).__init__(ns, pref, tag)


class Uucp(SyslogFacility):
    """
    The facility for the UUCP subsystem as defined in RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:ietf-syslog-types", pref="ietf-syslog-types", tag="ietf-syslog-types:uucp"):
        super(Uucp, self).__init__(ns, pref, tag)


class Console(SyslogFacility):
    """
    The facility for log alert messages as defined in RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:ietf-syslog-types", pref="ietf-syslog-types", tag="ietf-syslog-types:console"):
        super(Console, self).__init__(ns, pref, tag)


class Mail(SyslogFacility):
    """
    The facility for the mail system as defined in RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:ietf-syslog-types", pref="ietf-syslog-types", tag="ietf-syslog-types:mail"):
        super(Mail, self).__init__(ns, pref, tag)


class Authpriv(SyslogFacility):
    """
    The facility for privileged security/authorization messages 
    as defined in RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:ietf-syslog-types", pref="ietf-syslog-types", tag="ietf-syslog-types:authpriv"):
        super(Authpriv, self).__init__(ns, pref, tag)


class Ntp(SyslogFacility):
    """
    The facility for the NTP subsystem as defined in RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:ietf-syslog-types", pref="ietf-syslog-types", tag="ietf-syslog-types:ntp"):
        super(Ntp, self).__init__(ns, pref, tag)


class Auth(SyslogFacility):
    """
    The facility for security/authorization messages as defined 
    in RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:ietf-syslog-types", pref="ietf-syslog-types", tag="ietf-syslog-types:auth"):
        super(Auth, self).__init__(ns, pref, tag)


class User(SyslogFacility):
    """
    The facility for user\-level messages as defined in RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:ietf-syslog-types", pref="ietf-syslog-types", tag="ietf-syslog-types:user"):
        super(User, self).__init__(ns, pref, tag)


class Local5(SyslogFacility):
    """
    The facility for local use 5 messages as defined in 
    RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:ietf-syslog-types", pref="ietf-syslog-types", tag="ietf-syslog-types:local5"):
        super(Local5, self).__init__(ns, pref, tag)


class News(SyslogFacility):
    """
    The facility for the network news subsystem as defined in 
    RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:ietf-syslog-types", pref="ietf-syslog-types", tag="ietf-syslog-types:news"):
        super(News, self).__init__(ns, pref, tag)


class Local7(SyslogFacility):
    """
    The facility for local use 7 messages as defined in 
    RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:ietf-syslog-types", pref="ietf-syslog-types", tag="ietf-syslog-types:local7"):
        super(Local7, self).__init__(ns, pref, tag)


class Local6(SyslogFacility):
    """
    The facility for local use 6 messages as defined in 
    RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:ietf-syslog-types", pref="ietf-syslog-types", tag="ietf-syslog-types:local6"):
        super(Local6, self).__init__(ns, pref, tag)


class Local1(SyslogFacility):
    """
    The facility for local use 1 messages as defined in 
    RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:ietf-syslog-types", pref="ietf-syslog-types", tag="ietf-syslog-types:local1"):
        super(Local1, self).__init__(ns, pref, tag)


class Local0(SyslogFacility):
    """
    The facility for local use 0 messages as defined in 
    RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:ietf-syslog-types", pref="ietf-syslog-types", tag="ietf-syslog-types:local0"):
        super(Local0, self).__init__(ns, pref, tag)


class Local3(SyslogFacility):
    """
    The facility for local use 3 messages as defined in 
    RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:ietf-syslog-types", pref="ietf-syslog-types", tag="ietf-syslog-types:local3"):
        super(Local3, self).__init__(ns, pref, tag)


class Local2(SyslogFacility):
    """
    The facility for local use 2 messages as defined in 
    RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:ietf-syslog-types", pref="ietf-syslog-types", tag="ietf-syslog-types:local2"):
        super(Local2, self).__init__(ns, pref, tag)


class Audit(SyslogFacility):
    """
    The facility for log audit messages as defined in RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:ietf-syslog-types", pref="ietf-syslog-types", tag="ietf-syslog-types:audit"):
        super(Audit, self).__init__(ns, pref, tag)


class Daemon(SyslogFacility):
    """
    The facility for the system daemons as defined in RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:ietf-syslog-types", pref="ietf-syslog-types", tag="ietf-syslog-types:daemon"):
        super(Daemon, self).__init__(ns, pref, tag)


class Lpr(SyslogFacility):
    """
    The facility for the line printer subsystem as defined in 
    RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:ietf-syslog-types", pref="ietf-syslog-types", tag="ietf-syslog-types:lpr"):
        super(Lpr, self).__init__(ns, pref, tag)


class Kern(SyslogFacility):
    """
    The facility for kernel messages as defined in RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:ietf-syslog-types", pref="ietf-syslog-types", tag="ietf-syslog-types:kern"):
        super(Kern, self).__init__(ns, pref, tag)


