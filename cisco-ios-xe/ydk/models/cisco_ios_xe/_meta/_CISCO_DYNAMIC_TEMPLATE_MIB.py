


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'CiscoDynamicTemplateMib.Cdttemplatetable.Cdttemplateentry.CdttemplatesrcEnum' : _MetaInfoEnum('CdttemplatesrcEnum', 'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB',
        {
            'other':'other',
            'derived':'derived',
            'local':'local',
            'aaaUserProfile':'aaaUserProfile',
            'aaaServiceProfile':'aaaServiceProfile',
        }, 'CISCO-DYNAMIC-TEMPLATE-MIB', _yang_ns._namespaces['CISCO-DYNAMIC-TEMPLATE-MIB']),
    'CiscoDynamicTemplateMib.Cdttemplatetable.Cdttemplateentry' : {
        'meta_info' : _MetaInfoClass('CiscoDynamicTemplateMib.Cdttemplatetable.Cdttemplateentry',
            False, 
            [
            _MetaInfoClassMember('cdtTemplateName', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                This object indicates a string-value that uniquely identifies
                the dynamic template.
                
                If the corresponding instance of cdtTemplateSrc is not
                'local', then the system automatically generates the name
                identifying the dynamic template.
                ''',
                'cdttemplatename',
                'CISCO-DYNAMIC-TEMPLATE-MIB', True),
            _MetaInfoClassMember('cdtTemplateSrc', REFERENCE_ENUM_CLASS, 'CdttemplatesrcEnum' , 'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB', 'CiscoDynamicTemplateMib.Cdttemplatetable.Cdttemplateentry.CdttemplatesrcEnum', 
                [], [], 
                '''                This object specifies the source of the dynamic template:
                
                'other'
                    The implementation of the MIB module does not recognize the
                    source of the dynamic template.
                
                'derived'
                    The system created the set of attributes from one or
                    more dynamic templates.
                
                'local'
                    The dynamic template was locally configured through a
                    management entity, such as the local console or a SNMP
                    entity.
                
                'aaaUserProfile'
                    The dynamic template originated from a user profile
                    pushed from an external policy server.
                
                'aaaServiceProfile'
                    The dynamic template originated from a service profile
                    pushed from an external policy server.
                ''',
                'cdttemplatesrc',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtTemplateStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                This object specifies the status of the dynamic template.  The
                following columns must be valid before activating a dynamic
                template:
                
                    - cdtTemplateStorage
                    - cdtTemplateType
                
                However, these objects specify a default value.  Thus, it is
                possible to use create-and-go semantics without setting any
                additional columns.
                
                An implementation must allow the EMS/NMS to modify any column
                when this column is 'active', including columns defined in
                tables that have a one-to-one or sparse dependent relationship
                on this table.
                ''',
                'cdttemplatestatus',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtTemplateStorage', REFERENCE_ENUM_CLASS, 'StoragetypeEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'StoragetypeEnum', 
                [], [], 
                '''                This object specifies what happens to the dynamic template
                upon restart.
                
                If the corresponding instance of cdtTemplateSrc is not
                'local', then this column must be 'volatile'.
                ''',
                'cdttemplatestorage',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtTemplateType', REFERENCE_ENUM_CLASS, 'DynamictemplatetypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_TC_MIB', 'DynamictemplatetypeEnum', 
                [], [], 
                '''                This object indicates the types of dynamic template.
                ''',
                'cdttemplatetype',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtTemplateUsageCount', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object specifies the number of targets using a dynamic template
                ''',
                'cdttemplateusagecount',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            ],
            'CISCO-DYNAMIC-TEMPLATE-MIB',
            'cdtTemplateEntry',
            _yang_ns._namespaces['CISCO-DYNAMIC-TEMPLATE-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB'
        ),
    },
    'CiscoDynamicTemplateMib.Cdttemplatetable' : {
        'meta_info' : _MetaInfoClass('CiscoDynamicTemplateMib.Cdttemplatetable',
            False, 
            [
            _MetaInfoClassMember('cdtTemplateEntry', REFERENCE_LIST, 'Cdttemplateentry' , 'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB', 'CiscoDynamicTemplateMib.Cdttemplatetable.Cdttemplateentry', 
                [], [], 
                '''                An entry describes a dynamic template, which serves as a
                container for configuration attributes.  The configuration
                attributes contained by a dynamic template depends on its type.
                
                The system automatically creates a corresponding entry when a
                dynamic template has been created through another management
                entity (e.g., the system's local console).  Likewise, the system
                automatically destroys a corresponding entry when a dynamic
                template has been destroyed through another management entity.
                
                The system automatically creates a corresponding entry when an
                external policy server pushes a user profile or a service
                profile to the system.
                
                The system automatically creates a corresponding entry when it
                generates a derived configuration.
                ''',
                'cdttemplateentry',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            ],
            'CISCO-DYNAMIC-TEMPLATE-MIB',
            'cdtTemplateTable',
            _yang_ns._namespaces['CISCO-DYNAMIC-TEMPLATE-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB'
        ),
    },
    'CiscoDynamicTemplateMib.Cdttemplatetargettable.Cdttemplatetargetentry' : {
        'meta_info' : _MetaInfoClass('CiscoDynamicTemplateMib.Cdttemplatetargettable.Cdttemplatetargetentry',
            False, 
            [
            _MetaInfoClassMember('cdtTemplateTargetType', REFERENCE_ENUM_CLASS, 'DynamictemplatetargettypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_TC_MIB', 'DynamictemplatetargettypeEnum', 
                [], [], 
                '''                This object indicates the type of target.
                ''',
                'cdttemplatetargettype',
                'CISCO-DYNAMIC-TEMPLATE-MIB', True),
            _MetaInfoClassMember('cdtTemplateTargetId', ATTRIBUTE, 'str' , None, None, 
                [(1, 20)], [], 
                '''                This object uniquely identifies the target within the scope of
                its type.
                ''',
                'cdttemplatetargetid',
                'CISCO-DYNAMIC-TEMPLATE-MIB', True),
            _MetaInfoClassMember('cdtTemplateTargetStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                This object specifies the status of the dynamic template
                target.  The following columns must be valid before activating a
                subscriber access profile:
                
                    - cdtTemplateTargetStorage
                
                However, these objects specify a default value.  Thus, it is
                possible to use create-and-go semantics without setting any
                additional columns.
                
                An implementation must allow the EMS/NMS to modify any column
                when this column is 'active', including columns defined in
                tables that have a one-to-one or sparse dependent relationship
                on this table.
                ''',
                'cdttemplatetargetstatus',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtTemplateTargetStorage', REFERENCE_ENUM_CLASS, 'StoragetypeEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'StoragetypeEnum', 
                [], [], 
                '''                This object specifies what happens to the dynamic template
                target upon restart.
                ''',
                'cdttemplatetargetstorage',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            ],
            'CISCO-DYNAMIC-TEMPLATE-MIB',
            'cdtTemplateTargetEntry',
            _yang_ns._namespaces['CISCO-DYNAMIC-TEMPLATE-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB'
        ),
    },
    'CiscoDynamicTemplateMib.Cdttemplatetargettable' : {
        'meta_info' : _MetaInfoClass('CiscoDynamicTemplateMib.Cdttemplatetargettable',
            False, 
            [
            _MetaInfoClassMember('cdtTemplateTargetEntry', REFERENCE_LIST, 'Cdttemplatetargetentry' , 'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB', 'CiscoDynamicTemplateMib.Cdttemplatetargettable.Cdttemplatetargetentry', 
                [], [], 
                '''                An entry describes a target associated with one or more
                dynamic templates.
                
                The system automatically creates an entry when it associates a
                dynamic template to a target.  Likewise, the system
                automatically destroys an entry when a target no longer has any
                associated dynamic templates.
                ''',
                'cdttemplatetargetentry',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            ],
            'CISCO-DYNAMIC-TEMPLATE-MIB',
            'cdtTemplateTargetTable',
            _yang_ns._namespaces['CISCO-DYNAMIC-TEMPLATE-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB'
        ),
    },
    'CiscoDynamicTemplateMib.Cdttemplateassociationtable.Cdttemplateassociationentry' : {
        'meta_info' : _MetaInfoClass('CiscoDynamicTemplateMib.Cdttemplateassociationtable.Cdttemplateassociationentry',
            False, 
            [
            _MetaInfoClassMember('cdtTemplateTargetType', REFERENCE_ENUM_CLASS, 'DynamictemplatetargettypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_TC_MIB', 'DynamictemplatetargettypeEnum', 
                [], [], 
                '''                ''',
                'cdttemplatetargettype',
                'CISCO-DYNAMIC-TEMPLATE-MIB', True),
            _MetaInfoClassMember('cdtTemplateTargetId', ATTRIBUTE, 'str' , None, None, 
                [(1, 20)], [], 
                '''                ''',
                'cdttemplatetargetid',
                'CISCO-DYNAMIC-TEMPLATE-MIB', True),
            _MetaInfoClassMember('cdtTemplateAssociationName', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                This object indicates the name of the template associated with
                the target.
                ''',
                'cdttemplateassociationname',
                'CISCO-DYNAMIC-TEMPLATE-MIB', True),
            _MetaInfoClassMember('cdtTemplateAssociationPrecedence', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the relative precedence of the
                associated dynamic template.  Lower values have higher
                precedence than higher values.
                ''',
                'cdttemplateassociationprecedence',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            ],
            'CISCO-DYNAMIC-TEMPLATE-MIB',
            'cdtTemplateAssociationEntry',
            _yang_ns._namespaces['CISCO-DYNAMIC-TEMPLATE-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB'
        ),
    },
    'CiscoDynamicTemplateMib.Cdttemplateassociationtable' : {
        'meta_info' : _MetaInfoClass('CiscoDynamicTemplateMib.Cdttemplateassociationtable',
            False, 
            [
            _MetaInfoClassMember('cdtTemplateAssociationEntry', REFERENCE_LIST, 'Cdttemplateassociationentry' , 'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB', 'CiscoDynamicTemplateMib.Cdttemplateassociationtable.Cdttemplateassociationentry', 
                [], [], 
                '''                An entry indicates an association of a dynamic template with a
                target.
                
                The system automatically creates an entry when it associates a
                dynamic template to a target.
                
                The system also creates an entry when it derives the
                configuration that it applies to a target.
                
                The system automatically destroys an entry under the following
                circumstances:
                
                1)  The target indicated by the entry no longer exists.
                
                2)  The association between the target and the dynamic template
                    no longer exists.
                ''',
                'cdttemplateassociationentry',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            ],
            'CISCO-DYNAMIC-TEMPLATE-MIB',
            'cdtTemplateAssociationTable',
            _yang_ns._namespaces['CISCO-DYNAMIC-TEMPLATE-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB'
        ),
    },
    'CiscoDynamicTemplateMib.Cdttemplateusagetable.Cdttemplateusageentry' : {
        'meta_info' : _MetaInfoClass('CiscoDynamicTemplateMib.Cdttemplateusagetable.Cdttemplateusageentry',
            False, 
            [
            _MetaInfoClassMember('cdtTemplateName', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                ''',
                'cdttemplatename',
                'CISCO-DYNAMIC-TEMPLATE-MIB', True),
            _MetaInfoClassMember('cdtTemplateUsageTargetType', REFERENCE_ENUM_CLASS, 'DynamictemplatetargettypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_TC_MIB', 'DynamictemplatetargettypeEnum', 
                [], [], 
                '''                This object indicates the type of target using the
                dynamic template.
                ''',
                'cdttemplateusagetargettype',
                'CISCO-DYNAMIC-TEMPLATE-MIB', True),
            _MetaInfoClassMember('cdtTemplateUsageTargetId', ATTRIBUTE, 'str' , None, None, 
                [(1, 20)], [], 
                '''                This object indicates the name of the target using the dynamic
                template
                ''',
                'cdttemplateusagetargetid',
                'CISCO-DYNAMIC-TEMPLATE-MIB', True),
            ],
            'CISCO-DYNAMIC-TEMPLATE-MIB',
            'cdtTemplateUsageEntry',
            _yang_ns._namespaces['CISCO-DYNAMIC-TEMPLATE-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB'
        ),
    },
    'CiscoDynamicTemplateMib.Cdttemplateusagetable' : {
        'meta_info' : _MetaInfoClass('CiscoDynamicTemplateMib.Cdttemplateusagetable',
            False, 
            [
            _MetaInfoClassMember('cdtTemplateUsageEntry', REFERENCE_LIST, 'Cdttemplateusageentry' , 'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB', 'CiscoDynamicTemplateMib.Cdttemplateusagetable.Cdttemplateusageentry', 
                [], [], 
                '''                An entry indicates a target using the dynamic template.
                
                The system automatically creates an entry when it associates a
                dynamic template to a target.
                
                The system also creates an entry when it derives the
                configuration that it applies to a target.
                
                The system automatically destroys an entry under the following
                circumstances:
                
                1)  The target indicated by the entry no longer exists.
                
                2)  The association between the target and the dynamic template
                    no longer exists.
                ''',
                'cdttemplateusageentry',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            ],
            'CISCO-DYNAMIC-TEMPLATE-MIB',
            'cdtTemplateUsageTable',
            _yang_ns._namespaces['CISCO-DYNAMIC-TEMPLATE-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB'
        ),
    },
    'CiscoDynamicTemplateMib.Cdttemplatecommontable.Cdttemplatecommonentry' : {
        'meta_info' : _MetaInfoClass('CiscoDynamicTemplateMib.Cdttemplatecommontable.Cdttemplatecommonentry',
            False, 
            [
            _MetaInfoClassMember('cdtTemplateName', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                ''',
                'cdttemplatename',
                'CISCO-DYNAMIC-TEMPLATE-MIB', True),
            _MetaInfoClassMember('cdtCommonAddrPool', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                This object specifies the name of the IP address pool the
                system will use to assign an IP address to a peer of a target.
                
                This column is valid only if the 'addrPool' bit of the
                corresponding instance of cdtCommonValid is '1'.
                ''',
                'cdtcommonaddrpool',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtCommonDescr', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                This object specifies a human-readable description for the
                dynamic template.
                
                This column is valid only if the 'descr' bit of the
                corresponding instance of cdtCommonValid is '1'.
                ''',
                'cdtcommondescr',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtCommonIpv4AccessGroup', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                This object specifies the name (or number) of the IPv4 ACL
                applied to a target.
                
                This column is valid only if the 'ipv4AccessGroup' bit of the
                corresponding instance of cdtCommonValid is '1'.
                ''',
                'cdtcommonipv4accessgroup',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtCommonIpv4Unreachables', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object specifies whether a target generates ICMPv4
                unreachable messages.
                
                This column is valid only if the 'ipv4Unreachables' bit of the
                corresponding instance of cdtCommonValid is '1'.
                ''',
                'cdtcommonipv4unreachables',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtCommonIpv6AccessGroup', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                This object specifies the name (or number) of the IPv4 ACL
                applied to a target.
                
                This column is valid only if the 'ipv6AccessGroup' bit of the
                corresponding instance of cdtCommonValid is '1'.
                ''',
                'cdtcommonipv6accessgroup',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtCommonIpv6Unreachables', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object specifies whether a target generates ICMPv6
                unreachable messages.
                
                This column is valid only if the 'ipv6Unreachables' bit of the
                corresponding instance of cdtCommonValid is '1'.
                ''',
                'cdtcommonipv6unreachables',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtCommonKeepaliveInt', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                This object specifies the interval that the system sends
                keepalive messages to a target.
                
                This column is valid only if the 'keepaliveInterval' bit of the
                corresponding instance of cdtCommonValid is '1'.
                ''',
                'cdtcommonkeepaliveint',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtCommonKeepaliveRetries', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                This object specifies the number of times the system will
                resend a keepalive message without a response before it
                transitions a target to an operationally down state.
                
                This column is valid only if the 'keepaliveRetries' bit of the
                corresponding instance of cdtCommonValid is '1'.
                ''',
                'cdtcommonkeepaliveretries',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtCommonSrvAcct', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object specifies the name of the traffic accounting policy
                applied to a target.
                
                The system should assume that the cbpPolicyMapType (defined by
                the CISCO-CBP-BASE-CFG-MIB) of the policy is
                cbpPmtTrafficAccounting (defined by the CISCO-CBP-TYPE-OID-MIB).
                
                This column is valid only if the 'srvAcct' bit of the
                corresponding instance of cdtCommonValid is '1'.
                ''',
                'cdtcommonsrvacct',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtCommonSrvNetflow', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object specifies the name of the NetFlow policy applied to
                a target.
                
                The system should assume that the cbpPolicyMapType (defined by
                the CISCO-CBP-BASE-CFG-MIB) of the policy is
                cbpPmtNetflow (defined by the CISCO-CBP-TYPE-OID-MIB).
                
                This column is valid only if the 'srvNetflow' bit of the
                corresponding instance of cdtCommonValid is '1'.
                ''',
                'cdtcommonsrvnetflow',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtCommonSrvQos', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object specifies the name of the traffic QoS policy
                applied to a target.
                
                The system should assume that the cbpPolicyMapType (defined by
                the CISCO-CBP-BASE-CFG-MIB) of the policy is cbpPmtQos (defined
                by the CISCO-CBP-TYPE-OID-MIB).
                
                This column is valid only if the 'srvQos' bit of the
                corresponding instance of cdtCommonValid is '1'.
                ''',
                'cdtcommonsrvqos',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtCommonSrvRedirect', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object specifies the name of the traffic redirect policy
                applied to a target.
                
                The system should assume that the cbpPolicyMapType (defined by
                the CISCO-CBP-BASE-CFG-MIB) of the policy is
                cbpPmtTrafficRedirect (defined by the CISCO-CBP-TYPE-OID-MIB).
                
                This column is valid only if the 'srvRedirect' bit of the
                corresponding instance of cdtCommonValid is '1'.
                ''',
                'cdtcommonsrvredirect',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtCommonSrvSubControl', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object specifies the name of the subscriber control
                policy applied to a target.
                
                The system should assume that the cbpPolicyMapType (defined by
                the CISCO-CBP-BASE-CFG-MIB) of the policy is
                cbpPmtControlSubscriber (defined by the CISCO-CBP-TYPE-OID-MIB).
                
                This column is valid only if the 'srvSubControl' bit of the
                corresponding instance of cdtCommonValid is '1'.
                ''',
                'cdtcommonsrvsubcontrol',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtCommonValid', REFERENCE_BITS, 'Cdtcommonvalid' , 'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB', 'CiscoDynamicTemplateMib.Cdttemplatecommontable.Cdttemplatecommonentry.Cdtcommonvalid', 
                [], [], 
                '''                This object specifies which attributes in the dynamic template
                have been configured to valid values.
                
                Each bit in this bit string corresponds to a column in this
                table.  If the bit is '0', then the value of the corresponding
                column is not valid.  If the bit is '1', then the value of the
                corresponding column has been configured to a valid value.
                
                The following list specifies the mappings between bits and the
                columns:
                
                    'descr'             => cdtCommonDescr
                    'keepaliveInt'      => cdtCommonKeepaliveInt
                    'keepaliveRetries'  => cdtCommonKeepaliveRetries
                    'vrf'               => cdtCommonVrf
                    'addrPool'          => cdtCommonAddrPool
                    'ipv4AccessGroup'   => cdtCommonIpv4AccessGroup
                    'ipv4Unreachables'  => cdtCommonIpv4Unreachables
                    'ipv6AccessGroup'   => cdtCommonIpv6AccessGroup
                    'ipv6Unreachables'  => cdtCommonIpv6Unreachables
                    'srvSubControl'     => cdtCommonSrvSubControl
                    'srvRedirect'       => cdtCommonSrvRedirect
                    'srvAcct'           => cdtCommonSrvAcct
                    'srvQos'            => cdtCommonSrvQos
                    'srvNetflow'        => cdtCommonSrvNetflow
                ''',
                'cdtcommonvalid',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtCommonVrf', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                This object specifies the name of the VRF with which a target
                has an association.
                
                This column is valid only if the 'vrf' bit of the corresponding
                instance of cdtCommonValid is '1'.
                ''',
                'cdtcommonvrf',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            ],
            'CISCO-DYNAMIC-TEMPLATE-MIB',
            'cdtTemplateCommonEntry',
            _yang_ns._namespaces['CISCO-DYNAMIC-TEMPLATE-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB'
        ),
    },
    'CiscoDynamicTemplateMib.Cdttemplatecommontable' : {
        'meta_info' : _MetaInfoClass('CiscoDynamicTemplateMib.Cdttemplatecommontable',
            False, 
            [
            _MetaInfoClassMember('cdtTemplateCommonEntry', REFERENCE_LIST, 'Cdttemplatecommonentry' , 'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB', 'CiscoDynamicTemplateMib.Cdttemplatecommontable.Cdttemplatecommonentry', 
                [], [], 
                '''                An entry containing attributes relating to any target.
                
                The system automatically creates an entry when the system or the
                EMS/NMS creates a row in the cdtTemplateTable with a
                cdtTemplateType of on the following values:
                
                    'derived'
                    'ppp'
                    'ethernet'
                    'ipSubscriber'
                    'service'
                
                Likewise, the system automatically destroys an entry when the
                system or the EMS/NMS destroys the corresponding row in the
                cdtTemplateTable.
                ''',
                'cdttemplatecommonentry',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            ],
            'CISCO-DYNAMIC-TEMPLATE-MIB',
            'cdtTemplateCommonTable',
            _yang_ns._namespaces['CISCO-DYNAMIC-TEMPLATE-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB'
        ),
    },
    'CiscoDynamicTemplateMib.Cdtiftemplatetable.Cdtiftemplateentry.Cdtifipv6NdraintervalunitsEnum' : _MetaInfoEnum('Cdtifipv6NdraintervalunitsEnum', 'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB',
        {
            'seconds':'seconds',
            'milliseconds':'milliseconds',
        }, 'CISCO-DYNAMIC-TEMPLATE-MIB', _yang_ns._namespaces['CISCO-DYNAMIC-TEMPLATE-MIB']),
    'CiscoDynamicTemplateMib.Cdtiftemplatetable.Cdtiftemplateentry.Cdtifipv6NdrouterpreferenceEnum' : _MetaInfoEnum('Cdtifipv6NdrouterpreferenceEnum', 'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB',
        {
            'high':'high',
            'medium':'medium',
            'low':'low',
        }, 'CISCO-DYNAMIC-TEMPLATE-MIB', _yang_ns._namespaces['CISCO-DYNAMIC-TEMPLATE-MIB']),
    'CiscoDynamicTemplateMib.Cdtiftemplatetable.Cdtiftemplateentry' : {
        'meta_info' : _MetaInfoClass('CiscoDynamicTemplateMib.Cdtiftemplatetable.Cdtiftemplateentry',
            False, 
            [
            _MetaInfoClassMember('cdtTemplateName', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                ''',
                'cdttemplatename',
                'CISCO-DYNAMIC-TEMPLATE-MIB', True),
            _MetaInfoClassMember('cdtIfCdpEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object specifies whether the target interface participates
                in the Cisco Discovery Protocol (CDP).
                
                This column is valid only if the 'cdpEnable' bit of the
                corresponding instance of cdtIfValid is '1'.
                ''',
                'cdtifcdpenable',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtIfFlowMonitor', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                This object specifies the name of the flow monitor associated
                with the target interface.
                
                This column is valid only if the 'flowMonitor' bit of the
                corresponding instance of cdtIfValid is '1'.
                ''',
                'cdtifflowmonitor',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtIfIpv4Mtu', ATTRIBUTE, 'int' , None, None, 
                [('0', 'None'), ('128', '65535')], [], 
                '''                This object specifies the Maximum Transfer Unit (MTU) size for
                IPv4 packets sent on the target interface.
                
                The value '0' cannot be written to an instance of this object.
                However, it serves as a convenient value when the column is not
                valid.
                
                This column is valid only if the 'ipv4Mtu' bit of the
                corresponding instance of cdtIfValid is '1'.
                ''',
                'cdtifipv4mtu',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtIfIpv4SubEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object specifies whether the target interface allows IPv4
                subscriber sessions.
                
                This column is valid only if the 'ipv4SubEnable' bit of the
                corresponding instance of cdtIfValid is '1'.
                ''',
                'cdtifipv4subenable',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtIfIpv4TcpMssAdjust', ATTRIBUTE, 'int' , None, None, 
                [('0', 'None'), ('500', '1460')], [], 
                '''                This object specifies the adjustment to the Maximum Segment
                Size (MSS) of TCP SYN packets received by the target interface
                contained in IPv4 datagrams.
                
                The value '0' cannot be written to an instance of this object.
                However, it serves as a convenient value when the column is not
                valid.
                
                This column is valid only if the 'ipv4TcpMssAdjust' bit of the
                corresponding instance of cdtIfValid is '1'.
                ''',
                'cdtifipv4tcpmssadjust',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtIfIpv4Unnumbered', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                This object specifies the interface of the source address that
                the target interface uses when originating IPv4 packets.
                
                The value '0' cannot be written to an instance of this object.
                However, it serves as a convenient value when the column is
                not valid (e.g., immediately following the creation of an
                instance of the object).
                
                This column is valid only if the 'ipv4Unnumbered' bit of the
                corresponding instance of cdtIfValid is '1'.
                ''',
                'cdtifipv4unnumbered',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtIfIpv4VerifyUniRpf', REFERENCE_ENUM_CLASS, 'UnicastrpftypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB', 'UnicastrpftypeEnum', 
                [], [], 
                '''                This object specifies whether the type of unicast RPF the
                system performs on IPv4 packets received by the target
                interface.
                
                This column is valid only if the 'ipv4VerifyUniRpf' bit of the
                corresponding instance of cdtIfValid is '1'.
                ''',
                'cdtifipv4verifyunirpf',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtIfIpv4VerifyUniRpfAcl', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                This object specifies the name (or number) of the IPv4 ACL
                used to determine whether the system should permit/deny packets
                received by the target interface that fail unicast RPF
                verification.
                
                This column is valid only if the 'ipv4VerifyUniRpfAcl' bit of
                the corresponding instance of cdtIfValid is '1'.
                ''',
                'cdtifipv4verifyunirpfacl',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtIfIpv4VerifyUniRpfOpts', REFERENCE_BITS, 'Unicastrpfoptions' , 'ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB', 'Unicastrpfoptions', 
                [], [], 
                '''                This object specifies the options that affect how the system
                performs unicast RPF on IPv4 packets received by the target
                interface.
                
                This column is valid only if the 'ipv4VerifyUniRpfOpts' bit of
                the corresponding instance of cdtIfValid is '1'.
                ''',
                'cdtifipv4verifyunirpfopts',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtIfIpv6Enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object specifies whether the system processes IPv6
                packets received by the target interface.
                
                This column is valid only if the 'ipv6Enable' bit of the
                corresponding instance of cdtIfValid is '1'.
                ''',
                'cdtifipv6enable',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtIfIpv6NdDadAttempts', ATTRIBUTE, 'int' , None, None, 
                [('0', '600')], [], 
                '''                This object specifies the number of consecutive neighbor
                solitication messages the system sends on the target interface
                while performing duplicate address detection on unicast IPv6
                addresses on the target interface.  The value '0' disables
                duplicate address detection on the target interface.
                
                This column is valid only if the 'ipv6NdDadAttempts' bit of the
                corresponding instance of cdtIfValid is '1'.
                ''',
                'cdtifipv6nddadattempts',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtIfIpv6NdNsInterval', ATTRIBUTE, 'int' , None, None, 
                [('1000', '3600000')], [], 
                '''                This object specifies the interval between neighbor
                solicitation retransmissions on the target interface.
                
                This column is valid only if the 'ipv6NdNsIntervals' bit of the
                corresponding instance of cdtIfValid is '1'.
                ''',
                'cdtifipv6ndnsinterval',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtIfIpv6NdOpts', REFERENCE_BITS, 'Cdtifipv6Ndopts' , 'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB', 'CiscoDynamicTemplateMib.Cdtiftemplatetable.Cdtiftemplateentry.Cdtifipv6Ndopts', 
                [], [], 
                '''                This object specifies options that affect advertisements sent
                on the target interface:
                
                    'advertise'
                        This option specifies that the system should advertise
                        the IPv6 prefix (i.e., the corresponding instance of
                        cdtIfIpv6NdPrefix).
                
                    'onlink'
                        This option specifies that the IPv6 prefix has been
                        assigned to a link.  If set to '0', the system
                        advertises the IPv6 prefix as 'offlink'.
                
                    'router'
                        This option indicates that the router will send the full
                        router address and not set the 'R' bit in prefix
                        advertisements.
                
                    'autoConfig'
                        This option indicates to hosts on the local link that
                        the specified prefix supports IPv6 auto-configuration.
                
                    'advertisementInterval'
                        This option specifies the advertisement interval option
                        in router advertisements sent on the target interface.
                
                    'managedConfigFlag'
                        This option causes the system to set the 'managed
                        address configuration flag' in router advertisements
                        sent on the target interface.
                
                    'otherConfigFlag'
                        This option causes the system to set the 'other stateful
                        configuration' flag in router advertisements sent on the
                        target interface.
                
                    'frameIpv6Prefix'
                        This option causes the system to add the prefix in a
                        received RADIUS framed IPv6 prefix attribute to the
                        target interface's neighbor discovery prefix queue and
                        includes it in router advertisements sent on the target
                        interface.
                
                    'raSupress'
                        This option suppresses the transmission of router
                        advertisements on the target interface.
                
                This column is valid only if the 'ipv6NdOpts' bit of the
                corresponding instance of cdtIfValid is '1'.
                ''',
                'cdtifipv6ndopts',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtIfIpv6NdPreferredLife', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                This object specifies the interval that the system advertises
                the IPv6 prefix (i.e., the corresponding instance of
                cdtIfIpv6NdPrefix) as 'preferred' for IPv6 router advertisements
                sent on the target interface.
                
                This column is valid only if the 'ipv6NdPreferredLife' bit of
                the corresponding instance of cdtIfValid is '1'.
                ''',
                'cdtifipv6ndpreferredlife',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtIfIpv6NdPrefix', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object specifies the IPv6 network number included in
                IPv6 router advertisements sent on the target interface.
                
                This column is valid only if the 'ipv6NdPrefix' bit of
                the corresponding instance of cdtIfValid is '1'.
                ''',
                'cdtifipv6ndprefix',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtIfIpv6NdPrefixLength', ATTRIBUTE, 'int' , None, None, 
                [('0', '2040')], [], 
                '''                This object specifies the length of the IPv6 prefix specified
                by the corresponding instance of cdtIpv6NdPrefix.
                
                This column is valid only if the 'ipv6NdPrefix' bit of the
                corresponding instance of cdtIfValid is '1'.
                ''',
                'cdtifipv6ndprefixlength',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtIfIpv6NdRaIntervalMax', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object specifies the maximum interval between IPv6 router
                advertisements sent on the target interface.
                
                The value '0' cannot be written to an instance of this object.
                However, it serves as a convenient value when the column is not
                valid.
                
                This column is valid only if the 'ipv6NdRaInterval' bit of the
                corresponding instance of cdtIfValid is '1'.
                ''',
                'cdtifipv6ndraintervalmax',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtIfIpv6NdRaIntervalMin', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object specifies the minimum interval between IPv6 router
                advertisements sent on the target interface.  The value of this
                column has the following restrictions:
                
                1)  This value cannot be less than 75% of the value specified
                    for cdtIfIpv6NdRaIntervalMax.
                
                2)  If the corresponding instance of cdtIfIpv6NdRaIntervalUnits
                    is 'seconds', then this value cannot be less than '3'.
                
                3)  If the corresponding instance of cdtIfIpv6NdRaIntervalUnits
                    is 'milliseconds', then this value cannot be less than '30'.
                
                If the target interface template does not specify this value,
                then the system automatically assumes a minimum interval that is
                75% of the corresponding instance of cdtIfIpv6NdRaIntervalMax.
                
                The value '0' cannot be written to an instance of this object.
                However, it serves as a convenient value when the column is not
                valid.
                
                This column is valid only if the 'ipv6NdRaInterval' bit of the
                corresponding instance of cdtIfValid is '1'.
                ''',
                'cdtifipv6ndraintervalmin',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtIfIpv6NdRaIntervalUnits', REFERENCE_ENUM_CLASS, 'Cdtifipv6NdraintervalunitsEnum' , 'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB', 'CiscoDynamicTemplateMib.Cdtiftemplatetable.Cdtiftemplateentry.Cdtifipv6NdraintervalunitsEnum', 
                [], [], 
                '''                This object specifies the units of time for the corresponding
                instances of cdtIfIpv6NdRaIntervalMin and
                cdtIfIpv6NdRaIntervalMax.
                
                This column is valid only if the 'ipv6NdRaInterval' bit of the
                corresponding instance of cdtIfValid is '1'.
                ''',
                'cdtifipv6ndraintervalunits',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtIfIpv6NdRaLife', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object specifies the router lifetime value in IPv6 router
                advertisements sent on the target interface.  The value '0'
                specifies that neighbors should not consider the router as a
                default router.
                ''',
                'cdtifipv6ndralife',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtIfIpv6NdReachableTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object specifies the amount of time the system considers
                a neighbor of the target interface reachable after a
                reachability confirmation event has occurred.  The value '0'
                disables neighbor reachability detection on the target
                interface.
                
                This column is valid only if the 'ipv6NdReachable' bit of the
                corresponding instance of cdtIfValid is '1'.
                ''',
                'cdtifipv6ndreachabletime',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtIfIpv6NdRouterPreference', REFERENCE_ENUM_CLASS, 'Cdtifipv6NdrouterpreferenceEnum' , 'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB', 'CiscoDynamicTemplateMib.Cdtiftemplatetable.Cdtiftemplateentry.Cdtifipv6NdrouterpreferenceEnum', 
                [], [], 
                '''                This object specifies the Default Router Preference (DRP) for
                the router on the target interface.
                
                This column is valid only if the 'ipv6NdRouterPreference' bit of
                the corresponding instance of cdtIfValid is '1'.
                ''',
                'cdtifipv6ndrouterpreference',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtIfIpv6NdValidLife', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                This object specifies the interval that the system advertises
                the IPv6 prefix (i.e., the corresponding instance of
                cdtIfIpv6NdPrefix) as 'valid' for IPv6 router advertisements
                sent on the target interface.
                
                This column is valid only if the 'ipv6NdValidLife' bit of the
                corresponding instance of cdtIfValid is '1'.
                ''',
                'cdtifipv6ndvalidlife',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtIfIpv6SubEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object specifies whether the target interface allows IPv6
                subscriber sessions.
                
                This column is valid only if the 'ipv6SubEnable' bit of the
                corresponding instance of cdtIfValid is '1'.
                ''',
                'cdtifipv6subenable',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtIfIpv6TcpMssAdjust', ATTRIBUTE, 'int' , None, None, 
                [('0', 'None'), ('500', '1460')], [], 
                '''                This object specifies the adjustment to the Maximum Segment
                Size (MSS) of TCP SYN packets received by the target interface
                contained in IPv6 datagrams.
                
                The value '0' cannot be written to an instance of this object.
                However, it serves as a convenient value when the column is not
                valid.
                
                This column is valid only if the 'ipv6TcpMssAdjust' bit of the
                corresponding instance of cdtIfValid is '1'.
                ''',
                'cdtifipv6tcpmssadjust',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtIfIpv6VerifyUniRpf', REFERENCE_ENUM_CLASS, 'UnicastrpftypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB', 'UnicastrpftypeEnum', 
                [], [], 
                '''                This object specifies whether the type of unicast RPF the
                system performs on IPv6 packets received by the target
                interface.
                
                This column is valid only if the 'ipv6VerifyUniRpf' bit of the
                corresponding instance of cdtIfValid is '1'.
                ''',
                'cdtifipv6verifyunirpf',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtIfIpv6VerifyUniRpfAcl', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                This object specifies the name (or number) of the IPv6 ACL
                used to determine whether the system should permit/deny packets
                received by the target interface that fail unicast RPF
                verification.
                
                This column is valid only if the 'ipv6VerifyUniRpfAcl' bit of
                the corresponding instance of cdtIfValid is '1'.
                ''',
                'cdtifipv6verifyunirpfacl',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtIfIpv6VerifyUniRpfOpts', REFERENCE_BITS, 'Unicastrpfoptions' , 'ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB', 'Unicastrpfoptions', 
                [], [], 
                '''                This object specifies the options that affect how the system
                performs unicast RPF on IPv6 packets received by the target
                interface.
                
                This column is valid only if the 'ipv6VerifyUniRpfOpts' bit of
                the corresponding instance of cdtIfValid is '1'.
                ''',
                'cdtifipv6verifyunirpfopts',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtIfMtu', ATTRIBUTE, 'int' , None, None, 
                [('0', 'None'), ('64', '65535')], [], 
                '''                This object specifies the Maximum Transfer Unit (MTU) size for
                all packets sent on the target interface.
                
                The value '0' cannot be written to an instance of this object.
                However, it serves as a convenient value when the column is not
                valid.
                
                This column is valid only if the 'mtu' bit of the corresponding
                instance of cdtIfValid is '1'.
                ''',
                'cdtifmtu',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtIfValid', REFERENCE_BITS, 'Cdtifvalid' , 'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB', 'CiscoDynamicTemplateMib.Cdtiftemplatetable.Cdtiftemplateentry.Cdtifvalid', 
                [], [], 
                '''                This object specifies which attributes in the dynamic template
                have been configured to valid values.
                
                Each bit in this bit string corresponds to a column in this
                table.  If the bit is '0', then the value of the corresponding
                column is not valid.  If the bit is '1', then the value of the
                corresponding column has been configured to a valid value.
                
                The following list specifies the mappings between bits and the
                columns:
                
                    'mtu'                     => cdtIfMtu
                    'cdpEnable'               => cdtIfCdpEnable
                    'flowMonitor'             => cdtIfFlowMonitor
                    'ipv4Unnumbered'          => cdtIfIpv4Unnumbered
                    'ipv4SubEnable'           => cdtIfIpv4SubEnable
                    'ipv4Mtu'                 => cdtIfIpv4Mtu
                    'ipv4TcpMssAdjust'        => cdtIfIpv4TcpMssAdjust
                    'ipv4VerifyUniRpf'        => cdtIfIpv4VerifyUniRpf
                    'ipv4VerifyUniRpfAcl'     => cdtIfIpv4VerifyUniRpfAcl
                    'ipv4VerifyUniRpfOpts'    => cdtIfIpv4VerifyUniRpfOpts
                    'ipv6Enable'              => cdtIfIpv6Enable
                    'ipv6SubEnable'           => cdtIfIpv6SubEnable
                    'ipv6TcpMssAdjust'        => cdtIfIpv6TcpMssAdjust
                    'ipv6VerifyUniRpf'        => cdtIfIpv6VerifyUniRpf
                    'ipv6VerifyUniRpfAcl'     => cdtIfIpv6VerifyUniRpfAcl
                    'ipv6VerifyUniRpfOpts'    => cdtIfIpv6VerifyUniRpfOpts
                    'ipv6NdPrefix'            => cdtIfIpv6NdPrefix,
                                                 cdtIfIpv6NdPrefixLength
                    'ipv6NdValidLife'         => cdtIfIpv6NdValidLife
                    'ipv6NdPreferredLife'     => cdtIfIpv6NdPreferredLife
                    'ipv6NdOpts'              => cdtIfIpv6NdOpts
                    'ipv6NdDadAttempts'       => cdtIfIpv6NdDadAttempts
                    'ipv6NdNsInterval'        => cdtIfIpv6NdNsInterval
                    'ipv6NdReacableTime'      => cdtIfIpv6NdReacableTime
                    'ipv6NdRaIntervalMax'     => cdtIfIpv6NdRaIntervalUnits,
                                                 cdtIfIpv6NdRaIntervalMax
                    'ipv6NdRaIntervalMin'     => cdtIfIpv6NdRaIntervalMin
                    'ipv6NdRaLife'            => cdtIfIpv6NdRaLife
                    'ipv6NdRouterPreference'' => cdtIfIpv6NdRouterPreference
                ''',
                'cdtifvalid',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            ],
            'CISCO-DYNAMIC-TEMPLATE-MIB',
            'cdtIfTemplateEntry',
            _yang_ns._namespaces['CISCO-DYNAMIC-TEMPLATE-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB'
        ),
    },
    'CiscoDynamicTemplateMib.Cdtiftemplatetable' : {
        'meta_info' : _MetaInfoClass('CiscoDynamicTemplateMib.Cdtiftemplatetable',
            False, 
            [
            _MetaInfoClassMember('cdtIfTemplateEntry', REFERENCE_LIST, 'Cdtiftemplateentry' , 'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB', 'CiscoDynamicTemplateMib.Cdtiftemplatetable.Cdtiftemplateentry', 
                [], [], 
                '''                An entry containing attributes relating to interface
                configuration.
                
                The system automatically creates an entry when the system or the
                EMS/NMS creates a row in the cdtTemplateTable with a
                cdtTemplateType of one of the following values:
                
                    'derived'
                    'ppp'
                    'ethernet'
                    'ipSubscriber'
                
                Likewise, the system automatically destroys an entry when the
                system or the EMS/NMS destroys the corresponding row in the
                cdtTemplateTable.
                ''',
                'cdtiftemplateentry',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            ],
            'CISCO-DYNAMIC-TEMPLATE-MIB',
            'cdtIfTemplateTable',
            _yang_ns._namespaces['CISCO-DYNAMIC-TEMPLATE-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB'
        ),
    },
    'CiscoDynamicTemplateMib.Cdtppptemplatetable.Cdtppptemplateentry.CdtpppipcpaddroptionEnum' : _MetaInfoEnum('CdtpppipcpaddroptionEnum', 'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB',
        {
            'other':'other',
            'accept':'accept',
            'required':'required',
            'unique':'unique',
        }, 'CISCO-DYNAMIC-TEMPLATE-MIB', _yang_ns._namespaces['CISCO-DYNAMIC-TEMPLATE-MIB']),
    'CiscoDynamicTemplateMib.Cdtppptemplatetable.Cdtppptemplateentry.CdtpppipcpdnsoptionEnum' : _MetaInfoEnum('CdtpppipcpdnsoptionEnum', 'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB',
        {
            'other':'other',
            'accept':'accept',
            'request':'request',
            'reject':'reject',
        }, 'CISCO-DYNAMIC-TEMPLATE-MIB', _yang_ns._namespaces['CISCO-DYNAMIC-TEMPLATE-MIB']),
    'CiscoDynamicTemplateMib.Cdtppptemplatetable.Cdtppptemplateentry.CdtpppipcpmaskoptionEnum' : _MetaInfoEnum('CdtpppipcpmaskoptionEnum', 'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB',
        {
            'other':'other',
            'request':'request',
            'reject':'reject',
        }, 'CISCO-DYNAMIC-TEMPLATE-MIB', _yang_ns._namespaces['CISCO-DYNAMIC-TEMPLATE-MIB']),
    'CiscoDynamicTemplateMib.Cdtppptemplatetable.Cdtppptemplateentry.CdtpppipcpwinsoptionEnum' : _MetaInfoEnum('CdtpppipcpwinsoptionEnum', 'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB',
        {
            'other':'other',
            'accept':'accept',
            'request':'request',
            'reject':'reject',
        }, 'CISCO-DYNAMIC-TEMPLATE-MIB', _yang_ns._namespaces['CISCO-DYNAMIC-TEMPLATE-MIB']),
    'CiscoDynamicTemplateMib.Cdtppptemplatetable.Cdtppptemplateentry.CdtppppeerdefipaddrsrcEnum' : _MetaInfoEnum('CdtppppeerdefipaddrsrcEnum', 'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB',
        {
            'static':'static',
            'pool':'pool',
            'dhcp':'dhcp',
        }, 'CISCO-DYNAMIC-TEMPLATE-MIB', _yang_ns._namespaces['CISCO-DYNAMIC-TEMPLATE-MIB']),
    'CiscoDynamicTemplateMib.Cdtppptemplatetable.Cdtppptemplateentry' : {
        'meta_info' : _MetaInfoClass('CiscoDynamicTemplateMib.Cdtppptemplatetable.Cdtppptemplateentry',
            False, 
            [
            _MetaInfoClassMember('cdtTemplateName', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                ''',
                'cdttemplatename',
                'CISCO-DYNAMIC-TEMPLATE-MIB', True),
            _MetaInfoClassMember('cdtPppAccounting', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object specifies whether the system applies accounting
                services to the target PPP connection.
                
                This column is valid only if the 'accounting' bit of the
                corresponding instance of cdtPppValid is '1'.
                ''',
                'cdtpppaccounting',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtPppAuthentication', REFERENCE_BITS, 'Cdtpppauthentication' , 'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB', 'CiscoDynamicTemplateMib.Cdtppptemplatetable.Cdtppptemplateentry.Cdtpppauthentication', 
                [], [], 
                '''                This object specifies authentication services applied to a
                target PPP connection and other options affecting authentication
                services:
                
                    'chap'
                        This option enables the Challenge Handshake Protocol (CHAP)
                        on a target PPP connection.
                
                    'msChap'
                        This option enables Microsoft's CHAP on a target PPP
                        connection.
                
                    'msChapV2'
                        This option enables version 2 of Microsoft's CHAP on a
                        target PPP connection.
                
                    'pap'
                        This option enables Password Authentication Protocol (PAP)
                        on a target PPP connection.
                
                    'eap'
                        This option enables Extensible Authentication Protocol (EAP)
                        on a target PPP connection.
                
                    'optional'
                        This option specifies that the system accepts the connection
                        even if the peer of a target PPP connection refuses to
                        accept the authentication methods the system has
                        requested.
                
                    'callin'
                        This option specifies that authentication should only happen
                        for incoming calls.
                
                    'oneTime'
                        This option specifies that the system accepts the username
                        and password in the username field of authentication
                        responses received on a target PPP connection.
                
                This column is valid only if the 'authentication' bit of the
                corresponding instance of cdtPppValid is '1'.
                ''',
                'cdtpppauthentication',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtPppAuthenticationMethods', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                This object specifies the name of a list of authentication
                methods used on a target PPP connection.  If the template does
                not include this attribute, then the system uses the default
                method list.
                
                This column is valid only if the 'authentication' bit of the
                corresponding instance of cdtPppValid is '1'.
                ''',
                'cdtpppauthenticationmethods',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtPppAuthorization', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object specifies whether the system applies authorization
                services to a target PPP connection.
                
                This column is valid only if the 'authorization' bit of the
                corresponding instance of cditPppValid is '1'.
                ''',
                'cdtpppauthorization',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtPppChapHostname', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                This object specifies the hostname sent in a CHAP response
                on a target PPP connection.  If the template does not include
                this attribute, then the system uses its assigned hostname.
                
                This column is valid only if the 'chapHostname' bit of the
                corresponding instance of cdtPppValid is '1'.
                ''',
                'cdtpppchaphostname',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtPppChapOpts', REFERENCE_BITS, 'Cdtpppchapopts' , 'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB', 'CiscoDynamicTemplateMib.Cdtppptemplatetable.Cdtppptemplateentry.Cdtpppchapopts', 
                [], [], 
                '''                This object specifies how the system processes the CHAP on a
                target PPP connection:
                
                    'refuse'
                        This option specifies that the system should refuse CHAP
                        requests from peers of a target PPP connection.
                
                    'callin'
                        This option specifies that the system should only refuse
                        CHAP requests for incoming calls on a target PPP
                        connection.  This option is only relevant if the
                        'refuse' option is set to '1'.
                
                    'wait'
                        This option delays CHAP authentication until after the
                        peer of a target PPP connection has authenticated itself
                        to the system.
                
                    'encrypted'
                        This option specifies that the value specified by the
                        corresponding instance of cdtPppChapPassword is already
                        encrypted.
                
                This column is valid only if the 'chapOpts' bit of the
                corresponding instance of cdtPppValid is '1'.
                ''',
                'cdtpppchapopts',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtPppChapPassword', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                This object specifies the password used to construct a CHAP
                response on the target PPP connection.
                
                This column is valid only if the 'chapPassword' bit of the
                corresponding instance of cdtPppValid is '1'.
                ''',
                'cdtpppchappassword',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtPppEapIdentity', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                This object specifies the identity sent in an EAP response on
                a target PPP connection.
                
                This column is valid only if the 'eapIdentity' bit of the
                corresponding instance of cdtPppValid is '1'.
                ''',
                'cdtpppeapidentity',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtPppEapOpts', REFERENCE_BITS, 'Cdtpppeapopts' , 'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB', 'CiscoDynamicTemplateMib.Cdtppptemplatetable.Cdtppptemplateentry.Cdtpppeapopts', 
                [], [], 
                '''                This object specifies how the system processes the EAP on a
                target PPP connection:
                
                    'refuse'
                        This option specifies that the system should refuse EAP
                        requests from peers of a target PPP connection.
                
                    'callin'
                        This option specifies that the system should only refuse EAP
                        requests for incoming calls on a target PPP connection.
                        This option is only relevant if the 'refuse' option is
                        set to '1'.
                
                    'wait'
                        This option delays EAP authentication until after the
                        peer of a target PPP connection has authenticated itself
                        to the system.
                
                    'local'
                        This option specifies that the system should locally
                        authenticate the peer of a target PPP connection,
                        rather than acting as a proxy to an external AAA server.
                
                This column is valid only if the 'eapOpts' bit of the
                corresponding instance of cdtPppValid is '1'.
                ''',
                'cdtpppeapopts',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtPppEapPassword', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                This object specifies the password used to construct an EAP
                response on a target PPP connection.
                
                This column is valid only if the 'eapPassword' bit of the
                corresponding instance of cdtPppValid is '1'.
                ''',
                'cdtpppeappassword',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtPppIpcpAddrOption', REFERENCE_ENUM_CLASS, 'CdtpppipcpaddroptionEnum' , 'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB', 'CiscoDynamicTemplateMib.Cdtppptemplatetable.Cdtppptemplateentry.CdtpppipcpaddroptionEnum', 
                [], [], 
                '''                This object specifies the IPCP address option for a target PPP
                connection:
                
                    'other'
                        The implementation of this MIB module does not recognize
                        the configured IPCP address option.
                
                    'accept'
                        The system accepts any non-zero IP address from the peer
                        of a target PPP connection.
                
                    'required'
                        The system disconnects the peer of a target PPP
                        connection if it could not negotiate an IP address.
                
                    'unique'
                        The system disconnects the peer of a target PPP
                        connection if the IP address is already in use.
                
                This column is valid only if the 'ipcpAddrOption' bit of the
                corresponding instance of cdtPppValid is '1'.
                ''',
                'cdtpppipcpaddroption',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtPppIpcpDnsOption', REFERENCE_ENUM_CLASS, 'CdtpppipcpdnsoptionEnum' , 'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB', 'CiscoDynamicTemplateMib.Cdtppptemplatetable.Cdtppptemplateentry.CdtpppipcpdnsoptionEnum', 
                [], [], 
                '''                This object specifies the IPCP DNS option for the dynamic
                interface:
                
                    'other'
                        The implementation of this MIB module does not recognize
                        the configured DNS option.
                
                    'accept'
                        The system accepts any non-zero DNS address form the
                        peer of a target PPP connection.
                
                    'request'
                        The system requests the DNS address from the peer of a
                        target PPP connection.
                
                    'reject'
                        The system rejects the DNS option from the peer of a
                        target PPP connection.
                
                This column is valid only if the 'ipcpDnsOption' bit of the
                corresponding instance of cdtPppValid is '1'.
                ''',
                'cdtpppipcpdnsoption',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtPppIpcpDnsPrimary', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object specifies the IP address of the primary DNS server
                offered to the peer of a target PPP connection.
                
                This column is valid only if the 'ipcpDnsPrimary' bit of the
                corresponding instance of cdtPppValid is '1'.
                ''',
                'cdtpppipcpdnsprimary',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtPppIpcpDnsSecondary', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object specifies the IP address of the secondary DNS
                server offered to the peer of a target PPP connection.
                
                This column is valid only if the 'ipcpDnsSecondary' bit of the
                corresponding instance of cdtPppValid is '1'.
                ''',
                'cdtpppipcpdnssecondary',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtPppIpcpMask', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object specifies the IP address mask offered to the peer
                of a target PPP connection.
                
                This column is valid only if the 'ipcpMask' bit of the
                corresponding instance of cdtPppValid is '1'.
                ''',
                'cdtpppipcpmask',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtPppIpcpMaskOption', REFERENCE_ENUM_CLASS, 'CdtpppipcpmaskoptionEnum' , 'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB', 'CiscoDynamicTemplateMib.Cdtppptemplatetable.Cdtppptemplateentry.CdtpppipcpmaskoptionEnum', 
                [], [], 
                '''                This object specifies the IPCP IP subnet mask option for a
                target PPP connection:
                
                    'other'
                        The implementation of this MIB module does not recognize
                        the configured IP subnet mask option.
                
                    'request'
                        The system requests the IP subnet mask from the peer of
                        a target PPP connection.
                
                    'reject'
                        The system rejects the IP subnet mask option from the
                        peer of a target PPP connection.
                
                This column is valid only if the 'ipcpMaskOption' bit of the
                corresponding instance of cdtPppValid is '1'.
                ''',
                'cdtpppipcpmaskoption',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtPppIpcpWinsOption', REFERENCE_ENUM_CLASS, 'CdtpppipcpwinsoptionEnum' , 'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB', 'CiscoDynamicTemplateMib.Cdtppptemplatetable.Cdtppptemplateentry.CdtpppipcpwinsoptionEnum', 
                [], [], 
                '''                This object specifies the IPCP WINS option for a target PPP
                connection:
                
                    'other'
                        The implementation of this MIB module does not recognize
                        the configured WINS option.
                
                    'accept'
                        The system accepts any non-zero WINS address from the
                        peer of a target PPP connection.
                
                    'request'
                        The system requests the WINS address from the peer of
                        a target PPP connection.
                
                    'reject'
                        The system rejects the WINS option from the peer of a
                        target PPP connection.
                
                This column is valid only if the 'ipcpWinsOption' bit of the
                corresponding instance of cdtPppValid is '1'.
                ''',
                'cdtpppipcpwinsoption',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtPppIpcpWinsPrimary', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object specifies the IP address of the primary WINS server
                offered to the peer of a target PPP connection.
                
                This column is valid only if the 'ipcpWinsPrimary' bit of the
                corresponding instance of cdtPppValid is '1'.
                ''',
                'cdtpppipcpwinsprimary',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtPppIpcpWinsSecondary', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object specifies the IP address of the secondary WINS
                server offered to the peer of a target PPP connection.
                
                This column is valid only if the 'ipcpWinsSecondary' bit of the
                corresponding instance of cdtPppValid is '1'.
                ''',
                'cdtpppipcpwinssecondary',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtPppLoopbackIgnore', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object specifies whether the system ignores loopback on
                a target PPP connection.  When the system ignores loopback,
                loopback detection is disabled.
                
                This column is valid only if the 'loopbackIgnore' bit of the
                corresponding instance of cdtPppValid is '1'.
                ''',
                'cdtppploopbackignore',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtPppMaxBadAuth', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object specifies the number of authentication failures
                allowed by the system before a target PPP connection is reset.
                
                The value '0' cannot be written to an instance of this object.
                However, it serves as a convenient value when the column is not
                valid.
                
                This column is valid only if the 'maxBadAuth' bit of the
                corresponding instance of cdtPppValid is '1'.
                ''',
                'cdtpppmaxbadauth',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtPppMaxConfigure', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                This object specifies the number of unacknowledged
                Configure-Request messages a target PPP connection can send
                before the system abandons LCP or NCP negotiations.
                
                This column is valid only if the 'maxConfigure' bit of the
                corresponding instance of cdtPppValid is '1'.
                ''',
                'cdtpppmaxconfigure',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtPppMaxFailure', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                This object specifies the number of Configure-Nak messages a
                target PPP connection can receive before the system abandons LCP
                or NCP negotiations.
                
                This column is valid only if the 'maxFailure' bit of the
                corresponding instance of cdtPppValid is '1'.
                ''',
                'cdtpppmaxfailure',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtPppMaxTerminate', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                This object specifies the number of unacknowledged
                Terminate-Request messages a target PPP connection can send
                before the system abandons LCP or NCP negotiations.
                
                This column is valid only if the 'maxTerminate' bit of the
                corresponding instance of cdtPppValid is '1'.
                ''',
                'cdtpppmaxterminate',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtPppMsChapV1Hostname', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                This object specifies the hostname sent in a Microsoft CHAP
                (v1) response on a target PPP connection.  If the template does
                not include this attribute, then the system uses its assigned
                hostname.
                
                This column is valid only if the 'msChapV1Hostname' bit of the
                corresponding instance of cdtPppValid is '1'.
                ''',
                'cdtpppmschapv1hostname',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtPppMsChapV1Opts', REFERENCE_BITS, 'Cdtpppmschapv1Opts' , 'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB', 'CiscoDynamicTemplateMib.Cdtppptemplatetable.Cdtppptemplateentry.Cdtpppmschapv1Opts', 
                [], [], 
                '''                This object specifies how the system processes version 1 of
                Microsoft CHAP on a target PPP connection:
                
                    'refuse'
                        This option specifies that the system should refuse
                        Microsoft CHAP (v1) requests from peers of a target PPP
                        connection.
                
                    'callin'
                        This option specifies that the system should only refuse
                        Microsoft CHAP (v1) requests for incoming calls on a
                        target PPP connection.  This option is only relevant if
                        the 'refuse' option is set to '1'.
                
                    'wait'
                        This option delays Microsoft CHAP (v1) authentication
                        until after the peer of a target PPP connection has
                        authenticated itself to the system.
                
                    'encrypted'
                        This option specifies that the value specified by the
                        corresponding instance of cdtPppMsChapV1Password is
                        already encrypted.
                
                This column is valid only if the 'msChapV1Opts' bit of the
                corresponding instance of cdtPppValid is '1'.
                ''',
                'cdtpppmschapv1opts',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtPppMsChapV1Password', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                This object specifies the password used to construct a
                Microsoft CHAP (v1) response on a target PPP connection.
                
                This column is valid only if the 'msChapV1Password' bit of the
                corresponding instance of cdtPppValid is '1'.
                ''',
                'cdtpppmschapv1password',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtPppMsChapV2Hostname', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                This object specifies the hostname sent in a Microsoft CHAP
                (v2) response on a target PPP connection.  If the template does
                not include this attribute, then the system uses its assigned
                hostname.
                
                This column is valid only if the 'msChapV2Hostname' bit of the
                corresponding instance of cdtPppValid is '1'.
                ''',
                'cdtpppmschapv2hostname',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtPppMsChapV2Opts', REFERENCE_BITS, 'Cdtpppmschapv2Opts' , 'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB', 'CiscoDynamicTemplateMib.Cdtppptemplatetable.Cdtppptemplateentry.Cdtpppmschapv2Opts', 
                [], [], 
                '''                This object specifies how the system processes version 2 of
                Microsoft CHAP on a target PPP connection:
                
                    'refuse'
                        This option specifies that the system should refuse
                        Microsoft CHAP (v2) requests from peers of a target PPP
                        connection.
                
                    'callin'
                        This option specifies that the system should only refuse
                        Microsoft CHAP (v2) requests for incoming calls on a
                        target PPP connection.  This option is only relevant if
                        the 'refuse' option is set to '1'.
                
                    'wait'
                        This option delays Microsoft CHAP (v2) authentication
                        until after the peer of a target PPP connection has
                        authenticated itself to the system.
                
                    'encrypted'
                        This option specifies that the value specified by the
                        corresponding instance of cdtPppMsChapV2Password is
                        already encrypted.
                
                This column is valid only if the 'msChapV2Opts' bit of the
                corresponding instance of cdtPppValid is '1'.
                ''',
                'cdtpppmschapv2opts',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtPppMsChapV2Password', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                This object specifies the password used to construct a
                Microsoft CHAP (v2) response on a target PPP connection.
                
                This column is valid only if the 'msChapV2Password' bit of the
                corresponding instance of cdtPppValid is '1'.
                ''',
                'cdtpppmschapv2password',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtPppPapOpts', REFERENCE_BITS, 'Cdtppppapopts' , 'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB', 'CiscoDynamicTemplateMib.Cdtppptemplatetable.Cdtppptemplateentry.Cdtppppapopts', 
                [], [], 
                '''                This object specifies how the system processes the PAP on a
                target PPP connection:
                
                    'refuse'
                        This option specifies that the system should refuse PAP
                        requests from peers of a target PPP connection.
                
                    'encrypted'
                        This option specifies that the value specified by the
                        corresponding instance of cdtPppPapSentPassword is
                        already encrypted.
                
                This column is valid only if the 'papOpts' bit of the
                corresponding instance of cdtPppValid is '1'.
                ''',
                'cdtppppapopts',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtPppPapPassword', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                This object specifies the username used to construct a PAP
                response on a target PPP connection.
                
                This column is valid only if the 'papPassword' bit of the
                corresponding instance of cdtPppValid is '1'.
                ''',
                'cdtppppappassword',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtPppPapUsername', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                This object specifies the username sent in a PAP response on
                a target PPP connection.
                
                This column is valid only if the 'papUsername' bit of the
                corresponding instance of cdtPppValid is '1'.
                ''',
                'cdtppppapusername',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtPppPeerDefIpAddr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object specifies the IP address the system assigns to the
                peer of a target PPP connection.
                
                This column is valid only if the 'peerDefIpAddr' bit of the
                corresponding instance of cdtPppValid is '1'.
                ''',
                'cdtppppeerdefipaddr',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtPppPeerDefIpAddrOpts', REFERENCE_BITS, 'Cdtppppeerdefipaddropts' , 'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB', 'CiscoDynamicTemplateMib.Cdtppptemplatetable.Cdtppptemplateentry.Cdtppppeerdefipaddropts', 
                [], [], 
                '''                This object specifies options that affect how the system
                assigns an IP address to the peer of a target PPP connection:
                
                    'ipAddrForced'
                        This option forces the system to assign the next
                        available IP address in the pool to the peer of a
                        target PPP connection.  When disabled, the peer may
                        negotiate a specific IP address or the system can assign
                        the peer its previously assigned IP address.
                
                    'matchAaaPools'
                        This option specifies that the names of the IP address
                        pools provided by an external AAA server must appear in
                        the corresponding list of IP address pool specified by
                        the cdtPppPeerIpAddrPoolTable.
                
                    'backupPools'
                        This option specifies that the corresponding names of
                        the IP address pools specified by the
                        cditPppPeerIpAddrPoolTable serve as backup pools to
                        those provided by an external AAA server.
                
                    'staticPools'
                        This option suppresses an attempt to load pools from an
                        external AAA server when the system encounters a missing
                        pool name.
                
                This column is valid only if the 'peerIpAddrOpts' bit of the
                corresponding instance of cdtPppValid is '1'.
                ''',
                'cdtppppeerdefipaddropts',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtPppPeerDefIpAddrSrc', REFERENCE_ENUM_CLASS, 'CdtppppeerdefipaddrsrcEnum' , 'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB', 'CiscoDynamicTemplateMib.Cdtppptemplatetable.Cdtppptemplateentry.CdtppppeerdefipaddrsrcEnum', 
                [], [], 
                '''                This object specifies how the system assigns an IP address to
                the peer of a target PPP connection:
                
                    'static'
                        The system assigns the IP address specified by the
                        corresponding instance of cdtPppPeerDefIpAddr.
                
                    'pool'
                        The system allocates the first available IP address from
                        the corresponding list of named pools contained by the
                        cdtPppPeerIpAddrPoolTable.
                
                    'dhcp'
                        The system acts as a DHCP proxy-client to obtain an IP
                        address.
                
                This column is valid only if the 'peerDefIpAddrSrc' bit of the
                corresponding instance of cdtPppValid is '1'.
                ''',
                'cdtppppeerdefipaddrsrc',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtPppTimeoutAuthentication', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                This objects specifies the maximum time the system will wait
                for a response to an authentication request on a target PPP
                connection.
                
                This column is valid only if the 'timeoutAuthentication' bit of
                the corresponding instance of cdtPppValid is '1'.
                ''',
                'cdtppptimeoutauthentication',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtPppTimeoutRetry', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                This objects specifies the maximum time the system will wait
                for a response to a PPP control packets on a target PPP
                connection.
                
                This column is valid only if the 'timeoutRetry' bit of the
                corresponding instance of cdtPppValid is '1'.
                ''',
                'cdtppptimeoutretry',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtPppValid', REFERENCE_BITS, 'Cdtpppvalid' , 'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB', 'CiscoDynamicTemplateMib.Cdtppptemplatetable.Cdtppptemplateentry.Cdtpppvalid', 
                [], [], 
                '''                This object specifies which attributes in the dynamic template
                have been configured to valid values.
                
                Each bit in this bit string corresponds to a column in this
                table.  If the bit is '0', then the value of the corresponding
                column is not valid.  If the bit is '1', then the value of the
                corresponding column has been configured to a valid value.
                
                The following list specifies the mappings between bits and the
                columns:
                
                    accounting              => cdtPppAccounting
                    authentication          => cdtPppAuthentication
                    authenticationMethods   => cdtPppAuthenticationMethods
                    authorization           => cdtPppAuthorization
                    loopbackIgnore          => cdtPppLoopbackIgnore
                    maxBadAuth              => cdtPppMaxBadAuth
                    maxConfigure            => cdtPppMaxConfigure
                    maxFailure              => cdtPppMaxFailure
                    maxTerminate            => cdtPppMaxTerminate
                    timeoutAuthentication   => cdtPppTimeoutAuthentication
                    timeoutRetry            => cdtPppTimeoutRetry
                    chapOpts                => cdtPppChapOpts
                    chapHostname            => cdtPppChapHostname
                    chapPassword            => cdtPppChapPassword
                    msChapV1Opts            => cdtPppMsChapV1Opts
                    msChapV1Hostname        => cdtPppMsChapV1Hostname
                    msChapV1Password        => cdtPppMsChapV1Password
                    msChapV2Opts            => cdtPppMsChapV2Opts
                    msChapV2Hostname        => cdtPppMsChapV2Hostname
                    msChapV2Password        => cdtPppMsChapV2Password
                    papOpts                 => cdtPppPapOpts
                    papSentUsername         => cdtPppPapUsername
                    papSentPassword         => cdtPppPapPassword
                    eapOpts                 => cdtPppEapOpts
                    eapIdentity             => cdtPppEapIdentity
                    eapPassword             => cdtPppEapPassword
                    ipcpAddrOption          => cdtPppIpcpAddrOption
                    ipcpDnsOption           => cdtPppIpcpDnsOption
                    ipcpDnsPrimary          => cdtPppIpcpDnsPrimary
                    ipcpDnsSecondary        => cdtPppIpcpDnsSecondary
                    ipcpWinsOption          => cdtPppIpcpWinsOption
                    ipcpWinsPrimary         => cdtPppIpcpWinsPrimary
                    ipcpWinsSecondary       => cdtPppIpcpWinsSecondary
                    ipcpMaskOption          => cdtPppIpcpMaskOption
                    ipcpMask                => cdtPppIpcpMask
                    peerDefIpAddrOpts       => cdtPppPeerOpts
                    peerDefIpAddrSrc        => cdtPppPeerDefIpAddrSrc
                    peerDefIpAddr           => cdtPppPeerDefIpAddr
                ''',
                'cdtpppvalid',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            ],
            'CISCO-DYNAMIC-TEMPLATE-MIB',
            'cdtPppTemplateEntry',
            _yang_ns._namespaces['CISCO-DYNAMIC-TEMPLATE-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB'
        ),
    },
    'CiscoDynamicTemplateMib.Cdtppptemplatetable' : {
        'meta_info' : _MetaInfoClass('CiscoDynamicTemplateMib.Cdtppptemplatetable',
            False, 
            [
            _MetaInfoClassMember('cdtPppTemplateEntry', REFERENCE_LIST, 'Cdtppptemplateentry' , 'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB', 'CiscoDynamicTemplateMib.Cdtppptemplatetable.Cdtppptemplateentry', 
                [], [], 
                '''                An entry containing attributes relating to PPP connection
                configuration.
                
                The system automatically creates an entry when the system or the
                EMS/NMS creates a row in the cdtTemplateTable with a
                cdtTemplateType of one of the following values:
                
                    'derived'
                    'ppp'
                
                Likewise, the system automatically destroys an entry when the
                system or the EMS/NMS destroys the corresponding row in the
                cdtTemplateTable.
                ''',
                'cdtppptemplateentry',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            ],
            'CISCO-DYNAMIC-TEMPLATE-MIB',
            'cdtPppTemplateTable',
            _yang_ns._namespaces['CISCO-DYNAMIC-TEMPLATE-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB'
        ),
    },
    'CiscoDynamicTemplateMib.Cdtppppeeripaddrpooltable.Cdtppppeeripaddrpoolentry' : {
        'meta_info' : _MetaInfoClass('CiscoDynamicTemplateMib.Cdtppppeeripaddrpooltable.Cdtppppeeripaddrpoolentry',
            False, 
            [
            _MetaInfoClassMember('cdtTemplateName', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                ''',
                'cdttemplatename',
                'CISCO-DYNAMIC-TEMPLATE-MIB', True),
            _MetaInfoClassMember('cdtPppPeerIpAddrPoolPriority', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                This object indicates the relative priority of the named pool
                in the list corresponding to a PPP template.  The system
                searches pools in the order of priority, where lower values
                represent higher priority.
                ''',
                'cdtppppeeripaddrpoolpriority',
                'CISCO-DYNAMIC-TEMPLATE-MIB', True),
            _MetaInfoClassMember('cdtPppPeerIpAddrPoolName', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                This object specifies the name of the IP address pool
                associated with the PPP template.
                ''',
                'cdtppppeeripaddrpoolname',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtPppPeerIpAddrPoolStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                This object specifies the status of the entry.  The following
                columns must be valid before activating a subscriber access
                profile:
                
                    - cdtPppPeerIpAddrPoolStorage
                    - cdtPppPeerIpAddrPoolName
                
                However, these objects specify a default value.  Thus, it is
                possible to use create-and-go semantics without setting any
                additional columns.
                
                An implementation must not allow the EMS/NMS to create an entry
                if the corresponding instance of cdtPppPeerIpAddrSrc is not
                'pool'.
                
                An implementation must allow the EMS/NMS to modify any column
                when this column is 'active'.
                ''',
                'cdtppppeeripaddrpoolstatus',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtPppPeerIpAddrPoolStorage', REFERENCE_ENUM_CLASS, 'StoragetypeEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'StoragetypeEnum', 
                [], [], 
                '''                This object specifies what happens to the name pool entry upon
                restart.
                
                If the corresponding instance of cdtTemplateSrc is not 'local',
                then this column must be 'volatile'.
                ''',
                'cdtppppeeripaddrpoolstorage',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            ],
            'CISCO-DYNAMIC-TEMPLATE-MIB',
            'cdtPppPeerIpAddrPoolEntry',
            _yang_ns._namespaces['CISCO-DYNAMIC-TEMPLATE-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB'
        ),
    },
    'CiscoDynamicTemplateMib.Cdtppppeeripaddrpooltable' : {
        'meta_info' : _MetaInfoClass('CiscoDynamicTemplateMib.Cdtppppeeripaddrpooltable',
            False, 
            [
            _MetaInfoClassMember('cdtPppPeerIpAddrPoolEntry', REFERENCE_LIST, 'Cdtppppeeripaddrpoolentry' , 'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB', 'CiscoDynamicTemplateMib.Cdtppppeeripaddrpooltable.Cdtppppeeripaddrpoolentry', 
                [], [], 
                '''                An entry specifies a named pool in a list of pools associated
                with a PPP template.  A PPP template can only have named
                pools associated with it if it has a cdtPppPeerIpAddrSrc of
                'pool'.
                
                Any attempt to create an entry for a PPP template that does not
                have a cdtPppPeerIpAddrSrc of 'pool' must result in a response
                having an error-status of 'inconsistentValue'.
                
                The system automatically creates a corresponding entry when the
                system associates a named pool with a PPP template through
                another management entity (e.g., the system's local console).
                
                The system automatically destroys an entry under the following
                circumstances:
                
                1)  The system or EMS/NMS destroys the corresponding row in the
                    cdtTemplateTable.
                
                2)  The system or EMS/NMS sets the corresponding instance of
                    cdtPppPeerIpAddrSrc with a value other than 'pool'.
                ''',
                'cdtppppeeripaddrpoolentry',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            ],
            'CISCO-DYNAMIC-TEMPLATE-MIB',
            'cdtPppPeerIpAddrPoolTable',
            _yang_ns._namespaces['CISCO-DYNAMIC-TEMPLATE-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB'
        ),
    },
    'CiscoDynamicTemplateMib.Cdtethernettemplatetable.Cdtethernettemplateentry' : {
        'meta_info' : _MetaInfoClass('CiscoDynamicTemplateMib.Cdtethernettemplatetable.Cdtethernettemplateentry',
            False, 
            [
            _MetaInfoClassMember('cdtTemplateName', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                ''',
                'cdttemplatename',
                'CISCO-DYNAMIC-TEMPLATE-MIB', True),
            _MetaInfoClassMember('cdtEthernetBridgeDomain', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                This object specifies the name of the bridge domain...
                ''',
                'cdtethernetbridgedomain',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtEthernetIpv4PointToPoint', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object specifies whether...
                ''',
                'cdtethernetipv4pointtopoint',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtEthernetMacAddr', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                This object specifies the...
                ''',
                'cdtethernetmacaddr',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtEthernetPppoeEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object specifies whether...
                ''',
                'cdtethernetpppoeenable',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtEthernetValid', REFERENCE_BITS, 'Cdtethernetvalid' , 'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB', 'CiscoDynamicTemplateMib.Cdtethernettemplatetable.Cdtethernettemplateentry.Cdtethernetvalid', 
                [], [], 
                '''                This object specifies which attributes in the dynamic template
                have been configured to valid values.
                
                Each bit in this bit string corresponds to a column in this
                table.  If the bit is '0', then the value of the corresponding
                column is not valid.  If the bit is '1', then the value of the
                corresponding column has been configured to a valid value.
                
                The following list specifies the mappings between bits and the
                columns:
                
                    bridgeDomain     => cdtEthernetBridgeDomain
                    pppoeEnable      => cdtEthernetPppoeEnable
                    ipv4PointToPoint => cdtEthernetIpv4PointToPoint
                    macAddr          => cdtEthernetMacAddr
                ''',
                'cdtethernetvalid',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            ],
            'CISCO-DYNAMIC-TEMPLATE-MIB',
            'cdtEthernetTemplateEntry',
            _yang_ns._namespaces['CISCO-DYNAMIC-TEMPLATE-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB'
        ),
    },
    'CiscoDynamicTemplateMib.Cdtethernettemplatetable' : {
        'meta_info' : _MetaInfoClass('CiscoDynamicTemplateMib.Cdtethernettemplatetable',
            False, 
            [
            _MetaInfoClassMember('cdtEthernetTemplateEntry', REFERENCE_LIST, 'Cdtethernettemplateentry' , 'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB', 'CiscoDynamicTemplateMib.Cdtethernettemplatetable.Cdtethernettemplateentry', 
                [], [], 
                '''                An entry containing attributes relating to dynamic interfaces
                initiated on Ethernet virtual interfaces (e.g., EoMPLS) or
                automatically created VLANs.
                
                The system automatically creates an entry when the system or the
                EMS/NMS creates a row in the cdtTemplateTable with a
                cdtTemplateType of one of the following values:
                
                    'derived'
                    'ethernet'
                
                Likewise, the system automatically destroys an entry when the
                system or the EMS/NMS destroys the corresponding row in the
                cdtTemplateTable.
                ''',
                'cdtethernettemplateentry',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            ],
            'CISCO-DYNAMIC-TEMPLATE-MIB',
            'cdtEthernetTemplateTable',
            _yang_ns._namespaces['CISCO-DYNAMIC-TEMPLATE-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB'
        ),
    },
    'CiscoDynamicTemplateMib.Cdtsrvtemplatetable.Cdtsrvtemplateentry.CdtsrvnetworksrvEnum' : _MetaInfoEnum('CdtsrvnetworksrvEnum', 'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB',
        {
            'other':'other',
            'none':'none',
            'local':'local',
            'vpdn':'vpdn',
        }, 'CISCO-DYNAMIC-TEMPLATE-MIB', _yang_ns._namespaces['CISCO-DYNAMIC-TEMPLATE-MIB']),
    'CiscoDynamicTemplateMib.Cdtsrvtemplatetable.Cdtsrvtemplateentry.CdtsrvsgsrvtypeEnum' : _MetaInfoEnum('CdtsrvsgsrvtypeEnum', 'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB',
        {
            'primary':'primary',
            'secondary':'secondary',
        }, 'CISCO-DYNAMIC-TEMPLATE-MIB', _yang_ns._namespaces['CISCO-DYNAMIC-TEMPLATE-MIB']),
    'CiscoDynamicTemplateMib.Cdtsrvtemplatetable.Cdtsrvtemplateentry' : {
        'meta_info' : _MetaInfoClass('CiscoDynamicTemplateMib.Cdtsrvtemplatetable.Cdtsrvtemplateentry',
            False, 
            [
            _MetaInfoClassMember('cdtTemplateName', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                ''',
                'cdttemplatename',
                'CISCO-DYNAMIC-TEMPLATE-MIB', True),
            _MetaInfoClassMember('cdtSrvMulticast', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This objects specifies whether the system enables multicast
                service for subscriber sessions of the target service.
                
                This column is valid only if the 'sgSrvMcastRoutingIf' bit of
                the corresponding instance of cdtSrvValid is '1'.
                ''',
                'cdtsrvmulticast',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtSrvNetworkSrv', REFERENCE_ENUM_CLASS, 'CdtsrvnetworksrvEnum' , 'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB', 'CiscoDynamicTemplateMib.Cdtsrvtemplatetable.Cdtsrvtemplateentry.CdtsrvnetworksrvEnum', 
                [], [], 
                '''                This object specifies the type of network service provided by
                the target service:
                
                    'other'
                        The implementation of this MIB module does not recognize
                        the configured network service.
                
                    'none'
                        The target subscriber service does not provide a network
                        service to subscribers sessions.
                
                    'local'
                        The target subscriber service provides local termination
                        for subscriber sessions.
                
                    'vpdn'
                        The target subscriber service provides a Virtual Private
                        Dialup Network service for subscriber sessions.
                
                This column is valid only if the 'networkSrv' bit of the
                corresponding instance of cdtSrvValid is '1'.
                ''',
                'cdtsrvnetworksrv',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtSrvSgSrvGroup', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                This object specifies the name of the service group with which
                the system associates subscriber sessions.  A service group
                specifies a set of services that may be active simultaneously
                for a given subscriber session.  Typically, a service group
                contains a primary service and one or more secondary services.
                
                This column is valid only if the 'sgSrvGroup' bit of the
                corresponding instance of cdtSrvValid is '1'.
                ''',
                'cdtsrvsgsrvgroup',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtSrvSgSrvType', REFERENCE_ENUM_CLASS, 'CdtsrvsgsrvtypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB', 'CiscoDynamicTemplateMib.Cdtsrvtemplatetable.Cdtsrvtemplateentry.CdtsrvsgsrvtypeEnum', 
                [], [], 
                '''                This object specifies whether the target service specifies a
                network-forwarding policy:
                
                    'primary'
                        The target service specifies a network-forwarding
                        policy.  Primary services are mutually exclusive; that
                        is, only one primary service can be activated for any
                        given subscriber session.
                
                    'secondary'
                        The target service has a dependence on the primary
                        service in the group specified by the corresponding
                        instance of cdtSuBSrvSgSrvGroup.  After the system
                        activates the primary service, it activates secondary
                        services.  When the system deactivates the primary
                        service, then it deactivates all the secondary services
                        in the service group.
                
                This column is valid only if the 'sgSrvType' bit of the
                corresponding instance of cdtSrvValid is '1'.
                ''',
                'cdtsrvsgsrvtype',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtSrvValid', REFERENCE_BITS, 'Cdtsrvvalid' , 'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB', 'CiscoDynamicTemplateMib.Cdtsrvtemplatetable.Cdtsrvtemplateentry.Cdtsrvvalid', 
                [], [], 
                '''                This object specifies which attributes in the dynamic template
                have been configured to valid values.
                
                Each bit in this bit string corresponds to a column in this
                table.  If the bit is '0', then the value of the corresponding
                column is not valid.  If the bit is '1', then the value of the
                corresponding column has been configured to a valid value.
                
                The following list specifies the mappings between bits and the
                columns:
                
                    networkSrv     => cdtSrvNetworkSrv
                    vpdnGroup      => cdtSrvVpdnGroup
                    sgSrvGroup     => cdtSrvGroup
                    sgSrvType      => cdtSrvSgSrvType
                    multicast      => cdtSrvMulticast
                ''',
                'cdtsrvvalid',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtSrvVpdnGroup', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                This object specifies the name of the VPDN group used to
                configure the network service.
                
                This column is valid only if the 'vpdnGroup' bit of the
                corresponding instance of cdtSrvValid is '1'.
                ''',
                'cdtsrvvpdngroup',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            ],
            'CISCO-DYNAMIC-TEMPLATE-MIB',
            'cdtSrvTemplateEntry',
            _yang_ns._namespaces['CISCO-DYNAMIC-TEMPLATE-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB'
        ),
    },
    'CiscoDynamicTemplateMib.Cdtsrvtemplatetable' : {
        'meta_info' : _MetaInfoClass('CiscoDynamicTemplateMib.Cdtsrvtemplatetable',
            False, 
            [
            _MetaInfoClassMember('cdtSrvTemplateEntry', REFERENCE_LIST, 'Cdtsrvtemplateentry' , 'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB', 'CiscoDynamicTemplateMib.Cdtsrvtemplatetable.Cdtsrvtemplateentry', 
                [], [], 
                '''                An entry containing attributes relating to a service.
                
                The system automatically creates entry when the system or the
                EMS/NMS creates a row in the cdtTemplateTable with a
                cdtTemplateType of one of the following values:
                
                    'derived'
                    'service'
                
                Likewise, the system automatically destroys an entry when the
                system or the EMS/NMS destroys the corresponding row in the
                cdtTemplateTable.
                ''',
                'cdtsrvtemplateentry',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            ],
            'CISCO-DYNAMIC-TEMPLATE-MIB',
            'cdtSrvTemplateTable',
            _yang_ns._namespaces['CISCO-DYNAMIC-TEMPLATE-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB'
        ),
    },
    'CiscoDynamicTemplateMib' : {
        'meta_info' : _MetaInfoClass('CiscoDynamicTemplateMib',
            False, 
            [
            _MetaInfoClassMember('cdtEthernetTemplateTable', REFERENCE_CLASS, 'Cdtethernettemplatetable' , 'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB', 'CiscoDynamicTemplateMib.Cdtethernettemplatetable', 
                [], [], 
                '''                This table contains attributes relating to dynamic interfaces
                initiated on Ethernet virtual interfaces (e.g., EoMPLS) or
                automatically created VLANs.
                
                This table has a sparse-dependent relationship on the
                cdtTemplateTable, containing a row for each dynamic template
                having a cdtTemplateType of one of the following values:
                
                    'derived'
                    'ethernet'
                ''',
                'cdtethernettemplatetable',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtIfTemplateTable', REFERENCE_CLASS, 'Cdtiftemplatetable' , 'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB', 'CiscoDynamicTemplateMib.Cdtiftemplatetable', 
                [], [], 
                '''                This table contains attributes relating to interface
                configuration.
                
                This table has a sparse-dependent relationship on the
                cdtTemplateTable, containing a row for each dynamic template
                having a cdtTemplateType of one of the following values:
                
                    'derived'
                    'ppp'
                    'ethernet'
                    'ipSubscriber'
                ''',
                'cdtiftemplatetable',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtPppPeerIpAddrPoolTable', REFERENCE_CLASS, 'Cdtppppeeripaddrpooltable' , 'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB', 'CiscoDynamicTemplateMib.Cdtppppeeripaddrpooltable', 
                [], [], 
                '''                This table contains a prioritized list of named pools for each
                PPP template.  A list corresponding to a PPP template
                specifies the pools the system searches in an attempt to
                assign an IP address to the peer of a target PPP connection.
                The system searches the pools in the order of their priority.
                
                This table has an expansion dependent relationship on the
                cdtPppTemplateTable, containing zero or more rows for each PPP
                template.
                ''',
                'cdtppppeeripaddrpooltable',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtPppTemplateTable', REFERENCE_CLASS, 'Cdtppptemplatetable' , 'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB', 'CiscoDynamicTemplateMib.Cdtppptemplatetable', 
                [], [], 
                '''                This table contains attributes relating to PPP connection
                configuration.
                
                This table has a sparse-dependent relationship on the
                cdtTemplateTable, containing a row for each dynamic template
                having a cdtTemplateType of one of the following values:
                
                    'derived'
                    'ppp'
                ''',
                'cdtppptemplatetable',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtSrvTemplateTable', REFERENCE_CLASS, 'Cdtsrvtemplatetable' , 'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB', 'CiscoDynamicTemplateMib.Cdtsrvtemplatetable', 
                [], [], 
                '''                This table contains attributes relating to a service.
                
                This table has a sparse-dependent relationship on the
                cdtTemplateTable, containing a row for each dynamic template
                having a cdtTemplateType of one of the following values:
                
                    'derived'
                    'service'
                ''',
                'cdtsrvtemplatetable',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtTemplateAssociationTable', REFERENCE_CLASS, 'Cdttemplateassociationtable' , 'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB', 'CiscoDynamicTemplateMib.Cdttemplateassociationtable', 
                [], [], 
                '''                This table contains a list of templates associated with each
                target.
                
                This table has an expansion dependent relationship on the
                cdtTemplateTargetTable, containing zero or more rows for each
                target.
                ''',
                'cdttemplateassociationtable',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtTemplateCommonTable', REFERENCE_CLASS, 'Cdttemplatecommontable' , 'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB', 'CiscoDynamicTemplateMib.Cdttemplatecommontable', 
                [], [], 
                '''                This table contains attributes relating to all dynamic
                templates.  Observe that the type of dynamic templates
                containing these attributes may change with the addition of new
                dynamic template types.
                
                This table has a sparse-dependent relationship on the
                cdtTemplateTable, containing a row for each dynamic template
                having a cdtTemplateType of one of the following values:
                
                    'derived'
                    'ppp'
                    'ethernet'
                    'ipSubscriber'
                    'service'
                ''',
                'cdttemplatecommontable',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtTemplateTable', REFERENCE_CLASS, 'Cdttemplatetable' , 'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB', 'CiscoDynamicTemplateMib.Cdttemplatetable', 
                [], [], 
                '''                This table lists the dynamic templates maintained by the
                system, including those that have been locally-configured on the
                system and those pushed to the system by external policy
                servers.
                ''',
                'cdttemplatetable',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtTemplateTargetTable', REFERENCE_CLASS, 'Cdttemplatetargettable' , 'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB', 'CiscoDynamicTemplateMib.Cdttemplatetargettable', 
                [], [], 
                '''                This table contains a list of targets associated with
                one or more dynamic templates.
                ''',
                'cdttemplatetargettable',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            _MetaInfoClassMember('cdtTemplateUsageTable', REFERENCE_CLASS, 'Cdttemplateusagetable' , 'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB', 'CiscoDynamicTemplateMib.Cdttemplateusagetable', 
                [], [], 
                '''                This table contains a list of targets using each dynamic
                template.
                
                This table has an expansion dependent relationship on the
                cdtTemplateTable, containing zero or more rows for each
                dynamic template.
                ''',
                'cdttemplateusagetable',
                'CISCO-DYNAMIC-TEMPLATE-MIB', False),
            ],
            'CISCO-DYNAMIC-TEMPLATE-MIB',
            'CISCO-DYNAMIC-TEMPLATE-MIB',
            _yang_ns._namespaces['CISCO-DYNAMIC-TEMPLATE-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB'
        ),
    },
}
_meta_table['CiscoDynamicTemplateMib.Cdttemplatetable.Cdttemplateentry']['meta_info'].parent =_meta_table['CiscoDynamicTemplateMib.Cdttemplatetable']['meta_info']
_meta_table['CiscoDynamicTemplateMib.Cdttemplatetargettable.Cdttemplatetargetentry']['meta_info'].parent =_meta_table['CiscoDynamicTemplateMib.Cdttemplatetargettable']['meta_info']
_meta_table['CiscoDynamicTemplateMib.Cdttemplateassociationtable.Cdttemplateassociationentry']['meta_info'].parent =_meta_table['CiscoDynamicTemplateMib.Cdttemplateassociationtable']['meta_info']
_meta_table['CiscoDynamicTemplateMib.Cdttemplateusagetable.Cdttemplateusageentry']['meta_info'].parent =_meta_table['CiscoDynamicTemplateMib.Cdttemplateusagetable']['meta_info']
_meta_table['CiscoDynamicTemplateMib.Cdttemplatecommontable.Cdttemplatecommonentry']['meta_info'].parent =_meta_table['CiscoDynamicTemplateMib.Cdttemplatecommontable']['meta_info']
_meta_table['CiscoDynamicTemplateMib.Cdtiftemplatetable.Cdtiftemplateentry']['meta_info'].parent =_meta_table['CiscoDynamicTemplateMib.Cdtiftemplatetable']['meta_info']
_meta_table['CiscoDynamicTemplateMib.Cdtppptemplatetable.Cdtppptemplateentry']['meta_info'].parent =_meta_table['CiscoDynamicTemplateMib.Cdtppptemplatetable']['meta_info']
_meta_table['CiscoDynamicTemplateMib.Cdtppppeeripaddrpooltable.Cdtppppeeripaddrpoolentry']['meta_info'].parent =_meta_table['CiscoDynamicTemplateMib.Cdtppppeeripaddrpooltable']['meta_info']
_meta_table['CiscoDynamicTemplateMib.Cdtethernettemplatetable.Cdtethernettemplateentry']['meta_info'].parent =_meta_table['CiscoDynamicTemplateMib.Cdtethernettemplatetable']['meta_info']
_meta_table['CiscoDynamicTemplateMib.Cdtsrvtemplatetable.Cdtsrvtemplateentry']['meta_info'].parent =_meta_table['CiscoDynamicTemplateMib.Cdtsrvtemplatetable']['meta_info']
_meta_table['CiscoDynamicTemplateMib.Cdttemplatetable']['meta_info'].parent =_meta_table['CiscoDynamicTemplateMib']['meta_info']
_meta_table['CiscoDynamicTemplateMib.Cdttemplatetargettable']['meta_info'].parent =_meta_table['CiscoDynamicTemplateMib']['meta_info']
_meta_table['CiscoDynamicTemplateMib.Cdttemplateassociationtable']['meta_info'].parent =_meta_table['CiscoDynamicTemplateMib']['meta_info']
_meta_table['CiscoDynamicTemplateMib.Cdttemplateusagetable']['meta_info'].parent =_meta_table['CiscoDynamicTemplateMib']['meta_info']
_meta_table['CiscoDynamicTemplateMib.Cdttemplatecommontable']['meta_info'].parent =_meta_table['CiscoDynamicTemplateMib']['meta_info']
_meta_table['CiscoDynamicTemplateMib.Cdtiftemplatetable']['meta_info'].parent =_meta_table['CiscoDynamicTemplateMib']['meta_info']
_meta_table['CiscoDynamicTemplateMib.Cdtppptemplatetable']['meta_info'].parent =_meta_table['CiscoDynamicTemplateMib']['meta_info']
_meta_table['CiscoDynamicTemplateMib.Cdtppppeeripaddrpooltable']['meta_info'].parent =_meta_table['CiscoDynamicTemplateMib']['meta_info']
_meta_table['CiscoDynamicTemplateMib.Cdtethernettemplatetable']['meta_info'].parent =_meta_table['CiscoDynamicTemplateMib']['meta_info']
_meta_table['CiscoDynamicTemplateMib.Cdtsrvtemplatetable']['meta_info'].parent =_meta_table['CiscoDynamicTemplateMib']['meta_info']
