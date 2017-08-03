### 2017-08-01 version 0.6.0

#### Python
* Introduced new YDK python [`core`](https://github.com/CiscoDevNet/ydk-py/tree/master/core) package using [pybind11](https://github.com/pybind/pybind11) to wrap around YDK C++ [`core`](https://github.com/CiscoDevNet/ydk-cpp/tree/master/core) ([#507](https://github.com/CiscoDevNet/ydk-gen/pull/507))
  * Introduced `ydk.path` module consisting of APIs to read, manipulate and write YANG data using XPath-like expressions
  * Updated YDK services and providers to internally use the path API
  * Introduced `RestconfServiceProvider` and `OpenDaylightServiceProvider`
  * Updated `NetconfServiceProvider` to be able to download the device yang models on connecting to a device
  * Introduced ability to encode/decode subtree XML in `CodecService` and changed `CRUDService` to use XML subtree filtering to create filters for the `read` operation
  * Added equality/inequality operators to compare YDK model API objects
  * Add option for TCP transport in `NetconfServiceProvider` ([#476](https://github.com/CiscoDevNet/ydk-gen/pull/476), [#444](https://github.com/CiscoDevNet/ydk-gen/pull/444))
  * Support `get`/`get-config` with no filter in path API ([#503](https://github.com/CiscoDevNet/ydk-gen/pull/503))
  * Introduce optimized on-demand yang model downloading for `NetconfServiceProvider` ([#499](https://github.com/CiscoDevNet/ydk-gen/pull/499))
  * Add support for choosing either a per-device or a common cache for storing downloaded yang models ([#502](https://github.com/CiscoDevNet/ydk-gen/pull/502))
  * Introduced encoding/decoding subtree XML in `CodecService` and changed `CRUDService` to use XML subtree filtering to create filters for the `read` operation ([#489](https://github.com/CiscoDevNet/ydk-gen/pull/489))
  * Added support for non-standard RPCs as well in path API ([#498](https://github.com/CiscoDevNet/ydk-gen/pull/498))

#### ydk-gen
* Updated [`cisco-ios-xr`](https://github.com/CiscoDevNet/ydk-gen/blob/master/profiles/bundles/cisco-ios-xr_6_2_2.json) to support Cisco IOS XR 6.2.2 release
* Updated [`cisco-ios-xe`](https://github.com/CiscoDevNet/ydk-gen/blob/master/profiles/bundles/cisco-ios-xe_16_6_1.json) to support Cisco IOS XE 16.6.1 release
* Also updated [`openconfig`](https://github.com/CiscoDevNet/ydk-gen/blob/master/profiles/bundles/openconfig_0_1_3.json) and [`ietf`](https://github.com/CiscoDevNet/ydk-gen/blob/master/profiles/bundles/ietf_0_1_3.json) bundles

#### Note on backward compatibility
The [backward incompatible](http://ydk.cisco.com/py/docs/backward_compatibility.html) changes introduced with `0.6.0` release include:

 * **Installation:** When installing `YDK-Py`, there is a new system requirement which needs to be installed. This is the `libydk` library, which is available on the DevHub website for various OS platforms. Please refer to the [system requirements](https://github.com/CiscoDevNet/ydk-py/blob/master/README.rst#system-requirements) for details.
* **Windows support:** From release ``0.6.0`` onwards, YDK is no longer supported on the Windows platform. We plan to add back support for this platform in the future.
* **API changes:** Please refer to the [developer guide](http://ydk.cisco.com/py/docs/developer_guide.html) and [API guide](http://ydk.cisco.com/py/docs/api_guide.html) for details about APIs and how to use them.
   * `NetconfServiceProvider` no longer has the `close()` method. There is no need to explicitly close the provider as it will be automatically cleaned up when the object goes out of scope.
   * `YFilter` has replaced the functionality of the `READ` and `DELETE` objects
   * When using logging, the suggested level for users of YDK is `INFO` as `DEBUG` provides highly detailed logging suitable for dvelopers working on YDK
   * The type names of `enumerations` and `identities` no longer have `Enum` or `Identity` in their names. For example, the  identity `InterfaceTypeIdentity` in `ydk.models.ietf.ietf_interfaces` is now renamed to just `InterfaceType`.
   * The `is_config()` method is no longer available for the YDK model APIs. This may be added back in a future release.

### 2017-06-06 version 0.5.5

* Fixed bundle `setup.py` to match ydk `core` dependency in bundle profile ([#433](https://github.com/CiscoDevNet/ydk-gen/issues/443))
* Updated `lxml` dependency for ydk `core` package ([#427](https://github.com/CiscoDevNet/ydk-gen/issues/427))
* Improved reading of data using `ExecutorService` ([#332](https://github.com/CiscoDevNet/ydk-gen/issues/332)) and `CRUDService` ([#457](https://github.com/CiscoDevNet/ydk-gen/issues/457))
* Fixed encoding key elements of yang `list`s ([#363](https://github.com/CiscoDevNet/ydk-gen/issues/363)) and operational data ([#452](https://github.com/CiscoDevNet/ydk-gen/issues/452), [#455](https://github.com/CiscoDevNet/ydk-gen/issues/455))
* Added [`cisco-ios-xe` bundle](https://github.com/CiscoDevNet/ydk-gen/blob/master/profiles/bundles/cisco-ios-xe_16_5_1.json) to support Cisco IOS XE 16.5.1 release

#### Documentation
* Improved getting-started guides for YDK-Py and YDK-Cpp  ([#418](https://github.com/CiscoDevNet/ydk-gen/pull/418), [#419](https://github.com/CiscoDevNet/ydk-gen/pull/419))
* Made table of contents for bundle documentation be sorted alphabetically ([#446](https://github.com/CiscoDevNet/ydk-gen/pull/418), [#419](https://github.com/CiscoDevNet/ydk-gen/pull/446))
* Improved documentation of `rpc` classes ([#435](https://github.com/CiscoDevNet/ydk-gen/issues/435))

### 2017-03-17 version 0.5.4

 * Improved logging to indicate message directionality ([#388](https://github.com/CiscoDevNet/ydk-gen/pull/388))
 * Provide more details for validation error message for leaf-lists ([#398](https://github.com/CiscoDevNet/ydk-gen/pull/398))
 * Remove indirect python requirements from `setup.py` ([#392](https://github.com/CiscoDevNet/ydk-gen/pull/392))
 * If validation error occurs when decoding payload, include payload as an attribute of the `YPYModelError` raised ([#381](https://github.com/CiscoDevNet/ydk-gen/pull/381))
 * Updated [`cisco-ios-xr` bundle](https://github.com/CiscoDevNet/ydk-gen/blob/master/profiles/bundles/cisco-ios-xr_6_2_1.json) to support Cisco IOS XR 6.2.1 release

#### Documentation
 * Separated top data classes from type classes in table of contents ([#372](https://github.com/CiscoDevNet/ydk-gen/pull/372))
 * Fixed ydk version not being correctly printed for C++ documentation ([#374](https://github.com/CiscoDevNet/ydk-gen/pull/374))
 * Indicate bundle version in C++ and python bundle documentation ([#383](https://github.com/CiscoDevNet/ydk-gen/pull/383))

### 2017-01-30 version 0.5.3:

* Fixed issues with netconf service ([#323](https://github.com/CiscoDevNet/ydk-gen/issues/323), [#305](https://github.com/CiscoDevNet/ydk-gen/issues/305))
* Disambiguated model API classes called 'None' ([#318](https://github.com/CiscoDevNet/ydk-gen/issues/318))
* Removed 'Bits' from classes representing bits leafs ([#318](https://github.com/CiscoDevNet/ydk-gen/issues/318), [#320](https://github.com/CiscoDevNet/ydk-gen/issues/320))

### Documentation

* Included model revision in documentation ([#272](https://github.com/CiscoDevNet/ydk-gen/issues/272))
* Improved documentation for string leafs ([#346](https://github.com/CiscoDevNet/ydk-gen/issues/346)), decimal64 leafs ([#300](https://github.com/CiscoDevNet/ydk-gen/issues/300), [#294](https://github.com/CiscoDevNet/ydk-gen/issues/294))
* Improved look and feel of documentation ([#361](https://github.com/CiscoDevNet/ydk-gen/pull/361), [#356](https://github.com/CiscoDevNet/ydk-gen/pull/356))

### 2016-11-30 version 0.5.2:

* CRUD service / Codec service / Netconf service improvements
  * Improved error handling for mismatched model API types ([#241](https://github.com/CiscoDevNet/ydk-gen/issues/241))
  * Fixed issues with certain operations in netconf service ([#247](https://github.com/CiscoDevNet/ydk-gen/issues/247), [#248](https://github.com/CiscoDevNet/ydk-gen/issues/248), [#252](https://github.com/CiscoDevNet/ydk-gen/issues/252), [#235](https://github.com/CiscoDevNet/ydk-gen/issues/235))
  * Fixed issue with CRUD service identityref keys ([#257](https://github.com/CiscoDevNet/ydk-gen/issues/257))

* Bundle improvements
  * Made generate.py executable ([#227](https://github.com/CiscoDevNet/ydk-gen/issues/227))
  * Removed auto capitalization of enum literals ([#230](https://github.com/CiscoDevNet/ydk-gen/issues/230))
  * Updated [`cisco-ios-xr` bundle](https://github.com/CiscoDevNet/ydk-gen/blob/master/profiles/bundles/cisco-ios-xr_6_1_2.json) to support Cisco IOS XR 6.1.2 release ([#316](https://github.com/CiscoDevNet/ydk-gen/pull/316))
  
* Logging improvements
  * Improved logging for services and providers ([#251](https://github.com/CiscoDevNet/ydk-gen/issues/251), [#254](https://github.com/CiscoDevNet/ydk-gen/issues/254), [#280](https://github.com/CiscoDevNet/ydk-gen/issues/280), [#283](https://github.com/CiscoDevNet/ydk-gen/issues/283), [#284](https://github.com/CiscoDevNet/ydk-gen/issues/284))

* Documentation improvements
  * Added YDK logos and reorganized to be more readable ([#301](https://github.com/CiscoDevNet/ydk-gen/pull/301), [#296](https://github.com/CiscoDevNet/ydk-gen/pull/296), [#289](https://github.com/CiscoDevNet/ydk-gen/pull/289))
  * Improved documentation of YANG attributes like data type (configuration or state), default value, units, status etc ([#249](https://github.com/CiscoDevNet/ydk-gen/issues/249), [#290](https://github.com/CiscoDevNet/ydk-gen/issues/290))  
  * Improved netconf service documentation ([#235](https://github.com/CiscoDevNet/ydk-gen/issues/235))

### 2016-10-10 version 0.5.1:

* Support for Python3
  * Introduced support for Python 3 ([#60](https://github.com/CiscoDevNet/ydk-gen/issues/60))
  * Both Python 2 and Python 3 are now supported for `ydk-gen` and `ydk-py`

* Bundle improvements
  * Improved usage of import statements in YDK model API to reduce chances of circular import dependency ([#216](https://github.com/CiscoDevNet/ydk-gen/issues/216))
  * Updated [`cisco-ios-xr` bundle](https://github.com/CiscoDevNet/ydk-gen/blob/master/profiles/bundles/cisco-ios-xr_6_1_1.json) to support Cisco IOS XR 6.1.1 release ([#258](https://github.com/CiscoDevNet/ydk-gen/pull/258))
  * Updated [`openconfig` bundle](https://github.com/CiscoDevNet/ydk-gen/blob/master/profiles/bundles/openconfig_0_1_1.json) ([#258](https://github.com/CiscoDevNet/ydk-gen/pull/258))

* Documentation improvements
  * Improved documentation for bundle installation ([#244](https://github.com/CiscoDevNet/ydk-gen/pull/244))
  * Added documentation for executor service ([#263](https://github.com/CiscoDevNet/ydk-gen/pull/263))

### 2016-08-03 version 0.5.0:
 * Introduced YDK bundles ([#43](https://github.com/CiscoDevNet/ydk-gen/issues/43), [#148](https://github.com/CiscoDevNet/ydk-gen/issues/148), [#149](https://github.com/CiscoDevNet/ydk-gen/issues/149))
  * Created YDK core library and pluggable namespace packages that share the same module prefix `ydk.models`
  * Generated documentation for YDK core and bundles

* CRUD service / Codec service / Netconf service improvements
  * Improved support for presence containers, nested enum and identity classes ([#169](https://github.com/CiscoDevNet/ydk-gen/pull/169))
  * Improved support for lists with multiple keys by ensuring that the order of keys is preserved ([#179](https://github.com/CiscoDevNet/ydk-gen/issues/179))
  * Improved support for leaf-list of identity type ([#186](https://github.com/CiscoDevNet/ydk-gen/issues/186))
  * Added check for user error which can occur when self-referencing YDK object as parent object ([#184](https://github.com/CiscoDevNet/ydk-gen/issues/184))
  * Improved error-reporting for commit-time error ([#190](https://github.com/CiscoDevNet/ydk-gen/issues/190))
  * Fixed CRUD read support for modules containing top-level list ([#194](https://github.com/CiscoDevNet/ydk-gen/issues/194))

* Testing improvements
  * Added Mac OS X installation and running codec service sanity tests to CI ([#175](https://github.com/CiscoDevNet/ydk-gen/pull/175))

* Documentation improvements
  * Indicated mandatory leafs in the documentation ([#177](https://github.com/CiscoDevNet/ydk-gen/issues/177))
  * Specified path to referred leaf for leafrefs ([#177](https://github.com/CiscoDevNet/ydk-gen/issues/177))
  * Fix documentation of presence containers ([#192](https://github.com/CiscoDevNet/ydk-gen/issues/192))
  * Enhanced documentation of leafs of identityref type by indicating all the subclasses of identity base class referred to by the identityref ([#161](https://github.com/CiscoDevNet/ydk-gen/issues/161))
  * Added documentation on how to use YDK delete operation and improved documentation for YDK read operation ([#204](https://github.com/CiscoDevNet/ydk-gen/pull/204))

### 2016-06-17 version 0.4.2:
 * Error handling improvements
  * Fixed local validation to correctly check for types and values ([#116](https://github.com/CiscoDevNet/ydk-gen/issues/116))
  * Introduced error hierarchy to represent errors from various components, viz.: YPYModelErrors, YPYServiceError, YPYServiceProviderError ([#133](https://github.com/CiscoDevNet/ydk-gen/issues/133))
    * When raising YPYModelErrors, include errors dictionary with key as path to data, and value as tuple of error code and error message
  * Added more extensive negative test cases to ydk-gen to test handling of error ([#134](https://github.com/CiscoDevNet/ydk-gen/issues/134))
 * CRUD service / Codec service / Netconf service provider improvements
  * Added support for multiple objects to codec service ([#122](https://github.com/CiscoDevNet/ydk-gen/issues/122))
  * Added logging for codec service ([#97](https://github.com/CiscoDevNet/ydk-gen/issues/97))
  * Have logging hierarchy automatically follow package hierarchy ([#100](https://github.com/CiscoDevNet/ydk-gen/issues/100))
  * Have netconf service return YDK python objects instead of XML strings ([#120](https://github.com/CiscoDevNet/ydk-gen/issues/120))
  * Fixed decoding issue with leaf-list of enums ([#150](https://github.com/CiscoDevNet/ydk-gen/issues/150))
 * Removed requirements.txt from ydk-py and added all requirements to setup.py
 * Enforce PEP8 naming for Identity classes ([#152](https://github.com/CiscoDevNet/ydk-gen/issues/152))
 * Added full ydk-py version to the documentation ([#144](https://github.com/CiscoDevNet/ydk-gen/issues/144))

### 2016-05-20 version 0.4.1:
 * Added openconfig bgp-policy APIs to ydk-py ([#102](https://github.com/CiscoDevNet/ydk-gen/issues/102))
 * Introduced ability to programmatically retrieve SDK version of ydk-py ([#8](https://github.com/CiscoDevNet/ydk-gen/issues/8))
 * Removed unused dependencies from ydk-py's requirements.txt ([#48](https://github.com/CiscoDevNet/ydk-gen/issues/48))
 * Introduced [coveralls](https://coveralls.io) and improved [travis CI](https://travis-ci.org) integration for ydk-gen github ([#84](https://github.com/CiscoDevNet/ydk-gen/issues/84), [#54](https://github.com/CiscoDevNet/ydk-gen/issues/54), [#15](https://github.com/CiscoDevNet/ydk-gen/issues/15), [#46](https://github.com/CiscoDevNet/ydk-gen/issues/46))
 * CRUD service / Netconf service provider improvements
  * Added timeout parameter to NetconfServiceProvider ([#1](https://github.com/CiscoDevNet/ydk-gen/issues/1))
  * Fixed issues with decoding leafs of union type and nodes defined in sub-modules  ([#5](https://github.com/CiscoDevNet/ydk-gen/issues/5), [#56](https://github.com/CiscoDevNet/ydk-gen/issues/56))
  * Fixed issue with encoding enums, identities defined in external modules ([#30](https://github.com/CiscoDevNet/ydk-gen/issues/30), [#103](https://github.com/CiscoDevNet/ydk-gen/issues/103))
  * Improved support for deleting leafs, leaf-lists and lists ([#55](https://github.com/CiscoDevNet/ydk-gen/issues/55), [#103](https://github.com/CiscoDevNet/ydk-gen/issues/103))
 * Documentation improvements
  * Added 'About ydk-py' page with information about ydk-gen used to generate ydk-py ([#6](https://github.com/CiscoDevNet/ydk-gen/issues/6))
  * Indicate in documentation YDK class attributes that are keys ([#41](https://github.com/CiscoDevNet/ydk-gen/issues/41))
  * Made top containers show up at the top of the table of contents for every module document ([#39](https://github.com/CiscoDevNet/ydk-gen/issues/39))

### 2016-04-15 version 0.4.0:

  * Introduced netconf service and codec service
    * Netconf service provides APIs to execute netconf operations
    * Codec service provides APIs to encode python objects and decode payloads
  * Support for yang deviation
  * Support for subscribing to model-driven telemetry
  * Logging made more consistent
    * CRUDService outputs type of operation
    * When logging is enabled, all NETCONF messages are logged including commit
    * Log messages at various stages (send RPC request, receive reply, commit 
      etc) instead of logging all at once at the end
  * Updated enums in YDK classes to use enum34
    * Improved enum documentation
  * Improved error reporting for ydk-py and ydk-gen

### 2016-03-11 version 0.3.0:

  * First public release.
