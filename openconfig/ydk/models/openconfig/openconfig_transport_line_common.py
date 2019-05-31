""" openconfig_transport_line_common 

This module defines common data elements for OpenConfig data
models for optical transport line system elements, such as
amplifiers and ROADMs (wavelength routers).

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class OPTICALLINEPORTTYPE(Identity):
    """
    Type definition for optical node port types
    
    

    """

    _prefix = 'oc-line-com'
    _revision = '2017-07-08'

    def __init__(self, ns="http://openconfig.net/yang/transport-line-common", pref="openconfig-transport-line-common", tag="openconfig-transport-line-common:OPTICAL_LINE_PORT_TYPE"):
        super(OPTICALLINEPORTTYPE, self).__init__(ns, pref, tag)



class INGRESS(OPTICALLINEPORTTYPE):
    """
    Ingress port, corresponding to a signal entering
    a line device such as an amplifier or wavelength
    router.
    
    

    """

    _prefix = 'oc-line-com'
    _revision = '2017-07-08'

    def __init__(self, ns="http://openconfig.net/yang/transport-line-common", pref="openconfig-transport-line-common", tag="openconfig-transport-line-common:INGRESS"):
        super(INGRESS, self).__init__(ns, pref, tag)



class EGRESS(OPTICALLINEPORTTYPE):
    """
    Egress port, corresponding to a signal exiting
    a line device such as an amplifier or wavelength
    router.
    
    

    """

    _prefix = 'oc-line-com'
    _revision = '2017-07-08'

    def __init__(self, ns="http://openconfig.net/yang/transport-line-common", pref="openconfig-transport-line-common", tag="openconfig-transport-line-common:EGRESS"):
        super(EGRESS, self).__init__(ns, pref, tag)



class ADD(OPTICALLINEPORTTYPE):
    """
    Add port, corresponding to a signal injected
    at a wavelength router.
    
    

    """

    _prefix = 'oc-line-com'
    _revision = '2017-07-08'

    def __init__(self, ns="http://openconfig.net/yang/transport-line-common", pref="openconfig-transport-line-common", tag="openconfig-transport-line-common:ADD"):
        super(ADD, self).__init__(ns, pref, tag)



class DROP(OPTICALLINEPORTTYPE):
    """
    Drop port, corresponding to a signal dropped
    at a wavelength router.
    
    

    """

    _prefix = 'oc-line-com'
    _revision = '2017-07-08'

    def __init__(self, ns="http://openconfig.net/yang/transport-line-common", pref="openconfig-transport-line-common", tag="openconfig-transport-line-common:DROP"):
        super(DROP, self).__init__(ns, pref, tag)



class MONITOR(OPTICALLINEPORTTYPE):
    """
    Monitor port, corresponding to a signal used by an optical
    channel monitor. This is used to represent the connection
    that a channel monitor port is connected to. This
    connection may be via physical cable and faceplate ports or
    internal to the device
    
    

    """

    _prefix = 'oc-line-com'
    _revision = '2017-07-08'

    def __init__(self, ns="http://openconfig.net/yang/transport-line-common", pref="openconfig-transport-line-common", tag="openconfig-transport-line-common:MONITOR"):
        super(MONITOR, self).__init__(ns, pref, tag)



