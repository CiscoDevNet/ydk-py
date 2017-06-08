""" ietf_pw 

pw

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class CcTypeEnum(Enum):
    """
    CcTypeEnum

    The defined values for CC(Control Channel) Types for MPLS PWs.

    .. data:: pw_ach = 0

    	PWE3 Control Word with 0001b as first nibble (PW-ACH, see [RFC4385])

    .. data:: alert_label = 1

    	MPLS Router Alert Label

    .. data:: ttl = 2

    	MPLS PW Label with TTL == 1

    """

    pw_ach = 0

    alert_label = 1

    ttl = 2


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_pw as meta
        return meta._meta_table['CcTypeEnum']


class CvTypeEnum(Enum):
    """
    CvTypeEnum

    The defined values for CV(Connectivity Verification) Types for MPLS PWs

    .. data:: ICMP_ping = 0

    	ICMP-ping.

    .. data:: LSP_ping = 1

    	LSP-ping

    .. data:: BFD_basic_ip = 2

    	BFD basic ip

    .. data:: BFD_basic_raw = 3

    	BFD basic raw 

    .. data:: BFD_signalling_ip = 4

    	BFD signalling ip

    .. data:: BFD_signalling_raw = 5

    	BFD signalling raw

    """

    ICMP_ping = 0

    LSP_ping = 1

    BFD_basic_ip = 2

    BFD_basic_raw = 3

    BFD_signalling_ip = 4

    BFD_signalling_raw = 5


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_pw as meta
        return meta._meta_table['CvTypeEnum']


class CwCapableTypeEnum(Enum):
    """
    CwCapableTypeEnum

    control\-word capable preference type

    .. data:: non_preferred = 0

    	No preference for control-word

    .. data:: preferred = 1

    	Prefer to have control-word negotiation

    """

    non_preferred = 0

    preferred = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_pw as meta
        return meta._meta_table['CwCapableTypeEnum']


class PwRtpFlagEnum(Enum):
    """
    PwRtpFlagEnum

    The use flag of rtp header.

    .. data:: UNUSE = 0

    	Not use the rtp header.

    .. data:: USE = 1

    	Use the rtp header.

    .. data:: UNKNOWN = 3

    	The usage of the rtp header is unknown.

    """

    UNUSE = 0

    USE = 1

    UNKNOWN = 3


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_pw as meta
        return meta._meta_table['PwRtpFlagEnum']


class PwTimestampModeEnum(Enum):
    """
    PwTimestampModeEnum

    The timestamp mode of TDM service.

    .. data:: Absolute = 0

    	The timestamp mode is absolute.

    .. data:: Differential = 1

    	The timestamp mode is differential .

    .. data:: UNKNOWN = 3

    	The timestamp mode is unknown.

    """

    Absolute = 0

    Differential = 1

    UNKNOWN = 3


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_pw as meta
        return meta._meta_table['PwTimestampModeEnum']


class PwTypeEnum(Enum):
    """
    PwTypeEnum

    The PW type of the PW.

    .. data:: unknown = 0

    	The PW type is unknown

    .. data:: dlciOld = 1

    	The PW type is dlciOld

    .. data:: atmSdu = 2

    	The PW type is atmSdu

    .. data:: atmCell = 3

    	The PW type is atmCell

    .. data:: vlan = 4

    	The PW type is vlan

    .. data:: ethernet = 5

    	The PW type is ethernet

    .. data:: hdlc = 6

    	The PW type is hdlc

    .. data:: ppp = 7

    	The PW type is ppp

    .. data:: sdhCESoM = 8

    	The PW type is sdhCESoM

    .. data:: atmVCCn = 9

    	The PW type is atmVCCn

    .. data:: atmVPCn = 10

    	The PW type is atmVPCn

    .. data:: ipL2 = 11

    	The PW type is ipL2

    .. data:: atmVCC1 = 12

    	The PW type is atmVCC1

    .. data:: atmVPC1 = 13

    	The PW type is atmVPC1

    .. data:: atmPDU = 14

    	The PW type is atmPDU

    .. data:: frPort = 15

    	The PW type is frPort

    .. data:: sdhCEoP = 16

    	The PW type is sdhCEoP

    .. data:: saTopE1 = 17

    	The PW type is saTopE1

    .. data:: saTopT1 = 18

    	The PW type is saTopT1

    .. data:: saTopE3 = 19

    	The PW type is saTopE3

    .. data:: saTopT3 = 20

    	The PW type is saTopT3

    .. data:: ceSoPSNB = 21

    	The PW type is ceSoPSNB

    .. data:: tdmAAL1 = 22

    	The PW type is tdmAAL1

    .. data:: ceSoPSNC = 23

    	The PW type is ceSoPSNC

    .. data:: tdmAAL2 = 24

    	The PW type is tdmAAL2

    .. data:: dlciNew = 25

    	The PW type is dlciNew

    """

    unknown = 0

    dlciOld = 1

    atmSdu = 2

    atmCell = 3

    vlan = 4

    ethernet = 5

    hdlc = 6

    ppp = 7

    sdhCESoM = 8

    atmVCCn = 9

    atmVPCn = 10

    ipL2 = 11

    atmVCC1 = 12

    atmVPC1 = 13

    atmPDU = 14

    frPort = 15

    sdhCEoP = 16

    saTopE1 = 17

    saTopT1 = 18

    saTopE3 = 19

    saTopT3 = 20

    ceSoPSNB = 21

    tdmAAL1 = 22

    ceSoPSNC = 23

    tdmAAL2 = 24

    dlciNew = 25


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_pw as meta
        return meta._meta_table['PwTypeEnum']



class Pwe3(object):
    """
    configure pw
    
    .. attribute:: ms_pw
    
    	configure ms\-pw
    	**type**\:   :py:class:`MsPw <ydk.models.ietf.ietf_pw.Pwe3.MsPw>`
    
    .. attribute:: ss_pw
    
    	configure ss\-pw
    	**type**\:   :py:class:`SsPw <ydk.models.ietf.ietf_pw.Pwe3.SsPw>`
    
    

    """

    _prefix = 'pw'
    _revision = '2016-10-05'

    def __init__(self):
        self.ms_pw = Pwe3.MsPw()
        self.ms_pw.parent = self
        self.ss_pw = Pwe3.SsPw()
        self.ss_pw.parent = self


    class SsPw(object):
        """
        configure ss\-pw
        
        .. attribute:: ss_pw
        
        	ss\-pw list
        	**type**\: list of    :py:class:`SsPw_ <ydk.models.ietf.ietf_pw.Pwe3.SsPw.SsPw_>`
        
        

        """

        _prefix = 'pw'
        _revision = '2016-10-05'

        def __init__(self):
            self.parent = None
            self.ss_pw = YList()
            self.ss_pw.parent = self
            self.ss_pw.name = 'ss_pw'


        class SsPw_(object):
            """
            ss\-pw list
            
            .. attribute:: name  <key>
            
            	ss\-pseudowire name
            	**type**\:  str
            
            .. attribute:: agi
            
            	Attachment Group Identifier
            	**type**\:  str
            
            .. attribute:: autodiscovery_enable
            
            	enable the auto\-discovery
            	**type**\:  bool
            
            .. attribute:: cw_capable
            
            	control\-word negotiation preference
            	**type**\:   :py:class:`CwCapableTypeEnum <ydk.models.ietf.ietf_pw.CwCapableTypeEnum>`
            
            	**default value**\: preferred
            
            .. attribute:: interfaces
            
            	Interfaces
            	**type**\:   :py:class:`Interfaces <ydk.models.ietf.ietf_pw.Pwe3.SsPw.SsPw_.Interfaces>`
            
            .. attribute:: leaf_type
            
            	pseudo\-wire type
            	**type**\:   :py:class:`PwTypeEnum <ydk.models.ietf.ietf_pw.PwTypeEnum>`
            
            .. attribute:: peer_ip
            
            	peer IP address
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            
            ----
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            
            ----
            .. attribute:: pw_id
            
            	pseudowire id
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: receive_label
            
            	receive label
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: source_aii
            
            	Source Attachment individual identifier
            	**type**\:  str
            
            .. attribute:: static_pw_id
            
            	pseudowire id
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: target_aii
            
            	Target Attachment individual identifier
            	**type**\:  str
            
            .. attribute:: transmit_label
            
            	transmit lable
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tunnel
            
            	tunnel list
            	**type**\: list of    :py:class:`Tunnel <ydk.models.ietf.ietf_pw.Pwe3.SsPw.SsPw_.Tunnel>`
            
            .. attribute:: type
            
            	pseudo\-wire type
            	**type**\:   :py:class:`PwTypeEnum <ydk.models.ietf.ietf_pw.PwTypeEnum>`
            
            

            """

            _prefix = 'pw'
            _revision = '2016-10-05'

            def __init__(self):
                self.parent = None
                self.name = None
                self.agi = None
                self.autodiscovery_enable = None
                self.cw_capable = None
                self.interfaces = Pwe3.SsPw.SsPw_.Interfaces()
                self.interfaces.parent = self
                self.leaf_type = None
                self.peer_ip = None
                self.pw_id = None
                self.receive_label = None
                self.source_aii = None
                self.static_pw_id = None
                self.target_aii = None
                self.transmit_label = None
                self.tunnel = YList()
                self.tunnel.parent = self
                self.tunnel.name = 'tunnel'
                self.type = None


            class Tunnel(object):
                """
                tunnel list
                
                .. attribute:: tunnel_id  <key>
                
                	tunnel identifier
                	**type**\:  str
                
                

                """

                _prefix = 'pw'
                _revision = '2016-10-05'

                def __init__(self):
                    self.parent = None
                    self.tunnel_id = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.tunnel_id is None:
                        raise YPYModelError('Key property tunnel_id is None')

                    return self.parent._common_path +'/ietf-pw:tunnel[ietf-pw:tunnel-id = ' + str(self.tunnel_id) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.tunnel_id is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_pw as meta
                    return meta._meta_table['Pwe3.SsPw.SsPw_.Tunnel']['meta_info']


            class Interfaces(object):
                """
                Interfaces
                
                .. attribute:: interface
                
                	interface list
                	**type**\: list of    :py:class:`Interface <ydk.models.ietf.ietf_pw.Pwe3.SsPw.SsPw_.Interfaces.Interface>`
                
                

                """

                _prefix = 'pw'
                _revision = '2016-10-05'

                def __init__(self):
                    self.parent = None
                    self.interface = YList()
                    self.interface.parent = self
                    self.interface.name = 'interface'


                class Interface(object):
                    """
                    interface list
                    
                    .. attribute:: name  <key>
                    
                    	Interfaces used for pw
                    	**type**\:  str
                    
                    	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
                    
                    .. attribute:: bit_rate
                    
                    	The local bit rate of the PW
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: cells_per_packet
                    
                    	The local TDMoIP AAL1 cells per packet of the PW
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: cep_option
                    
                    	The CEP Options parameter of the PW
                    	**type**\:   :py:class:`CepOption <ydk.models.ietf.ietf_pw.Pwe3.SsPw.SsPw_.Interfaces.Interface.CepOption>`
                    
                    .. attribute:: fcs_retention_indicator
                    
                    	The negotiated fcs retention indicator of the PW
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: fr_dlci_len
                    
                    	The local fr dlci length of the PW
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: frag_indicator
                    
                    	The local fragmentation indicator of the PW
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interface_description
                    
                    	The local interface description of the PW
                    	**type**\:  str
                    
                    	**length:** 0..81
                    
                    .. attribute:: max_atm_cells
                    
                    	The local max atm cells of the PW
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: mtu
                    
                    	pseudowire mtu
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: payload_bytes
                    
                    	The local payload bytes of the PW
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: requested_vlan_id
                    
                    	The local requested VLAN ID of the PW
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tdm_options
                    
                    	The TDM Options parameter of the PW
                    	**type**\:   :py:class:`TdmOptions <ydk.models.ietf.ietf_pw.Pwe3.SsPw.SsPw_.Interfaces.Interface.TdmOptions>`
                    
                    .. attribute:: vccv_parameter
                    
                    	vccv\-parameter
                    	**type**\:   :py:class:`VccvParameter <ydk.models.ietf.ietf_pw.Pwe3.SsPw.SsPw_.Interfaces.Interface.VccvParameter>`
                    
                    

                    """

                    _prefix = 'pw'
                    _revision = '2016-10-05'

                    def __init__(self):
                        self.parent = None
                        self.name = None
                        self.bit_rate = None
                        self.cells_per_packet = None
                        self.cep_option = Pwe3.SsPw.SsPw_.Interfaces.Interface.CepOption()
                        self.cep_option.parent = self
                        self.fcs_retention_indicator = None
                        self.fr_dlci_len = None
                        self.frag_indicator = None
                        self.interface_description = None
                        self.max_atm_cells = None
                        self.mtu = None
                        self.payload_bytes = None
                        self.requested_vlan_id = None
                        self.tdm_options = Pwe3.SsPw.SsPw_.Interfaces.Interface.TdmOptions()
                        self.tdm_options.parent = self
                        self.vccv_parameter = Pwe3.SsPw.SsPw_.Interfaces.Interface.VccvParameter()
                        self.vccv_parameter.parent = self


                    class VccvParameter(object):
                        """
                        vccv\-parameter
                        
                        .. attribute:: cc
                        
                        	Control Channel Types
                        	**type**\:   :py:class:`CcTypeEnum <ydk.models.ietf.ietf_pw.CcTypeEnum>`
                        
                        .. attribute:: cv
                        
                        	Connectivity Verification Types
                        	**type**\:   :py:class:`CvTypeEnum <ydk.models.ietf.ietf_pw.CvTypeEnum>`
                        
                        

                        """

                        _prefix = 'pw'
                        _revision = '2016-10-05'

                        def __init__(self):
                            self.parent = None
                            self.cc = None
                            self.cv = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/ietf-pw:vccv-parameter'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.cc is not None:
                                return True

                            if self.cv is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ietf._meta import _ietf_pw as meta
                            return meta._meta_table['Pwe3.SsPw.SsPw_.Interfaces.Interface.VccvParameter']['meta_info']


                    class TdmOptions(object):
                        """
                        The TDM Options parameter of the PW
                        
                        .. attribute:: cas
                        
                        	The local cas of the PW
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: frequency
                        
                        	The local frequency of timestamping clock
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: payload_type
                        
                        	The local payload type in the RTP header expected by the PW endpoint distributing this FEC
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: rtp
                        
                        	The local rtp header usage
                        	**type**\:   :py:class:`PwRtpFlagEnum <ydk.models.ietf.ietf_pw.PwRtpFlagEnum>`
                        
                        .. attribute:: sp
                        
                        	The local sp of the PW
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: ssrc
                        
                        	The local value of the Synchronization source ID
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: timestamp_mode
                        
                        	The local timestamp mode
                        	**type**\:   :py:class:`PwTimestampModeEnum <ydk.models.ietf.ietf_pw.PwTimestampModeEnum>`
                        
                        

                        """

                        _prefix = 'pw'
                        _revision = '2016-10-05'

                        def __init__(self):
                            self.parent = None
                            self.cas = None
                            self.frequency = None
                            self.payload_type = None
                            self.rtp = None
                            self.sp = None
                            self.ssrc = None
                            self.timestamp_mode = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/ietf-pw:tdm-options'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.cas is not None:
                                return True

                            if self.frequency is not None:
                                return True

                            if self.payload_type is not None:
                                return True

                            if self.rtp is not None:
                                return True

                            if self.sp is not None:
                                return True

                            if self.ssrc is not None:
                                return True

                            if self.timestamp_mode is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ietf._meta import _ietf_pw as meta
                            return meta._meta_table['Pwe3.SsPw.SsPw_.Interfaces.Interface.TdmOptions']['meta_info']


                    class CepOption(object):
                        """
                        The CEP Options parameter of the PW
                        
                        .. attribute:: ais
                        
                        	The local ais of CEP Options parameter of the PW
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: async_e3
                        
                        	The local async\-e3 of CEP Options parameter of the PW
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: async_t3
                        
                        	The local async\-t3 of CEP Options parameter of the PW
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: cep_type
                        
                        	The local cep type of CEP Options parameter of the PW
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: ebm
                        
                        	The local ebm of CEP Options parameter of the PW
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: rtp
                        
                        	The local rtp of CEP Options parameter of the PW
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: une
                        
                        	The local une of CEP Options parameter of the PW
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        

                        """

                        _prefix = 'pw'
                        _revision = '2016-10-05'

                        def __init__(self):
                            self.parent = None
                            self.ais = None
                            self.async_e3 = None
                            self.async_t3 = None
                            self.cep_type = None
                            self.ebm = None
                            self.rtp = None
                            self.une = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/ietf-pw:cep-option'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.ais is not None:
                                return True

                            if self.async_e3 is not None:
                                return True

                            if self.async_t3 is not None:
                                return True

                            if self.cep_type is not None:
                                return True

                            if self.ebm is not None:
                                return True

                            if self.rtp is not None:
                                return True

                            if self.une is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ietf._meta import _ietf_pw as meta
                            return meta._meta_table['Pwe3.SsPw.SsPw_.Interfaces.Interface.CepOption']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.name is None:
                            raise YPYModelError('Key property name is None')

                        return self.parent._common_path +'/ietf-pw:interface[ietf-pw:name = ' + str(self.name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.name is not None:
                            return True

                        if self.bit_rate is not None:
                            return True

                        if self.cells_per_packet is not None:
                            return True

                        if self.cep_option is not None and self.cep_option._has_data():
                            return True

                        if self.fcs_retention_indicator is not None:
                            return True

                        if self.fr_dlci_len is not None:
                            return True

                        if self.frag_indicator is not None:
                            return True

                        if self.interface_description is not None:
                            return True

                        if self.max_atm_cells is not None:
                            return True

                        if self.mtu is not None:
                            return True

                        if self.payload_bytes is not None:
                            return True

                        if self.requested_vlan_id is not None:
                            return True

                        if self.tdm_options is not None and self.tdm_options._has_data():
                            return True

                        if self.vccv_parameter is not None and self.vccv_parameter._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_pw as meta
                        return meta._meta_table['Pwe3.SsPw.SsPw_.Interfaces.Interface']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-pw:interfaces'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.interface is not None:
                        for child_ref in self.interface:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_pw as meta
                    return meta._meta_table['Pwe3.SsPw.SsPw_.Interfaces']['meta_info']

            @property
            def _common_path(self):
                if self.name is None:
                    raise YPYModelError('Key property name is None')

                return '/ietf-pw:pwe3/ietf-pw:ss-pw/ietf-pw:ss-pw[ietf-pw:name = ' + str(self.name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.name is not None:
                    return True

                if self.agi is not None:
                    return True

                if self.autodiscovery_enable is not None:
                    return True

                if self.cw_capable is not None:
                    return True

                if self.interfaces is not None and self.interfaces._has_data():
                    return True

                if self.leaf_type is not None:
                    return True

                if self.peer_ip is not None:
                    return True

                if self.pw_id is not None:
                    return True

                if self.receive_label is not None:
                    return True

                if self.source_aii is not None:
                    return True

                if self.static_pw_id is not None:
                    return True

                if self.target_aii is not None:
                    return True

                if self.transmit_label is not None:
                    return True

                if self.tunnel is not None:
                    for child_ref in self.tunnel:
                        if child_ref._has_data():
                            return True

                if self.type is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_pw as meta
                return meta._meta_table['Pwe3.SsPw.SsPw_']['meta_info']

        @property
        def _common_path(self):

            return '/ietf-pw:pwe3/ietf-pw:ss-pw'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.ss_pw is not None:
                for child_ref in self.ss_pw:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_pw as meta
            return meta._meta_table['Pwe3.SsPw']['meta_info']


    class MsPw(object):
        """
        configure ms\-pw
        
        .. attribute:: ms_pw
        
        	ms\-pw list
        	**type**\: list of    :py:class:`MsPw_ <ydk.models.ietf.ietf_pw.Pwe3.MsPw.MsPw_>`
        
        

        """

        _prefix = 'pw'
        _revision = '2016-10-05'

        def __init__(self):
            self.parent = None
            self.ms_pw = YList()
            self.ms_pw.parent = self
            self.ms_pw.name = 'ms_pw'


        class MsPw_(object):
            """
            ms\-pw list
            
            .. attribute:: name  <key>
            
            	ms\-pseudowire name
            	**type**\:  str
            
            .. attribute:: pw_segment_a
            
            	pw segment\-a list
            	**type**\: list of    :py:class:`PwSegmentA <ydk.models.ietf.ietf_pw.Pwe3.MsPw.MsPw_.PwSegmentA>`
            
            .. attribute:: pw_segment_z
            
            	pw segment\-z list
            	**type**\: list of    :py:class:`PwSegmentZ <ydk.models.ietf.ietf_pw.Pwe3.MsPw.MsPw_.PwSegmentZ>`
            
            

            """

            _prefix = 'pw'
            _revision = '2016-10-05'

            def __init__(self):
                self.parent = None
                self.name = None
                self.pw_segment_a = YList()
                self.pw_segment_a.parent = self
                self.pw_segment_a.name = 'pw_segment_a'
                self.pw_segment_z = YList()
                self.pw_segment_z.parent = self
                self.pw_segment_z.name = 'pw_segment_z'


            class PwSegmentA(object):
                """
                pw segment\-a list
                
                .. attribute:: name  <key>
                
                	pseudowire segment a name
                	**type**\:  str
                
                

                """

                _prefix = 'pw'
                _revision = '2016-10-05'

                def __init__(self):
                    self.parent = None
                    self.name = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.name is None:
                        raise YPYModelError('Key property name is None')

                    return self.parent._common_path +'/ietf-pw:pw-segment-a[ietf-pw:name = ' + str(self.name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.name is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_pw as meta
                    return meta._meta_table['Pwe3.MsPw.MsPw_.PwSegmentA']['meta_info']


            class PwSegmentZ(object):
                """
                pw segment\-z list
                
                .. attribute:: name  <key>
                
                	pseudowire segment z name
                	**type**\:  str
                
                

                """

                _prefix = 'pw'
                _revision = '2016-10-05'

                def __init__(self):
                    self.parent = None
                    self.name = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.name is None:
                        raise YPYModelError('Key property name is None')

                    return self.parent._common_path +'/ietf-pw:pw-segment-z[ietf-pw:name = ' + str(self.name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.name is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_pw as meta
                    return meta._meta_table['Pwe3.MsPw.MsPw_.PwSegmentZ']['meta_info']

            @property
            def _common_path(self):
                if self.name is None:
                    raise YPYModelError('Key property name is None')

                return '/ietf-pw:pwe3/ietf-pw:ms-pw/ietf-pw:ms-pw[ietf-pw:name = ' + str(self.name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.name is not None:
                    return True

                if self.pw_segment_a is not None:
                    for child_ref in self.pw_segment_a:
                        if child_ref._has_data():
                            return True

                if self.pw_segment_z is not None:
                    for child_ref in self.pw_segment_z:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_pw as meta
                return meta._meta_table['Pwe3.MsPw.MsPw_']['meta_info']

        @property
        def _common_path(self):

            return '/ietf-pw:pwe3/ietf-pw:ms-pw'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.ms_pw is not None:
                for child_ref in self.ms_pw:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_pw as meta
            return meta._meta_table['Pwe3.MsPw']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-pw:pwe3'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.ms_pw is not None and self.ms_pw._has_data():
            return True

        if self.ss_pw is not None and self.ss_pw._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_pw as meta
        return meta._meta_table['Pwe3']['meta_info']


