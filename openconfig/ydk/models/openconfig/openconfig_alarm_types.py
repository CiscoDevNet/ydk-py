""" openconfig_alarm_types 

This module defines operational state data related to alarms
that the device is reporting.

This model reuses some data items defined in the draft IETF
YANG Alarm Module\:
https\://tools.ietf.org/html/draft\-vallin\-netmod\-alarm\-module\-02

Portions of this code were derived from the draft IETF YANG Alarm
Module. Please reproduce this note if possible.

IETF code is subject to the following copyright and license\:
Copyright (c) IETF Trust and the persons identified as authors of
the code.
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, is permitted pursuant to, and subject to the license
terms contained in, the Simplified BSD License set forth in
Section 4.c of the IETF Trust's Legal Provisions Relating
to IETF Documents (http\://trustee.ietf.org/license\-info).

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class OPENCONFIGALARMTYPEID(Identity):
    """
    Base identity for alarm type ID profiles
    
    

    """

    _prefix = 'oc-alarm-types'
    _revision = '2018-01-16'

    def __init__(self, ns="http://openconfig.net/yang/alarms/types", pref="openconfig-alarm-types", tag="openconfig-alarm-types:OPENCONFIG_ALARM_TYPE_ID"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(OPENCONFIGALARMTYPEID, self).__init__(ns, pref, tag)



class OPENCONFIGALARMSEVERITY(Identity):
    """
    Base identity for alarm severity profiles. Derived
    identities are based on contents of the draft
    IETF YANG Alarm Module
    
    

    """

    _prefix = 'oc-alarm-types'
    _revision = '2018-01-16'

    def __init__(self, ns="http://openconfig.net/yang/alarms/types", pref="openconfig-alarm-types", tag="openconfig-alarm-types:OPENCONFIG_ALARM_SEVERITY"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(OPENCONFIGALARMSEVERITY, self).__init__(ns, pref, tag)



class AIS(OPENCONFIGALARMTYPEID):
    """
    Defines an alarm indication signal type of alarm
    
    

    """

    _prefix = 'oc-alarm-types'
    _revision = '2018-01-16'

    def __init__(self, ns="http://openconfig.net/yang/alarms/types", pref="openconfig-alarm-types", tag="openconfig-alarm-types:AIS"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(AIS, self).__init__(ns, pref, tag)



class EQPT(OPENCONFIGALARMTYPEID):
    """
    Defines an equipment related type of alarm that is specific
    to the physical hardware
    
    

    """

    _prefix = 'oc-alarm-types'
    _revision = '2018-01-16'

    def __init__(self, ns="http://openconfig.net/yang/alarms/types", pref="openconfig-alarm-types", tag="openconfig-alarm-types:EQPT"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(EQPT, self).__init__(ns, pref, tag)



class LOS(OPENCONFIGALARMTYPEID):
    """
    Defines a loss of signal type of alarm
    
    

    """

    _prefix = 'oc-alarm-types'
    _revision = '2018-01-16'

    def __init__(self, ns="http://openconfig.net/yang/alarms/types", pref="openconfig-alarm-types", tag="openconfig-alarm-types:LOS"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(LOS, self).__init__(ns, pref, tag)



class OTS(OPENCONFIGALARMTYPEID):
    """
    Defines a optical transport signal type of alarm
    
    

    """

    _prefix = 'oc-alarm-types'
    _revision = '2018-01-16'

    def __init__(self, ns="http://openconfig.net/yang/alarms/types", pref="openconfig-alarm-types", tag="openconfig-alarm-types:OTS"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(OTS, self).__init__(ns, pref, tag)



class UNKNOWN(OPENCONFIGALARMSEVERITY):
    """
    Indicates that the severity level could not be determined.
    This level SHOULD be avoided.
    
    

    """

    _prefix = 'oc-alarm-types'
    _revision = '2018-01-16'

    def __init__(self, ns="http://openconfig.net/yang/alarms/types", pref="openconfig-alarm-types", tag="openconfig-alarm-types:UNKNOWN"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(UNKNOWN, self).__init__(ns, pref, tag)



class MINOR(OPENCONFIGALARMSEVERITY):
    """
    Indicates the existence of a non\-service affecting fault
    condition and that corrective action should be taken in
    order to prevent a more serious (for example, service
    affecting) fault. Such a severity can be reported, for
    example, when the detected alarm condition is not currently
    degrading the capacity of the resource
    
    

    """

    _prefix = 'oc-alarm-types'
    _revision = '2018-01-16'

    def __init__(self, ns="http://openconfig.net/yang/alarms/types", pref="openconfig-alarm-types", tag="openconfig-alarm-types:MINOR"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(MINOR, self).__init__(ns, pref, tag)



class WARNING(OPENCONFIGALARMSEVERITY):
    """
    Indicates the detection of a potential or impending service
    affecting fault, before any significant effects have been felt.
    Action should be taken to further diagnose (if necessary) and
    correct the problem in order to prevent it from becoming a more
    serious service affecting fault.
    
    

    """

    _prefix = 'oc-alarm-types'
    _revision = '2018-01-16'

    def __init__(self, ns="http://openconfig.net/yang/alarms/types", pref="openconfig-alarm-types", tag="openconfig-alarm-types:WARNING"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(WARNING, self).__init__(ns, pref, tag)



class MAJOR(OPENCONFIGALARMSEVERITY):
    """
    Indicates that a service affecting condition has developed
    and an urgent corrective action is required. Such a severity
    can be reported, for example, when there is a severe
    degradation in the capability of the resource and its full
    capability must be restored.
    
    

    """

    _prefix = 'oc-alarm-types'
    _revision = '2018-01-16'

    def __init__(self, ns="http://openconfig.net/yang/alarms/types", pref="openconfig-alarm-types", tag="openconfig-alarm-types:MAJOR"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(MAJOR, self).__init__(ns, pref, tag)



class CRITICAL(OPENCONFIGALARMSEVERITY):
    """
    Indicates that a service affecting condition has occurred
    and an immediate corrective action is required. Such a
    severity can be reported, for example, when a resource becomes
    totally out of service and its capability must be restored.
    
    

    """

    _prefix = 'oc-alarm-types'
    _revision = '2018-01-16'

    def __init__(self, ns="http://openconfig.net/yang/alarms/types", pref="openconfig-alarm-types", tag="openconfig-alarm-types:CRITICAL"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(CRITICAL, self).__init__(ns, pref, tag)



