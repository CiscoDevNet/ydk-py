""" tailf_webui 

This module defines the Tail\-f Web UI data model

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class Webui(object):
    """
    
    
    .. attribute:: data_stores
    
    	
    	**type**\:   :py:class:`DataStores <ydk.models.cisco_ios_xe.tailf_webui.Webui.DataStores>`
    
    .. attribute:: schematics
    
    	
    	**type**\:   :py:class:`Schematics <ydk.models.cisco_ios_xe.tailf_webui.Webui.Schematics>`
    
    

    """

    _prefix = 'webui'
    _revision = '2013-03-07'

    def __init__(self):
        self.data_stores = Webui.DataStores()
        self.data_stores.parent = self
        self.schematics = Webui.Schematics()
        self.schematics.parent = self


    class Schematics(object):
        """
        
        
        .. attribute:: assets
        
        	
        	**type**\:   :py:class:`Assets <ydk.models.cisco_ios_xe.tailf_webui.Webui.Schematics.Assets>`
        
        .. attribute:: panels
        
        	
        	**type**\:   :py:class:`Panels <ydk.models.cisco_ios_xe.tailf_webui.Webui.Schematics.Panels>`
        
        

        """

        _prefix = 'webui'
        _revision = '2013-03-07'

        def __init__(self):
            self.parent = None
            self.assets = Webui.Schematics.Assets()
            self.assets.parent = self
            self.panels = Webui.Schematics.Panels()
            self.panels.parent = self


        class Panels(object):
            """
            
            
            .. attribute:: panel
            
            	
            	**type**\: list of    :py:class:`Panel <ydk.models.cisco_ios_xe.tailf_webui.Webui.Schematics.Panels.Panel>`
            
            

            """

            _prefix = 'webui'
            _revision = '2013-03-07'

            def __init__(self):
                self.parent = None
                self.panel = YList()
                self.panel.parent = self
                self.panel.name = 'panel'


            class Panel(object):
                """
                
                
                .. attribute:: name  <key>
                
                	
                	**type**\:  str
                
                .. attribute:: components
                
                	
                	**type**\:   :py:class:`Components <ydk.models.cisco_ios_xe.tailf_webui.Webui.Schematics.Panels.Panel.Components>`
                
                .. attribute:: properties
                
                	
                	**type**\:   :py:class:`Properties <ydk.models.cisco_ios_xe.tailf_webui.Webui.Schematics.Panels.Panel.Properties>`
                
                

                """

                _prefix = 'webui'
                _revision = '2013-03-07'

                def __init__(self):
                    self.parent = None
                    self.name = None
                    self.components = Webui.Schematics.Panels.Panel.Components()
                    self.components.parent = self
                    self.properties = Webui.Schematics.Panels.Panel.Properties()
                    self.properties.parent = self


                class Properties(object):
                    """
                    
                    
                    .. attribute:: description
                    
                    	
                    	**type**\:  str
                    
                    .. attribute:: height
                    
                    	
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: title
                    
                    	
                    	**type**\:  str
                    
                    .. attribute:: width
                    
                    	
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    

                    """

                    _prefix = 'webui'
                    _revision = '2013-03-07'

                    def __init__(self):
                        self.parent = None
                        self.description = None
                        self.height = None
                        self.title = None
                        self.width = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/tailf-webui:properties'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.description is not None:
                            return True

                        if self.height is not None:
                            return True

                        if self.title is not None:
                            return True

                        if self.width is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _tailf_webui as meta
                        return meta._meta_table['Webui.Schematics.Panels.Panel.Properties']['meta_info']


                class Components(object):
                    """
                    
                    
                    .. attribute:: component
                    
                    	
                    	**type**\: list of    :py:class:`Component <ydk.models.cisco_ios_xe.tailf_webui.Webui.Schematics.Panels.Panel.Components.Component>`
                    
                    

                    """

                    _prefix = 'webui'
                    _revision = '2013-03-07'

                    def __init__(self):
                        self.parent = None
                        self.component = YList()
                        self.component.parent = self
                        self.component.name = 'component'


                    class Component(object):
                        """
                        
                        
                        .. attribute:: id  <key>
                        
                        	
                        	**type**\:  str
                        
                        .. attribute:: properties
                        
                        	
                        	**type**\:   :py:class:`Properties <ydk.models.cisco_ios_xe.tailf_webui.Webui.Schematics.Panels.Panel.Components.Component.Properties>`
                        
                        

                        """

                        _prefix = 'webui'
                        _revision = '2013-03-07'

                        def __init__(self):
                            self.parent = None
                            self.id = None
                            self.properties = Webui.Schematics.Panels.Panel.Components.Component.Properties()
                            self.properties.parent = self


                        class Properties(object):
                            """
                            
                            
                            .. attribute:: height
                            
                            	
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: image
                            
                            	
                            	**type**\:   :py:class:`Image <ydk.models.cisco_ios_xe.tailf_webui.Webui.Schematics.Panels.Panel.Components.Component.Properties.Image>`
                            
                            .. attribute:: left
                            
                            	
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: link
                            
                            	
                            	**type**\:   :py:class:`Link <ydk.models.cisco_ios_xe.tailf_webui.Webui.Schematics.Panels.Panel.Components.Component.Properties.Link>`
                            
                            .. attribute:: top
                            
                            	
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: width
                            
                            	
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: z_index
                            
                            	
                            	**type**\:  int
                            
                            	**range:** \-32768..32767
                            
                            

                            """

                            _prefix = 'webui'
                            _revision = '2013-03-07'

                            def __init__(self):
                                self.parent = None
                                self.height = None
                                self.image = Webui.Schematics.Panels.Panel.Components.Component.Properties.Image()
                                self.image.parent = self
                                self.left = None
                                self.link = Webui.Schematics.Panels.Panel.Components.Component.Properties.Link()
                                self.link.parent = self
                                self.top = None
                                self.width = None
                                self.z_index = None


                            class Image(object):
                                """
                                
                                
                                .. attribute:: image
                                
                                	
                                	**type**\:  str
                                
                                	**refers to**\:  :py:class:`name <ydk.models.cisco_ios_xe.tailf_webui.Webui.Schematics.Assets.Asset>`
                                
                                	**mandatory**\: True
                                
                                

                                """

                                _prefix = 'webui'
                                _revision = '2013-03-07'

                                def __init__(self):
                                    self.parent = None
                                    self.image = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/tailf-webui:image'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.image is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xe._meta import _tailf_webui as meta
                                    return meta._meta_table['Webui.Schematics.Panels.Panel.Components.Component.Properties.Image']['meta_info']


                            class Link(object):
                                """
                                
                                
                                .. attribute:: link
                                
                                	
                                	**type**\:  str
                                
                                	**mandatory**\: True
                                
                                .. attribute:: text
                                
                                	
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'webui'
                                _revision = '2013-03-07'

                                def __init__(self):
                                    self.parent = None
                                    self.link = None
                                    self.text = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/tailf-webui:link'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.link is not None:
                                        return True

                                    if self.text is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xe._meta import _tailf_webui as meta
                                    return meta._meta_table['Webui.Schematics.Panels.Panel.Components.Component.Properties.Link']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/tailf-webui:properties'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.height is not None:
                                    return True

                                if self.image is not None and self.image._has_data():
                                    return True

                                if self.left is not None:
                                    return True

                                if self.link is not None and self.link._has_data():
                                    return True

                                if self.top is not None:
                                    return True

                                if self.width is not None:
                                    return True

                                if self.z_index is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xe._meta import _tailf_webui as meta
                                return meta._meta_table['Webui.Schematics.Panels.Panel.Components.Component.Properties']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.id is None:
                                raise YPYModelError('Key property id is None')

                            return self.parent._common_path +'/tailf-webui:component[tailf-webui:id = ' + str(self.id) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.id is not None:
                                return True

                            if self.properties is not None and self.properties._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xe._meta import _tailf_webui as meta
                            return meta._meta_table['Webui.Schematics.Panels.Panel.Components.Component']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/tailf-webui:components'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.component is not None:
                            for child_ref in self.component:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _tailf_webui as meta
                        return meta._meta_table['Webui.Schematics.Panels.Panel.Components']['meta_info']

                @property
                def _common_path(self):
                    if self.name is None:
                        raise YPYModelError('Key property name is None')

                    return '/tailf-webui:webui/tailf-webui:schematics/tailf-webui:panels/tailf-webui:panel[tailf-webui:name = ' + str(self.name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.name is not None:
                        return True

                    if self.components is not None and self.components._has_data():
                        return True

                    if self.properties is not None and self.properties._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _tailf_webui as meta
                    return meta._meta_table['Webui.Schematics.Panels.Panel']['meta_info']

            @property
            def _common_path(self):

                return '/tailf-webui:webui/tailf-webui:schematics/tailf-webui:panels'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.panel is not None:
                    for child_ref in self.panel:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _tailf_webui as meta
                return meta._meta_table['Webui.Schematics.Panels']['meta_info']


        class Assets(object):
            """
            
            
            .. attribute:: asset
            
            	
            	**type**\: list of    :py:class:`Asset <ydk.models.cisco_ios_xe.tailf_webui.Webui.Schematics.Assets.Asset>`
            
            

            """

            _prefix = 'webui'
            _revision = '2013-03-07'

            def __init__(self):
                self.parent = None
                self.asset = YList()
                self.asset.parent = self
                self.asset.name = 'asset'


            class Asset(object):
                """
                
                
                .. attribute:: name  <key>
                
                	
                	**type**\:  str
                
                .. attribute:: base_64_image
                
                	
                	**type**\:  str
                
                	**mandatory**\: True
                
                .. attribute:: type
                
                	
                	**type**\:   :py:class:`TypeEnum <ydk.models.cisco_ios_xe.tailf_webui.Webui.Schematics.Assets.Asset.TypeEnum>`
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'webui'
                _revision = '2013-03-07'

                def __init__(self):
                    self.parent = None
                    self.name = None
                    self.base_64_image = None
                    self.type = None

                class TypeEnum(Enum):
                    """
                    TypeEnum

                    .. data:: jpeg = 0

                    .. data:: png = 1

                    .. data:: gif = 2

                    """

                    jpeg = 0

                    png = 1

                    gif = 2


                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _tailf_webui as meta
                        return meta._meta_table['Webui.Schematics.Assets.Asset.TypeEnum']


                @property
                def _common_path(self):
                    if self.name is None:
                        raise YPYModelError('Key property name is None')

                    return '/tailf-webui:webui/tailf-webui:schematics/tailf-webui:assets/tailf-webui:asset[tailf-webui:name = ' + str(self.name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.name is not None:
                        return True

                    if self.base_64_image is not None:
                        return True

                    if self.type is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _tailf_webui as meta
                    return meta._meta_table['Webui.Schematics.Assets.Asset']['meta_info']

            @property
            def _common_path(self):

                return '/tailf-webui:webui/tailf-webui:schematics/tailf-webui:assets'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.asset is not None:
                    for child_ref in self.asset:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _tailf_webui as meta
                return meta._meta_table['Webui.Schematics.Assets']['meta_info']

        @property
        def _common_path(self):

            return '/tailf-webui:webui/tailf-webui:schematics'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.assets is not None and self.assets._has_data():
                return True

            if self.panels is not None and self.panels._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _tailf_webui as meta
            return meta._meta_table['Webui.Schematics']['meta_info']


    class DataStores(object):
        """
        
        
        .. attribute:: data_store
        
        	
        	**type**\: list of    :py:class:`DataStore <ydk.models.cisco_ios_xe.tailf_webui.Webui.DataStores.DataStore>`
        
        .. attribute:: saved_query
        
        	
        	**type**\: list of    :py:class:`SavedQuery <ydk.models.cisco_ios_xe.tailf_webui.Webui.DataStores.SavedQuery>`
        
        .. attribute:: user_profile
        
        	
        	**type**\: list of    :py:class:`UserProfile <ydk.models.cisco_ios_xe.tailf_webui.Webui.DataStores.UserProfile>`
        
        

        """

        _prefix = 'webui'
        _revision = '2013-03-07'

        def __init__(self):
            self.parent = None
            self.data_store = YList()
            self.data_store.parent = self
            self.data_store.name = 'data_store'
            self.saved_query = YList()
            self.saved_query.parent = self
            self.saved_query.name = 'saved_query'
            self.user_profile = YList()
            self.user_profile.parent = self
            self.user_profile.name = 'user_profile'


        class UserProfile(object):
            """
            
            
            .. attribute:: username  <key>
            
            	
            	**type**\:  str
            
            .. attribute:: profile
            
            	
            	**type**\: list of    :py:class:`Profile <ydk.models.cisco_ios_xe.tailf_webui.Webui.DataStores.UserProfile.Profile>`
            
            .. attribute:: saved_query
            
            	
            	**type**\: list of    :py:class:`SavedQuery <ydk.models.cisco_ios_xe.tailf_webui.Webui.DataStores.UserProfile.SavedQuery>`
            
            

            """

            _prefix = 'webui'
            _revision = '2013-03-07'

            def __init__(self):
                self.parent = None
                self.username = None
                self.profile = YList()
                self.profile.parent = self
                self.profile.name = 'profile'
                self.saved_query = YList()
                self.saved_query.parent = self
                self.saved_query.name = 'saved_query'


            class Profile(object):
                """
                
                
                .. attribute:: key  <key>
                
                	
                	**type**\:  str
                
                .. attribute:: value
                
                	
                	**type**\:  str
                
                

                """

                _prefix = 'webui'
                _revision = '2013-03-07'

                def __init__(self):
                    self.parent = None
                    self.key = None
                    self.value = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.key is None:
                        raise YPYModelError('Key property key is None')

                    return self.parent._common_path +'/tailf-webui:profile[tailf-webui:key = ' + str(self.key) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.key is not None:
                        return True

                    if self.value is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _tailf_webui as meta
                    return meta._meta_table['Webui.DataStores.UserProfile.Profile']['meta_info']


            class SavedQuery(object):
                """
                
                
                .. attribute:: list_path  <key>
                
                	
                	**type**\:  str
                
                .. attribute:: name  <key>
                
                	
                	**type**\:  str
                
                .. attribute:: serialized_query
                
                	
                	**type**\:  str
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'webui'
                _revision = '2013-03-07'

                def __init__(self):
                    self.parent = None
                    self.list_path = None
                    self.name = None
                    self.serialized_query = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.list_path is None:
                        raise YPYModelError('Key property list_path is None')
                    if self.name is None:
                        raise YPYModelError('Key property name is None')

                    return self.parent._common_path +'/tailf-webui:saved-query[tailf-webui:list-path = ' + str(self.list_path) + '][tailf-webui:name = ' + str(self.name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.list_path is not None:
                        return True

                    if self.name is not None:
                        return True

                    if self.serialized_query is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _tailf_webui as meta
                    return meta._meta_table['Webui.DataStores.UserProfile.SavedQuery']['meta_info']

            @property
            def _common_path(self):
                if self.username is None:
                    raise YPYModelError('Key property username is None')

                return '/tailf-webui:webui/tailf-webui:data-stores/tailf-webui:user-profile[tailf-webui:username = ' + str(self.username) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.username is not None:
                    return True

                if self.profile is not None:
                    for child_ref in self.profile:
                        if child_ref._has_data():
                            return True

                if self.saved_query is not None:
                    for child_ref in self.saved_query:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _tailf_webui as meta
                return meta._meta_table['Webui.DataStores.UserProfile']['meta_info']


        class DataStore(object):
            """
            
            
            .. attribute:: key  <key>
            
            	
            	**type**\:  str
            
            .. attribute:: value
            
            	
            	**type**\:  str
            
            

            """

            _prefix = 'webui'
            _revision = '2013-03-07'

            def __init__(self):
                self.parent = None
                self.key = None
                self.value = None

            @property
            def _common_path(self):
                if self.key is None:
                    raise YPYModelError('Key property key is None')

                return '/tailf-webui:webui/tailf-webui:data-stores/tailf-webui:data-store[tailf-webui:key = ' + str(self.key) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.key is not None:
                    return True

                if self.value is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _tailf_webui as meta
                return meta._meta_table['Webui.DataStores.DataStore']['meta_info']


        class SavedQuery(object):
            """
            
            
            .. attribute:: list_path  <key>
            
            	
            	**type**\:  str
            
            .. attribute:: name  <key>
            
            	
            	**type**\:  str
            
            .. attribute:: serialized_query
            
            	
            	**type**\:  str
            
            	**mandatory**\: True
            
            

            """

            _prefix = 'webui'
            _revision = '2013-03-07'

            def __init__(self):
                self.parent = None
                self.list_path = None
                self.name = None
                self.serialized_query = None

            @property
            def _common_path(self):
                if self.list_path is None:
                    raise YPYModelError('Key property list_path is None')
                if self.name is None:
                    raise YPYModelError('Key property name is None')

                return '/tailf-webui:webui/tailf-webui:data-stores/tailf-webui:saved-query[tailf-webui:list-path = ' + str(self.list_path) + '][tailf-webui:name = ' + str(self.name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.list_path is not None:
                    return True

                if self.name is not None:
                    return True

                if self.serialized_query is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _tailf_webui as meta
                return meta._meta_table['Webui.DataStores.SavedQuery']['meta_info']

        @property
        def _common_path(self):

            return '/tailf-webui:webui/tailf-webui:data-stores'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.data_store is not None:
                for child_ref in self.data_store:
                    if child_ref._has_data():
                        return True

            if self.saved_query is not None:
                for child_ref in self.saved_query:
                    if child_ref._has_data():
                        return True

            if self.user_profile is not None:
                for child_ref in self.user_profile:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _tailf_webui as meta
            return meta._meta_table['Webui.DataStores']['meta_info']

    @property
    def _common_path(self):

        return '/tailf-webui:webui'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.data_stores is not None and self.data_stores._has_data():
            return True

        if self.schematics is not None and self.schematics._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _tailf_webui as meta
        return meta._meta_table['Webui']['meta_info']


