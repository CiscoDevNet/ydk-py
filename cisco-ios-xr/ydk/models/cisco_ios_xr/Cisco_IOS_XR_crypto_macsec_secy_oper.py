""" Cisco_IOS_XR_crypto_macsec_secy_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR crypto\-macsec\-secy package operational data.

This module contains definitions
for the following management objects\:
  macsec\: Macsec operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Macsec(Entity):
    """
    Macsec operational data
    
    .. attribute:: secy
    
    	MAC Security Entity
    	**type**\:   :py:class:`Secy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_secy_oper.Macsec.Secy>`
    
    

    """

    _prefix = 'crypto-macsec-secy-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Macsec, self).__init__()
        self._top_entity = None

        self.yang_name = "macsec"
        self.yang_parent_name = "Cisco-IOS-XR-crypto-macsec-secy-oper"

        self.secy = Macsec.Secy()
        self.secy.parent = self
        self._children_name_map["secy"] = "secy"
        self._children_yang_names.add("secy")


    class Secy(Entity):
        """
        MAC Security Entity
        
        .. attribute:: interfaces
        
        	MAC Security Data
        	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_secy_oper.Macsec.Secy.Interfaces>`
        
        

        """

        _prefix = 'crypto-macsec-secy-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Macsec.Secy, self).__init__()

            self.yang_name = "secy"
            self.yang_parent_name = "macsec"

            self.interfaces = Macsec.Secy.Interfaces()
            self.interfaces.parent = self
            self._children_name_map["interfaces"] = "interfaces"
            self._children_yang_names.add("interfaces")


        class Interfaces(Entity):
            """
            MAC Security Data
            
            .. attribute:: interface
            
            	MAC Security Data for the Interface
            	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_secy_oper.Macsec.Secy.Interfaces.Interface>`
            
            

            """

            _prefix = 'crypto-macsec-secy-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Macsec.Secy.Interfaces, self).__init__()

                self.yang_name = "interfaces"
                self.yang_parent_name = "secy"

                self.interface = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in () and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Macsec.Secy.Interfaces, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Macsec.Secy.Interfaces, self).__setattr__(name, value)


            class Interface(Entity):
                """
                MAC Security Data for the Interface
                
                .. attribute:: name  <key>
                
                	Interface Name
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: stats
                
                	MACsec Stats
                	**type**\:   :py:class:`Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_secy_oper.Macsec.Secy.Interfaces.Interface.Stats>`
                
                

                """

                _prefix = 'crypto-macsec-secy-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Macsec.Secy.Interfaces.Interface, self).__init__()

                    self.yang_name = "interface"
                    self.yang_parent_name = "interfaces"

                    self.name = YLeaf(YType.str, "name")

                    self.stats = Macsec.Secy.Interfaces.Interface.Stats()
                    self.stats.parent = self
                    self._children_name_map["stats"] = "stats"
                    self._children_yang_names.add("stats")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Macsec.Secy.Interfaces.Interface, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Macsec.Secy.Interfaces.Interface, self).__setattr__(name, value)


                class Stats(Entity):
                    """
                    MACsec Stats
                    
                    .. attribute:: intf_stats
                    
                    	Interface stats
                    	**type**\:   :py:class:`IntfStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_secy_oper.Macsec.Secy.Interfaces.Interface.Stats.IntfStats>`
                    
                    .. attribute:: rx_sc_stats
                    
                    	RX SC Stats List
                    	**type**\: list of    :py:class:`RxScStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_secy_oper.Macsec.Secy.Interfaces.Interface.Stats.RxScStats>`
                    
                    .. attribute:: tx_sc_stats
                    
                    	Tx SC Stats
                    	**type**\:   :py:class:`TxScStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_secy_oper.Macsec.Secy.Interfaces.Interface.Stats.TxScStats>`
                    
                    

                    """

                    _prefix = 'crypto-macsec-secy-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Macsec.Secy.Interfaces.Interface.Stats, self).__init__()

                        self.yang_name = "stats"
                        self.yang_parent_name = "interface"

                        self.intf_stats = Macsec.Secy.Interfaces.Interface.Stats.IntfStats()
                        self.intf_stats.parent = self
                        self._children_name_map["intf_stats"] = "intf-stats"
                        self._children_yang_names.add("intf-stats")

                        self.tx_sc_stats = Macsec.Secy.Interfaces.Interface.Stats.TxScStats()
                        self.tx_sc_stats.parent = self
                        self._children_name_map["tx_sc_stats"] = "tx-sc-stats"
                        self._children_yang_names.add("tx-sc-stats")

                        self.rx_sc_stats = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in () and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Macsec.Secy.Interfaces.Interface.Stats, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Macsec.Secy.Interfaces.Interface.Stats, self).__setattr__(name, value)


                    class IntfStats(Entity):
                        """
                        Interface stats
                        
                        .. attribute:: in_octets_decrypted
                        
                        	InOctetsDecrypted
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_octets_validated
                        
                        	InOctetsValidated
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_pkts_bad_tag
                        
                        	InPktsBadTag
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_pkts_no_sci
                        
                        	InPktsNoSCI
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_pkts_no_tag
                        
                        	InPktsNoTag
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_pkts_overrun
                        
                        	InPktsOverrun
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_pkts_unknown_sci
                        
                        	InPktsUnknownSCI
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_pkts_untagged
                        
                        	InPktsUntagged
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: out_octets_encrypted
                        
                        	OutOctetsEncrypted
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: out_octets_protected
                        
                        	OutOctetsProtected
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: out_pkts_too_long
                        
                        	OutPktsTooLong
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: out_pkts_untagged
                        
                        	OutPktsUntagged
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'crypto-macsec-secy-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Macsec.Secy.Interfaces.Interface.Stats.IntfStats, self).__init__()

                            self.yang_name = "intf-stats"
                            self.yang_parent_name = "stats"

                            self.in_octets_decrypted = YLeaf(YType.uint64, "in-octets-decrypted")

                            self.in_octets_validated = YLeaf(YType.uint64, "in-octets-validated")

                            self.in_pkts_bad_tag = YLeaf(YType.uint64, "in-pkts-bad-tag")

                            self.in_pkts_no_sci = YLeaf(YType.uint64, "in-pkts-no-sci")

                            self.in_pkts_no_tag = YLeaf(YType.uint64, "in-pkts-no-tag")

                            self.in_pkts_overrun = YLeaf(YType.uint64, "in-pkts-overrun")

                            self.in_pkts_unknown_sci = YLeaf(YType.uint64, "in-pkts-unknown-sci")

                            self.in_pkts_untagged = YLeaf(YType.uint64, "in-pkts-untagged")

                            self.out_octets_encrypted = YLeaf(YType.uint64, "out-octets-encrypted")

                            self.out_octets_protected = YLeaf(YType.uint64, "out-octets-protected")

                            self.out_pkts_too_long = YLeaf(YType.uint64, "out-pkts-too-long")

                            self.out_pkts_untagged = YLeaf(YType.uint64, "out-pkts-untagged")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("in_octets_decrypted",
                                            "in_octets_validated",
                                            "in_pkts_bad_tag",
                                            "in_pkts_no_sci",
                                            "in_pkts_no_tag",
                                            "in_pkts_overrun",
                                            "in_pkts_unknown_sci",
                                            "in_pkts_untagged",
                                            "out_octets_encrypted",
                                            "out_octets_protected",
                                            "out_pkts_too_long",
                                            "out_pkts_untagged") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Macsec.Secy.Interfaces.Interface.Stats.IntfStats, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Macsec.Secy.Interfaces.Interface.Stats.IntfStats, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.in_octets_decrypted.is_set or
                                self.in_octets_validated.is_set or
                                self.in_pkts_bad_tag.is_set or
                                self.in_pkts_no_sci.is_set or
                                self.in_pkts_no_tag.is_set or
                                self.in_pkts_overrun.is_set or
                                self.in_pkts_unknown_sci.is_set or
                                self.in_pkts_untagged.is_set or
                                self.out_octets_encrypted.is_set or
                                self.out_octets_protected.is_set or
                                self.out_pkts_too_long.is_set or
                                self.out_pkts_untagged.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.in_octets_decrypted.yfilter != YFilter.not_set or
                                self.in_octets_validated.yfilter != YFilter.not_set or
                                self.in_pkts_bad_tag.yfilter != YFilter.not_set or
                                self.in_pkts_no_sci.yfilter != YFilter.not_set or
                                self.in_pkts_no_tag.yfilter != YFilter.not_set or
                                self.in_pkts_overrun.yfilter != YFilter.not_set or
                                self.in_pkts_unknown_sci.yfilter != YFilter.not_set or
                                self.in_pkts_untagged.yfilter != YFilter.not_set or
                                self.out_octets_encrypted.yfilter != YFilter.not_set or
                                self.out_octets_protected.yfilter != YFilter.not_set or
                                self.out_pkts_too_long.yfilter != YFilter.not_set or
                                self.out_pkts_untagged.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "intf-stats" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.in_octets_decrypted.is_set or self.in_octets_decrypted.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.in_octets_decrypted.get_name_leafdata())
                            if (self.in_octets_validated.is_set or self.in_octets_validated.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.in_octets_validated.get_name_leafdata())
                            if (self.in_pkts_bad_tag.is_set or self.in_pkts_bad_tag.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.in_pkts_bad_tag.get_name_leafdata())
                            if (self.in_pkts_no_sci.is_set or self.in_pkts_no_sci.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.in_pkts_no_sci.get_name_leafdata())
                            if (self.in_pkts_no_tag.is_set or self.in_pkts_no_tag.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.in_pkts_no_tag.get_name_leafdata())
                            if (self.in_pkts_overrun.is_set or self.in_pkts_overrun.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.in_pkts_overrun.get_name_leafdata())
                            if (self.in_pkts_unknown_sci.is_set or self.in_pkts_unknown_sci.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.in_pkts_unknown_sci.get_name_leafdata())
                            if (self.in_pkts_untagged.is_set or self.in_pkts_untagged.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.in_pkts_untagged.get_name_leafdata())
                            if (self.out_octets_encrypted.is_set or self.out_octets_encrypted.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.out_octets_encrypted.get_name_leafdata())
                            if (self.out_octets_protected.is_set or self.out_octets_protected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.out_octets_protected.get_name_leafdata())
                            if (self.out_pkts_too_long.is_set or self.out_pkts_too_long.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.out_pkts_too_long.get_name_leafdata())
                            if (self.out_pkts_untagged.is_set or self.out_pkts_untagged.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.out_pkts_untagged.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "in-octets-decrypted" or name == "in-octets-validated" or name == "in-pkts-bad-tag" or name == "in-pkts-no-sci" or name == "in-pkts-no-tag" or name == "in-pkts-overrun" or name == "in-pkts-unknown-sci" or name == "in-pkts-untagged" or name == "out-octets-encrypted" or name == "out-octets-protected" or name == "out-pkts-too-long" or name == "out-pkts-untagged"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "in-octets-decrypted"):
                                self.in_octets_decrypted = value
                                self.in_octets_decrypted.value_namespace = name_space
                                self.in_octets_decrypted.value_namespace_prefix = name_space_prefix
                            if(value_path == "in-octets-validated"):
                                self.in_octets_validated = value
                                self.in_octets_validated.value_namespace = name_space
                                self.in_octets_validated.value_namespace_prefix = name_space_prefix
                            if(value_path == "in-pkts-bad-tag"):
                                self.in_pkts_bad_tag = value
                                self.in_pkts_bad_tag.value_namespace = name_space
                                self.in_pkts_bad_tag.value_namespace_prefix = name_space_prefix
                            if(value_path == "in-pkts-no-sci"):
                                self.in_pkts_no_sci = value
                                self.in_pkts_no_sci.value_namespace = name_space
                                self.in_pkts_no_sci.value_namespace_prefix = name_space_prefix
                            if(value_path == "in-pkts-no-tag"):
                                self.in_pkts_no_tag = value
                                self.in_pkts_no_tag.value_namespace = name_space
                                self.in_pkts_no_tag.value_namespace_prefix = name_space_prefix
                            if(value_path == "in-pkts-overrun"):
                                self.in_pkts_overrun = value
                                self.in_pkts_overrun.value_namespace = name_space
                                self.in_pkts_overrun.value_namespace_prefix = name_space_prefix
                            if(value_path == "in-pkts-unknown-sci"):
                                self.in_pkts_unknown_sci = value
                                self.in_pkts_unknown_sci.value_namespace = name_space
                                self.in_pkts_unknown_sci.value_namespace_prefix = name_space_prefix
                            if(value_path == "in-pkts-untagged"):
                                self.in_pkts_untagged = value
                                self.in_pkts_untagged.value_namespace = name_space
                                self.in_pkts_untagged.value_namespace_prefix = name_space_prefix
                            if(value_path == "out-octets-encrypted"):
                                self.out_octets_encrypted = value
                                self.out_octets_encrypted.value_namespace = name_space
                                self.out_octets_encrypted.value_namespace_prefix = name_space_prefix
                            if(value_path == "out-octets-protected"):
                                self.out_octets_protected = value
                                self.out_octets_protected.value_namespace = name_space
                                self.out_octets_protected.value_namespace_prefix = name_space_prefix
                            if(value_path == "out-pkts-too-long"):
                                self.out_pkts_too_long = value
                                self.out_pkts_too_long.value_namespace = name_space
                                self.out_pkts_too_long.value_namespace_prefix = name_space_prefix
                            if(value_path == "out-pkts-untagged"):
                                self.out_pkts_untagged = value
                                self.out_pkts_untagged.value_namespace = name_space
                                self.out_pkts_untagged.value_namespace_prefix = name_space_prefix


                    class TxScStats(Entity):
                        """
                        Tx SC Stats
                        
                        .. attribute:: out_octets_encrypted
                        
                        	OutOctetsEncrypted
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: out_octets_protected
                        
                        	OutOctetsProtected
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: out_pkts_encrypted
                        
                        	OutPktsEncrypted
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: out_pkts_protected
                        
                        	OutPktsProtected
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: out_pkts_too_long
                        
                        	OutPktsTooLong
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: tx_sci
                        
                        	Tx SCI
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: txsa_stat
                        
                        	tx sa stats
                        	**type**\: list of    :py:class:`TxsaStat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_secy_oper.Macsec.Secy.Interfaces.Interface.Stats.TxScStats.TxsaStat>`
                        
                        

                        """

                        _prefix = 'crypto-macsec-secy-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Macsec.Secy.Interfaces.Interface.Stats.TxScStats, self).__init__()

                            self.yang_name = "tx-sc-stats"
                            self.yang_parent_name = "stats"

                            self.out_octets_encrypted = YLeaf(YType.uint64, "out-octets-encrypted")

                            self.out_octets_protected = YLeaf(YType.uint64, "out-octets-protected")

                            self.out_pkts_encrypted = YLeaf(YType.uint64, "out-pkts-encrypted")

                            self.out_pkts_protected = YLeaf(YType.uint64, "out-pkts-protected")

                            self.out_pkts_too_long = YLeaf(YType.uint64, "out-pkts-too-long")

                            self.tx_sci = YLeaf(YType.uint64, "tx-sci")

                            self.txsa_stat = YList(self)

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("out_octets_encrypted",
                                            "out_octets_protected",
                                            "out_pkts_encrypted",
                                            "out_pkts_protected",
                                            "out_pkts_too_long",
                                            "tx_sci") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Macsec.Secy.Interfaces.Interface.Stats.TxScStats, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Macsec.Secy.Interfaces.Interface.Stats.TxScStats, self).__setattr__(name, value)


                        class TxsaStat(Entity):
                            """
                            tx sa stats
                            
                            .. attribute:: next_pn
                            
                            	NextPN
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: out_pkts_encrypted
                            
                            	OutPktsEncrypted
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: out_pkts_protected
                            
                            	OutPktsProtected
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'crypto-macsec-secy-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Macsec.Secy.Interfaces.Interface.Stats.TxScStats.TxsaStat, self).__init__()

                                self.yang_name = "txsa-stat"
                                self.yang_parent_name = "tx-sc-stats"

                                self.next_pn = YLeaf(YType.uint64, "next-pn")

                                self.out_pkts_encrypted = YLeaf(YType.uint64, "out-pkts-encrypted")

                                self.out_pkts_protected = YLeaf(YType.uint64, "out-pkts-protected")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("next_pn",
                                                "out_pkts_encrypted",
                                                "out_pkts_protected") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Macsec.Secy.Interfaces.Interface.Stats.TxScStats.TxsaStat, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Macsec.Secy.Interfaces.Interface.Stats.TxScStats.TxsaStat, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.next_pn.is_set or
                                    self.out_pkts_encrypted.is_set or
                                    self.out_pkts_protected.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.next_pn.yfilter != YFilter.not_set or
                                    self.out_pkts_encrypted.yfilter != YFilter.not_set or
                                    self.out_pkts_protected.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "txsa-stat" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.next_pn.is_set or self.next_pn.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.next_pn.get_name_leafdata())
                                if (self.out_pkts_encrypted.is_set or self.out_pkts_encrypted.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.out_pkts_encrypted.get_name_leafdata())
                                if (self.out_pkts_protected.is_set or self.out_pkts_protected.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.out_pkts_protected.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "next-pn" or name == "out-pkts-encrypted" or name == "out-pkts-protected"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "next-pn"):
                                    self.next_pn = value
                                    self.next_pn.value_namespace = name_space
                                    self.next_pn.value_namespace_prefix = name_space_prefix
                                if(value_path == "out-pkts-encrypted"):
                                    self.out_pkts_encrypted = value
                                    self.out_pkts_encrypted.value_namespace = name_space
                                    self.out_pkts_encrypted.value_namespace_prefix = name_space_prefix
                                if(value_path == "out-pkts-protected"):
                                    self.out_pkts_protected = value
                                    self.out_pkts_protected.value_namespace = name_space
                                    self.out_pkts_protected.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.txsa_stat:
                                if (c.has_data()):
                                    return True
                            return (
                                self.out_octets_encrypted.is_set or
                                self.out_octets_protected.is_set or
                                self.out_pkts_encrypted.is_set or
                                self.out_pkts_protected.is_set or
                                self.out_pkts_too_long.is_set or
                                self.tx_sci.is_set)

                        def has_operation(self):
                            for c in self.txsa_stat:
                                if (c.has_operation()):
                                    return True
                            return (
                                self.yfilter != YFilter.not_set or
                                self.out_octets_encrypted.yfilter != YFilter.not_set or
                                self.out_octets_protected.yfilter != YFilter.not_set or
                                self.out_pkts_encrypted.yfilter != YFilter.not_set or
                                self.out_pkts_protected.yfilter != YFilter.not_set or
                                self.out_pkts_too_long.yfilter != YFilter.not_set or
                                self.tx_sci.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "tx-sc-stats" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.out_octets_encrypted.is_set or self.out_octets_encrypted.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.out_octets_encrypted.get_name_leafdata())
                            if (self.out_octets_protected.is_set or self.out_octets_protected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.out_octets_protected.get_name_leafdata())
                            if (self.out_pkts_encrypted.is_set or self.out_pkts_encrypted.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.out_pkts_encrypted.get_name_leafdata())
                            if (self.out_pkts_protected.is_set or self.out_pkts_protected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.out_pkts_protected.get_name_leafdata())
                            if (self.out_pkts_too_long.is_set or self.out_pkts_too_long.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.out_pkts_too_long.get_name_leafdata())
                            if (self.tx_sci.is_set or self.tx_sci.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.tx_sci.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "txsa-stat"):
                                for c in self.txsa_stat:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Macsec.Secy.Interfaces.Interface.Stats.TxScStats.TxsaStat()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.txsa_stat.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "txsa-stat" or name == "out-octets-encrypted" or name == "out-octets-protected" or name == "out-pkts-encrypted" or name == "out-pkts-protected" or name == "out-pkts-too-long" or name == "tx-sci"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "out-octets-encrypted"):
                                self.out_octets_encrypted = value
                                self.out_octets_encrypted.value_namespace = name_space
                                self.out_octets_encrypted.value_namespace_prefix = name_space_prefix
                            if(value_path == "out-octets-protected"):
                                self.out_octets_protected = value
                                self.out_octets_protected.value_namespace = name_space
                                self.out_octets_protected.value_namespace_prefix = name_space_prefix
                            if(value_path == "out-pkts-encrypted"):
                                self.out_pkts_encrypted = value
                                self.out_pkts_encrypted.value_namespace = name_space
                                self.out_pkts_encrypted.value_namespace_prefix = name_space_prefix
                            if(value_path == "out-pkts-protected"):
                                self.out_pkts_protected = value
                                self.out_pkts_protected.value_namespace = name_space
                                self.out_pkts_protected.value_namespace_prefix = name_space_prefix
                            if(value_path == "out-pkts-too-long"):
                                self.out_pkts_too_long = value
                                self.out_pkts_too_long.value_namespace = name_space
                                self.out_pkts_too_long.value_namespace_prefix = name_space_prefix
                            if(value_path == "tx-sci"):
                                self.tx_sci = value
                                self.tx_sci.value_namespace = name_space
                                self.tx_sci.value_namespace_prefix = name_space_prefix


                    class RxScStats(Entity):
                        """
                        RX SC Stats List
                        
                        .. attribute:: in_octets_decrypted
                        
                        	InOctetsDecrypted
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_octets_validated
                        
                        	InOctetsValidated
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_pkts_delayed
                        
                        	InPktsDelayed
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_pkts_invalid
                        
                        	InPktsInvalid
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_pkts_late
                        
                        	InPktsLate
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_pkts_not_using_sa
                        
                        	InPktsNotUsingSA
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_pkts_not_valid
                        
                        	InPktsNotValid
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_pkts_ok
                        
                        	InPktsOK
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_pkts_unchecked
                        
                        	InPktsUnchecked
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_pkts_untagged_hit
                        
                        	InPktsUntaggedHit
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_pkts_unused_sa
                        
                        	InPktsUnusedSA
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: rx_sci
                        
                        	Rx SCI
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: rxsa_stat
                        
                        	rxsa stats
                        	**type**\: list of    :py:class:`RxsaStat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_secy_oper.Macsec.Secy.Interfaces.Interface.Stats.RxScStats.RxsaStat>`
                        
                        

                        """

                        _prefix = 'crypto-macsec-secy-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Macsec.Secy.Interfaces.Interface.Stats.RxScStats, self).__init__()

                            self.yang_name = "rx-sc-stats"
                            self.yang_parent_name = "stats"

                            self.in_octets_decrypted = YLeaf(YType.uint64, "in-octets-decrypted")

                            self.in_octets_validated = YLeaf(YType.uint64, "in-octets-validated")

                            self.in_pkts_delayed = YLeaf(YType.uint64, "in-pkts-delayed")

                            self.in_pkts_invalid = YLeaf(YType.uint64, "in-pkts-invalid")

                            self.in_pkts_late = YLeaf(YType.uint64, "in-pkts-late")

                            self.in_pkts_not_using_sa = YLeaf(YType.uint64, "in-pkts-not-using-sa")

                            self.in_pkts_not_valid = YLeaf(YType.uint64, "in-pkts-not-valid")

                            self.in_pkts_ok = YLeaf(YType.uint64, "in-pkts-ok")

                            self.in_pkts_unchecked = YLeaf(YType.uint64, "in-pkts-unchecked")

                            self.in_pkts_untagged_hit = YLeaf(YType.uint64, "in-pkts-untagged-hit")

                            self.in_pkts_unused_sa = YLeaf(YType.uint64, "in-pkts-unused-sa")

                            self.rx_sci = YLeaf(YType.uint64, "rx-sci")

                            self.rxsa_stat = YList(self)

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("in_octets_decrypted",
                                            "in_octets_validated",
                                            "in_pkts_delayed",
                                            "in_pkts_invalid",
                                            "in_pkts_late",
                                            "in_pkts_not_using_sa",
                                            "in_pkts_not_valid",
                                            "in_pkts_ok",
                                            "in_pkts_unchecked",
                                            "in_pkts_untagged_hit",
                                            "in_pkts_unused_sa",
                                            "rx_sci") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Macsec.Secy.Interfaces.Interface.Stats.RxScStats, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Macsec.Secy.Interfaces.Interface.Stats.RxScStats, self).__setattr__(name, value)


                        class RxsaStat(Entity):
                            """
                            rxsa stats
                            
                            .. attribute:: in_pkts_invalid
                            
                            	InPktsInvalid
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in_pkts_not_using_sa
                            
                            	InPktsNotUsingSA
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in_pkts_not_valid
                            
                            	InPktsNotValid
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in_pkts_ok
                            
                            	InPktsOK
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in_pkts_unused_sa
                            
                            	InPktsUnusedSA
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: next_pn
                            
                            	NextPN
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'crypto-macsec-secy-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Macsec.Secy.Interfaces.Interface.Stats.RxScStats.RxsaStat, self).__init__()

                                self.yang_name = "rxsa-stat"
                                self.yang_parent_name = "rx-sc-stats"

                                self.in_pkts_invalid = YLeaf(YType.uint64, "in-pkts-invalid")

                                self.in_pkts_not_using_sa = YLeaf(YType.uint64, "in-pkts-not-using-sa")

                                self.in_pkts_not_valid = YLeaf(YType.uint64, "in-pkts-not-valid")

                                self.in_pkts_ok = YLeaf(YType.uint64, "in-pkts-ok")

                                self.in_pkts_unused_sa = YLeaf(YType.uint64, "in-pkts-unused-sa")

                                self.next_pn = YLeaf(YType.uint64, "next-pn")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("in_pkts_invalid",
                                                "in_pkts_not_using_sa",
                                                "in_pkts_not_valid",
                                                "in_pkts_ok",
                                                "in_pkts_unused_sa",
                                                "next_pn") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Macsec.Secy.Interfaces.Interface.Stats.RxScStats.RxsaStat, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Macsec.Secy.Interfaces.Interface.Stats.RxScStats.RxsaStat, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.in_pkts_invalid.is_set or
                                    self.in_pkts_not_using_sa.is_set or
                                    self.in_pkts_not_valid.is_set or
                                    self.in_pkts_ok.is_set or
                                    self.in_pkts_unused_sa.is_set or
                                    self.next_pn.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.in_pkts_invalid.yfilter != YFilter.not_set or
                                    self.in_pkts_not_using_sa.yfilter != YFilter.not_set or
                                    self.in_pkts_not_valid.yfilter != YFilter.not_set or
                                    self.in_pkts_ok.yfilter != YFilter.not_set or
                                    self.in_pkts_unused_sa.yfilter != YFilter.not_set or
                                    self.next_pn.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "rxsa-stat" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.in_pkts_invalid.is_set or self.in_pkts_invalid.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.in_pkts_invalid.get_name_leafdata())
                                if (self.in_pkts_not_using_sa.is_set or self.in_pkts_not_using_sa.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.in_pkts_not_using_sa.get_name_leafdata())
                                if (self.in_pkts_not_valid.is_set or self.in_pkts_not_valid.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.in_pkts_not_valid.get_name_leafdata())
                                if (self.in_pkts_ok.is_set or self.in_pkts_ok.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.in_pkts_ok.get_name_leafdata())
                                if (self.in_pkts_unused_sa.is_set or self.in_pkts_unused_sa.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.in_pkts_unused_sa.get_name_leafdata())
                                if (self.next_pn.is_set or self.next_pn.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.next_pn.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "in-pkts-invalid" or name == "in-pkts-not-using-sa" or name == "in-pkts-not-valid" or name == "in-pkts-ok" or name == "in-pkts-unused-sa" or name == "next-pn"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "in-pkts-invalid"):
                                    self.in_pkts_invalid = value
                                    self.in_pkts_invalid.value_namespace = name_space
                                    self.in_pkts_invalid.value_namespace_prefix = name_space_prefix
                                if(value_path == "in-pkts-not-using-sa"):
                                    self.in_pkts_not_using_sa = value
                                    self.in_pkts_not_using_sa.value_namespace = name_space
                                    self.in_pkts_not_using_sa.value_namespace_prefix = name_space_prefix
                                if(value_path == "in-pkts-not-valid"):
                                    self.in_pkts_not_valid = value
                                    self.in_pkts_not_valid.value_namespace = name_space
                                    self.in_pkts_not_valid.value_namespace_prefix = name_space_prefix
                                if(value_path == "in-pkts-ok"):
                                    self.in_pkts_ok = value
                                    self.in_pkts_ok.value_namespace = name_space
                                    self.in_pkts_ok.value_namespace_prefix = name_space_prefix
                                if(value_path == "in-pkts-unused-sa"):
                                    self.in_pkts_unused_sa = value
                                    self.in_pkts_unused_sa.value_namespace = name_space
                                    self.in_pkts_unused_sa.value_namespace_prefix = name_space_prefix
                                if(value_path == "next-pn"):
                                    self.next_pn = value
                                    self.next_pn.value_namespace = name_space
                                    self.next_pn.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.rxsa_stat:
                                if (c.has_data()):
                                    return True
                            return (
                                self.in_octets_decrypted.is_set or
                                self.in_octets_validated.is_set or
                                self.in_pkts_delayed.is_set or
                                self.in_pkts_invalid.is_set or
                                self.in_pkts_late.is_set or
                                self.in_pkts_not_using_sa.is_set or
                                self.in_pkts_not_valid.is_set or
                                self.in_pkts_ok.is_set or
                                self.in_pkts_unchecked.is_set or
                                self.in_pkts_untagged_hit.is_set or
                                self.in_pkts_unused_sa.is_set or
                                self.rx_sci.is_set)

                        def has_operation(self):
                            for c in self.rxsa_stat:
                                if (c.has_operation()):
                                    return True
                            return (
                                self.yfilter != YFilter.not_set or
                                self.in_octets_decrypted.yfilter != YFilter.not_set or
                                self.in_octets_validated.yfilter != YFilter.not_set or
                                self.in_pkts_delayed.yfilter != YFilter.not_set or
                                self.in_pkts_invalid.yfilter != YFilter.not_set or
                                self.in_pkts_late.yfilter != YFilter.not_set or
                                self.in_pkts_not_using_sa.yfilter != YFilter.not_set or
                                self.in_pkts_not_valid.yfilter != YFilter.not_set or
                                self.in_pkts_ok.yfilter != YFilter.not_set or
                                self.in_pkts_unchecked.yfilter != YFilter.not_set or
                                self.in_pkts_untagged_hit.yfilter != YFilter.not_set or
                                self.in_pkts_unused_sa.yfilter != YFilter.not_set or
                                self.rx_sci.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "rx-sc-stats" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.in_octets_decrypted.is_set or self.in_octets_decrypted.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.in_octets_decrypted.get_name_leafdata())
                            if (self.in_octets_validated.is_set or self.in_octets_validated.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.in_octets_validated.get_name_leafdata())
                            if (self.in_pkts_delayed.is_set or self.in_pkts_delayed.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.in_pkts_delayed.get_name_leafdata())
                            if (self.in_pkts_invalid.is_set or self.in_pkts_invalid.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.in_pkts_invalid.get_name_leafdata())
                            if (self.in_pkts_late.is_set or self.in_pkts_late.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.in_pkts_late.get_name_leafdata())
                            if (self.in_pkts_not_using_sa.is_set or self.in_pkts_not_using_sa.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.in_pkts_not_using_sa.get_name_leafdata())
                            if (self.in_pkts_not_valid.is_set or self.in_pkts_not_valid.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.in_pkts_not_valid.get_name_leafdata())
                            if (self.in_pkts_ok.is_set or self.in_pkts_ok.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.in_pkts_ok.get_name_leafdata())
                            if (self.in_pkts_unchecked.is_set or self.in_pkts_unchecked.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.in_pkts_unchecked.get_name_leafdata())
                            if (self.in_pkts_untagged_hit.is_set or self.in_pkts_untagged_hit.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.in_pkts_untagged_hit.get_name_leafdata())
                            if (self.in_pkts_unused_sa.is_set or self.in_pkts_unused_sa.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.in_pkts_unused_sa.get_name_leafdata())
                            if (self.rx_sci.is_set or self.rx_sci.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.rx_sci.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "rxsa-stat"):
                                for c in self.rxsa_stat:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Macsec.Secy.Interfaces.Interface.Stats.RxScStats.RxsaStat()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.rxsa_stat.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "rxsa-stat" or name == "in-octets-decrypted" or name == "in-octets-validated" or name == "in-pkts-delayed" or name == "in-pkts-invalid" or name == "in-pkts-late" or name == "in-pkts-not-using-sa" or name == "in-pkts-not-valid" or name == "in-pkts-ok" or name == "in-pkts-unchecked" or name == "in-pkts-untagged-hit" or name == "in-pkts-unused-sa" or name == "rx-sci"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "in-octets-decrypted"):
                                self.in_octets_decrypted = value
                                self.in_octets_decrypted.value_namespace = name_space
                                self.in_octets_decrypted.value_namespace_prefix = name_space_prefix
                            if(value_path == "in-octets-validated"):
                                self.in_octets_validated = value
                                self.in_octets_validated.value_namespace = name_space
                                self.in_octets_validated.value_namespace_prefix = name_space_prefix
                            if(value_path == "in-pkts-delayed"):
                                self.in_pkts_delayed = value
                                self.in_pkts_delayed.value_namespace = name_space
                                self.in_pkts_delayed.value_namespace_prefix = name_space_prefix
                            if(value_path == "in-pkts-invalid"):
                                self.in_pkts_invalid = value
                                self.in_pkts_invalid.value_namespace = name_space
                                self.in_pkts_invalid.value_namespace_prefix = name_space_prefix
                            if(value_path == "in-pkts-late"):
                                self.in_pkts_late = value
                                self.in_pkts_late.value_namespace = name_space
                                self.in_pkts_late.value_namespace_prefix = name_space_prefix
                            if(value_path == "in-pkts-not-using-sa"):
                                self.in_pkts_not_using_sa = value
                                self.in_pkts_not_using_sa.value_namespace = name_space
                                self.in_pkts_not_using_sa.value_namespace_prefix = name_space_prefix
                            if(value_path == "in-pkts-not-valid"):
                                self.in_pkts_not_valid = value
                                self.in_pkts_not_valid.value_namespace = name_space
                                self.in_pkts_not_valid.value_namespace_prefix = name_space_prefix
                            if(value_path == "in-pkts-ok"):
                                self.in_pkts_ok = value
                                self.in_pkts_ok.value_namespace = name_space
                                self.in_pkts_ok.value_namespace_prefix = name_space_prefix
                            if(value_path == "in-pkts-unchecked"):
                                self.in_pkts_unchecked = value
                                self.in_pkts_unchecked.value_namespace = name_space
                                self.in_pkts_unchecked.value_namespace_prefix = name_space_prefix
                            if(value_path == "in-pkts-untagged-hit"):
                                self.in_pkts_untagged_hit = value
                                self.in_pkts_untagged_hit.value_namespace = name_space
                                self.in_pkts_untagged_hit.value_namespace_prefix = name_space_prefix
                            if(value_path == "in-pkts-unused-sa"):
                                self.in_pkts_unused_sa = value
                                self.in_pkts_unused_sa.value_namespace = name_space
                                self.in_pkts_unused_sa.value_namespace_prefix = name_space_prefix
                            if(value_path == "rx-sci"):
                                self.rx_sci = value
                                self.rx_sci.value_namespace = name_space
                                self.rx_sci.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.rx_sc_stats:
                            if (c.has_data()):
                                return True
                        return (
                            (self.intf_stats is not None and self.intf_stats.has_data()) or
                            (self.tx_sc_stats is not None and self.tx_sc_stats.has_data()))

                    def has_operation(self):
                        for c in self.rx_sc_stats:
                            if (c.has_operation()):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.intf_stats is not None and self.intf_stats.has_operation()) or
                            (self.tx_sc_stats is not None and self.tx_sc_stats.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "stats" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "intf-stats"):
                            if (self.intf_stats is None):
                                self.intf_stats = Macsec.Secy.Interfaces.Interface.Stats.IntfStats()
                                self.intf_stats.parent = self
                                self._children_name_map["intf_stats"] = "intf-stats"
                            return self.intf_stats

                        if (child_yang_name == "rx-sc-stats"):
                            for c in self.rx_sc_stats:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Macsec.Secy.Interfaces.Interface.Stats.RxScStats()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.rx_sc_stats.append(c)
                            return c

                        if (child_yang_name == "tx-sc-stats"):
                            if (self.tx_sc_stats is None):
                                self.tx_sc_stats = Macsec.Secy.Interfaces.Interface.Stats.TxScStats()
                                self.tx_sc_stats.parent = self
                                self._children_name_map["tx_sc_stats"] = "tx-sc-stats"
                            return self.tx_sc_stats

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "intf-stats" or name == "rx-sc-stats" or name == "tx-sc-stats"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        self.name.is_set or
                        (self.stats is not None and self.stats.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.name.yfilter != YFilter.not_set or
                        (self.stats is not None and self.stats.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "interface" + "[name='" + self.name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-crypto-macsec-secy-oper:macsec/secy/interfaces/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.name.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "stats"):
                        if (self.stats is None):
                            self.stats = Macsec.Secy.Interfaces.Interface.Stats()
                            self.stats.parent = self
                            self._children_name_map["stats"] = "stats"
                        return self.stats

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "stats" or name == "name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "name"):
                        self.name = value
                        self.name.value_namespace = name_space
                        self.name.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.interface:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.interface:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "interfaces" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-crypto-macsec-secy-oper:macsec/secy/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "interface"):
                    for c in self.interface:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Macsec.Secy.Interfaces.Interface()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.interface.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "interface"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (self.interfaces is not None and self.interfaces.has_data())

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.interfaces is not None and self.interfaces.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "secy" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-crypto-macsec-secy-oper:macsec/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "interfaces"):
                if (self.interfaces is None):
                    self.interfaces = Macsec.Secy.Interfaces()
                    self.interfaces.parent = self
                    self._children_name_map["interfaces"] = "interfaces"
                return self.interfaces

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "interfaces"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.secy is not None and self.secy.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.secy is not None and self.secy.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-crypto-macsec-secy-oper:macsec" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "secy"):
            if (self.secy is None):
                self.secy = Macsec.Secy()
                self.secy.parent = self
                self._children_name_map["secy"] = "secy"
            return self.secy

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "secy"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Macsec()
        return self._top_entity

