""" Cisco_IOS_XR_fia_internal_tcam_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR fia\-internal\-tcam package operational data.

This module contains definitions
for the following management objects\:
  controller\: Controller Resources

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class Controller(object):
    """
    Controller Resources
    
    .. attribute:: dpa
    
    	Controller DPA operational data
    	**type**\:   :py:class:`Dpa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_internal_tcam_oper.Controller.Dpa>`
    
    

    """

    _prefix = 'fia-internal-tcam-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.dpa = Controller.Dpa()
        self.dpa.parent = self


    class Dpa(object):
        """
        Controller DPA operational data
        
        .. attribute:: nodes
        
        	DPA data for available nodes
        	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_internal_tcam_oper.Controller.Dpa.Nodes>`
        
        

        """

        _prefix = 'fia-internal-tcam-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.nodes = Controller.Dpa.Nodes()
            self.nodes.parent = self


        class Nodes(object):
            """
            DPA data for available nodes
            
            .. attribute:: node
            
            	DPA operational data for a particular node
            	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_internal_tcam_oper.Controller.Dpa.Nodes.Node>`
            
            

            """

            _prefix = 'fia-internal-tcam-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.node = YList()
                self.node.parent = self
                self.node.name = 'node'


            class Node(object):
                """
                DPA operational data for a particular node
                
                .. attribute:: node_name  <key>
                
                	Node ID
                	**type**\:  str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                .. attribute:: internal_tcam_resources
                
                	Internal TCAM Resource Information
                	**type**\:   :py:class:`InternalTcamResources <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_internal_tcam_oper.Controller.Dpa.Nodes.Node.InternalTcamResources>`
                
                

                """

                _prefix = 'fia-internal-tcam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.node_name = None
                    self.internal_tcam_resources = Controller.Dpa.Nodes.Node.InternalTcamResources()
                    self.internal_tcam_resources.parent = self


                class InternalTcamResources(object):
                    """
                    Internal TCAM Resource Information
                    
                    .. attribute:: npu_tcam
                    
                    	npu tcam
                    	**type**\: list of    :py:class:`NpuTcam <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_internal_tcam_oper.Controller.Dpa.Nodes.Node.InternalTcamResources.NpuTcam>`
                    
                    

                    """

                    _prefix = 'fia-internal-tcam-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.npu_tcam = YList()
                        self.npu_tcam.parent = self
                        self.npu_tcam.name = 'npu_tcam'


                    class NpuTcam(object):
                        """
                        npu tcam
                        
                        .. attribute:: npu_id
                        
                        	npu id
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: tcam_bank
                        
                        	tcam bank
                        	**type**\: list of    :py:class:`TcamBank <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_internal_tcam_oper.Controller.Dpa.Nodes.Node.InternalTcamResources.NpuTcam.TcamBank>`
                        
                        

                        """

                        _prefix = 'fia-internal-tcam-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.npu_id = None
                            self.tcam_bank = YList()
                            self.tcam_bank.parent = self
                            self.tcam_bank.name = 'tcam_bank'


                        class TcamBank(object):
                            """
                            tcam bank
                            
                            .. attribute:: bank_db
                            
                            	bank db
                            	**type**\: list of    :py:class:`BankDb <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_internal_tcam_oper.Controller.Dpa.Nodes.Node.InternalTcamResources.NpuTcam.TcamBank.BankDb>`
                            
                            .. attribute:: bank_free_entries
                            
                            	bank free entries
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: bank_id
                            
                            	bank id
                            	**type**\:  str
                            
                            .. attribute:: bank_inuse_entries
                            
                            	bank inuse entries
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: bank_key_size
                            
                            	bank key size
                            	**type**\:  str
                            
                            .. attribute:: nof_dbs
                            
                            	nof dbs
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: owner
                            
                            	owner
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'fia-internal-tcam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.bank_db = YList()
                                self.bank_db.parent = self
                                self.bank_db.name = 'bank_db'
                                self.bank_free_entries = None
                                self.bank_id = None
                                self.bank_inuse_entries = None
                                self.bank_key_size = None
                                self.nof_dbs = None
                                self.owner = None


                            class BankDb(object):
                                """
                                bank db
                                
                                .. attribute:: db_id
                                
                                	db id
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: db_inuse_entries
                                
                                	db inuse entries
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: db_prefix
                                
                                	db prefix
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'fia-internal-tcam-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.db_id = None
                                    self.db_inuse_entries = None
                                    self.db_prefix = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-fia-internal-tcam-oper:bank-db'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.db_id is not None:
                                        return True

                                    if self.db_inuse_entries is not None:
                                        return True

                                    if self.db_prefix is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fia_internal_tcam_oper as meta
                                    return meta._meta_table['Controller.Dpa.Nodes.Node.InternalTcamResources.NpuTcam.TcamBank.BankDb']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-fia-internal-tcam-oper:tcam-bank'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.bank_db is not None:
                                    for child_ref in self.bank_db:
                                        if child_ref._has_data():
                                            return True

                                if self.bank_free_entries is not None:
                                    return True

                                if self.bank_id is not None:
                                    return True

                                if self.bank_inuse_entries is not None:
                                    return True

                                if self.bank_key_size is not None:
                                    return True

                                if self.nof_dbs is not None:
                                    return True

                                if self.owner is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fia_internal_tcam_oper as meta
                                return meta._meta_table['Controller.Dpa.Nodes.Node.InternalTcamResources.NpuTcam.TcamBank']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-fia-internal-tcam-oper:npu-tcam'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.npu_id is not None:
                                return True

                            if self.tcam_bank is not None:
                                for child_ref in self.tcam_bank:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fia_internal_tcam_oper as meta
                            return meta._meta_table['Controller.Dpa.Nodes.Node.InternalTcamResources.NpuTcam']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-fia-internal-tcam-oper:internal-tcam-resources'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.npu_tcam is not None:
                            for child_ref in self.npu_tcam:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fia_internal_tcam_oper as meta
                        return meta._meta_table['Controller.Dpa.Nodes.Node.InternalTcamResources']['meta_info']

                @property
                def _common_path(self):
                    if self.node_name is None:
                        raise YPYModelError('Key property node_name is None')

                    return '/Cisco-IOS-XR-fia-internal-tcam-oper:controller/Cisco-IOS-XR-fia-internal-tcam-oper:dpa/Cisco-IOS-XR-fia-internal-tcam-oper:nodes/Cisco-IOS-XR-fia-internal-tcam-oper:node[Cisco-IOS-XR-fia-internal-tcam-oper:node-name = ' + str(self.node_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.node_name is not None:
                        return True

                    if self.internal_tcam_resources is not None and self.internal_tcam_resources._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fia_internal_tcam_oper as meta
                    return meta._meta_table['Controller.Dpa.Nodes.Node']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-fia-internal-tcam-oper:controller/Cisco-IOS-XR-fia-internal-tcam-oper:dpa/Cisco-IOS-XR-fia-internal-tcam-oper:nodes'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.node is not None:
                    for child_ref in self.node:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fia_internal_tcam_oper as meta
                return meta._meta_table['Controller.Dpa.Nodes']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-fia-internal-tcam-oper:controller/Cisco-IOS-XR-fia-internal-tcam-oper:dpa'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.nodes is not None and self.nodes._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fia_internal_tcam_oper as meta
            return meta._meta_table['Controller.Dpa']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-fia-internal-tcam-oper:controller'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.dpa is not None and self.dpa._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fia_internal_tcam_oper as meta
        return meta._meta_table['Controller']['meta_info']


