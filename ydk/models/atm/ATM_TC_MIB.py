""" ATM_TC_MIB 

This MIB Module provides Textual Conventions
and OBJECT\-IDENTITY Objects to be used by
ATM systems.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.ietf.ietf_yang_smiv2 import ObjectIdentity_Identity

class AtmConnCastType_Enum(Enum):
    """
    AtmConnCastType_Enum

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

    """

    P2P = 1

    P2MPROOT = 2

    P2MPLEAF = 3


    @staticmethod
    def _meta_info():
        from ydk.models.atm._meta import _ATM_TC_MIB as meta
        return meta._meta_table['AtmConnCastType_Enum']


class AtmConnKind_Enum(Enum):
    """
    AtmConnKind_Enum

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

    """

    PVC = 1

    SVCINCOMING = 2

    SVCOUTGOING = 3

    SPVCINITIATOR = 4

    SPVCTARGET = 5


    @staticmethod
    def _meta_info():
        from ydk.models.atm._meta import _ATM_TC_MIB as meta
        return meta._meta_table['AtmConnKind_Enum']


class AtmInterfaceType_Enum(Enum):
    """
    AtmInterfaceType_Enum

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

    """

    OTHER = 1

    AUTOCONFIG = 2

    ITUDSS2 = 3

    ATMFUNI3DOT0 = 4

    ATMFUNI3DOT1 = 5

    ATMFUNI4DOT0 = 6

    ATMFIISPUNI3DOT0 = 7

    ATMFIISPUNI3DOT1 = 8

    ATMFIISPUNI4DOT0 = 9

    ATMFPNNI1DOT0 = 10

    ATMFBICI2DOT0 = 11

    ATMFUNIPVCONLY = 12

    ATMFNNIPVCONLY = 13


    @staticmethod
    def _meta_info():
        from ydk.models.atm._meta import _ATM_TC_MIB as meta
        return meta._meta_table['AtmInterfaceType_Enum']


class AtmServiceCategory_Enum(Enum):
    """
    AtmServiceCategory_Enum

    The service category for a connection.

    """

    OTHER = 1

    CBR = 2

    RTVBR = 3

    NRTVBR = 4

    ABR = 5

    UBR = 6


    @staticmethod
    def _meta_info():
        from ydk.models.atm._meta import _ATM_TC_MIB as meta
        return meta._meta_table['AtmServiceCategory_Enum']


class AtmVorXAdminStatus_Enum(Enum):
    """
    AtmVorXAdminStatus_Enum

    The value determines the desired administrative
    status of a virtual link or cross\-connect. The up
    and down states indicate that the traffic flow is
    enabled or disabled respectively on the virtual
    link or cross\-connect.

    """

    UP = 1

    DOWN = 2


    @staticmethod
    def _meta_info():
        from ydk.models.atm._meta import _ATM_TC_MIB as meta
        return meta._meta_table['AtmVorXAdminStatus_Enum']


class AtmVorXOperStatus_Enum(Enum):
    """
    AtmVorXOperStatus_Enum

    The value determines the operational status of a
    virtual link or cross\-connect. The up and down
    states indicate that the traffic flow is enabled
    or disabled respectively on the virtual link or
    cross\-connect. The unknown state indicates that
    the state of it cannot be determined. The state
    will be down or unknown if the supporting ATM
    interface(s) is down or unknown respectively.

    """

    UP = 1

    DOWN = 2

    UNKNOWN = 3


    @staticmethod
    def _meta_info():
        from ydk.models.atm._meta import _ATM_TC_MIB as meta
        return meta._meta_table['AtmVorXOperStatus_Enum']



class AtmClpNoTaggingMcr_Identity(ObjectIdentity_Identity):
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

    _prefix = 'atm-tc'
    _revision = '1998-10-19'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.atm._meta import _ATM_TC_MIB as meta
        return meta._meta_table['AtmClpNoTaggingMcr_Identity']['meta_info']


class AtmClpNoTaggingNoScr_Identity(ObjectIdentity_Identity):
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

    _prefix = 'atm-tc'
    _revision = '1998-10-19'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.atm._meta import _ATM_TC_MIB as meta
        return meta._meta_table['AtmClpNoTaggingNoScr_Identity']['meta_info']


class AtmClpNoTaggingScrCdvt_Identity(ObjectIdentity_Identity):
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

    _prefix = 'atm-tc'
    _revision = '1998-10-19'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.atm._meta import _ATM_TC_MIB as meta
        return meta._meta_table['AtmClpNoTaggingScrCdvt_Identity']['meta_info']


class AtmClpNoTaggingScr_Identity(ObjectIdentity_Identity):
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

    _prefix = 'atm-tc'
    _revision = '1998-10-19'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.atm._meta import _ATM_TC_MIB as meta
        return meta._meta_table['AtmClpNoTaggingScr_Identity']['meta_info']


class AtmClpTaggingNoScr_Identity(ObjectIdentity_Identity):
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

    _prefix = 'atm-tc'
    _revision = '1998-10-19'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.atm._meta import _ATM_TC_MIB as meta
        return meta._meta_table['AtmClpTaggingNoScr_Identity']['meta_info']


class AtmClpTaggingScrCdvt_Identity(ObjectIdentity_Identity):
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

    _prefix = 'atm-tc'
    _revision = '1998-10-19'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.atm._meta import _ATM_TC_MIB as meta
        return meta._meta_table['AtmClpTaggingScrCdvt_Identity']['meta_info']


class AtmClpTaggingScr_Identity(ObjectIdentity_Identity):
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

    _prefix = 'atm-tc'
    _revision = '1998-10-19'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.atm._meta import _ATM_TC_MIB as meta
        return meta._meta_table['AtmClpTaggingScr_Identity']['meta_info']


class AtmClpTransparentNoScr_Identity(ObjectIdentity_Identity):
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

    _prefix = 'atm-tc'
    _revision = '1998-10-19'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.atm._meta import _ATM_TC_MIB as meta
        return meta._meta_table['AtmClpTransparentNoScr_Identity']['meta_info']


class AtmClpTransparentScr_Identity(ObjectIdentity_Identity):
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

    _prefix = 'atm-tc'
    _revision = '1998-10-19'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.atm._meta import _ATM_TC_MIB as meta
        return meta._meta_table['AtmClpTransparentScr_Identity']['meta_info']


class AtmNoClpNoScrCdvt_Identity(ObjectIdentity_Identity):
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

    _prefix = 'atm-tc'
    _revision = '1998-10-19'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.atm._meta import _ATM_TC_MIB as meta
        return meta._meta_table['AtmNoClpNoScrCdvt_Identity']['meta_info']


class AtmNoClpNoScr_Identity(ObjectIdentity_Identity):
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

    _prefix = 'atm-tc'
    _revision = '1998-10-19'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.atm._meta import _ATM_TC_MIB as meta
        return meta._meta_table['AtmNoClpNoScr_Identity']['meta_info']


class AtmNoClpScrCdvt_Identity(ObjectIdentity_Identity):
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

    _prefix = 'atm-tc'
    _revision = '1998-10-19'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.atm._meta import _ATM_TC_MIB as meta
        return meta._meta_table['AtmNoClpScrCdvt_Identity']['meta_info']


class AtmNoClpScr_Identity(ObjectIdentity_Identity):
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

    _prefix = 'atm-tc'
    _revision = '1998-10-19'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.atm._meta import _ATM_TC_MIB as meta
        return meta._meta_table['AtmNoClpScr_Identity']['meta_info']


class AtmNoClpTaggingNoScr_Identity(ObjectIdentity_Identity):
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

    _prefix = 'atm-tc'
    _revision = '1998-10-19'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.atm._meta import _ATM_TC_MIB as meta
        return meta._meta_table['AtmNoClpTaggingNoScr_Identity']['meta_info']


class AtmNoTrafficDescriptor_Identity(ObjectIdentity_Identity):
    """
    This identifies the no ATM traffic
    descriptor type.  Parameters 1, 2, 3, 4,
    and 5 are not used.  This traffic descriptor
    type can be used for best effort traffic.
    
    

    """

    _prefix = 'atm-tc'
    _revision = '1998-10-19'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.atm._meta import _ATM_TC_MIB as meta
        return meta._meta_table['AtmNoTrafficDescriptor_Identity']['meta_info']


