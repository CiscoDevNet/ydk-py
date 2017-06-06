""" ietf_syslog_types 

This module contains a collection of YANG type definitions for 
SYSLOG.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class SeverityEnum(Enum):
    """
    SeverityEnum

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

    emergency = 0

    alert = 1

    critical = 2

    error = 3

    warning = 4

    notice = 5

    info = 6

    debug = 7


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_syslog_types as meta
        return meta._meta_table['SeverityEnum']



class SyslogFacilityIdentity(object):
    """
    The base identity to represent syslog facilities
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_syslog_types as meta
        return meta._meta_table['SyslogFacilityIdentity']['meta_info']


class Local3Identity(SyslogFacilityIdentity):
    """
    The facility for local use 3 messages as defined in 
    RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self):
        SyslogFacilityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_syslog_types as meta
        return meta._meta_table['Local3Identity']['meta_info']


class DaemonIdentity(SyslogFacilityIdentity):
    """
    The facility for the system daemons as defined in RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self):
        SyslogFacilityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_syslog_types as meta
        return meta._meta_table['DaemonIdentity']['meta_info']


class Local0Identity(SyslogFacilityIdentity):
    """
    The facility for local use 0 messages as defined in 
    RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self):
        SyslogFacilityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_syslog_types as meta
        return meta._meta_table['Local0Identity']['meta_info']


class NtpIdentity(SyslogFacilityIdentity):
    """
    The facility for the NTP subsystem as defined in RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self):
        SyslogFacilityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_syslog_types as meta
        return meta._meta_table['NtpIdentity']['meta_info']


class CronIdentity(SyslogFacilityIdentity):
    """
    The facility for the clock daemon as defined in RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self):
        SyslogFacilityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_syslog_types as meta
        return meta._meta_table['CronIdentity']['meta_info']


class AuditIdentity(SyslogFacilityIdentity):
    """
    The facility for log audit messages as defined in RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self):
        SyslogFacilityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_syslog_types as meta
        return meta._meta_table['AuditIdentity']['meta_info']


class KernIdentity(SyslogFacilityIdentity):
    """
    The facility for kernel messages as defined in RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self):
        SyslogFacilityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_syslog_types as meta
        return meta._meta_table['KernIdentity']['meta_info']


class Local4Identity(SyslogFacilityIdentity):
    """
    The facility for local use 4 messages as defined in 
    RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self):
        SyslogFacilityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_syslog_types as meta
        return meta._meta_table['Local4Identity']['meta_info']


class MailIdentity(SyslogFacilityIdentity):
    """
    The facility for the mail system as defined in RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self):
        SyslogFacilityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_syslog_types as meta
        return meta._meta_table['MailIdentity']['meta_info']


class UserIdentity(SyslogFacilityIdentity):
    """
    The facility for user\-level messages as defined in RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self):
        SyslogFacilityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_syslog_types as meta
        return meta._meta_table['UserIdentity']['meta_info']


class FtpIdentity(SyslogFacilityIdentity):
    """
    The facility for the FTP daemon as defined in RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self):
        SyslogFacilityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_syslog_types as meta
        return meta._meta_table['FtpIdentity']['meta_info']


class Local6Identity(SyslogFacilityIdentity):
    """
    The facility for local use 6 messages as defined in 
    RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self):
        SyslogFacilityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_syslog_types as meta
        return meta._meta_table['Local6Identity']['meta_info']


class ConsoleIdentity(SyslogFacilityIdentity):
    """
    The facility for log alert messages as defined in RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self):
        SyslogFacilityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_syslog_types as meta
        return meta._meta_table['ConsoleIdentity']['meta_info']


class LprIdentity(SyslogFacilityIdentity):
    """
    The facility for the line printer subsystem as defined in 
    RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self):
        SyslogFacilityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_syslog_types as meta
        return meta._meta_table['LprIdentity']['meta_info']


class Local1Identity(SyslogFacilityIdentity):
    """
    The facility for local use 1 messages as defined in 
    RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self):
        SyslogFacilityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_syslog_types as meta
        return meta._meta_table['Local1Identity']['meta_info']


class AuthIdentity(SyslogFacilityIdentity):
    """
    The facility for security/authorization messages as defined 
    in RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self):
        SyslogFacilityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_syslog_types as meta
        return meta._meta_table['AuthIdentity']['meta_info']


class Local2Identity(SyslogFacilityIdentity):
    """
    The facility for local use 2 messages as defined in 
    RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self):
        SyslogFacilityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_syslog_types as meta
        return meta._meta_table['Local2Identity']['meta_info']


class Local5Identity(SyslogFacilityIdentity):
    """
    The facility for local use 5 messages as defined in 
    RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self):
        SyslogFacilityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_syslog_types as meta
        return meta._meta_table['Local5Identity']['meta_info']


class Local7Identity(SyslogFacilityIdentity):
    """
    The facility for local use 7 messages as defined in 
    RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self):
        SyslogFacilityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_syslog_types as meta
        return meta._meta_table['Local7Identity']['meta_info']


class UucpIdentity(SyslogFacilityIdentity):
    """
    The facility for the UUCP subsystem as defined in RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self):
        SyslogFacilityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_syslog_types as meta
        return meta._meta_table['UucpIdentity']['meta_info']


class NewsIdentity(SyslogFacilityIdentity):
    """
    The facility for the network news subsystem as defined in 
    RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self):
        SyslogFacilityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_syslog_types as meta
        return meta._meta_table['NewsIdentity']['meta_info']


class AuthprivIdentity(SyslogFacilityIdentity):
    """
    The facility for privileged security/authorization messages 
    as defined in RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self):
        SyslogFacilityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_syslog_types as meta
        return meta._meta_table['AuthprivIdentity']['meta_info']


class Cron2Identity(SyslogFacilityIdentity):
    """
    The facility for the second clock daemon as defined in 
    RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self):
        SyslogFacilityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_syslog_types as meta
        return meta._meta_table['Cron2Identity']['meta_info']


class SyslogIdentity(SyslogFacilityIdentity):
    """
    The facility for messages generated internally by syslogd 
    facility as defined in RFC 5424.
    
    

    """

    _prefix = 'syslogtypes'
    _revision = '2015-11-09'

    def __init__(self):
        SyslogFacilityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_syslog_types as meta
        return meta._meta_table['SyslogIdentity']['meta_info']


