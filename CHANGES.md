**2016-05-20 version 0.4.1:**
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

**2016-04-15 version 0.4.0:**

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

**2016-03-11 version 0.3.0:**

  * First public release.
