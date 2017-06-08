""" ietf_pmip_qos 

This module contains a collection of YANG definitions for
quality of service paramaters used in Proxy Mobile IPv6.

Copyright (c) 2016 IETF Trust and the persons identified as the
document authors. All rights reserved.

This document is subject to BCP 78 and the IETF Trust's Legal
Provisions Relating to IETF Documents
(http\://trustee.ietf.org/license\-info) in effect on the date of
publication of this document. Please review these documents
carefully, as they describe your rights and restrictions with
respect to this document. Code Components extracted from this
document must include Simplified BSD License text as described
in Section 4.e of the Trust Legal Provisions and are provided
without warranty as described in the Simplified BSD License.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class OperationalCodeEnum(Enum):
    """
    OperationalCodeEnum

    1\-octet Operational code indicates the type of QoS request.

       Reserved values\:   (6) to (255)

            Currently not used.  Receiver MUST ignore the option

            received with any value in this range.

    .. data:: RESPONSE = 0

    	Response to a QoS request

    .. data:: ALLOCATE = 1

    	Request to allocate QoS resources

    .. data:: DE_ALLOCATE = 2

    	Request to de-Allocate QoS resources

    .. data:: MODIFY = 3

    	Request to modify QoS parameters for a

    	previously negotiated QoS Service Request

    .. data:: QUERY = 4

    	Query to list the previously negotiated QoS

    	Service Requests that are still active

    .. data:: NEGOTIATE = 5

    	Response to a QoS Service Request with a

    	counter QoS proposal

    """

    RESPONSE = 0

    ALLOCATE = 1

    DE_ALLOCATE = 2

    MODIFY = 3

    QUERY = 4

    NEGOTIATE = 5


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_pmip_qos as meta
        return meta._meta_table['OperationalCodeEnum']


class QosAttrubiteTypeEnumEnum(Enum):
    """
    QosAttrubiteTypeEnumEnum

    8\-bit unsigned integer indicating the type of the QoS

     attribute.  This specification reserves the following

    reserved values.

     (12) to (254) \-  Reserved

        These values are reserved for future allocation.

     (255)  Reserved

        This value is reserved and cannot be used.

    .. data:: Reserved = 0

    	This value is reserved and cannot be used

    .. data:: Per_MN_Agg_Max_DL_Bit_Rate = 1

    	Per-Mobile-Node Aggregate Maximum Downlink

    	Bit Rate.

    .. data:: Per_MN_Agg_Max_UL_Bit_Rate = 2

    	Per-Mobile-Node Aggregate Maximum Uplink Bit

    	Rate.

    .. data:: Per_Session_Agg_Max_DL_Bit_Rate = 3

    	Per-Mobility-Session Aggregate Maximum

    	Downlink Bit Rate.

    .. data:: Per_Session_Agg_Max_UL_Bit_Rate = 4

    	Per-Mobility-Session Aggregate Maximum

    	Uplink Bit Rate.

    .. data:: Allocation_Retention_Priority = 5

    	Allocation and Retention Priority.

    .. data:: Aggregate_Max_DL_Bit_Rate = 6

    	Aggregate Maximum Downlink Bit Rate.

    .. data:: Aggregate_Max_UL_Bit_Rate = 7

    	Aggregate Maximum Uplink Bit Rate.

    .. data:: Guaranteed_DL_Bit_Rate = 8

    	Guaranteed Downlink Bit Rate.

    .. data:: Guaranteed_UL_Bit_Rate = 9

    	Guaranteed Uplink Bit Rate.

    .. data:: QoS_Traffic_Selector = 10

    	QoS Traffic Selector.

    .. data:: QoS_Vendor_Specific_Attribute = 11

    	QoS Vendor-Specific Attribute.

    """

    Reserved = 0

    Per_MN_Agg_Max_DL_Bit_Rate = 1

    Per_MN_Agg_Max_UL_Bit_Rate = 2

    Per_Session_Agg_Max_DL_Bit_Rate = 3

    Per_Session_Agg_Max_UL_Bit_Rate = 4

    Allocation_Retention_Priority = 5

    Aggregate_Max_DL_Bit_Rate = 6

    Aggregate_Max_UL_Bit_Rate = 7

    Guaranteed_DL_Bit_Rate = 8

    Guaranteed_UL_Bit_Rate = 9

    QoS_Traffic_Selector = 10

    QoS_Vendor_Specific_Attribute = 11


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_pmip_qos as meta
        return meta._meta_table['QosAttrubiteTypeEnumEnum']



class QosAttributeTypeIdentity(object):
    """
    Base type for Quality of Service Attributes
    
    

    """

    _prefix = 'qos-pmip'
    _revision = '2016-02-10'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_pmip_qos as meta
        return meta._meta_table['QosAttributeTypeIdentity']['meta_info']


class QosTrafficSelectorTypeIdentity(QosAttributeTypeIdentity):
    """
    QoS Traffic Selector.
    
    

    """

    _prefix = 'qos-pmip'
    _revision = '2016-02-10'

    def __init__(self):
        QosAttributeTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_pmip_qos as meta
        return meta._meta_table['QosTrafficSelectorTypeIdentity']['meta_info']


class PerMnAggMaxUlBitRateTypeIdentity(QosAttributeTypeIdentity):
    """
    Per\-Mobile\-Node Aggregate Maximum Uplink Bit Rate
    
    

    """

    _prefix = 'qos-pmip'
    _revision = '2016-02-10'

    def __init__(self):
        QosAttributeTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_pmip_qos as meta
        return meta._meta_table['PerMnAggMaxUlBitRateTypeIdentity']['meta_info']


class PerSessionAggMaxDlBitRateTypeIdentity(QosAttributeTypeIdentity):
    """
    Per\-Mobility\-Session Aggregate Maximum Downlink Bit Rate.
    
    

    """

    _prefix = 'qos-pmip'
    _revision = '2016-02-10'

    def __init__(self):
        QosAttributeTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_pmip_qos as meta
        return meta._meta_table['PerSessionAggMaxDlBitRateTypeIdentity']['meta_info']


class GuaranteedDlBitRateTypeIdentity(QosAttributeTypeIdentity):
    """
    Guaranteed Downlink Bit Rate.
    
    

    """

    _prefix = 'qos-pmip'
    _revision = '2016-02-10'

    def __init__(self):
        QosAttributeTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_pmip_qos as meta
        return meta._meta_table['GuaranteedDlBitRateTypeIdentity']['meta_info']


class AggregateMaxUlBitRateTypeIdentity(QosAttributeTypeIdentity):
    """
    Aggregate Maximum Uplink Bit Rate.
    
    

    """

    _prefix = 'qos-pmip'
    _revision = '2016-02-10'

    def __init__(self):
        QosAttributeTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_pmip_qos as meta
        return meta._meta_table['AggregateMaxUlBitRateTypeIdentity']['meta_info']


class QosVendorSpecificAttributeTypeIdentity(QosAttributeTypeIdentity):
    """
    QoS Vendor\-Specific Attribute.
    
    

    """

    _prefix = 'qos-pmip'
    _revision = '2016-02-10'

    def __init__(self):
        QosAttributeTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_pmip_qos as meta
        return meta._meta_table['QosVendorSpecificAttributeTypeIdentity']['meta_info']


class AggregateMaxDlBitRateTypeIdentity(QosAttributeTypeIdentity):
    """
    Aggregate Maximum Downlink Bit Rate.
    
    

    """

    _prefix = 'qos-pmip'
    _revision = '2016-02-10'

    def __init__(self):
        QosAttributeTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_pmip_qos as meta
        return meta._meta_table['AggregateMaxDlBitRateTypeIdentity']['meta_info']


class PerMnAggMaxDlBitRateTypeIdentity(QosAttributeTypeIdentity):
    """
    Per\-Mobile\-Node Aggregate Maximum Downlink Bit Rate.
    
    

    """

    _prefix = 'qos-pmip'
    _revision = '2016-02-10'

    def __init__(self):
        QosAttributeTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_pmip_qos as meta
        return meta._meta_table['PerMnAggMaxDlBitRateTypeIdentity']['meta_info']


class AllocationRetentionPriorityTypeIdentity(QosAttributeTypeIdentity):
    """
    Allocation and Retention Priority.
    
    

    """

    _prefix = 'qos-pmip'
    _revision = '2016-02-10'

    def __init__(self):
        QosAttributeTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_pmip_qos as meta
        return meta._meta_table['AllocationRetentionPriorityTypeIdentity']['meta_info']


class PerSessionAggMaxUlBitRateTypeIdentity(QosAttributeTypeIdentity):
    """
    Per\-Mobility\-Session Aggregate Maximum Uplink Bit Rate.
    
    

    """

    _prefix = 'qos-pmip'
    _revision = '2016-02-10'

    def __init__(self):
        QosAttributeTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_pmip_qos as meta
        return meta._meta_table['PerSessionAggMaxUlBitRateTypeIdentity']['meta_info']


class GuaranteedUlBitRateTypeIdentity(QosAttributeTypeIdentity):
    """
    Guaranteed Uplink Bit Rate.
    
    

    """

    _prefix = 'qos-pmip'
    _revision = '2016-02-10'

    def __init__(self):
        QosAttributeTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_pmip_qos as meta
        return meta._meta_table['GuaranteedUlBitRateTypeIdentity']['meta_info']


