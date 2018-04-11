""" cisco_xe_ietf_yang_push_ext 

This module contains augmentations on top of IETF yang push.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class EncodeTdl(Identity):
    """
    Encode data using TDL.
    
    

    """

    _prefix = 'cyp'
    _revision = '2017-08-14'

    def __init__(self):
        super(EncodeTdl, self).__init__("urn:cisco:params:xml:ns:yang:cisco-xe-ietf-yang-push-ext", "cisco-xe-ietf-yang-push-ext", "cisco-xe-ietf-yang-push-ext:encode-tdl")


class TdlStream(Identity):
    """
    Stream for native TDL datastore updates.
    
    

    """

    _prefix = 'cyp'
    _revision = '2017-08-14'

    def __init__(self):
        super(TdlStream, self).__init__("urn:cisco:params:xml:ns:yang:cisco-xe-ietf-yang-push-ext", "cisco-xe-ietf-yang-push-ext", "cisco-xe-ietf-yang-push-ext:tdl-stream")


