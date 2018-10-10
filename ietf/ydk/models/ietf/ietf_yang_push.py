""" ietf_yang_push 

This module contains conceptual YANG specifications
for YANG push.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error

from ydk.models.ietf.ietf_event_notifications import Error
from ydk.models.ietf.ietf_event_notifications import Stream
from ydk.models.ietf.ietf_event_notifications import Transport


class ChangeType(Enum):
    """
    ChangeType (Enum Class)

    Specifies different types of changes that may occur

    to a datastore.

    .. data:: create = 0

    	A new data node was created

    .. data:: delete = 1

    	A data node was deleted

    .. data:: modify = 2

    	The value of a data node has changed

    """

    create = Enum.YLeaf(0, "create")

    delete = Enum.YLeaf(1, "delete")

    modify = Enum.YLeaf(2, "modify")



class CustomStream(Stream):
    """
    A conceptual datastream for datastore
    updates with custom updates as defined by a user.
    
    

    """

    _prefix = 'yp'
    _revision = '2016-10-28'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:ietf-yang-push", pref="ietf-yang-push", tag="ietf-yang-push:custom-stream"):
        super(CustomStream, self).__init__(ns, pref, tag)


class YangPush(Stream):
    """
    A conceptual datastream consisting of all datastore
    updates, including operational and configuration data.
    
    

    """

    _prefix = 'yp'
    _revision = '2016-10-28'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:ietf-yang-push", pref="ietf-yang-push", tag="ietf-yang-push:yang-push"):
        super(YangPush, self).__init__(ns, pref, tag)


class ErrorDataNotAuthorized(Error):
    """
    No read authorization for a requested data node.
    
    

    """

    _prefix = 'yp'
    _revision = '2016-10-28'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:ietf-yang-push", pref="ietf-yang-push", tag="ietf-yang-push:error-data-not-authorized"):
        super(ErrorDataNotAuthorized, self).__init__(ns, pref, tag)


class Http2(Transport):
    """
    HTTP2 notifications as a transport
    
    

    """

    _prefix = 'yp'
    _revision = '2016-10-28'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:ietf-yang-push", pref="ietf-yang-push", tag="ietf-yang-push:http2"):
        super(Http2, self).__init__(ns, pref, tag)


