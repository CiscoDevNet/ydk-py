""" CLAB_DEF_MIB 

This MIB module defines the namespace organization for the
CableLabs enterprise OID registry.

Copyright 1999\-2012 Cable Television Laboratories, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class CLABDEFMIB(Entity):
    """
    
    
    .. attribute:: clabseccertobject
    
    	
    	**type**\:  :py:class:`ClabSecCertObject <ydk.models.cisco_ios_xe.CLAB_DEF_MIB.CLABDEFMIB.ClabSecCertObject>`
    
    	**config**\: False
    
    

    """

    _prefix = 'CLAB-DEF-MIB'
    _revision = '2012-08-09'

    def __init__(self):
        super(CLABDEFMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CLAB-DEF-MIB"
        self.yang_parent_name = "CLAB-DEF-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("clabSecCertObject", ("clabseccertobject", CLABDEFMIB.ClabSecCertObject))])
        self._leafs = OrderedDict()

        self.clabseccertobject = CLABDEFMIB.ClabSecCertObject()
        self.clabseccertobject.parent = self
        self._children_name_map["clabseccertobject"] = "clabSecCertObject"
        self._segment_path = lambda: "CLAB-DEF-MIB:CLAB-DEF-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(CLABDEFMIB, [], name, value)


    class ClabSecCertObject(Entity):
        """
        
        
        .. attribute:: clabsrvcprvdrrootcacert
        
        	The X509 DER\-encoded CableLabs Service Provider Root CA Certificate
        	**type**\: str
        
        	**length:** 0..4096
        
        	**config**\: False
        
        .. attribute:: clabcvcrootcacert
        
        	The X509 DER\-encoded CableLabs CVC Root CA Certificate
        	**type**\: str
        
        	**length:** 0..4096
        
        	**config**\: False
        
        .. attribute:: clabcvccacert
        
        	The X509 DER\-encoded CableLabs CVC CA Certificate
        	**type**\: str
        
        	**length:** 0..4096
        
        	**config**\: False
        
        .. attribute:: clabmfgcvccert
        
        	The X509 DER\-encoded Manufacturer CVC Certificate
        	**type**\: str
        
        	**length:** 0..4096
        
        	**config**\: False
        
        .. attribute:: clabmfgcacert
        
        	The X509 DER\-encoded Manufacturer CA Certificate
        	**type**\: str
        
        	**length:** 0..4096
        
        	**config**\: False
        
        

        """

        _prefix = 'CLAB-DEF-MIB'
        _revision = '2012-08-09'

        def __init__(self):
            super(CLABDEFMIB.ClabSecCertObject, self).__init__()

            self.yang_name = "clabSecCertObject"
            self.yang_parent_name = "CLAB-DEF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('clabsrvcprvdrrootcacert', (YLeaf(YType.str, 'clabSrvcPrvdrRootCACert'), ['str'])),
                ('clabcvcrootcacert', (YLeaf(YType.str, 'clabCVCRootCACert'), ['str'])),
                ('clabcvccacert', (YLeaf(YType.str, 'clabCVCCACert'), ['str'])),
                ('clabmfgcvccert', (YLeaf(YType.str, 'clabMfgCVCCert'), ['str'])),
                ('clabmfgcacert', (YLeaf(YType.str, 'clabMfgCACert'), ['str'])),
            ])
            self.clabsrvcprvdrrootcacert = None
            self.clabcvcrootcacert = None
            self.clabcvccacert = None
            self.clabmfgcvccert = None
            self.clabmfgcacert = None
            self._segment_path = lambda: "clabSecCertObject"
            self._absolute_path = lambda: "CLAB-DEF-MIB:CLAB-DEF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CLABDEFMIB.ClabSecCertObject, ['clabsrvcprvdrrootcacert', 'clabcvcrootcacert', 'clabcvccacert', 'clabmfgcvccert', 'clabmfgcacert'], name, value)


    def clone_ptr(self):
        self._top_entity = CLABDEFMIB()
        return self._top_entity



