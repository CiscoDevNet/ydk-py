""" ATM_TC_MIB 

This MIB Module provides Textual Conventions
and OBJECT\-IDENTITY Objects to be used by
ATM systems.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Atmconncasttype(Enum):
    """
    Atmconncasttype

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

    p2p = Enum.YLeaf(1, "p2p")

    p2mpRoot = Enum.YLeaf(2, "p2mpRoot")

    p2mpLeaf = Enum.YLeaf(3, "p2mpLeaf")


class Atmconnkind(Enum):
    """
    Atmconnkind

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

    pvc = Enum.YLeaf(1, "pvc")

    svcIncoming = Enum.YLeaf(2, "svcIncoming")

    svcOutgoing = Enum.YLeaf(3, "svcOutgoing")

    spvcInitiator = Enum.YLeaf(4, "spvcInitiator")

    spvcTarget = Enum.YLeaf(5, "spvcTarget")


class Atminterfacetype(Enum):
    """
    Atminterfacetype

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

    other = Enum.YLeaf(1, "other")

    autoConfig = Enum.YLeaf(2, "autoConfig")

    ituDss2 = Enum.YLeaf(3, "ituDss2")

    atmfUni3Dot0 = Enum.YLeaf(4, "atmfUni3Dot0")

    atmfUni3Dot1 = Enum.YLeaf(5, "atmfUni3Dot1")

    atmfUni4Dot0 = Enum.YLeaf(6, "atmfUni4Dot0")

    atmfIispUni3Dot0 = Enum.YLeaf(7, "atmfIispUni3Dot0")

    atmfIispUni3Dot1 = Enum.YLeaf(8, "atmfIispUni3Dot1")

    atmfIispUni4Dot0 = Enum.YLeaf(9, "atmfIispUni4Dot0")

    atmfPnni1Dot0 = Enum.YLeaf(10, "atmfPnni1Dot0")

    atmfBici2Dot0 = Enum.YLeaf(11, "atmfBici2Dot0")

    atmfUniPvcOnly = Enum.YLeaf(12, "atmfUniPvcOnly")

    atmfNniPvcOnly = Enum.YLeaf(13, "atmfNniPvcOnly")


class Atmservicecategory(Enum):
    """
    Atmservicecategory

    The service category for a connection.

    .. data:: other = 1

    .. data:: cbr = 2

    .. data:: rtVbr = 3

    .. data:: nrtVbr = 4

    .. data:: abr = 5

    .. data:: ubr = 6

    """

    other = Enum.YLeaf(1, "other")

    cbr = Enum.YLeaf(2, "cbr")

    rtVbr = Enum.YLeaf(3, "rtVbr")

    nrtVbr = Enum.YLeaf(4, "nrtVbr")

    abr = Enum.YLeaf(5, "abr")

    ubr = Enum.YLeaf(6, "ubr")


class Atmvorxadminstatus(Enum):
    """
    Atmvorxadminstatus

    The value determines the desired administrative

    status of a virtual link or cross\-connect. The up

    and down states indicate that the traffic flow is

    enabled or disabled respectively on the virtual

    link or cross\-connect.

    .. data:: up = 1

    .. data:: down = 2

    """

    up = Enum.YLeaf(1, "up")

    down = Enum.YLeaf(2, "down")


class Atmvorxoperstatus(Enum):
    """
    Atmvorxoperstatus

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

    up = Enum.YLeaf(1, "up")

    down = Enum.YLeaf(2, "down")

    unknown = Enum.YLeaf(3, "unknown")



class Atmnoclpscrcdvt(Identity):
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
        super(Atmnoclpscrcdvt, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:ATM-TC-MIB", "ATM-TC-MIB", "ATM-TC-MIB:atmNoClpScrCdvt")


class Atmclptaggingnoscr(Identity):
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
        super(Atmclptaggingnoscr, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:ATM-TC-MIB", "ATM-TC-MIB", "ATM-TC-MIB:atmClpTaggingNoScr")


class Atmclpnotaggingnoscr(Identity):
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
        super(Atmclpnotaggingnoscr, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:ATM-TC-MIB", "ATM-TC-MIB", "ATM-TC-MIB:atmClpNoTaggingNoScr")


class Atmclpnotaggingscrcdvt(Identity):
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
        super(Atmclpnotaggingscrcdvt, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:ATM-TC-MIB", "ATM-TC-MIB", "ATM-TC-MIB:atmClpNoTaggingScrCdvt")


class Atmnotrafficdescriptor(Identity):
    """
    This identifies the no ATM traffic
    descriptor type.  Parameters 1, 2, 3, 4,
    and 5 are not used.  This traffic descriptor
    type can be used for best effort traffic.
    
    

    """

    _prefix = 'ATM-TC-MIB'
    _revision = '1998-10-19'

    def __init__(self):
        super(Atmnotrafficdescriptor, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:ATM-TC-MIB", "ATM-TC-MIB", "ATM-TC-MIB:atmNoTrafficDescriptor")


class Atmnoclptaggingnoscr(Identity):
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
        super(Atmnoclptaggingnoscr, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:ATM-TC-MIB", "ATM-TC-MIB", "ATM-TC-MIB:atmNoClpTaggingNoScr")


class Atmclpnotaggingmcr(Identity):
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
        super(Atmclpnotaggingmcr, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:ATM-TC-MIB", "ATM-TC-MIB", "ATM-TC-MIB:atmClpNoTaggingMcr")


class Atmclptaggingscrcdvt(Identity):
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
        super(Atmclptaggingscrcdvt, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:ATM-TC-MIB", "ATM-TC-MIB", "ATM-TC-MIB:atmClpTaggingScrCdvt")


class Atmclptransparentnoscr(Identity):
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
        super(Atmclptransparentnoscr, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:ATM-TC-MIB", "ATM-TC-MIB", "ATM-TC-MIB:atmClpTransparentNoScr")


class Atmnoclpnoscrcdvt(Identity):
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
        super(Atmnoclpnoscrcdvt, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:ATM-TC-MIB", "ATM-TC-MIB", "ATM-TC-MIB:atmNoClpNoScrCdvt")


class Atmclptransparentscr(Identity):
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
        super(Atmclptransparentscr, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:ATM-TC-MIB", "ATM-TC-MIB", "ATM-TC-MIB:atmClpTransparentScr")


class Atmclptaggingscr(Identity):
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
        super(Atmclptaggingscr, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:ATM-TC-MIB", "ATM-TC-MIB", "ATM-TC-MIB:atmClpTaggingScr")


class Atmnoclpscr(Identity):
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
        super(Atmnoclpscr, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:ATM-TC-MIB", "ATM-TC-MIB", "ATM-TC-MIB:atmNoClpScr")


class Atmnoclpnoscr(Identity):
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
        super(Atmnoclpnoscr, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:ATM-TC-MIB", "ATM-TC-MIB", "ATM-TC-MIB:atmNoClpNoScr")


class Atmclpnotaggingscr(Identity):
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
        super(Atmclpnotaggingscr, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:ATM-TC-MIB", "ATM-TC-MIB", "ATM-TC-MIB:atmClpNoTaggingScr")


