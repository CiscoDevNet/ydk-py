""" ietf_yang_mpl_statistics 

This module contains information about the operation
of the MPL protocol.

Copyright (c) 2016 IETF Trust and the persons identified as
authors of the code.  All rights reserved.

Redistribution and use in source and binary forms, with or

without modification, is permitted pursuant to, and subject
to the license terms contained in, the Simplified BSD License
set forth in Section 4.c of the IETF Trust's Legal Provisions
Relating to IETF Documents
(http\://trustee.ietf.org/license\-info).

This version of this YANG module is part of RFC XXXX; see
the RFC itself for full legal notices.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class MplStatistics(object):
    """
    List describes performance statistics integrated over
    the messages identified by seed and domain identifiers. A
    forwarder can receive and forward multiple copies of a message
    uniquely identified by seqno, domain, and seed.
    
    .. attribute:: domainid  <key>
    
    	together with seed\-ID uniquely identifies buffer set
    	**type**\:  int
    
    	**range:** 0..65535
    
    .. attribute:: seedid  <key>
    
    	value uniquely identifies the MPL Seed within a MPL domain
    	**type**\:  int
    
    	**range:** 0..18446744073709551615
    
    .. attribute:: c_too_high
    
    	Number of times that a copy was not forwarded   because c > k
    	**type**\:  int
    
    	**range:** 0..18446744073709551615
    
    .. attribute:: nr_forwarded
    
    	number of times copies are forwarded, while c <= k
    	**type**\:  int
    
    	**range:** 0..18446744073709551615
    
    .. attribute:: nr_of_consistent_control
    
    	number of consistent control messages
    	**type**\:  int
    
    	**range:** 0..18446744073709551615
    
    .. attribute:: nr_of_consistent_data
    
    	number of consistent data messages
    	**type**\:  int
    
    	**range:** 0..18446744073709551615
    
    .. attribute:: nr_of_copies_forwarded
    
    	number of forwarded copies, can be larger than number\-of\-copies\-received
    	**type**\:  int
    
    	**range:** 0..18446744073709551615
    
    .. attribute:: nr_of_copies_received
    
    	total number of message copies received
    	**type**\:  int
    
    	**range:** 0..18446744073709551615
    
    .. attribute:: nr_of_inconsistent_control
    
    	number of inconsistent control messages
    	**type**\:  int
    
    	**range:** 0..18446744073709551615
    
    .. attribute:: nr_of_inconsistent_data
    
    	number of inconsistent data messages
    	**type**\:  int
    
    	**range:** 0..18446744073709551615
    
    .. attribute:: nr_of_messages_forwarded
    
    	number of forwarded messages, must be smaller than or equal to nr\-of\-messages\-received
    	**type**\:  int
    
    	**range:** 0..18446744073709551615
    
    .. attribute:: nr_of_messages_received
    
    	number of messages (one or more copies) received, must be smaller than or equal to seqno
    	**type**\:  int
    
    	**range:** 0..18446744073709551615
    
    .. attribute:: nr_of_missed
    
    	number of messages that were not received (derived from gaps in received seqno's.)
    	**type**\:  int
    
    	**range:** 0..18446744073709551615
    
    .. attribute:: nr_of_notreceived
    
    	number of messages that were not received according to control message
    	**type**\:  int
    
    	**range:** 0..18446744073709551615
    
    .. attribute:: nr_of_refused
    
    	number of refused copies because seqno too small
    	**type**\:  int
    
    	**range:** 0..18446744073709551615
    
    

    """

    _prefix = 'mpl'
    _revision = '2016-10-25'

    def __init__(self):
        self.domainid = None
        self.seedid = None
        self.c_too_high = None
        self.nr_forwarded = None
        self.nr_of_consistent_control = None
        self.nr_of_consistent_data = None
        self.nr_of_copies_forwarded = None
        self.nr_of_copies_received = None
        self.nr_of_inconsistent_control = None
        self.nr_of_inconsistent_data = None
        self.nr_of_messages_forwarded = None
        self.nr_of_messages_received = None
        self.nr_of_missed = None
        self.nr_of_notreceived = None
        self.nr_of_refused = None

    @property
    def _common_path(self):
        if self.domainid is None:
            raise YPYModelError('Key property domainid is None')
        if self.seedid is None:
            raise YPYModelError('Key property seedid is None')

        return '/ietf-yang-mpl-statistics:mpl-statistics[ietf-yang-mpl-statistics:domainID = ' + str(self.domainid) + '][ietf-yang-mpl-statistics:seedID = ' + str(self.seedid) + ']'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.domainid is not None:
            return True

        if self.seedid is not None:
            return True

        if self.c_too_high is not None:
            return True

        if self.nr_forwarded is not None:
            return True

        if self.nr_of_consistent_control is not None:
            return True

        if self.nr_of_consistent_data is not None:
            return True

        if self.nr_of_copies_forwarded is not None:
            return True

        if self.nr_of_copies_received is not None:
            return True

        if self.nr_of_inconsistent_control is not None:
            return True

        if self.nr_of_inconsistent_data is not None:
            return True

        if self.nr_of_messages_forwarded is not None:
            return True

        if self.nr_of_messages_received is not None:
            return True

        if self.nr_of_missed is not None:
            return True

        if self.nr_of_notreceived is not None:
            return True

        if self.nr_of_refused is not None:
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_yang_mpl_statistics as meta
        return meta._meta_table['MplStatistics']['meta_info']


