""" confd_dyncfg 

This module defines the Tail\-f ConfD configuration parameters
that can be modified in runtime.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Auditusernametype(Enum):
    """
    Auditusernametype

    .. data:: always = 1980885055

    .. data:: known = 584303659

    .. data:: never = 1258673503

    """

    always = Enum.YLeaf(1980885055, "always")

    known = Enum.YLeaf(584303659, "known")

    never = Enum.YLeaf(1258673503, "never")


class Bsdfacilitytype(Enum):
    """
    Bsdfacilitytype

    .. data:: daemon = 137874048

    .. data:: authpriv = 2143429981

    .. data:: local0 = 1223389442

    .. data:: local1 = 659974174

    .. data:: local2 = 388815177

    .. data:: local3 = 133202671

    .. data:: local4 = 1369253367

    .. data:: local5 = 37794477

    .. data:: local6 = 918612352

    .. data:: local7 = 1098748970

    """

    daemon = Enum.YLeaf(137874048, "daemon")

    authpriv = Enum.YLeaf(2143429981, "authpriv")

    local0 = Enum.YLeaf(1223389442, "local0")

    local1 = Enum.YLeaf(659974174, "local1")

    local2 = Enum.YLeaf(388815177, "local2")

    local3 = Enum.YLeaf(133202671, "local3")

    local4 = Enum.YLeaf(1369253367, "local4")

    local5 = Enum.YLeaf(37794477, "local5")

    local6 = Enum.YLeaf(918612352, "local6")

    local7 = Enum.YLeaf(1098748970, "local7")


class Bsdfacilitytype(Enum):
    """
    Bsdfacilitytype

    .. data:: daemon = 137874048

    .. data:: authpriv = 2143429981

    .. data:: local0 = 1223389442

    .. data:: local1 = 659974174

    .. data:: local2 = 388815177

    .. data:: local3 = 133202671

    .. data:: local4 = 1369253367

    .. data:: local5 = 37794477

    .. data:: local6 = 918612352

    .. data:: local7 = 1098748970

    """

    daemon = Enum.YLeaf(137874048, "daemon")

    authpriv = Enum.YLeaf(2143429981, "authpriv")

    local0 = Enum.YLeaf(1223389442, "local0")

    local1 = Enum.YLeaf(659974174, "local1")

    local2 = Enum.YLeaf(388815177, "local2")

    local3 = Enum.YLeaf(133202671, "local3")

    local4 = Enum.YLeaf(1369253367, "local4")

    local5 = Enum.YLeaf(37794477, "local5")

    local6 = Enum.YLeaf(918612352, "local6")

    local7 = Enum.YLeaf(1098748970, "local7")


class Candidateimplementationtype(Enum):
    """
    Candidateimplementationtype

    .. data:: confd = 664387550

    .. data:: external = 1055777754

    """

    confd = Enum.YLeaf(664387550, "confd")

    external = Enum.YLeaf(1055777754, "external")


class Candidatestoragetype(Enum):
    """
    Candidatestoragetype

    .. data:: disk = 334675513

    .. data:: ram = 781613798

    .. data:: auto = 1146214388

    """

    disk = Enum.YLeaf(334675513, "disk")

    ram = Enum.YLeaf(781613798, "ram")

    auto = Enum.YLeaf(1146214388, "auto")


class Cliactionmaptype(Enum):
    """
    Cliactionmaptype

    .. data:: both = 1577301616

    .. data:: config = 2105663071

    .. data:: oper = 1313484953

    """

    both = Enum.YLeaf(1577301616, "both")

    config = Enum.YLeaf(2105663071, "config")

    oper = Enum.YLeaf(1313484953, "oper")


class Cliauditlogtype(Enum):
    """
    Cliauditlogtype

    .. data:: all = 2031982792

    .. data:: none = 432063804

    .. data:: denied = 1293974345

    .. data:: allowed = 1631106802

    """

    all = Enum.YLeaf(2031982792, "all")

    none = Enum.YLeaf(432063804, "none")

    denied = Enum.YLeaf(1293974345, "denied")

    allowed = Enum.YLeaf(1631106802, "allowed")


class Climodenamestyletype(Enum):
    """
    Climodenamestyletype

    .. data:: short = 2029155337

    .. data:: two = 87009233

    .. data:: full = 476261018

    """

    short = Enum.YLeaf(2029155337, "short")

    two = Enum.YLeaf(87009233, "two")

    full = Enum.YLeaf(476261018, "full")


class Clistyle(Enum):
    """
    Clistyle

    .. data:: j = 641834109

    .. data:: c = 589337185

    .. data:: i = 1541010383

    """

    j = Enum.YLeaf(641834109, "j")

    c = Enum.YLeaf(589337185, "c")

    i = Enum.YLeaf(1541010383, "i")


class Clitimezonetype(Enum):
    """
    Clitimezonetype

    .. data:: utc = 1427039597

    .. data:: local = 2129802687

    """

    utc = Enum.YLeaf(1427039597, "utc")

    local = Enum.YLeaf(2129802687, "local")


class Completionmetainfotype(Enum):
    """
    Completionmetainfotype

    .. data:: false = 1249155036

    .. data:: alt1 = 1173421906

    .. data:: alt2 = 780021010

    """

    false = Enum.YLeaf(1249155036, "false")

    alt1 = Enum.YLeaf(1173421906, "alt1")

    alt2 = Enum.YLeaf(780021010, "alt2")


class Configurationreplicationtype(Enum):
    """
    Configurationreplicationtype

    .. data:: async = 1368962940

    .. data:: sync = 2047869128

    """

    async = Enum.YLeaf(1368962940, "async")

    sync = Enum.YLeaf(2047869128, "sync")


class Confirmuncommitedonexittype(Enum):
    """
    Confirmuncommitedonexittype

    .. data:: prompt = 1796253006

    .. data:: discard = 664427145

    .. data:: commit = 128787545

    """

    prompt = Enum.YLeaf(1796253006, "prompt")

    discard = Enum.YLeaf(664427145, "discard")

    commit = Enum.YLeaf(128787545, "commit")


class Crypthashalgorithmtype(Enum):
    """
    Crypthashalgorithmtype

    .. data:: md5 = 721897608

    .. data:: sha_256 = 1426210322

    .. data:: sha_512 = 945188773

    """

    md5 = Enum.YLeaf(721897608, "md5")

    sha_256 = Enum.YLeaf(1426210322, "sha-256")

    sha_512 = Enum.YLeaf(945188773, "sha-512")


class Dbaccesstype(Enum):
    """
    Dbaccesstype

    .. data:: read_write = 1464236954

    .. data:: writable_through_candidate = 532826246

    """

    read_write = Enum.YLeaf(1464236954, "read-write")

    writable_through_candidate = Enum.YLeaf(532826246, "writable-through-candidate")


class Defaulthandlingmodetype(Enum):
    """
    Defaulthandlingmodetype

    .. data:: explicit = 920928367

    .. data:: trim = 250701330

    .. data:: report_all = 1824535838

    """

    explicit = Enum.YLeaf(920928367, "explicit")

    trim = Enum.YLeaf(250701330, "trim")

    report_all = Enum.YLeaf(1824535838, "report-all")


class Developerlogleveltype(Enum):
    """
    Developerlogleveltype

    .. data:: error = 126243105

    .. data:: info = 2062105651

    .. data:: trace = 1896625767

    """

    error = Enum.YLeaf(126243105, "error")

    info = Enum.YLeaf(2062105651, "info")

    trace = Enum.YLeaf(1896625767, "trace")


class Editwrapmodetype(Enum):
    """
    Editwrapmodetype

    .. data:: wrap = 1386835265

    .. data:: newline = 100405574

    .. data:: vt100 = 321017956

    """

    wrap = Enum.YLeaf(1386835265, "wrap")

    newline = Enum.YLeaf(100405574, "newline")

    vt100 = Enum.YLeaf(321017956, "vt100")


class Enabledisplayleveltype(Enum):
    """
    Enabledisplayleveltype

    .. data:: true = 1808796341

    .. data:: false = 1249155036

    .. data:: pipe = 612053909

    """

    true = Enum.YLeaf(1808796341, "true")

    false = Enum.YLeaf(1249155036, "false")

    pipe = Enum.YLeaf(612053909, "pipe")


class Expirationwarningtype(Enum):
    """
    Expirationwarningtype

    .. data:: ignore = 1852995428

    .. data:: display = 2135153981

    .. data:: prompt = 1796253006

    """

    ignore = Enum.YLeaf(1852995428, "ignore")

    display = Enum.YLeaf(2135153981, "display")

    prompt = Enum.YLeaf(1796253006, "prompt")


class Falsetype(Enum):
    """
    Falsetype

    .. data:: false = 1249155036

    """

    false = Enum.YLeaf(1249155036, "false")


class Falsetype(Enum):
    """
    Falsetype

    .. data:: false = 1249155036

    """

    false = Enum.YLeaf(1249155036, "false")


class Fixedidtype(Enum):
    """
    Fixedidtype

    .. data:: confd = 664387550

    .. data:: user = 1529217067

    .. data:: root = 1945751049

    """

    confd = Enum.YLeaf(664387550, "confd")

    user = Enum.YLeaf(1529217067, "user")

    root = Enum.YLeaf(1945751049, "root")


class Fixedidtype(Enum):
    """
    Fixedidtype

    .. data:: confd = 664387550

    .. data:: user = 1529217067

    .. data:: root = 1945751049

    """

    confd = Enum.YLeaf(664387550, "confd")

    user = Enum.YLeaf(1529217067, "user")

    root = Enum.YLeaf(1945751049, "root")


class Infinitytype(Enum):
    """
    Infinitytype

    .. data:: infinity = 1378257424

    """

    infinity = Enum.YLeaf(1378257424, "infinity")


class Infinitytype(Enum):
    """
    Infinitytype

    .. data:: infinity = 1378257424

    """

    infinity = Enum.YLeaf(1378257424, "infinity")


class Journalcompactiontype(Enum):
    """
    Journalcompactiontype

    .. data:: automatic = 1726921432

    .. data:: manual = 48828153

    """

    automatic = Enum.YLeaf(1726921432, "automatic")

    manual = Enum.YLeaf(48828153, "manual")


class Modeinfoinaaatype(Enum):
    """
    Modeinfoinaaatype

    .. data:: true = 1808796341

    .. data:: false = 1249155036

    .. data:: path = 1002915403

    """

    true = Enum.YLeaf(1808796341, "true")

    false = Enum.YLeaf(1249155036, "false")

    path = Enum.YLeaf(1002915403, "path")


class Modeinfoinaudittype(Enum):
    """
    Modeinfoinaudittype

    .. data:: true = 1808796341

    .. data:: false = 1249155036

    .. data:: path = 1002915403

    """

    true = Enum.YLeaf(1808796341, "true")

    false = Enum.YLeaf(1249155036, "false")

    path = Enum.YLeaf(1002915403, "path")


class Multipatternoperationtype(Enum):
    """
    Multipatternoperationtype

    .. data:: any = 383440309

    .. data:: all = 2031982792

    """

    any = Enum.YLeaf(383440309, "any")

    all = Enum.YLeaf(2031982792, "all")


class Netconftraceformattype(Enum):
    """
    Netconftraceformattype

    .. data:: pretty = 560733322

    .. data:: raw = 764753385

    """

    pretty = Enum.YLeaf(560733322, "pretty")

    raw = Enum.YLeaf(764753385, "raw")


class Operationalpersistenttype(Enum):
    """
    Operationalpersistenttype

    .. data:: confspec = 2093298699

    .. data:: always = 1980885055

    .. data:: never = 1258673503

    """

    confspec = Enum.YLeaf(2093298699, "confspec")

    always = Enum.YLeaf(1980885055, "always")

    never = Enum.YLeaf(1258673503, "never")


class Operationalreplicationmodetype(Enum):
    """
    Operationalreplicationmodetype

    .. data:: async = 1368962940

    .. data:: sync = 2047869128

    """

    async = Enum.YLeaf(1368962940, "async")

    sync = Enum.YLeaf(2047869128, "sync")


class Operationalreplicationtype(Enum):
    """
    Operationalreplicationtype

    .. data:: never = 1258673503

    .. data:: always = 1980885055

    .. data:: persistent = 1783422916

    """

    never = Enum.YLeaf(1258673503, "never")

    always = Enum.YLeaf(1980885055, "always")

    persistent = Enum.YLeaf(1783422916, "persistent")


class Pendingchangesactiontype(Enum):
    """
    Pendingchangesactiontype

    .. data:: continue_ = 1852005625

    .. data:: fail = 1504483183

    """

    continue_ = Enum.YLeaf(1852005625, "continue")

    fail = Enum.YLeaf(1504483183, "fail")


class Pipehelpmodetype(Enum):
    """
    Pipehelpmodetype

    .. data:: always = 1980885055

    .. data:: auto = 1146214388

    .. data:: never = 1258673503

    """

    always = Enum.YLeaf(1980885055, "always")

    auto = Enum.YLeaf(1146214388, "auto")

    never = Enum.YLeaf(1258673503, "never")


class Pubkeyauthenticationtype(Enum):
    """
    Pubkeyauthenticationtype

    .. data:: none = 432063804

    .. data:: local = 2129802687

    .. data:: system = 1534086422

    """

    none = Enum.YLeaf(432063804, "none")

    local = Enum.YLeaf(2129802687, "local")

    system = Enum.YLeaf(1534086422, "system")


class Quotestyletype(Enum):
    """
    Quotestyletype

    .. data:: quote = 883581901

    .. data:: backslash = 1857839842

    """

    quote = Enum.YLeaf(883581901, "quote")

    backslash = Enum.YLeaf(1857839842, "backslash")


class Rollbacktype(Enum):
    """
    Rollbacktype

    .. data:: full = 476261018

    .. data:: delta = 1928409309

    """

    full = Enum.YLeaf(476261018, "full")

    delta = Enum.YLeaf(1928409309, "delta")


class Rollnumbering(Enum):
    """
    Rollnumbering

    .. data:: fixed = 1180146474

    .. data:: rolling = 492733776

    """

    fixed = Enum.YLeaf(1180146474, "fixed")

    rolling = Enum.YLeaf(492733776, "rolling")


class Rpcerrortype(Enum):
    """
    Rpcerrortype

    .. data:: close = 1912083739

    .. data:: inline = 1987224790

    """

    close = Enum.YLeaf(1912083739, "close")

    inline = Enum.YLeaf(1987224790, "inline")


class Runtimereconfigurationtype(Enum):
    """
    Runtimereconfigurationtype

    .. data:: config_file = 2073952695

    .. data:: namespace = 1847615892

    """

    config_file = Enum.YLeaf(2073952695, "config-file")

    namespace = Enum.YLeaf(1847615892, "namespace")


class Snmplogleveltype(Enum):
    """
    Snmplogleveltype

    .. data:: error = 126243105

    .. data:: info = 2062105651

    """

    error = Enum.YLeaf(126243105, "error")

    info = Enum.YLeaf(2062105651, "info")


class Snmpversiontype(Enum):
    """
    Snmpversiontype

    .. data:: v1 = 1223356638

    .. data:: v2c = 406691283

    """

    v1 = Enum.YLeaf(1223356638, "v1")

    v2c = Enum.YLeaf(406691283, "v2c")


class Syslogversiontype(Enum):
    """
    Syslogversiontype

    .. data:: bsd = 1701318

    .. data:: Y_1 = 1535449617

    """

    bsd = Enum.YLeaf(1701318, "bsd")

    Y_1 = Enum.YLeaf(1535449617, "1")


class Tablebehaviortype(Enum):
    """
    Tablebehaviortype

    .. data:: dynamic = 1339207079

    .. data:: suppress = 1746378947

    .. data:: enforce = 868039165

    """

    dynamic = Enum.YLeaf(1339207079, "dynamic")

    suppress = Enum.YLeaf(1746378947, "suppress")

    enforce = Enum.YLeaf(868039165, "enforce")


class Unboundedtype(Enum):
    """
    Unboundedtype

    .. data:: unbounded = 1813338730

    """

    unbounded = Enum.YLeaf(1813338730, "unbounded")


class Unboundedtype(Enum):
    """
    Unboundedtype

    .. data:: unbounded = 1813338730

    """

    unbounded = Enum.YLeaf(1813338730, "unbounded")


class Whohistorydatetimeformattype(Enum):
    """
    Whohistorydatetimeformattype

    .. data:: long = 105537656

    .. data:: short = 2029155337

    """

    long = Enum.YLeaf(105537656, "long")

    short = Enum.YLeaf(2029155337, "short")


class XFrameOptionstype(Enum):
    """
    XFrameOptionstype

    .. data:: DENY = 864815184

    .. data:: SAMEORIGIN = 1594198254

    .. data:: ALLOW_FROM = 2088887798

    """

    DENY = Enum.YLeaf(864815184, "DENY")

    SAMEORIGIN = Enum.YLeaf(1594198254, "SAMEORIGIN")

    ALLOW_FROM = Enum.YLeaf(2088887798, "ALLOW-FROM")



class Confdconfig(Entity):
    """
    
    
    .. attribute:: aaa
    
    	
    	**type**\:   :py:class:`Aaa <ydk.models.confd_dyncfg.Confdconfig.Aaa>`
    
    	**presence node**\: True
    
    .. attribute:: cli
    
    	
    	**type**\:   :py:class:`Cli <ydk.models.confd_dyncfg.Confdconfig.Cli>`
    
    	**presence node**\: True
    
    .. attribute:: encryptedstrings
    
    	
    	**type**\:   :py:class:`Encryptedstrings <ydk.models.confd_dyncfg.Confdconfig.Encryptedstrings>`
    
    	**presence node**\: True
    
    .. attribute:: hidegroup
    
    	
    	**type**\: list of    :py:class:`Hidegroup <ydk.models.confd_dyncfg.Confdconfig.Hidegroup>`
    
    .. attribute:: logs
    
    	
    	**type**\:   :py:class:`Logs <ydk.models.confd_dyncfg.Confdconfig.Logs>`
    
    	**presence node**\: True
    
    .. attribute:: netconf
    
    	
    	**type**\:   :py:class:`Netconf <ydk.models.confd_dyncfg.Confdconfig.Netconf>`
    
    	**presence node**\: True
    
    .. attribute:: notifications
    
    	
    	**type**\:   :py:class:`Notifications <ydk.models.confd_dyncfg.Confdconfig.Notifications>`
    
    	**presence node**\: True
    
    .. attribute:: opcache
    
    	
    	**type**\:   :py:class:`Opcache <ydk.models.confd_dyncfg.Confdconfig.Opcache>`
    
    	**presence node**\: True
    
    .. attribute:: proxyforwarding
    
    	
    	**type**\:   :py:class:`Proxyforwarding <ydk.models.confd_dyncfg.Confdconfig.Proxyforwarding>`
    
    	**presence node**\: True
    
    .. attribute:: rest
    
    	
    	**type**\:   :py:class:`Rest <ydk.models.confd_dyncfg.Confdconfig.Rest>`
    
    	**presence node**\: True
    
    .. attribute:: restconf
    
    	
    	**type**\:   :py:class:`Restconf <ydk.models.confd_dyncfg.Confdconfig.Restconf>`
    
    	**presence node**\: True
    
    .. attribute:: sessionlimits
    
    	
    	**type**\:   :py:class:`Sessionlimits <ydk.models.confd_dyncfg.Confdconfig.Sessionlimits>`
    
    	**presence node**\: True
    
    .. attribute:: snmpagent
    
    	
    	**type**\:   :py:class:`Snmpagent <ydk.models.confd_dyncfg.Confdconfig.Snmpagent>`
    
    	**presence node**\: True
    
    .. attribute:: snmpgw
    
    	
    	**type**\:   :py:class:`Snmpgw <ydk.models.confd_dyncfg.Confdconfig.Snmpgw>`
    
    	**presence node**\: True
    
    .. attribute:: ssh
    
    	
    	**type**\:   :py:class:`Ssh <ydk.models.confd_dyncfg.Confdconfig.Ssh>`
    
    	**presence node**\: True
    
    .. attribute:: subagents
    
    	
    	**type**\:   :py:class:`Subagents <ydk.models.confd_dyncfg.Confdconfig.Subagents>`
    
    	**presence node**\: True
    
    .. attribute:: webui
    
    	
    	**type**\:   :py:class:`Webui <ydk.models.confd_dyncfg.Confdconfig.Webui>`
    
    	**presence node**\: True
    
    

    """

    _prefix = 'confd_dyncfg'
    _revision = '2017-01-16'

    def __init__(self):
        super(Confdconfig, self).__init__()
        self._top_entity = None

        self.yang_name = "confdConfig"
        self.yang_parent_name = "confd_dyncfg"

        self.aaa = None
        self._children_name_map["aaa"] = "aaa"
        self._children_yang_names.add("aaa")

        self.cli = None
        self._children_name_map["cli"] = "cli"
        self._children_yang_names.add("cli")

        self.encryptedstrings = None
        self._children_name_map["encryptedstrings"] = "encryptedStrings"
        self._children_yang_names.add("encryptedStrings")

        self.logs = None
        self._children_name_map["logs"] = "logs"
        self._children_yang_names.add("logs")

        self.netconf = None
        self._children_name_map["netconf"] = "netconf"
        self._children_yang_names.add("netconf")

        self.notifications = None
        self._children_name_map["notifications"] = "notifications"
        self._children_yang_names.add("notifications")

        self.opcache = None
        self._children_name_map["opcache"] = "opcache"
        self._children_yang_names.add("opcache")

        self.proxyforwarding = None
        self._children_name_map["proxyforwarding"] = "proxyForwarding"
        self._children_yang_names.add("proxyForwarding")

        self.rest = None
        self._children_name_map["rest"] = "rest"
        self._children_yang_names.add("rest")

        self.restconf = None
        self._children_name_map["restconf"] = "restconf"
        self._children_yang_names.add("restconf")

        self.sessionlimits = None
        self._children_name_map["sessionlimits"] = "sessionLimits"
        self._children_yang_names.add("sessionLimits")

        self.snmpagent = None
        self._children_name_map["snmpagent"] = "snmpAgent"
        self._children_yang_names.add("snmpAgent")

        self.snmpgw = None
        self._children_name_map["snmpgw"] = "snmpgw"
        self._children_yang_names.add("snmpgw")

        self.ssh = None
        self._children_name_map["ssh"] = "ssh"
        self._children_yang_names.add("ssh")

        self.subagents = None
        self._children_name_map["subagents"] = "subagents"
        self._children_yang_names.add("subagents")

        self.webui = None
        self._children_name_map["webui"] = "webui"
        self._children_yang_names.add("webui")

        self.hidegroup = YList(self)

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
                    super(Confdconfig, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(Confdconfig, self).__setattr__(name, value)


    class Subagents(Entity):
        """
        
        
        .. attribute:: subagent
        
        	
        	**type**\: list of    :py:class:`Subagent <ydk.models.confd_dyncfg.Confdconfig.Subagents.Subagent>`
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'confd_dyncfg'
        _revision = '2017-01-16'

        def __init__(self):
            super(Confdconfig.Subagents, self).__init__()

            self.yang_name = "subagents"
            self.yang_parent_name = "confdConfig"
            self.is_presence_container = True

            self.subagent = YList(self)

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
                        super(Confdconfig.Subagents, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Confdconfig.Subagents, self).__setattr__(name, value)


        class Subagent(Entity):
            """
            
            
            .. attribute:: name  <key>
            
            	
            	**type**\:  str
            
            	**length:** 0..31
            
            .. attribute:: disablesubtreeoptimization
            
            	
            	**type**\:  bool
            
            	**default value**\: false
            
            .. attribute:: enabled
            
            	
            	**type**\:  bool
            
            	**default value**\: true
            
            .. attribute:: mount
            
            	
            	**type**\:   :py:class:`Mount <ydk.models.confd_dyncfg.Confdconfig.Subagents.Subagent.Mount>`
            
            .. attribute:: ssh
            
            	
            	**type**\:   :py:class:`Ssh <ydk.models.confd_dyncfg.Confdconfig.Subagents.Subagent.Ssh>`
            
            	**presence node**\: True
            
            .. attribute:: tcp
            
            	
            	**type**\:   :py:class:`Tcp <ydk.models.confd_dyncfg.Confdconfig.Subagents.Subagent.Tcp>`
            
            	**presence node**\: True
            
            

            """

            _prefix = 'confd_dyncfg'
            _revision = '2017-01-16'

            def __init__(self):
                super(Confdconfig.Subagents.Subagent, self).__init__()

                self.yang_name = "subagent"
                self.yang_parent_name = "subagents"

                self.name = YLeaf(YType.str, "name")

                self.disablesubtreeoptimization = YLeaf(YType.boolean, "disableSubtreeOptimization")

                self.enabled = YLeaf(YType.boolean, "enabled")

                self.mount = Confdconfig.Subagents.Subagent.Mount()
                self.mount.parent = self
                self._children_name_map["mount"] = "mount"
                self._children_yang_names.add("mount")

                self.ssh = None
                self._children_name_map["ssh"] = "ssh"
                self._children_yang_names.add("ssh")

                self.tcp = None
                self._children_name_map["tcp"] = "tcp"
                self._children_yang_names.add("tcp")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("name",
                                "disablesubtreeoptimization",
                                "enabled") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Confdconfig.Subagents.Subagent, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Confdconfig.Subagents.Subagent, self).__setattr__(name, value)


            class Tcp(Entity):
                """
                
                
                .. attribute:: confdauth
                
                	
                	**type**\:   :py:class:`Confdauth <ydk.models.confd_dyncfg.Confdconfig.Subagents.Subagent.Tcp.Confdauth>`
                
                .. attribute:: ip
                
                	
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                	**mandatory**\: True
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                	**mandatory**\: True
                
                
                ----
                .. attribute:: port
                
                	
                	**type**\:  int
                
                	**range:** 0..65535
                
                	**default value**\: 2023
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'confd_dyncfg'
                _revision = '2017-01-16'

                def __init__(self):
                    super(Confdconfig.Subagents.Subagent.Tcp, self).__init__()

                    self.yang_name = "tcp"
                    self.yang_parent_name = "subagent"
                    self.is_presence_container = True

                    self.ip = YLeaf(YType.str, "ip")

                    self.port = YLeaf(YType.uint16, "port")

                    self.confdauth = Confdconfig.Subagents.Subagent.Tcp.Confdauth()
                    self.confdauth.parent = self
                    self._children_name_map["confdauth"] = "confdAuth"
                    self._children_yang_names.add("confdAuth")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("ip",
                                    "port") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Confdconfig.Subagents.Subagent.Tcp, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Confdconfig.Subagents.Subagent.Tcp, self).__setattr__(name, value)


                class Confdauth(Entity):
                    """
                    
                    
                    .. attribute:: group
                    
                    	
                    	**type**\:  str
                    
                    	**mandatory**\: True
                    
                    .. attribute:: user
                    
                    	
                    	**type**\:  str
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'confd_dyncfg'
                    _revision = '2017-01-16'

                    def __init__(self):
                        super(Confdconfig.Subagents.Subagent.Tcp.Confdauth, self).__init__()

                        self.yang_name = "confdAuth"
                        self.yang_parent_name = "tcp"

                        self.group = YLeaf(YType.str, "group")

                        self.user = YLeaf(YType.str, "user")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("group",
                                        "user") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Confdconfig.Subagents.Subagent.Tcp.Confdauth, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Confdconfig.Subagents.Subagent.Tcp.Confdauth, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.group.is_set or
                            self.user.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.group.yfilter != YFilter.not_set or
                            self.user.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "confdAuth" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.group.is_set or self.group.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.group.get_name_leafdata())
                        if (self.user.is_set or self.user.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.user.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "group" or name == "user"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "group"):
                            self.group = value
                            self.group.value_namespace = name_space
                            self.group.value_namespace_prefix = name_space_prefix
                        if(value_path == "user"):
                            self.user = value
                            self.user.value_namespace = name_space
                            self.user.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.ip.is_set or
                        self.port.is_set or
                        (self.confdauth is not None and self.confdauth.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.ip.yfilter != YFilter.not_set or
                        self.port.yfilter != YFilter.not_set or
                        (self.confdauth is not None and self.confdauth.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "tcp" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.ip.is_set or self.ip.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ip.get_name_leafdata())
                    if (self.port.is_set or self.port.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.port.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "confdAuth"):
                        if (self.confdauth is None):
                            self.confdauth = Confdconfig.Subagents.Subagent.Tcp.Confdauth()
                            self.confdauth.parent = self
                            self._children_name_map["confdauth"] = "confdAuth"
                        return self.confdauth

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "confdAuth" or name == "ip" or name == "port"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "ip"):
                        self.ip = value
                        self.ip.value_namespace = name_space
                        self.ip.value_namespace_prefix = name_space_prefix
                    if(value_path == "port"):
                        self.port = value
                        self.port.value_namespace = name_space
                        self.port.value_namespace_prefix = name_space_prefix


            class Ssh(Entity):
                """
                
                
                .. attribute:: ip
                
                	
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                	**mandatory**\: True
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                	**mandatory**\: True
                
                
                ----
                .. attribute:: password
                
                	
                	**type**\:  str
                
                	**mandatory**\: True
                
                .. attribute:: port
                
                	
                	**type**\:  int
                
                	**range:** 0..65535
                
                	**default value**\: 2022
                
                .. attribute:: user
                
                	
                	**type**\:  str
                
                	**mandatory**\: True
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'confd_dyncfg'
                _revision = '2017-01-16'

                def __init__(self):
                    super(Confdconfig.Subagents.Subagent.Ssh, self).__init__()

                    self.yang_name = "ssh"
                    self.yang_parent_name = "subagent"
                    self.is_presence_container = True

                    self.ip = YLeaf(YType.str, "ip")

                    self.password = YLeaf(YType.str, "password")

                    self.port = YLeaf(YType.uint16, "port")

                    self.user = YLeaf(YType.str, "user")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("ip",
                                    "password",
                                    "port",
                                    "user") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Confdconfig.Subagents.Subagent.Ssh, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Confdconfig.Subagents.Subagent.Ssh, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.ip.is_set or
                        self.password.is_set or
                        self.port.is_set or
                        self.user.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.ip.yfilter != YFilter.not_set or
                        self.password.yfilter != YFilter.not_set or
                        self.port.yfilter != YFilter.not_set or
                        self.user.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "ssh" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.ip.is_set or self.ip.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ip.get_name_leafdata())
                    if (self.password.is_set or self.password.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.password.get_name_leafdata())
                    if (self.port.is_set or self.port.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.port.get_name_leafdata())
                    if (self.user.is_set or self.user.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.user.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "ip" or name == "password" or name == "port" or name == "user"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "ip"):
                        self.ip = value
                        self.ip.value_namespace = name_space
                        self.ip.value_namespace_prefix = name_space_prefix
                    if(value_path == "password"):
                        self.password = value
                        self.password.value_namespace = name_space
                        self.password.value_namespace_prefix = name_space_prefix
                    if(value_path == "port"):
                        self.port = value
                        self.port.value_namespace = name_space
                        self.port.value_namespace_prefix = name_space_prefix
                    if(value_path == "user"):
                        self.user = value
                        self.user.value_namespace = name_space
                        self.user.value_namespace_prefix = name_space_prefix


            class Mount(Entity):
                """
                
                
                .. attribute:: node
                
                	
                	**type**\:  list of str
                
                .. attribute:: path
                
                	
                	**type**\:  str
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'confd_dyncfg'
                _revision = '2017-01-16'

                def __init__(self):
                    super(Confdconfig.Subagents.Subagent.Mount, self).__init__()

                    self.yang_name = "mount"
                    self.yang_parent_name = "subagent"

                    self.node = YLeafList(YType.str, "node")

                    self.path = YLeaf(YType.str, "path")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("node",
                                    "path") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Confdconfig.Subagents.Subagent.Mount, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Confdconfig.Subagents.Subagent.Mount, self).__setattr__(name, value)

                def has_data(self):
                    for leaf in self.node.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    return self.path.is_set

                def has_operation(self):
                    for leaf in self.node.getYLeafs():
                        if (leaf.is_set):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.node.yfilter != YFilter.not_set or
                        self.path.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "mount" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.path.is_set or self.path.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.path.get_name_leafdata())

                    leaf_name_data.extend(self.node.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "node" or name == "path"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "node"):
                        self.node.append(value)
                    if(value_path == "path"):
                        self.path = value
                        self.path.value_namespace = name_space
                        self.path.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.name.is_set or
                    self.disablesubtreeoptimization.is_set or
                    self.enabled.is_set or
                    (self.mount is not None and self.mount.has_data()) or
                    (self.ssh is not None) or
                    (self.tcp is not None))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.name.yfilter != YFilter.not_set or
                    self.disablesubtreeoptimization.yfilter != YFilter.not_set or
                    self.enabled.yfilter != YFilter.not_set or
                    (self.mount is not None and self.mount.has_operation()) or
                    (self.ssh is not None and self.ssh.has_operation()) or
                    (self.tcp is not None and self.tcp.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "subagent" + "[name='" + self.name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "confd_dyncfg:confdConfig/subagents/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.name.get_name_leafdata())
                if (self.disablesubtreeoptimization.is_set or self.disablesubtreeoptimization.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.disablesubtreeoptimization.get_name_leafdata())
                if (self.enabled.is_set or self.enabled.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.enabled.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "mount"):
                    if (self.mount is None):
                        self.mount = Confdconfig.Subagents.Subagent.Mount()
                        self.mount.parent = self
                        self._children_name_map["mount"] = "mount"
                    return self.mount

                if (child_yang_name == "ssh"):
                    if (self.ssh is None):
                        self.ssh = Confdconfig.Subagents.Subagent.Ssh()
                        self.ssh.parent = self
                        self._children_name_map["ssh"] = "ssh"
                    return self.ssh

                if (child_yang_name == "tcp"):
                    if (self.tcp is None):
                        self.tcp = Confdconfig.Subagents.Subagent.Tcp()
                        self.tcp.parent = self
                        self._children_name_map["tcp"] = "tcp"
                    return self.tcp

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "mount" or name == "ssh" or name == "tcp" or name == "name" or name == "disableSubtreeOptimization" or name == "enabled"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "name"):
                    self.name = value
                    self.name.value_namespace = name_space
                    self.name.value_namespace_prefix = name_space_prefix
                if(value_path == "disableSubtreeOptimization"):
                    self.disablesubtreeoptimization = value
                    self.disablesubtreeoptimization.value_namespace = name_space
                    self.disablesubtreeoptimization.value_namespace_prefix = name_space_prefix
                if(value_path == "enabled"):
                    self.enabled = value
                    self.enabled.value_namespace = name_space
                    self.enabled.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.subagent:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.subagent:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "subagents" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "confd_dyncfg:confdConfig/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "subagent"):
                for c in self.subagent:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Confdconfig.Subagents.Subagent()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.subagent.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "subagent"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Notifications(Entity):
        """
        
        
        .. attribute:: eventstreams
        
        	
        	**type**\:   :py:class:`Eventstreams <ydk.models.confd_dyncfg.Confdconfig.Notifications.Eventstreams>`
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'confd_dyncfg'
        _revision = '2017-01-16'

        def __init__(self):
            super(Confdconfig.Notifications, self).__init__()

            self.yang_name = "notifications"
            self.yang_parent_name = "confdConfig"
            self.is_presence_container = True

            self.eventstreams = Confdconfig.Notifications.Eventstreams()
            self.eventstreams.parent = self
            self._children_name_map["eventstreams"] = "eventStreams"
            self._children_yang_names.add("eventStreams")


        class Eventstreams(Entity):
            """
            
            
            .. attribute:: stream
            
            	
            	**type**\: list of    :py:class:`Stream <ydk.models.confd_dyncfg.Confdconfig.Notifications.Eventstreams.Stream>`
            
            

            """

            _prefix = 'confd_dyncfg'
            _revision = '2017-01-16'

            def __init__(self):
                super(Confdconfig.Notifications.Eventstreams, self).__init__()

                self.yang_name = "eventStreams"
                self.yang_parent_name = "notifications"

                self.stream = YList(self)

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
                            super(Confdconfig.Notifications.Eventstreams, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Confdconfig.Notifications.Eventstreams, self).__setattr__(name, value)


            class Stream(Entity):
                """
                
                
                .. attribute:: name  <key>
                
                	
                	**type**\:  str
                
                .. attribute:: builtinreplaystore
                
                	
                	**type**\:   :py:class:`Builtinreplaystore <ydk.models.confd_dyncfg.Confdconfig.Notifications.Eventstreams.Stream.Builtinreplaystore>`
                
                	**presence node**\: True
                
                .. attribute:: description
                
                	
                	**type**\:  str
                
                	**mandatory**\: True
                
                .. attribute:: replaysupport
                
                	
                	**type**\:  bool
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'confd_dyncfg'
                _revision = '2017-01-16'

                def __init__(self):
                    super(Confdconfig.Notifications.Eventstreams.Stream, self).__init__()

                    self.yang_name = "stream"
                    self.yang_parent_name = "eventStreams"

                    self.name = YLeaf(YType.str, "name")

                    self.description = YLeaf(YType.str, "description")

                    self.replaysupport = YLeaf(YType.boolean, "replaySupport")

                    self.builtinreplaystore = None
                    self._children_name_map["builtinreplaystore"] = "builtinReplayStore"
                    self._children_yang_names.add("builtinReplayStore")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("name",
                                    "description",
                                    "replaysupport") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Confdconfig.Notifications.Eventstreams.Stream, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Confdconfig.Notifications.Eventstreams.Stream, self).__setattr__(name, value)


                class Builtinreplaystore(Entity):
                    """
                    
                    
                    .. attribute:: dir
                    
                    	
                    	**type**\:  str
                    
                    	**mandatory**\: True
                    
                    .. attribute:: enabled
                    
                    	
                    	**type**\:  bool
                    
                    	**default value**\: false
                    
                    .. attribute:: maxfiles
                    
                    	
                    	**type**\:  int
                    
                    	**range:** 2..9223372036854775807
                    
                    	**mandatory**\: True
                    
                    .. attribute:: maxsize
                    
                    	
                    	**type**\:  str
                    
                    	**pattern:** S(\\d+G)?(\\d+M)?(\\d+K)?(\\d+B)?
                    
                    	**mandatory**\: True
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'confd_dyncfg'
                    _revision = '2017-01-16'

                    def __init__(self):
                        super(Confdconfig.Notifications.Eventstreams.Stream.Builtinreplaystore, self).__init__()

                        self.yang_name = "builtinReplayStore"
                        self.yang_parent_name = "stream"
                        self.is_presence_container = True

                        self.dir = YLeaf(YType.str, "dir")

                        self.enabled = YLeaf(YType.boolean, "enabled")

                        self.maxfiles = YLeaf(YType.int64, "maxFiles")

                        self.maxsize = YLeaf(YType.str, "maxSize")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("dir",
                                        "enabled",
                                        "maxfiles",
                                        "maxsize") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Confdconfig.Notifications.Eventstreams.Stream.Builtinreplaystore, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Confdconfig.Notifications.Eventstreams.Stream.Builtinreplaystore, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.dir.is_set or
                            self.enabled.is_set or
                            self.maxfiles.is_set or
                            self.maxsize.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.dir.yfilter != YFilter.not_set or
                            self.enabled.yfilter != YFilter.not_set or
                            self.maxfiles.yfilter != YFilter.not_set or
                            self.maxsize.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "builtinReplayStore" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.dir.is_set or self.dir.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.dir.get_name_leafdata())
                        if (self.enabled.is_set or self.enabled.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.enabled.get_name_leafdata())
                        if (self.maxfiles.is_set or self.maxfiles.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.maxfiles.get_name_leafdata())
                        if (self.maxsize.is_set or self.maxsize.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.maxsize.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "dir" or name == "enabled" or name == "maxFiles" or name == "maxSize"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "dir"):
                            self.dir = value
                            self.dir.value_namespace = name_space
                            self.dir.value_namespace_prefix = name_space_prefix
                        if(value_path == "enabled"):
                            self.enabled = value
                            self.enabled.value_namespace = name_space
                            self.enabled.value_namespace_prefix = name_space_prefix
                        if(value_path == "maxFiles"):
                            self.maxfiles = value
                            self.maxfiles.value_namespace = name_space
                            self.maxfiles.value_namespace_prefix = name_space_prefix
                        if(value_path == "maxSize"):
                            self.maxsize = value
                            self.maxsize.value_namespace = name_space
                            self.maxsize.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.name.is_set or
                        self.description.is_set or
                        self.replaysupport.is_set or
                        (self.builtinreplaystore is not None))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.name.yfilter != YFilter.not_set or
                        self.description.yfilter != YFilter.not_set or
                        self.replaysupport.yfilter != YFilter.not_set or
                        (self.builtinreplaystore is not None and self.builtinreplaystore.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "stream" + "[name='" + self.name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "confd_dyncfg:confdConfig/notifications/eventStreams/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.name.get_name_leafdata())
                    if (self.description.is_set or self.description.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.description.get_name_leafdata())
                    if (self.replaysupport.is_set or self.replaysupport.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.replaysupport.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "builtinReplayStore"):
                        if (self.builtinreplaystore is None):
                            self.builtinreplaystore = Confdconfig.Notifications.Eventstreams.Stream.Builtinreplaystore()
                            self.builtinreplaystore.parent = self
                            self._children_name_map["builtinreplaystore"] = "builtinReplayStore"
                        return self.builtinreplaystore

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "builtinReplayStore" or name == "name" or name == "description" or name == "replaySupport"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "name"):
                        self.name = value
                        self.name.value_namespace = name_space
                        self.name.value_namespace_prefix = name_space_prefix
                    if(value_path == "description"):
                        self.description = value
                        self.description.value_namespace = name_space
                        self.description.value_namespace_prefix = name_space_prefix
                    if(value_path == "replaySupport"):
                        self.replaysupport = value
                        self.replaysupport.value_namespace = name_space
                        self.replaysupport.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.stream:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.stream:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "eventStreams" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "confd_dyncfg:confdConfig/notifications/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "stream"):
                    for c in self.stream:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Confdconfig.Notifications.Eventstreams.Stream()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.stream.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "stream"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (self.eventstreams is not None and self.eventstreams.has_data())

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.eventstreams is not None and self.eventstreams.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "notifications" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "confd_dyncfg:confdConfig/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "eventStreams"):
                if (self.eventstreams is None):
                    self.eventstreams = Confdconfig.Notifications.Eventstreams()
                    self.eventstreams.parent = self
                    self._children_name_map["eventstreams"] = "eventStreams"
                return self.eventstreams

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "eventStreams"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Opcache(Entity):
        """
        
        
        .. attribute:: enabled
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: timeout
        
        	
        	**type**\:  int
        
        	**range:** 0..18446744073709551615 \| 0..18446744073709551615
        
        	**mandatory**\: True
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'confd_dyncfg'
        _revision = '2017-01-16'

        def __init__(self):
            super(Confdconfig.Opcache, self).__init__()

            self.yang_name = "opcache"
            self.yang_parent_name = "confdConfig"
            self.is_presence_container = True

            self.enabled = YLeaf(YType.boolean, "enabled")

            self.timeout = YLeaf(YType.uint64, "timeout")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("enabled",
                            "timeout") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Confdconfig.Opcache, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Confdconfig.Opcache, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.enabled.is_set or
                self.timeout.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.enabled.yfilter != YFilter.not_set or
                self.timeout.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "opcache" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "confd_dyncfg:confdConfig/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.enabled.is_set or self.enabled.yfilter != YFilter.not_set):
                leaf_name_data.append(self.enabled.get_name_leafdata())
            if (self.timeout.is_set or self.timeout.yfilter != YFilter.not_set):
                leaf_name_data.append(self.timeout.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "enabled" or name == "timeout"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "enabled"):
                self.enabled = value
                self.enabled.value_namespace = name_space
                self.enabled.value_namespace_prefix = name_space_prefix
            if(value_path == "timeout"):
                self.timeout = value
                self.timeout.value_namespace = name_space
                self.timeout.value_namespace_prefix = name_space_prefix


    class Snmpgw(Entity):
        """
        
        
        .. attribute:: agent
        
        	
        	**type**\: list of    :py:class:`Agent <ydk.models.confd_dyncfg.Confdconfig.Snmpgw.Agent>`
        
        .. attribute:: enabled
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: trapport
        
        	
        	**type**\:  int
        
        	**range:** 0..65535
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'confd_dyncfg'
        _revision = '2017-01-16'

        def __init__(self):
            super(Confdconfig.Snmpgw, self).__init__()

            self.yang_name = "snmpgw"
            self.yang_parent_name = "confdConfig"
            self.is_presence_container = True

            self.enabled = YLeaf(YType.boolean, "enabled")

            self.trapport = YLeaf(YType.uint16, "trapPort")

            self.agent = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("enabled",
                            "trapport") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Confdconfig.Snmpgw, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Confdconfig.Snmpgw, self).__setattr__(name, value)


        class Agent(Entity):
            """
            
            
            .. attribute:: name  <key>
            
            	
            	**type**\:  str
            
            	**length:** 0..31
            
            .. attribute:: community
            
            	
            	**type**\:  str
            
            	**default value**\: private
            
            .. attribute:: community_bin
            
            	
            	**type**\:  str
            
            .. attribute:: enabled
            
            	
            	**type**\:  bool
            
            	**default value**\: true
            
            .. attribute:: forwardnotifstream
            
            	
            	**type**\:  str
            
            .. attribute:: ip
            
            	
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**mandatory**\: True
            
            
            ----
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            	**mandatory**\: True
            
            
            ----
            .. attribute:: module
            
            	
            	**type**\:  list of str
            
            .. attribute:: port
            
            	
            	**type**\:  int
            
            	**range:** 0..65535
            
            	**default value**\: 161
            
            .. attribute:: subscriptionid
            
            	
            	**type**\:  str
            
            .. attribute:: timeout
            
            	
            	**type**\:  str
            
            	**default value**\: PT5S
            
            .. attribute:: version
            
            	
            	**type**\:   :py:class:`Snmpversiontype <ydk.models.confd_dyncfg.Snmpversiontype>`
            
            	**default value**\: v2c
            
            

            """

            _prefix = 'confd_dyncfg'
            _revision = '2017-01-16'

            def __init__(self):
                super(Confdconfig.Snmpgw.Agent, self).__init__()

                self.yang_name = "agent"
                self.yang_parent_name = "snmpgw"

                self.name = YLeaf(YType.str, "name")

                self.community = YLeaf(YType.str, "community")

                self.community_bin = YLeaf(YType.str, "community_bin")

                self.enabled = YLeaf(YType.boolean, "enabled")

                self.forwardnotifstream = YLeaf(YType.str, "forwardNotifStream")

                self.ip = YLeaf(YType.str, "ip")

                self.module = YLeafList(YType.str, "module")

                self.port = YLeaf(YType.uint16, "port")

                self.subscriptionid = YLeaf(YType.str, "subscriptionId")

                self.timeout = YLeaf(YType.str, "timeout")

                self.version = YLeaf(YType.enumeration, "version")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("name",
                                "community",
                                "community_bin",
                                "enabled",
                                "forwardnotifstream",
                                "ip",
                                "module",
                                "port",
                                "subscriptionid",
                                "timeout",
                                "version") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Confdconfig.Snmpgw.Agent, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Confdconfig.Snmpgw.Agent, self).__setattr__(name, value)

            def has_data(self):
                for leaf in self.module.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                return (
                    self.name.is_set or
                    self.community.is_set or
                    self.community_bin.is_set or
                    self.enabled.is_set or
                    self.forwardnotifstream.is_set or
                    self.ip.is_set or
                    self.port.is_set or
                    self.subscriptionid.is_set or
                    self.timeout.is_set or
                    self.version.is_set)

            def has_operation(self):
                for leaf in self.module.getYLeafs():
                    if (leaf.is_set):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.name.yfilter != YFilter.not_set or
                    self.community.yfilter != YFilter.not_set or
                    self.community_bin.yfilter != YFilter.not_set or
                    self.enabled.yfilter != YFilter.not_set or
                    self.forwardnotifstream.yfilter != YFilter.not_set or
                    self.ip.yfilter != YFilter.not_set or
                    self.module.yfilter != YFilter.not_set or
                    self.port.yfilter != YFilter.not_set or
                    self.subscriptionid.yfilter != YFilter.not_set or
                    self.timeout.yfilter != YFilter.not_set or
                    self.version.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "agent" + "[name='" + self.name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "confd_dyncfg:confdConfig/snmpgw/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.name.get_name_leafdata())
                if (self.community.is_set or self.community.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.community.get_name_leafdata())
                if (self.community_bin.is_set or self.community_bin.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.community_bin.get_name_leafdata())
                if (self.enabled.is_set or self.enabled.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.enabled.get_name_leafdata())
                if (self.forwardnotifstream.is_set or self.forwardnotifstream.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.forwardnotifstream.get_name_leafdata())
                if (self.ip.is_set or self.ip.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ip.get_name_leafdata())
                if (self.port.is_set or self.port.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.port.get_name_leafdata())
                if (self.subscriptionid.is_set or self.subscriptionid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.subscriptionid.get_name_leafdata())
                if (self.timeout.is_set or self.timeout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.timeout.get_name_leafdata())
                if (self.version.is_set or self.version.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.version.get_name_leafdata())

                leaf_name_data.extend(self.module.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "name" or name == "community" or name == "community_bin" or name == "enabled" or name == "forwardNotifStream" or name == "ip" or name == "module" or name == "port" or name == "subscriptionId" or name == "timeout" or name == "version"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "name"):
                    self.name = value
                    self.name.value_namespace = name_space
                    self.name.value_namespace_prefix = name_space_prefix
                if(value_path == "community"):
                    self.community = value
                    self.community.value_namespace = name_space
                    self.community.value_namespace_prefix = name_space_prefix
                if(value_path == "community_bin"):
                    self.community_bin = value
                    self.community_bin.value_namespace = name_space
                    self.community_bin.value_namespace_prefix = name_space_prefix
                if(value_path == "enabled"):
                    self.enabled = value
                    self.enabled.value_namespace = name_space
                    self.enabled.value_namespace_prefix = name_space_prefix
                if(value_path == "forwardNotifStream"):
                    self.forwardnotifstream = value
                    self.forwardnotifstream.value_namespace = name_space
                    self.forwardnotifstream.value_namespace_prefix = name_space_prefix
                if(value_path == "ip"):
                    self.ip = value
                    self.ip.value_namespace = name_space
                    self.ip.value_namespace_prefix = name_space_prefix
                if(value_path == "module"):
                    self.module.append(value)
                if(value_path == "port"):
                    self.port = value
                    self.port.value_namespace = name_space
                    self.port.value_namespace_prefix = name_space_prefix
                if(value_path == "subscriptionId"):
                    self.subscriptionid = value
                    self.subscriptionid.value_namespace = name_space
                    self.subscriptionid.value_namespace_prefix = name_space_prefix
                if(value_path == "timeout"):
                    self.timeout = value
                    self.timeout.value_namespace = name_space
                    self.timeout.value_namespace_prefix = name_space_prefix
                if(value_path == "version"):
                    self.version = value
                    self.version.value_namespace = name_space
                    self.version.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.agent:
                if (c.has_data()):
                    return True
            return (
                self.enabled.is_set or
                self.trapport.is_set)

        def has_operation(self):
            for c in self.agent:
                if (c.has_operation()):
                    return True
            return (
                self.yfilter != YFilter.not_set or
                self.enabled.yfilter != YFilter.not_set or
                self.trapport.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "snmpgw" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "confd_dyncfg:confdConfig/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.enabled.is_set or self.enabled.yfilter != YFilter.not_set):
                leaf_name_data.append(self.enabled.get_name_leafdata())
            if (self.trapport.is_set or self.trapport.yfilter != YFilter.not_set):
                leaf_name_data.append(self.trapport.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "agent"):
                for c in self.agent:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Confdconfig.Snmpgw.Agent()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.agent.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "agent" or name == "enabled" or name == "trapPort"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "enabled"):
                self.enabled = value
                self.enabled.value_namespace = name_space
                self.enabled.value_namespace_prefix = name_space_prefix
            if(value_path == "trapPort"):
                self.trapport = value
                self.trapport.value_namespace = name_space
                self.trapport.value_namespace_prefix = name_space_prefix


    class Hidegroup(Entity):
        """
        
        
        .. attribute:: name  <key>
        
        	
        	**type**\:  str
        
        .. attribute:: callback
        
        	
        	**type**\:  str
        
        .. attribute:: password
        
        	
        	**type**\:  str
        
        

        """

        _prefix = 'confd_dyncfg'
        _revision = '2017-01-16'

        def __init__(self):
            super(Confdconfig.Hidegroup, self).__init__()

            self.yang_name = "hideGroup"
            self.yang_parent_name = "confdConfig"

            self.name = YLeaf(YType.str, "name")

            self.callback = YLeaf(YType.str, "callback")

            self.password = YLeaf(YType.str, "password")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("name",
                            "callback",
                            "password") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Confdconfig.Hidegroup, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Confdconfig.Hidegroup, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.name.is_set or
                self.callback.is_set or
                self.password.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.name.yfilter != YFilter.not_set or
                self.callback.yfilter != YFilter.not_set or
                self.password.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "hideGroup" + "[name='" + self.name.get() + "']" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "confd_dyncfg:confdConfig/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                leaf_name_data.append(self.name.get_name_leafdata())
            if (self.callback.is_set or self.callback.yfilter != YFilter.not_set):
                leaf_name_data.append(self.callback.get_name_leafdata())
            if (self.password.is_set or self.password.yfilter != YFilter.not_set):
                leaf_name_data.append(self.password.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "name" or name == "callback" or name == "password"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "name"):
                self.name = value
                self.name.value_namespace = name_space
                self.name.value_namespace_prefix = name_space_prefix
            if(value_path == "callback"):
                self.callback = value
                self.callback.value_namespace = name_space
                self.callback.value_namespace_prefix = name_space_prefix
            if(value_path == "password"):
                self.password = value
                self.password.value_namespace = name_space
                self.password.value_namespace_prefix = name_space_prefix


    class Encryptedstrings(Entity):
        """
        
        
        .. attribute:: aescfb128
        
        	
        	**type**\:   :py:class:`Aescfb128 <ydk.models.confd_dyncfg.Confdconfig.Encryptedstrings.Aescfb128>`
        
        	**presence node**\: True
        
        .. attribute:: des3cbc
        
        	
        	**type**\:   :py:class:`Des3Cbc <ydk.models.confd_dyncfg.Confdconfig.Encryptedstrings.Des3Cbc>`
        
        	**presence node**\: True
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'confd_dyncfg'
        _revision = '2017-01-16'

        def __init__(self):
            super(Confdconfig.Encryptedstrings, self).__init__()

            self.yang_name = "encryptedStrings"
            self.yang_parent_name = "confdConfig"
            self.is_presence_container = True

            self.aescfb128 = None
            self._children_name_map["aescfb128"] = "AESCFB128"
            self._children_yang_names.add("AESCFB128")

            self.des3cbc = None
            self._children_name_map["des3cbc"] = "DES3CBC"
            self._children_yang_names.add("DES3CBC")


        class Des3Cbc(Entity):
            """
            
            
            .. attribute:: initvector
            
            	
            	**type**\:  str
            
            .. attribute:: key1
            
            	
            	**type**\:  str
            
            	**mandatory**\: True
            
            .. attribute:: key2
            
            	
            	**type**\:  str
            
            	**mandatory**\: True
            
            .. attribute:: key3
            
            	
            	**type**\:  str
            
            	**mandatory**\: True
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'confd_dyncfg'
            _revision = '2017-01-16'

            def __init__(self):
                super(Confdconfig.Encryptedstrings.Des3Cbc, self).__init__()

                self.yang_name = "DES3CBC"
                self.yang_parent_name = "encryptedStrings"
                self.is_presence_container = True

                self.initvector = YLeaf(YType.str, "initVector")

                self.key1 = YLeaf(YType.str, "key1")

                self.key2 = YLeaf(YType.str, "key2")

                self.key3 = YLeaf(YType.str, "key3")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("initvector",
                                "key1",
                                "key2",
                                "key3") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Confdconfig.Encryptedstrings.Des3Cbc, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Confdconfig.Encryptedstrings.Des3Cbc, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.initvector.is_set or
                    self.key1.is_set or
                    self.key2.is_set or
                    self.key3.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.initvector.yfilter != YFilter.not_set or
                    self.key1.yfilter != YFilter.not_set or
                    self.key2.yfilter != YFilter.not_set or
                    self.key3.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "DES3CBC" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "confd_dyncfg:confdConfig/encryptedStrings/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.initvector.is_set or self.initvector.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.initvector.get_name_leafdata())
                if (self.key1.is_set or self.key1.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.key1.get_name_leafdata())
                if (self.key2.is_set or self.key2.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.key2.get_name_leafdata())
                if (self.key3.is_set or self.key3.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.key3.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "initVector" or name == "key1" or name == "key2" or name == "key3"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "initVector"):
                    self.initvector = value
                    self.initvector.value_namespace = name_space
                    self.initvector.value_namespace_prefix = name_space_prefix
                if(value_path == "key1"):
                    self.key1 = value
                    self.key1.value_namespace = name_space
                    self.key1.value_namespace_prefix = name_space_prefix
                if(value_path == "key2"):
                    self.key2 = value
                    self.key2.value_namespace = name_space
                    self.key2.value_namespace_prefix = name_space_prefix
                if(value_path == "key3"):
                    self.key3 = value
                    self.key3.value_namespace = name_space
                    self.key3.value_namespace_prefix = name_space_prefix


        class Aescfb128(Entity):
            """
            
            
            .. attribute:: initvector
            
            	
            	**type**\:  str
            
            .. attribute:: key
            
            	
            	**type**\:  str
            
            	**mandatory**\: True
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'confd_dyncfg'
            _revision = '2017-01-16'

            def __init__(self):
                super(Confdconfig.Encryptedstrings.Aescfb128, self).__init__()

                self.yang_name = "AESCFB128"
                self.yang_parent_name = "encryptedStrings"
                self.is_presence_container = True

                self.initvector = YLeaf(YType.str, "initVector")

                self.key = YLeaf(YType.str, "key")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("initvector",
                                "key") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Confdconfig.Encryptedstrings.Aescfb128, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Confdconfig.Encryptedstrings.Aescfb128, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.initvector.is_set or
                    self.key.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.initvector.yfilter != YFilter.not_set or
                    self.key.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "AESCFB128" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "confd_dyncfg:confdConfig/encryptedStrings/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.initvector.is_set or self.initvector.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.initvector.get_name_leafdata())
                if (self.key.is_set or self.key.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.key.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "initVector" or name == "key"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "initVector"):
                    self.initvector = value
                    self.initvector.value_namespace = name_space
                    self.initvector.value_namespace_prefix = name_space_prefix
                if(value_path == "key"):
                    self.key = value
                    self.key.value_namespace = name_space
                    self.key.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (
                (self.aescfb128 is not None) or
                (self.des3cbc is not None))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.aescfb128 is not None and self.aescfb128.has_operation()) or
                (self.des3cbc is not None and self.des3cbc.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "encryptedStrings" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "confd_dyncfg:confdConfig/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "AESCFB128"):
                if (self.aescfb128 is None):
                    self.aescfb128 = Confdconfig.Encryptedstrings.Aescfb128()
                    self.aescfb128.parent = self
                    self._children_name_map["aescfb128"] = "AESCFB128"
                return self.aescfb128

            if (child_yang_name == "DES3CBC"):
                if (self.des3cbc is None):
                    self.des3cbc = Confdconfig.Encryptedstrings.Des3Cbc()
                    self.des3cbc.parent = self
                    self._children_name_map["des3cbc"] = "DES3CBC"
                return self.des3cbc

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "AESCFB128" or name == "DES3CBC"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Logs(Entity):
        """
        
        
        .. attribute:: auditlog
        
        	
        	**type**\:   :py:class:`Auditlog <ydk.models.confd_dyncfg.Confdconfig.Logs.Auditlog>`
        
        	**presence node**\: True
        
        .. attribute:: auditlogcommit
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: confdlog
        
        	
        	**type**\:   :py:class:`Confdlog <ydk.models.confd_dyncfg.Confdconfig.Logs.Confdlog>`
        
        	**presence node**\: True
        
        .. attribute:: developerlog
        
        	
        	**type**\:   :py:class:`Developerlog <ydk.models.confd_dyncfg.Confdconfig.Logs.Developerlog>`
        
        	**presence node**\: True
        
        .. attribute:: developerloglevel
        
        	
        	**type**\:   :py:class:`Developerlogleveltype <ydk.models.confd_dyncfg.Developerlogleveltype>`
        
        	**default value**\: info
        
        .. attribute:: errorlog
        
        	
        	**type**\:   :py:class:`Errorlog <ydk.models.confd_dyncfg.Confdconfig.Logs.Errorlog>`
        
        	**presence node**\: True
        
        .. attribute:: netconflog
        
        	
        	**type**\:   :py:class:`Netconflog <ydk.models.confd_dyncfg.Confdconfig.Logs.Netconflog>`
        
        	**presence node**\: True
        
        .. attribute:: netconftracelog
        
        	
        	**type**\:   :py:class:`Netconftracelog <ydk.models.confd_dyncfg.Confdconfig.Logs.Netconftracelog>`
        
        	**presence node**\: True
        
        .. attribute:: snmplog
        
        	
        	**type**\:   :py:class:`Snmplog <ydk.models.confd_dyncfg.Confdconfig.Logs.Snmplog>`
        
        	**presence node**\: True
        
        .. attribute:: snmploglevel
        
        	
        	**type**\:   :py:class:`Snmplogleveltype <ydk.models.confd_dyncfg.Snmplogleveltype>`
        
        	**default value**\: info
        
        .. attribute:: syslogconfig
        
        	
        	**type**\:   :py:class:`Syslogconfig <ydk.models.confd_dyncfg.Confdconfig.Logs.Syslogconfig>`
        
        	**presence node**\: True
        
        .. attribute:: webuiaccesslog
        
        	
        	**type**\:   :py:class:`Webuiaccesslog <ydk.models.confd_dyncfg.Confdconfig.Logs.Webuiaccesslog>`
        
        	**presence node**\: True
        
        .. attribute:: webuibrowserlog
        
        	
        	**type**\:   :py:class:`Webuibrowserlog <ydk.models.confd_dyncfg.Confdconfig.Logs.Webuibrowserlog>`
        
        	**presence node**\: True
        
        .. attribute:: xpathtracelog
        
        	
        	**type**\:   :py:class:`Xpathtracelog <ydk.models.confd_dyncfg.Confdconfig.Logs.Xpathtracelog>`
        
        	**presence node**\: True
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'confd_dyncfg'
        _revision = '2017-01-16'

        def __init__(self):
            super(Confdconfig.Logs, self).__init__()

            self.yang_name = "logs"
            self.yang_parent_name = "confdConfig"
            self.is_presence_container = True

            self.auditlogcommit = YLeaf(YType.boolean, "auditLogCommit")

            self.developerloglevel = YLeaf(YType.enumeration, "developerLogLevel")

            self.snmploglevel = YLeaf(YType.enumeration, "snmpLogLevel")

            self.auditlog = None
            self._children_name_map["auditlog"] = "auditLog"
            self._children_yang_names.add("auditLog")

            self.confdlog = None
            self._children_name_map["confdlog"] = "confdLog"
            self._children_yang_names.add("confdLog")

            self.developerlog = None
            self._children_name_map["developerlog"] = "developerLog"
            self._children_yang_names.add("developerLog")

            self.errorlog = None
            self._children_name_map["errorlog"] = "errorLog"
            self._children_yang_names.add("errorLog")

            self.netconflog = None
            self._children_name_map["netconflog"] = "netconfLog"
            self._children_yang_names.add("netconfLog")

            self.netconftracelog = None
            self._children_name_map["netconftracelog"] = "netconfTraceLog"
            self._children_yang_names.add("netconfTraceLog")

            self.snmplog = None
            self._children_name_map["snmplog"] = "snmpLog"
            self._children_yang_names.add("snmpLog")

            self.syslogconfig = None
            self._children_name_map["syslogconfig"] = "syslogConfig"
            self._children_yang_names.add("syslogConfig")

            self.webuiaccesslog = None
            self._children_name_map["webuiaccesslog"] = "webuiAccessLog"
            self._children_yang_names.add("webuiAccessLog")

            self.webuibrowserlog = None
            self._children_name_map["webuibrowserlog"] = "webuiBrowserLog"
            self._children_yang_names.add("webuiBrowserLog")

            self.xpathtracelog = None
            self._children_name_map["xpathtracelog"] = "xpathTraceLog"
            self._children_yang_names.add("xpathTraceLog")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("auditlogcommit",
                            "developerloglevel",
                            "snmploglevel") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Confdconfig.Logs, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Confdconfig.Logs, self).__setattr__(name, value)


        class Syslogconfig(Entity):
            """
            
            
            .. attribute:: facility
            
            	
            	**type**\: one of the below types:
            
            	**type**\:   :py:class:`Bsdfacilitytype <ydk.models.confd_dyncfg.Bsdfacilitytype>`
            
            	**default value**\: daemon
            
            
            ----
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**default value**\: daemon
            
            
            ----
            .. attribute:: syslogservers
            
            	
            	**type**\:   :py:class:`Syslogservers <ydk.models.confd_dyncfg.Confdconfig.Logs.Syslogconfig.Syslogservers>`
            
            	**presence node**\: True
            
            .. attribute:: udp
            
            	
            	**type**\:   :py:class:`Udp <ydk.models.confd_dyncfg.Confdconfig.Logs.Syslogconfig.Udp>`
            
            	**presence node**\: True
            
            .. attribute:: version
            
            	
            	**type**\:   :py:class:`Syslogversiontype <ydk.models.confd_dyncfg.Syslogversiontype>`
            
            	**default value**\: bsd
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'confd_dyncfg'
            _revision = '2017-01-16'

            def __init__(self):
                super(Confdconfig.Logs.Syslogconfig, self).__init__()

                self.yang_name = "syslogConfig"
                self.yang_parent_name = "logs"
                self.is_presence_container = True

                self.facility = YLeaf(YType.str, "facility")

                self.version = YLeaf(YType.enumeration, "version")

                self.syslogservers = None
                self._children_name_map["syslogservers"] = "syslogServers"
                self._children_yang_names.add("syslogServers")

                self.udp = None
                self._children_name_map["udp"] = "udp"
                self._children_yang_names.add("udp")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("facility",
                                "version") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Confdconfig.Logs.Syslogconfig, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Confdconfig.Logs.Syslogconfig, self).__setattr__(name, value)


            class Udp(Entity):
                """
                
                
                .. attribute:: enabled
                
                	
                	**type**\:  bool
                
                	**default value**\: false
                
                .. attribute:: host
                
                	
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                	**mandatory**\: True
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                	**mandatory**\: True
                
                
                ----
                
                ----
                	**type**\:  str
                
                	**pattern:** ((([a\-zA\-Z0\-9\_]([a\-zA\-Z0\-9\\\-\_]){0,61})?[a\-zA\-Z0\-9]\\.)\*([a\-zA\-Z0\-9\_]([a\-zA\-Z0\-9\\\-\_]){0,61})?[a\-zA\-Z0\-9]\\.?)\|\\.
                
                	**mandatory**\: True
                
                
                ----
                .. attribute:: port
                
                	
                	**type**\:  int
                
                	**range:** 0..65535
                
                	**default value**\: 514
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'confd_dyncfg'
                _revision = '2017-01-16'

                def __init__(self):
                    super(Confdconfig.Logs.Syslogconfig.Udp, self).__init__()

                    self.yang_name = "udp"
                    self.yang_parent_name = "syslogConfig"
                    self.is_presence_container = True

                    self.enabled = YLeaf(YType.boolean, "enabled")

                    self.host = YLeaf(YType.str, "host")

                    self.port = YLeaf(YType.uint16, "port")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("enabled",
                                    "host",
                                    "port") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Confdconfig.Logs.Syslogconfig.Udp, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Confdconfig.Logs.Syslogconfig.Udp, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.enabled.is_set or
                        self.host.is_set or
                        self.port.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.enabled.yfilter != YFilter.not_set or
                        self.host.yfilter != YFilter.not_set or
                        self.port.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "udp" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "confd_dyncfg:confdConfig/logs/syslogConfig/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.enabled.is_set or self.enabled.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.enabled.get_name_leafdata())
                    if (self.host.is_set or self.host.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.host.get_name_leafdata())
                    if (self.port.is_set or self.port.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.port.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "enabled" or name == "host" or name == "port"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "enabled"):
                        self.enabled = value
                        self.enabled.value_namespace = name_space
                        self.enabled.value_namespace_prefix = name_space_prefix
                    if(value_path == "host"):
                        self.host = value
                        self.host.value_namespace = name_space
                        self.host.value_namespace_prefix = name_space_prefix
                    if(value_path == "port"):
                        self.port = value
                        self.port.value_namespace = name_space
                        self.port.value_namespace_prefix = name_space_prefix


            class Syslogservers(Entity):
                """
                
                
                .. attribute:: server
                
                	
                	**type**\: list of    :py:class:`Server <ydk.models.confd_dyncfg.Confdconfig.Logs.Syslogconfig.Syslogservers.Server>`
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'confd_dyncfg'
                _revision = '2017-01-16'

                def __init__(self):
                    super(Confdconfig.Logs.Syslogconfig.Syslogservers, self).__init__()

                    self.yang_name = "syslogServers"
                    self.yang_parent_name = "syslogConfig"
                    self.is_presence_container = True

                    self.server = YList(self)

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
                                super(Confdconfig.Logs.Syslogconfig.Syslogservers, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Confdconfig.Logs.Syslogconfig.Syslogservers, self).__setattr__(name, value)


                class Server(Entity):
                    """
                    
                    
                    .. attribute:: host  <key>
                    
                    	
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((([a\-zA\-Z0\-9\_]([a\-zA\-Z0\-9\\\-\_]){0,61})?[a\-zA\-Z0\-9]\\.)\*([a\-zA\-Z0\-9\_]([a\-zA\-Z0\-9\\\-\_]){0,61})?[a\-zA\-Z0\-9]\\.?)\|\\.
                    
                    
                    ----
                    .. attribute:: enabled
                    
                    	
                    	**type**\:  bool
                    
                    	**default value**\: true
                    
                    .. attribute:: facility
                    
                    	
                    	**type**\: one of the below types:
                    
                    	**type**\:   :py:class:`Bsdfacilitytype <ydk.models.confd_dyncfg.Bsdfacilitytype>`
                    
                    	**default value**\: daemon
                    
                    
                    ----
                    	**type**\:  int
                    
                    	**range:** 0..2147483647
                    
                    	**default value**\: daemon
                    
                    
                    ----
                    .. attribute:: port
                    
                    	
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    	**default value**\: 514
                    
                    .. attribute:: version
                    
                    	
                    	**type**\:   :py:class:`Syslogversiontype <ydk.models.confd_dyncfg.Syslogversiontype>`
                    
                    	**default value**\: bsd
                    
                    

                    """

                    _prefix = 'confd_dyncfg'
                    _revision = '2017-01-16'

                    def __init__(self):
                        super(Confdconfig.Logs.Syslogconfig.Syslogservers.Server, self).__init__()

                        self.yang_name = "server"
                        self.yang_parent_name = "syslogServers"

                        self.host = YLeaf(YType.str, "host")

                        self.enabled = YLeaf(YType.boolean, "enabled")

                        self.facility = YLeaf(YType.str, "facility")

                        self.port = YLeaf(YType.uint16, "port")

                        self.version = YLeaf(YType.enumeration, "version")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("host",
                                        "enabled",
                                        "facility",
                                        "port",
                                        "version") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Confdconfig.Logs.Syslogconfig.Syslogservers.Server, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Confdconfig.Logs.Syslogconfig.Syslogservers.Server, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.host.is_set or
                            self.enabled.is_set or
                            self.facility.is_set or
                            self.port.is_set or
                            self.version.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.host.yfilter != YFilter.not_set or
                            self.enabled.yfilter != YFilter.not_set or
                            self.facility.yfilter != YFilter.not_set or
                            self.port.yfilter != YFilter.not_set or
                            self.version.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "server" + "[host='" + self.host.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "confd_dyncfg:confdConfig/logs/syslogConfig/syslogServers/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.host.is_set or self.host.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.host.get_name_leafdata())
                        if (self.enabled.is_set or self.enabled.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.enabled.get_name_leafdata())
                        if (self.facility.is_set or self.facility.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.facility.get_name_leafdata())
                        if (self.port.is_set or self.port.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.port.get_name_leafdata())
                        if (self.version.is_set or self.version.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.version.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "host" or name == "enabled" or name == "facility" or name == "port" or name == "version"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "host"):
                            self.host = value
                            self.host.value_namespace = name_space
                            self.host.value_namespace_prefix = name_space_prefix
                        if(value_path == "enabled"):
                            self.enabled = value
                            self.enabled.value_namespace = name_space
                            self.enabled.value_namespace_prefix = name_space_prefix
                        if(value_path == "facility"):
                            self.facility = value
                            self.facility.value_namespace = name_space
                            self.facility.value_namespace_prefix = name_space_prefix
                        if(value_path == "port"):
                            self.port = value
                            self.port.value_namespace = name_space
                            self.port.value_namespace_prefix = name_space_prefix
                        if(value_path == "version"):
                            self.version = value
                            self.version.value_namespace = name_space
                            self.version.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.server:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.server:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "syslogServers" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "confd_dyncfg:confdConfig/logs/syslogConfig/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "server"):
                        for c in self.server:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Confdconfig.Logs.Syslogconfig.Syslogservers.Server()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.server.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "server"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.facility.is_set or
                    self.version.is_set or
                    (self.syslogservers is not None) or
                    (self.udp is not None))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.facility.yfilter != YFilter.not_set or
                    self.version.yfilter != YFilter.not_set or
                    (self.syslogservers is not None and self.syslogservers.has_operation()) or
                    (self.udp is not None and self.udp.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "syslogConfig" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "confd_dyncfg:confdConfig/logs/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.facility.is_set or self.facility.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.facility.get_name_leafdata())
                if (self.version.is_set or self.version.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.version.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "syslogServers"):
                    if (self.syslogservers is None):
                        self.syslogservers = Confdconfig.Logs.Syslogconfig.Syslogservers()
                        self.syslogservers.parent = self
                        self._children_name_map["syslogservers"] = "syslogServers"
                    return self.syslogservers

                if (child_yang_name == "udp"):
                    if (self.udp is None):
                        self.udp = Confdconfig.Logs.Syslogconfig.Udp()
                        self.udp.parent = self
                        self._children_name_map["udp"] = "udp"
                    return self.udp

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "syslogServers" or name == "udp" or name == "facility" or name == "version"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "facility"):
                    self.facility = value
                    self.facility.value_namespace = name_space
                    self.facility.value_namespace_prefix = name_space_prefix
                if(value_path == "version"):
                    self.version = value
                    self.version.value_namespace = name_space
                    self.version.value_namespace_prefix = name_space_prefix


        class Confdlog(Entity):
            """
            
            
            .. attribute:: enabled
            
            	
            	**type**\:  bool
            
            	**default value**\: true
            
            .. attribute:: file
            
            	
            	**type**\:   :py:class:`File <ydk.models.confd_dyncfg.Confdconfig.Logs.Confdlog.File>`
            
            	**presence node**\: True
            
            .. attribute:: syslog
            
            	
            	**type**\:   :py:class:`Syslog <ydk.models.confd_dyncfg.Confdconfig.Logs.Confdlog.Syslog>`
            
            	**presence node**\: True
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'confd_dyncfg'
            _revision = '2017-01-16'

            def __init__(self):
                super(Confdconfig.Logs.Confdlog, self).__init__()

                self.yang_name = "confdLog"
                self.yang_parent_name = "logs"
                self.is_presence_container = True

                self.enabled = YLeaf(YType.boolean, "enabled")

                self.file = None
                self._children_name_map["file"] = "file"
                self._children_yang_names.add("file")

                self.syslog = None
                self._children_name_map["syslog"] = "syslog"
                self._children_yang_names.add("syslog")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("enabled") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Confdconfig.Logs.Confdlog, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Confdconfig.Logs.Confdlog, self).__setattr__(name, value)


            class File(Entity):
                """
                
                
                .. attribute:: enabled
                
                	
                	**type**\:  bool
                
                	**default value**\: false
                
                .. attribute:: name
                
                	
                	**type**\:  str
                
                	**mandatory**\: True
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'confd_dyncfg'
                _revision = '2017-01-16'

                def __init__(self):
                    super(Confdconfig.Logs.Confdlog.File, self).__init__()

                    self.yang_name = "file"
                    self.yang_parent_name = "confdLog"
                    self.is_presence_container = True

                    self.enabled = YLeaf(YType.boolean, "enabled")

                    self.name = YLeaf(YType.str, "name")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("enabled",
                                    "name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Confdconfig.Logs.Confdlog.File, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Confdconfig.Logs.Confdlog.File, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.enabled.is_set or
                        self.name.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.enabled.yfilter != YFilter.not_set or
                        self.name.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "file" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "confd_dyncfg:confdConfig/logs/confdLog/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.enabled.is_set or self.enabled.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.enabled.get_name_leafdata())
                    if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.name.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "enabled" or name == "name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "enabled"):
                        self.enabled = value
                        self.enabled.value_namespace = name_space
                        self.enabled.value_namespace_prefix = name_space_prefix
                    if(value_path == "name"):
                        self.name = value
                        self.name.value_namespace = name_space
                        self.name.value_namespace_prefix = name_space_prefix


            class Syslog(Entity):
                """
                
                
                .. attribute:: enabled
                
                	
                	**type**\:  bool
                
                	**default value**\: false
                
                .. attribute:: facility
                
                	
                	**type**\: one of the below types:
                
                	**type**\:   :py:class:`Bsdfacilitytype <ydk.models.confd_dyncfg.Bsdfacilitytype>`
                
                
                ----
                	**type**\:  int
                
                	**range:** 0..2147483647
                
                
                ----
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'confd_dyncfg'
                _revision = '2017-01-16'

                def __init__(self):
                    super(Confdconfig.Logs.Confdlog.Syslog, self).__init__()

                    self.yang_name = "syslog"
                    self.yang_parent_name = "confdLog"
                    self.is_presence_container = True

                    self.enabled = YLeaf(YType.boolean, "enabled")

                    self.facility = YLeaf(YType.str, "facility")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("enabled",
                                    "facility") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Confdconfig.Logs.Confdlog.Syslog, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Confdconfig.Logs.Confdlog.Syslog, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.enabled.is_set or
                        self.facility.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.enabled.yfilter != YFilter.not_set or
                        self.facility.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "syslog" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "confd_dyncfg:confdConfig/logs/confdLog/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.enabled.is_set or self.enabled.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.enabled.get_name_leafdata())
                    if (self.facility.is_set or self.facility.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.facility.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "enabled" or name == "facility"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "enabled"):
                        self.enabled = value
                        self.enabled.value_namespace = name_space
                        self.enabled.value_namespace_prefix = name_space_prefix
                    if(value_path == "facility"):
                        self.facility = value
                        self.facility.value_namespace = name_space
                        self.facility.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.enabled.is_set or
                    (self.file is not None) or
                    (self.syslog is not None))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.enabled.yfilter != YFilter.not_set or
                    (self.file is not None and self.file.has_operation()) or
                    (self.syslog is not None and self.syslog.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "confdLog" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "confd_dyncfg:confdConfig/logs/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.enabled.is_set or self.enabled.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.enabled.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "file"):
                    if (self.file is None):
                        self.file = Confdconfig.Logs.Confdlog.File()
                        self.file.parent = self
                        self._children_name_map["file"] = "file"
                    return self.file

                if (child_yang_name == "syslog"):
                    if (self.syslog is None):
                        self.syslog = Confdconfig.Logs.Confdlog.Syslog()
                        self.syslog.parent = self
                        self._children_name_map["syslog"] = "syslog"
                    return self.syslog

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "file" or name == "syslog" or name == "enabled"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "enabled"):
                    self.enabled = value
                    self.enabled.value_namespace = name_space
                    self.enabled.value_namespace_prefix = name_space_prefix


        class Developerlog(Entity):
            """
            
            
            .. attribute:: enabled
            
            	
            	**type**\:  bool
            
            	**default value**\: true
            
            .. attribute:: file
            
            	
            	**type**\:   :py:class:`File <ydk.models.confd_dyncfg.Confdconfig.Logs.Developerlog.File>`
            
            	**presence node**\: True
            
            .. attribute:: syslog
            
            	
            	**type**\:   :py:class:`Syslog <ydk.models.confd_dyncfg.Confdconfig.Logs.Developerlog.Syslog>`
            
            	**presence node**\: True
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'confd_dyncfg'
            _revision = '2017-01-16'

            def __init__(self):
                super(Confdconfig.Logs.Developerlog, self).__init__()

                self.yang_name = "developerLog"
                self.yang_parent_name = "logs"
                self.is_presence_container = True

                self.enabled = YLeaf(YType.boolean, "enabled")

                self.file = None
                self._children_name_map["file"] = "file"
                self._children_yang_names.add("file")

                self.syslog = None
                self._children_name_map["syslog"] = "syslog"
                self._children_yang_names.add("syslog")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("enabled") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Confdconfig.Logs.Developerlog, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Confdconfig.Logs.Developerlog, self).__setattr__(name, value)


            class File(Entity):
                """
                
                
                .. attribute:: enabled
                
                	
                	**type**\:  bool
                
                	**default value**\: false
                
                .. attribute:: name
                
                	
                	**type**\:  str
                
                	**mandatory**\: True
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'confd_dyncfg'
                _revision = '2017-01-16'

                def __init__(self):
                    super(Confdconfig.Logs.Developerlog.File, self).__init__()

                    self.yang_name = "file"
                    self.yang_parent_name = "developerLog"
                    self.is_presence_container = True

                    self.enabled = YLeaf(YType.boolean, "enabled")

                    self.name = YLeaf(YType.str, "name")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("enabled",
                                    "name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Confdconfig.Logs.Developerlog.File, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Confdconfig.Logs.Developerlog.File, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.enabled.is_set or
                        self.name.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.enabled.yfilter != YFilter.not_set or
                        self.name.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "file" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "confd_dyncfg:confdConfig/logs/developerLog/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.enabled.is_set or self.enabled.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.enabled.get_name_leafdata())
                    if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.name.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "enabled" or name == "name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "enabled"):
                        self.enabled = value
                        self.enabled.value_namespace = name_space
                        self.enabled.value_namespace_prefix = name_space_prefix
                    if(value_path == "name"):
                        self.name = value
                        self.name.value_namespace = name_space
                        self.name.value_namespace_prefix = name_space_prefix


            class Syslog(Entity):
                """
                
                
                .. attribute:: enabled
                
                	
                	**type**\:  bool
                
                	**default value**\: false
                
                .. attribute:: facility
                
                	
                	**type**\: one of the below types:
                
                	**type**\:   :py:class:`Bsdfacilitytype <ydk.models.confd_dyncfg.Bsdfacilitytype>`
                
                
                ----
                	**type**\:  int
                
                	**range:** 0..2147483647
                
                
                ----
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'confd_dyncfg'
                _revision = '2017-01-16'

                def __init__(self):
                    super(Confdconfig.Logs.Developerlog.Syslog, self).__init__()

                    self.yang_name = "syslog"
                    self.yang_parent_name = "developerLog"
                    self.is_presence_container = True

                    self.enabled = YLeaf(YType.boolean, "enabled")

                    self.facility = YLeaf(YType.str, "facility")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("enabled",
                                    "facility") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Confdconfig.Logs.Developerlog.Syslog, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Confdconfig.Logs.Developerlog.Syslog, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.enabled.is_set or
                        self.facility.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.enabled.yfilter != YFilter.not_set or
                        self.facility.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "syslog" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "confd_dyncfg:confdConfig/logs/developerLog/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.enabled.is_set or self.enabled.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.enabled.get_name_leafdata())
                    if (self.facility.is_set or self.facility.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.facility.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "enabled" or name == "facility"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "enabled"):
                        self.enabled = value
                        self.enabled.value_namespace = name_space
                        self.enabled.value_namespace_prefix = name_space_prefix
                    if(value_path == "facility"):
                        self.facility = value
                        self.facility.value_namespace = name_space
                        self.facility.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.enabled.is_set or
                    (self.file is not None) or
                    (self.syslog is not None))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.enabled.yfilter != YFilter.not_set or
                    (self.file is not None and self.file.has_operation()) or
                    (self.syslog is not None and self.syslog.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "developerLog" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "confd_dyncfg:confdConfig/logs/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.enabled.is_set or self.enabled.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.enabled.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "file"):
                    if (self.file is None):
                        self.file = Confdconfig.Logs.Developerlog.File()
                        self.file.parent = self
                        self._children_name_map["file"] = "file"
                    return self.file

                if (child_yang_name == "syslog"):
                    if (self.syslog is None):
                        self.syslog = Confdconfig.Logs.Developerlog.Syslog()
                        self.syslog.parent = self
                        self._children_name_map["syslog"] = "syslog"
                    return self.syslog

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "file" or name == "syslog" or name == "enabled"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "enabled"):
                    self.enabled = value
                    self.enabled.value_namespace = name_space
                    self.enabled.value_namespace_prefix = name_space_prefix


        class Auditlog(Entity):
            """
            
            
            .. attribute:: enabled
            
            	
            	**type**\:  bool
            
            	**default value**\: true
            
            .. attribute:: file
            
            	
            	**type**\:   :py:class:`File <ydk.models.confd_dyncfg.Confdconfig.Logs.Auditlog.File>`
            
            	**presence node**\: True
            
            .. attribute:: syslog
            
            	
            	**type**\:   :py:class:`Syslog <ydk.models.confd_dyncfg.Confdconfig.Logs.Auditlog.Syslog>`
            
            	**presence node**\: True
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'confd_dyncfg'
            _revision = '2017-01-16'

            def __init__(self):
                super(Confdconfig.Logs.Auditlog, self).__init__()

                self.yang_name = "auditLog"
                self.yang_parent_name = "logs"
                self.is_presence_container = True

                self.enabled = YLeaf(YType.boolean, "enabled")

                self.file = None
                self._children_name_map["file"] = "file"
                self._children_yang_names.add("file")

                self.syslog = None
                self._children_name_map["syslog"] = "syslog"
                self._children_yang_names.add("syslog")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("enabled") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Confdconfig.Logs.Auditlog, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Confdconfig.Logs.Auditlog, self).__setattr__(name, value)


            class File(Entity):
                """
                
                
                .. attribute:: enabled
                
                	
                	**type**\:  bool
                
                	**default value**\: false
                
                .. attribute:: name
                
                	
                	**type**\:  str
                
                	**mandatory**\: True
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'confd_dyncfg'
                _revision = '2017-01-16'

                def __init__(self):
                    super(Confdconfig.Logs.Auditlog.File, self).__init__()

                    self.yang_name = "file"
                    self.yang_parent_name = "auditLog"
                    self.is_presence_container = True

                    self.enabled = YLeaf(YType.boolean, "enabled")

                    self.name = YLeaf(YType.str, "name")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("enabled",
                                    "name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Confdconfig.Logs.Auditlog.File, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Confdconfig.Logs.Auditlog.File, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.enabled.is_set or
                        self.name.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.enabled.yfilter != YFilter.not_set or
                        self.name.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "file" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "confd_dyncfg:confdConfig/logs/auditLog/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.enabled.is_set or self.enabled.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.enabled.get_name_leafdata())
                    if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.name.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "enabled" or name == "name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "enabled"):
                        self.enabled = value
                        self.enabled.value_namespace = name_space
                        self.enabled.value_namespace_prefix = name_space_prefix
                    if(value_path == "name"):
                        self.name = value
                        self.name.value_namespace = name_space
                        self.name.value_namespace_prefix = name_space_prefix


            class Syslog(Entity):
                """
                
                
                .. attribute:: enabled
                
                	
                	**type**\:  bool
                
                	**default value**\: false
                
                .. attribute:: facility
                
                	
                	**type**\: one of the below types:
                
                	**type**\:   :py:class:`Bsdfacilitytype <ydk.models.confd_dyncfg.Bsdfacilitytype>`
                
                
                ----
                	**type**\:  int
                
                	**range:** 0..2147483647
                
                
                ----
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'confd_dyncfg'
                _revision = '2017-01-16'

                def __init__(self):
                    super(Confdconfig.Logs.Auditlog.Syslog, self).__init__()

                    self.yang_name = "syslog"
                    self.yang_parent_name = "auditLog"
                    self.is_presence_container = True

                    self.enabled = YLeaf(YType.boolean, "enabled")

                    self.facility = YLeaf(YType.str, "facility")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("enabled",
                                    "facility") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Confdconfig.Logs.Auditlog.Syslog, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Confdconfig.Logs.Auditlog.Syslog, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.enabled.is_set or
                        self.facility.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.enabled.yfilter != YFilter.not_set or
                        self.facility.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "syslog" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "confd_dyncfg:confdConfig/logs/auditLog/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.enabled.is_set or self.enabled.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.enabled.get_name_leafdata())
                    if (self.facility.is_set or self.facility.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.facility.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "enabled" or name == "facility"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "enabled"):
                        self.enabled = value
                        self.enabled.value_namespace = name_space
                        self.enabled.value_namespace_prefix = name_space_prefix
                    if(value_path == "facility"):
                        self.facility = value
                        self.facility.value_namespace = name_space
                        self.facility.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.enabled.is_set or
                    (self.file is not None) or
                    (self.syslog is not None))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.enabled.yfilter != YFilter.not_set or
                    (self.file is not None and self.file.has_operation()) or
                    (self.syslog is not None and self.syslog.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "auditLog" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "confd_dyncfg:confdConfig/logs/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.enabled.is_set or self.enabled.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.enabled.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "file"):
                    if (self.file is None):
                        self.file = Confdconfig.Logs.Auditlog.File()
                        self.file.parent = self
                        self._children_name_map["file"] = "file"
                    return self.file

                if (child_yang_name == "syslog"):
                    if (self.syslog is None):
                        self.syslog = Confdconfig.Logs.Auditlog.Syslog()
                        self.syslog.parent = self
                        self._children_name_map["syslog"] = "syslog"
                    return self.syslog

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "file" or name == "syslog" or name == "enabled"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "enabled"):
                    self.enabled = value
                    self.enabled.value_namespace = name_space
                    self.enabled.value_namespace_prefix = name_space_prefix


        class Netconflog(Entity):
            """
            
            
            .. attribute:: enabled
            
            	
            	**type**\:  bool
            
            	**default value**\: true
            
            .. attribute:: file
            
            	
            	**type**\:   :py:class:`File <ydk.models.confd_dyncfg.Confdconfig.Logs.Netconflog.File>`
            
            	**presence node**\: True
            
            .. attribute:: syslog
            
            	
            	**type**\:   :py:class:`Syslog <ydk.models.confd_dyncfg.Confdconfig.Logs.Netconflog.Syslog>`
            
            	**presence node**\: True
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'confd_dyncfg'
            _revision = '2017-01-16'

            def __init__(self):
                super(Confdconfig.Logs.Netconflog, self).__init__()

                self.yang_name = "netconfLog"
                self.yang_parent_name = "logs"
                self.is_presence_container = True

                self.enabled = YLeaf(YType.boolean, "enabled")

                self.file = None
                self._children_name_map["file"] = "file"
                self._children_yang_names.add("file")

                self.syslog = None
                self._children_name_map["syslog"] = "syslog"
                self._children_yang_names.add("syslog")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("enabled") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Confdconfig.Logs.Netconflog, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Confdconfig.Logs.Netconflog, self).__setattr__(name, value)


            class File(Entity):
                """
                
                
                .. attribute:: enabled
                
                	
                	**type**\:  bool
                
                	**default value**\: false
                
                .. attribute:: name
                
                	
                	**type**\:  str
                
                	**mandatory**\: True
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'confd_dyncfg'
                _revision = '2017-01-16'

                def __init__(self):
                    super(Confdconfig.Logs.Netconflog.File, self).__init__()

                    self.yang_name = "file"
                    self.yang_parent_name = "netconfLog"
                    self.is_presence_container = True

                    self.enabled = YLeaf(YType.boolean, "enabled")

                    self.name = YLeaf(YType.str, "name")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("enabled",
                                    "name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Confdconfig.Logs.Netconflog.File, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Confdconfig.Logs.Netconflog.File, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.enabled.is_set or
                        self.name.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.enabled.yfilter != YFilter.not_set or
                        self.name.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "file" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "confd_dyncfg:confdConfig/logs/netconfLog/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.enabled.is_set or self.enabled.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.enabled.get_name_leafdata())
                    if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.name.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "enabled" or name == "name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "enabled"):
                        self.enabled = value
                        self.enabled.value_namespace = name_space
                        self.enabled.value_namespace_prefix = name_space_prefix
                    if(value_path == "name"):
                        self.name = value
                        self.name.value_namespace = name_space
                        self.name.value_namespace_prefix = name_space_prefix


            class Syslog(Entity):
                """
                
                
                .. attribute:: enabled
                
                	
                	**type**\:  bool
                
                	**default value**\: false
                
                .. attribute:: facility
                
                	
                	**type**\: one of the below types:
                
                	**type**\:   :py:class:`Bsdfacilitytype <ydk.models.confd_dyncfg.Bsdfacilitytype>`
                
                
                ----
                	**type**\:  int
                
                	**range:** 0..2147483647
                
                
                ----
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'confd_dyncfg'
                _revision = '2017-01-16'

                def __init__(self):
                    super(Confdconfig.Logs.Netconflog.Syslog, self).__init__()

                    self.yang_name = "syslog"
                    self.yang_parent_name = "netconfLog"
                    self.is_presence_container = True

                    self.enabled = YLeaf(YType.boolean, "enabled")

                    self.facility = YLeaf(YType.str, "facility")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("enabled",
                                    "facility") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Confdconfig.Logs.Netconflog.Syslog, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Confdconfig.Logs.Netconflog.Syslog, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.enabled.is_set or
                        self.facility.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.enabled.yfilter != YFilter.not_set or
                        self.facility.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "syslog" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "confd_dyncfg:confdConfig/logs/netconfLog/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.enabled.is_set or self.enabled.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.enabled.get_name_leafdata())
                    if (self.facility.is_set or self.facility.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.facility.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "enabled" or name == "facility"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "enabled"):
                        self.enabled = value
                        self.enabled.value_namespace = name_space
                        self.enabled.value_namespace_prefix = name_space_prefix
                    if(value_path == "facility"):
                        self.facility = value
                        self.facility.value_namespace = name_space
                        self.facility.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.enabled.is_set or
                    (self.file is not None) or
                    (self.syslog is not None))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.enabled.yfilter != YFilter.not_set or
                    (self.file is not None and self.file.has_operation()) or
                    (self.syslog is not None and self.syslog.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "netconfLog" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "confd_dyncfg:confdConfig/logs/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.enabled.is_set or self.enabled.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.enabled.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "file"):
                    if (self.file is None):
                        self.file = Confdconfig.Logs.Netconflog.File()
                        self.file.parent = self
                        self._children_name_map["file"] = "file"
                    return self.file

                if (child_yang_name == "syslog"):
                    if (self.syslog is None):
                        self.syslog = Confdconfig.Logs.Netconflog.Syslog()
                        self.syslog.parent = self
                        self._children_name_map["syslog"] = "syslog"
                    return self.syslog

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "file" or name == "syslog" or name == "enabled"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "enabled"):
                    self.enabled = value
                    self.enabled.value_namespace = name_space
                    self.enabled.value_namespace_prefix = name_space_prefix


        class Snmplog(Entity):
            """
            
            
            .. attribute:: enabled
            
            	
            	**type**\:  bool
            
            	**default value**\: true
            
            .. attribute:: file
            
            	
            	**type**\:   :py:class:`File <ydk.models.confd_dyncfg.Confdconfig.Logs.Snmplog.File>`
            
            	**presence node**\: True
            
            .. attribute:: syslog
            
            	
            	**type**\:   :py:class:`Syslog <ydk.models.confd_dyncfg.Confdconfig.Logs.Snmplog.Syslog>`
            
            	**presence node**\: True
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'confd_dyncfg'
            _revision = '2017-01-16'

            def __init__(self):
                super(Confdconfig.Logs.Snmplog, self).__init__()

                self.yang_name = "snmpLog"
                self.yang_parent_name = "logs"
                self.is_presence_container = True

                self.enabled = YLeaf(YType.boolean, "enabled")

                self.file = None
                self._children_name_map["file"] = "file"
                self._children_yang_names.add("file")

                self.syslog = None
                self._children_name_map["syslog"] = "syslog"
                self._children_yang_names.add("syslog")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("enabled") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Confdconfig.Logs.Snmplog, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Confdconfig.Logs.Snmplog, self).__setattr__(name, value)


            class File(Entity):
                """
                
                
                .. attribute:: enabled
                
                	
                	**type**\:  bool
                
                	**default value**\: false
                
                .. attribute:: name
                
                	
                	**type**\:  str
                
                	**mandatory**\: True
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'confd_dyncfg'
                _revision = '2017-01-16'

                def __init__(self):
                    super(Confdconfig.Logs.Snmplog.File, self).__init__()

                    self.yang_name = "file"
                    self.yang_parent_name = "snmpLog"
                    self.is_presence_container = True

                    self.enabled = YLeaf(YType.boolean, "enabled")

                    self.name = YLeaf(YType.str, "name")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("enabled",
                                    "name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Confdconfig.Logs.Snmplog.File, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Confdconfig.Logs.Snmplog.File, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.enabled.is_set or
                        self.name.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.enabled.yfilter != YFilter.not_set or
                        self.name.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "file" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "confd_dyncfg:confdConfig/logs/snmpLog/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.enabled.is_set or self.enabled.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.enabled.get_name_leafdata())
                    if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.name.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "enabled" or name == "name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "enabled"):
                        self.enabled = value
                        self.enabled.value_namespace = name_space
                        self.enabled.value_namespace_prefix = name_space_prefix
                    if(value_path == "name"):
                        self.name = value
                        self.name.value_namespace = name_space
                        self.name.value_namespace_prefix = name_space_prefix


            class Syslog(Entity):
                """
                
                
                .. attribute:: enabled
                
                	
                	**type**\:  bool
                
                	**default value**\: false
                
                .. attribute:: facility
                
                	
                	**type**\: one of the below types:
                
                	**type**\:   :py:class:`Bsdfacilitytype <ydk.models.confd_dyncfg.Bsdfacilitytype>`
                
                
                ----
                	**type**\:  int
                
                	**range:** 0..2147483647
                
                
                ----
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'confd_dyncfg'
                _revision = '2017-01-16'

                def __init__(self):
                    super(Confdconfig.Logs.Snmplog.Syslog, self).__init__()

                    self.yang_name = "syslog"
                    self.yang_parent_name = "snmpLog"
                    self.is_presence_container = True

                    self.enabled = YLeaf(YType.boolean, "enabled")

                    self.facility = YLeaf(YType.str, "facility")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("enabled",
                                    "facility") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Confdconfig.Logs.Snmplog.Syslog, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Confdconfig.Logs.Snmplog.Syslog, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.enabled.is_set or
                        self.facility.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.enabled.yfilter != YFilter.not_set or
                        self.facility.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "syslog" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "confd_dyncfg:confdConfig/logs/snmpLog/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.enabled.is_set or self.enabled.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.enabled.get_name_leafdata())
                    if (self.facility.is_set or self.facility.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.facility.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "enabled" or name == "facility"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "enabled"):
                        self.enabled = value
                        self.enabled.value_namespace = name_space
                        self.enabled.value_namespace_prefix = name_space_prefix
                    if(value_path == "facility"):
                        self.facility = value
                        self.facility.value_namespace = name_space
                        self.facility.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.enabled.is_set or
                    (self.file is not None) or
                    (self.syslog is not None))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.enabled.yfilter != YFilter.not_set or
                    (self.file is not None and self.file.has_operation()) or
                    (self.syslog is not None and self.syslog.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "snmpLog" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "confd_dyncfg:confdConfig/logs/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.enabled.is_set or self.enabled.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.enabled.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "file"):
                    if (self.file is None):
                        self.file = Confdconfig.Logs.Snmplog.File()
                        self.file.parent = self
                        self._children_name_map["file"] = "file"
                    return self.file

                if (child_yang_name == "syslog"):
                    if (self.syslog is None):
                        self.syslog = Confdconfig.Logs.Snmplog.Syslog()
                        self.syslog.parent = self
                        self._children_name_map["syslog"] = "syslog"
                    return self.syslog

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "file" or name == "syslog" or name == "enabled"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "enabled"):
                    self.enabled = value
                    self.enabled.value_namespace = name_space
                    self.enabled.value_namespace_prefix = name_space_prefix


        class Webuibrowserlog(Entity):
            """
            
            
            .. attribute:: enabled
            
            	
            	**type**\:  bool
            
            	**default value**\: false
            
            .. attribute:: filename
            
            	
            	**type**\:  str
            
            	**mandatory**\: True
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'confd_dyncfg'
            _revision = '2017-01-16'

            def __init__(self):
                super(Confdconfig.Logs.Webuibrowserlog, self).__init__()

                self.yang_name = "webuiBrowserLog"
                self.yang_parent_name = "logs"
                self.is_presence_container = True

                self.enabled = YLeaf(YType.boolean, "enabled")

                self.filename = YLeaf(YType.str, "filename")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("enabled",
                                "filename") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Confdconfig.Logs.Webuibrowserlog, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Confdconfig.Logs.Webuibrowserlog, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.enabled.is_set or
                    self.filename.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.enabled.yfilter != YFilter.not_set or
                    self.filename.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "webuiBrowserLog" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "confd_dyncfg:confdConfig/logs/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.enabled.is_set or self.enabled.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.enabled.get_name_leafdata())
                if (self.filename.is_set or self.filename.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.filename.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "enabled" or name == "filename"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "enabled"):
                    self.enabled = value
                    self.enabled.value_namespace = name_space
                    self.enabled.value_namespace_prefix = name_space_prefix
                if(value_path == "filename"):
                    self.filename = value
                    self.filename.value_namespace = name_space
                    self.filename.value_namespace_prefix = name_space_prefix


        class Webuiaccesslog(Entity):
            """
            
            
            .. attribute:: dir
            
            	
            	**type**\:  str
            
            	**mandatory**\: True
            
            .. attribute:: enabled
            
            	
            	**type**\:  bool
            
            	**default value**\: false
            
            .. attribute:: trafficlog
            
            	
            	**type**\:  bool
            
            	**default value**\: false
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'confd_dyncfg'
            _revision = '2017-01-16'

            def __init__(self):
                super(Confdconfig.Logs.Webuiaccesslog, self).__init__()

                self.yang_name = "webuiAccessLog"
                self.yang_parent_name = "logs"
                self.is_presence_container = True

                self.dir = YLeaf(YType.str, "dir")

                self.enabled = YLeaf(YType.boolean, "enabled")

                self.trafficlog = YLeaf(YType.boolean, "trafficLog")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("dir",
                                "enabled",
                                "trafficlog") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Confdconfig.Logs.Webuiaccesslog, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Confdconfig.Logs.Webuiaccesslog, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.dir.is_set or
                    self.enabled.is_set or
                    self.trafficlog.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.dir.yfilter != YFilter.not_set or
                    self.enabled.yfilter != YFilter.not_set or
                    self.trafficlog.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "webuiAccessLog" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "confd_dyncfg:confdConfig/logs/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.dir.is_set or self.dir.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dir.get_name_leafdata())
                if (self.enabled.is_set or self.enabled.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.enabled.get_name_leafdata())
                if (self.trafficlog.is_set or self.trafficlog.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.trafficlog.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "dir" or name == "enabled" or name == "trafficLog"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "dir"):
                    self.dir = value
                    self.dir.value_namespace = name_space
                    self.dir.value_namespace_prefix = name_space_prefix
                if(value_path == "enabled"):
                    self.enabled = value
                    self.enabled.value_namespace = name_space
                    self.enabled.value_namespace_prefix = name_space_prefix
                if(value_path == "trafficLog"):
                    self.trafficlog = value
                    self.trafficlog.value_namespace = name_space
                    self.trafficlog.value_namespace_prefix = name_space_prefix


        class Netconftracelog(Entity):
            """
            
            
            .. attribute:: enabled
            
            	
            	**type**\:  bool
            
            	**default value**\: false
            
            .. attribute:: filename
            
            	
            	**type**\:  str
            
            	**mandatory**\: True
            
            .. attribute:: format
            
            	
            	**type**\:   :py:class:`Netconftraceformattype <ydk.models.confd_dyncfg.Netconftraceformattype>`
            
            	**default value**\: pretty
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'confd_dyncfg'
            _revision = '2017-01-16'

            def __init__(self):
                super(Confdconfig.Logs.Netconftracelog, self).__init__()

                self.yang_name = "netconfTraceLog"
                self.yang_parent_name = "logs"
                self.is_presence_container = True

                self.enabled = YLeaf(YType.boolean, "enabled")

                self.filename = YLeaf(YType.str, "filename")

                self.format = YLeaf(YType.enumeration, "format")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("enabled",
                                "filename",
                                "format") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Confdconfig.Logs.Netconftracelog, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Confdconfig.Logs.Netconftracelog, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.enabled.is_set or
                    self.filename.is_set or
                    self.format.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.enabled.yfilter != YFilter.not_set or
                    self.filename.yfilter != YFilter.not_set or
                    self.format.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "netconfTraceLog" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "confd_dyncfg:confdConfig/logs/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.enabled.is_set or self.enabled.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.enabled.get_name_leafdata())
                if (self.filename.is_set or self.filename.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.filename.get_name_leafdata())
                if (self.format.is_set or self.format.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.format.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "enabled" or name == "filename" or name == "format"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "enabled"):
                    self.enabled = value
                    self.enabled.value_namespace = name_space
                    self.enabled.value_namespace_prefix = name_space_prefix
                if(value_path == "filename"):
                    self.filename = value
                    self.filename.value_namespace = name_space
                    self.filename.value_namespace_prefix = name_space_prefix
                if(value_path == "format"):
                    self.format = value
                    self.format.value_namespace = name_space
                    self.format.value_namespace_prefix = name_space_prefix


        class Xpathtracelog(Entity):
            """
            
            
            .. attribute:: enabled
            
            	
            	**type**\:  bool
            
            	**default value**\: false
            
            .. attribute:: filename
            
            	
            	**type**\:  str
            
            	**mandatory**\: True
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'confd_dyncfg'
            _revision = '2017-01-16'

            def __init__(self):
                super(Confdconfig.Logs.Xpathtracelog, self).__init__()

                self.yang_name = "xpathTraceLog"
                self.yang_parent_name = "logs"
                self.is_presence_container = True

                self.enabled = YLeaf(YType.boolean, "enabled")

                self.filename = YLeaf(YType.str, "filename")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("enabled",
                                "filename") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Confdconfig.Logs.Xpathtracelog, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Confdconfig.Logs.Xpathtracelog, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.enabled.is_set or
                    self.filename.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.enabled.yfilter != YFilter.not_set or
                    self.filename.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "xpathTraceLog" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "confd_dyncfg:confdConfig/logs/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.enabled.is_set or self.enabled.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.enabled.get_name_leafdata())
                if (self.filename.is_set or self.filename.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.filename.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "enabled" or name == "filename"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "enabled"):
                    self.enabled = value
                    self.enabled.value_namespace = name_space
                    self.enabled.value_namespace_prefix = name_space_prefix
                if(value_path == "filename"):
                    self.filename = value
                    self.filename.value_namespace = name_space
                    self.filename.value_namespace_prefix = name_space_prefix


        class Errorlog(Entity):
            """
            
            
            .. attribute:: debug
            
            	
            	**type**\:   :py:class:`Debug <ydk.models.confd_dyncfg.Confdconfig.Logs.Errorlog.Debug>`
            
            	**presence node**\: True
            
            .. attribute:: enabled
            
            	
            	**type**\:  bool
            
            	**default value**\: false
            
            .. attribute:: filename
            
            	
            	**type**\:  str
            
            	**mandatory**\: True
            
            .. attribute:: maxsize
            
            	
            	**type**\:  str
            
            	**pattern:** S(\\d+G)?(\\d+M)?(\\d+K)?(\\d+B)?
            
            	**default value**\: S1M
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'confd_dyncfg'
            _revision = '2017-01-16'

            def __init__(self):
                super(Confdconfig.Logs.Errorlog, self).__init__()

                self.yang_name = "errorLog"
                self.yang_parent_name = "logs"
                self.is_presence_container = True

                self.enabled = YLeaf(YType.boolean, "enabled")

                self.filename = YLeaf(YType.str, "filename")

                self.maxsize = YLeaf(YType.str, "maxSize")

                self.debug = None
                self._children_name_map["debug"] = "debug"
                self._children_yang_names.add("debug")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("enabled",
                                "filename",
                                "maxsize") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Confdconfig.Logs.Errorlog, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Confdconfig.Logs.Errorlog, self).__setattr__(name, value)


            class Debug(Entity):
                """
                
                
                .. attribute:: enabled
                
                	
                	**type**\:  bool
                
                	**default value**\: false
                
                .. attribute:: level
                
                	
                	**type**\:  int
                
                	**range:** 0..65535
                
                	**default value**\: 2
                
                .. attribute:: tag
                
                	
                	**type**\:  list of str
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'confd_dyncfg'
                _revision = '2017-01-16'

                def __init__(self):
                    super(Confdconfig.Logs.Errorlog.Debug, self).__init__()

                    self.yang_name = "debug"
                    self.yang_parent_name = "errorLog"
                    self.is_presence_container = True

                    self.enabled = YLeaf(YType.boolean, "enabled")

                    self.level = YLeaf(YType.uint16, "level")

                    self.tag = YLeafList(YType.str, "tag")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("enabled",
                                    "level",
                                    "tag") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Confdconfig.Logs.Errorlog.Debug, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Confdconfig.Logs.Errorlog.Debug, self).__setattr__(name, value)

                def has_data(self):
                    for leaf in self.tag.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    return (
                        self.enabled.is_set or
                        self.level.is_set)

                def has_operation(self):
                    for leaf in self.tag.getYLeafs():
                        if (leaf.is_set):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.enabled.yfilter != YFilter.not_set or
                        self.level.yfilter != YFilter.not_set or
                        self.tag.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "debug" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "confd_dyncfg:confdConfig/logs/errorLog/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.enabled.is_set or self.enabled.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.enabled.get_name_leafdata())
                    if (self.level.is_set or self.level.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.level.get_name_leafdata())

                    leaf_name_data.extend(self.tag.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "enabled" or name == "level" or name == "tag"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "enabled"):
                        self.enabled = value
                        self.enabled.value_namespace = name_space
                        self.enabled.value_namespace_prefix = name_space_prefix
                    if(value_path == "level"):
                        self.level = value
                        self.level.value_namespace = name_space
                        self.level.value_namespace_prefix = name_space_prefix
                    if(value_path == "tag"):
                        self.tag.append(value)

            def has_data(self):
                return (
                    self.enabled.is_set or
                    self.filename.is_set or
                    self.maxsize.is_set or
                    (self.debug is not None))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.enabled.yfilter != YFilter.not_set or
                    self.filename.yfilter != YFilter.not_set or
                    self.maxsize.yfilter != YFilter.not_set or
                    (self.debug is not None and self.debug.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "errorLog" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "confd_dyncfg:confdConfig/logs/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.enabled.is_set or self.enabled.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.enabled.get_name_leafdata())
                if (self.filename.is_set or self.filename.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.filename.get_name_leafdata())
                if (self.maxsize.is_set or self.maxsize.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.maxsize.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "debug"):
                    if (self.debug is None):
                        self.debug = Confdconfig.Logs.Errorlog.Debug()
                        self.debug.parent = self
                        self._children_name_map["debug"] = "debug"
                    return self.debug

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "debug" or name == "enabled" or name == "filename" or name == "maxSize"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "enabled"):
                    self.enabled = value
                    self.enabled.value_namespace = name_space
                    self.enabled.value_namespace_prefix = name_space_prefix
                if(value_path == "filename"):
                    self.filename = value
                    self.filename.value_namespace = name_space
                    self.filename.value_namespace_prefix = name_space_prefix
                if(value_path == "maxSize"):
                    self.maxsize = value
                    self.maxsize.value_namespace = name_space
                    self.maxsize.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (
                self.auditlogcommit.is_set or
                self.developerloglevel.is_set or
                self.snmploglevel.is_set or
                (self.auditlog is not None) or
                (self.confdlog is not None) or
                (self.developerlog is not None) or
                (self.errorlog is not None) or
                (self.netconflog is not None) or
                (self.netconftracelog is not None) or
                (self.snmplog is not None) or
                (self.syslogconfig is not None) or
                (self.webuiaccesslog is not None) or
                (self.webuibrowserlog is not None) or
                (self.xpathtracelog is not None))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.auditlogcommit.yfilter != YFilter.not_set or
                self.developerloglevel.yfilter != YFilter.not_set or
                self.snmploglevel.yfilter != YFilter.not_set or
                (self.auditlog is not None and self.auditlog.has_operation()) or
                (self.confdlog is not None and self.confdlog.has_operation()) or
                (self.developerlog is not None and self.developerlog.has_operation()) or
                (self.errorlog is not None and self.errorlog.has_operation()) or
                (self.netconflog is not None and self.netconflog.has_operation()) or
                (self.netconftracelog is not None and self.netconftracelog.has_operation()) or
                (self.snmplog is not None and self.snmplog.has_operation()) or
                (self.syslogconfig is not None and self.syslogconfig.has_operation()) or
                (self.webuiaccesslog is not None and self.webuiaccesslog.has_operation()) or
                (self.webuibrowserlog is not None and self.webuibrowserlog.has_operation()) or
                (self.xpathtracelog is not None and self.xpathtracelog.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "logs" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "confd_dyncfg:confdConfig/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.auditlogcommit.is_set or self.auditlogcommit.yfilter != YFilter.not_set):
                leaf_name_data.append(self.auditlogcommit.get_name_leafdata())
            if (self.developerloglevel.is_set or self.developerloglevel.yfilter != YFilter.not_set):
                leaf_name_data.append(self.developerloglevel.get_name_leafdata())
            if (self.snmploglevel.is_set or self.snmploglevel.yfilter != YFilter.not_set):
                leaf_name_data.append(self.snmploglevel.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "auditLog"):
                if (self.auditlog is None):
                    self.auditlog = Confdconfig.Logs.Auditlog()
                    self.auditlog.parent = self
                    self._children_name_map["auditlog"] = "auditLog"
                return self.auditlog

            if (child_yang_name == "confdLog"):
                if (self.confdlog is None):
                    self.confdlog = Confdconfig.Logs.Confdlog()
                    self.confdlog.parent = self
                    self._children_name_map["confdlog"] = "confdLog"
                return self.confdlog

            if (child_yang_name == "developerLog"):
                if (self.developerlog is None):
                    self.developerlog = Confdconfig.Logs.Developerlog()
                    self.developerlog.parent = self
                    self._children_name_map["developerlog"] = "developerLog"
                return self.developerlog

            if (child_yang_name == "errorLog"):
                if (self.errorlog is None):
                    self.errorlog = Confdconfig.Logs.Errorlog()
                    self.errorlog.parent = self
                    self._children_name_map["errorlog"] = "errorLog"
                return self.errorlog

            if (child_yang_name == "netconfLog"):
                if (self.netconflog is None):
                    self.netconflog = Confdconfig.Logs.Netconflog()
                    self.netconflog.parent = self
                    self._children_name_map["netconflog"] = "netconfLog"
                return self.netconflog

            if (child_yang_name == "netconfTraceLog"):
                if (self.netconftracelog is None):
                    self.netconftracelog = Confdconfig.Logs.Netconftracelog()
                    self.netconftracelog.parent = self
                    self._children_name_map["netconftracelog"] = "netconfTraceLog"
                return self.netconftracelog

            if (child_yang_name == "snmpLog"):
                if (self.snmplog is None):
                    self.snmplog = Confdconfig.Logs.Snmplog()
                    self.snmplog.parent = self
                    self._children_name_map["snmplog"] = "snmpLog"
                return self.snmplog

            if (child_yang_name == "syslogConfig"):
                if (self.syslogconfig is None):
                    self.syslogconfig = Confdconfig.Logs.Syslogconfig()
                    self.syslogconfig.parent = self
                    self._children_name_map["syslogconfig"] = "syslogConfig"
                return self.syslogconfig

            if (child_yang_name == "webuiAccessLog"):
                if (self.webuiaccesslog is None):
                    self.webuiaccesslog = Confdconfig.Logs.Webuiaccesslog()
                    self.webuiaccesslog.parent = self
                    self._children_name_map["webuiaccesslog"] = "webuiAccessLog"
                return self.webuiaccesslog

            if (child_yang_name == "webuiBrowserLog"):
                if (self.webuibrowserlog is None):
                    self.webuibrowserlog = Confdconfig.Logs.Webuibrowserlog()
                    self.webuibrowserlog.parent = self
                    self._children_name_map["webuibrowserlog"] = "webuiBrowserLog"
                return self.webuibrowserlog

            if (child_yang_name == "xpathTraceLog"):
                if (self.xpathtracelog is None):
                    self.xpathtracelog = Confdconfig.Logs.Xpathtracelog()
                    self.xpathtracelog.parent = self
                    self._children_name_map["xpathtracelog"] = "xpathTraceLog"
                return self.xpathtracelog

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "auditLog" or name == "confdLog" or name == "developerLog" or name == "errorLog" or name == "netconfLog" or name == "netconfTraceLog" or name == "snmpLog" or name == "syslogConfig" or name == "webuiAccessLog" or name == "webuiBrowserLog" or name == "xpathTraceLog" or name == "auditLogCommit" or name == "developerLogLevel" or name == "snmpLogLevel"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "auditLogCommit"):
                self.auditlogcommit = value
                self.auditlogcommit.value_namespace = name_space
                self.auditlogcommit.value_namespace_prefix = name_space_prefix
            if(value_path == "developerLogLevel"):
                self.developerloglevel = value
                self.developerloglevel.value_namespace = name_space
                self.developerloglevel.value_namespace_prefix = name_space_prefix
            if(value_path == "snmpLogLevel"):
                self.snmploglevel = value
                self.snmploglevel.value_namespace = name_space
                self.snmploglevel.value_namespace_prefix = name_space_prefix


    class Sessionlimits(Entity):
        """
        
        
        .. attribute:: configsessionlimit
        
        	
        	**type**\: list of    :py:class:`Configsessionlimit <ydk.models.confd_dyncfg.Confdconfig.Sessionlimits.Configsessionlimit>`
        
        .. attribute:: maxconfigsessions
        
        	
        	**type**\: one of the below types:
        
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**default value**\: unbounded
        
        
        ----
        	**type**\:   :py:class:`Unboundedtype <ydk.models.confd_dyncfg.Unboundedtype>`
        
        	**default value**\: unbounded
        
        
        ----
        .. attribute:: maxsessions
        
        	
        	**type**\: one of the below types:
        
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**default value**\: unbounded
        
        
        ----
        	**type**\:   :py:class:`Unboundedtype <ydk.models.confd_dyncfg.Unboundedtype>`
        
        	**default value**\: unbounded
        
        
        ----
        .. attribute:: sessionlimit
        
        	
        	**type**\: list of    :py:class:`Sessionlimit <ydk.models.confd_dyncfg.Confdconfig.Sessionlimits.Sessionlimit>`
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'confd_dyncfg'
        _revision = '2017-01-16'

        def __init__(self):
            super(Confdconfig.Sessionlimits, self).__init__()

            self.yang_name = "sessionLimits"
            self.yang_parent_name = "confdConfig"
            self.is_presence_container = True

            self.maxconfigsessions = YLeaf(YType.str, "maxConfigSessions")

            self.maxsessions = YLeaf(YType.str, "maxSessions")

            self.configsessionlimit = YList(self)
            self.sessionlimit = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("maxconfigsessions",
                            "maxsessions") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Confdconfig.Sessionlimits, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Confdconfig.Sessionlimits, self).__setattr__(name, value)


        class Sessionlimit(Entity):
            """
            
            
            .. attribute:: context  <key>
            
            	
            	**type**\:  str
            
            .. attribute:: maxsessions
            
            	
            	**type**\: one of the below types:
            
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**mandatory**\: True
            
            
            ----
            	**type**\:   :py:class:`Unboundedtype <ydk.models.confd_dyncfg.Unboundedtype>`
            
            	**mandatory**\: True
            
            
            ----
            

            """

            _prefix = 'confd_dyncfg'
            _revision = '2017-01-16'

            def __init__(self):
                super(Confdconfig.Sessionlimits.Sessionlimit, self).__init__()

                self.yang_name = "sessionLimit"
                self.yang_parent_name = "sessionLimits"

                self.context = YLeaf(YType.str, "context")

                self.maxsessions = YLeaf(YType.str, "maxSessions")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("context",
                                "maxsessions") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Confdconfig.Sessionlimits.Sessionlimit, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Confdconfig.Sessionlimits.Sessionlimit, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.context.is_set or
                    self.maxsessions.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.context.yfilter != YFilter.not_set or
                    self.maxsessions.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "sessionLimit" + "[context='" + self.context.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "confd_dyncfg:confdConfig/sessionLimits/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.context.is_set or self.context.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.context.get_name_leafdata())
                if (self.maxsessions.is_set or self.maxsessions.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.maxsessions.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "context" or name == "maxSessions"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "context"):
                    self.context = value
                    self.context.value_namespace = name_space
                    self.context.value_namespace_prefix = name_space_prefix
                if(value_path == "maxSessions"):
                    self.maxsessions = value
                    self.maxsessions.value_namespace = name_space
                    self.maxsessions.value_namespace_prefix = name_space_prefix


        class Configsessionlimit(Entity):
            """
            
            
            .. attribute:: context  <key>
            
            	
            	**type**\:  str
            
            .. attribute:: maxsessions
            
            	
            	**type**\: one of the below types:
            
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**mandatory**\: True
            
            
            ----
            	**type**\:   :py:class:`Unboundedtype <ydk.models.confd_dyncfg.Unboundedtype>`
            
            	**mandatory**\: True
            
            
            ----
            

            """

            _prefix = 'confd_dyncfg'
            _revision = '2017-01-16'

            def __init__(self):
                super(Confdconfig.Sessionlimits.Configsessionlimit, self).__init__()

                self.yang_name = "configSessionLimit"
                self.yang_parent_name = "sessionLimits"

                self.context = YLeaf(YType.str, "context")

                self.maxsessions = YLeaf(YType.str, "maxSessions")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("context",
                                "maxsessions") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Confdconfig.Sessionlimits.Configsessionlimit, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Confdconfig.Sessionlimits.Configsessionlimit, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.context.is_set or
                    self.maxsessions.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.context.yfilter != YFilter.not_set or
                    self.maxsessions.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "configSessionLimit" + "[context='" + self.context.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "confd_dyncfg:confdConfig/sessionLimits/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.context.is_set or self.context.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.context.get_name_leafdata())
                if (self.maxsessions.is_set or self.maxsessions.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.maxsessions.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "context" or name == "maxSessions"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "context"):
                    self.context = value
                    self.context.value_namespace = name_space
                    self.context.value_namespace_prefix = name_space_prefix
                if(value_path == "maxSessions"):
                    self.maxsessions = value
                    self.maxsessions.value_namespace = name_space
                    self.maxsessions.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.configsessionlimit:
                if (c.has_data()):
                    return True
            for c in self.sessionlimit:
                if (c.has_data()):
                    return True
            return (
                self.maxconfigsessions.is_set or
                self.maxsessions.is_set)

        def has_operation(self):
            for c in self.configsessionlimit:
                if (c.has_operation()):
                    return True
            for c in self.sessionlimit:
                if (c.has_operation()):
                    return True
            return (
                self.yfilter != YFilter.not_set or
                self.maxconfigsessions.yfilter != YFilter.not_set or
                self.maxsessions.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "sessionLimits" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "confd_dyncfg:confdConfig/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.maxconfigsessions.is_set or self.maxconfigsessions.yfilter != YFilter.not_set):
                leaf_name_data.append(self.maxconfigsessions.get_name_leafdata())
            if (self.maxsessions.is_set or self.maxsessions.yfilter != YFilter.not_set):
                leaf_name_data.append(self.maxsessions.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "configSessionLimit"):
                for c in self.configsessionlimit:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Confdconfig.Sessionlimits.Configsessionlimit()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.configsessionlimit.append(c)
                return c

            if (child_yang_name == "sessionLimit"):
                for c in self.sessionlimit:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Confdconfig.Sessionlimits.Sessionlimit()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.sessionlimit.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "configSessionLimit" or name == "sessionLimit" or name == "maxConfigSessions" or name == "maxSessions"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "maxConfigSessions"):
                self.maxconfigsessions = value
                self.maxconfigsessions.value_namespace = name_space
                self.maxconfigsessions.value_namespace_prefix = name_space_prefix
            if(value_path == "maxSessions"):
                self.maxsessions = value
                self.maxsessions.value_namespace = name_space
                self.maxsessions.value_namespace_prefix = name_space_prefix


    class Aaa(Entity):
        """
        
        
        .. attribute:: auditusername
        
        	
        	**type**\:   :py:class:`Auditusernametype <ydk.models.confd_dyncfg.Auditusernametype>`
        
        	**default value**\: always
        
        .. attribute:: authenticationcallback
        
        	
        	**type**\:   :py:class:`Authenticationcallback <ydk.models.confd_dyncfg.Confdconfig.Aaa.Authenticationcallback>`
        
        	**presence node**\: True
        
        .. attribute:: authorder
        
        	
        	**type**\:  str
        
        .. attribute:: authorization
        
        	
        	**type**\:   :py:class:`Authorization <ydk.models.confd_dyncfg.Confdconfig.Aaa.Authorization>`
        
        	**presence node**\: True
        
        .. attribute:: defaultgroup
        
        	
        	**type**\:  str
        
        .. attribute:: expirationwarning
        
        	
        	**type**\:   :py:class:`Expirationwarningtype <ydk.models.confd_dyncfg.Expirationwarningtype>`
        
        	**default value**\: ignore
        
        .. attribute:: externalauthentication
        
        	
        	**type**\:   :py:class:`Externalauthentication <ydk.models.confd_dyncfg.Confdconfig.Aaa.Externalauthentication>`
        
        	**presence node**\: True
        
        .. attribute:: localauthentication
        
        	
        	**type**\:   :py:class:`Localauthentication <ydk.models.confd_dyncfg.Confdconfig.Aaa.Localauthentication>`
        
        	**presence node**\: True
        
        .. attribute:: pam
        
        	
        	**type**\:   :py:class:`Pam <ydk.models.confd_dyncfg.Confdconfig.Aaa.Pam>`
        
        	**presence node**\: True
        
        .. attribute:: sshlogingracetime
        
        	
        	**type**\:  str
        
        	**default value**\: PT10M
        
        .. attribute:: sshmaxauthtries
        
        	
        	**type**\: one of the below types:
        
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**default value**\: unbounded
        
        
        ----
        	**type**\:   :py:class:`Unboundedtype <ydk.models.confd_dyncfg.Unboundedtype>`
        
        	**default value**\: unbounded
        
        
        ----
        .. attribute:: sshpubkeyauthentication
        
        	
        	**type**\:   :py:class:`Pubkeyauthenticationtype <ydk.models.confd_dyncfg.Pubkeyauthenticationtype>`
        
        	**default value**\: system
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'confd_dyncfg'
        _revision = '2017-01-16'

        def __init__(self):
            super(Confdconfig.Aaa, self).__init__()

            self.yang_name = "aaa"
            self.yang_parent_name = "confdConfig"
            self.is_presence_container = True

            self.auditusername = YLeaf(YType.enumeration, "auditUserName")

            self.authorder = YLeaf(YType.str, "authOrder")

            self.defaultgroup = YLeaf(YType.str, "defaultGroup")

            self.expirationwarning = YLeaf(YType.enumeration, "expirationWarning")

            self.sshlogingracetime = YLeaf(YType.str, "sshLoginGraceTime")

            self.sshmaxauthtries = YLeaf(YType.str, "sshMaxAuthTries")

            self.sshpubkeyauthentication = YLeaf(YType.enumeration, "sshPubkeyAuthentication")

            self.authenticationcallback = None
            self._children_name_map["authenticationcallback"] = "authenticationCallback"
            self._children_yang_names.add("authenticationCallback")

            self.authorization = None
            self._children_name_map["authorization"] = "authorization"
            self._children_yang_names.add("authorization")

            self.externalauthentication = None
            self._children_name_map["externalauthentication"] = "externalAuthentication"
            self._children_yang_names.add("externalAuthentication")

            self.localauthentication = None
            self._children_name_map["localauthentication"] = "localAuthentication"
            self._children_yang_names.add("localAuthentication")

            self.pam = None
            self._children_name_map["pam"] = "pam"
            self._children_yang_names.add("pam")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("auditusername",
                            "authorder",
                            "defaultgroup",
                            "expirationwarning",
                            "sshlogingracetime",
                            "sshmaxauthtries",
                            "sshpubkeyauthentication") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Confdconfig.Aaa, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Confdconfig.Aaa, self).__setattr__(name, value)


        class Pam(Entity):
            """
            
            
            .. attribute:: enabled
            
            	
            	**type**\:  bool
            
            	**default value**\: false
            
            .. attribute:: service
            
            	
            	**type**\:  str
            
            	**default value**\: common-auth
            
            .. attribute:: timeout
            
            	
            	**type**\:  str
            
            	**default value**\: PT10S
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'confd_dyncfg'
            _revision = '2017-01-16'

            def __init__(self):
                super(Confdconfig.Aaa.Pam, self).__init__()

                self.yang_name = "pam"
                self.yang_parent_name = "aaa"
                self.is_presence_container = True

                self.enabled = YLeaf(YType.boolean, "enabled")

                self.service = YLeaf(YType.str, "service")

                self.timeout = YLeaf(YType.str, "timeout")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("enabled",
                                "service",
                                "timeout") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Confdconfig.Aaa.Pam, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Confdconfig.Aaa.Pam, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.enabled.is_set or
                    self.service.is_set or
                    self.timeout.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.enabled.yfilter != YFilter.not_set or
                    self.service.yfilter != YFilter.not_set or
                    self.timeout.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "pam" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "confd_dyncfg:confdConfig/aaa/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.enabled.is_set or self.enabled.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.enabled.get_name_leafdata())
                if (self.service.is_set or self.service.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.service.get_name_leafdata())
                if (self.timeout.is_set or self.timeout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.timeout.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "enabled" or name == "service" or name == "timeout"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "enabled"):
                    self.enabled = value
                    self.enabled.value_namespace = name_space
                    self.enabled.value_namespace_prefix = name_space_prefix
                if(value_path == "service"):
                    self.service = value
                    self.service.value_namespace = name_space
                    self.service.value_namespace_prefix = name_space_prefix
                if(value_path == "timeout"):
                    self.timeout = value
                    self.timeout.value_namespace = name_space
                    self.timeout.value_namespace_prefix = name_space_prefix


        class Externalauthentication(Entity):
            """
            
            
            .. attribute:: enabled
            
            	
            	**type**\:  bool
            
            	**default value**\: false
            
            .. attribute:: executable
            
            	
            	**type**\:  str
            
            .. attribute:: includeextra
            
            	
            	**type**\:  bool
            
            	**default value**\: false
            
            .. attribute:: usebase64
            
            	
            	**type**\:  bool
            
            	**default value**\: false
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'confd_dyncfg'
            _revision = '2017-01-16'

            def __init__(self):
                super(Confdconfig.Aaa.Externalauthentication, self).__init__()

                self.yang_name = "externalAuthentication"
                self.yang_parent_name = "aaa"
                self.is_presence_container = True

                self.enabled = YLeaf(YType.boolean, "enabled")

                self.executable = YLeaf(YType.str, "executable")

                self.includeextra = YLeaf(YType.boolean, "includeExtra")

                self.usebase64 = YLeaf(YType.boolean, "useBase64")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("enabled",
                                "executable",
                                "includeextra",
                                "usebase64") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Confdconfig.Aaa.Externalauthentication, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Confdconfig.Aaa.Externalauthentication, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.enabled.is_set or
                    self.executable.is_set or
                    self.includeextra.is_set or
                    self.usebase64.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.enabled.yfilter != YFilter.not_set or
                    self.executable.yfilter != YFilter.not_set or
                    self.includeextra.yfilter != YFilter.not_set or
                    self.usebase64.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "externalAuthentication" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "confd_dyncfg:confdConfig/aaa/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.enabled.is_set or self.enabled.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.enabled.get_name_leafdata())
                if (self.executable.is_set or self.executable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.executable.get_name_leafdata())
                if (self.includeextra.is_set or self.includeextra.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.includeextra.get_name_leafdata())
                if (self.usebase64.is_set or self.usebase64.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.usebase64.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "enabled" or name == "executable" or name == "includeExtra" or name == "useBase64"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "enabled"):
                    self.enabled = value
                    self.enabled.value_namespace = name_space
                    self.enabled.value_namespace_prefix = name_space_prefix
                if(value_path == "executable"):
                    self.executable = value
                    self.executable.value_namespace = name_space
                    self.executable.value_namespace_prefix = name_space_prefix
                if(value_path == "includeExtra"):
                    self.includeextra = value
                    self.includeextra.value_namespace = name_space
                    self.includeextra.value_namespace_prefix = name_space_prefix
                if(value_path == "useBase64"):
                    self.usebase64 = value
                    self.usebase64.value_namespace = name_space
                    self.usebase64.value_namespace_prefix = name_space_prefix


        class Localauthentication(Entity):
            """
            
            
            .. attribute:: enabled
            
            	
            	**type**\:  bool
            
            	**default value**\: true
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'confd_dyncfg'
            _revision = '2017-01-16'

            def __init__(self):
                super(Confdconfig.Aaa.Localauthentication, self).__init__()

                self.yang_name = "localAuthentication"
                self.yang_parent_name = "aaa"
                self.is_presence_container = True

                self.enabled = YLeaf(YType.boolean, "enabled")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("enabled") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Confdconfig.Aaa.Localauthentication, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Confdconfig.Aaa.Localauthentication, self).__setattr__(name, value)

            def has_data(self):
                return self.enabled.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.enabled.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "localAuthentication" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "confd_dyncfg:confdConfig/aaa/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.enabled.is_set or self.enabled.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.enabled.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "enabled"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "enabled"):
                    self.enabled = value
                    self.enabled.value_namespace = name_space
                    self.enabled.value_namespace_prefix = name_space_prefix


        class Authenticationcallback(Entity):
            """
            
            
            .. attribute:: enabled
            
            	
            	**type**\:  bool
            
            	**default value**\: false
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'confd_dyncfg'
            _revision = '2017-01-16'

            def __init__(self):
                super(Confdconfig.Aaa.Authenticationcallback, self).__init__()

                self.yang_name = "authenticationCallback"
                self.yang_parent_name = "aaa"
                self.is_presence_container = True

                self.enabled = YLeaf(YType.boolean, "enabled")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("enabled") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Confdconfig.Aaa.Authenticationcallback, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Confdconfig.Aaa.Authenticationcallback, self).__setattr__(name, value)

            def has_data(self):
                return self.enabled.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.enabled.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "authenticationCallback" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "confd_dyncfg:confdConfig/aaa/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.enabled.is_set or self.enabled.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.enabled.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "enabled"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "enabled"):
                    self.enabled = value
                    self.enabled.value_namespace = name_space
                    self.enabled.value_namespace_prefix = name_space_prefix


        class Authorization(Entity):
            """
            
            
            .. attribute:: callback
            
            	
            	**type**\:   :py:class:`Callback <ydk.models.confd_dyncfg.Confdconfig.Aaa.Authorization.Callback>`
            
            	**presence node**\: True
            
            .. attribute:: enabled
            
            	
            	**type**\:  bool
            
            	**default value**\: true
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'confd_dyncfg'
            _revision = '2017-01-16'

            def __init__(self):
                super(Confdconfig.Aaa.Authorization, self).__init__()

                self.yang_name = "authorization"
                self.yang_parent_name = "aaa"
                self.is_presence_container = True

                self.enabled = YLeaf(YType.boolean, "enabled")

                self.callback = None
                self._children_name_map["callback"] = "callback"
                self._children_yang_names.add("callback")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("enabled") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Confdconfig.Aaa.Authorization, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Confdconfig.Aaa.Authorization, self).__setattr__(name, value)


            class Callback(Entity):
                """
                
                
                .. attribute:: enabled
                
                	
                	**type**\:  bool
                
                	**default value**\: false
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'confd_dyncfg'
                _revision = '2017-01-16'

                def __init__(self):
                    super(Confdconfig.Aaa.Authorization.Callback, self).__init__()

                    self.yang_name = "callback"
                    self.yang_parent_name = "authorization"
                    self.is_presence_container = True

                    self.enabled = YLeaf(YType.boolean, "enabled")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("enabled") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Confdconfig.Aaa.Authorization.Callback, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Confdconfig.Aaa.Authorization.Callback, self).__setattr__(name, value)

                def has_data(self):
                    return self.enabled.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.enabled.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "callback" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "confd_dyncfg:confdConfig/aaa/authorization/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.enabled.is_set or self.enabled.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.enabled.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "enabled"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "enabled"):
                        self.enabled = value
                        self.enabled.value_namespace = name_space
                        self.enabled.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.enabled.is_set or
                    (self.callback is not None))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.enabled.yfilter != YFilter.not_set or
                    (self.callback is not None and self.callback.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "authorization" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "confd_dyncfg:confdConfig/aaa/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.enabled.is_set or self.enabled.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.enabled.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "callback"):
                    if (self.callback is None):
                        self.callback = Confdconfig.Aaa.Authorization.Callback()
                        self.callback.parent = self
                        self._children_name_map["callback"] = "callback"
                    return self.callback

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "callback" or name == "enabled"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "enabled"):
                    self.enabled = value
                    self.enabled.value_namespace = name_space
                    self.enabled.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (
                self.auditusername.is_set or
                self.authorder.is_set or
                self.defaultgroup.is_set or
                self.expirationwarning.is_set or
                self.sshlogingracetime.is_set or
                self.sshmaxauthtries.is_set or
                self.sshpubkeyauthentication.is_set or
                (self.authenticationcallback is not None) or
                (self.authorization is not None) or
                (self.externalauthentication is not None) or
                (self.localauthentication is not None) or
                (self.pam is not None))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.auditusername.yfilter != YFilter.not_set or
                self.authorder.yfilter != YFilter.not_set or
                self.defaultgroup.yfilter != YFilter.not_set or
                self.expirationwarning.yfilter != YFilter.not_set or
                self.sshlogingracetime.yfilter != YFilter.not_set or
                self.sshmaxauthtries.yfilter != YFilter.not_set or
                self.sshpubkeyauthentication.yfilter != YFilter.not_set or
                (self.authenticationcallback is not None and self.authenticationcallback.has_operation()) or
                (self.authorization is not None and self.authorization.has_operation()) or
                (self.externalauthentication is not None and self.externalauthentication.has_operation()) or
                (self.localauthentication is not None and self.localauthentication.has_operation()) or
                (self.pam is not None and self.pam.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "aaa" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "confd_dyncfg:confdConfig/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.auditusername.is_set or self.auditusername.yfilter != YFilter.not_set):
                leaf_name_data.append(self.auditusername.get_name_leafdata())
            if (self.authorder.is_set or self.authorder.yfilter != YFilter.not_set):
                leaf_name_data.append(self.authorder.get_name_leafdata())
            if (self.defaultgroup.is_set or self.defaultgroup.yfilter != YFilter.not_set):
                leaf_name_data.append(self.defaultgroup.get_name_leafdata())
            if (self.expirationwarning.is_set or self.expirationwarning.yfilter != YFilter.not_set):
                leaf_name_data.append(self.expirationwarning.get_name_leafdata())
            if (self.sshlogingracetime.is_set or self.sshlogingracetime.yfilter != YFilter.not_set):
                leaf_name_data.append(self.sshlogingracetime.get_name_leafdata())
            if (self.sshmaxauthtries.is_set or self.sshmaxauthtries.yfilter != YFilter.not_set):
                leaf_name_data.append(self.sshmaxauthtries.get_name_leafdata())
            if (self.sshpubkeyauthentication.is_set or self.sshpubkeyauthentication.yfilter != YFilter.not_set):
                leaf_name_data.append(self.sshpubkeyauthentication.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "authenticationCallback"):
                if (self.authenticationcallback is None):
                    self.authenticationcallback = Confdconfig.Aaa.Authenticationcallback()
                    self.authenticationcallback.parent = self
                    self._children_name_map["authenticationcallback"] = "authenticationCallback"
                return self.authenticationcallback

            if (child_yang_name == "authorization"):
                if (self.authorization is None):
                    self.authorization = Confdconfig.Aaa.Authorization()
                    self.authorization.parent = self
                    self._children_name_map["authorization"] = "authorization"
                return self.authorization

            if (child_yang_name == "externalAuthentication"):
                if (self.externalauthentication is None):
                    self.externalauthentication = Confdconfig.Aaa.Externalauthentication()
                    self.externalauthentication.parent = self
                    self._children_name_map["externalauthentication"] = "externalAuthentication"
                return self.externalauthentication

            if (child_yang_name == "localAuthentication"):
                if (self.localauthentication is None):
                    self.localauthentication = Confdconfig.Aaa.Localauthentication()
                    self.localauthentication.parent = self
                    self._children_name_map["localauthentication"] = "localAuthentication"
                return self.localauthentication

            if (child_yang_name == "pam"):
                if (self.pam is None):
                    self.pam = Confdconfig.Aaa.Pam()
                    self.pam.parent = self
                    self._children_name_map["pam"] = "pam"
                return self.pam

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "authenticationCallback" or name == "authorization" or name == "externalAuthentication" or name == "localAuthentication" or name == "pam" or name == "auditUserName" or name == "authOrder" or name == "defaultGroup" or name == "expirationWarning" or name == "sshLoginGraceTime" or name == "sshMaxAuthTries" or name == "sshPubkeyAuthentication"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "auditUserName"):
                self.auditusername = value
                self.auditusername.value_namespace = name_space
                self.auditusername.value_namespace_prefix = name_space_prefix
            if(value_path == "authOrder"):
                self.authorder = value
                self.authorder.value_namespace = name_space
                self.authorder.value_namespace_prefix = name_space_prefix
            if(value_path == "defaultGroup"):
                self.defaultgroup = value
                self.defaultgroup.value_namespace = name_space
                self.defaultgroup.value_namespace_prefix = name_space_prefix
            if(value_path == "expirationWarning"):
                self.expirationwarning = value
                self.expirationwarning.value_namespace = name_space
                self.expirationwarning.value_namespace_prefix = name_space_prefix
            if(value_path == "sshLoginGraceTime"):
                self.sshlogingracetime = value
                self.sshlogingracetime.value_namespace = name_space
                self.sshlogingracetime.value_namespace_prefix = name_space_prefix
            if(value_path == "sshMaxAuthTries"):
                self.sshmaxauthtries = value
                self.sshmaxauthtries.value_namespace = name_space
                self.sshmaxauthtries.value_namespace_prefix = name_space_prefix
            if(value_path == "sshPubkeyAuthentication"):
                self.sshpubkeyauthentication = value
                self.sshpubkeyauthentication.value_namespace = name_space
                self.sshpubkeyauthentication.value_namespace_prefix = name_space_prefix


    class Ssh(Entity):
        """
        
        
        .. attribute:: algorithms
        
        	
        	**type**\:   :py:class:`Algorithms <ydk.models.confd_dyncfg.Confdconfig.Ssh.Algorithms>`
        
        	**presence node**\: True
        
        .. attribute:: clientalivecountmax
        
        	
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**default value**\: 3
        
        .. attribute:: clientaliveinterval
        
        	
        	**type**\: one of the below types:
        
        	**type**\:  str
        
        	**default value**\: infinity
        
        
        ----
        	**type**\:   :py:class:`Infinitytype <ydk.models.confd_dyncfg.Infinitytype>`
        
        	**default value**\: infinity
        
        
        ----
        .. attribute:: idleconnectiontimeout
        
        	
        	**type**\:  str
        
        	**default value**\: PT10M
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'confd_dyncfg'
        _revision = '2017-01-16'

        def __init__(self):
            super(Confdconfig.Ssh, self).__init__()

            self.yang_name = "ssh"
            self.yang_parent_name = "confdConfig"
            self.is_presence_container = True

            self.clientalivecountmax = YLeaf(YType.uint32, "clientAliveCountMax")

            self.clientaliveinterval = YLeaf(YType.str, "clientAliveInterval")

            self.idleconnectiontimeout = YLeaf(YType.str, "idleConnectionTimeout")

            self.algorithms = None
            self._children_name_map["algorithms"] = "algorithms"
            self._children_yang_names.add("algorithms")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("clientalivecountmax",
                            "clientaliveinterval",
                            "idleconnectiontimeout") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Confdconfig.Ssh, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Confdconfig.Ssh, self).__setattr__(name, value)


        class Algorithms(Entity):
            """
            
            
            .. attribute:: dhgroup
            
            	
            	**type**\:   :py:class:`Dhgroup <ydk.models.confd_dyncfg.Confdconfig.Ssh.Algorithms.Dhgroup>`
            
            	**presence node**\: True
            
            .. attribute:: encryption
            
            	
            	**type**\:  str
            
            .. attribute:: kex
            
            	
            	**type**\:  str
            
            .. attribute:: mac
            
            	
            	**type**\:  str
            
            .. attribute:: serverhostkey
            
            	
            	**type**\:  str
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'confd_dyncfg'
            _revision = '2017-01-16'

            def __init__(self):
                super(Confdconfig.Ssh.Algorithms, self).__init__()

                self.yang_name = "algorithms"
                self.yang_parent_name = "ssh"
                self.is_presence_container = True

                self.encryption = YLeaf(YType.str, "encryption")

                self.kex = YLeaf(YType.str, "kex")

                self.mac = YLeaf(YType.str, "mac")

                self.serverhostkey = YLeaf(YType.str, "serverHostKey")

                self.dhgroup = None
                self._children_name_map["dhgroup"] = "dhGroup"
                self._children_yang_names.add("dhGroup")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("encryption",
                                "kex",
                                "mac",
                                "serverhostkey") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Confdconfig.Ssh.Algorithms, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Confdconfig.Ssh.Algorithms, self).__setattr__(name, value)


            class Dhgroup(Entity):
                """
                
                
                .. attribute:: maxsize
                
                	
                	**type**\:  int
                
                	**range:** 1024..8192
                
                	**default value**\: 4096
                
                .. attribute:: minsize
                
                	
                	**type**\:  int
                
                	**range:** 1024..8192
                
                	**default value**\: 2048
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'confd_dyncfg'
                _revision = '2017-01-16'

                def __init__(self):
                    super(Confdconfig.Ssh.Algorithms.Dhgroup, self).__init__()

                    self.yang_name = "dhGroup"
                    self.yang_parent_name = "algorithms"
                    self.is_presence_container = True

                    self.maxsize = YLeaf(YType.uint32, "maxSize")

                    self.minsize = YLeaf(YType.uint32, "minSize")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("maxsize",
                                    "minsize") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Confdconfig.Ssh.Algorithms.Dhgroup, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Confdconfig.Ssh.Algorithms.Dhgroup, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.maxsize.is_set or
                        self.minsize.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.maxsize.yfilter != YFilter.not_set or
                        self.minsize.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "dhGroup" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "confd_dyncfg:confdConfig/ssh/algorithms/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.maxsize.is_set or self.maxsize.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.maxsize.get_name_leafdata())
                    if (self.minsize.is_set or self.minsize.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.minsize.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "maxSize" or name == "minSize"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "maxSize"):
                        self.maxsize = value
                        self.maxsize.value_namespace = name_space
                        self.maxsize.value_namespace_prefix = name_space_prefix
                    if(value_path == "minSize"):
                        self.minsize = value
                        self.minsize.value_namespace = name_space
                        self.minsize.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.encryption.is_set or
                    self.kex.is_set or
                    self.mac.is_set or
                    self.serverhostkey.is_set or
                    (self.dhgroup is not None))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.encryption.yfilter != YFilter.not_set or
                    self.kex.yfilter != YFilter.not_set or
                    self.mac.yfilter != YFilter.not_set or
                    self.serverhostkey.yfilter != YFilter.not_set or
                    (self.dhgroup is not None and self.dhgroup.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "algorithms" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "confd_dyncfg:confdConfig/ssh/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.encryption.is_set or self.encryption.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.encryption.get_name_leafdata())
                if (self.kex.is_set or self.kex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.kex.get_name_leafdata())
                if (self.mac.is_set or self.mac.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mac.get_name_leafdata())
                if (self.serverhostkey.is_set or self.serverhostkey.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.serverhostkey.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "dhGroup"):
                    if (self.dhgroup is None):
                        self.dhgroup = Confdconfig.Ssh.Algorithms.Dhgroup()
                        self.dhgroup.parent = self
                        self._children_name_map["dhgroup"] = "dhGroup"
                    return self.dhgroup

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "dhGroup" or name == "encryption" or name == "kex" or name == "mac" or name == "serverHostKey"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "encryption"):
                    self.encryption = value
                    self.encryption.value_namespace = name_space
                    self.encryption.value_namespace_prefix = name_space_prefix
                if(value_path == "kex"):
                    self.kex = value
                    self.kex.value_namespace = name_space
                    self.kex.value_namespace_prefix = name_space_prefix
                if(value_path == "mac"):
                    self.mac = value
                    self.mac.value_namespace = name_space
                    self.mac.value_namespace_prefix = name_space_prefix
                if(value_path == "serverHostKey"):
                    self.serverhostkey = value
                    self.serverhostkey.value_namespace = name_space
                    self.serverhostkey.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (
                self.clientalivecountmax.is_set or
                self.clientaliveinterval.is_set or
                self.idleconnectiontimeout.is_set or
                (self.algorithms is not None))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.clientalivecountmax.yfilter != YFilter.not_set or
                self.clientaliveinterval.yfilter != YFilter.not_set or
                self.idleconnectiontimeout.yfilter != YFilter.not_set or
                (self.algorithms is not None and self.algorithms.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ssh" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "confd_dyncfg:confdConfig/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.clientalivecountmax.is_set or self.clientalivecountmax.yfilter != YFilter.not_set):
                leaf_name_data.append(self.clientalivecountmax.get_name_leafdata())
            if (self.clientaliveinterval.is_set or self.clientaliveinterval.yfilter != YFilter.not_set):
                leaf_name_data.append(self.clientaliveinterval.get_name_leafdata())
            if (self.idleconnectiontimeout.is_set or self.idleconnectiontimeout.yfilter != YFilter.not_set):
                leaf_name_data.append(self.idleconnectiontimeout.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "algorithms"):
                if (self.algorithms is None):
                    self.algorithms = Confdconfig.Ssh.Algorithms()
                    self.algorithms.parent = self
                    self._children_name_map["algorithms"] = "algorithms"
                return self.algorithms

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "algorithms" or name == "clientAliveCountMax" or name == "clientAliveInterval" or name == "idleConnectionTimeout"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "clientAliveCountMax"):
                self.clientalivecountmax = value
                self.clientalivecountmax.value_namespace = name_space
                self.clientalivecountmax.value_namespace_prefix = name_space_prefix
            if(value_path == "clientAliveInterval"):
                self.clientaliveinterval = value
                self.clientaliveinterval.value_namespace = name_space
                self.clientaliveinterval.value_namespace_prefix = name_space_prefix
            if(value_path == "idleConnectionTimeout"):
                self.idleconnectiontimeout = value
                self.idleconnectiontimeout.value_namespace = name_space
                self.idleconnectiontimeout.value_namespace_prefix = name_space_prefix


    class Cli(Entity):
        """
        
        
        .. attribute:: adderrorprefixsuffix
        
        	
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: addextratablespacing
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: allornothingload
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: allowabbrevcmds
        
        	
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: allowabbrevcmdsonload
        
        	
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: allowabbrevenums
        
        	
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: allowabbrevkeys
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: allowabbrevparamnames
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: allowallaswildcard
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: allowcaseinsensitiveenums
        
        	
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: allowimplicitwildcard
        
        	
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: allowoldstylemodecmds
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: allowoverwriteoncopy
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: allowparenquotes
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: allowrangeexpression
        
        	
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: allowrangeexpressionalltypes
        
        	
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: allowtablecellwrap
        
        	
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: allowtableoverflow
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: allowwildcard
        
        	
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: asyncpromptrefresh
        
        	
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: auditlogmode
        
        	
        	**type**\:   :py:class:`Cliauditlogtype <ydk.models.confd_dyncfg.Cliauditlogtype>`
        
        	**default value**\: all
        
        .. attribute:: autocommitload
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: autocommitloadchunksize
        
        	
        	**type**\:  int
        
        	**range:** 1..18446744073709551615 \| 1..18446744073709551615
        
        	**default value**\: 1
        
        .. attribute:: autowizard
        
        	
        	**type**\:   :py:class:`Autowizard <ydk.models.confd_dyncfg.Confdconfig.Cli.Autowizard>`
        
        	**presence node**\: True
        
        .. attribute:: banner
        
        	
        	**type**\:  str
        
        .. attribute:: bannerfile
        
        	
        	**type**\:  str
        
        .. attribute:: cabortedprefix
        
        	
        	**type**\:  str
        
        	**default value**\: Aborted: 
        
        .. attribute:: calignleafvalues
        
        	
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: caseinsensitive
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: caseinsensitivekeys
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: cerrorprefix
        
        	
        	**type**\:  str
        
        	**default value**\: Error: 
        
        .. attribute:: cextendedcmdsearch
        
        	
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: chelp
        
        	
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: cmdaaaforautowizard
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: cmodeexitformat
        
        	
        	**type**\:  str
        
        	**default value**\: !
        
        .. attribute:: columnstats
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: commandtimeout
        
        	
        	**type**\: one of the below types:
        
        	**type**\:  str
        
        	**default value**\: infinity
        
        
        ----
        	**type**\:   :py:class:`Infinitytype <ydk.models.confd_dyncfg.Infinitytype>`
        
        	**default value**\: infinity
        
        
        ----
        .. attribute:: commitactivityclock
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: commitmessage
        
        	
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: commitmessageformat
        
        	
        	**type**\:  str
        
        	**default value**\: \nSystem message at $(time)...\nCommit performed by $(user) via $(proto) using $(ctx).\n
        
        .. attribute:: commitretrytimeout
        
        	
        	**type**\: one of the below types:
        
        	**type**\:  str
        
        	**default value**\: PT0S
        
        
        ----
        	**type**\:   :py:class:`Infinitytype <ydk.models.confd_dyncfg.Infinitytype>`
        
        	**default value**\: PT0S
        
        
        ----
        .. attribute:: compactshow
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: compactstatsshow
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: compacttable
        
        	
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: completionlistline
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: completionmetainfo
        
        	
        	**type**\:   :py:class:`Completionmetainfotype <ydk.models.confd_dyncfg.Completionmetainfotype>`
        
        	**default value**\: false
        
        .. attribute:: completionshowmax
        
        	
        	**type**\:  int
        
        	**range:** 5..2147483647
        
        	**default value**\: 100
        
        .. attribute:: completionshowoldval
        
        	
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: complistcompact
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: confirmuncommitedonexit
        
        	
        	**type**\:   :py:class:`Confirmuncommitedonexittype <ydk.models.confd_dyncfg.Confirmuncommitedonexittype>`
        
        	**default value**\: prompt
        
        .. attribute:: continueonerrorcmdstack
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: cprivate
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: cprompt1
        
        	
        	**type**\:  str
        
        	**default value**\: \h\M# 
        
        .. attribute:: cprompt2
        
        	
        	**type**\:  str
        
        	**default value**\: \h(\m)# 
        
        .. attribute:: crestrictiveno
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: csilentno
        
        	
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: cstylepromptinjstyle
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: csuppresscmdsearch
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: ctab
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: ctabinfo
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: cwarningprefix
        
        	
        	**type**\:  str
        
        	**default value**\: Warning: 
        
        .. attribute:: defaultdisplaylevel
        
        	
        	**type**\:  int
        
        	**range:** \-9223372036854775808..9223372036854775807
        
        	**default value**\: 99999999
        
        .. attribute:: defaultprefix
        
        	
        	**type**\:  str
        
        .. attribute:: defaulttablebehavior
        
        	
        	**type**\:   :py:class:`Tablebehaviortype <ydk.models.confd_dyncfg.Tablebehaviortype>`
        
        	**default value**\: dynamic
        
        .. attribute:: dequotehidden
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: disableidletimeoutoncmd
        
        	
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: disablepipe
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: disablepipeconfig
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: displayemptyconfigcontainers
        
        	
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: displaynonpresenceattributes
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: docwrap
        
        	
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: editwrapmode
        
        	
        	**type**\:   :py:class:`Editwrapmodetype <ydk.models.confd_dyncfg.Editwrapmodetype>`
        
        	**default value**\: wrap
        
        .. attribute:: enabled
        
        	
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: enabledisplaygroups
        
        	
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: enabledisplaylevel
        
        	
        	**type**\:   :py:class:`Enabledisplayleveltype <ydk.models.confd_dyncfg.Enabledisplayleveltype>`
        
        	**default value**\: pipe
        
        .. attribute:: enableloadmerge
        
        	
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: entersubmodeonleaf
        
        	
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: enumkeyinfo
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: escapebackslash
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: execnavigationcmds
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: exitconfigmodeonctrlc
        
        	
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: exitmodeonemptyrange
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: expandaliasescape
        
        	
        	**type**\: one of the below types:
        
        	**type**\:   :py:class:`Falsetype <ydk.models.confd_dyncfg.Falsetype>`
        
        	**default value**\: false
        
        
        ----
        	**type**\:  str
        
        	**length:** 1
        
        	**default value**\: false
        
        
        ----
        .. attribute:: expandaliasoncompletion
        
        	
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: explicitsetcreate
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: externalactionerrormsg
        
        	
        	**type**\:  str
        
        .. attribute:: forcedexitformat
        
        	
        	**type**\:  str
        
        	**default value**\: \nYou are forced out of configure mode by $(sender).\n
        
        .. attribute:: hidedotfiles
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: historymaxsize
        
        	
        	**type**\:  int
        
        	**range:** \-9223372036854775808..9223372036854775807
        
        	**default value**\: 1000
        
        .. attribute:: historyremoveduplicates
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: historysave
        
        	
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: idletimeout
        
        	
        	**type**\:  str
        
        	**default value**\: PT30M
        
        .. attribute:: ignoreleadingwhitespace
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: ignoreshowwithdefaultondiff
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: ignoresubsystemfailures
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: inconsistentdatabasesuffix
        
        	
        	**type**\:  str
        
        .. attribute:: indenttemplates
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: infoonmatch
        
        	
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: infoonspace
        
        	
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: infoontab
        
        	
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: inheritpaginate
        
        	
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: instancedescription
        
        	
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: invaliddatastring
        
        	
        	**type**\:  str
        
        	**default value**\: --ERROR--
        
        .. attribute:: jabortedprefix
        
        	
        	**type**\:  str
        
        	**default value**\: Aborted: 
        
        .. attribute:: jalignleafvalues
        
        	
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: jallowdeleteall
        
        	
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: jerrorprefix
        
        	
        	**type**\:  str
        
        	**default value**\: Error: 
        
        .. attribute:: jextendedshow
        
        	
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: jhidehelp
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: jshowcr
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: jshowtablerecursive
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: jshowunset
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: jshowunsettext
        
        	
        	**type**\:  str
        
        	**default value**\: UNSET
        
        .. attribute:: jstatusformat
        
        	
        	**type**\:  str
        
        	**default value**\: [$(status)][$(time)]\n
        
        .. attribute:: jwarningprefix
        
        	
        	**type**\:  str
        
        	**default value**\: Warning: 
        
        .. attribute:: laxbarquoting
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: leafprompting
        
        	
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: loadactivityclock
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: mapactions
        
        	
        	**type**\:   :py:class:`Cliactionmaptype <ydk.models.confd_dyncfg.Cliactionmaptype>`
        
        	**default value**\: both
        
        .. attribute:: matchcompletionsformat
        
        	
        	**type**\:  str
        
        	**default value**\: Possible match completions:
        
        .. attribute:: messageformat
        
        	
        	**type**\:  str
        
        	**default value**\: \nMessage from $(sender) at $(time)...\n$(message)\nEOF\n
        
        .. attribute:: messagemaxsize
        
        	
        	**type**\:  int
        
        	**range:** \-9223372036854775808..9223372036854775807
        
        	**default value**\: 10000
        
        .. attribute:: messagequeuesize
        
        	
        	**type**\:  int
        
        	**range:** \-9223372036854775808..9223372036854775807
        
        	**default value**\: 10
        
        .. attribute:: messagewordwrap
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: mixedmode
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: modeinfoinaaa
        
        	
        	**type**\:   :py:class:`Modeinfoinaaatype <ydk.models.confd_dyncfg.Modeinfoinaaatype>`
        
        	**default value**\: false
        
        .. attribute:: modeinfoinaudit
        
        	
        	**type**\:   :py:class:`Modeinfoinaudittype <ydk.models.confd_dyncfg.Modeinfoinaudittype>`
        
        	**default value**\: false
        
        .. attribute:: modenamestyle
        
        	
        	**type**\:   :py:class:`Climodenamestyletype <ydk.models.confd_dyncfg.Climodenamestyletype>`
        
        	**default value**\: short
        
        .. attribute:: morebufferlines
        
        	
        	**type**\: one of the below types:
        
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**default value**\: 5000
        
        
        ----
        	**type**\:   :py:class:`Unboundedtype <ydk.models.confd_dyncfg.Unboundedtype>`
        
        	**default value**\: 5000
        
        
        ----
        .. attribute:: multipatternoperation
        
        	
        	**type**\:   :py:class:`Multipatternoperationtype <ydk.models.confd_dyncfg.Multipatternoperationtype>`
        
        	**default value**\: any
        
        .. attribute:: newinsert
        
        	
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: newlogout
        
        	
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: nofollowincompletecommand
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: nomatchcompletionsformat
        
        	
        	**type**\:  str
        
        .. attribute:: olddetailsarg
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: orderedshowconfig
        
        	
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: pipehelpmode
        
        	
        	**type**\:   :py:class:`Pipehelpmodetype <ydk.models.confd_dyncfg.Pipehelpmodetype>`
        
        	**default value**\: auto
        
        .. attribute:: possiblecompletionsformat
        
        	
        	**type**\:  str
        
        	**default value**\: Possible completions:
        
        .. attribute:: prettifystatsname
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: prioritizesubmodecmds
        
        	
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: prompt1
        
        	
        	**type**\:  str
        
        	**default value**\: \u@\h\M> 
        
        .. attribute:: prompt2
        
        	
        	**type**\:  str
        
        	**default value**\: \u@\h\M% 
        
        .. attribute:: promptenumlimit
        
        	
        	**type**\:  int
        
        	**range:** 0..18446744073709551615 \| 0..18446744073709551615
        
        	**default value**\: 4
        
        .. attribute:: prompthostnamedelimiter
        
        	
        	**type**\:  str
        
        	**default value**\: .
        
        .. attribute:: promptsessionscli
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: quicksshteardown
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: quotestyle
        
        	
        	**type**\:   :py:class:`Quotestyletype <ydk.models.confd_dyncfg.Quotestyletype>`
        
        	**default value**\: backslash
        
        .. attribute:: reallocateopertrans
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: reconfirmhidden
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: reportinvalidcompletioninput
        
        	
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: restrictedfileaccess
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: restrictedfileregexp
        
        	
        	**type**\:  str
        
        .. attribute:: rollbackaaa
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: rollbackmax
        
        	
        	**type**\:  int
        
        	**range:** 0..2147483647
        
        	**default value**\: 1000
        
        .. attribute:: rollbacknumbering
        
        	
        	**type**\:   :py:class:`Rollnumbering <ydk.models.confd_dyncfg.Rollnumbering>`
        
        	**default value**\: rolling
        
        .. attribute:: rollbacknumberinginitial
        
        	
        	**type**\:  int
        
        	**range:** \-9223372036854775808..9223372036854775807
        
        	**default value**\: 10000
        
        .. attribute:: safescriptexecution
        
        	
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: showallns
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: showannotations
        
        	
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: showcommitprogress
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: showdefaults
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: showdescription
        
        	
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: showeditors
        
        	
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: showemptycontainers
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: showkeyname
        
        	
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: showlogdirectory
        
        	
        	**type**\:  str
        
        	**default value**\: /var/log
        
        .. attribute:: showmatchbeforepossible
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: shownederrorasinfo
        
        	
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: showpipe
        
        	
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: showpipeconfig
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: showservicemetadata
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: showsubsystemmessages
        
        	
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: showtablelabelsifmultiple
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: showtags
        
        	
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: singleelempattern
        
        	
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: smartrenamefiltering
        
        	
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: sortlocalcmds
        
        	
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: sortshowelems
        
        	
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: sortsubmodecmds
        
        	
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: spacecompletion
        
        	
        	**type**\:   :py:class:`Spacecompletion <ydk.models.confd_dyncfg.Confdconfig.Cli.Spacecompletion>`
        
        	**presence node**\: True
        
        .. attribute:: ssh
        
        	
        	**type**\:   :py:class:`Ssh <ydk.models.confd_dyncfg.Confdconfig.Cli.Ssh>`
        
        	**presence node**\: True
        
        .. attribute:: startupscriptnoninteractive
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: stoploadonerror
        
        	
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: strictrefsonload
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: style
        
        	
        	**type**\:   :py:class:`Clistyle <ydk.models.confd_dyncfg.Clistyle>`
        
        	**default value**\: j
        
        .. attribute:: supportquotedeol
        
        	
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: suppresscommitmessages
        
        	
        	**type**\:   :py:class:`Suppresscommitmessages <ydk.models.confd_dyncfg.Confdconfig.Cli.Suppresscommitmessages>`
        
        	**presence node**\: True
        
        .. attribute:: suppressfastshow
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: suppressnederrors
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: suppressrangekeyword
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: tabextend
        
        	
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: tablelabel
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: tablelookahead
        
        	
        	**type**\:  int
        
        	**range:** 1..18446744073709551615 \| 1..18446744073709551615
        
        	**default value**\: 50
        
        .. attribute:: tableoverflowtruncate
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: templatefilter
        
        	
        	**type**\: list of    :py:class:`Templatefilter <ydk.models.confd_dyncfg.Confdconfig.Cli.Templatefilter>`
        
        .. attribute:: timestamp
        
        	
        	**type**\:   :py:class:`Timestamp <ydk.models.confd_dyncfg.Confdconfig.Cli.Timestamp>`
        
        	**presence node**\: True
        
        .. attribute:: timezone
        
        	
        	**type**\:   :py:class:`Clitimezonetype <ydk.models.confd_dyncfg.Clitimezonetype>`
        
        	**default value**\: local
        
        .. attribute:: toplevelcmdsinsubmode
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: transactionctrlcmds
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: transactions
        
        	
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: trimdefaultsave
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: trimdefaultshow
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: unifiedhistory
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: usedoubledotranges
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: useexposensprefix
        
        	
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: useshortenabled
        
        	
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: utcoffset
        
        	
        	**type**\:  int
        
        	**range:** \-9223372036854775808..9223372036854775807
        
        	**default value**\: 0
        
        .. attribute:: whohistorydatetimeformat
        
        	
        	**type**\:   :py:class:`Whohistorydatetimeformattype <ydk.models.confd_dyncfg.Whohistorydatetimeformattype>`
        
        	**default value**\: short
        
        .. attribute:: whoshowmode
        
        	
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: withdefaults
        
        	DEPRECATED \- use /confdConfig/defaultHandlingMode instead to control this behavior consistently for all northbound interfaces.  withDefaults is either 'true' or 'false'. If 'false' then leaf nodes that have their default values will not be shown when the user displays the configuration, unless the user gives the 'details' option to the 'show' command.  This is useful when there are many settings which are seldom used. When set to 'false' only the values actually modified by the user will be shown
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: wrapinfo
        
        	
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: wrapprompt
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'confd_dyncfg'
        _revision = '2017-01-16'

        def __init__(self):
            super(Confdconfig.Cli, self).__init__()

            self.yang_name = "cli"
            self.yang_parent_name = "confdConfig"
            self.is_presence_container = True

            self.adderrorprefixsuffix = YLeaf(YType.boolean, "addErrorPrefixSuffix")

            self.addextratablespacing = YLeaf(YType.boolean, "addExtraTableSpacing")

            self.allornothingload = YLeaf(YType.boolean, "allOrNothingLoad")

            self.allowabbrevcmds = YLeaf(YType.boolean, "allowAbbrevCmds")

            self.allowabbrevcmdsonload = YLeaf(YType.boolean, "allowAbbrevCmdsOnLoad")

            self.allowabbrevenums = YLeaf(YType.boolean, "allowAbbrevEnums")

            self.allowabbrevkeys = YLeaf(YType.boolean, "allowAbbrevKeys")

            self.allowabbrevparamnames = YLeaf(YType.boolean, "allowAbbrevParamNames")

            self.allowallaswildcard = YLeaf(YType.boolean, "allowAllAsWildcard")

            self.allowcaseinsensitiveenums = YLeaf(YType.boolean, "allowCaseInsensitiveEnums")

            self.allowimplicitwildcard = YLeaf(YType.boolean, "allowImplicitWildcard")

            self.allowoldstylemodecmds = YLeaf(YType.boolean, "allowOldStyleModeCmds")

            self.allowoverwriteoncopy = YLeaf(YType.boolean, "allowOverwriteOnCopy")

            self.allowparenquotes = YLeaf(YType.boolean, "allowParenQuotes")

            self.allowrangeexpression = YLeaf(YType.boolean, "allowRangeExpression")

            self.allowrangeexpressionalltypes = YLeaf(YType.boolean, "allowRangeExpressionAllTypes")

            self.allowtablecellwrap = YLeaf(YType.boolean, "allowTableCellWrap")

            self.allowtableoverflow = YLeaf(YType.boolean, "allowTableOverflow")

            self.allowwildcard = YLeaf(YType.boolean, "allowWildcard")

            self.asyncpromptrefresh = YLeaf(YType.boolean, "asyncPromptRefresh")

            self.auditlogmode = YLeaf(YType.enumeration, "auditLogMode")

            self.autocommitload = YLeaf(YType.boolean, "autocommitLoad")

            self.autocommitloadchunksize = YLeaf(YType.uint64, "autocommitLoadChunkSize")

            self.banner = YLeaf(YType.str, "banner")

            self.bannerfile = YLeaf(YType.str, "bannerFile")

            self.cabortedprefix = YLeaf(YType.str, "cAbortedPrefix")

            self.calignleafvalues = YLeaf(YType.boolean, "cAlignLeafValues")

            self.caseinsensitive = YLeaf(YType.boolean, "caseInsensitive")

            self.caseinsensitivekeys = YLeaf(YType.boolean, "caseInsensitiveKeys")

            self.cerrorprefix = YLeaf(YType.str, "cErrorPrefix")

            self.cextendedcmdsearch = YLeaf(YType.boolean, "cExtendedCmdSearch")

            self.chelp = YLeaf(YType.boolean, "cHelp")

            self.cmdaaaforautowizard = YLeaf(YType.boolean, "cmdAAAForAutowizard")

            self.cmodeexitformat = YLeaf(YType.str, "cModeExitFormat")

            self.columnstats = YLeaf(YType.boolean, "columnStats")

            self.commandtimeout = YLeaf(YType.str, "commandTimeout")

            self.commitactivityclock = YLeaf(YType.boolean, "commitActivityClock")

            self.commitmessage = YLeaf(YType.boolean, "commitMessage")

            self.commitmessageformat = YLeaf(YType.str, "commitMessageFormat")

            self.commitretrytimeout = YLeaf(YType.str, "commitRetryTimeout")

            self.compactshow = YLeaf(YType.boolean, "compactShow")

            self.compactstatsshow = YLeaf(YType.boolean, "compactStatsShow")

            self.compacttable = YLeaf(YType.boolean, "compactTable")

            self.completionlistline = YLeaf(YType.boolean, "completionListLine")

            self.completionmetainfo = YLeaf(YType.enumeration, "completionMetaInfo")

            self.completionshowmax = YLeaf(YType.uint32, "completionShowMax")

            self.completionshowoldval = YLeaf(YType.boolean, "completionShowOldVal")

            self.complistcompact = YLeaf(YType.boolean, "compListCompact")

            self.confirmuncommitedonexit = YLeaf(YType.enumeration, "confirmUncommitedOnExit")

            self.continueonerrorcmdstack = YLeaf(YType.boolean, "continueOnErrorCmdStack")

            self.cprivate = YLeaf(YType.boolean, "cPrivate")

            self.cprompt1 = YLeaf(YType.str, "cPrompt1")

            self.cprompt2 = YLeaf(YType.str, "cPrompt2")

            self.crestrictiveno = YLeaf(YType.boolean, "cRestrictiveNo")

            self.csilentno = YLeaf(YType.boolean, "cSilentNo")

            self.cstylepromptinjstyle = YLeaf(YType.boolean, "cStylePromptInJStyle")

            self.csuppresscmdsearch = YLeaf(YType.boolean, "cSuppressCmdSearch")

            self.ctab = YLeaf(YType.boolean, "cTab")

            self.ctabinfo = YLeaf(YType.boolean, "cTabInfo")

            self.cwarningprefix = YLeaf(YType.str, "cWarningPrefix")

            self.defaultdisplaylevel = YLeaf(YType.int64, "defaultDisplayLevel")

            self.defaultprefix = YLeaf(YType.str, "defaultPrefix")

            self.defaulttablebehavior = YLeaf(YType.enumeration, "defaultTableBehavior")

            self.dequotehidden = YLeaf(YType.boolean, "dequoteHidden")

            self.disableidletimeoutoncmd = YLeaf(YType.boolean, "disableIdleTimeoutOnCmd")

            self.disablepipe = YLeaf(YType.boolean, "disablePipe")

            self.disablepipeconfig = YLeaf(YType.boolean, "disablePipeConfig")

            self.displayemptyconfigcontainers = YLeaf(YType.boolean, "displayEmptyConfigContainers")

            self.displaynonpresenceattributes = YLeaf(YType.boolean, "displayNonPresenceAttributes")

            self.docwrap = YLeaf(YType.boolean, "docWrap")

            self.editwrapmode = YLeaf(YType.enumeration, "editWrapMode")

            self.enabled = YLeaf(YType.boolean, "enabled")

            self.enabledisplaygroups = YLeaf(YType.boolean, "enableDisplayGroups")

            self.enabledisplaylevel = YLeaf(YType.enumeration, "enableDisplayLevel")

            self.enableloadmerge = YLeaf(YType.boolean, "enableLoadMerge")

            self.entersubmodeonleaf = YLeaf(YType.boolean, "enterSubmodeOnLeaf")

            self.enumkeyinfo = YLeaf(YType.boolean, "enumKeyInfo")

            self.escapebackslash = YLeaf(YType.boolean, "escapeBackslash")

            self.execnavigationcmds = YLeaf(YType.boolean, "execNavigationCmds")

            self.exitconfigmodeonctrlc = YLeaf(YType.boolean, "exitConfigModeOnCtrlC")

            self.exitmodeonemptyrange = YLeaf(YType.boolean, "exitModeOnEmptyRange")

            self.expandaliasescape = YLeaf(YType.str, "expandAliasEscape")

            self.expandaliasoncompletion = YLeaf(YType.boolean, "expandAliasOnCompletion")

            self.explicitsetcreate = YLeaf(YType.boolean, "explicitSetCreate")

            self.externalactionerrormsg = YLeaf(YType.str, "externalActionErrorMsg")

            self.forcedexitformat = YLeaf(YType.str, "forcedExitFormat")

            self.hidedotfiles = YLeaf(YType.boolean, "hideDotFiles")

            self.historymaxsize = YLeaf(YType.int64, "historyMaxSize")

            self.historyremoveduplicates = YLeaf(YType.boolean, "historyRemoveDuplicates")

            self.historysave = YLeaf(YType.boolean, "historySave")

            self.idletimeout = YLeaf(YType.str, "idleTimeout")

            self.ignoreleadingwhitespace = YLeaf(YType.boolean, "ignoreLeadingWhitespace")

            self.ignoreshowwithdefaultondiff = YLeaf(YType.boolean, "ignoreShowWithDefaultOnDiff")

            self.ignoresubsystemfailures = YLeaf(YType.boolean, "ignoreSubsystemFailures")

            self.inconsistentdatabasesuffix = YLeaf(YType.str, "inconsistentDatabaseSuffix")

            self.indenttemplates = YLeaf(YType.boolean, "indentTemplates")

            self.infoonmatch = YLeaf(YType.boolean, "infoOnMatch")

            self.infoonspace = YLeaf(YType.boolean, "infoOnSpace")

            self.infoontab = YLeaf(YType.boolean, "infoOnTab")

            self.inheritpaginate = YLeaf(YType.boolean, "inheritPaginate")

            self.instancedescription = YLeaf(YType.boolean, "instanceDescription")

            self.invaliddatastring = YLeaf(YType.str, "invalidDataString")

            self.jabortedprefix = YLeaf(YType.str, "jAbortedPrefix")

            self.jalignleafvalues = YLeaf(YType.boolean, "jAlignLeafValues")

            self.jallowdeleteall = YLeaf(YType.boolean, "jAllowDeleteAll")

            self.jerrorprefix = YLeaf(YType.str, "jErrorPrefix")

            self.jextendedshow = YLeaf(YType.boolean, "jExtendedShow")

            self.jhidehelp = YLeaf(YType.boolean, "jHideHelp")

            self.jshowcr = YLeaf(YType.boolean, "jShowCR")

            self.jshowtablerecursive = YLeaf(YType.boolean, "jShowTableRecursive")

            self.jshowunset = YLeaf(YType.boolean, "jShowUnset")

            self.jshowunsettext = YLeaf(YType.str, "jShowUnsetText")

            self.jstatusformat = YLeaf(YType.str, "jStatusFormat")

            self.jwarningprefix = YLeaf(YType.str, "jWarningPrefix")

            self.laxbarquoting = YLeaf(YType.boolean, "laxBarQuoting")

            self.leafprompting = YLeaf(YType.boolean, "leafPrompting")

            self.loadactivityclock = YLeaf(YType.boolean, "loadActivityClock")

            self.mapactions = YLeaf(YType.enumeration, "mapActions")

            self.matchcompletionsformat = YLeaf(YType.str, "matchCompletionsFormat")

            self.messageformat = YLeaf(YType.str, "messageFormat")

            self.messagemaxsize = YLeaf(YType.int64, "messageMaxSize")

            self.messagequeuesize = YLeaf(YType.int64, "messageQueueSize")

            self.messagewordwrap = YLeaf(YType.boolean, "messageWordWrap")

            self.mixedmode = YLeaf(YType.boolean, "mixedMode")

            self.modeinfoinaaa = YLeaf(YType.enumeration, "modeInfoInAAA")

            self.modeinfoinaudit = YLeaf(YType.enumeration, "modeInfoInAudit")

            self.modenamestyle = YLeaf(YType.enumeration, "modeNameStyle")

            self.morebufferlines = YLeaf(YType.str, "moreBufferLines")

            self.multipatternoperation = YLeaf(YType.enumeration, "multiPatternOperation")

            self.newinsert = YLeaf(YType.boolean, "newInsert")

            self.newlogout = YLeaf(YType.boolean, "newLogout")

            self.nofollowincompletecommand = YLeaf(YType.boolean, "noFollowIncompleteCommand")

            self.nomatchcompletionsformat = YLeaf(YType.str, "noMatchCompletionsFormat")

            self.olddetailsarg = YLeaf(YType.boolean, "oldDetailsArg")

            self.orderedshowconfig = YLeaf(YType.boolean, "orderedShowConfig")

            self.pipehelpmode = YLeaf(YType.enumeration, "pipeHelpMode")

            self.possiblecompletionsformat = YLeaf(YType.str, "possibleCompletionsFormat")

            self.prettifystatsname = YLeaf(YType.boolean, "prettifyStatsName")

            self.prioritizesubmodecmds = YLeaf(YType.boolean, "prioritizeSubmodeCmds")

            self.prompt1 = YLeaf(YType.str, "prompt1")

            self.prompt2 = YLeaf(YType.str, "prompt2")

            self.promptenumlimit = YLeaf(YType.uint64, "promptEnumLimit")

            self.prompthostnamedelimiter = YLeaf(YType.str, "promptHostnameDelimiter")

            self.promptsessionscli = YLeaf(YType.boolean, "promptSessionsCLI")

            self.quicksshteardown = YLeaf(YType.boolean, "quickSshTeardown")

            self.quotestyle = YLeaf(YType.enumeration, "quoteStyle")

            self.reallocateopertrans = YLeaf(YType.boolean, "reallocateOperTrans")

            self.reconfirmhidden = YLeaf(YType.boolean, "reconfirmHidden")

            self.reportinvalidcompletioninput = YLeaf(YType.boolean, "reportInvalidCompletionInput")

            self.restrictedfileaccess = YLeaf(YType.boolean, "restrictedFileAccess")

            self.restrictedfileregexp = YLeaf(YType.str, "restrictedFileRegexp")

            self.rollbackaaa = YLeaf(YType.boolean, "rollbackAAA")

            self.rollbackmax = YLeaf(YType.uint32, "rollbackMax")

            self.rollbacknumbering = YLeaf(YType.enumeration, "rollbackNumbering")

            self.rollbacknumberinginitial = YLeaf(YType.int64, "rollbackNumberingInitial")

            self.safescriptexecution = YLeaf(YType.boolean, "safeScriptExecution")

            self.showallns = YLeaf(YType.boolean, "showAllNs")

            self.showannotations = YLeaf(YType.boolean, "showAnnotations")

            self.showcommitprogress = YLeaf(YType.boolean, "showCommitProgress")

            self.showdefaults = YLeaf(YType.boolean, "showDefaults")

            self.showdescription = YLeaf(YType.boolean, "showDescription")

            self.showeditors = YLeaf(YType.boolean, "showEditors")

            self.showemptycontainers = YLeaf(YType.boolean, "showEmptyContainers")

            self.showkeyname = YLeaf(YType.boolean, "showKeyName")

            self.showlogdirectory = YLeaf(YType.str, "showLogDirectory")

            self.showmatchbeforepossible = YLeaf(YType.boolean, "showMatchBeforePossible")

            self.shownederrorasinfo = YLeaf(YType.boolean, "showNedErrorAsInfo")

            self.showpipe = YLeaf(YType.boolean, "showPipe")

            self.showpipeconfig = YLeaf(YType.boolean, "showPipeConfig")

            self.showservicemetadata = YLeaf(YType.boolean, "showServiceMetaData")

            self.showsubsystemmessages = YLeaf(YType.boolean, "showSubsystemMessages")

            self.showtablelabelsifmultiple = YLeaf(YType.boolean, "showTableLabelsIfMultiple")

            self.showtags = YLeaf(YType.boolean, "showTags")

            self.singleelempattern = YLeaf(YType.boolean, "singleElemPattern")

            self.smartrenamefiltering = YLeaf(YType.boolean, "smartRenameFiltering")

            self.sortlocalcmds = YLeaf(YType.boolean, "sortLocalCmds")

            self.sortshowelems = YLeaf(YType.boolean, "sortShowElems")

            self.sortsubmodecmds = YLeaf(YType.boolean, "sortSubmodeCmds")

            self.startupscriptnoninteractive = YLeaf(YType.boolean, "startupScriptNonInteractive")

            self.stoploadonerror = YLeaf(YType.boolean, "stopLoadOnError")

            self.strictrefsonload = YLeaf(YType.boolean, "strictRefsOnLoad")

            self.style = YLeaf(YType.enumeration, "style")

            self.supportquotedeol = YLeaf(YType.boolean, "supportQuotedEOL")

            self.suppressfastshow = YLeaf(YType.boolean, "suppressFastShow")

            self.suppressnederrors = YLeaf(YType.boolean, "suppressNedErrors")

            self.suppressrangekeyword = YLeaf(YType.boolean, "suppressRangeKeyword")

            self.tabextend = YLeaf(YType.boolean, "tabExtend")

            self.tablelabel = YLeaf(YType.boolean, "tableLabel")

            self.tablelookahead = YLeaf(YType.uint64, "tableLookAhead")

            self.tableoverflowtruncate = YLeaf(YType.boolean, "tableOverflowTruncate")

            self.timezone = YLeaf(YType.enumeration, "timezone")

            self.toplevelcmdsinsubmode = YLeaf(YType.boolean, "topLevelCmdsInSubMode")

            self.transactionctrlcmds = YLeaf(YType.boolean, "transactionCtrlCmds")

            self.transactions = YLeaf(YType.boolean, "transactions")

            self.trimdefaultsave = YLeaf(YType.boolean, "trimDefaultSave")

            self.trimdefaultshow = YLeaf(YType.boolean, "trimDefaultShow")

            self.unifiedhistory = YLeaf(YType.boolean, "unifiedHistory")

            self.usedoubledotranges = YLeaf(YType.boolean, "useDoubleDotRanges")

            self.useexposensprefix = YLeaf(YType.boolean, "useExposeNsPrefix")

            self.useshortenabled = YLeaf(YType.boolean, "useShortEnabled")

            self.utcoffset = YLeaf(YType.int64, "utcOffset")

            self.whohistorydatetimeformat = YLeaf(YType.enumeration, "whoHistoryDateTimeFormat")

            self.whoshowmode = YLeaf(YType.boolean, "whoShowMode")

            self.withdefaults = YLeaf(YType.boolean, "withDefaults")

            self.wrapinfo = YLeaf(YType.boolean, "wrapInfo")

            self.wrapprompt = YLeaf(YType.boolean, "wrapPrompt")

            self.autowizard = None
            self._children_name_map["autowizard"] = "autoWizard"
            self._children_yang_names.add("autoWizard")

            self.spacecompletion = None
            self._children_name_map["spacecompletion"] = "spaceCompletion"
            self._children_yang_names.add("spaceCompletion")

            self.ssh = None
            self._children_name_map["ssh"] = "ssh"
            self._children_yang_names.add("ssh")

            self.suppresscommitmessages = None
            self._children_name_map["suppresscommitmessages"] = "suppressCommitMessages"
            self._children_yang_names.add("suppressCommitMessages")

            self.timestamp = None
            self._children_name_map["timestamp"] = "timestamp"
            self._children_yang_names.add("timestamp")

            self.templatefilter = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("adderrorprefixsuffix",
                            "addextratablespacing",
                            "allornothingload",
                            "allowabbrevcmds",
                            "allowabbrevcmdsonload",
                            "allowabbrevenums",
                            "allowabbrevkeys",
                            "allowabbrevparamnames",
                            "allowallaswildcard",
                            "allowcaseinsensitiveenums",
                            "allowimplicitwildcard",
                            "allowoldstylemodecmds",
                            "allowoverwriteoncopy",
                            "allowparenquotes",
                            "allowrangeexpression",
                            "allowrangeexpressionalltypes",
                            "allowtablecellwrap",
                            "allowtableoverflow",
                            "allowwildcard",
                            "asyncpromptrefresh",
                            "auditlogmode",
                            "autocommitload",
                            "autocommitloadchunksize",
                            "banner",
                            "bannerfile",
                            "cabortedprefix",
                            "calignleafvalues",
                            "caseinsensitive",
                            "caseinsensitivekeys",
                            "cerrorprefix",
                            "cextendedcmdsearch",
                            "chelp",
                            "cmdaaaforautowizard",
                            "cmodeexitformat",
                            "columnstats",
                            "commandtimeout",
                            "commitactivityclock",
                            "commitmessage",
                            "commitmessageformat",
                            "commitretrytimeout",
                            "compactshow",
                            "compactstatsshow",
                            "compacttable",
                            "completionlistline",
                            "completionmetainfo",
                            "completionshowmax",
                            "completionshowoldval",
                            "complistcompact",
                            "confirmuncommitedonexit",
                            "continueonerrorcmdstack",
                            "cprivate",
                            "cprompt1",
                            "cprompt2",
                            "crestrictiveno",
                            "csilentno",
                            "cstylepromptinjstyle",
                            "csuppresscmdsearch",
                            "ctab",
                            "ctabinfo",
                            "cwarningprefix",
                            "defaultdisplaylevel",
                            "defaultprefix",
                            "defaulttablebehavior",
                            "dequotehidden",
                            "disableidletimeoutoncmd",
                            "disablepipe",
                            "disablepipeconfig",
                            "displayemptyconfigcontainers",
                            "displaynonpresenceattributes",
                            "docwrap",
                            "editwrapmode",
                            "enabled",
                            "enabledisplaygroups",
                            "enabledisplaylevel",
                            "enableloadmerge",
                            "entersubmodeonleaf",
                            "enumkeyinfo",
                            "escapebackslash",
                            "execnavigationcmds",
                            "exitconfigmodeonctrlc",
                            "exitmodeonemptyrange",
                            "expandaliasescape",
                            "expandaliasoncompletion",
                            "explicitsetcreate",
                            "externalactionerrormsg",
                            "forcedexitformat",
                            "hidedotfiles",
                            "historymaxsize",
                            "historyremoveduplicates",
                            "historysave",
                            "idletimeout",
                            "ignoreleadingwhitespace",
                            "ignoreshowwithdefaultondiff",
                            "ignoresubsystemfailures",
                            "inconsistentdatabasesuffix",
                            "indenttemplates",
                            "infoonmatch",
                            "infoonspace",
                            "infoontab",
                            "inheritpaginate",
                            "instancedescription",
                            "invaliddatastring",
                            "jabortedprefix",
                            "jalignleafvalues",
                            "jallowdeleteall",
                            "jerrorprefix",
                            "jextendedshow",
                            "jhidehelp",
                            "jshowcr",
                            "jshowtablerecursive",
                            "jshowunset",
                            "jshowunsettext",
                            "jstatusformat",
                            "jwarningprefix",
                            "laxbarquoting",
                            "leafprompting",
                            "loadactivityclock",
                            "mapactions",
                            "matchcompletionsformat",
                            "messageformat",
                            "messagemaxsize",
                            "messagequeuesize",
                            "messagewordwrap",
                            "mixedmode",
                            "modeinfoinaaa",
                            "modeinfoinaudit",
                            "modenamestyle",
                            "morebufferlines",
                            "multipatternoperation",
                            "newinsert",
                            "newlogout",
                            "nofollowincompletecommand",
                            "nomatchcompletionsformat",
                            "olddetailsarg",
                            "orderedshowconfig",
                            "pipehelpmode",
                            "possiblecompletionsformat",
                            "prettifystatsname",
                            "prioritizesubmodecmds",
                            "prompt1",
                            "prompt2",
                            "promptenumlimit",
                            "prompthostnamedelimiter",
                            "promptsessionscli",
                            "quicksshteardown",
                            "quotestyle",
                            "reallocateopertrans",
                            "reconfirmhidden",
                            "reportinvalidcompletioninput",
                            "restrictedfileaccess",
                            "restrictedfileregexp",
                            "rollbackaaa",
                            "rollbackmax",
                            "rollbacknumbering",
                            "rollbacknumberinginitial",
                            "safescriptexecution",
                            "showallns",
                            "showannotations",
                            "showcommitprogress",
                            "showdefaults",
                            "showdescription",
                            "showeditors",
                            "showemptycontainers",
                            "showkeyname",
                            "showlogdirectory",
                            "showmatchbeforepossible",
                            "shownederrorasinfo",
                            "showpipe",
                            "showpipeconfig",
                            "showservicemetadata",
                            "showsubsystemmessages",
                            "showtablelabelsifmultiple",
                            "showtags",
                            "singleelempattern",
                            "smartrenamefiltering",
                            "sortlocalcmds",
                            "sortshowelems",
                            "sortsubmodecmds",
                            "startupscriptnoninteractive",
                            "stoploadonerror",
                            "strictrefsonload",
                            "style",
                            "supportquotedeol",
                            "suppressfastshow",
                            "suppressnederrors",
                            "suppressrangekeyword",
                            "tabextend",
                            "tablelabel",
                            "tablelookahead",
                            "tableoverflowtruncate",
                            "timezone",
                            "toplevelcmdsinsubmode",
                            "transactionctrlcmds",
                            "transactions",
                            "trimdefaultsave",
                            "trimdefaultshow",
                            "unifiedhistory",
                            "usedoubledotranges",
                            "useexposensprefix",
                            "useshortenabled",
                            "utcoffset",
                            "whohistorydatetimeformat",
                            "whoshowmode",
                            "withdefaults",
                            "wrapinfo",
                            "wrapprompt") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Confdconfig.Cli, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Confdconfig.Cli, self).__setattr__(name, value)


        class Spacecompletion(Entity):
            """
            
            
            .. attribute:: enabled
            
            	
            	**type**\:  bool
            
            	**default value**\: true
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'confd_dyncfg'
            _revision = '2017-01-16'

            def __init__(self):
                super(Confdconfig.Cli.Spacecompletion, self).__init__()

                self.yang_name = "spaceCompletion"
                self.yang_parent_name = "cli"
                self.is_presence_container = True

                self.enabled = YLeaf(YType.boolean, "enabled")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("enabled") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Confdconfig.Cli.Spacecompletion, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Confdconfig.Cli.Spacecompletion, self).__setattr__(name, value)

            def has_data(self):
                return self.enabled.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.enabled.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "spaceCompletion" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "confd_dyncfg:confdConfig/cli/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.enabled.is_set or self.enabled.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.enabled.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "enabled"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "enabled"):
                    self.enabled = value
                    self.enabled.value_namespace = name_space
                    self.enabled.value_namespace_prefix = name_space_prefix


        class Timestamp(Entity):
            """
            
            
            .. attribute:: clock24
            
            	
            	**type**\:  bool
            
            	**default value**\: true
            
            .. attribute:: enabled
            
            	
            	**type**\:  bool
            
            	**default value**\: false
            
            .. attribute:: format
            
            	
            	**type**\:  str
            
            	**default value**\: \d{l,4}\m{l,5}\D{l,3}\H{r,2,0}:\t{r,2,0}:\s{r,2,0}.\c{l,3,0} UTC\u{l,1}\o{r,2,0}:\k{r,2,0}
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'confd_dyncfg'
            _revision = '2017-01-16'

            def __init__(self):
                super(Confdconfig.Cli.Timestamp, self).__init__()

                self.yang_name = "timestamp"
                self.yang_parent_name = "cli"
                self.is_presence_container = True

                self.clock24 = YLeaf(YType.boolean, "clock24")

                self.enabled = YLeaf(YType.boolean, "enabled")

                self.format = YLeaf(YType.str, "format")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("clock24",
                                "enabled",
                                "format") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Confdconfig.Cli.Timestamp, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Confdconfig.Cli.Timestamp, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.clock24.is_set or
                    self.enabled.is_set or
                    self.format.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.clock24.yfilter != YFilter.not_set or
                    self.enabled.yfilter != YFilter.not_set or
                    self.format.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "timestamp" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "confd_dyncfg:confdConfig/cli/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.clock24.is_set or self.clock24.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.clock24.get_name_leafdata())
                if (self.enabled.is_set or self.enabled.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.enabled.get_name_leafdata())
                if (self.format.is_set or self.format.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.format.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "clock24" or name == "enabled" or name == "format"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "clock24"):
                    self.clock24 = value
                    self.clock24.value_namespace = name_space
                    self.clock24.value_namespace_prefix = name_space_prefix
                if(value_path == "enabled"):
                    self.enabled = value
                    self.enabled.value_namespace = name_space
                    self.enabled.value_namespace_prefix = name_space_prefix
                if(value_path == "format"):
                    self.format = value
                    self.format.value_namespace = name_space
                    self.format.value_namespace_prefix = name_space_prefix


        class Autowizard(Entity):
            """
            
            
            .. attribute:: enabled
            
            	
            	**type**\:  bool
            
            	**default value**\: true
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'confd_dyncfg'
            _revision = '2017-01-16'

            def __init__(self):
                super(Confdconfig.Cli.Autowizard, self).__init__()

                self.yang_name = "autoWizard"
                self.yang_parent_name = "cli"
                self.is_presence_container = True

                self.enabled = YLeaf(YType.boolean, "enabled")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("enabled") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Confdconfig.Cli.Autowizard, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Confdconfig.Cli.Autowizard, self).__setattr__(name, value)

            def has_data(self):
                return self.enabled.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.enabled.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "autoWizard" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "confd_dyncfg:confdConfig/cli/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.enabled.is_set or self.enabled.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.enabled.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "enabled"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "enabled"):
                    self.enabled = value
                    self.enabled.value_namespace = name_space
                    self.enabled.value_namespace_prefix = name_space_prefix


        class Ssh(Entity):
            """
            
            
            .. attribute:: banner
            
            	
            	**type**\:  str
            
            .. attribute:: bannerfile
            
            	
            	**type**\:  str
            
            .. attribute:: dscp
            
            	
            	**type**\:  int
            
            	**range:** 0..63
            
            .. attribute:: enabled
            
            	
            	**type**\:  bool
            
            	**default value**\: true
            
            .. attribute:: extraipports
            
            	
            	**type**\:  list of str
            
            .. attribute:: ip
            
            	
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**default value**\: 0.0.0.0
            
            
            ----
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            	**default value**\: 0.0.0.0
            
            
            ----
            .. attribute:: port
            
            	
            	**type**\:  int
            
            	**range:** 0..65535
            
            	**default value**\: 2024
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'confd_dyncfg'
            _revision = '2017-01-16'

            def __init__(self):
                super(Confdconfig.Cli.Ssh, self).__init__()

                self.yang_name = "ssh"
                self.yang_parent_name = "cli"
                self.is_presence_container = True

                self.banner = YLeaf(YType.str, "banner")

                self.bannerfile = YLeaf(YType.str, "bannerFile")

                self.dscp = YLeaf(YType.uint8, "dscp")

                self.enabled = YLeaf(YType.boolean, "enabled")

                self.extraipports = YLeafList(YType.str, "extraIpPorts")

                self.ip = YLeaf(YType.str, "ip")

                self.port = YLeaf(YType.uint16, "port")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("banner",
                                "bannerfile",
                                "dscp",
                                "enabled",
                                "extraipports",
                                "ip",
                                "port") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Confdconfig.Cli.Ssh, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Confdconfig.Cli.Ssh, self).__setattr__(name, value)

            def has_data(self):
                for leaf in self.extraipports.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                return (
                    self.banner.is_set or
                    self.bannerfile.is_set or
                    self.dscp.is_set or
                    self.enabled.is_set or
                    self.ip.is_set or
                    self.port.is_set)

            def has_operation(self):
                for leaf in self.extraipports.getYLeafs():
                    if (leaf.is_set):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.banner.yfilter != YFilter.not_set or
                    self.bannerfile.yfilter != YFilter.not_set or
                    self.dscp.yfilter != YFilter.not_set or
                    self.enabled.yfilter != YFilter.not_set or
                    self.extraipports.yfilter != YFilter.not_set or
                    self.ip.yfilter != YFilter.not_set or
                    self.port.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ssh" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "confd_dyncfg:confdConfig/cli/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.banner.is_set or self.banner.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.banner.get_name_leafdata())
                if (self.bannerfile.is_set or self.bannerfile.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.bannerfile.get_name_leafdata())
                if (self.dscp.is_set or self.dscp.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dscp.get_name_leafdata())
                if (self.enabled.is_set or self.enabled.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.enabled.get_name_leafdata())
                if (self.ip.is_set or self.ip.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ip.get_name_leafdata())
                if (self.port.is_set or self.port.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.port.get_name_leafdata())

                leaf_name_data.extend(self.extraipports.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "banner" or name == "bannerFile" or name == "dscp" or name == "enabled" or name == "extraIpPorts" or name == "ip" or name == "port"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "banner"):
                    self.banner = value
                    self.banner.value_namespace = name_space
                    self.banner.value_namespace_prefix = name_space_prefix
                if(value_path == "bannerFile"):
                    self.bannerfile = value
                    self.bannerfile.value_namespace = name_space
                    self.bannerfile.value_namespace_prefix = name_space_prefix
                if(value_path == "dscp"):
                    self.dscp = value
                    self.dscp.value_namespace = name_space
                    self.dscp.value_namespace_prefix = name_space_prefix
                if(value_path == "enabled"):
                    self.enabled = value
                    self.enabled.value_namespace = name_space
                    self.enabled.value_namespace_prefix = name_space_prefix
                if(value_path == "extraIpPorts"):
                    self.extraipports.append(value)
                if(value_path == "ip"):
                    self.ip = value
                    self.ip.value_namespace = name_space
                    self.ip.value_namespace_prefix = name_space_prefix
                if(value_path == "port"):
                    self.port = value
                    self.port.value_namespace = name_space
                    self.port.value_namespace_prefix = name_space_prefix


        class Suppresscommitmessages(Entity):
            """
            
            
            .. attribute:: context
            
            	
            	**type**\:  list of str
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'confd_dyncfg'
            _revision = '2017-01-16'

            def __init__(self):
                super(Confdconfig.Cli.Suppresscommitmessages, self).__init__()

                self.yang_name = "suppressCommitMessages"
                self.yang_parent_name = "cli"
                self.is_presence_container = True

                self.context = YLeafList(YType.str, "context")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("context") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Confdconfig.Cli.Suppresscommitmessages, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Confdconfig.Cli.Suppresscommitmessages, self).__setattr__(name, value)

            def has_data(self):
                for leaf in self.context.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                return False

            def has_operation(self):
                for leaf in self.context.getYLeafs():
                    if (leaf.is_set):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.context.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "suppressCommitMessages" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "confd_dyncfg:confdConfig/cli/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                leaf_name_data.extend(self.context.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "context"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "context"):
                    self.context.append(value)


        class Templatefilter(Entity):
            """
            
            
            .. attribute:: name  <key>
            
            	
            	**type**\:  str
            
            .. attribute:: callback
            
            	
            	**type**\:  str
            
            

            """

            _prefix = 'confd_dyncfg'
            _revision = '2017-01-16'

            def __init__(self):
                super(Confdconfig.Cli.Templatefilter, self).__init__()

                self.yang_name = "templateFilter"
                self.yang_parent_name = "cli"

                self.name = YLeaf(YType.str, "name")

                self.callback = YLeaf(YType.str, "callback")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("name",
                                "callback") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Confdconfig.Cli.Templatefilter, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Confdconfig.Cli.Templatefilter, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.name.is_set or
                    self.callback.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.name.yfilter != YFilter.not_set or
                    self.callback.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "templateFilter" + "[name='" + self.name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "confd_dyncfg:confdConfig/cli/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.name.get_name_leafdata())
                if (self.callback.is_set or self.callback.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.callback.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "name" or name == "callback"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "name"):
                    self.name = value
                    self.name.value_namespace = name_space
                    self.name.value_namespace_prefix = name_space_prefix
                if(value_path == "callback"):
                    self.callback = value
                    self.callback.value_namespace = name_space
                    self.callback.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.templatefilter:
                if (c.has_data()):
                    return True
            return (
                self.adderrorprefixsuffix.is_set or
                self.addextratablespacing.is_set or
                self.allornothingload.is_set or
                self.allowabbrevcmds.is_set or
                self.allowabbrevcmdsonload.is_set or
                self.allowabbrevenums.is_set or
                self.allowabbrevkeys.is_set or
                self.allowabbrevparamnames.is_set or
                self.allowallaswildcard.is_set or
                self.allowcaseinsensitiveenums.is_set or
                self.allowimplicitwildcard.is_set or
                self.allowoldstylemodecmds.is_set or
                self.allowoverwriteoncopy.is_set or
                self.allowparenquotes.is_set or
                self.allowrangeexpression.is_set or
                self.allowrangeexpressionalltypes.is_set or
                self.allowtablecellwrap.is_set or
                self.allowtableoverflow.is_set or
                self.allowwildcard.is_set or
                self.asyncpromptrefresh.is_set or
                self.auditlogmode.is_set or
                self.autocommitload.is_set or
                self.autocommitloadchunksize.is_set or
                self.banner.is_set or
                self.bannerfile.is_set or
                self.cabortedprefix.is_set or
                self.calignleafvalues.is_set or
                self.caseinsensitive.is_set or
                self.caseinsensitivekeys.is_set or
                self.cerrorprefix.is_set or
                self.cextendedcmdsearch.is_set or
                self.chelp.is_set or
                self.cmdaaaforautowizard.is_set or
                self.cmodeexitformat.is_set or
                self.columnstats.is_set or
                self.commandtimeout.is_set or
                self.commitactivityclock.is_set or
                self.commitmessage.is_set or
                self.commitmessageformat.is_set or
                self.commitretrytimeout.is_set or
                self.compactshow.is_set or
                self.compactstatsshow.is_set or
                self.compacttable.is_set or
                self.completionlistline.is_set or
                self.completionmetainfo.is_set or
                self.completionshowmax.is_set or
                self.completionshowoldval.is_set or
                self.complistcompact.is_set or
                self.confirmuncommitedonexit.is_set or
                self.continueonerrorcmdstack.is_set or
                self.cprivate.is_set or
                self.cprompt1.is_set or
                self.cprompt2.is_set or
                self.crestrictiveno.is_set or
                self.csilentno.is_set or
                self.cstylepromptinjstyle.is_set or
                self.csuppresscmdsearch.is_set or
                self.ctab.is_set or
                self.ctabinfo.is_set or
                self.cwarningprefix.is_set or
                self.defaultdisplaylevel.is_set or
                self.defaultprefix.is_set or
                self.defaulttablebehavior.is_set or
                self.dequotehidden.is_set or
                self.disableidletimeoutoncmd.is_set or
                self.disablepipe.is_set or
                self.disablepipeconfig.is_set or
                self.displayemptyconfigcontainers.is_set or
                self.displaynonpresenceattributes.is_set or
                self.docwrap.is_set or
                self.editwrapmode.is_set or
                self.enabled.is_set or
                self.enabledisplaygroups.is_set or
                self.enabledisplaylevel.is_set or
                self.enableloadmerge.is_set or
                self.entersubmodeonleaf.is_set or
                self.enumkeyinfo.is_set or
                self.escapebackslash.is_set or
                self.execnavigationcmds.is_set or
                self.exitconfigmodeonctrlc.is_set or
                self.exitmodeonemptyrange.is_set or
                self.expandaliasescape.is_set or
                self.expandaliasoncompletion.is_set or
                self.explicitsetcreate.is_set or
                self.externalactionerrormsg.is_set or
                self.forcedexitformat.is_set or
                self.hidedotfiles.is_set or
                self.historymaxsize.is_set or
                self.historyremoveduplicates.is_set or
                self.historysave.is_set or
                self.idletimeout.is_set or
                self.ignoreleadingwhitespace.is_set or
                self.ignoreshowwithdefaultondiff.is_set or
                self.ignoresubsystemfailures.is_set or
                self.inconsistentdatabasesuffix.is_set or
                self.indenttemplates.is_set or
                self.infoonmatch.is_set or
                self.infoonspace.is_set or
                self.infoontab.is_set or
                self.inheritpaginate.is_set or
                self.instancedescription.is_set or
                self.invaliddatastring.is_set or
                self.jabortedprefix.is_set or
                self.jalignleafvalues.is_set or
                self.jallowdeleteall.is_set or
                self.jerrorprefix.is_set or
                self.jextendedshow.is_set or
                self.jhidehelp.is_set or
                self.jshowcr.is_set or
                self.jshowtablerecursive.is_set or
                self.jshowunset.is_set or
                self.jshowunsettext.is_set or
                self.jstatusformat.is_set or
                self.jwarningprefix.is_set or
                self.laxbarquoting.is_set or
                self.leafprompting.is_set or
                self.loadactivityclock.is_set or
                self.mapactions.is_set or
                self.matchcompletionsformat.is_set or
                self.messageformat.is_set or
                self.messagemaxsize.is_set or
                self.messagequeuesize.is_set or
                self.messagewordwrap.is_set or
                self.mixedmode.is_set or
                self.modeinfoinaaa.is_set or
                self.modeinfoinaudit.is_set or
                self.modenamestyle.is_set or
                self.morebufferlines.is_set or
                self.multipatternoperation.is_set or
                self.newinsert.is_set or
                self.newlogout.is_set or
                self.nofollowincompletecommand.is_set or
                self.nomatchcompletionsformat.is_set or
                self.olddetailsarg.is_set or
                self.orderedshowconfig.is_set or
                self.pipehelpmode.is_set or
                self.possiblecompletionsformat.is_set or
                self.prettifystatsname.is_set or
                self.prioritizesubmodecmds.is_set or
                self.prompt1.is_set or
                self.prompt2.is_set or
                self.promptenumlimit.is_set or
                self.prompthostnamedelimiter.is_set or
                self.promptsessionscli.is_set or
                self.quicksshteardown.is_set or
                self.quotestyle.is_set or
                self.reallocateopertrans.is_set or
                self.reconfirmhidden.is_set or
                self.reportinvalidcompletioninput.is_set or
                self.restrictedfileaccess.is_set or
                self.restrictedfileregexp.is_set or
                self.rollbackaaa.is_set or
                self.rollbackmax.is_set or
                self.rollbacknumbering.is_set or
                self.rollbacknumberinginitial.is_set or
                self.safescriptexecution.is_set or
                self.showallns.is_set or
                self.showannotations.is_set or
                self.showcommitprogress.is_set or
                self.showdefaults.is_set or
                self.showdescription.is_set or
                self.showeditors.is_set or
                self.showemptycontainers.is_set or
                self.showkeyname.is_set or
                self.showlogdirectory.is_set or
                self.showmatchbeforepossible.is_set or
                self.shownederrorasinfo.is_set or
                self.showpipe.is_set or
                self.showpipeconfig.is_set or
                self.showservicemetadata.is_set or
                self.showsubsystemmessages.is_set or
                self.showtablelabelsifmultiple.is_set or
                self.showtags.is_set or
                self.singleelempattern.is_set or
                self.smartrenamefiltering.is_set or
                self.sortlocalcmds.is_set or
                self.sortshowelems.is_set or
                self.sortsubmodecmds.is_set or
                self.startupscriptnoninteractive.is_set or
                self.stoploadonerror.is_set or
                self.strictrefsonload.is_set or
                self.style.is_set or
                self.supportquotedeol.is_set or
                self.suppressfastshow.is_set or
                self.suppressnederrors.is_set or
                self.suppressrangekeyword.is_set or
                self.tabextend.is_set or
                self.tablelabel.is_set or
                self.tablelookahead.is_set or
                self.tableoverflowtruncate.is_set or
                self.timezone.is_set or
                self.toplevelcmdsinsubmode.is_set or
                self.transactionctrlcmds.is_set or
                self.transactions.is_set or
                self.trimdefaultsave.is_set or
                self.trimdefaultshow.is_set or
                self.unifiedhistory.is_set or
                self.usedoubledotranges.is_set or
                self.useexposensprefix.is_set or
                self.useshortenabled.is_set or
                self.utcoffset.is_set or
                self.whohistorydatetimeformat.is_set or
                self.whoshowmode.is_set or
                self.withdefaults.is_set or
                self.wrapinfo.is_set or
                self.wrapprompt.is_set or
                (self.autowizard is not None) or
                (self.spacecompletion is not None) or
                (self.ssh is not None) or
                (self.suppresscommitmessages is not None) or
                (self.timestamp is not None))

        def has_operation(self):
            for c in self.templatefilter:
                if (c.has_operation()):
                    return True
            return (
                self.yfilter != YFilter.not_set or
                self.adderrorprefixsuffix.yfilter != YFilter.not_set or
                self.addextratablespacing.yfilter != YFilter.not_set or
                self.allornothingload.yfilter != YFilter.not_set or
                self.allowabbrevcmds.yfilter != YFilter.not_set or
                self.allowabbrevcmdsonload.yfilter != YFilter.not_set or
                self.allowabbrevenums.yfilter != YFilter.not_set or
                self.allowabbrevkeys.yfilter != YFilter.not_set or
                self.allowabbrevparamnames.yfilter != YFilter.not_set or
                self.allowallaswildcard.yfilter != YFilter.not_set or
                self.allowcaseinsensitiveenums.yfilter != YFilter.not_set or
                self.allowimplicitwildcard.yfilter != YFilter.not_set or
                self.allowoldstylemodecmds.yfilter != YFilter.not_set or
                self.allowoverwriteoncopy.yfilter != YFilter.not_set or
                self.allowparenquotes.yfilter != YFilter.not_set or
                self.allowrangeexpression.yfilter != YFilter.not_set or
                self.allowrangeexpressionalltypes.yfilter != YFilter.not_set or
                self.allowtablecellwrap.yfilter != YFilter.not_set or
                self.allowtableoverflow.yfilter != YFilter.not_set or
                self.allowwildcard.yfilter != YFilter.not_set or
                self.asyncpromptrefresh.yfilter != YFilter.not_set or
                self.auditlogmode.yfilter != YFilter.not_set or
                self.autocommitload.yfilter != YFilter.not_set or
                self.autocommitloadchunksize.yfilter != YFilter.not_set or
                self.banner.yfilter != YFilter.not_set or
                self.bannerfile.yfilter != YFilter.not_set or
                self.cabortedprefix.yfilter != YFilter.not_set or
                self.calignleafvalues.yfilter != YFilter.not_set or
                self.caseinsensitive.yfilter != YFilter.not_set or
                self.caseinsensitivekeys.yfilter != YFilter.not_set or
                self.cerrorprefix.yfilter != YFilter.not_set or
                self.cextendedcmdsearch.yfilter != YFilter.not_set or
                self.chelp.yfilter != YFilter.not_set or
                self.cmdaaaforautowizard.yfilter != YFilter.not_set or
                self.cmodeexitformat.yfilter != YFilter.not_set or
                self.columnstats.yfilter != YFilter.not_set or
                self.commandtimeout.yfilter != YFilter.not_set or
                self.commitactivityclock.yfilter != YFilter.not_set or
                self.commitmessage.yfilter != YFilter.not_set or
                self.commitmessageformat.yfilter != YFilter.not_set or
                self.commitretrytimeout.yfilter != YFilter.not_set or
                self.compactshow.yfilter != YFilter.not_set or
                self.compactstatsshow.yfilter != YFilter.not_set or
                self.compacttable.yfilter != YFilter.not_set or
                self.completionlistline.yfilter != YFilter.not_set or
                self.completionmetainfo.yfilter != YFilter.not_set or
                self.completionshowmax.yfilter != YFilter.not_set or
                self.completionshowoldval.yfilter != YFilter.not_set or
                self.complistcompact.yfilter != YFilter.not_set or
                self.confirmuncommitedonexit.yfilter != YFilter.not_set or
                self.continueonerrorcmdstack.yfilter != YFilter.not_set or
                self.cprivate.yfilter != YFilter.not_set or
                self.cprompt1.yfilter != YFilter.not_set or
                self.cprompt2.yfilter != YFilter.not_set or
                self.crestrictiveno.yfilter != YFilter.not_set or
                self.csilentno.yfilter != YFilter.not_set or
                self.cstylepromptinjstyle.yfilter != YFilter.not_set or
                self.csuppresscmdsearch.yfilter != YFilter.not_set or
                self.ctab.yfilter != YFilter.not_set or
                self.ctabinfo.yfilter != YFilter.not_set or
                self.cwarningprefix.yfilter != YFilter.not_set or
                self.defaultdisplaylevel.yfilter != YFilter.not_set or
                self.defaultprefix.yfilter != YFilter.not_set or
                self.defaulttablebehavior.yfilter != YFilter.not_set or
                self.dequotehidden.yfilter != YFilter.not_set or
                self.disableidletimeoutoncmd.yfilter != YFilter.not_set or
                self.disablepipe.yfilter != YFilter.not_set or
                self.disablepipeconfig.yfilter != YFilter.not_set or
                self.displayemptyconfigcontainers.yfilter != YFilter.not_set or
                self.displaynonpresenceattributes.yfilter != YFilter.not_set or
                self.docwrap.yfilter != YFilter.not_set or
                self.editwrapmode.yfilter != YFilter.not_set or
                self.enabled.yfilter != YFilter.not_set or
                self.enabledisplaygroups.yfilter != YFilter.not_set or
                self.enabledisplaylevel.yfilter != YFilter.not_set or
                self.enableloadmerge.yfilter != YFilter.not_set or
                self.entersubmodeonleaf.yfilter != YFilter.not_set or
                self.enumkeyinfo.yfilter != YFilter.not_set or
                self.escapebackslash.yfilter != YFilter.not_set or
                self.execnavigationcmds.yfilter != YFilter.not_set or
                self.exitconfigmodeonctrlc.yfilter != YFilter.not_set or
                self.exitmodeonemptyrange.yfilter != YFilter.not_set or
                self.expandaliasescape.yfilter != YFilter.not_set or
                self.expandaliasoncompletion.yfilter != YFilter.not_set or
                self.explicitsetcreate.yfilter != YFilter.not_set or
                self.externalactionerrormsg.yfilter != YFilter.not_set or
                self.forcedexitformat.yfilter != YFilter.not_set or
                self.hidedotfiles.yfilter != YFilter.not_set or
                self.historymaxsize.yfilter != YFilter.not_set or
                self.historyremoveduplicates.yfilter != YFilter.not_set or
                self.historysave.yfilter != YFilter.not_set or
                self.idletimeout.yfilter != YFilter.not_set or
                self.ignoreleadingwhitespace.yfilter != YFilter.not_set or
                self.ignoreshowwithdefaultondiff.yfilter != YFilter.not_set or
                self.ignoresubsystemfailures.yfilter != YFilter.not_set or
                self.inconsistentdatabasesuffix.yfilter != YFilter.not_set or
                self.indenttemplates.yfilter != YFilter.not_set or
                self.infoonmatch.yfilter != YFilter.not_set or
                self.infoonspace.yfilter != YFilter.not_set or
                self.infoontab.yfilter != YFilter.not_set or
                self.inheritpaginate.yfilter != YFilter.not_set or
                self.instancedescription.yfilter != YFilter.not_set or
                self.invaliddatastring.yfilter != YFilter.not_set or
                self.jabortedprefix.yfilter != YFilter.not_set or
                self.jalignleafvalues.yfilter != YFilter.not_set or
                self.jallowdeleteall.yfilter != YFilter.not_set or
                self.jerrorprefix.yfilter != YFilter.not_set or
                self.jextendedshow.yfilter != YFilter.not_set or
                self.jhidehelp.yfilter != YFilter.not_set or
                self.jshowcr.yfilter != YFilter.not_set or
                self.jshowtablerecursive.yfilter != YFilter.not_set or
                self.jshowunset.yfilter != YFilter.not_set or
                self.jshowunsettext.yfilter != YFilter.not_set or
                self.jstatusformat.yfilter != YFilter.not_set or
                self.jwarningprefix.yfilter != YFilter.not_set or
                self.laxbarquoting.yfilter != YFilter.not_set or
                self.leafprompting.yfilter != YFilter.not_set or
                self.loadactivityclock.yfilter != YFilter.not_set or
                self.mapactions.yfilter != YFilter.not_set or
                self.matchcompletionsformat.yfilter != YFilter.not_set or
                self.messageformat.yfilter != YFilter.not_set or
                self.messagemaxsize.yfilter != YFilter.not_set or
                self.messagequeuesize.yfilter != YFilter.not_set or
                self.messagewordwrap.yfilter != YFilter.not_set or
                self.mixedmode.yfilter != YFilter.not_set or
                self.modeinfoinaaa.yfilter != YFilter.not_set or
                self.modeinfoinaudit.yfilter != YFilter.not_set or
                self.modenamestyle.yfilter != YFilter.not_set or
                self.morebufferlines.yfilter != YFilter.not_set or
                self.multipatternoperation.yfilter != YFilter.not_set or
                self.newinsert.yfilter != YFilter.not_set or
                self.newlogout.yfilter != YFilter.not_set or
                self.nofollowincompletecommand.yfilter != YFilter.not_set or
                self.nomatchcompletionsformat.yfilter != YFilter.not_set or
                self.olddetailsarg.yfilter != YFilter.not_set or
                self.orderedshowconfig.yfilter != YFilter.not_set or
                self.pipehelpmode.yfilter != YFilter.not_set or
                self.possiblecompletionsformat.yfilter != YFilter.not_set or
                self.prettifystatsname.yfilter != YFilter.not_set or
                self.prioritizesubmodecmds.yfilter != YFilter.not_set or
                self.prompt1.yfilter != YFilter.not_set or
                self.prompt2.yfilter != YFilter.not_set or
                self.promptenumlimit.yfilter != YFilter.not_set or
                self.prompthostnamedelimiter.yfilter != YFilter.not_set or
                self.promptsessionscli.yfilter != YFilter.not_set or
                self.quicksshteardown.yfilter != YFilter.not_set or
                self.quotestyle.yfilter != YFilter.not_set or
                self.reallocateopertrans.yfilter != YFilter.not_set or
                self.reconfirmhidden.yfilter != YFilter.not_set or
                self.reportinvalidcompletioninput.yfilter != YFilter.not_set or
                self.restrictedfileaccess.yfilter != YFilter.not_set or
                self.restrictedfileregexp.yfilter != YFilter.not_set or
                self.rollbackaaa.yfilter != YFilter.not_set or
                self.rollbackmax.yfilter != YFilter.not_set or
                self.rollbacknumbering.yfilter != YFilter.not_set or
                self.rollbacknumberinginitial.yfilter != YFilter.not_set or
                self.safescriptexecution.yfilter != YFilter.not_set or
                self.showallns.yfilter != YFilter.not_set or
                self.showannotations.yfilter != YFilter.not_set or
                self.showcommitprogress.yfilter != YFilter.not_set or
                self.showdefaults.yfilter != YFilter.not_set or
                self.showdescription.yfilter != YFilter.not_set or
                self.showeditors.yfilter != YFilter.not_set or
                self.showemptycontainers.yfilter != YFilter.not_set or
                self.showkeyname.yfilter != YFilter.not_set or
                self.showlogdirectory.yfilter != YFilter.not_set or
                self.showmatchbeforepossible.yfilter != YFilter.not_set or
                self.shownederrorasinfo.yfilter != YFilter.not_set or
                self.showpipe.yfilter != YFilter.not_set or
                self.showpipeconfig.yfilter != YFilter.not_set or
                self.showservicemetadata.yfilter != YFilter.not_set or
                self.showsubsystemmessages.yfilter != YFilter.not_set or
                self.showtablelabelsifmultiple.yfilter != YFilter.not_set or
                self.showtags.yfilter != YFilter.not_set or
                self.singleelempattern.yfilter != YFilter.not_set or
                self.smartrenamefiltering.yfilter != YFilter.not_set or
                self.sortlocalcmds.yfilter != YFilter.not_set or
                self.sortshowelems.yfilter != YFilter.not_set or
                self.sortsubmodecmds.yfilter != YFilter.not_set or
                self.startupscriptnoninteractive.yfilter != YFilter.not_set or
                self.stoploadonerror.yfilter != YFilter.not_set or
                self.strictrefsonload.yfilter != YFilter.not_set or
                self.style.yfilter != YFilter.not_set or
                self.supportquotedeol.yfilter != YFilter.not_set or
                self.suppressfastshow.yfilter != YFilter.not_set or
                self.suppressnederrors.yfilter != YFilter.not_set or
                self.suppressrangekeyword.yfilter != YFilter.not_set or
                self.tabextend.yfilter != YFilter.not_set or
                self.tablelabel.yfilter != YFilter.not_set or
                self.tablelookahead.yfilter != YFilter.not_set or
                self.tableoverflowtruncate.yfilter != YFilter.not_set or
                self.timezone.yfilter != YFilter.not_set or
                self.toplevelcmdsinsubmode.yfilter != YFilter.not_set or
                self.transactionctrlcmds.yfilter != YFilter.not_set or
                self.transactions.yfilter != YFilter.not_set or
                self.trimdefaultsave.yfilter != YFilter.not_set or
                self.trimdefaultshow.yfilter != YFilter.not_set or
                self.unifiedhistory.yfilter != YFilter.not_set or
                self.usedoubledotranges.yfilter != YFilter.not_set or
                self.useexposensprefix.yfilter != YFilter.not_set or
                self.useshortenabled.yfilter != YFilter.not_set or
                self.utcoffset.yfilter != YFilter.not_set or
                self.whohistorydatetimeformat.yfilter != YFilter.not_set or
                self.whoshowmode.yfilter != YFilter.not_set or
                self.withdefaults.yfilter != YFilter.not_set or
                self.wrapinfo.yfilter != YFilter.not_set or
                self.wrapprompt.yfilter != YFilter.not_set or
                (self.autowizard is not None and self.autowizard.has_operation()) or
                (self.spacecompletion is not None and self.spacecompletion.has_operation()) or
                (self.ssh is not None and self.ssh.has_operation()) or
                (self.suppresscommitmessages is not None and self.suppresscommitmessages.has_operation()) or
                (self.timestamp is not None and self.timestamp.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cli" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "confd_dyncfg:confdConfig/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.adderrorprefixsuffix.is_set or self.adderrorprefixsuffix.yfilter != YFilter.not_set):
                leaf_name_data.append(self.adderrorprefixsuffix.get_name_leafdata())
            if (self.addextratablespacing.is_set or self.addextratablespacing.yfilter != YFilter.not_set):
                leaf_name_data.append(self.addextratablespacing.get_name_leafdata())
            if (self.allornothingload.is_set or self.allornothingload.yfilter != YFilter.not_set):
                leaf_name_data.append(self.allornothingload.get_name_leafdata())
            if (self.allowabbrevcmds.is_set or self.allowabbrevcmds.yfilter != YFilter.not_set):
                leaf_name_data.append(self.allowabbrevcmds.get_name_leafdata())
            if (self.allowabbrevcmdsonload.is_set or self.allowabbrevcmdsonload.yfilter != YFilter.not_set):
                leaf_name_data.append(self.allowabbrevcmdsonload.get_name_leafdata())
            if (self.allowabbrevenums.is_set or self.allowabbrevenums.yfilter != YFilter.not_set):
                leaf_name_data.append(self.allowabbrevenums.get_name_leafdata())
            if (self.allowabbrevkeys.is_set or self.allowabbrevkeys.yfilter != YFilter.not_set):
                leaf_name_data.append(self.allowabbrevkeys.get_name_leafdata())
            if (self.allowabbrevparamnames.is_set or self.allowabbrevparamnames.yfilter != YFilter.not_set):
                leaf_name_data.append(self.allowabbrevparamnames.get_name_leafdata())
            if (self.allowallaswildcard.is_set or self.allowallaswildcard.yfilter != YFilter.not_set):
                leaf_name_data.append(self.allowallaswildcard.get_name_leafdata())
            if (self.allowcaseinsensitiveenums.is_set or self.allowcaseinsensitiveenums.yfilter != YFilter.not_set):
                leaf_name_data.append(self.allowcaseinsensitiveenums.get_name_leafdata())
            if (self.allowimplicitwildcard.is_set or self.allowimplicitwildcard.yfilter != YFilter.not_set):
                leaf_name_data.append(self.allowimplicitwildcard.get_name_leafdata())
            if (self.allowoldstylemodecmds.is_set or self.allowoldstylemodecmds.yfilter != YFilter.not_set):
                leaf_name_data.append(self.allowoldstylemodecmds.get_name_leafdata())
            if (self.allowoverwriteoncopy.is_set or self.allowoverwriteoncopy.yfilter != YFilter.not_set):
                leaf_name_data.append(self.allowoverwriteoncopy.get_name_leafdata())
            if (self.allowparenquotes.is_set or self.allowparenquotes.yfilter != YFilter.not_set):
                leaf_name_data.append(self.allowparenquotes.get_name_leafdata())
            if (self.allowrangeexpression.is_set or self.allowrangeexpression.yfilter != YFilter.not_set):
                leaf_name_data.append(self.allowrangeexpression.get_name_leafdata())
            if (self.allowrangeexpressionalltypes.is_set or self.allowrangeexpressionalltypes.yfilter != YFilter.not_set):
                leaf_name_data.append(self.allowrangeexpressionalltypes.get_name_leafdata())
            if (self.allowtablecellwrap.is_set or self.allowtablecellwrap.yfilter != YFilter.not_set):
                leaf_name_data.append(self.allowtablecellwrap.get_name_leafdata())
            if (self.allowtableoverflow.is_set or self.allowtableoverflow.yfilter != YFilter.not_set):
                leaf_name_data.append(self.allowtableoverflow.get_name_leafdata())
            if (self.allowwildcard.is_set or self.allowwildcard.yfilter != YFilter.not_set):
                leaf_name_data.append(self.allowwildcard.get_name_leafdata())
            if (self.asyncpromptrefresh.is_set or self.asyncpromptrefresh.yfilter != YFilter.not_set):
                leaf_name_data.append(self.asyncpromptrefresh.get_name_leafdata())
            if (self.auditlogmode.is_set or self.auditlogmode.yfilter != YFilter.not_set):
                leaf_name_data.append(self.auditlogmode.get_name_leafdata())
            if (self.autocommitload.is_set or self.autocommitload.yfilter != YFilter.not_set):
                leaf_name_data.append(self.autocommitload.get_name_leafdata())
            if (self.autocommitloadchunksize.is_set or self.autocommitloadchunksize.yfilter != YFilter.not_set):
                leaf_name_data.append(self.autocommitloadchunksize.get_name_leafdata())
            if (self.banner.is_set or self.banner.yfilter != YFilter.not_set):
                leaf_name_data.append(self.banner.get_name_leafdata())
            if (self.bannerfile.is_set or self.bannerfile.yfilter != YFilter.not_set):
                leaf_name_data.append(self.bannerfile.get_name_leafdata())
            if (self.cabortedprefix.is_set or self.cabortedprefix.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cabortedprefix.get_name_leafdata())
            if (self.calignleafvalues.is_set or self.calignleafvalues.yfilter != YFilter.not_set):
                leaf_name_data.append(self.calignleafvalues.get_name_leafdata())
            if (self.caseinsensitive.is_set or self.caseinsensitive.yfilter != YFilter.not_set):
                leaf_name_data.append(self.caseinsensitive.get_name_leafdata())
            if (self.caseinsensitivekeys.is_set or self.caseinsensitivekeys.yfilter != YFilter.not_set):
                leaf_name_data.append(self.caseinsensitivekeys.get_name_leafdata())
            if (self.cerrorprefix.is_set or self.cerrorprefix.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cerrorprefix.get_name_leafdata())
            if (self.cextendedcmdsearch.is_set or self.cextendedcmdsearch.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cextendedcmdsearch.get_name_leafdata())
            if (self.chelp.is_set or self.chelp.yfilter != YFilter.not_set):
                leaf_name_data.append(self.chelp.get_name_leafdata())
            if (self.cmdaaaforautowizard.is_set or self.cmdaaaforautowizard.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cmdaaaforautowizard.get_name_leafdata())
            if (self.cmodeexitformat.is_set or self.cmodeexitformat.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cmodeexitformat.get_name_leafdata())
            if (self.columnstats.is_set or self.columnstats.yfilter != YFilter.not_set):
                leaf_name_data.append(self.columnstats.get_name_leafdata())
            if (self.commandtimeout.is_set or self.commandtimeout.yfilter != YFilter.not_set):
                leaf_name_data.append(self.commandtimeout.get_name_leafdata())
            if (self.commitactivityclock.is_set or self.commitactivityclock.yfilter != YFilter.not_set):
                leaf_name_data.append(self.commitactivityclock.get_name_leafdata())
            if (self.commitmessage.is_set or self.commitmessage.yfilter != YFilter.not_set):
                leaf_name_data.append(self.commitmessage.get_name_leafdata())
            if (self.commitmessageformat.is_set or self.commitmessageformat.yfilter != YFilter.not_set):
                leaf_name_data.append(self.commitmessageformat.get_name_leafdata())
            if (self.commitretrytimeout.is_set or self.commitretrytimeout.yfilter != YFilter.not_set):
                leaf_name_data.append(self.commitretrytimeout.get_name_leafdata())
            if (self.compactshow.is_set or self.compactshow.yfilter != YFilter.not_set):
                leaf_name_data.append(self.compactshow.get_name_leafdata())
            if (self.compactstatsshow.is_set or self.compactstatsshow.yfilter != YFilter.not_set):
                leaf_name_data.append(self.compactstatsshow.get_name_leafdata())
            if (self.compacttable.is_set or self.compacttable.yfilter != YFilter.not_set):
                leaf_name_data.append(self.compacttable.get_name_leafdata())
            if (self.completionlistline.is_set or self.completionlistline.yfilter != YFilter.not_set):
                leaf_name_data.append(self.completionlistline.get_name_leafdata())
            if (self.completionmetainfo.is_set or self.completionmetainfo.yfilter != YFilter.not_set):
                leaf_name_data.append(self.completionmetainfo.get_name_leafdata())
            if (self.completionshowmax.is_set or self.completionshowmax.yfilter != YFilter.not_set):
                leaf_name_data.append(self.completionshowmax.get_name_leafdata())
            if (self.completionshowoldval.is_set or self.completionshowoldval.yfilter != YFilter.not_set):
                leaf_name_data.append(self.completionshowoldval.get_name_leafdata())
            if (self.complistcompact.is_set or self.complistcompact.yfilter != YFilter.not_set):
                leaf_name_data.append(self.complistcompact.get_name_leafdata())
            if (self.confirmuncommitedonexit.is_set or self.confirmuncommitedonexit.yfilter != YFilter.not_set):
                leaf_name_data.append(self.confirmuncommitedonexit.get_name_leafdata())
            if (self.continueonerrorcmdstack.is_set or self.continueonerrorcmdstack.yfilter != YFilter.not_set):
                leaf_name_data.append(self.continueonerrorcmdstack.get_name_leafdata())
            if (self.cprivate.is_set or self.cprivate.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cprivate.get_name_leafdata())
            if (self.cprompt1.is_set or self.cprompt1.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cprompt1.get_name_leafdata())
            if (self.cprompt2.is_set or self.cprompt2.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cprompt2.get_name_leafdata())
            if (self.crestrictiveno.is_set or self.crestrictiveno.yfilter != YFilter.not_set):
                leaf_name_data.append(self.crestrictiveno.get_name_leafdata())
            if (self.csilentno.is_set or self.csilentno.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csilentno.get_name_leafdata())
            if (self.cstylepromptinjstyle.is_set or self.cstylepromptinjstyle.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cstylepromptinjstyle.get_name_leafdata())
            if (self.csuppresscmdsearch.is_set or self.csuppresscmdsearch.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csuppresscmdsearch.get_name_leafdata())
            if (self.ctab.is_set or self.ctab.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ctab.get_name_leafdata())
            if (self.ctabinfo.is_set or self.ctabinfo.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ctabinfo.get_name_leafdata())
            if (self.cwarningprefix.is_set or self.cwarningprefix.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cwarningprefix.get_name_leafdata())
            if (self.defaultdisplaylevel.is_set or self.defaultdisplaylevel.yfilter != YFilter.not_set):
                leaf_name_data.append(self.defaultdisplaylevel.get_name_leafdata())
            if (self.defaultprefix.is_set or self.defaultprefix.yfilter != YFilter.not_set):
                leaf_name_data.append(self.defaultprefix.get_name_leafdata())
            if (self.defaulttablebehavior.is_set or self.defaulttablebehavior.yfilter != YFilter.not_set):
                leaf_name_data.append(self.defaulttablebehavior.get_name_leafdata())
            if (self.dequotehidden.is_set or self.dequotehidden.yfilter != YFilter.not_set):
                leaf_name_data.append(self.dequotehidden.get_name_leafdata())
            if (self.disableidletimeoutoncmd.is_set or self.disableidletimeoutoncmd.yfilter != YFilter.not_set):
                leaf_name_data.append(self.disableidletimeoutoncmd.get_name_leafdata())
            if (self.disablepipe.is_set or self.disablepipe.yfilter != YFilter.not_set):
                leaf_name_data.append(self.disablepipe.get_name_leafdata())
            if (self.disablepipeconfig.is_set or self.disablepipeconfig.yfilter != YFilter.not_set):
                leaf_name_data.append(self.disablepipeconfig.get_name_leafdata())
            if (self.displayemptyconfigcontainers.is_set or self.displayemptyconfigcontainers.yfilter != YFilter.not_set):
                leaf_name_data.append(self.displayemptyconfigcontainers.get_name_leafdata())
            if (self.displaynonpresenceattributes.is_set or self.displaynonpresenceattributes.yfilter != YFilter.not_set):
                leaf_name_data.append(self.displaynonpresenceattributes.get_name_leafdata())
            if (self.docwrap.is_set or self.docwrap.yfilter != YFilter.not_set):
                leaf_name_data.append(self.docwrap.get_name_leafdata())
            if (self.editwrapmode.is_set or self.editwrapmode.yfilter != YFilter.not_set):
                leaf_name_data.append(self.editwrapmode.get_name_leafdata())
            if (self.enabled.is_set or self.enabled.yfilter != YFilter.not_set):
                leaf_name_data.append(self.enabled.get_name_leafdata())
            if (self.enabledisplaygroups.is_set or self.enabledisplaygroups.yfilter != YFilter.not_set):
                leaf_name_data.append(self.enabledisplaygroups.get_name_leafdata())
            if (self.enabledisplaylevel.is_set or self.enabledisplaylevel.yfilter != YFilter.not_set):
                leaf_name_data.append(self.enabledisplaylevel.get_name_leafdata())
            if (self.enableloadmerge.is_set or self.enableloadmerge.yfilter != YFilter.not_set):
                leaf_name_data.append(self.enableloadmerge.get_name_leafdata())
            if (self.entersubmodeonleaf.is_set or self.entersubmodeonleaf.yfilter != YFilter.not_set):
                leaf_name_data.append(self.entersubmodeonleaf.get_name_leafdata())
            if (self.enumkeyinfo.is_set or self.enumkeyinfo.yfilter != YFilter.not_set):
                leaf_name_data.append(self.enumkeyinfo.get_name_leafdata())
            if (self.escapebackslash.is_set or self.escapebackslash.yfilter != YFilter.not_set):
                leaf_name_data.append(self.escapebackslash.get_name_leafdata())
            if (self.execnavigationcmds.is_set or self.execnavigationcmds.yfilter != YFilter.not_set):
                leaf_name_data.append(self.execnavigationcmds.get_name_leafdata())
            if (self.exitconfigmodeonctrlc.is_set or self.exitconfigmodeonctrlc.yfilter != YFilter.not_set):
                leaf_name_data.append(self.exitconfigmodeonctrlc.get_name_leafdata())
            if (self.exitmodeonemptyrange.is_set or self.exitmodeonemptyrange.yfilter != YFilter.not_set):
                leaf_name_data.append(self.exitmodeonemptyrange.get_name_leafdata())
            if (self.expandaliasescape.is_set or self.expandaliasescape.yfilter != YFilter.not_set):
                leaf_name_data.append(self.expandaliasescape.get_name_leafdata())
            if (self.expandaliasoncompletion.is_set or self.expandaliasoncompletion.yfilter != YFilter.not_set):
                leaf_name_data.append(self.expandaliasoncompletion.get_name_leafdata())
            if (self.explicitsetcreate.is_set or self.explicitsetcreate.yfilter != YFilter.not_set):
                leaf_name_data.append(self.explicitsetcreate.get_name_leafdata())
            if (self.externalactionerrormsg.is_set or self.externalactionerrormsg.yfilter != YFilter.not_set):
                leaf_name_data.append(self.externalactionerrormsg.get_name_leafdata())
            if (self.forcedexitformat.is_set or self.forcedexitformat.yfilter != YFilter.not_set):
                leaf_name_data.append(self.forcedexitformat.get_name_leafdata())
            if (self.hidedotfiles.is_set or self.hidedotfiles.yfilter != YFilter.not_set):
                leaf_name_data.append(self.hidedotfiles.get_name_leafdata())
            if (self.historymaxsize.is_set or self.historymaxsize.yfilter != YFilter.not_set):
                leaf_name_data.append(self.historymaxsize.get_name_leafdata())
            if (self.historyremoveduplicates.is_set or self.historyremoveduplicates.yfilter != YFilter.not_set):
                leaf_name_data.append(self.historyremoveduplicates.get_name_leafdata())
            if (self.historysave.is_set or self.historysave.yfilter != YFilter.not_set):
                leaf_name_data.append(self.historysave.get_name_leafdata())
            if (self.idletimeout.is_set or self.idletimeout.yfilter != YFilter.not_set):
                leaf_name_data.append(self.idletimeout.get_name_leafdata())
            if (self.ignoreleadingwhitespace.is_set or self.ignoreleadingwhitespace.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ignoreleadingwhitespace.get_name_leafdata())
            if (self.ignoreshowwithdefaultondiff.is_set or self.ignoreshowwithdefaultondiff.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ignoreshowwithdefaultondiff.get_name_leafdata())
            if (self.ignoresubsystemfailures.is_set or self.ignoresubsystemfailures.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ignoresubsystemfailures.get_name_leafdata())
            if (self.inconsistentdatabasesuffix.is_set or self.inconsistentdatabasesuffix.yfilter != YFilter.not_set):
                leaf_name_data.append(self.inconsistentdatabasesuffix.get_name_leafdata())
            if (self.indenttemplates.is_set or self.indenttemplates.yfilter != YFilter.not_set):
                leaf_name_data.append(self.indenttemplates.get_name_leafdata())
            if (self.infoonmatch.is_set or self.infoonmatch.yfilter != YFilter.not_set):
                leaf_name_data.append(self.infoonmatch.get_name_leafdata())
            if (self.infoonspace.is_set or self.infoonspace.yfilter != YFilter.not_set):
                leaf_name_data.append(self.infoonspace.get_name_leafdata())
            if (self.infoontab.is_set or self.infoontab.yfilter != YFilter.not_set):
                leaf_name_data.append(self.infoontab.get_name_leafdata())
            if (self.inheritpaginate.is_set or self.inheritpaginate.yfilter != YFilter.not_set):
                leaf_name_data.append(self.inheritpaginate.get_name_leafdata())
            if (self.instancedescription.is_set or self.instancedescription.yfilter != YFilter.not_set):
                leaf_name_data.append(self.instancedescription.get_name_leafdata())
            if (self.invaliddatastring.is_set or self.invaliddatastring.yfilter != YFilter.not_set):
                leaf_name_data.append(self.invaliddatastring.get_name_leafdata())
            if (self.jabortedprefix.is_set or self.jabortedprefix.yfilter != YFilter.not_set):
                leaf_name_data.append(self.jabortedprefix.get_name_leafdata())
            if (self.jalignleafvalues.is_set or self.jalignleafvalues.yfilter != YFilter.not_set):
                leaf_name_data.append(self.jalignleafvalues.get_name_leafdata())
            if (self.jallowdeleteall.is_set or self.jallowdeleteall.yfilter != YFilter.not_set):
                leaf_name_data.append(self.jallowdeleteall.get_name_leafdata())
            if (self.jerrorprefix.is_set or self.jerrorprefix.yfilter != YFilter.not_set):
                leaf_name_data.append(self.jerrorprefix.get_name_leafdata())
            if (self.jextendedshow.is_set or self.jextendedshow.yfilter != YFilter.not_set):
                leaf_name_data.append(self.jextendedshow.get_name_leafdata())
            if (self.jhidehelp.is_set or self.jhidehelp.yfilter != YFilter.not_set):
                leaf_name_data.append(self.jhidehelp.get_name_leafdata())
            if (self.jshowcr.is_set or self.jshowcr.yfilter != YFilter.not_set):
                leaf_name_data.append(self.jshowcr.get_name_leafdata())
            if (self.jshowtablerecursive.is_set or self.jshowtablerecursive.yfilter != YFilter.not_set):
                leaf_name_data.append(self.jshowtablerecursive.get_name_leafdata())
            if (self.jshowunset.is_set or self.jshowunset.yfilter != YFilter.not_set):
                leaf_name_data.append(self.jshowunset.get_name_leafdata())
            if (self.jshowunsettext.is_set or self.jshowunsettext.yfilter != YFilter.not_set):
                leaf_name_data.append(self.jshowunsettext.get_name_leafdata())
            if (self.jstatusformat.is_set or self.jstatusformat.yfilter != YFilter.not_set):
                leaf_name_data.append(self.jstatusformat.get_name_leafdata())
            if (self.jwarningprefix.is_set or self.jwarningprefix.yfilter != YFilter.not_set):
                leaf_name_data.append(self.jwarningprefix.get_name_leafdata())
            if (self.laxbarquoting.is_set or self.laxbarquoting.yfilter != YFilter.not_set):
                leaf_name_data.append(self.laxbarquoting.get_name_leafdata())
            if (self.leafprompting.is_set or self.leafprompting.yfilter != YFilter.not_set):
                leaf_name_data.append(self.leafprompting.get_name_leafdata())
            if (self.loadactivityclock.is_set or self.loadactivityclock.yfilter != YFilter.not_set):
                leaf_name_data.append(self.loadactivityclock.get_name_leafdata())
            if (self.mapactions.is_set or self.mapactions.yfilter != YFilter.not_set):
                leaf_name_data.append(self.mapactions.get_name_leafdata())
            if (self.matchcompletionsformat.is_set or self.matchcompletionsformat.yfilter != YFilter.not_set):
                leaf_name_data.append(self.matchcompletionsformat.get_name_leafdata())
            if (self.messageformat.is_set or self.messageformat.yfilter != YFilter.not_set):
                leaf_name_data.append(self.messageformat.get_name_leafdata())
            if (self.messagemaxsize.is_set or self.messagemaxsize.yfilter != YFilter.not_set):
                leaf_name_data.append(self.messagemaxsize.get_name_leafdata())
            if (self.messagequeuesize.is_set or self.messagequeuesize.yfilter != YFilter.not_set):
                leaf_name_data.append(self.messagequeuesize.get_name_leafdata())
            if (self.messagewordwrap.is_set or self.messagewordwrap.yfilter != YFilter.not_set):
                leaf_name_data.append(self.messagewordwrap.get_name_leafdata())
            if (self.mixedmode.is_set or self.mixedmode.yfilter != YFilter.not_set):
                leaf_name_data.append(self.mixedmode.get_name_leafdata())
            if (self.modeinfoinaaa.is_set or self.modeinfoinaaa.yfilter != YFilter.not_set):
                leaf_name_data.append(self.modeinfoinaaa.get_name_leafdata())
            if (self.modeinfoinaudit.is_set or self.modeinfoinaudit.yfilter != YFilter.not_set):
                leaf_name_data.append(self.modeinfoinaudit.get_name_leafdata())
            if (self.modenamestyle.is_set or self.modenamestyle.yfilter != YFilter.not_set):
                leaf_name_data.append(self.modenamestyle.get_name_leafdata())
            if (self.morebufferlines.is_set or self.morebufferlines.yfilter != YFilter.not_set):
                leaf_name_data.append(self.morebufferlines.get_name_leafdata())
            if (self.multipatternoperation.is_set or self.multipatternoperation.yfilter != YFilter.not_set):
                leaf_name_data.append(self.multipatternoperation.get_name_leafdata())
            if (self.newinsert.is_set or self.newinsert.yfilter != YFilter.not_set):
                leaf_name_data.append(self.newinsert.get_name_leafdata())
            if (self.newlogout.is_set or self.newlogout.yfilter != YFilter.not_set):
                leaf_name_data.append(self.newlogout.get_name_leafdata())
            if (self.nofollowincompletecommand.is_set or self.nofollowincompletecommand.yfilter != YFilter.not_set):
                leaf_name_data.append(self.nofollowincompletecommand.get_name_leafdata())
            if (self.nomatchcompletionsformat.is_set or self.nomatchcompletionsformat.yfilter != YFilter.not_set):
                leaf_name_data.append(self.nomatchcompletionsformat.get_name_leafdata())
            if (self.olddetailsarg.is_set or self.olddetailsarg.yfilter != YFilter.not_set):
                leaf_name_data.append(self.olddetailsarg.get_name_leafdata())
            if (self.orderedshowconfig.is_set or self.orderedshowconfig.yfilter != YFilter.not_set):
                leaf_name_data.append(self.orderedshowconfig.get_name_leafdata())
            if (self.pipehelpmode.is_set or self.pipehelpmode.yfilter != YFilter.not_set):
                leaf_name_data.append(self.pipehelpmode.get_name_leafdata())
            if (self.possiblecompletionsformat.is_set or self.possiblecompletionsformat.yfilter != YFilter.not_set):
                leaf_name_data.append(self.possiblecompletionsformat.get_name_leafdata())
            if (self.prettifystatsname.is_set or self.prettifystatsname.yfilter != YFilter.not_set):
                leaf_name_data.append(self.prettifystatsname.get_name_leafdata())
            if (self.prioritizesubmodecmds.is_set or self.prioritizesubmodecmds.yfilter != YFilter.not_set):
                leaf_name_data.append(self.prioritizesubmodecmds.get_name_leafdata())
            if (self.prompt1.is_set or self.prompt1.yfilter != YFilter.not_set):
                leaf_name_data.append(self.prompt1.get_name_leafdata())
            if (self.prompt2.is_set or self.prompt2.yfilter != YFilter.not_set):
                leaf_name_data.append(self.prompt2.get_name_leafdata())
            if (self.promptenumlimit.is_set or self.promptenumlimit.yfilter != YFilter.not_set):
                leaf_name_data.append(self.promptenumlimit.get_name_leafdata())
            if (self.prompthostnamedelimiter.is_set or self.prompthostnamedelimiter.yfilter != YFilter.not_set):
                leaf_name_data.append(self.prompthostnamedelimiter.get_name_leafdata())
            if (self.promptsessionscli.is_set or self.promptsessionscli.yfilter != YFilter.not_set):
                leaf_name_data.append(self.promptsessionscli.get_name_leafdata())
            if (self.quicksshteardown.is_set or self.quicksshteardown.yfilter != YFilter.not_set):
                leaf_name_data.append(self.quicksshteardown.get_name_leafdata())
            if (self.quotestyle.is_set or self.quotestyle.yfilter != YFilter.not_set):
                leaf_name_data.append(self.quotestyle.get_name_leafdata())
            if (self.reallocateopertrans.is_set or self.reallocateopertrans.yfilter != YFilter.not_set):
                leaf_name_data.append(self.reallocateopertrans.get_name_leafdata())
            if (self.reconfirmhidden.is_set or self.reconfirmhidden.yfilter != YFilter.not_set):
                leaf_name_data.append(self.reconfirmhidden.get_name_leafdata())
            if (self.reportinvalidcompletioninput.is_set or self.reportinvalidcompletioninput.yfilter != YFilter.not_set):
                leaf_name_data.append(self.reportinvalidcompletioninput.get_name_leafdata())
            if (self.restrictedfileaccess.is_set or self.restrictedfileaccess.yfilter != YFilter.not_set):
                leaf_name_data.append(self.restrictedfileaccess.get_name_leafdata())
            if (self.restrictedfileregexp.is_set or self.restrictedfileregexp.yfilter != YFilter.not_set):
                leaf_name_data.append(self.restrictedfileregexp.get_name_leafdata())
            if (self.rollbackaaa.is_set or self.rollbackaaa.yfilter != YFilter.not_set):
                leaf_name_data.append(self.rollbackaaa.get_name_leafdata())
            if (self.rollbackmax.is_set or self.rollbackmax.yfilter != YFilter.not_set):
                leaf_name_data.append(self.rollbackmax.get_name_leafdata())
            if (self.rollbacknumbering.is_set or self.rollbacknumbering.yfilter != YFilter.not_set):
                leaf_name_data.append(self.rollbacknumbering.get_name_leafdata())
            if (self.rollbacknumberinginitial.is_set or self.rollbacknumberinginitial.yfilter != YFilter.not_set):
                leaf_name_data.append(self.rollbacknumberinginitial.get_name_leafdata())
            if (self.safescriptexecution.is_set or self.safescriptexecution.yfilter != YFilter.not_set):
                leaf_name_data.append(self.safescriptexecution.get_name_leafdata())
            if (self.showallns.is_set or self.showallns.yfilter != YFilter.not_set):
                leaf_name_data.append(self.showallns.get_name_leafdata())
            if (self.showannotations.is_set or self.showannotations.yfilter != YFilter.not_set):
                leaf_name_data.append(self.showannotations.get_name_leafdata())
            if (self.showcommitprogress.is_set or self.showcommitprogress.yfilter != YFilter.not_set):
                leaf_name_data.append(self.showcommitprogress.get_name_leafdata())
            if (self.showdefaults.is_set or self.showdefaults.yfilter != YFilter.not_set):
                leaf_name_data.append(self.showdefaults.get_name_leafdata())
            if (self.showdescription.is_set or self.showdescription.yfilter != YFilter.not_set):
                leaf_name_data.append(self.showdescription.get_name_leafdata())
            if (self.showeditors.is_set or self.showeditors.yfilter != YFilter.not_set):
                leaf_name_data.append(self.showeditors.get_name_leafdata())
            if (self.showemptycontainers.is_set or self.showemptycontainers.yfilter != YFilter.not_set):
                leaf_name_data.append(self.showemptycontainers.get_name_leafdata())
            if (self.showkeyname.is_set or self.showkeyname.yfilter != YFilter.not_set):
                leaf_name_data.append(self.showkeyname.get_name_leafdata())
            if (self.showlogdirectory.is_set or self.showlogdirectory.yfilter != YFilter.not_set):
                leaf_name_data.append(self.showlogdirectory.get_name_leafdata())
            if (self.showmatchbeforepossible.is_set or self.showmatchbeforepossible.yfilter != YFilter.not_set):
                leaf_name_data.append(self.showmatchbeforepossible.get_name_leafdata())
            if (self.shownederrorasinfo.is_set or self.shownederrorasinfo.yfilter != YFilter.not_set):
                leaf_name_data.append(self.shownederrorasinfo.get_name_leafdata())
            if (self.showpipe.is_set or self.showpipe.yfilter != YFilter.not_set):
                leaf_name_data.append(self.showpipe.get_name_leafdata())
            if (self.showpipeconfig.is_set or self.showpipeconfig.yfilter != YFilter.not_set):
                leaf_name_data.append(self.showpipeconfig.get_name_leafdata())
            if (self.showservicemetadata.is_set or self.showservicemetadata.yfilter != YFilter.not_set):
                leaf_name_data.append(self.showservicemetadata.get_name_leafdata())
            if (self.showsubsystemmessages.is_set or self.showsubsystemmessages.yfilter != YFilter.not_set):
                leaf_name_data.append(self.showsubsystemmessages.get_name_leafdata())
            if (self.showtablelabelsifmultiple.is_set or self.showtablelabelsifmultiple.yfilter != YFilter.not_set):
                leaf_name_data.append(self.showtablelabelsifmultiple.get_name_leafdata())
            if (self.showtags.is_set or self.showtags.yfilter != YFilter.not_set):
                leaf_name_data.append(self.showtags.get_name_leafdata())
            if (self.singleelempattern.is_set or self.singleelempattern.yfilter != YFilter.not_set):
                leaf_name_data.append(self.singleelempattern.get_name_leafdata())
            if (self.smartrenamefiltering.is_set or self.smartrenamefiltering.yfilter != YFilter.not_set):
                leaf_name_data.append(self.smartrenamefiltering.get_name_leafdata())
            if (self.sortlocalcmds.is_set or self.sortlocalcmds.yfilter != YFilter.not_set):
                leaf_name_data.append(self.sortlocalcmds.get_name_leafdata())
            if (self.sortshowelems.is_set or self.sortshowelems.yfilter != YFilter.not_set):
                leaf_name_data.append(self.sortshowelems.get_name_leafdata())
            if (self.sortsubmodecmds.is_set or self.sortsubmodecmds.yfilter != YFilter.not_set):
                leaf_name_data.append(self.sortsubmodecmds.get_name_leafdata())
            if (self.startupscriptnoninteractive.is_set or self.startupscriptnoninteractive.yfilter != YFilter.not_set):
                leaf_name_data.append(self.startupscriptnoninteractive.get_name_leafdata())
            if (self.stoploadonerror.is_set or self.stoploadonerror.yfilter != YFilter.not_set):
                leaf_name_data.append(self.stoploadonerror.get_name_leafdata())
            if (self.strictrefsonload.is_set or self.strictrefsonload.yfilter != YFilter.not_set):
                leaf_name_data.append(self.strictrefsonload.get_name_leafdata())
            if (self.style.is_set or self.style.yfilter != YFilter.not_set):
                leaf_name_data.append(self.style.get_name_leafdata())
            if (self.supportquotedeol.is_set or self.supportquotedeol.yfilter != YFilter.not_set):
                leaf_name_data.append(self.supportquotedeol.get_name_leafdata())
            if (self.suppressfastshow.is_set or self.suppressfastshow.yfilter != YFilter.not_set):
                leaf_name_data.append(self.suppressfastshow.get_name_leafdata())
            if (self.suppressnederrors.is_set or self.suppressnederrors.yfilter != YFilter.not_set):
                leaf_name_data.append(self.suppressnederrors.get_name_leafdata())
            if (self.suppressrangekeyword.is_set or self.suppressrangekeyword.yfilter != YFilter.not_set):
                leaf_name_data.append(self.suppressrangekeyword.get_name_leafdata())
            if (self.tabextend.is_set or self.tabextend.yfilter != YFilter.not_set):
                leaf_name_data.append(self.tabextend.get_name_leafdata())
            if (self.tablelabel.is_set or self.tablelabel.yfilter != YFilter.not_set):
                leaf_name_data.append(self.tablelabel.get_name_leafdata())
            if (self.tablelookahead.is_set or self.tablelookahead.yfilter != YFilter.not_set):
                leaf_name_data.append(self.tablelookahead.get_name_leafdata())
            if (self.tableoverflowtruncate.is_set or self.tableoverflowtruncate.yfilter != YFilter.not_set):
                leaf_name_data.append(self.tableoverflowtruncate.get_name_leafdata())
            if (self.timezone.is_set or self.timezone.yfilter != YFilter.not_set):
                leaf_name_data.append(self.timezone.get_name_leafdata())
            if (self.toplevelcmdsinsubmode.is_set or self.toplevelcmdsinsubmode.yfilter != YFilter.not_set):
                leaf_name_data.append(self.toplevelcmdsinsubmode.get_name_leafdata())
            if (self.transactionctrlcmds.is_set or self.transactionctrlcmds.yfilter != YFilter.not_set):
                leaf_name_data.append(self.transactionctrlcmds.get_name_leafdata())
            if (self.transactions.is_set or self.transactions.yfilter != YFilter.not_set):
                leaf_name_data.append(self.transactions.get_name_leafdata())
            if (self.trimdefaultsave.is_set or self.trimdefaultsave.yfilter != YFilter.not_set):
                leaf_name_data.append(self.trimdefaultsave.get_name_leafdata())
            if (self.trimdefaultshow.is_set or self.trimdefaultshow.yfilter != YFilter.not_set):
                leaf_name_data.append(self.trimdefaultshow.get_name_leafdata())
            if (self.unifiedhistory.is_set or self.unifiedhistory.yfilter != YFilter.not_set):
                leaf_name_data.append(self.unifiedhistory.get_name_leafdata())
            if (self.usedoubledotranges.is_set or self.usedoubledotranges.yfilter != YFilter.not_set):
                leaf_name_data.append(self.usedoubledotranges.get_name_leafdata())
            if (self.useexposensprefix.is_set or self.useexposensprefix.yfilter != YFilter.not_set):
                leaf_name_data.append(self.useexposensprefix.get_name_leafdata())
            if (self.useshortenabled.is_set or self.useshortenabled.yfilter != YFilter.not_set):
                leaf_name_data.append(self.useshortenabled.get_name_leafdata())
            if (self.utcoffset.is_set or self.utcoffset.yfilter != YFilter.not_set):
                leaf_name_data.append(self.utcoffset.get_name_leafdata())
            if (self.whohistorydatetimeformat.is_set or self.whohistorydatetimeformat.yfilter != YFilter.not_set):
                leaf_name_data.append(self.whohistorydatetimeformat.get_name_leafdata())
            if (self.whoshowmode.is_set or self.whoshowmode.yfilter != YFilter.not_set):
                leaf_name_data.append(self.whoshowmode.get_name_leafdata())
            if (self.withdefaults.is_set or self.withdefaults.yfilter != YFilter.not_set):
                leaf_name_data.append(self.withdefaults.get_name_leafdata())
            if (self.wrapinfo.is_set or self.wrapinfo.yfilter != YFilter.not_set):
                leaf_name_data.append(self.wrapinfo.get_name_leafdata())
            if (self.wrapprompt.is_set or self.wrapprompt.yfilter != YFilter.not_set):
                leaf_name_data.append(self.wrapprompt.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "autoWizard"):
                if (self.autowizard is None):
                    self.autowizard = Confdconfig.Cli.Autowizard()
                    self.autowizard.parent = self
                    self._children_name_map["autowizard"] = "autoWizard"
                return self.autowizard

            if (child_yang_name == "spaceCompletion"):
                if (self.spacecompletion is None):
                    self.spacecompletion = Confdconfig.Cli.Spacecompletion()
                    self.spacecompletion.parent = self
                    self._children_name_map["spacecompletion"] = "spaceCompletion"
                return self.spacecompletion

            if (child_yang_name == "ssh"):
                if (self.ssh is None):
                    self.ssh = Confdconfig.Cli.Ssh()
                    self.ssh.parent = self
                    self._children_name_map["ssh"] = "ssh"
                return self.ssh

            if (child_yang_name == "suppressCommitMessages"):
                if (self.suppresscommitmessages is None):
                    self.suppresscommitmessages = Confdconfig.Cli.Suppresscommitmessages()
                    self.suppresscommitmessages.parent = self
                    self._children_name_map["suppresscommitmessages"] = "suppressCommitMessages"
                return self.suppresscommitmessages

            if (child_yang_name == "templateFilter"):
                for c in self.templatefilter:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Confdconfig.Cli.Templatefilter()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.templatefilter.append(c)
                return c

            if (child_yang_name == "timestamp"):
                if (self.timestamp is None):
                    self.timestamp = Confdconfig.Cli.Timestamp()
                    self.timestamp.parent = self
                    self._children_name_map["timestamp"] = "timestamp"
                return self.timestamp

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "autoWizard" or name == "spaceCompletion" or name == "ssh" or name == "suppressCommitMessages" or name == "templateFilter" or name == "timestamp" or name == "addErrorPrefixSuffix" or name == "addExtraTableSpacing" or name == "allOrNothingLoad" or name == "allowAbbrevCmds" or name == "allowAbbrevCmdsOnLoad" or name == "allowAbbrevEnums" or name == "allowAbbrevKeys" or name == "allowAbbrevParamNames" or name == "allowAllAsWildcard" or name == "allowCaseInsensitiveEnums" or name == "allowImplicitWildcard" or name == "allowOldStyleModeCmds" or name == "allowOverwriteOnCopy" or name == "allowParenQuotes" or name == "allowRangeExpression" or name == "allowRangeExpressionAllTypes" or name == "allowTableCellWrap" or name == "allowTableOverflow" or name == "allowWildcard" or name == "asyncPromptRefresh" or name == "auditLogMode" or name == "autocommitLoad" or name == "autocommitLoadChunkSize" or name == "banner" or name == "bannerFile" or name == "cAbortedPrefix" or name == "cAlignLeafValues" or name == "caseInsensitive" or name == "caseInsensitiveKeys" or name == "cErrorPrefix" or name == "cExtendedCmdSearch" or name == "cHelp" or name == "cmdAAAForAutowizard" or name == "cModeExitFormat" or name == "columnStats" or name == "commandTimeout" or name == "commitActivityClock" or name == "commitMessage" or name == "commitMessageFormat" or name == "commitRetryTimeout" or name == "compactShow" or name == "compactStatsShow" or name == "compactTable" or name == "completionListLine" or name == "completionMetaInfo" or name == "completionShowMax" or name == "completionShowOldVal" or name == "compListCompact" or name == "confirmUncommitedOnExit" or name == "continueOnErrorCmdStack" or name == "cPrivate" or name == "cPrompt1" or name == "cPrompt2" or name == "cRestrictiveNo" or name == "cSilentNo" or name == "cStylePromptInJStyle" or name == "cSuppressCmdSearch" or name == "cTab" or name == "cTabInfo" or name == "cWarningPrefix" or name == "defaultDisplayLevel" or name == "defaultPrefix" or name == "defaultTableBehavior" or name == "dequoteHidden" or name == "disableIdleTimeoutOnCmd" or name == "disablePipe" or name == "disablePipeConfig" or name == "displayEmptyConfigContainers" or name == "displayNonPresenceAttributes" or name == "docWrap" or name == "editWrapMode" or name == "enabled" or name == "enableDisplayGroups" or name == "enableDisplayLevel" or name == "enableLoadMerge" or name == "enterSubmodeOnLeaf" or name == "enumKeyInfo" or name == "escapeBackslash" or name == "execNavigationCmds" or name == "exitConfigModeOnCtrlC" or name == "exitModeOnEmptyRange" or name == "expandAliasEscape" or name == "expandAliasOnCompletion" or name == "explicitSetCreate" or name == "externalActionErrorMsg" or name == "forcedExitFormat" or name == "hideDotFiles" or name == "historyMaxSize" or name == "historyRemoveDuplicates" or name == "historySave" or name == "idleTimeout" or name == "ignoreLeadingWhitespace" or name == "ignoreShowWithDefaultOnDiff" or name == "ignoreSubsystemFailures" or name == "inconsistentDatabaseSuffix" or name == "indentTemplates" or name == "infoOnMatch" or name == "infoOnSpace" or name == "infoOnTab" or name == "inheritPaginate" or name == "instanceDescription" or name == "invalidDataString" or name == "jAbortedPrefix" or name == "jAlignLeafValues" or name == "jAllowDeleteAll" or name == "jErrorPrefix" or name == "jExtendedShow" or name == "jHideHelp" or name == "jShowCR" or name == "jShowTableRecursive" or name == "jShowUnset" or name == "jShowUnsetText" or name == "jStatusFormat" or name == "jWarningPrefix" or name == "laxBarQuoting" or name == "leafPrompting" or name == "loadActivityClock" or name == "mapActions" or name == "matchCompletionsFormat" or name == "messageFormat" or name == "messageMaxSize" or name == "messageQueueSize" or name == "messageWordWrap" or name == "mixedMode" or name == "modeInfoInAAA" or name == "modeInfoInAudit" or name == "modeNameStyle" or name == "moreBufferLines" or name == "multiPatternOperation" or name == "newInsert" or name == "newLogout" or name == "noFollowIncompleteCommand" or name == "noMatchCompletionsFormat" or name == "oldDetailsArg" or name == "orderedShowConfig" or name == "pipeHelpMode" or name == "possibleCompletionsFormat" or name == "prettifyStatsName" or name == "prioritizeSubmodeCmds" or name == "prompt1" or name == "prompt2" or name == "promptEnumLimit" or name == "promptHostnameDelimiter" or name == "promptSessionsCLI" or name == "quickSshTeardown" or name == "quoteStyle" or name == "reallocateOperTrans" or name == "reconfirmHidden" or name == "reportInvalidCompletionInput" or name == "restrictedFileAccess" or name == "restrictedFileRegexp" or name == "rollbackAAA" or name == "rollbackMax" or name == "rollbackNumbering" or name == "rollbackNumberingInitial" or name == "safeScriptExecution" or name == "showAllNs" or name == "showAnnotations" or name == "showCommitProgress" or name == "showDefaults" or name == "showDescription" or name == "showEditors" or name == "showEmptyContainers" or name == "showKeyName" or name == "showLogDirectory" or name == "showMatchBeforePossible" or name == "showNedErrorAsInfo" or name == "showPipe" or name == "showPipeConfig" or name == "showServiceMetaData" or name == "showSubsystemMessages" or name == "showTableLabelsIfMultiple" or name == "showTags" or name == "singleElemPattern" or name == "smartRenameFiltering" or name == "sortLocalCmds" or name == "sortShowElems" or name == "sortSubmodeCmds" or name == "startupScriptNonInteractive" or name == "stopLoadOnError" or name == "strictRefsOnLoad" or name == "style" or name == "supportQuotedEOL" or name == "suppressFastShow" or name == "suppressNedErrors" or name == "suppressRangeKeyword" or name == "tabExtend" or name == "tableLabel" or name == "tableLookAhead" or name == "tableOverflowTruncate" or name == "timezone" or name == "topLevelCmdsInSubMode" or name == "transactionCtrlCmds" or name == "transactions" or name == "trimDefaultSave" or name == "trimDefaultShow" or name == "unifiedHistory" or name == "useDoubleDotRanges" or name == "useExposeNsPrefix" or name == "useShortEnabled" or name == "utcOffset" or name == "whoHistoryDateTimeFormat" or name == "whoShowMode" or name == "withDefaults" or name == "wrapInfo" or name == "wrapPrompt"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "addErrorPrefixSuffix"):
                self.adderrorprefixsuffix = value
                self.adderrorprefixsuffix.value_namespace = name_space
                self.adderrorprefixsuffix.value_namespace_prefix = name_space_prefix
            if(value_path == "addExtraTableSpacing"):
                self.addextratablespacing = value
                self.addextratablespacing.value_namespace = name_space
                self.addextratablespacing.value_namespace_prefix = name_space_prefix
            if(value_path == "allOrNothingLoad"):
                self.allornothingload = value
                self.allornothingload.value_namespace = name_space
                self.allornothingload.value_namespace_prefix = name_space_prefix
            if(value_path == "allowAbbrevCmds"):
                self.allowabbrevcmds = value
                self.allowabbrevcmds.value_namespace = name_space
                self.allowabbrevcmds.value_namespace_prefix = name_space_prefix
            if(value_path == "allowAbbrevCmdsOnLoad"):
                self.allowabbrevcmdsonload = value
                self.allowabbrevcmdsonload.value_namespace = name_space
                self.allowabbrevcmdsonload.value_namespace_prefix = name_space_prefix
            if(value_path == "allowAbbrevEnums"):
                self.allowabbrevenums = value
                self.allowabbrevenums.value_namespace = name_space
                self.allowabbrevenums.value_namespace_prefix = name_space_prefix
            if(value_path == "allowAbbrevKeys"):
                self.allowabbrevkeys = value
                self.allowabbrevkeys.value_namespace = name_space
                self.allowabbrevkeys.value_namespace_prefix = name_space_prefix
            if(value_path == "allowAbbrevParamNames"):
                self.allowabbrevparamnames = value
                self.allowabbrevparamnames.value_namespace = name_space
                self.allowabbrevparamnames.value_namespace_prefix = name_space_prefix
            if(value_path == "allowAllAsWildcard"):
                self.allowallaswildcard = value
                self.allowallaswildcard.value_namespace = name_space
                self.allowallaswildcard.value_namespace_prefix = name_space_prefix
            if(value_path == "allowCaseInsensitiveEnums"):
                self.allowcaseinsensitiveenums = value
                self.allowcaseinsensitiveenums.value_namespace = name_space
                self.allowcaseinsensitiveenums.value_namespace_prefix = name_space_prefix
            if(value_path == "allowImplicitWildcard"):
                self.allowimplicitwildcard = value
                self.allowimplicitwildcard.value_namespace = name_space
                self.allowimplicitwildcard.value_namespace_prefix = name_space_prefix
            if(value_path == "allowOldStyleModeCmds"):
                self.allowoldstylemodecmds = value
                self.allowoldstylemodecmds.value_namespace = name_space
                self.allowoldstylemodecmds.value_namespace_prefix = name_space_prefix
            if(value_path == "allowOverwriteOnCopy"):
                self.allowoverwriteoncopy = value
                self.allowoverwriteoncopy.value_namespace = name_space
                self.allowoverwriteoncopy.value_namespace_prefix = name_space_prefix
            if(value_path == "allowParenQuotes"):
                self.allowparenquotes = value
                self.allowparenquotes.value_namespace = name_space
                self.allowparenquotes.value_namespace_prefix = name_space_prefix
            if(value_path == "allowRangeExpression"):
                self.allowrangeexpression = value
                self.allowrangeexpression.value_namespace = name_space
                self.allowrangeexpression.value_namespace_prefix = name_space_prefix
            if(value_path == "allowRangeExpressionAllTypes"):
                self.allowrangeexpressionalltypes = value
                self.allowrangeexpressionalltypes.value_namespace = name_space
                self.allowrangeexpressionalltypes.value_namespace_prefix = name_space_prefix
            if(value_path == "allowTableCellWrap"):
                self.allowtablecellwrap = value
                self.allowtablecellwrap.value_namespace = name_space
                self.allowtablecellwrap.value_namespace_prefix = name_space_prefix
            if(value_path == "allowTableOverflow"):
                self.allowtableoverflow = value
                self.allowtableoverflow.value_namespace = name_space
                self.allowtableoverflow.value_namespace_prefix = name_space_prefix
            if(value_path == "allowWildcard"):
                self.allowwildcard = value
                self.allowwildcard.value_namespace = name_space
                self.allowwildcard.value_namespace_prefix = name_space_prefix
            if(value_path == "asyncPromptRefresh"):
                self.asyncpromptrefresh = value
                self.asyncpromptrefresh.value_namespace = name_space
                self.asyncpromptrefresh.value_namespace_prefix = name_space_prefix
            if(value_path == "auditLogMode"):
                self.auditlogmode = value
                self.auditlogmode.value_namespace = name_space
                self.auditlogmode.value_namespace_prefix = name_space_prefix
            if(value_path == "autocommitLoad"):
                self.autocommitload = value
                self.autocommitload.value_namespace = name_space
                self.autocommitload.value_namespace_prefix = name_space_prefix
            if(value_path == "autocommitLoadChunkSize"):
                self.autocommitloadchunksize = value
                self.autocommitloadchunksize.value_namespace = name_space
                self.autocommitloadchunksize.value_namespace_prefix = name_space_prefix
            if(value_path == "banner"):
                self.banner = value
                self.banner.value_namespace = name_space
                self.banner.value_namespace_prefix = name_space_prefix
            if(value_path == "bannerFile"):
                self.bannerfile = value
                self.bannerfile.value_namespace = name_space
                self.bannerfile.value_namespace_prefix = name_space_prefix
            if(value_path == "cAbortedPrefix"):
                self.cabortedprefix = value
                self.cabortedprefix.value_namespace = name_space
                self.cabortedprefix.value_namespace_prefix = name_space_prefix
            if(value_path == "cAlignLeafValues"):
                self.calignleafvalues = value
                self.calignleafvalues.value_namespace = name_space
                self.calignleafvalues.value_namespace_prefix = name_space_prefix
            if(value_path == "caseInsensitive"):
                self.caseinsensitive = value
                self.caseinsensitive.value_namespace = name_space
                self.caseinsensitive.value_namespace_prefix = name_space_prefix
            if(value_path == "caseInsensitiveKeys"):
                self.caseinsensitivekeys = value
                self.caseinsensitivekeys.value_namespace = name_space
                self.caseinsensitivekeys.value_namespace_prefix = name_space_prefix
            if(value_path == "cErrorPrefix"):
                self.cerrorprefix = value
                self.cerrorprefix.value_namespace = name_space
                self.cerrorprefix.value_namespace_prefix = name_space_prefix
            if(value_path == "cExtendedCmdSearch"):
                self.cextendedcmdsearch = value
                self.cextendedcmdsearch.value_namespace = name_space
                self.cextendedcmdsearch.value_namespace_prefix = name_space_prefix
            if(value_path == "cHelp"):
                self.chelp = value
                self.chelp.value_namespace = name_space
                self.chelp.value_namespace_prefix = name_space_prefix
            if(value_path == "cmdAAAForAutowizard"):
                self.cmdaaaforautowizard = value
                self.cmdaaaforautowizard.value_namespace = name_space
                self.cmdaaaforautowizard.value_namespace_prefix = name_space_prefix
            if(value_path == "cModeExitFormat"):
                self.cmodeexitformat = value
                self.cmodeexitformat.value_namespace = name_space
                self.cmodeexitformat.value_namespace_prefix = name_space_prefix
            if(value_path == "columnStats"):
                self.columnstats = value
                self.columnstats.value_namespace = name_space
                self.columnstats.value_namespace_prefix = name_space_prefix
            if(value_path == "commandTimeout"):
                self.commandtimeout = value
                self.commandtimeout.value_namespace = name_space
                self.commandtimeout.value_namespace_prefix = name_space_prefix
            if(value_path == "commitActivityClock"):
                self.commitactivityclock = value
                self.commitactivityclock.value_namespace = name_space
                self.commitactivityclock.value_namespace_prefix = name_space_prefix
            if(value_path == "commitMessage"):
                self.commitmessage = value
                self.commitmessage.value_namespace = name_space
                self.commitmessage.value_namespace_prefix = name_space_prefix
            if(value_path == "commitMessageFormat"):
                self.commitmessageformat = value
                self.commitmessageformat.value_namespace = name_space
                self.commitmessageformat.value_namespace_prefix = name_space_prefix
            if(value_path == "commitRetryTimeout"):
                self.commitretrytimeout = value
                self.commitretrytimeout.value_namespace = name_space
                self.commitretrytimeout.value_namespace_prefix = name_space_prefix
            if(value_path == "compactShow"):
                self.compactshow = value
                self.compactshow.value_namespace = name_space
                self.compactshow.value_namespace_prefix = name_space_prefix
            if(value_path == "compactStatsShow"):
                self.compactstatsshow = value
                self.compactstatsshow.value_namespace = name_space
                self.compactstatsshow.value_namespace_prefix = name_space_prefix
            if(value_path == "compactTable"):
                self.compacttable = value
                self.compacttable.value_namespace = name_space
                self.compacttable.value_namespace_prefix = name_space_prefix
            if(value_path == "completionListLine"):
                self.completionlistline = value
                self.completionlistline.value_namespace = name_space
                self.completionlistline.value_namespace_prefix = name_space_prefix
            if(value_path == "completionMetaInfo"):
                self.completionmetainfo = value
                self.completionmetainfo.value_namespace = name_space
                self.completionmetainfo.value_namespace_prefix = name_space_prefix
            if(value_path == "completionShowMax"):
                self.completionshowmax = value
                self.completionshowmax.value_namespace = name_space
                self.completionshowmax.value_namespace_prefix = name_space_prefix
            if(value_path == "completionShowOldVal"):
                self.completionshowoldval = value
                self.completionshowoldval.value_namespace = name_space
                self.completionshowoldval.value_namespace_prefix = name_space_prefix
            if(value_path == "compListCompact"):
                self.complistcompact = value
                self.complistcompact.value_namespace = name_space
                self.complistcompact.value_namespace_prefix = name_space_prefix
            if(value_path == "confirmUncommitedOnExit"):
                self.confirmuncommitedonexit = value
                self.confirmuncommitedonexit.value_namespace = name_space
                self.confirmuncommitedonexit.value_namespace_prefix = name_space_prefix
            if(value_path == "continueOnErrorCmdStack"):
                self.continueonerrorcmdstack = value
                self.continueonerrorcmdstack.value_namespace = name_space
                self.continueonerrorcmdstack.value_namespace_prefix = name_space_prefix
            if(value_path == "cPrivate"):
                self.cprivate = value
                self.cprivate.value_namespace = name_space
                self.cprivate.value_namespace_prefix = name_space_prefix
            if(value_path == "cPrompt1"):
                self.cprompt1 = value
                self.cprompt1.value_namespace = name_space
                self.cprompt1.value_namespace_prefix = name_space_prefix
            if(value_path == "cPrompt2"):
                self.cprompt2 = value
                self.cprompt2.value_namespace = name_space
                self.cprompt2.value_namespace_prefix = name_space_prefix
            if(value_path == "cRestrictiveNo"):
                self.crestrictiveno = value
                self.crestrictiveno.value_namespace = name_space
                self.crestrictiveno.value_namespace_prefix = name_space_prefix
            if(value_path == "cSilentNo"):
                self.csilentno = value
                self.csilentno.value_namespace = name_space
                self.csilentno.value_namespace_prefix = name_space_prefix
            if(value_path == "cStylePromptInJStyle"):
                self.cstylepromptinjstyle = value
                self.cstylepromptinjstyle.value_namespace = name_space
                self.cstylepromptinjstyle.value_namespace_prefix = name_space_prefix
            if(value_path == "cSuppressCmdSearch"):
                self.csuppresscmdsearch = value
                self.csuppresscmdsearch.value_namespace = name_space
                self.csuppresscmdsearch.value_namespace_prefix = name_space_prefix
            if(value_path == "cTab"):
                self.ctab = value
                self.ctab.value_namespace = name_space
                self.ctab.value_namespace_prefix = name_space_prefix
            if(value_path == "cTabInfo"):
                self.ctabinfo = value
                self.ctabinfo.value_namespace = name_space
                self.ctabinfo.value_namespace_prefix = name_space_prefix
            if(value_path == "cWarningPrefix"):
                self.cwarningprefix = value
                self.cwarningprefix.value_namespace = name_space
                self.cwarningprefix.value_namespace_prefix = name_space_prefix
            if(value_path == "defaultDisplayLevel"):
                self.defaultdisplaylevel = value
                self.defaultdisplaylevel.value_namespace = name_space
                self.defaultdisplaylevel.value_namespace_prefix = name_space_prefix
            if(value_path == "defaultPrefix"):
                self.defaultprefix = value
                self.defaultprefix.value_namespace = name_space
                self.defaultprefix.value_namespace_prefix = name_space_prefix
            if(value_path == "defaultTableBehavior"):
                self.defaulttablebehavior = value
                self.defaulttablebehavior.value_namespace = name_space
                self.defaulttablebehavior.value_namespace_prefix = name_space_prefix
            if(value_path == "dequoteHidden"):
                self.dequotehidden = value
                self.dequotehidden.value_namespace = name_space
                self.dequotehidden.value_namespace_prefix = name_space_prefix
            if(value_path == "disableIdleTimeoutOnCmd"):
                self.disableidletimeoutoncmd = value
                self.disableidletimeoutoncmd.value_namespace = name_space
                self.disableidletimeoutoncmd.value_namespace_prefix = name_space_prefix
            if(value_path == "disablePipe"):
                self.disablepipe = value
                self.disablepipe.value_namespace = name_space
                self.disablepipe.value_namespace_prefix = name_space_prefix
            if(value_path == "disablePipeConfig"):
                self.disablepipeconfig = value
                self.disablepipeconfig.value_namespace = name_space
                self.disablepipeconfig.value_namespace_prefix = name_space_prefix
            if(value_path == "displayEmptyConfigContainers"):
                self.displayemptyconfigcontainers = value
                self.displayemptyconfigcontainers.value_namespace = name_space
                self.displayemptyconfigcontainers.value_namespace_prefix = name_space_prefix
            if(value_path == "displayNonPresenceAttributes"):
                self.displaynonpresenceattributes = value
                self.displaynonpresenceattributes.value_namespace = name_space
                self.displaynonpresenceattributes.value_namespace_prefix = name_space_prefix
            if(value_path == "docWrap"):
                self.docwrap = value
                self.docwrap.value_namespace = name_space
                self.docwrap.value_namespace_prefix = name_space_prefix
            if(value_path == "editWrapMode"):
                self.editwrapmode = value
                self.editwrapmode.value_namespace = name_space
                self.editwrapmode.value_namespace_prefix = name_space_prefix
            if(value_path == "enabled"):
                self.enabled = value
                self.enabled.value_namespace = name_space
                self.enabled.value_namespace_prefix = name_space_prefix
            if(value_path == "enableDisplayGroups"):
                self.enabledisplaygroups = value
                self.enabledisplaygroups.value_namespace = name_space
                self.enabledisplaygroups.value_namespace_prefix = name_space_prefix
            if(value_path == "enableDisplayLevel"):
                self.enabledisplaylevel = value
                self.enabledisplaylevel.value_namespace = name_space
                self.enabledisplaylevel.value_namespace_prefix = name_space_prefix
            if(value_path == "enableLoadMerge"):
                self.enableloadmerge = value
                self.enableloadmerge.value_namespace = name_space
                self.enableloadmerge.value_namespace_prefix = name_space_prefix
            if(value_path == "enterSubmodeOnLeaf"):
                self.entersubmodeonleaf = value
                self.entersubmodeonleaf.value_namespace = name_space
                self.entersubmodeonleaf.value_namespace_prefix = name_space_prefix
            if(value_path == "enumKeyInfo"):
                self.enumkeyinfo = value
                self.enumkeyinfo.value_namespace = name_space
                self.enumkeyinfo.value_namespace_prefix = name_space_prefix
            if(value_path == "escapeBackslash"):
                self.escapebackslash = value
                self.escapebackslash.value_namespace = name_space
                self.escapebackslash.value_namespace_prefix = name_space_prefix
            if(value_path == "execNavigationCmds"):
                self.execnavigationcmds = value
                self.execnavigationcmds.value_namespace = name_space
                self.execnavigationcmds.value_namespace_prefix = name_space_prefix
            if(value_path == "exitConfigModeOnCtrlC"):
                self.exitconfigmodeonctrlc = value
                self.exitconfigmodeonctrlc.value_namespace = name_space
                self.exitconfigmodeonctrlc.value_namespace_prefix = name_space_prefix
            if(value_path == "exitModeOnEmptyRange"):
                self.exitmodeonemptyrange = value
                self.exitmodeonemptyrange.value_namespace = name_space
                self.exitmodeonemptyrange.value_namespace_prefix = name_space_prefix
            if(value_path == "expandAliasEscape"):
                self.expandaliasescape = value
                self.expandaliasescape.value_namespace = name_space
                self.expandaliasescape.value_namespace_prefix = name_space_prefix
            if(value_path == "expandAliasOnCompletion"):
                self.expandaliasoncompletion = value
                self.expandaliasoncompletion.value_namespace = name_space
                self.expandaliasoncompletion.value_namespace_prefix = name_space_prefix
            if(value_path == "explicitSetCreate"):
                self.explicitsetcreate = value
                self.explicitsetcreate.value_namespace = name_space
                self.explicitsetcreate.value_namespace_prefix = name_space_prefix
            if(value_path == "externalActionErrorMsg"):
                self.externalactionerrormsg = value
                self.externalactionerrormsg.value_namespace = name_space
                self.externalactionerrormsg.value_namespace_prefix = name_space_prefix
            if(value_path == "forcedExitFormat"):
                self.forcedexitformat = value
                self.forcedexitformat.value_namespace = name_space
                self.forcedexitformat.value_namespace_prefix = name_space_prefix
            if(value_path == "hideDotFiles"):
                self.hidedotfiles = value
                self.hidedotfiles.value_namespace = name_space
                self.hidedotfiles.value_namespace_prefix = name_space_prefix
            if(value_path == "historyMaxSize"):
                self.historymaxsize = value
                self.historymaxsize.value_namespace = name_space
                self.historymaxsize.value_namespace_prefix = name_space_prefix
            if(value_path == "historyRemoveDuplicates"):
                self.historyremoveduplicates = value
                self.historyremoveduplicates.value_namespace = name_space
                self.historyremoveduplicates.value_namespace_prefix = name_space_prefix
            if(value_path == "historySave"):
                self.historysave = value
                self.historysave.value_namespace = name_space
                self.historysave.value_namespace_prefix = name_space_prefix
            if(value_path == "idleTimeout"):
                self.idletimeout = value
                self.idletimeout.value_namespace = name_space
                self.idletimeout.value_namespace_prefix = name_space_prefix
            if(value_path == "ignoreLeadingWhitespace"):
                self.ignoreleadingwhitespace = value
                self.ignoreleadingwhitespace.value_namespace = name_space
                self.ignoreleadingwhitespace.value_namespace_prefix = name_space_prefix
            if(value_path == "ignoreShowWithDefaultOnDiff"):
                self.ignoreshowwithdefaultondiff = value
                self.ignoreshowwithdefaultondiff.value_namespace = name_space
                self.ignoreshowwithdefaultondiff.value_namespace_prefix = name_space_prefix
            if(value_path == "ignoreSubsystemFailures"):
                self.ignoresubsystemfailures = value
                self.ignoresubsystemfailures.value_namespace = name_space
                self.ignoresubsystemfailures.value_namespace_prefix = name_space_prefix
            if(value_path == "inconsistentDatabaseSuffix"):
                self.inconsistentdatabasesuffix = value
                self.inconsistentdatabasesuffix.value_namespace = name_space
                self.inconsistentdatabasesuffix.value_namespace_prefix = name_space_prefix
            if(value_path == "indentTemplates"):
                self.indenttemplates = value
                self.indenttemplates.value_namespace = name_space
                self.indenttemplates.value_namespace_prefix = name_space_prefix
            if(value_path == "infoOnMatch"):
                self.infoonmatch = value
                self.infoonmatch.value_namespace = name_space
                self.infoonmatch.value_namespace_prefix = name_space_prefix
            if(value_path == "infoOnSpace"):
                self.infoonspace = value
                self.infoonspace.value_namespace = name_space
                self.infoonspace.value_namespace_prefix = name_space_prefix
            if(value_path == "infoOnTab"):
                self.infoontab = value
                self.infoontab.value_namespace = name_space
                self.infoontab.value_namespace_prefix = name_space_prefix
            if(value_path == "inheritPaginate"):
                self.inheritpaginate = value
                self.inheritpaginate.value_namespace = name_space
                self.inheritpaginate.value_namespace_prefix = name_space_prefix
            if(value_path == "instanceDescription"):
                self.instancedescription = value
                self.instancedescription.value_namespace = name_space
                self.instancedescription.value_namespace_prefix = name_space_prefix
            if(value_path == "invalidDataString"):
                self.invaliddatastring = value
                self.invaliddatastring.value_namespace = name_space
                self.invaliddatastring.value_namespace_prefix = name_space_prefix
            if(value_path == "jAbortedPrefix"):
                self.jabortedprefix = value
                self.jabortedprefix.value_namespace = name_space
                self.jabortedprefix.value_namespace_prefix = name_space_prefix
            if(value_path == "jAlignLeafValues"):
                self.jalignleafvalues = value
                self.jalignleafvalues.value_namespace = name_space
                self.jalignleafvalues.value_namespace_prefix = name_space_prefix
            if(value_path == "jAllowDeleteAll"):
                self.jallowdeleteall = value
                self.jallowdeleteall.value_namespace = name_space
                self.jallowdeleteall.value_namespace_prefix = name_space_prefix
            if(value_path == "jErrorPrefix"):
                self.jerrorprefix = value
                self.jerrorprefix.value_namespace = name_space
                self.jerrorprefix.value_namespace_prefix = name_space_prefix
            if(value_path == "jExtendedShow"):
                self.jextendedshow = value
                self.jextendedshow.value_namespace = name_space
                self.jextendedshow.value_namespace_prefix = name_space_prefix
            if(value_path == "jHideHelp"):
                self.jhidehelp = value
                self.jhidehelp.value_namespace = name_space
                self.jhidehelp.value_namespace_prefix = name_space_prefix
            if(value_path == "jShowCR"):
                self.jshowcr = value
                self.jshowcr.value_namespace = name_space
                self.jshowcr.value_namespace_prefix = name_space_prefix
            if(value_path == "jShowTableRecursive"):
                self.jshowtablerecursive = value
                self.jshowtablerecursive.value_namespace = name_space
                self.jshowtablerecursive.value_namespace_prefix = name_space_prefix
            if(value_path == "jShowUnset"):
                self.jshowunset = value
                self.jshowunset.value_namespace = name_space
                self.jshowunset.value_namespace_prefix = name_space_prefix
            if(value_path == "jShowUnsetText"):
                self.jshowunsettext = value
                self.jshowunsettext.value_namespace = name_space
                self.jshowunsettext.value_namespace_prefix = name_space_prefix
            if(value_path == "jStatusFormat"):
                self.jstatusformat = value
                self.jstatusformat.value_namespace = name_space
                self.jstatusformat.value_namespace_prefix = name_space_prefix
            if(value_path == "jWarningPrefix"):
                self.jwarningprefix = value
                self.jwarningprefix.value_namespace = name_space
                self.jwarningprefix.value_namespace_prefix = name_space_prefix
            if(value_path == "laxBarQuoting"):
                self.laxbarquoting = value
                self.laxbarquoting.value_namespace = name_space
                self.laxbarquoting.value_namespace_prefix = name_space_prefix
            if(value_path == "leafPrompting"):
                self.leafprompting = value
                self.leafprompting.value_namespace = name_space
                self.leafprompting.value_namespace_prefix = name_space_prefix
            if(value_path == "loadActivityClock"):
                self.loadactivityclock = value
                self.loadactivityclock.value_namespace = name_space
                self.loadactivityclock.value_namespace_prefix = name_space_prefix
            if(value_path == "mapActions"):
                self.mapactions = value
                self.mapactions.value_namespace = name_space
                self.mapactions.value_namespace_prefix = name_space_prefix
            if(value_path == "matchCompletionsFormat"):
                self.matchcompletionsformat = value
                self.matchcompletionsformat.value_namespace = name_space
                self.matchcompletionsformat.value_namespace_prefix = name_space_prefix
            if(value_path == "messageFormat"):
                self.messageformat = value
                self.messageformat.value_namespace = name_space
                self.messageformat.value_namespace_prefix = name_space_prefix
            if(value_path == "messageMaxSize"):
                self.messagemaxsize = value
                self.messagemaxsize.value_namespace = name_space
                self.messagemaxsize.value_namespace_prefix = name_space_prefix
            if(value_path == "messageQueueSize"):
                self.messagequeuesize = value
                self.messagequeuesize.value_namespace = name_space
                self.messagequeuesize.value_namespace_prefix = name_space_prefix
            if(value_path == "messageWordWrap"):
                self.messagewordwrap = value
                self.messagewordwrap.value_namespace = name_space
                self.messagewordwrap.value_namespace_prefix = name_space_prefix
            if(value_path == "mixedMode"):
                self.mixedmode = value
                self.mixedmode.value_namespace = name_space
                self.mixedmode.value_namespace_prefix = name_space_prefix
            if(value_path == "modeInfoInAAA"):
                self.modeinfoinaaa = value
                self.modeinfoinaaa.value_namespace = name_space
                self.modeinfoinaaa.value_namespace_prefix = name_space_prefix
            if(value_path == "modeInfoInAudit"):
                self.modeinfoinaudit = value
                self.modeinfoinaudit.value_namespace = name_space
                self.modeinfoinaudit.value_namespace_prefix = name_space_prefix
            if(value_path == "modeNameStyle"):
                self.modenamestyle = value
                self.modenamestyle.value_namespace = name_space
                self.modenamestyle.value_namespace_prefix = name_space_prefix
            if(value_path == "moreBufferLines"):
                self.morebufferlines = value
                self.morebufferlines.value_namespace = name_space
                self.morebufferlines.value_namespace_prefix = name_space_prefix
            if(value_path == "multiPatternOperation"):
                self.multipatternoperation = value
                self.multipatternoperation.value_namespace = name_space
                self.multipatternoperation.value_namespace_prefix = name_space_prefix
            if(value_path == "newInsert"):
                self.newinsert = value
                self.newinsert.value_namespace = name_space
                self.newinsert.value_namespace_prefix = name_space_prefix
            if(value_path == "newLogout"):
                self.newlogout = value
                self.newlogout.value_namespace = name_space
                self.newlogout.value_namespace_prefix = name_space_prefix
            if(value_path == "noFollowIncompleteCommand"):
                self.nofollowincompletecommand = value
                self.nofollowincompletecommand.value_namespace = name_space
                self.nofollowincompletecommand.value_namespace_prefix = name_space_prefix
            if(value_path == "noMatchCompletionsFormat"):
                self.nomatchcompletionsformat = value
                self.nomatchcompletionsformat.value_namespace = name_space
                self.nomatchcompletionsformat.value_namespace_prefix = name_space_prefix
            if(value_path == "oldDetailsArg"):
                self.olddetailsarg = value
                self.olddetailsarg.value_namespace = name_space
                self.olddetailsarg.value_namespace_prefix = name_space_prefix
            if(value_path == "orderedShowConfig"):
                self.orderedshowconfig = value
                self.orderedshowconfig.value_namespace = name_space
                self.orderedshowconfig.value_namespace_prefix = name_space_prefix
            if(value_path == "pipeHelpMode"):
                self.pipehelpmode = value
                self.pipehelpmode.value_namespace = name_space
                self.pipehelpmode.value_namespace_prefix = name_space_prefix
            if(value_path == "possibleCompletionsFormat"):
                self.possiblecompletionsformat = value
                self.possiblecompletionsformat.value_namespace = name_space
                self.possiblecompletionsformat.value_namespace_prefix = name_space_prefix
            if(value_path == "prettifyStatsName"):
                self.prettifystatsname = value
                self.prettifystatsname.value_namespace = name_space
                self.prettifystatsname.value_namespace_prefix = name_space_prefix
            if(value_path == "prioritizeSubmodeCmds"):
                self.prioritizesubmodecmds = value
                self.prioritizesubmodecmds.value_namespace = name_space
                self.prioritizesubmodecmds.value_namespace_prefix = name_space_prefix
            if(value_path == "prompt1"):
                self.prompt1 = value
                self.prompt1.value_namespace = name_space
                self.prompt1.value_namespace_prefix = name_space_prefix
            if(value_path == "prompt2"):
                self.prompt2 = value
                self.prompt2.value_namespace = name_space
                self.prompt2.value_namespace_prefix = name_space_prefix
            if(value_path == "promptEnumLimit"):
                self.promptenumlimit = value
                self.promptenumlimit.value_namespace = name_space
                self.promptenumlimit.value_namespace_prefix = name_space_prefix
            if(value_path == "promptHostnameDelimiter"):
                self.prompthostnamedelimiter = value
                self.prompthostnamedelimiter.value_namespace = name_space
                self.prompthostnamedelimiter.value_namespace_prefix = name_space_prefix
            if(value_path == "promptSessionsCLI"):
                self.promptsessionscli = value
                self.promptsessionscli.value_namespace = name_space
                self.promptsessionscli.value_namespace_prefix = name_space_prefix
            if(value_path == "quickSshTeardown"):
                self.quicksshteardown = value
                self.quicksshteardown.value_namespace = name_space
                self.quicksshteardown.value_namespace_prefix = name_space_prefix
            if(value_path == "quoteStyle"):
                self.quotestyle = value
                self.quotestyle.value_namespace = name_space
                self.quotestyle.value_namespace_prefix = name_space_prefix
            if(value_path == "reallocateOperTrans"):
                self.reallocateopertrans = value
                self.reallocateopertrans.value_namespace = name_space
                self.reallocateopertrans.value_namespace_prefix = name_space_prefix
            if(value_path == "reconfirmHidden"):
                self.reconfirmhidden = value
                self.reconfirmhidden.value_namespace = name_space
                self.reconfirmhidden.value_namespace_prefix = name_space_prefix
            if(value_path == "reportInvalidCompletionInput"):
                self.reportinvalidcompletioninput = value
                self.reportinvalidcompletioninput.value_namespace = name_space
                self.reportinvalidcompletioninput.value_namespace_prefix = name_space_prefix
            if(value_path == "restrictedFileAccess"):
                self.restrictedfileaccess = value
                self.restrictedfileaccess.value_namespace = name_space
                self.restrictedfileaccess.value_namespace_prefix = name_space_prefix
            if(value_path == "restrictedFileRegexp"):
                self.restrictedfileregexp = value
                self.restrictedfileregexp.value_namespace = name_space
                self.restrictedfileregexp.value_namespace_prefix = name_space_prefix
            if(value_path == "rollbackAAA"):
                self.rollbackaaa = value
                self.rollbackaaa.value_namespace = name_space
                self.rollbackaaa.value_namespace_prefix = name_space_prefix
            if(value_path == "rollbackMax"):
                self.rollbackmax = value
                self.rollbackmax.value_namespace = name_space
                self.rollbackmax.value_namespace_prefix = name_space_prefix
            if(value_path == "rollbackNumbering"):
                self.rollbacknumbering = value
                self.rollbacknumbering.value_namespace = name_space
                self.rollbacknumbering.value_namespace_prefix = name_space_prefix
            if(value_path == "rollbackNumberingInitial"):
                self.rollbacknumberinginitial = value
                self.rollbacknumberinginitial.value_namespace = name_space
                self.rollbacknumberinginitial.value_namespace_prefix = name_space_prefix
            if(value_path == "safeScriptExecution"):
                self.safescriptexecution = value
                self.safescriptexecution.value_namespace = name_space
                self.safescriptexecution.value_namespace_prefix = name_space_prefix
            if(value_path == "showAllNs"):
                self.showallns = value
                self.showallns.value_namespace = name_space
                self.showallns.value_namespace_prefix = name_space_prefix
            if(value_path == "showAnnotations"):
                self.showannotations = value
                self.showannotations.value_namespace = name_space
                self.showannotations.value_namespace_prefix = name_space_prefix
            if(value_path == "showCommitProgress"):
                self.showcommitprogress = value
                self.showcommitprogress.value_namespace = name_space
                self.showcommitprogress.value_namespace_prefix = name_space_prefix
            if(value_path == "showDefaults"):
                self.showdefaults = value
                self.showdefaults.value_namespace = name_space
                self.showdefaults.value_namespace_prefix = name_space_prefix
            if(value_path == "showDescription"):
                self.showdescription = value
                self.showdescription.value_namespace = name_space
                self.showdescription.value_namespace_prefix = name_space_prefix
            if(value_path == "showEditors"):
                self.showeditors = value
                self.showeditors.value_namespace = name_space
                self.showeditors.value_namespace_prefix = name_space_prefix
            if(value_path == "showEmptyContainers"):
                self.showemptycontainers = value
                self.showemptycontainers.value_namespace = name_space
                self.showemptycontainers.value_namespace_prefix = name_space_prefix
            if(value_path == "showKeyName"):
                self.showkeyname = value
                self.showkeyname.value_namespace = name_space
                self.showkeyname.value_namespace_prefix = name_space_prefix
            if(value_path == "showLogDirectory"):
                self.showlogdirectory = value
                self.showlogdirectory.value_namespace = name_space
                self.showlogdirectory.value_namespace_prefix = name_space_prefix
            if(value_path == "showMatchBeforePossible"):
                self.showmatchbeforepossible = value
                self.showmatchbeforepossible.value_namespace = name_space
                self.showmatchbeforepossible.value_namespace_prefix = name_space_prefix
            if(value_path == "showNedErrorAsInfo"):
                self.shownederrorasinfo = value
                self.shownederrorasinfo.value_namespace = name_space
                self.shownederrorasinfo.value_namespace_prefix = name_space_prefix
            if(value_path == "showPipe"):
                self.showpipe = value
                self.showpipe.value_namespace = name_space
                self.showpipe.value_namespace_prefix = name_space_prefix
            if(value_path == "showPipeConfig"):
                self.showpipeconfig = value
                self.showpipeconfig.value_namespace = name_space
                self.showpipeconfig.value_namespace_prefix = name_space_prefix
            if(value_path == "showServiceMetaData"):
                self.showservicemetadata = value
                self.showservicemetadata.value_namespace = name_space
                self.showservicemetadata.value_namespace_prefix = name_space_prefix
            if(value_path == "showSubsystemMessages"):
                self.showsubsystemmessages = value
                self.showsubsystemmessages.value_namespace = name_space
                self.showsubsystemmessages.value_namespace_prefix = name_space_prefix
            if(value_path == "showTableLabelsIfMultiple"):
                self.showtablelabelsifmultiple = value
                self.showtablelabelsifmultiple.value_namespace = name_space
                self.showtablelabelsifmultiple.value_namespace_prefix = name_space_prefix
            if(value_path == "showTags"):
                self.showtags = value
                self.showtags.value_namespace = name_space
                self.showtags.value_namespace_prefix = name_space_prefix
            if(value_path == "singleElemPattern"):
                self.singleelempattern = value
                self.singleelempattern.value_namespace = name_space
                self.singleelempattern.value_namespace_prefix = name_space_prefix
            if(value_path == "smartRenameFiltering"):
                self.smartrenamefiltering = value
                self.smartrenamefiltering.value_namespace = name_space
                self.smartrenamefiltering.value_namespace_prefix = name_space_prefix
            if(value_path == "sortLocalCmds"):
                self.sortlocalcmds = value
                self.sortlocalcmds.value_namespace = name_space
                self.sortlocalcmds.value_namespace_prefix = name_space_prefix
            if(value_path == "sortShowElems"):
                self.sortshowelems = value
                self.sortshowelems.value_namespace = name_space
                self.sortshowelems.value_namespace_prefix = name_space_prefix
            if(value_path == "sortSubmodeCmds"):
                self.sortsubmodecmds = value
                self.sortsubmodecmds.value_namespace = name_space
                self.sortsubmodecmds.value_namespace_prefix = name_space_prefix
            if(value_path == "startupScriptNonInteractive"):
                self.startupscriptnoninteractive = value
                self.startupscriptnoninteractive.value_namespace = name_space
                self.startupscriptnoninteractive.value_namespace_prefix = name_space_prefix
            if(value_path == "stopLoadOnError"):
                self.stoploadonerror = value
                self.stoploadonerror.value_namespace = name_space
                self.stoploadonerror.value_namespace_prefix = name_space_prefix
            if(value_path == "strictRefsOnLoad"):
                self.strictrefsonload = value
                self.strictrefsonload.value_namespace = name_space
                self.strictrefsonload.value_namespace_prefix = name_space_prefix
            if(value_path == "style"):
                self.style = value
                self.style.value_namespace = name_space
                self.style.value_namespace_prefix = name_space_prefix
            if(value_path == "supportQuotedEOL"):
                self.supportquotedeol = value
                self.supportquotedeol.value_namespace = name_space
                self.supportquotedeol.value_namespace_prefix = name_space_prefix
            if(value_path == "suppressFastShow"):
                self.suppressfastshow = value
                self.suppressfastshow.value_namespace = name_space
                self.suppressfastshow.value_namespace_prefix = name_space_prefix
            if(value_path == "suppressNedErrors"):
                self.suppressnederrors = value
                self.suppressnederrors.value_namespace = name_space
                self.suppressnederrors.value_namespace_prefix = name_space_prefix
            if(value_path == "suppressRangeKeyword"):
                self.suppressrangekeyword = value
                self.suppressrangekeyword.value_namespace = name_space
                self.suppressrangekeyword.value_namespace_prefix = name_space_prefix
            if(value_path == "tabExtend"):
                self.tabextend = value
                self.tabextend.value_namespace = name_space
                self.tabextend.value_namespace_prefix = name_space_prefix
            if(value_path == "tableLabel"):
                self.tablelabel = value
                self.tablelabel.value_namespace = name_space
                self.tablelabel.value_namespace_prefix = name_space_prefix
            if(value_path == "tableLookAhead"):
                self.tablelookahead = value
                self.tablelookahead.value_namespace = name_space
                self.tablelookahead.value_namespace_prefix = name_space_prefix
            if(value_path == "tableOverflowTruncate"):
                self.tableoverflowtruncate = value
                self.tableoverflowtruncate.value_namespace = name_space
                self.tableoverflowtruncate.value_namespace_prefix = name_space_prefix
            if(value_path == "timezone"):
                self.timezone = value
                self.timezone.value_namespace = name_space
                self.timezone.value_namespace_prefix = name_space_prefix
            if(value_path == "topLevelCmdsInSubMode"):
                self.toplevelcmdsinsubmode = value
                self.toplevelcmdsinsubmode.value_namespace = name_space
                self.toplevelcmdsinsubmode.value_namespace_prefix = name_space_prefix
            if(value_path == "transactionCtrlCmds"):
                self.transactionctrlcmds = value
                self.transactionctrlcmds.value_namespace = name_space
                self.transactionctrlcmds.value_namespace_prefix = name_space_prefix
            if(value_path == "transactions"):
                self.transactions = value
                self.transactions.value_namespace = name_space
                self.transactions.value_namespace_prefix = name_space_prefix
            if(value_path == "trimDefaultSave"):
                self.trimdefaultsave = value
                self.trimdefaultsave.value_namespace = name_space
                self.trimdefaultsave.value_namespace_prefix = name_space_prefix
            if(value_path == "trimDefaultShow"):
                self.trimdefaultshow = value
                self.trimdefaultshow.value_namespace = name_space
                self.trimdefaultshow.value_namespace_prefix = name_space_prefix
            if(value_path == "unifiedHistory"):
                self.unifiedhistory = value
                self.unifiedhistory.value_namespace = name_space
                self.unifiedhistory.value_namespace_prefix = name_space_prefix
            if(value_path == "useDoubleDotRanges"):
                self.usedoubledotranges = value
                self.usedoubledotranges.value_namespace = name_space
                self.usedoubledotranges.value_namespace_prefix = name_space_prefix
            if(value_path == "useExposeNsPrefix"):
                self.useexposensprefix = value
                self.useexposensprefix.value_namespace = name_space
                self.useexposensprefix.value_namespace_prefix = name_space_prefix
            if(value_path == "useShortEnabled"):
                self.useshortenabled = value
                self.useshortenabled.value_namespace = name_space
                self.useshortenabled.value_namespace_prefix = name_space_prefix
            if(value_path == "utcOffset"):
                self.utcoffset = value
                self.utcoffset.value_namespace = name_space
                self.utcoffset.value_namespace_prefix = name_space_prefix
            if(value_path == "whoHistoryDateTimeFormat"):
                self.whohistorydatetimeformat = value
                self.whohistorydatetimeformat.value_namespace = name_space
                self.whohistorydatetimeformat.value_namespace_prefix = name_space_prefix
            if(value_path == "whoShowMode"):
                self.whoshowmode = value
                self.whoshowmode.value_namespace = name_space
                self.whoshowmode.value_namespace_prefix = name_space_prefix
            if(value_path == "withDefaults"):
                self.withdefaults = value
                self.withdefaults.value_namespace = name_space
                self.withdefaults.value_namespace_prefix = name_space_prefix
            if(value_path == "wrapInfo"):
                self.wrapinfo = value
                self.wrapinfo.value_namespace = name_space
                self.wrapinfo.value_namespace_prefix = name_space_prefix
            if(value_path == "wrapPrompt"):
                self.wrapprompt = value
                self.wrapprompt.value_namespace = name_space
                self.wrapprompt.value_namespace_prefix = name_space_prefix


    class Webui(Entity):
        """
        
        
        .. attribute:: absolutetimeout
        
        	
        	**type**\:  str
        
        	**default value**\: PT60M
        
        .. attribute:: allowsymlinks
        
        	
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: audit
        
        	
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: cacherefreshsecs
        
        	
        	**type**\:  int
        
        	**range:** 0..18446744073709551615 \| 0..18446744073709551615
        
        	**default value**\: 0
        
        .. attribute:: cgi
        
        	
        	**type**\:   :py:class:`Cgi <ydk.models.confd_dyncfg.Confdconfig.Webui.Cgi>`
        
        	**presence node**\: True
        
        .. attribute:: customdir
        
        	
        	**type**\:  str
        
        .. attribute:: customheaders
        
        	
        	**type**\:   :py:class:`Customheaders <ydk.models.confd_dyncfg.Confdconfig.Webui.Customheaders>`
        
        	**presence node**\: True
        
        .. attribute:: disableauth
        
        	
        	**type**\:   :py:class:`Disableauth <ydk.models.confd_dyncfg.Confdconfig.Webui.Disableauth>`
        
        	**presence node**\: True
        
        .. attribute:: docroot
        
        	
        	**type**\:  str
        
        .. attribute:: enabled
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: idletimeout
        
        	
        	**type**\:  str
        
        	**default value**\: PT30M
        
        .. attribute:: logindir
        
        	
        	**type**\:  str
        
        .. attribute:: matchhostname
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: maxrefentries
        
        	
        	**type**\:  int
        
        	**range:** 0..18446744073709551615 \| 0..18446744073709551615
        
        	**default value**\: 100
        
        .. attribute:: ratelimiting
        
        	
        	**type**\:  int
        
        	**range:** 0..18446744073709551615 \| 0..18446744073709551615
        
        	**default value**\: 1000000
        
        .. attribute:: servername
        
        	
        	**type**\:  str
        
        	**default value**\: localhost
        
        .. attribute:: transport
        
        	
        	**type**\:   :py:class:`Transport <ydk.models.confd_dyncfg.Confdconfig.Webui.Transport>`
        
        	**presence node**\: True
        
        .. attribute:: x_frame_options
        
        	
        	**type**\:   :py:class:`XFrameOptionstype <ydk.models.confd_dyncfg.XFrameOptionstype>`
        
        	**default value**\: DENY
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'confd_dyncfg'
        _revision = '2017-01-16'

        def __init__(self):
            super(Confdconfig.Webui, self).__init__()

            self.yang_name = "webui"
            self.yang_parent_name = "confdConfig"
            self.is_presence_container = True

            self.absolutetimeout = YLeaf(YType.str, "absoluteTimeout")

            self.allowsymlinks = YLeaf(YType.boolean, "allowSymlinks")

            self.audit = YLeaf(YType.boolean, "audit")

            self.cacherefreshsecs = YLeaf(YType.uint64, "cacheRefreshSecs")

            self.customdir = YLeaf(YType.str, "customDir")

            self.docroot = YLeaf(YType.str, "docroot")

            self.enabled = YLeaf(YType.boolean, "enabled")

            self.idletimeout = YLeaf(YType.str, "idleTimeout")

            self.logindir = YLeaf(YType.str, "loginDir")

            self.matchhostname = YLeaf(YType.boolean, "matchHostName")

            self.maxrefentries = YLeaf(YType.uint64, "maxRefEntries")

            self.ratelimiting = YLeaf(YType.uint64, "rateLimiting")

            self.servername = YLeaf(YType.str, "serverName")

            self.x_frame_options = YLeaf(YType.enumeration, "X-Frame-Options")

            self.cgi = None
            self._children_name_map["cgi"] = "cgi"
            self._children_yang_names.add("cgi")

            self.customheaders = None
            self._children_name_map["customheaders"] = "customHeaders"
            self._children_yang_names.add("customHeaders")

            self.disableauth = None
            self._children_name_map["disableauth"] = "disableAuth"
            self._children_yang_names.add("disableAuth")

            self.transport = None
            self._children_name_map["transport"] = "transport"
            self._children_yang_names.add("transport")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("absolutetimeout",
                            "allowsymlinks",
                            "audit",
                            "cacherefreshsecs",
                            "customdir",
                            "docroot",
                            "enabled",
                            "idletimeout",
                            "logindir",
                            "matchhostname",
                            "maxrefentries",
                            "ratelimiting",
                            "servername",
                            "x_frame_options") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Confdconfig.Webui, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Confdconfig.Webui, self).__setattr__(name, value)


        class Customheaders(Entity):
            """
            
            
            .. attribute:: header
            
            	
            	**type**\: list of    :py:class:`Header <ydk.models.confd_dyncfg.Confdconfig.Webui.Customheaders.Header>`
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'confd_dyncfg'
            _revision = '2017-01-16'

            def __init__(self):
                super(Confdconfig.Webui.Customheaders, self).__init__()

                self.yang_name = "customHeaders"
                self.yang_parent_name = "webui"
                self.is_presence_container = True

                self.header = YList(self)

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
                            super(Confdconfig.Webui.Customheaders, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Confdconfig.Webui.Customheaders, self).__setattr__(name, value)


            class Header(Entity):
                """
                
                
                .. attribute:: name  <key>
                
                	
                	**type**\:  str
                
                .. attribute:: value
                
                	
                	**type**\:  str
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'confd_dyncfg'
                _revision = '2017-01-16'

                def __init__(self):
                    super(Confdconfig.Webui.Customheaders.Header, self).__init__()

                    self.yang_name = "header"
                    self.yang_parent_name = "customHeaders"

                    self.name = YLeaf(YType.str, "name")

                    self.value = YLeaf(YType.str, "value")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("name",
                                    "value") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Confdconfig.Webui.Customheaders.Header, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Confdconfig.Webui.Customheaders.Header, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.name.is_set or
                        self.value.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.name.yfilter != YFilter.not_set or
                        self.value.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "header" + "[name='" + self.name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "confd_dyncfg:confdConfig/webui/customHeaders/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.name.get_name_leafdata())
                    if (self.value.is_set or self.value.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.value.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "name" or name == "value"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "name"):
                        self.name = value
                        self.name.value_namespace = name_space
                        self.name.value_namespace_prefix = name_space_prefix
                    if(value_path == "value"):
                        self.value = value
                        self.value.value_namespace = name_space
                        self.value.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.header:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.header:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "customHeaders" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "confd_dyncfg:confdConfig/webui/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "header"):
                    for c in self.header:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Confdconfig.Webui.Customheaders.Header()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.header.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "header"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class Disableauth(Entity):
            """
            
            
            .. attribute:: dir
            
            	
            	**type**\:  list of str
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'confd_dyncfg'
            _revision = '2017-01-16'

            def __init__(self):
                super(Confdconfig.Webui.Disableauth, self).__init__()

                self.yang_name = "disableAuth"
                self.yang_parent_name = "webui"
                self.is_presence_container = True

                self.dir = YLeafList(YType.str, "dir")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("dir") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Confdconfig.Webui.Disableauth, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Confdconfig.Webui.Disableauth, self).__setattr__(name, value)

            def has_data(self):
                for leaf in self.dir.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                return False

            def has_operation(self):
                for leaf in self.dir.getYLeafs():
                    if (leaf.is_set):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.dir.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "disableAuth" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "confd_dyncfg:confdConfig/webui/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                leaf_name_data.extend(self.dir.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "dir"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "dir"):
                    self.dir.append(value)


        class Transport(Entity):
            """
            
            
            .. attribute:: ssl
            
            	
            	**type**\:   :py:class:`Ssl <ydk.models.confd_dyncfg.Confdconfig.Webui.Transport.Ssl>`
            
            	**presence node**\: True
            
            .. attribute:: tcp
            
            	
            	**type**\:   :py:class:`Tcp <ydk.models.confd_dyncfg.Confdconfig.Webui.Transport.Tcp>`
            
            	**presence node**\: True
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'confd_dyncfg'
            _revision = '2017-01-16'

            def __init__(self):
                super(Confdconfig.Webui.Transport, self).__init__()

                self.yang_name = "transport"
                self.yang_parent_name = "webui"
                self.is_presence_container = True

                self.ssl = None
                self._children_name_map["ssl"] = "ssl"
                self._children_yang_names.add("ssl")

                self.tcp = None
                self._children_name_map["tcp"] = "tcp"
                self._children_yang_names.add("tcp")


            class Tcp(Entity):
                """
                
                
                .. attribute:: disablenonauthredirect
                
                	
                	**type**\:  bool
                
                	**default value**\: false
                
                .. attribute:: dscp
                
                	
                	**type**\:  int
                
                	**range:** 0..63
                
                .. attribute:: enabled
                
                	
                	**type**\:  bool
                
                	**default value**\: true
                
                .. attribute:: extraipports
                
                	
                	**type**\:  list of str
                
                .. attribute:: ip
                
                	
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                	**default value**\: 0.0.0.0
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                	**default value**\: 0.0.0.0
                
                
                ----
                .. attribute:: port
                
                	
                	**type**\:  int
                
                	**range:** 0..65535
                
                	**default value**\: 8008
                
                .. attribute:: redirect
                
                	
                	**type**\:  str
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'confd_dyncfg'
                _revision = '2017-01-16'

                def __init__(self):
                    super(Confdconfig.Webui.Transport.Tcp, self).__init__()

                    self.yang_name = "tcp"
                    self.yang_parent_name = "transport"
                    self.is_presence_container = True

                    self.disablenonauthredirect = YLeaf(YType.boolean, "disableNonAuthRedirect")

                    self.dscp = YLeaf(YType.uint8, "dscp")

                    self.enabled = YLeaf(YType.boolean, "enabled")

                    self.extraipports = YLeafList(YType.str, "extraIpPorts")

                    self.ip = YLeaf(YType.str, "ip")

                    self.port = YLeaf(YType.uint16, "port")

                    self.redirect = YLeaf(YType.str, "redirect")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("disablenonauthredirect",
                                    "dscp",
                                    "enabled",
                                    "extraipports",
                                    "ip",
                                    "port",
                                    "redirect") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Confdconfig.Webui.Transport.Tcp, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Confdconfig.Webui.Transport.Tcp, self).__setattr__(name, value)

                def has_data(self):
                    for leaf in self.extraipports.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    return (
                        self.disablenonauthredirect.is_set or
                        self.dscp.is_set or
                        self.enabled.is_set or
                        self.ip.is_set or
                        self.port.is_set or
                        self.redirect.is_set)

                def has_operation(self):
                    for leaf in self.extraipports.getYLeafs():
                        if (leaf.is_set):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.disablenonauthredirect.yfilter != YFilter.not_set or
                        self.dscp.yfilter != YFilter.not_set or
                        self.enabled.yfilter != YFilter.not_set or
                        self.extraipports.yfilter != YFilter.not_set or
                        self.ip.yfilter != YFilter.not_set or
                        self.port.yfilter != YFilter.not_set or
                        self.redirect.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "tcp" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "confd_dyncfg:confdConfig/webui/transport/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.disablenonauthredirect.is_set or self.disablenonauthredirect.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.disablenonauthredirect.get_name_leafdata())
                    if (self.dscp.is_set or self.dscp.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.dscp.get_name_leafdata())
                    if (self.enabled.is_set or self.enabled.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.enabled.get_name_leafdata())
                    if (self.ip.is_set or self.ip.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ip.get_name_leafdata())
                    if (self.port.is_set or self.port.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.port.get_name_leafdata())
                    if (self.redirect.is_set or self.redirect.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.redirect.get_name_leafdata())

                    leaf_name_data.extend(self.extraipports.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "disableNonAuthRedirect" or name == "dscp" or name == "enabled" or name == "extraIpPorts" or name == "ip" or name == "port" or name == "redirect"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "disableNonAuthRedirect"):
                        self.disablenonauthredirect = value
                        self.disablenonauthredirect.value_namespace = name_space
                        self.disablenonauthredirect.value_namespace_prefix = name_space_prefix
                    if(value_path == "dscp"):
                        self.dscp = value
                        self.dscp.value_namespace = name_space
                        self.dscp.value_namespace_prefix = name_space_prefix
                    if(value_path == "enabled"):
                        self.enabled = value
                        self.enabled.value_namespace = name_space
                        self.enabled.value_namespace_prefix = name_space_prefix
                    if(value_path == "extraIpPorts"):
                        self.extraipports.append(value)
                    if(value_path == "ip"):
                        self.ip = value
                        self.ip.value_namespace = name_space
                        self.ip.value_namespace_prefix = name_space_prefix
                    if(value_path == "port"):
                        self.port = value
                        self.port.value_namespace = name_space
                        self.port.value_namespace_prefix = name_space_prefix
                    if(value_path == "redirect"):
                        self.redirect = value
                        self.redirect.value_namespace = name_space
                        self.redirect.value_namespace_prefix = name_space_prefix


            class Ssl(Entity):
                """
                
                
                .. attribute:: cacertfile
                
                	
                	**type**\:  str
                
                .. attribute:: certfile
                
                	
                	**type**\:  str
                
                .. attribute:: ciphers
                
                	
                	**type**\:  str
                
                	**default value**\: DEFAULT
                
                .. attribute:: depth
                
                	
                	**type**\:  int
                
                	**range:** 0..18446744073709551615 \| 0..18446744073709551615
                
                	**default value**\: 1
                
                .. attribute:: disablenonauthredirect
                
                	
                	**type**\:  bool
                
                	**default value**\: false
                
                .. attribute:: dscp
                
                	
                	**type**\:  int
                
                	**range:** 0..63
                
                .. attribute:: enabled
                
                	
                	**type**\:  bool
                
                	**default value**\: false
                
                .. attribute:: extraipports
                
                	
                	**type**\:  list of str
                
                .. attribute:: ip
                
                	
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                	**default value**\: 0.0.0.0
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                	**default value**\: 0.0.0.0
                
                
                ----
                .. attribute:: keyfile
                
                	
                	**type**\:  str
                
                .. attribute:: port
                
                	
                	**type**\:  int
                
                	**range:** 0..65535
                
                	**default value**\: 8888
                
                .. attribute:: protocols
                
                	
                	**type**\:  str
                
                	**default value**\: DEFAULT
                
                .. attribute:: redirect
                
                	
                	**type**\:  str
                
                .. attribute:: verify
                
                	
                	**type**\:  int
                
                	**range:** 1..3
                
                	**default value**\: 1
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'confd_dyncfg'
                _revision = '2017-01-16'

                def __init__(self):
                    super(Confdconfig.Webui.Transport.Ssl, self).__init__()

                    self.yang_name = "ssl"
                    self.yang_parent_name = "transport"
                    self.is_presence_container = True

                    self.cacertfile = YLeaf(YType.str, "caCertFile")

                    self.certfile = YLeaf(YType.str, "certFile")

                    self.ciphers = YLeaf(YType.str, "ciphers")

                    self.depth = YLeaf(YType.uint64, "depth")

                    self.disablenonauthredirect = YLeaf(YType.boolean, "disableNonAuthRedirect")

                    self.dscp = YLeaf(YType.uint8, "dscp")

                    self.enabled = YLeaf(YType.boolean, "enabled")

                    self.extraipports = YLeafList(YType.str, "extraIpPorts")

                    self.ip = YLeaf(YType.str, "ip")

                    self.keyfile = YLeaf(YType.str, "keyFile")

                    self.port = YLeaf(YType.uint16, "port")

                    self.protocols = YLeaf(YType.str, "protocols")

                    self.redirect = YLeaf(YType.str, "redirect")

                    self.verify = YLeaf(YType.uint32, "verify")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("cacertfile",
                                    "certfile",
                                    "ciphers",
                                    "depth",
                                    "disablenonauthredirect",
                                    "dscp",
                                    "enabled",
                                    "extraipports",
                                    "ip",
                                    "keyfile",
                                    "port",
                                    "protocols",
                                    "redirect",
                                    "verify") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Confdconfig.Webui.Transport.Ssl, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Confdconfig.Webui.Transport.Ssl, self).__setattr__(name, value)

                def has_data(self):
                    for leaf in self.extraipports.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    return (
                        self.cacertfile.is_set or
                        self.certfile.is_set or
                        self.ciphers.is_set or
                        self.depth.is_set or
                        self.disablenonauthredirect.is_set or
                        self.dscp.is_set or
                        self.enabled.is_set or
                        self.ip.is_set or
                        self.keyfile.is_set or
                        self.port.is_set or
                        self.protocols.is_set or
                        self.redirect.is_set or
                        self.verify.is_set)

                def has_operation(self):
                    for leaf in self.extraipports.getYLeafs():
                        if (leaf.is_set):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.cacertfile.yfilter != YFilter.not_set or
                        self.certfile.yfilter != YFilter.not_set or
                        self.ciphers.yfilter != YFilter.not_set or
                        self.depth.yfilter != YFilter.not_set or
                        self.disablenonauthredirect.yfilter != YFilter.not_set or
                        self.dscp.yfilter != YFilter.not_set or
                        self.enabled.yfilter != YFilter.not_set or
                        self.extraipports.yfilter != YFilter.not_set or
                        self.ip.yfilter != YFilter.not_set or
                        self.keyfile.yfilter != YFilter.not_set or
                        self.port.yfilter != YFilter.not_set or
                        self.protocols.yfilter != YFilter.not_set or
                        self.redirect.yfilter != YFilter.not_set or
                        self.verify.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "ssl" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "confd_dyncfg:confdConfig/webui/transport/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.cacertfile.is_set or self.cacertfile.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.cacertfile.get_name_leafdata())
                    if (self.certfile.is_set or self.certfile.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.certfile.get_name_leafdata())
                    if (self.ciphers.is_set or self.ciphers.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ciphers.get_name_leafdata())
                    if (self.depth.is_set or self.depth.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.depth.get_name_leafdata())
                    if (self.disablenonauthredirect.is_set or self.disablenonauthredirect.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.disablenonauthredirect.get_name_leafdata())
                    if (self.dscp.is_set or self.dscp.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.dscp.get_name_leafdata())
                    if (self.enabled.is_set or self.enabled.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.enabled.get_name_leafdata())
                    if (self.ip.is_set or self.ip.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ip.get_name_leafdata())
                    if (self.keyfile.is_set or self.keyfile.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.keyfile.get_name_leafdata())
                    if (self.port.is_set or self.port.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.port.get_name_leafdata())
                    if (self.protocols.is_set or self.protocols.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.protocols.get_name_leafdata())
                    if (self.redirect.is_set or self.redirect.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.redirect.get_name_leafdata())
                    if (self.verify.is_set or self.verify.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.verify.get_name_leafdata())

                    leaf_name_data.extend(self.extraipports.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "caCertFile" or name == "certFile" or name == "ciphers" or name == "depth" or name == "disableNonAuthRedirect" or name == "dscp" or name == "enabled" or name == "extraIpPorts" or name == "ip" or name == "keyFile" or name == "port" or name == "protocols" or name == "redirect" or name == "verify"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "caCertFile"):
                        self.cacertfile = value
                        self.cacertfile.value_namespace = name_space
                        self.cacertfile.value_namespace_prefix = name_space_prefix
                    if(value_path == "certFile"):
                        self.certfile = value
                        self.certfile.value_namespace = name_space
                        self.certfile.value_namespace_prefix = name_space_prefix
                    if(value_path == "ciphers"):
                        self.ciphers = value
                        self.ciphers.value_namespace = name_space
                        self.ciphers.value_namespace_prefix = name_space_prefix
                    if(value_path == "depth"):
                        self.depth = value
                        self.depth.value_namespace = name_space
                        self.depth.value_namespace_prefix = name_space_prefix
                    if(value_path == "disableNonAuthRedirect"):
                        self.disablenonauthredirect = value
                        self.disablenonauthredirect.value_namespace = name_space
                        self.disablenonauthredirect.value_namespace_prefix = name_space_prefix
                    if(value_path == "dscp"):
                        self.dscp = value
                        self.dscp.value_namespace = name_space
                        self.dscp.value_namespace_prefix = name_space_prefix
                    if(value_path == "enabled"):
                        self.enabled = value
                        self.enabled.value_namespace = name_space
                        self.enabled.value_namespace_prefix = name_space_prefix
                    if(value_path == "extraIpPorts"):
                        self.extraipports.append(value)
                    if(value_path == "ip"):
                        self.ip = value
                        self.ip.value_namespace = name_space
                        self.ip.value_namespace_prefix = name_space_prefix
                    if(value_path == "keyFile"):
                        self.keyfile = value
                        self.keyfile.value_namespace = name_space
                        self.keyfile.value_namespace_prefix = name_space_prefix
                    if(value_path == "port"):
                        self.port = value
                        self.port.value_namespace = name_space
                        self.port.value_namespace_prefix = name_space_prefix
                    if(value_path == "protocols"):
                        self.protocols = value
                        self.protocols.value_namespace = name_space
                        self.protocols.value_namespace_prefix = name_space_prefix
                    if(value_path == "redirect"):
                        self.redirect = value
                        self.redirect.value_namespace = name_space
                        self.redirect.value_namespace_prefix = name_space_prefix
                    if(value_path == "verify"):
                        self.verify = value
                        self.verify.value_namespace = name_space
                        self.verify.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    (self.ssl is not None) or
                    (self.tcp is not None))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.ssl is not None and self.ssl.has_operation()) or
                    (self.tcp is not None and self.tcp.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "transport" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "confd_dyncfg:confdConfig/webui/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "ssl"):
                    if (self.ssl is None):
                        self.ssl = Confdconfig.Webui.Transport.Ssl()
                        self.ssl.parent = self
                        self._children_name_map["ssl"] = "ssl"
                    return self.ssl

                if (child_yang_name == "tcp"):
                    if (self.tcp is None):
                        self.tcp = Confdconfig.Webui.Transport.Tcp()
                        self.tcp.parent = self
                        self._children_name_map["tcp"] = "tcp"
                    return self.tcp

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ssl" or name == "tcp"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class Cgi(Entity):
            """
            
            
            .. attribute:: dir
            
            	
            	**type**\:  str
            
            	**default value**\: cgi-bin
            
            .. attribute:: enabled
            
            	
            	**type**\:  bool
            
            	**default value**\: false
            
            .. attribute:: maxrequestlength
            
            	
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: php
            
            	
            	**type**\:   :py:class:`Php <ydk.models.confd_dyncfg.Confdconfig.Webui.Cgi.Php>`
            
            	**presence node**\: True
            
            .. attribute:: requestfilter
            
            	
            	**type**\:  str
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'confd_dyncfg'
            _revision = '2017-01-16'

            def __init__(self):
                super(Confdconfig.Webui.Cgi, self).__init__()

                self.yang_name = "cgi"
                self.yang_parent_name = "webui"
                self.is_presence_container = True

                self.dir = YLeaf(YType.str, "dir")

                self.enabled = YLeaf(YType.boolean, "enabled")

                self.maxrequestlength = YLeaf(YType.uint16, "maxRequestLength")

                self.requestfilter = YLeaf(YType.str, "requestFilter")

                self.php = None
                self._children_name_map["php"] = "php"
                self._children_yang_names.add("php")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("dir",
                                "enabled",
                                "maxrequestlength",
                                "requestfilter") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Confdconfig.Webui.Cgi, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Confdconfig.Webui.Cgi, self).__setattr__(name, value)


            class Php(Entity):
                """
                
                
                .. attribute:: enabled
                
                	
                	**type**\:  bool
                
                	**default value**\: false
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'confd_dyncfg'
                _revision = '2017-01-16'

                def __init__(self):
                    super(Confdconfig.Webui.Cgi.Php, self).__init__()

                    self.yang_name = "php"
                    self.yang_parent_name = "cgi"
                    self.is_presence_container = True

                    self.enabled = YLeaf(YType.boolean, "enabled")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("enabled") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Confdconfig.Webui.Cgi.Php, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Confdconfig.Webui.Cgi.Php, self).__setattr__(name, value)

                def has_data(self):
                    return self.enabled.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.enabled.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "php" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "confd_dyncfg:confdConfig/webui/cgi/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.enabled.is_set or self.enabled.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.enabled.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "enabled"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "enabled"):
                        self.enabled = value
                        self.enabled.value_namespace = name_space
                        self.enabled.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.dir.is_set or
                    self.enabled.is_set or
                    self.maxrequestlength.is_set or
                    self.requestfilter.is_set or
                    (self.php is not None))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.dir.yfilter != YFilter.not_set or
                    self.enabled.yfilter != YFilter.not_set or
                    self.maxrequestlength.yfilter != YFilter.not_set or
                    self.requestfilter.yfilter != YFilter.not_set or
                    (self.php is not None and self.php.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cgi" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "confd_dyncfg:confdConfig/webui/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.dir.is_set or self.dir.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dir.get_name_leafdata())
                if (self.enabled.is_set or self.enabled.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.enabled.get_name_leafdata())
                if (self.maxrequestlength.is_set or self.maxrequestlength.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.maxrequestlength.get_name_leafdata())
                if (self.requestfilter.is_set or self.requestfilter.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.requestfilter.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "php"):
                    if (self.php is None):
                        self.php = Confdconfig.Webui.Cgi.Php()
                        self.php.parent = self
                        self._children_name_map["php"] = "php"
                    return self.php

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "php" or name == "dir" or name == "enabled" or name == "maxRequestLength" or name == "requestFilter"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "dir"):
                    self.dir = value
                    self.dir.value_namespace = name_space
                    self.dir.value_namespace_prefix = name_space_prefix
                if(value_path == "enabled"):
                    self.enabled = value
                    self.enabled.value_namespace = name_space
                    self.enabled.value_namespace_prefix = name_space_prefix
                if(value_path == "maxRequestLength"):
                    self.maxrequestlength = value
                    self.maxrequestlength.value_namespace = name_space
                    self.maxrequestlength.value_namespace_prefix = name_space_prefix
                if(value_path == "requestFilter"):
                    self.requestfilter = value
                    self.requestfilter.value_namespace = name_space
                    self.requestfilter.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (
                self.absolutetimeout.is_set or
                self.allowsymlinks.is_set or
                self.audit.is_set or
                self.cacherefreshsecs.is_set or
                self.customdir.is_set or
                self.docroot.is_set or
                self.enabled.is_set or
                self.idletimeout.is_set or
                self.logindir.is_set or
                self.matchhostname.is_set or
                self.maxrefentries.is_set or
                self.ratelimiting.is_set or
                self.servername.is_set or
                self.x_frame_options.is_set or
                (self.cgi is not None) or
                (self.customheaders is not None) or
                (self.disableauth is not None) or
                (self.transport is not None))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.absolutetimeout.yfilter != YFilter.not_set or
                self.allowsymlinks.yfilter != YFilter.not_set or
                self.audit.yfilter != YFilter.not_set or
                self.cacherefreshsecs.yfilter != YFilter.not_set or
                self.customdir.yfilter != YFilter.not_set or
                self.docroot.yfilter != YFilter.not_set or
                self.enabled.yfilter != YFilter.not_set or
                self.idletimeout.yfilter != YFilter.not_set or
                self.logindir.yfilter != YFilter.not_set or
                self.matchhostname.yfilter != YFilter.not_set or
                self.maxrefentries.yfilter != YFilter.not_set or
                self.ratelimiting.yfilter != YFilter.not_set or
                self.servername.yfilter != YFilter.not_set or
                self.x_frame_options.yfilter != YFilter.not_set or
                (self.cgi is not None and self.cgi.has_operation()) or
                (self.customheaders is not None and self.customheaders.has_operation()) or
                (self.disableauth is not None and self.disableauth.has_operation()) or
                (self.transport is not None and self.transport.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "webui" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "confd_dyncfg:confdConfig/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.absolutetimeout.is_set or self.absolutetimeout.yfilter != YFilter.not_set):
                leaf_name_data.append(self.absolutetimeout.get_name_leafdata())
            if (self.allowsymlinks.is_set or self.allowsymlinks.yfilter != YFilter.not_set):
                leaf_name_data.append(self.allowsymlinks.get_name_leafdata())
            if (self.audit.is_set or self.audit.yfilter != YFilter.not_set):
                leaf_name_data.append(self.audit.get_name_leafdata())
            if (self.cacherefreshsecs.is_set or self.cacherefreshsecs.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cacherefreshsecs.get_name_leafdata())
            if (self.customdir.is_set or self.customdir.yfilter != YFilter.not_set):
                leaf_name_data.append(self.customdir.get_name_leafdata())
            if (self.docroot.is_set or self.docroot.yfilter != YFilter.not_set):
                leaf_name_data.append(self.docroot.get_name_leafdata())
            if (self.enabled.is_set or self.enabled.yfilter != YFilter.not_set):
                leaf_name_data.append(self.enabled.get_name_leafdata())
            if (self.idletimeout.is_set or self.idletimeout.yfilter != YFilter.not_set):
                leaf_name_data.append(self.idletimeout.get_name_leafdata())
            if (self.logindir.is_set or self.logindir.yfilter != YFilter.not_set):
                leaf_name_data.append(self.logindir.get_name_leafdata())
            if (self.matchhostname.is_set or self.matchhostname.yfilter != YFilter.not_set):
                leaf_name_data.append(self.matchhostname.get_name_leafdata())
            if (self.maxrefentries.is_set or self.maxrefentries.yfilter != YFilter.not_set):
                leaf_name_data.append(self.maxrefentries.get_name_leafdata())
            if (self.ratelimiting.is_set or self.ratelimiting.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ratelimiting.get_name_leafdata())
            if (self.servername.is_set or self.servername.yfilter != YFilter.not_set):
                leaf_name_data.append(self.servername.get_name_leafdata())
            if (self.x_frame_options.is_set or self.x_frame_options.yfilter != YFilter.not_set):
                leaf_name_data.append(self.x_frame_options.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cgi"):
                if (self.cgi is None):
                    self.cgi = Confdconfig.Webui.Cgi()
                    self.cgi.parent = self
                    self._children_name_map["cgi"] = "cgi"
                return self.cgi

            if (child_yang_name == "customHeaders"):
                if (self.customheaders is None):
                    self.customheaders = Confdconfig.Webui.Customheaders()
                    self.customheaders.parent = self
                    self._children_name_map["customheaders"] = "customHeaders"
                return self.customheaders

            if (child_yang_name == "disableAuth"):
                if (self.disableauth is None):
                    self.disableauth = Confdconfig.Webui.Disableauth()
                    self.disableauth.parent = self
                    self._children_name_map["disableauth"] = "disableAuth"
                return self.disableauth

            if (child_yang_name == "transport"):
                if (self.transport is None):
                    self.transport = Confdconfig.Webui.Transport()
                    self.transport.parent = self
                    self._children_name_map["transport"] = "transport"
                return self.transport

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cgi" or name == "customHeaders" or name == "disableAuth" or name == "transport" or name == "absoluteTimeout" or name == "allowSymlinks" or name == "audit" or name == "cacheRefreshSecs" or name == "customDir" or name == "docroot" or name == "enabled" or name == "idleTimeout" or name == "loginDir" or name == "matchHostName" or name == "maxRefEntries" or name == "rateLimiting" or name == "serverName" or name == "X-Frame-Options"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "absoluteTimeout"):
                self.absolutetimeout = value
                self.absolutetimeout.value_namespace = name_space
                self.absolutetimeout.value_namespace_prefix = name_space_prefix
            if(value_path == "allowSymlinks"):
                self.allowsymlinks = value
                self.allowsymlinks.value_namespace = name_space
                self.allowsymlinks.value_namespace_prefix = name_space_prefix
            if(value_path == "audit"):
                self.audit = value
                self.audit.value_namespace = name_space
                self.audit.value_namespace_prefix = name_space_prefix
            if(value_path == "cacheRefreshSecs"):
                self.cacherefreshsecs = value
                self.cacherefreshsecs.value_namespace = name_space
                self.cacherefreshsecs.value_namespace_prefix = name_space_prefix
            if(value_path == "customDir"):
                self.customdir = value
                self.customdir.value_namespace = name_space
                self.customdir.value_namespace_prefix = name_space_prefix
            if(value_path == "docroot"):
                self.docroot = value
                self.docroot.value_namespace = name_space
                self.docroot.value_namespace_prefix = name_space_prefix
            if(value_path == "enabled"):
                self.enabled = value
                self.enabled.value_namespace = name_space
                self.enabled.value_namespace_prefix = name_space_prefix
            if(value_path == "idleTimeout"):
                self.idletimeout = value
                self.idletimeout.value_namespace = name_space
                self.idletimeout.value_namespace_prefix = name_space_prefix
            if(value_path == "loginDir"):
                self.logindir = value
                self.logindir.value_namespace = name_space
                self.logindir.value_namespace_prefix = name_space_prefix
            if(value_path == "matchHostName"):
                self.matchhostname = value
                self.matchhostname.value_namespace = name_space
                self.matchhostname.value_namespace_prefix = name_space_prefix
            if(value_path == "maxRefEntries"):
                self.maxrefentries = value
                self.maxrefentries.value_namespace = name_space
                self.maxrefentries.value_namespace_prefix = name_space_prefix
            if(value_path == "rateLimiting"):
                self.ratelimiting = value
                self.ratelimiting.value_namespace = name_space
                self.ratelimiting.value_namespace_prefix = name_space_prefix
            if(value_path == "serverName"):
                self.servername = value
                self.servername.value_namespace = name_space
                self.servername.value_namespace_prefix = name_space_prefix
            if(value_path == "X-Frame-Options"):
                self.x_frame_options = value
                self.x_frame_options.value_namespace = name_space
                self.x_frame_options.value_namespace_prefix = name_space_prefix


    class Rest(Entity):
        """
        
        
        .. attribute:: customheaders
        
        	
        	**type**\:   :py:class:`Customheaders <ydk.models.confd_dyncfg.Confdconfig.Rest.Customheaders>`
        
        	**presence node**\: True
        
        .. attribute:: enabled
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: showhidden
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'confd_dyncfg'
        _revision = '2017-01-16'

        def __init__(self):
            super(Confdconfig.Rest, self).__init__()

            self.yang_name = "rest"
            self.yang_parent_name = "confdConfig"
            self.is_presence_container = True

            self.enabled = YLeaf(YType.boolean, "enabled")

            self.showhidden = YLeaf(YType.boolean, "showHidden")

            self.customheaders = None
            self._children_name_map["customheaders"] = "customHeaders"
            self._children_yang_names.add("customHeaders")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("enabled",
                            "showhidden") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Confdconfig.Rest, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Confdconfig.Rest, self).__setattr__(name, value)


        class Customheaders(Entity):
            """
            
            
            .. attribute:: header
            
            	
            	**type**\: list of    :py:class:`Header <ydk.models.confd_dyncfg.Confdconfig.Rest.Customheaders.Header>`
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'confd_dyncfg'
            _revision = '2017-01-16'

            def __init__(self):
                super(Confdconfig.Rest.Customheaders, self).__init__()

                self.yang_name = "customHeaders"
                self.yang_parent_name = "rest"
                self.is_presence_container = True

                self.header = YList(self)

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
                            super(Confdconfig.Rest.Customheaders, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Confdconfig.Rest.Customheaders, self).__setattr__(name, value)


            class Header(Entity):
                """
                
                
                .. attribute:: name  <key>
                
                	
                	**type**\:  str
                
                .. attribute:: value
                
                	
                	**type**\:  str
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'confd_dyncfg'
                _revision = '2017-01-16'

                def __init__(self):
                    super(Confdconfig.Rest.Customheaders.Header, self).__init__()

                    self.yang_name = "header"
                    self.yang_parent_name = "customHeaders"

                    self.name = YLeaf(YType.str, "name")

                    self.value = YLeaf(YType.str, "value")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("name",
                                    "value") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Confdconfig.Rest.Customheaders.Header, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Confdconfig.Rest.Customheaders.Header, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.name.is_set or
                        self.value.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.name.yfilter != YFilter.not_set or
                        self.value.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "header" + "[name='" + self.name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "confd_dyncfg:confdConfig/rest/customHeaders/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.name.get_name_leafdata())
                    if (self.value.is_set or self.value.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.value.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "name" or name == "value"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "name"):
                        self.name = value
                        self.name.value_namespace = name_space
                        self.name.value_namespace_prefix = name_space_prefix
                    if(value_path == "value"):
                        self.value = value
                        self.value.value_namespace = name_space
                        self.value.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.header:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.header:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "customHeaders" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "confd_dyncfg:confdConfig/rest/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "header"):
                    for c in self.header:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Confdconfig.Rest.Customheaders.Header()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.header.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "header"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                self.enabled.is_set or
                self.showhidden.is_set or
                (self.customheaders is not None))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.enabled.yfilter != YFilter.not_set or
                self.showhidden.yfilter != YFilter.not_set or
                (self.customheaders is not None and self.customheaders.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "rest" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "confd_dyncfg:confdConfig/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.enabled.is_set or self.enabled.yfilter != YFilter.not_set):
                leaf_name_data.append(self.enabled.get_name_leafdata())
            if (self.showhidden.is_set or self.showhidden.yfilter != YFilter.not_set):
                leaf_name_data.append(self.showhidden.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "customHeaders"):
                if (self.customheaders is None):
                    self.customheaders = Confdconfig.Rest.Customheaders()
                    self.customheaders.parent = self
                    self._children_name_map["customheaders"] = "customHeaders"
                return self.customheaders

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "customHeaders" or name == "enabled" or name == "showHidden"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "enabled"):
                self.enabled = value
                self.enabled.value_namespace = name_space
                self.enabled.value_namespace_prefix = name_space_prefix
            if(value_path == "showHidden"):
                self.showhidden = value
                self.showhidden.value_namespace = name_space
                self.showhidden.value_namespace_prefix = name_space_prefix


    class Restconf(Entity):
        """
        
        
        .. attribute:: enabled
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: rootresource
        
        	
        	**type**\:  str
        
        	**default value**\: restconf
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'confd_dyncfg'
        _revision = '2017-01-16'

        def __init__(self):
            super(Confdconfig.Restconf, self).__init__()

            self.yang_name = "restconf"
            self.yang_parent_name = "confdConfig"
            self.is_presence_container = True

            self.enabled = YLeaf(YType.boolean, "enabled")

            self.rootresource = YLeaf(YType.str, "rootResource")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("enabled",
                            "rootresource") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Confdconfig.Restconf, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Confdconfig.Restconf, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.enabled.is_set or
                self.rootresource.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.enabled.yfilter != YFilter.not_set or
                self.rootresource.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "restconf" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "confd_dyncfg:confdConfig/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.enabled.is_set or self.enabled.yfilter != YFilter.not_set):
                leaf_name_data.append(self.enabled.get_name_leafdata())
            if (self.rootresource.is_set or self.rootresource.yfilter != YFilter.not_set):
                leaf_name_data.append(self.rootresource.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "enabled" or name == "rootResource"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "enabled"):
                self.enabled = value
                self.enabled.value_namespace = name_space
                self.enabled.value_namespace_prefix = name_space_prefix
            if(value_path == "rootResource"):
                self.rootresource = value
                self.rootresource.value_namespace = name_space
                self.rootresource.value_namespace_prefix = name_space_prefix


    class Proxyforwarding(Entity):
        """
        
        
        .. attribute:: autologin
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: proxy
        
        	
        	**type**\: list of    :py:class:`Proxy <ydk.models.confd_dyncfg.Confdconfig.Proxyforwarding.Proxy>`
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'confd_dyncfg'
        _revision = '2017-01-16'

        def __init__(self):
            super(Confdconfig.Proxyforwarding, self).__init__()

            self.yang_name = "proxyForwarding"
            self.yang_parent_name = "confdConfig"
            self.is_presence_container = True

            self.autologin = YLeaf(YType.boolean, "autoLogin")

            self.proxy = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("autologin") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Confdconfig.Proxyforwarding, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Confdconfig.Proxyforwarding, self).__setattr__(name, value)


        class Proxy(Entity):
            """
            
            
            .. attribute:: target  <key>
            
            	
            	**type**\:  str
            
            .. attribute:: address
            
            	
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**mandatory**\: True
            
            
            ----
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            	**mandatory**\: True
            
            
            ----
            
            ----
            	**type**\:  str
            
            	**pattern:** ((([a\-zA\-Z0\-9\_]([a\-zA\-Z0\-9\\\-\_]){0,61})?[a\-zA\-Z0\-9]\\.)\*([a\-zA\-Z0\-9\_]([a\-zA\-Z0\-9\\\-\_]){0,61})?[a\-zA\-Z0\-9]\\.?)\|\\.
            
            	**mandatory**\: True
            
            
            ----
            .. attribute:: cli
            
            	
            	**type**\:   :py:class:`Cli <ydk.models.confd_dyncfg.Confdconfig.Proxyforwarding.Proxy.Cli>`
            
            	**presence node**\: True
            
            .. attribute:: netconf
            
            	
            	**type**\:   :py:class:`Netconf <ydk.models.confd_dyncfg.Confdconfig.Proxyforwarding.Proxy.Netconf>`
            
            	**presence node**\: True
            
            

            """

            _prefix = 'confd_dyncfg'
            _revision = '2017-01-16'

            def __init__(self):
                super(Confdconfig.Proxyforwarding.Proxy, self).__init__()

                self.yang_name = "proxy"
                self.yang_parent_name = "proxyForwarding"

                self.target = YLeaf(YType.str, "target")

                self.address = YLeaf(YType.str, "address")

                self.cli = None
                self._children_name_map["cli"] = "cli"
                self._children_yang_names.add("cli")

                self.netconf = None
                self._children_name_map["netconf"] = "netconf"
                self._children_yang_names.add("netconf")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("target",
                                "address") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Confdconfig.Proxyforwarding.Proxy, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Confdconfig.Proxyforwarding.Proxy, self).__setattr__(name, value)


            class Netconf(Entity):
                """
                
                
                .. attribute:: ssh
                
                	
                	**type**\:   :py:class:`Ssh <ydk.models.confd_dyncfg.Confdconfig.Proxyforwarding.Proxy.Netconf.Ssh>`
                
                .. attribute:: tcp
                
                	
                	**type**\:   :py:class:`Tcp <ydk.models.confd_dyncfg.Confdconfig.Proxyforwarding.Proxy.Netconf.Tcp>`
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'confd_dyncfg'
                _revision = '2017-01-16'

                def __init__(self):
                    super(Confdconfig.Proxyforwarding.Proxy.Netconf, self).__init__()

                    self.yang_name = "netconf"
                    self.yang_parent_name = "proxy"
                    self.is_presence_container = True

                    self.ssh = Confdconfig.Proxyforwarding.Proxy.Netconf.Ssh()
                    self.ssh.parent = self
                    self._children_name_map["ssh"] = "ssh"
                    self._children_yang_names.add("ssh")

                    self.tcp = Confdconfig.Proxyforwarding.Proxy.Netconf.Tcp()
                    self.tcp.parent = self
                    self._children_name_map["tcp"] = "tcp"
                    self._children_yang_names.add("tcp")


                class Ssh(Entity):
                    """
                    
                    
                    .. attribute:: port
                    
                    	
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    	**default value**\: 2022
                    
                    

                    """

                    _prefix = 'confd_dyncfg'
                    _revision = '2017-01-16'

                    def __init__(self):
                        super(Confdconfig.Proxyforwarding.Proxy.Netconf.Ssh, self).__init__()

                        self.yang_name = "ssh"
                        self.yang_parent_name = "netconf"

                        self.port = YLeaf(YType.uint16, "port")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("port") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Confdconfig.Proxyforwarding.Proxy.Netconf.Ssh, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Confdconfig.Proxyforwarding.Proxy.Netconf.Ssh, self).__setattr__(name, value)

                    def has_data(self):
                        return self.port.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.port.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ssh" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.port.is_set or self.port.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.port.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "port"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "port"):
                            self.port = value
                            self.port.value_namespace = name_space
                            self.port.value_namespace_prefix = name_space_prefix


                class Tcp(Entity):
                    """
                    
                    
                    .. attribute:: port
                    
                    	
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    	**default value**\: 2023
                    
                    

                    """

                    _prefix = 'confd_dyncfg'
                    _revision = '2017-01-16'

                    def __init__(self):
                        super(Confdconfig.Proxyforwarding.Proxy.Netconf.Tcp, self).__init__()

                        self.yang_name = "tcp"
                        self.yang_parent_name = "netconf"

                        self.port = YLeaf(YType.uint16, "port")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("port") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Confdconfig.Proxyforwarding.Proxy.Netconf.Tcp, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Confdconfig.Proxyforwarding.Proxy.Netconf.Tcp, self).__setattr__(name, value)

                    def has_data(self):
                        return self.port.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.port.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "tcp" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.port.is_set or self.port.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.port.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "port"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "port"):
                            self.port = value
                            self.port.value_namespace = name_space
                            self.port.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        (self.ssh is not None and self.ssh.has_data()) or
                        (self.tcp is not None and self.tcp.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.ssh is not None and self.ssh.has_operation()) or
                        (self.tcp is not None and self.tcp.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "netconf" + path_buffer

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

                    if (child_yang_name == "ssh"):
                        if (self.ssh is None):
                            self.ssh = Confdconfig.Proxyforwarding.Proxy.Netconf.Ssh()
                            self.ssh.parent = self
                            self._children_name_map["ssh"] = "ssh"
                        return self.ssh

                    if (child_yang_name == "tcp"):
                        if (self.tcp is None):
                            self.tcp = Confdconfig.Proxyforwarding.Proxy.Netconf.Tcp()
                            self.tcp.parent = self
                            self._children_name_map["tcp"] = "tcp"
                        return self.tcp

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "ssh" or name == "tcp"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Cli(Entity):
                """
                
                
                .. attribute:: ssh
                
                	
                	**type**\:   :py:class:`Ssh <ydk.models.confd_dyncfg.Confdconfig.Proxyforwarding.Proxy.Cli.Ssh>`
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'confd_dyncfg'
                _revision = '2017-01-16'

                def __init__(self):
                    super(Confdconfig.Proxyforwarding.Proxy.Cli, self).__init__()

                    self.yang_name = "cli"
                    self.yang_parent_name = "proxy"
                    self.is_presence_container = True

                    self.ssh = Confdconfig.Proxyforwarding.Proxy.Cli.Ssh()
                    self.ssh.parent = self
                    self._children_name_map["ssh"] = "ssh"
                    self._children_yang_names.add("ssh")


                class Ssh(Entity):
                    """
                    
                    
                    .. attribute:: port
                    
                    	
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    	**default value**\: 22
                    
                    

                    """

                    _prefix = 'confd_dyncfg'
                    _revision = '2017-01-16'

                    def __init__(self):
                        super(Confdconfig.Proxyforwarding.Proxy.Cli.Ssh, self).__init__()

                        self.yang_name = "ssh"
                        self.yang_parent_name = "cli"

                        self.port = YLeaf(YType.uint16, "port")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("port") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Confdconfig.Proxyforwarding.Proxy.Cli.Ssh, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Confdconfig.Proxyforwarding.Proxy.Cli.Ssh, self).__setattr__(name, value)

                    def has_data(self):
                        return self.port.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.port.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ssh" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.port.is_set or self.port.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.port.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "port"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "port"):
                            self.port = value
                            self.port.value_namespace = name_space
                            self.port.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (self.ssh is not None and self.ssh.has_data())

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.ssh is not None and self.ssh.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "cli" + path_buffer

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

                    if (child_yang_name == "ssh"):
                        if (self.ssh is None):
                            self.ssh = Confdconfig.Proxyforwarding.Proxy.Cli.Ssh()
                            self.ssh.parent = self
                            self._children_name_map["ssh"] = "ssh"
                        return self.ssh

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "ssh"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.target.is_set or
                    self.address.is_set or
                    (self.cli is not None) or
                    (self.netconf is not None))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.target.yfilter != YFilter.not_set or
                    self.address.yfilter != YFilter.not_set or
                    (self.cli is not None and self.cli.has_operation()) or
                    (self.netconf is not None and self.netconf.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "proxy" + "[target='" + self.target.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "confd_dyncfg:confdConfig/proxyForwarding/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.target.is_set or self.target.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.target.get_name_leafdata())
                if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.address.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "cli"):
                    if (self.cli is None):
                        self.cli = Confdconfig.Proxyforwarding.Proxy.Cli()
                        self.cli.parent = self
                        self._children_name_map["cli"] = "cli"
                    return self.cli

                if (child_yang_name == "netconf"):
                    if (self.netconf is None):
                        self.netconf = Confdconfig.Proxyforwarding.Proxy.Netconf()
                        self.netconf.parent = self
                        self._children_name_map["netconf"] = "netconf"
                    return self.netconf

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cli" or name == "netconf" or name == "target" or name == "address"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "target"):
                    self.target = value
                    self.target.value_namespace = name_space
                    self.target.value_namespace_prefix = name_space_prefix
                if(value_path == "address"):
                    self.address = value
                    self.address.value_namespace = name_space
                    self.address.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.proxy:
                if (c.has_data()):
                    return True
            return self.autologin.is_set

        def has_operation(self):
            for c in self.proxy:
                if (c.has_operation()):
                    return True
            return (
                self.yfilter != YFilter.not_set or
                self.autologin.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "proxyForwarding" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "confd_dyncfg:confdConfig/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.autologin.is_set or self.autologin.yfilter != YFilter.not_set):
                leaf_name_data.append(self.autologin.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "proxy"):
                for c in self.proxy:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Confdconfig.Proxyforwarding.Proxy()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.proxy.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "proxy" or name == "autoLogin"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "autoLogin"):
                self.autologin = value
                self.autologin.value_namespace = name_space
                self.autologin.value_namespace_prefix = name_space_prefix


    class Snmpagent(Entity):
        """
        
        
        .. attribute:: authenticationfailurenotifyname
        
        	
        	**type**\:  str
        
        .. attribute:: candidate
        
        	
        	**type**\:   :py:class:`Candidate <ydk.models.confd_dyncfg.Confdconfig.Snmpagent.Candidate>`
        
        	**presence node**\: True
        
        .. attribute:: contexts
        
        	
        	**type**\:  list of str
        
        	**length:** 0..31
        
        .. attribute:: dropwheninuse
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: dscp
        
        	
        	**type**\:  int
        
        	**range:** 0..63
        
        .. attribute:: enabled
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: extraipports
        
        	
        	**type**\:  list of str
        
        .. attribute:: ip
        
        	
        	**type**\: one of the below types:
        
        	**type**\:  str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        	**default value**\: 0.0.0.0
        
        
        ----
        	**type**\:  str
        
        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
        
        	**default value**\: 0.0.0.0
        
        
        ----
        .. attribute:: mibs
        
        	
        	**type**\:   :py:class:`Mibs <ydk.models.confd_dyncfg.Confdconfig.Snmpagent.Mibs>`
        
        	**presence node**\: True
        
        .. attribute:: port
        
        	
        	**type**\:  int
        
        	**range:** 0..65535
        
        	**default value**\: 161
        
        .. attribute:: sessionignoreport
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: snmpengine
        
        	
        	**type**\:   :py:class:`Snmpengine <ydk.models.confd_dyncfg.Confdconfig.Snmpagent.Snmpengine>`
        
        	**presence node**\: True
        
        .. attribute:: snmpversions
        
        	
        	**type**\:   :py:class:`Snmpversions <ydk.models.confd_dyncfg.Confdconfig.Snmpagent.Snmpversions>`
        
        	**presence node**\: True
        
        .. attribute:: system
        
        	
        	**type**\:   :py:class:`System <ydk.models.confd_dyncfg.Confdconfig.Snmpagent.System>`
        
        	**presence node**\: True
        
        .. attribute:: temporarystoragetime
        
        	
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**default value**\: 300
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'confd_dyncfg'
        _revision = '2017-01-16'

        def __init__(self):
            super(Confdconfig.Snmpagent, self).__init__()

            self.yang_name = "snmpAgent"
            self.yang_parent_name = "confdConfig"
            self.is_presence_container = True

            self.authenticationfailurenotifyname = YLeaf(YType.str, "authenticationFailureNotifyName")

            self.contexts = YLeafList(YType.str, "contexts")

            self.dropwheninuse = YLeaf(YType.boolean, "dropWhenInUse")

            self.dscp = YLeaf(YType.uint8, "dscp")

            self.enabled = YLeaf(YType.boolean, "enabled")

            self.extraipports = YLeafList(YType.str, "extraIpPorts")

            self.ip = YLeaf(YType.str, "ip")

            self.port = YLeaf(YType.uint16, "port")

            self.sessionignoreport = YLeaf(YType.boolean, "sessionIgnorePort")

            self.temporarystoragetime = YLeaf(YType.uint32, "temporaryStorageTime")

            self.candidate = None
            self._children_name_map["candidate"] = "candidate"
            self._children_yang_names.add("candidate")

            self.mibs = None
            self._children_name_map["mibs"] = "mibs"
            self._children_yang_names.add("mibs")

            self.snmpengine = None
            self._children_name_map["snmpengine"] = "snmpEngine"
            self._children_yang_names.add("snmpEngine")

            self.snmpversions = None
            self._children_name_map["snmpversions"] = "snmpVersions"
            self._children_yang_names.add("snmpVersions")

            self.system = None
            self._children_name_map["system"] = "system"
            self._children_yang_names.add("system")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("authenticationfailurenotifyname",
                            "contexts",
                            "dropwheninuse",
                            "dscp",
                            "enabled",
                            "extraipports",
                            "ip",
                            "port",
                            "sessionignoreport",
                            "temporarystoragetime") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Confdconfig.Snmpagent, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Confdconfig.Snmpagent, self).__setattr__(name, value)


        class Mibs(Entity):
            """
            
            
            .. attribute:: file
            
            	
            	**type**\:  list of str
            
            .. attribute:: fromloadpath
            
            	
            	**type**\:  bool
            
            	**default value**\: false
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'confd_dyncfg'
            _revision = '2017-01-16'

            def __init__(self):
                super(Confdconfig.Snmpagent.Mibs, self).__init__()

                self.yang_name = "mibs"
                self.yang_parent_name = "snmpAgent"
                self.is_presence_container = True

                self.file = YLeafList(YType.str, "file")

                self.fromloadpath = YLeaf(YType.boolean, "fromLoadPath")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("file",
                                "fromloadpath") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Confdconfig.Snmpagent.Mibs, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Confdconfig.Snmpagent.Mibs, self).__setattr__(name, value)

            def has_data(self):
                for leaf in self.file.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                return self.fromloadpath.is_set

            def has_operation(self):
                for leaf in self.file.getYLeafs():
                    if (leaf.is_set):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.file.yfilter != YFilter.not_set or
                    self.fromloadpath.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "mibs" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "confd_dyncfg:confdConfig/snmpAgent/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.fromloadpath.is_set or self.fromloadpath.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.fromloadpath.get_name_leafdata())

                leaf_name_data.extend(self.file.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "file" or name == "fromLoadPath"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "file"):
                    self.file.append(value)
                if(value_path == "fromLoadPath"):
                    self.fromloadpath = value
                    self.fromloadpath.value_namespace = name_space
                    self.fromloadpath.value_namespace_prefix = name_space_prefix


        class Snmpversions(Entity):
            """
            
            
            .. attribute:: v1
            
            	
            	**type**\:  bool
            
            	**default value**\: true
            
            .. attribute:: v2c
            
            	
            	**type**\:  bool
            
            	**default value**\: true
            
            .. attribute:: v3
            
            	
            	**type**\:  bool
            
            	**default value**\: true
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'confd_dyncfg'
            _revision = '2017-01-16'

            def __init__(self):
                super(Confdconfig.Snmpagent.Snmpversions, self).__init__()

                self.yang_name = "snmpVersions"
                self.yang_parent_name = "snmpAgent"
                self.is_presence_container = True

                self.v1 = YLeaf(YType.boolean, "v1")

                self.v2c = YLeaf(YType.boolean, "v2c")

                self.v3 = YLeaf(YType.boolean, "v3")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("v1",
                                "v2c",
                                "v3") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Confdconfig.Snmpagent.Snmpversions, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Confdconfig.Snmpagent.Snmpversions, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.v1.is_set or
                    self.v2c.is_set or
                    self.v3.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.v1.yfilter != YFilter.not_set or
                    self.v2c.yfilter != YFilter.not_set or
                    self.v3.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "snmpVersions" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "confd_dyncfg:confdConfig/snmpAgent/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.v1.is_set or self.v1.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.v1.get_name_leafdata())
                if (self.v2c.is_set or self.v2c.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.v2c.get_name_leafdata())
                if (self.v3.is_set or self.v3.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.v3.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "v1" or name == "v2c" or name == "v3"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "v1"):
                    self.v1 = value
                    self.v1.value_namespace = name_space
                    self.v1.value_namespace_prefix = name_space_prefix
                if(value_path == "v2c"):
                    self.v2c = value
                    self.v2c.value_namespace = name_space
                    self.v2c.value_namespace_prefix = name_space_prefix
                if(value_path == "v3"):
                    self.v3 = value
                    self.v3.value_namespace = name_space
                    self.v3.value_namespace_prefix = name_space_prefix


        class Snmpengine(Entity):
            """
            
            
            .. attribute:: snmpengineid
            
            	
            	**type**\:  str
            
            	**pattern:** (([0\-9a\-fA\-F]){2}(\:([0\-9a\-fA\-F]){2})\*)?
            
            	**mandatory**\: True
            
            .. attribute:: snmpenginemaxmessagesize
            
            	
            	**type**\:  int
            
            	**range:** 0..18446744073709551615 \| 0..18446744073709551615
            
            	**default value**\: 50000
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'confd_dyncfg'
            _revision = '2017-01-16'

            def __init__(self):
                super(Confdconfig.Snmpagent.Snmpengine, self).__init__()

                self.yang_name = "snmpEngine"
                self.yang_parent_name = "snmpAgent"
                self.is_presence_container = True

                self.snmpengineid = YLeaf(YType.str, "snmpEngineID")

                self.snmpenginemaxmessagesize = YLeaf(YType.uint64, "snmpEngineMaxMessageSize")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("snmpengineid",
                                "snmpenginemaxmessagesize") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Confdconfig.Snmpagent.Snmpengine, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Confdconfig.Snmpagent.Snmpengine, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.snmpengineid.is_set or
                    self.snmpenginemaxmessagesize.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.snmpengineid.yfilter != YFilter.not_set or
                    self.snmpenginemaxmessagesize.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "snmpEngine" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "confd_dyncfg:confdConfig/snmpAgent/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.snmpengineid.is_set or self.snmpengineid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.snmpengineid.get_name_leafdata())
                if (self.snmpenginemaxmessagesize.is_set or self.snmpenginemaxmessagesize.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.snmpenginemaxmessagesize.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "snmpEngineID" or name == "snmpEngineMaxMessageSize"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "snmpEngineID"):
                    self.snmpengineid = value
                    self.snmpengineid.value_namespace = name_space
                    self.snmpengineid.value_namespace_prefix = name_space_prefix
                if(value_path == "snmpEngineMaxMessageSize"):
                    self.snmpenginemaxmessagesize = value
                    self.snmpenginemaxmessagesize.value_namespace = name_space
                    self.snmpenginemaxmessagesize.value_namespace_prefix = name_space_prefix


        class Candidate(Entity):
            """
            
            
            .. attribute:: maxlockwait
            
            	
            	**type**\:  str
            
            	**default value**\: PT0S
            
            .. attribute:: pendingchangesaction
            
            	
            	**type**\:   :py:class:`Pendingchangesactiontype <ydk.models.confd_dyncfg.Pendingchangesactiontype>`
            
            	**default value**\: continue
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'confd_dyncfg'
            _revision = '2017-01-16'

            def __init__(self):
                super(Confdconfig.Snmpagent.Candidate, self).__init__()

                self.yang_name = "candidate"
                self.yang_parent_name = "snmpAgent"
                self.is_presence_container = True

                self.maxlockwait = YLeaf(YType.str, "maxLockWait")

                self.pendingchangesaction = YLeaf(YType.enumeration, "pendingChangesAction")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("maxlockwait",
                                "pendingchangesaction") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Confdconfig.Snmpagent.Candidate, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Confdconfig.Snmpagent.Candidate, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.maxlockwait.is_set or
                    self.pendingchangesaction.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.maxlockwait.yfilter != YFilter.not_set or
                    self.pendingchangesaction.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "candidate" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "confd_dyncfg:confdConfig/snmpAgent/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.maxlockwait.is_set or self.maxlockwait.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.maxlockwait.get_name_leafdata())
                if (self.pendingchangesaction.is_set or self.pendingchangesaction.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.pendingchangesaction.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "maxLockWait" or name == "pendingChangesAction"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "maxLockWait"):
                    self.maxlockwait = value
                    self.maxlockwait.value_namespace = name_space
                    self.maxlockwait.value_namespace_prefix = name_space_prefix
                if(value_path == "pendingChangesAction"):
                    self.pendingchangesaction = value
                    self.pendingchangesaction.value_namespace = name_space
                    self.pendingchangesaction.value_namespace_prefix = name_space_prefix


        class System(Entity):
            """
            
            
            .. attribute:: sysdescr
            
            	
            	**type**\:  str
            
            .. attribute:: sysobjectid
            
            	
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: sysortable
            
            	
            	**type**\:   :py:class:`Sysortable <ydk.models.confd_dyncfg.Confdconfig.Snmpagent.System.Sysortable>`
            
            	**presence node**\: True
            
            .. attribute:: sysservices
            
            	
            	**type**\:  int
            
            	**range:** 0..18446744073709551615 \| 0..18446744073709551615
            
            	**default value**\: 72
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'confd_dyncfg'
            _revision = '2017-01-16'

            def __init__(self):
                super(Confdconfig.Snmpagent.System, self).__init__()

                self.yang_name = "system"
                self.yang_parent_name = "snmpAgent"
                self.is_presence_container = True

                self.sysdescr = YLeaf(YType.str, "sysDescr")

                self.sysobjectid = YLeaf(YType.str, "sysObjectID")

                self.sysservices = YLeaf(YType.uint64, "sysServices")

                self.sysortable = None
                self._children_name_map["sysortable"] = "sysORTable"
                self._children_yang_names.add("sysORTable")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("sysdescr",
                                "sysobjectid",
                                "sysservices") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Confdconfig.Snmpagent.System, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Confdconfig.Snmpagent.System, self).__setattr__(name, value)


            class Sysortable(Entity):
                """
                
                
                .. attribute:: sysorentry
                
                	
                	**type**\: list of    :py:class:`Sysorentry <ydk.models.confd_dyncfg.Confdconfig.Snmpagent.System.Sysortable.Sysorentry>`
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'confd_dyncfg'
                _revision = '2017-01-16'

                def __init__(self):
                    super(Confdconfig.Snmpagent.System.Sysortable, self).__init__()

                    self.yang_name = "sysORTable"
                    self.yang_parent_name = "system"
                    self.is_presence_container = True

                    self.sysorentry = YList(self)

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
                                super(Confdconfig.Snmpagent.System.Sysortable, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Confdconfig.Snmpagent.System.Sysortable, self).__setattr__(name, value)


                class Sysorentry(Entity):
                    """
                    
                    
                    .. attribute:: sysorindex  <key>
                    
                    	
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615 \| 0..18446744073709551615
                    
                    .. attribute:: sysordescr
                    
                    	
                    	**type**\:  str
                    
                    	**mandatory**\: True
                    
                    .. attribute:: sysorid
                    
                    	
                    	**type**\:  str
                    
                    	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'confd_dyncfg'
                    _revision = '2017-01-16'

                    def __init__(self):
                        super(Confdconfig.Snmpagent.System.Sysortable.Sysorentry, self).__init__()

                        self.yang_name = "sysOREntry"
                        self.yang_parent_name = "sysORTable"

                        self.sysorindex = YLeaf(YType.uint64, "sysORIndex")

                        self.sysordescr = YLeaf(YType.str, "sysORDescr")

                        self.sysorid = YLeaf(YType.str, "sysORID")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("sysorindex",
                                        "sysordescr",
                                        "sysorid") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Confdconfig.Snmpagent.System.Sysortable.Sysorentry, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Confdconfig.Snmpagent.System.Sysortable.Sysorentry, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.sysorindex.is_set or
                            self.sysordescr.is_set or
                            self.sysorid.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.sysorindex.yfilter != YFilter.not_set or
                            self.sysordescr.yfilter != YFilter.not_set or
                            self.sysorid.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "sysOREntry" + "[sysORIndex='" + self.sysorindex.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "confd_dyncfg:confdConfig/snmpAgent/system/sysORTable/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.sysorindex.is_set or self.sysorindex.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.sysorindex.get_name_leafdata())
                        if (self.sysordescr.is_set or self.sysordescr.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.sysordescr.get_name_leafdata())
                        if (self.sysorid.is_set or self.sysorid.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.sysorid.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "sysORIndex" or name == "sysORDescr" or name == "sysORID"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "sysORIndex"):
                            self.sysorindex = value
                            self.sysorindex.value_namespace = name_space
                            self.sysorindex.value_namespace_prefix = name_space_prefix
                        if(value_path == "sysORDescr"):
                            self.sysordescr = value
                            self.sysordescr.value_namespace = name_space
                            self.sysordescr.value_namespace_prefix = name_space_prefix
                        if(value_path == "sysORID"):
                            self.sysorid = value
                            self.sysorid.value_namespace = name_space
                            self.sysorid.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.sysorentry:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.sysorentry:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "sysORTable" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "confd_dyncfg:confdConfig/snmpAgent/system/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "sysOREntry"):
                        for c in self.sysorentry:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Confdconfig.Snmpagent.System.Sysortable.Sysorentry()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.sysorentry.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "sysOREntry"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.sysdescr.is_set or
                    self.sysobjectid.is_set or
                    self.sysservices.is_set or
                    (self.sysortable is not None))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.sysdescr.yfilter != YFilter.not_set or
                    self.sysobjectid.yfilter != YFilter.not_set or
                    self.sysservices.yfilter != YFilter.not_set or
                    (self.sysortable is not None and self.sysortable.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "system" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "confd_dyncfg:confdConfig/snmpAgent/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.sysdescr.is_set or self.sysdescr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sysdescr.get_name_leafdata())
                if (self.sysobjectid.is_set or self.sysobjectid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sysobjectid.get_name_leafdata())
                if (self.sysservices.is_set or self.sysservices.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sysservices.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "sysORTable"):
                    if (self.sysortable is None):
                        self.sysortable = Confdconfig.Snmpagent.System.Sysortable()
                        self.sysortable.parent = self
                        self._children_name_map["sysortable"] = "sysORTable"
                    return self.sysortable

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "sysORTable" or name == "sysDescr" or name == "sysObjectID" or name == "sysServices"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "sysDescr"):
                    self.sysdescr = value
                    self.sysdescr.value_namespace = name_space
                    self.sysdescr.value_namespace_prefix = name_space_prefix
                if(value_path == "sysObjectID"):
                    self.sysobjectid = value
                    self.sysobjectid.value_namespace = name_space
                    self.sysobjectid.value_namespace_prefix = name_space_prefix
                if(value_path == "sysServices"):
                    self.sysservices = value
                    self.sysservices.value_namespace = name_space
                    self.sysservices.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for leaf in self.contexts.getYLeafs():
                if (leaf.yfilter != YFilter.not_set):
                    return True
            for leaf in self.extraipports.getYLeafs():
                if (leaf.yfilter != YFilter.not_set):
                    return True
            return (
                self.authenticationfailurenotifyname.is_set or
                self.dropwheninuse.is_set or
                self.dscp.is_set or
                self.enabled.is_set or
                self.ip.is_set or
                self.port.is_set or
                self.sessionignoreport.is_set or
                self.temporarystoragetime.is_set or
                (self.candidate is not None) or
                (self.mibs is not None) or
                (self.snmpengine is not None) or
                (self.snmpversions is not None) or
                (self.system is not None))

        def has_operation(self):
            for leaf in self.contexts.getYLeafs():
                if (leaf.is_set):
                    return True
            for leaf in self.extraipports.getYLeafs():
                if (leaf.is_set):
                    return True
            return (
                self.yfilter != YFilter.not_set or
                self.authenticationfailurenotifyname.yfilter != YFilter.not_set or
                self.contexts.yfilter != YFilter.not_set or
                self.dropwheninuse.yfilter != YFilter.not_set or
                self.dscp.yfilter != YFilter.not_set or
                self.enabled.yfilter != YFilter.not_set or
                self.extraipports.yfilter != YFilter.not_set or
                self.ip.yfilter != YFilter.not_set or
                self.port.yfilter != YFilter.not_set or
                self.sessionignoreport.yfilter != YFilter.not_set or
                self.temporarystoragetime.yfilter != YFilter.not_set or
                (self.candidate is not None and self.candidate.has_operation()) or
                (self.mibs is not None and self.mibs.has_operation()) or
                (self.snmpengine is not None and self.snmpengine.has_operation()) or
                (self.snmpversions is not None and self.snmpversions.has_operation()) or
                (self.system is not None and self.system.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "snmpAgent" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "confd_dyncfg:confdConfig/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.authenticationfailurenotifyname.is_set or self.authenticationfailurenotifyname.yfilter != YFilter.not_set):
                leaf_name_data.append(self.authenticationfailurenotifyname.get_name_leafdata())
            if (self.dropwheninuse.is_set or self.dropwheninuse.yfilter != YFilter.not_set):
                leaf_name_data.append(self.dropwheninuse.get_name_leafdata())
            if (self.dscp.is_set or self.dscp.yfilter != YFilter.not_set):
                leaf_name_data.append(self.dscp.get_name_leafdata())
            if (self.enabled.is_set or self.enabled.yfilter != YFilter.not_set):
                leaf_name_data.append(self.enabled.get_name_leafdata())
            if (self.ip.is_set or self.ip.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ip.get_name_leafdata())
            if (self.port.is_set or self.port.yfilter != YFilter.not_set):
                leaf_name_data.append(self.port.get_name_leafdata())
            if (self.sessionignoreport.is_set or self.sessionignoreport.yfilter != YFilter.not_set):
                leaf_name_data.append(self.sessionignoreport.get_name_leafdata())
            if (self.temporarystoragetime.is_set or self.temporarystoragetime.yfilter != YFilter.not_set):
                leaf_name_data.append(self.temporarystoragetime.get_name_leafdata())

            leaf_name_data.extend(self.contexts.get_name_leafdata())

            leaf_name_data.extend(self.extraipports.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "candidate"):
                if (self.candidate is None):
                    self.candidate = Confdconfig.Snmpagent.Candidate()
                    self.candidate.parent = self
                    self._children_name_map["candidate"] = "candidate"
                return self.candidate

            if (child_yang_name == "mibs"):
                if (self.mibs is None):
                    self.mibs = Confdconfig.Snmpagent.Mibs()
                    self.mibs.parent = self
                    self._children_name_map["mibs"] = "mibs"
                return self.mibs

            if (child_yang_name == "snmpEngine"):
                if (self.snmpengine is None):
                    self.snmpengine = Confdconfig.Snmpagent.Snmpengine()
                    self.snmpengine.parent = self
                    self._children_name_map["snmpengine"] = "snmpEngine"
                return self.snmpengine

            if (child_yang_name == "snmpVersions"):
                if (self.snmpversions is None):
                    self.snmpversions = Confdconfig.Snmpagent.Snmpversions()
                    self.snmpversions.parent = self
                    self._children_name_map["snmpversions"] = "snmpVersions"
                return self.snmpversions

            if (child_yang_name == "system"):
                if (self.system is None):
                    self.system = Confdconfig.Snmpagent.System()
                    self.system.parent = self
                    self._children_name_map["system"] = "system"
                return self.system

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "candidate" or name == "mibs" or name == "snmpEngine" or name == "snmpVersions" or name == "system" or name == "authenticationFailureNotifyName" or name == "contexts" or name == "dropWhenInUse" or name == "dscp" or name == "enabled" or name == "extraIpPorts" or name == "ip" or name == "port" or name == "sessionIgnorePort" or name == "temporaryStorageTime"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "authenticationFailureNotifyName"):
                self.authenticationfailurenotifyname = value
                self.authenticationfailurenotifyname.value_namespace = name_space
                self.authenticationfailurenotifyname.value_namespace_prefix = name_space_prefix
            if(value_path == "contexts"):
                self.contexts.append(value)
            if(value_path == "dropWhenInUse"):
                self.dropwheninuse = value
                self.dropwheninuse.value_namespace = name_space
                self.dropwheninuse.value_namespace_prefix = name_space_prefix
            if(value_path == "dscp"):
                self.dscp = value
                self.dscp.value_namespace = name_space
                self.dscp.value_namespace_prefix = name_space_prefix
            if(value_path == "enabled"):
                self.enabled = value
                self.enabled.value_namespace = name_space
                self.enabled.value_namespace_prefix = name_space_prefix
            if(value_path == "extraIpPorts"):
                self.extraipports.append(value)
            if(value_path == "ip"):
                self.ip = value
                self.ip.value_namespace = name_space
                self.ip.value_namespace_prefix = name_space_prefix
            if(value_path == "port"):
                self.port = value
                self.port.value_namespace = name_space
                self.port.value_namespace_prefix = name_space_prefix
            if(value_path == "sessionIgnorePort"):
                self.sessionignoreport = value
                self.sessionignoreport.value_namespace = name_space
                self.sessionignoreport.value_namespace_prefix = name_space_prefix
            if(value_path == "temporaryStorageTime"):
                self.temporarystoragetime = value
                self.temporarystoragetime.value_namespace = name_space
                self.temporarystoragetime.value_namespace_prefix = name_space_prefix


    class Netconf(Entity):
        """
        
        
        .. attribute:: enabled
        
        	
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: extendedsessions
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: idletimeout
        
        	
        	**type**\:  str
        
        	**default value**\: PT0S
        
        .. attribute:: maxbatchprocesses
        
        	
        	**type**\: one of the below types:
        
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**default value**\: unbounded
        
        
        ----
        	**type**\:   :py:class:`Unboundedtype <ydk.models.confd_dyncfg.Unboundedtype>`
        
        	**default value**\: unbounded
        
        
        ----
        .. attribute:: rpcerrors
        
        	
        	**type**\:   :py:class:`Rpcerrortype <ydk.models.confd_dyncfg.Rpcerrortype>`
        
        	**default value**\: close
        
        .. attribute:: senddefaults
        
        	DEPRECATED \- use /confdConfig/defaultHandlingMode instead to control this behavior consistently for all northbound interfaces.  If sendDefaults is true, default values will be included in the replies to <get>, <get\-config>, and <copy\-config>.  If sendDefaults is false, default values will not be included by default.  If /confdConfig/netconf/capabilities/with\-defaults is enabled, this behavior can be controlled by the NETCONF client
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: transport
        
        	
        	**type**\:   :py:class:`Transport <ydk.models.confd_dyncfg.Confdconfig.Netconf.Transport>`
        
        	**presence node**\: True
        
        .. attribute:: writetimeout
        
        	
        	**type**\:  str
        
        	**default value**\: PT0S
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'confd_dyncfg'
        _revision = '2017-01-16'

        def __init__(self):
            super(Confdconfig.Netconf, self).__init__()

            self.yang_name = "netconf"
            self.yang_parent_name = "confdConfig"
            self.is_presence_container = True

            self.enabled = YLeaf(YType.boolean, "enabled")

            self.extendedsessions = YLeaf(YType.boolean, "extendedSessions")

            self.idletimeout = YLeaf(YType.str, "idleTimeout")

            self.maxbatchprocesses = YLeaf(YType.str, "maxBatchProcesses")

            self.rpcerrors = YLeaf(YType.enumeration, "rpcErrors")

            self.senddefaults = YLeaf(YType.boolean, "sendDefaults")

            self.writetimeout = YLeaf(YType.str, "writeTimeout")

            self.transport = None
            self._children_name_map["transport"] = "transport"
            self._children_yang_names.add("transport")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("enabled",
                            "extendedsessions",
                            "idletimeout",
                            "maxbatchprocesses",
                            "rpcerrors",
                            "senddefaults",
                            "writetimeout") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Confdconfig.Netconf, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Confdconfig.Netconf, self).__setattr__(name, value)


        class Transport(Entity):
            """
            
            
            .. attribute:: ssh
            
            	
            	**type**\:   :py:class:`Ssh <ydk.models.confd_dyncfg.Confdconfig.Netconf.Transport.Ssh>`
            
            	**presence node**\: True
            
            .. attribute:: tcp
            
            	
            	**type**\:   :py:class:`Tcp <ydk.models.confd_dyncfg.Confdconfig.Netconf.Transport.Tcp>`
            
            	**presence node**\: True
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'confd_dyncfg'
            _revision = '2017-01-16'

            def __init__(self):
                super(Confdconfig.Netconf.Transport, self).__init__()

                self.yang_name = "transport"
                self.yang_parent_name = "netconf"
                self.is_presence_container = True

                self.ssh = None
                self._children_name_map["ssh"] = "ssh"
                self._children_yang_names.add("ssh")

                self.tcp = None
                self._children_name_map["tcp"] = "tcp"
                self._children_yang_names.add("tcp")


            class Ssh(Entity):
                """
                
                
                .. attribute:: dscp
                
                	
                	**type**\:  int
                
                	**range:** 0..63
                
                .. attribute:: enabled
                
                	
                	**type**\:  bool
                
                	**default value**\: true
                
                .. attribute:: extraipports
                
                	
                	**type**\:  list of str
                
                .. attribute:: ip
                
                	
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                	**default value**\: 0.0.0.0
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                	**default value**\: 0.0.0.0
                
                
                ----
                .. attribute:: port
                
                	
                	**type**\:  int
                
                	**range:** 0..65535
                
                	**default value**\: 2022
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'confd_dyncfg'
                _revision = '2017-01-16'

                def __init__(self):
                    super(Confdconfig.Netconf.Transport.Ssh, self).__init__()

                    self.yang_name = "ssh"
                    self.yang_parent_name = "transport"
                    self.is_presence_container = True

                    self.dscp = YLeaf(YType.uint8, "dscp")

                    self.enabled = YLeaf(YType.boolean, "enabled")

                    self.extraipports = YLeafList(YType.str, "extraIpPorts")

                    self.ip = YLeaf(YType.str, "ip")

                    self.port = YLeaf(YType.uint16, "port")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("dscp",
                                    "enabled",
                                    "extraipports",
                                    "ip",
                                    "port") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Confdconfig.Netconf.Transport.Ssh, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Confdconfig.Netconf.Transport.Ssh, self).__setattr__(name, value)

                def has_data(self):
                    for leaf in self.extraipports.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    return (
                        self.dscp.is_set or
                        self.enabled.is_set or
                        self.ip.is_set or
                        self.port.is_set)

                def has_operation(self):
                    for leaf in self.extraipports.getYLeafs():
                        if (leaf.is_set):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.dscp.yfilter != YFilter.not_set or
                        self.enabled.yfilter != YFilter.not_set or
                        self.extraipports.yfilter != YFilter.not_set or
                        self.ip.yfilter != YFilter.not_set or
                        self.port.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "ssh" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "confd_dyncfg:confdConfig/netconf/transport/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.dscp.is_set or self.dscp.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.dscp.get_name_leafdata())
                    if (self.enabled.is_set or self.enabled.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.enabled.get_name_leafdata())
                    if (self.ip.is_set or self.ip.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ip.get_name_leafdata())
                    if (self.port.is_set or self.port.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.port.get_name_leafdata())

                    leaf_name_data.extend(self.extraipports.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "dscp" or name == "enabled" or name == "extraIpPorts" or name == "ip" or name == "port"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "dscp"):
                        self.dscp = value
                        self.dscp.value_namespace = name_space
                        self.dscp.value_namespace_prefix = name_space_prefix
                    if(value_path == "enabled"):
                        self.enabled = value
                        self.enabled.value_namespace = name_space
                        self.enabled.value_namespace_prefix = name_space_prefix
                    if(value_path == "extraIpPorts"):
                        self.extraipports.append(value)
                    if(value_path == "ip"):
                        self.ip = value
                        self.ip.value_namespace = name_space
                        self.ip.value_namespace_prefix = name_space_prefix
                    if(value_path == "port"):
                        self.port = value
                        self.port.value_namespace = name_space
                        self.port.value_namespace_prefix = name_space_prefix


            class Tcp(Entity):
                """
                
                
                .. attribute:: dscp
                
                	
                	**type**\:  int
                
                	**range:** 0..63
                
                .. attribute:: enabled
                
                	
                	**type**\:  bool
                
                	**default value**\: false
                
                .. attribute:: extraipports
                
                	
                	**type**\:  list of str
                
                .. attribute:: ip
                
                	
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                	**default value**\: 0.0.0.0
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                	**default value**\: 0.0.0.0
                
                
                ----
                .. attribute:: port
                
                	
                	**type**\:  int
                
                	**range:** 0..65535
                
                	**default value**\: 2023
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'confd_dyncfg'
                _revision = '2017-01-16'

                def __init__(self):
                    super(Confdconfig.Netconf.Transport.Tcp, self).__init__()

                    self.yang_name = "tcp"
                    self.yang_parent_name = "transport"
                    self.is_presence_container = True

                    self.dscp = YLeaf(YType.uint8, "dscp")

                    self.enabled = YLeaf(YType.boolean, "enabled")

                    self.extraipports = YLeafList(YType.str, "extraIpPorts")

                    self.ip = YLeaf(YType.str, "ip")

                    self.port = YLeaf(YType.uint16, "port")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("dscp",
                                    "enabled",
                                    "extraipports",
                                    "ip",
                                    "port") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Confdconfig.Netconf.Transport.Tcp, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Confdconfig.Netconf.Transport.Tcp, self).__setattr__(name, value)

                def has_data(self):
                    for leaf in self.extraipports.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    return (
                        self.dscp.is_set or
                        self.enabled.is_set or
                        self.ip.is_set or
                        self.port.is_set)

                def has_operation(self):
                    for leaf in self.extraipports.getYLeafs():
                        if (leaf.is_set):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.dscp.yfilter != YFilter.not_set or
                        self.enabled.yfilter != YFilter.not_set or
                        self.extraipports.yfilter != YFilter.not_set or
                        self.ip.yfilter != YFilter.not_set or
                        self.port.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "tcp" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "confd_dyncfg:confdConfig/netconf/transport/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.dscp.is_set or self.dscp.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.dscp.get_name_leafdata())
                    if (self.enabled.is_set or self.enabled.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.enabled.get_name_leafdata())
                    if (self.ip.is_set or self.ip.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ip.get_name_leafdata())
                    if (self.port.is_set or self.port.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.port.get_name_leafdata())

                    leaf_name_data.extend(self.extraipports.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "dscp" or name == "enabled" or name == "extraIpPorts" or name == "ip" or name == "port"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "dscp"):
                        self.dscp = value
                        self.dscp.value_namespace = name_space
                        self.dscp.value_namespace_prefix = name_space_prefix
                    if(value_path == "enabled"):
                        self.enabled = value
                        self.enabled.value_namespace = name_space
                        self.enabled.value_namespace_prefix = name_space_prefix
                    if(value_path == "extraIpPorts"):
                        self.extraipports.append(value)
                    if(value_path == "ip"):
                        self.ip = value
                        self.ip.value_namespace = name_space
                        self.ip.value_namespace_prefix = name_space_prefix
                    if(value_path == "port"):
                        self.port = value
                        self.port.value_namespace = name_space
                        self.port.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    (self.ssh is not None) or
                    (self.tcp is not None))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.ssh is not None and self.ssh.has_operation()) or
                    (self.tcp is not None and self.tcp.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "transport" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "confd_dyncfg:confdConfig/netconf/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "ssh"):
                    if (self.ssh is None):
                        self.ssh = Confdconfig.Netconf.Transport.Ssh()
                        self.ssh.parent = self
                        self._children_name_map["ssh"] = "ssh"
                    return self.ssh

                if (child_yang_name == "tcp"):
                    if (self.tcp is None):
                        self.tcp = Confdconfig.Netconf.Transport.Tcp()
                        self.tcp.parent = self
                        self._children_name_map["tcp"] = "tcp"
                    return self.tcp

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ssh" or name == "tcp"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                self.enabled.is_set or
                self.extendedsessions.is_set or
                self.idletimeout.is_set or
                self.maxbatchprocesses.is_set or
                self.rpcerrors.is_set or
                self.senddefaults.is_set or
                self.writetimeout.is_set or
                (self.transport is not None))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.enabled.yfilter != YFilter.not_set or
                self.extendedsessions.yfilter != YFilter.not_set or
                self.idletimeout.yfilter != YFilter.not_set or
                self.maxbatchprocesses.yfilter != YFilter.not_set or
                self.rpcerrors.yfilter != YFilter.not_set or
                self.senddefaults.yfilter != YFilter.not_set or
                self.writetimeout.yfilter != YFilter.not_set or
                (self.transport is not None and self.transport.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "netconf" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "confd_dyncfg:confdConfig/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.enabled.is_set or self.enabled.yfilter != YFilter.not_set):
                leaf_name_data.append(self.enabled.get_name_leafdata())
            if (self.extendedsessions.is_set or self.extendedsessions.yfilter != YFilter.not_set):
                leaf_name_data.append(self.extendedsessions.get_name_leafdata())
            if (self.idletimeout.is_set or self.idletimeout.yfilter != YFilter.not_set):
                leaf_name_data.append(self.idletimeout.get_name_leafdata())
            if (self.maxbatchprocesses.is_set or self.maxbatchprocesses.yfilter != YFilter.not_set):
                leaf_name_data.append(self.maxbatchprocesses.get_name_leafdata())
            if (self.rpcerrors.is_set or self.rpcerrors.yfilter != YFilter.not_set):
                leaf_name_data.append(self.rpcerrors.get_name_leafdata())
            if (self.senddefaults.is_set or self.senddefaults.yfilter != YFilter.not_set):
                leaf_name_data.append(self.senddefaults.get_name_leafdata())
            if (self.writetimeout.is_set or self.writetimeout.yfilter != YFilter.not_set):
                leaf_name_data.append(self.writetimeout.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "transport"):
                if (self.transport is None):
                    self.transport = Confdconfig.Netconf.Transport()
                    self.transport.parent = self
                    self._children_name_map["transport"] = "transport"
                return self.transport

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "transport" or name == "enabled" or name == "extendedSessions" or name == "idleTimeout" or name == "maxBatchProcesses" or name == "rpcErrors" or name == "sendDefaults" or name == "writeTimeout"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "enabled"):
                self.enabled = value
                self.enabled.value_namespace = name_space
                self.enabled.value_namespace_prefix = name_space_prefix
            if(value_path == "extendedSessions"):
                self.extendedsessions = value
                self.extendedsessions.value_namespace = name_space
                self.extendedsessions.value_namespace_prefix = name_space_prefix
            if(value_path == "idleTimeout"):
                self.idletimeout = value
                self.idletimeout.value_namespace = name_space
                self.idletimeout.value_namespace_prefix = name_space_prefix
            if(value_path == "maxBatchProcesses"):
                self.maxbatchprocesses = value
                self.maxbatchprocesses.value_namespace = name_space
                self.maxbatchprocesses.value_namespace_prefix = name_space_prefix
            if(value_path == "rpcErrors"):
                self.rpcerrors = value
                self.rpcerrors.value_namespace = name_space
                self.rpcerrors.value_namespace_prefix = name_space_prefix
            if(value_path == "sendDefaults"):
                self.senddefaults = value
                self.senddefaults.value_namespace = name_space
                self.senddefaults.value_namespace_prefix = name_space_prefix
            if(value_path == "writeTimeout"):
                self.writetimeout = value
                self.writetimeout.value_namespace = name_space
                self.writetimeout.value_namespace_prefix = name_space_prefix

    def has_data(self):
        for c in self.hidegroup:
            if (c.has_data()):
                return True
        return (
            (self.aaa is not None) or
            (self.cli is not None) or
            (self.encryptedstrings is not None) or
            (self.logs is not None) or
            (self.netconf is not None) or
            (self.notifications is not None) or
            (self.opcache is not None) or
            (self.proxyforwarding is not None) or
            (self.rest is not None) or
            (self.restconf is not None) or
            (self.sessionlimits is not None) or
            (self.snmpagent is not None) or
            (self.snmpgw is not None) or
            (self.ssh is not None) or
            (self.subagents is not None) or
            (self.webui is not None))

    def has_operation(self):
        for c in self.hidegroup:
            if (c.has_operation()):
                return True
        return (
            self.yfilter != YFilter.not_set or
            (self.aaa is not None and self.aaa.has_operation()) or
            (self.cli is not None and self.cli.has_operation()) or
            (self.encryptedstrings is not None and self.encryptedstrings.has_operation()) or
            (self.logs is not None and self.logs.has_operation()) or
            (self.netconf is not None and self.netconf.has_operation()) or
            (self.notifications is not None and self.notifications.has_operation()) or
            (self.opcache is not None and self.opcache.has_operation()) or
            (self.proxyforwarding is not None and self.proxyforwarding.has_operation()) or
            (self.rest is not None and self.rest.has_operation()) or
            (self.restconf is not None and self.restconf.has_operation()) or
            (self.sessionlimits is not None and self.sessionlimits.has_operation()) or
            (self.snmpagent is not None and self.snmpagent.has_operation()) or
            (self.snmpgw is not None and self.snmpgw.has_operation()) or
            (self.ssh is not None and self.ssh.has_operation()) or
            (self.subagents is not None and self.subagents.has_operation()) or
            (self.webui is not None and self.webui.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "confd_dyncfg:confdConfig" + path_buffer

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

        if (child_yang_name == "aaa"):
            if (self.aaa is None):
                self.aaa = Confdconfig.Aaa()
                self.aaa.parent = self
                self._children_name_map["aaa"] = "aaa"
            return self.aaa

        if (child_yang_name == "cli"):
            if (self.cli is None):
                self.cli = Confdconfig.Cli()
                self.cli.parent = self
                self._children_name_map["cli"] = "cli"
            return self.cli

        if (child_yang_name == "encryptedStrings"):
            if (self.encryptedstrings is None):
                self.encryptedstrings = Confdconfig.Encryptedstrings()
                self.encryptedstrings.parent = self
                self._children_name_map["encryptedstrings"] = "encryptedStrings"
            return self.encryptedstrings

        if (child_yang_name == "hideGroup"):
            for c in self.hidegroup:
                segment = c.get_segment_path()
                if (segment_path == segment):
                    return c
            c = Confdconfig.Hidegroup()
            c.parent = self
            local_reference_key = "ydk::seg::%s" % segment_path
            self._local_refs[local_reference_key] = c
            self.hidegroup.append(c)
            return c

        if (child_yang_name == "logs"):
            if (self.logs is None):
                self.logs = Confdconfig.Logs()
                self.logs.parent = self
                self._children_name_map["logs"] = "logs"
            return self.logs

        if (child_yang_name == "netconf"):
            if (self.netconf is None):
                self.netconf = Confdconfig.Netconf()
                self.netconf.parent = self
                self._children_name_map["netconf"] = "netconf"
            return self.netconf

        if (child_yang_name == "notifications"):
            if (self.notifications is None):
                self.notifications = Confdconfig.Notifications()
                self.notifications.parent = self
                self._children_name_map["notifications"] = "notifications"
            return self.notifications

        if (child_yang_name == "opcache"):
            if (self.opcache is None):
                self.opcache = Confdconfig.Opcache()
                self.opcache.parent = self
                self._children_name_map["opcache"] = "opcache"
            return self.opcache

        if (child_yang_name == "proxyForwarding"):
            if (self.proxyforwarding is None):
                self.proxyforwarding = Confdconfig.Proxyforwarding()
                self.proxyforwarding.parent = self
                self._children_name_map["proxyforwarding"] = "proxyForwarding"
            return self.proxyforwarding

        if (child_yang_name == "rest"):
            if (self.rest is None):
                self.rest = Confdconfig.Rest()
                self.rest.parent = self
                self._children_name_map["rest"] = "rest"
            return self.rest

        if (child_yang_name == "restconf"):
            if (self.restconf is None):
                self.restconf = Confdconfig.Restconf()
                self.restconf.parent = self
                self._children_name_map["restconf"] = "restconf"
            return self.restconf

        if (child_yang_name == "sessionLimits"):
            if (self.sessionlimits is None):
                self.sessionlimits = Confdconfig.Sessionlimits()
                self.sessionlimits.parent = self
                self._children_name_map["sessionlimits"] = "sessionLimits"
            return self.sessionlimits

        if (child_yang_name == "snmpAgent"):
            if (self.snmpagent is None):
                self.snmpagent = Confdconfig.Snmpagent()
                self.snmpagent.parent = self
                self._children_name_map["snmpagent"] = "snmpAgent"
            return self.snmpagent

        if (child_yang_name == "snmpgw"):
            if (self.snmpgw is None):
                self.snmpgw = Confdconfig.Snmpgw()
                self.snmpgw.parent = self
                self._children_name_map["snmpgw"] = "snmpgw"
            return self.snmpgw

        if (child_yang_name == "ssh"):
            if (self.ssh is None):
                self.ssh = Confdconfig.Ssh()
                self.ssh.parent = self
                self._children_name_map["ssh"] = "ssh"
            return self.ssh

        if (child_yang_name == "subagents"):
            if (self.subagents is None):
                self.subagents = Confdconfig.Subagents()
                self.subagents.parent = self
                self._children_name_map["subagents"] = "subagents"
            return self.subagents

        if (child_yang_name == "webui"):
            if (self.webui is None):
                self.webui = Confdconfig.Webui()
                self.webui.parent = self
                self._children_name_map["webui"] = "webui"
            return self.webui

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "aaa" or name == "cli" or name == "encryptedStrings" or name == "hideGroup" or name == "logs" or name == "netconf" or name == "notifications" or name == "opcache" or name == "proxyForwarding" or name == "rest" or name == "restconf" or name == "sessionLimits" or name == "snmpAgent" or name == "snmpgw" or name == "ssh" or name == "subagents" or name == "webui"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Confdconfig()
        return self._top_entity

