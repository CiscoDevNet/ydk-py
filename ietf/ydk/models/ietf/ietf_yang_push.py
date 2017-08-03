""" ietf_yang_push 

This module contains conceptual YANG specifications
for YANG push.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class ChangeType(Enum):
    """
    ChangeType

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



class YangPush(Identity):
    """
    A conceptual datastream consisting of all datastore
    updates, including operational and configuration data.
    
    

    """

    _prefix = 'yp'
    _revision = '2016-10-28'

    def __init__(self):
        super(YangPush, self).__init__("urn:ietf:params:xml:ns:yang:ietf-yang-push", "ietf-yang-push", "ietf-yang-push:yang-push")


class Http2(Identity):
    """
    HTTP2 notifications as a transport
    
    

    """

    _prefix = 'yp'
    _revision = '2016-10-28'

    def __init__(self):
        super(Http2, self).__init__("urn:ietf:params:xml:ns:yang:ietf-yang-push", "ietf-yang-push", "ietf-yang-push:http2")


class ErrorDataNotAuthorized(Identity):
    """
    No read authorization for a requested data node.
    
    

    """

    _prefix = 'yp'
    _revision = '2016-10-28'

    def __init__(self):
        super(ErrorDataNotAuthorized, self).__init__("urn:ietf:params:xml:ns:yang:ietf-yang-push", "ietf-yang-push", "ietf-yang-push:error-data-not-authorized")


class CustomStream(Identity):
    """
    A conceptual datastream for datastore
    updates with custom updates as defined by a user.
    
    

    """

    _prefix = 'yp'
    _revision = '2016-10-28'

    def __init__(self):
        super(CustomStream, self).__init__("urn:ietf:params:xml:ns:yang:ietf-yang-push", "ietf-yang-push", "ietf-yang-push:custom-stream")


