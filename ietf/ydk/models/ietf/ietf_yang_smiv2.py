""" ietf_yang_smiv2 

This module defines YANG extensions that are used to translate
SMIv2 concepts into YANG.

Copyright (c) 2012 IETF Trust and the persons identified as
authors of the code.  All rights reserved.

Redistribution and use in source and binary forms, with or
without modification, is permitted pursuant to, and subject
to the license terms contained in, the Simplified BSD License
set forth in Section 4.c of the IETF Trust's Legal Provisions
Relating to IETF Documents
(http\://trustee.ietf.org/license\-info).

This version of this YANG module is part of RFC 6643; see
the RFC itself for full legal notices.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class ObjectIdentity(Identity):
    """
    Base identity for all SMIv2 OBJECT\-IDENTITYs.
    
    

    """

    _prefix = 'smiv2'
    _revision = '2012-06-22'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:ietf-yang-smiv2", pref="ietf-yang-smiv2", tag="ietf-yang-smiv2:object-identity"):
        super(ObjectIdentity, self).__init__(ns, pref, tag)



