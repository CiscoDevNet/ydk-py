""" ATM_TC_MIB 

This MIB Module provides Textual Conventions
and OBJECT\-IDENTITY Objects to be used by
ATM systems.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError


from ydk.models.ietf.ietf_yang_smiv2 import ObjectIdentityIdentity

class AtmconncasttypeEnum(Enum):
    """
    AtmconncasttypeEnum

    The type of topology of a connection (point\-

    to\-point, point\-to\-multipoint). In the case

    of point\-to\-multipoint, the orientation of

    this VPL or VCL in the connection.

    On a host\:

    \- p2mpRoot indicates that the host

      is the root of the p2mp connection.

    \- p2mpLeaf indicates that the host

      is a leaf of the p2mp connection.

    On a switch interface\:

    \- p2mpRoot indicates that cells received

      by the switching fabric from the interface

      are from the root of the p2mp connection.

    \- p2mpLeaf indicates that cells transmitted

      to the interface from the switching fabric

      are to the leaf of the p2mp connection.

    .. data:: p2p = 1

    .. data:: p2mpRoot = 2

    .. data:: p2mpLeaf = 3

    """

    p2p = 1

    p2mpRoot = 2

    p2mpLeaf = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _ATM_TC_MIB as meta
        return meta._meta_table['AtmconncasttypeEnum']


class AtmconnkindEnum(Enum):
    """
    AtmconnkindEnum

    The type of call control used for an ATM

    connection at a particular interface. The use

    is as follows\:

       pvc(1)

          Virtual link of a PVC. Should not be

          used for an PVC/SVC (i.e., Soft PVC)

          crossconnect.

       svcIncoming(2)

          Virtual link established after a

          received signaling request to setup

          an SVC.

       svcOutgoing(3)

          Virtual link established after a

          transmitted or forwarded signaling

          request to setup an SVC.

       spvcInitiator(4)

          Virtual link at the PVC side of an

          SVC/PVC crossconnect, where the

          switch is the initiator of the Soft PVC

          setup.

       spvcTarget(5)

          Virtual link at the PVC side of an

          SVC/PVC crossconnect, where the

          switch is the target of the Soft PVC

          setup.

    For PVCs, a pvc virtual link is always cross\-

    connected to a pvc virtual link.

    For SVCs, an svcIncoming virtual link is always cross\-

    connected to an svcOutgoing virtual link.

    For Soft PVCs, an spvcInitiator is either cross\-connected to

    an svcOutgoing or an spvcTarget, and an spvcTarget is either

    cross\-connected to an svcIncoming or an spvcInitiator.

    .. data:: pvc = 1

    .. data:: svcIncoming = 2

    .. data:: svcOutgoing = 3

    .. data:: spvcInitiator = 4

    .. data:: spvcTarget = 5

    """

    pvc = 1

    svcIncoming = 2

    svcOutgoing = 3

    spvcInitiator = 4

    spvcTarget = 5


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _ATM_TC_MIB as meta
        return meta._meta_table['AtmconnkindEnum']


class AtminterfacetypeEnum(Enum):
    """
    AtminterfacetypeEnum

    The connection setup procedures used for the

    identified interface.

    Other\: Connection setup procedures other than

       those listed below.

    Auto\-configuration\:

       Indicates that the connection setup

       procedures are to be determined dynamically,

       or that determination has not yet been

       completed. One such mechanism is via ATM

       Forum ILMI auto\-configuration procedures.

    ITU\-T DSS2\:

    \-  ITU\-T Recommendation Q.2931, Broadband

       Integrated Service Digital Network (B\-ISDN)

       Digital Subscriber Signalling System No.2

       (DSS2) User\-Network Interface (UNI) Layer 3

       Specification for Basic Call/Connection

       Control (September 1994)

    \-  ITU\-T Draft Recommendation Q.2961,

       B\-ISDN DSS 2 Support of Additional Traffic

       Parameters (May 1995)

    \-  ITU\-T Draft Recommendation Q.2971,

       B\-ISDN DSS 2 User Network Interface Layer 3

       Specification for Point\-to\-multipoint

       Call/connection Control (May 1995)

    ATM Forum UNI 3.0\:

       ATM Forum, ATM User\-Network Interface,

       Version 3.0 (UNI 3.0) Specification,

       (1994).

    ATM Forum UNI 3.1\:

       ATM Forum, ATM User\-Network Interface,

       Version 3.1 (UNI 3.1) Specification,

       (November 1994).

    ATM Forum UNI Signalling 4.0\:

       ATM Forum, ATM User\-Network Interface (UNI)

       Signalling Specification Version 4.0,

       af\-sig\-0061.000 (June 1996).

    ATM Forum IISP (based on UNI 3.0 or UNI 3.1) \:

       Interim Inter\-switch Signaling Protocol

       (IISP) Specification, Version 1.0,

       af\-pnni\-0026.000, (December 1994).

    ATM Forum PNNI 1.0 \:

       ATM Forum, Private Network\-Network Interface

       Specification, Version 1.0, af\-pnni\-0055.000,

       (March 1996).

    ATM Forum B\-ICI\:

       ATM Forum, B\-ICI Specification, Version 2.0,

       af\-bici\-0013.002, (November 1995).

    ATM Forum UNI PVC Only\:

       An ATM Forum compliant UNI with the

       signalling disabled.

    ATM Forum NNI PVC Only\:

       An ATM Forum compliant NNI with the

       signalling disabled.

    .. data:: other = 1

    .. data:: autoConfig = 2

    .. data:: ituDss2 = 3

    .. data:: atmfUni3Dot0 = 4

    .. data:: atmfUni3Dot1 = 5

    .. data:: atmfUni4Dot0 = 6

    .. data:: atmfIispUni3Dot0 = 7

    .. data:: atmfIispUni3Dot1 = 8

    .. data:: atmfIispUni4Dot0 = 9

    .. data:: atmfPnni1Dot0 = 10

    .. data:: atmfBici2Dot0 = 11

    .. data:: atmfUniPvcOnly = 12

    .. data:: atmfNniPvcOnly = 13

    """

    other = 1

    autoConfig = 2

    ituDss2 = 3

    atmfUni3Dot0 = 4

    atmfUni3Dot1 = 5

    atmfUni4Dot0 = 6

    atmfIispUni3Dot0 = 7

    atmfIispUni3Dot1 = 8

    atmfIispUni4Dot0 = 9

    atmfPnni1Dot0 = 10

    atmfBici2Dot0 = 11

    atmfUniPvcOnly = 12

    atmfNniPvcOnly = 13


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _ATM_TC_MIB as meta
        return meta._meta_table['AtminterfacetypeEnum']


class AtmservicecategoryEnum(Enum):
    """
    AtmservicecategoryEnum

    The service category for a connection.

    .. data:: other = 1

    .. data:: cbr = 2

    .. data:: rtVbr = 3

    .. data:: nrtVbr = 4

    .. data:: abr = 5

    .. data:: ubr = 6

    """

    other = 1

    cbr = 2

    rtVbr = 3

    nrtVbr = 4

    abr = 5

    ubr = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _ATM_TC_MIB as meta
        return meta._meta_table['AtmservicecategoryEnum']


class AtmvorxadminstatusEnum(Enum):
    """
    AtmvorxadminstatusEnum

    The value determines the desired administrative

    status of a virtual link or cross\-connect. The up

    and down states indicate that the traffic flow is

    enabled or disabled respectively on the virtual

    link or cross\-connect.

    .. data:: up = 1

    .. data:: down = 2

    """

    up = 1

    down = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _ATM_TC_MIB as meta
        return meta._meta_table['AtmvorxadminstatusEnum']


class AtmvorxoperstatusEnum(Enum):
    """
    AtmvorxoperstatusEnum

    The value determines the operational status of a

    virtual link or cross\-connect. The up and down

    states indicate that the traffic flow is enabled

    or disabled respectively on the virtual link or

    cross\-connect. The unknown state indicates that

    the state of it cannot be determined. The state

    will be down or unknown if the supporting ATM

    interface(s) is down or unknown respectively.

    .. data:: up = 1

    .. data:: down = 2

    .. data:: unknown = 3

    """

    up = 1

    down = 2

    unknown = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _ATM_TC_MIB as meta
        return meta._meta_table['AtmvorxoperstatusEnum']



class AtmclptransparentscrIdentity(ObjectIdentityIdentity):
    """
    This traffic descriptor type is for the CLP\-
    transparent model with Sustained Cell Rate.
    The use of the parameter vector for this type\:
    Parameter 1\: peak cell rate in cells/second
                 for CLP=0+1 traffic
    Parameter 2\: sustainable cell rate in cells/second
                 for CLP=0+1 traffic
    Parameter 3\: maximum burst size in cells
    Parameter 4\: CDVT in tenths of microseconds
    Parameter 5\: not used.
    
    This traffic descriptor type is applicable to
    connections following the VBR.1 conformance
    definition.
    
    Connections specifying this traffic descriptor
    type will be rejected at UNI 3.0 or UNI 3.1
    interfaces.  For a similar traffic descriptor
    type that can be accepted at UNI 3.0 and
    UNI 3.1 interfaces, see atmNoClpScr.
    
    

    """

    _prefix = 'ATM-TC-MIB'
    _revision = '1998-10-19'

    def __init__(self):
        ObjectIdentityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _ATM_TC_MIB as meta
        return meta._meta_table['AtmclptransparentscrIdentity']['meta_info']


class AtmclpnotaggingmcrIdentity(ObjectIdentityIdentity):
    """
    This traffic descriptor type is for CLP with
    Minimum Cell Rate and no tagging.  The use of
    the parameter vector for this type\:
    Parameter 1\: peak cell rate in cells/second
                 for CLP=0+1 traffic
    Parameter 2\: CDVT in tenths of microseconds
    Parameter 3\: minimum cell rate in cells/second
    Parameter 4\: unused
    Parameter 5\: unused.
    
    

    """

    _prefix = 'ATM-TC-MIB'
    _revision = '1998-10-19'

    def __init__(self):
        ObjectIdentityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _ATM_TC_MIB as meta
        return meta._meta_table['AtmclpnotaggingmcrIdentity']['meta_info']


class AtmnoclpnoscrcdvtIdentity(ObjectIdentityIdentity):
    """
    This traffic descriptor type is for no CLP
    and no Sustained Cell Rate.  The use of the
    parameter vector for this type\:
    Parameter 1\: peak cell rate in cells/second
                 for CLP=0+1 traffic
    Parameter 2\: CDVT in tenths of microseconds
    Parameter 3\: not used
    Parameter 4\: not used
    Parameter 5\: not used.
    
    This traffic descriptor type is applicable to
    CBR connections following the UNI 3.0/3.1
    conformance definition for PCR CLP=0+1.
    These CBR connections differ from CBR.1
    connections in that the CLR objective
    applies only to the CLP=0 cell flow.
    
    This traffic descriptor type is also
    applicable to connections following the UBR.1
    conformance definition.
    
    

    """

    _prefix = 'ATM-TC-MIB'
    _revision = '1998-10-19'

    def __init__(self):
        ObjectIdentityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _ATM_TC_MIB as meta
        return meta._meta_table['AtmnoclpnoscrcdvtIdentity']['meta_info']


class AtmclptaggingscrcdvtIdentity(ObjectIdentityIdentity):
    """
    This traffic descriptor type is for CLP with
    tagging and Sustained Cell Rate.  The use of
    the parameter vector for this type\:
    Parameter 1\: peak cell rate in cells/second
                 for CLP=0+1 traffic
    Parameter 2\: sustainable cell rate in cells/second
                 for CLP=0 traffic, excess tagged as
                 CLP=1
    Parameter 3\: maximum burst size in cells
    Parameter 4\: CDVT in tenths of microseconds
    Parameter 5\: not used.
    
    This traffic descriptor type is applicable to
    connections following the VBR.3 conformance
    definition.
    
    

    """

    _prefix = 'ATM-TC-MIB'
    _revision = '1998-10-19'

    def __init__(self):
        ObjectIdentityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _ATM_TC_MIB as meta
        return meta._meta_table['AtmclptaggingscrcdvtIdentity']['meta_info']


class AtmclpnotaggingscrIdentity(ObjectIdentityIdentity):
    """
    This traffic descriptor type is for CLP with
    Sustained Cell Rate and no tagging.  The use
    of the parameter vector for this type\:
    Parameter 1\: peak cell rate in cells/second
                 for CLP=0+1 traffic
    Parameter 2\: sustainable cell rate in cells/second
                 for CLP=0 traffic
    Parameter 3\: maximum burst size in cells
    Parameter 4\: not used
    Parameter 5\: not used.
    
    

    """

    _prefix = 'ATM-TC-MIB'
    _revision = '1998-10-19'

    def __init__(self):
        ObjectIdentityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _ATM_TC_MIB as meta
        return meta._meta_table['AtmclpnotaggingscrIdentity']['meta_info']


class AtmnoclpscrcdvtIdentity(ObjectIdentityIdentity):
    """
    This traffic descriptor type is for no CLP
    with Sustained Cell Rate.  The use of the
    parameter vector for this type\:
    Parameter 1\: peak cell rate in cells/second
                 for CLP=0+1 traffic
    Parameter 2\: sustainable cell rate in cells/second
                 for CLP=0+1 traffic
    Parameter 3\: maximum burst size in cells
    Parameter 4\: CDVT in tenths of microseconds
    Parameter 5\: not used.
    
    This traffic descriptor type is applicable
    to VBR connections following the UNI 3.0/3.1
    conformance definition for PCR CLP=0+1 and
    SCR CLP=0+1.  These VBR connections
    differ from VBR.1 connections in that
    the CLR objective applies only to the CLP=0
    cell flow.
    
    

    """

    _prefix = 'ATM-TC-MIB'
    _revision = '1998-10-19'

    def __init__(self):
        ObjectIdentityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _ATM_TC_MIB as meta
        return meta._meta_table['AtmnoclpscrcdvtIdentity']['meta_info']


class AtmnotrafficdescriptorIdentity(ObjectIdentityIdentity):
    """
    This identifies the no ATM traffic
    descriptor type.  Parameters 1, 2, 3, 4,
    and 5 are not used.  This traffic descriptor
    type can be used for best effort traffic.
    
    

    """

    _prefix = 'ATM-TC-MIB'
    _revision = '1998-10-19'

    def __init__(self):
        ObjectIdentityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _ATM_TC_MIB as meta
        return meta._meta_table['AtmnotrafficdescriptorIdentity']['meta_info']


class AtmclptransparentnoscrIdentity(ObjectIdentityIdentity):
    """
    This traffic descriptor type is for the CLP\-
    transparent model and no Sustained Cell Rate.
    The use of the parameter vector for this type\:
    Parameter 1\: peak cell rate in cells/second
                 for CLP=0+1 traffic
    Parameter 2\: CDVT in tenths of microseconds
    Parameter 3\: not used
    Parameter 4\: not used
    Parameter 5\: not used.
    
    This traffic descriptor type is applicable to
    connections following the CBR.1 conformance
    definition.
    
    Connections specifying this traffic descriptor
    type will be rejected at UNI 3.0 or UNI 3.1
    interfaces.  For a similar traffic descriptor
    type that can be accepted at UNI 3.0 and
    UNI 3.1 interfaces, see atmNoClpNoScr.
    
    

    """

    _prefix = 'ATM-TC-MIB'
    _revision = '1998-10-19'

    def __init__(self):
        ObjectIdentityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _ATM_TC_MIB as meta
        return meta._meta_table['AtmclptransparentnoscrIdentity']['meta_info']


class AtmclptaggingscrIdentity(ObjectIdentityIdentity):
    """
    This traffic descriptor type is for CLP with
    tagging and Sustained Cell Rate.  The use of
    the parameter vector for this type\:
    Parameter 1\: peak cell rate in cells/second
                 for CLP=0+1 traffic
    Parameter 2\: sustainable cell rate in cells/second
                 for CLP=0 traffic, excess tagged as
                 CLP=1
    Parameter 3\: maximum burst size in cells
    Parameter 4\: not used
    Parameter 5\: not used.
    
    

    """

    _prefix = 'ATM-TC-MIB'
    _revision = '1998-10-19'

    def __init__(self):
        ObjectIdentityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _ATM_TC_MIB as meta
        return meta._meta_table['AtmclptaggingscrIdentity']['meta_info']


class AtmnoclpnoscrIdentity(ObjectIdentityIdentity):
    """
    This traffic descriptor type is for no CLP
    and no Sustained Cell Rate.  The use of the
    parameter vector for this type\:
    Parameter 1\: peak cell rate in cells/second
                 for CLP=0+1 traffic
    Parameter 2\: not used
    Parameter 3\: not used
    Parameter 4\: not used
    Parameter 5\: not used.
    
    

    """

    _prefix = 'ATM-TC-MIB'
    _revision = '1998-10-19'

    def __init__(self):
        ObjectIdentityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _ATM_TC_MIB as meta
        return meta._meta_table['AtmnoclpnoscrIdentity']['meta_info']


class AtmnoclpscrIdentity(ObjectIdentityIdentity):
    """
    This traffic descriptor type is for no CLP
    with Sustained Cell Rate.  The use of the
    parameter vector for this type\:
    Parameter 1\: peak cell rate in cells/second
                 for CLP=0+1 traffic
    Parameter 2\: sustainable cell rate in cells/second
                 for CLP=0+1 traffic
    Parameter 3\: maximum burst size in cells
    Parameter 4\: not used
    Parameter 5\: not used.
    
    

    """

    _prefix = 'ATM-TC-MIB'
    _revision = '1998-10-19'

    def __init__(self):
        ObjectIdentityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _ATM_TC_MIB as meta
        return meta._meta_table['AtmnoclpscrIdentity']['meta_info']


class AtmclpnotaggingnoscrIdentity(ObjectIdentityIdentity):
    """
    This traffic descriptor is for CLP without
    tagging and no Sustained Cell Rate.  The use
    of the parameter vector for this type\:
    Parameter 1\: peak cell rate in cells/second
                 for CLP=0+1 traffic
    Parameter 2\: peak cell rate in cells/second
                 for CLP=0 traffic
    Parameter 3\: not used
    Parameter 4\: not used
    Parameter 5\: not used.
    
    

    """

    _prefix = 'ATM-TC-MIB'
    _revision = '1998-10-19'

    def __init__(self):
        ObjectIdentityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _ATM_TC_MIB as meta
        return meta._meta_table['AtmclpnotaggingnoscrIdentity']['meta_info']


class AtmclptaggingnoscrIdentity(ObjectIdentityIdentity):
    """
    This traffic descriptor is for CLP with
    tagging and no Sustained Cell Rate.  The use
    of the parameter vector for this type\:
    Parameter 1\: peak cell rate in cells/second
                 for CLP=0+1 traffic
    Parameter 2\: peak cell rate in cells/second
                 for CLP=0 traffic, excess
                 tagged as CLP=1
    Parameter 3\: not used
    Parameter 4\: not used
    Parameter 5\: not used.
    
    

    """

    _prefix = 'ATM-TC-MIB'
    _revision = '1998-10-19'

    def __init__(self):
        ObjectIdentityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _ATM_TC_MIB as meta
        return meta._meta_table['AtmclptaggingnoscrIdentity']['meta_info']


class AtmclpnotaggingscrcdvtIdentity(ObjectIdentityIdentity):
    """
    This traffic descriptor type is for CLP with
    Sustained Cell Rate and no tagging.  The use
    of the parameter vector for this type\:
    Parameter 1\: peak cell rate in cells/second
                 for CLP=0+1 traffic
    Parameter 2\: sustainable cell rate in cells/second
                 for CLP=0 traffic
    Parameter 3\: maximum burst size in cells
    Parameter 4\: CDVT in tenths of microseconds
    Parameter 5\: not used.
    
    This traffic descriptor type is applicable to
    connections following the VBR.2 conformance
    definition.
    
    

    """

    _prefix = 'ATM-TC-MIB'
    _revision = '1998-10-19'

    def __init__(self):
        ObjectIdentityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _ATM_TC_MIB as meta
        return meta._meta_table['AtmclpnotaggingscrcdvtIdentity']['meta_info']


class AtmnoclptaggingnoscrIdentity(ObjectIdentityIdentity):
    """
    This traffic descriptor type is for no CLP
    with tagging and no Sustained Cell Rate.  The
    use of the parameter vector for this type\:
    Parameter 1\: peak cell rate in cells/second
                 for CLP=0+1 traffic
    Parameter 2\: CDVT in tenths of microseconds
    Parameter 3\: not used
    Parameter 4\: not used
    Parameter 5\: not used.
    
    This traffic descriptor type is applicable to
    connections following the UBR.2 conformance
    definition .
    
    

    """

    _prefix = 'ATM-TC-MIB'
    _revision = '1998-10-19'

    def __init__(self):
        ObjectIdentityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _ATM_TC_MIB as meta
        return meta._meta_table['AtmnoclptaggingnoscrIdentity']['meta_info']


