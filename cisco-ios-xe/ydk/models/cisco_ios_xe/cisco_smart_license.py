""" cisco_smart_license 

Smart licensing configuration, RPC, notification and operational data.

Copyright (c) 2016\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class AuthorizationStateEnum(Enum):
    """
    AuthorizationStateEnum (Enum Class)

    The smart licensing authorization state.

    .. data:: auth_state_none = 0

    	No licenses are in use so there is no authorization 

    	state to report.

    .. data:: auth_state_eval = 1

    	Evaluation period is in use and is counting down.

    .. data:: auth_state_eval_expired = 2

    	Evaluation period in use but it has expired.

    .. data:: auth_state_authorized = 3

    	All license usage is authorized and within terms 

    	of the customer's contract.

    .. data:: auth_state_authorized_reservation = 4

    	All license usage is authorized because a  

    	reservation authorization code is installed.

    .. data:: auth_state_out_of_compliance = 5

    	License usage is out of compliance with the 

    	terms of the contract. Either too many licenses are in

    	use or licenses that were not purchased are in use.

    .. data:: auth_state_authorization_expired = 6

    	The authorization period has expired because this

    	product instance has not communicated with the

    	SSM or satellite in over 90 days.

    """

    auth_state_none = Enum.YLeaf(0, "auth-state-none")

    auth_state_eval = Enum.YLeaf(1, "auth-state-eval")

    auth_state_eval_expired = Enum.YLeaf(2, "auth-state-eval-expired")

    auth_state_authorized = Enum.YLeaf(3, "auth-state-authorized")

    auth_state_authorized_reservation = Enum.YLeaf(4, "auth-state-authorized-reservation")

    auth_state_out_of_compliance = Enum.YLeaf(5, "auth-state-out-of-compliance")

    auth_state_authorization_expired = Enum.YLeaf(6, "auth-state-authorization-expired")


class EnforcementModeEnum(Enum):
    """
    EnforcementModeEnum (Enum Class)

    For an entitlement tag (license) that is in use this enumeration

     tells us how the license is being enforced.

    .. data:: enforcement_waiting = 0

    	The initial state after an entitlement request while we are waiting 

    	the Authorization request response. In this mode the device will 

    	have established communications with Cisco and successfully 

    	registered with the Cisco Licensing cloud.

    .. data:: enforcement_in_compliance = 1

    	Cisco Smart Software Manager (CSSM) has responded that

    	the entitlement requested is in compliance.

    .. data:: enforcement_out_of_compliance = 2

    	Cisco Smart Software Manager (CSSM) has responded that

    	the entitlement requested is out of compliance. 

    	either too many licenses /entitlements are in use or the license 

    	has not been purchased

    .. data:: enforcement_overage = 3

    	more licenses are in use than were purchased but the customer

    	 is still within the terms of their contract

    .. data:: enforcement_evaluation = 4

    	The evaluation period is in use.

    	It will remain in use until the following

    	two messages have been received by the product from the 

    	Cisco Smart Software Manager (CSSM):

    	 Successful response to a registration request,

    	 successful response to an entitlement authorization request

    .. data:: enforcement_evaluation_expired = 5

    	The evaluation period has expired

    .. data:: enforcement_authorization_expired = 6

    	Authorization period has expired. This will occur if the product

    	has not been able to communicate with Cisco or a satellite 

    	for an extended period of time, usually 90 days.

    .. data:: enforcement_reservation_in_compliance = 7

    	The entitlement requested is in compliance because 

    	a reservation authorization code is installed and the product

    	is in Permanent License Reservation mode.

    .. data:: enforcement_invalid_tag = 8

    	The entitlement tag is invalid.

    	The CSSM does not recognize the entitlement tag

    	because it is not in the database. This usually only occurs

    	during testing.

    .. data:: enforcement_disabled = 9

    	Smart licensing has been disabled. The feature using this license

    	should be disabled.

    """

    enforcement_waiting = Enum.YLeaf(0, "enforcement-waiting")

    enforcement_in_compliance = Enum.YLeaf(1, "enforcement-in-compliance")

    enforcement_out_of_compliance = Enum.YLeaf(2, "enforcement-out-of-compliance")

    enforcement_overage = Enum.YLeaf(3, "enforcement-overage")

    enforcement_evaluation = Enum.YLeaf(4, "enforcement-evaluation")

    enforcement_evaluation_expired = Enum.YLeaf(5, "enforcement-evaluation-expired")

    enforcement_authorization_expired = Enum.YLeaf(6, "enforcement-authorization-expired")

    enforcement_reservation_in_compliance = Enum.YLeaf(7, "enforcement-reservation-in-compliance")

    enforcement_invalid_tag = Enum.YLeaf(8, "enforcement-invalid-tag")

    enforcement_disabled = Enum.YLeaf(9, "enforcement-disabled")


class ErrorEnum(Enum):
    """
    ErrorEnum (Enum Class)

    Smart License error codes returned by 

    Smart Licensing RPC calls

    .. data:: success = 0

    	Success

    .. data:: malloc = 1

    	Malloc Error

    .. data:: nullpointer = 2

    	Null pointer Error

    .. data:: error3 = 3

    	deprecated DO NOT remove

    .. data:: error4 = 4

    	deprecated DO NOT remove

    .. data:: error5 = 5

    	deprecated DO NOT remove

    .. data:: BadInputParams = 6

    	Bad input parameter

    .. data:: error7 = 7

    	deprecated DO NOT remove

    .. data:: badhandle = 8

    	Bad handle

    .. data:: notfound = 9

    	The requested item was not found

    .. data:: notsupported = 10

    	The requested operation is not supported

    .. data:: alreadyinit = 11

    	Init failed because the agent is already initialized

    .. data:: notinit = 12

    	API failed because the agent is not initialized

    .. data:: smfailtocreate = 13

    	State machine creation failed

    .. data:: smfailtorun = 14

    	State machine not running

    .. data:: smfailtoinit = 15

    	State machine failed to init

    .. data:: smfailtodestroy = 16

    	State machine failed to destroy

    .. data:: msgparse = 17

    	message parsing error

    .. data:: msgbuild = 18

    	message building error

    .. data:: notenabled = 19

    	Smart Agent not enabled

    .. data:: invalidrequest = 20

    	Smart Agent request invalid

    .. data:: init = 21

    	General initialization error. We call a number of 

    	system routines to 

    	initialize system resources and we can't translate their error 

    	codes to Smart Agent error codes. The log should have a detailed 

    	description of the error.

    .. data:: failtosetstate = 22

    	Smart Agent Fail to set state

    .. data:: unsupportedresponse = 23

    	Unsupported response type

    .. data:: invalidresponse = 24

    	Invalid response type

    .. data:: storagefailtostore = 25

    	Smart Agent Trusted Storage failed to store*

    .. data:: storagefailtoretrieve = 26

    	Smart Agent Trusted Storage failed to retrieve*

    .. data:: nullccoidtoken = 27

    	Null CCOId and IdToken

    .. data:: matchidentifier = 28

    	Product Instance identifier failed to match

    .. data:: matchvendor = 29

    	Vendor string failed to match

    .. data:: matchnonce = 30

    	nonce failed to match

    .. data:: commdisabled = 31

    	communication channel error. Comm layer (call home) is disabled 

    .. data:: commsend = 32

    	Call Home message send error. probably a timeout so we

    	will retry the send. any other error from the comm send should

    	be a permanent failure

    .. data:: commresponse = 33

    	Call Home message send response error

    .. data:: communkown = 34

    	Call Home unknown error

    .. data:: smpostnotallow = 35

    	State machine Operation not permitted

    .. data:: reqmsgmissingmandatoryfield = 36

    	Missing mandatory field in request message

    .. data:: responsefailed = 37

    	We received a failure status in a response message.

    	The log will contain a error message

    .. data:: pinotinit = 38

    	PI not initialized 

    .. data:: alreadyenabled = 39

    	The agent cannot be enabled more than once

    .. data:: alreadyregistered = 40

    	The agent is already registered

    .. data:: certinvalid = 41

    	The certificate is invalid 

    .. data:: certexpired = 42

    	The certificate has expired 

    .. data:: notregistered = 43

    	The agent is not registered 

    .. data:: csrgenerationfailed = 44

    	The CSR generation failed 

    .. data:: verifysignaturefailed = 45

    	Signature Verification failed 

    .. data:: generatesignaturefailed = 46

    	Signature Generation failed 

    .. data:: signcertverificationfailed = 47

    	Signing Certificate Verification failed 

    .. data:: nodecertverificationfailed = 48

    	Node Certificate Verification failed 

    .. data:: parsecertificatefailed = 49

    	Certificate Parsing failed 

    .. data:: cryptorootcaimportfailed = 50

    	Root Certificate Import failed 

    .. data:: taginvalid = 51

    	The tag is invalid 

    .. data:: standby = 52

    	Smart agent is running on a standby RP 

    .. data:: registrationinprogress = 53

    	Smart agent id token registration is in progress

    .. data:: commretry = 54

    	Call Home is not ready because it is in restart ipc

    .. data:: authrenewinprogress = 55

    	Smart agent authorization renew is in progress

    .. data:: idcertrenewinprogress = 56

    	Smart agent id certificate renew is in progress

    .. data:: noudichange = 57

    	Udi List Has Not been changed 

    .. data:: callhomeserviceoff = 58

    	Call home service cannot be turned on. 

    .. data:: msgexecinprogress = 59

    	message execution already in progress

    .. data:: msgexecinproglocked = 60

    	message execution in progress flag is locked

    .. data:: certmatchessubsetudis = 61

    	The ID cert only matches some of the system Udi's

    .. data:: storagegroupchangeincomplete = 62

    	A Storage group has not all been changed

    .. data:: storagemgmtnotinit = 63

    	Storage Management is not Init

    .. data:: tspathnotchanged = 64

    	TS System Path list is not changed 

    .. data:: cryptoinitnotcompleted = 65

    	Crypto Initialization is not completed

    .. data:: notinunidentified = 66

    	The agent is not in unidentified state 

    .. data:: platformpathinvalid = 67

    	The platform provided path is invalid 

    .. data:: platformudiinvalid = 68

    	The platform provided UDI is invalid 

    .. data:: storageobjfailtocreate = 69

    	failed to create Trusted Store object 

    .. data:: storageobjfailtoerase = 70

    	failed to erase trusted store object 

    .. data:: storageobjdoesnotexist = 71

    	trusted storage object/file does not exist

    .. data:: messageeventexceedspeer = 72

    	The message event is beyond the peer 

    .. data:: codevalidationfailed = 73

    	Validation of the authorization key failed.

    	It probably does not match the UDI. The device will go to

    	the unidentified state (not registered)

    .. data:: reserved = 74

    	operation not supported because the agent is running in

    	permanent License reservation mode

    .. data:: noreservationinprogress = 75

    	No license reservation is in progress 

    .. data:: noauthorizationinstalled = 76

    	No authorization code instaled in device 

    .. data:: reservationmismatch = 77

    	The reservation authorization code does not match the 

    	reservation request code

    .. data:: notreservationmode = 78

    	not in license reservation mode 

    .. data:: reservationerror = 79

    	 General reservation error. This is used with the API 

    	functions that are called by the CLI. the API will return a 

    	very specific displayString that describes the error.

    .. data:: sysmgrinit = 80

    	Sysmgr Init Failed 

    .. data:: alreadyexists = 81

    	Generic error for something already existing 

    .. data:: listinsertfailed = 82

    	Error in object insert to xos list 

    .. data:: sessionmgmtnotinit = 83

    	Session management not initialized

    .. data:: listinitfailed = 84

    	Error Creating Linked List

    .. data:: listbusy = 85

    	List in use

    .. data:: noclients = 86

    	No Connected Clients 

    .. data:: ipc = 87

    	Generic IPC layer error 

    .. data:: ipcopen = 88

    	The IPC socket open error 

    .. data:: ipcinit = 89

    	The IPC Initialization error 

    .. data:: ipcconnect = 90

    	The IPC Connection error 

    .. data:: ipcevents = 91

    	The IPC Server Event error 

    .. data:: ipcmgmt = 92

    	The IPC Management error 

    .. data:: ipcsend = 93

    	The IPC Send error 

    .. data:: ipcreceive = 94

    	The IPC Recevive error 

    .. data:: ipctimeout = 95

    	The IPC Recevive error 

    .. data:: enqueuefailed = 96

    	Failed to enqueue a message to the IPC Queue

    .. data:: dequeuefailed = 97

    	Failed to dequeue a message from the IPC queue

    .. data:: shuttingdown = 98

    	Fail because we are about to shutdown and we need

    	to stop processing any more messages or responses

    .. data:: couldnotvalidatetrustchain = 99

    	Could not validate Trust Chain

    .. data:: reservationalreadyinstalled = 100

    	The reservation authorization code is already installed 

    .. data:: reservationinstallparsefail = 101

    	Failed to parse reservation authorization code 

    .. data:: base64encoding = 102

    	Base64 encoding failed 

    .. data:: base64decoding = 103

    	Base64 decoding failed 

    .. data:: invalidsoftwareidtag = 104

    	Failed to find UUID inside software id tag 

    .. data:: certificatemismatch = 105

    	Development certificates are being used with Production 

    	Root certificate 

    .. data:: noreservation = 106

    	No License Reservation 

    .. data:: agentunreachable = 107

    	the agent Daemon is unreachable 

    .. data:: ignoreevent = 108

    	the agent ignores event 

    .. data:: b58overflow = 109

    	Base58 overflow, number too large. 

    .. data:: b58decode = 110

    	Base58 decode error. 

    .. data:: b58badlen = 111

    	Bad base58 length. 

    .. data:: b58invdigit = 112

    	Invalid base58 digit. 

    .. data:: b58decodeoverflow = 113

    	Overflow detected during base58 decode. 

    .. data:: reservationversionoutofbound = 114

    	Reservation version out of bound 

    .. data:: base58encode = 115

    	General Base58 encoding error 

    .. data:: duplicatedentry = 116

    	General error code for adding item that already exists. 

    	Used in App HA setup when adding an HA peer device info that 

    	is already added 

    .. data:: missingentry = 117

    	General error code for trying to remove item that do 

    	not exist. Used in App HA setup when removing an HA peer device 

    	info that does not exist

    .. data:: badpeerinfoformat = 118

    	The given peer info contain incorrect data format 

    .. data:: badapplicationhaattributedataset = 119

    	The given handle attribute list contains incomplete

    	application HA attributes

    .. data:: reservationinprogress = 120

    	license reservation is in progress 

    .. data:: xdmcreatehandle = 121

    	The xos_dm_create() failure causes this error code to be return 

    .. data:: versionmismatchinentitlementrsp = 122

    	Version in entitlement response message does not match 

    	with the

    	one already saved from last completed response message. We need

    	to send entitlemeent request again with proper version and data

    .. data:: harolenotsupported = 123

    	Given valid HA Role is not supported by this operation. 

    	For Application HA valid roles are Active or Standby.

    .. data:: apphainvalidcharacter = 124

    	Application HA attribute contains invalid character.  

    	Character set supported is alphanumeric.

    .. data:: apphaaddpeerfromsamedevice = 125

    	The peer info given is from the same device. 

    .. data:: apphaappduplicatedinstance = 126

    	When setting Application HA Attribute, a different 

    	handle with exactly

    	same tag, app ha name, app ha id exists in the agent.

    .. data:: versionmismatchinregresponse = 127

    	Backend server does not support AppHA enabled message 

    	version. So

    	registration response (from backend) received with status set as 

    	FAILED or VERSION_TOO_HIGH.

    .. data:: conversionnocb = 128

    	Migration function was called but there are no i

    	call backs registered 

    .. data:: conversionnotallowed = 129

    	Migration was not enabled with the 

    	MIGRATION_ALLOWED property 

    .. data:: conversioninprogress = 130

    	Migration is in progress 

    .. data:: conversionalreadystarted = 131

    	Migration has already been started 

    .. data:: conversionnotenabled = 132

    	Migration is not enabled 

    .. data:: versionconversionnotsupported = 133

    	The backend derver this device is connected to does 

    	not support conversion

    .. data:: noconversioninprogress = 134

    	No conversion in progress

    .. data:: cryptoversionmismatch = 135

    	Loaded OpenSSL version is not the same as used for 

    	development

    .. data:: conversionstoppedpartially = 136

    	Some Smart Licensing Conversion jobs stopped successfully

    .. data:: utilityenabled = 137

    	Operation is not supported because Utility management 

    	is enabled

    .. data:: utilitynotenabled = 138

    	Utility is not enabled

    .. data:: transportnotavailable = 139

    	Transport layer not abvailable

    .. data:: fqdn = 140

    	Unable to get FQDN

    .. data:: thirdparty = 141

    	The current transport type does not support this feature

    .. data:: transporttype = 142

    	The transport type needed is not configured

    .. data:: max = 143

    	max error code

    """

    success = Enum.YLeaf(0, "success")

    malloc = Enum.YLeaf(1, "malloc")

    nullpointer = Enum.YLeaf(2, "nullpointer")

    error3 = Enum.YLeaf(3, "error3")

    error4 = Enum.YLeaf(4, "error4")

    error5 = Enum.YLeaf(5, "error5")

    BadInputParams = Enum.YLeaf(6, "BadInputParams")

    error7 = Enum.YLeaf(7, "error7")

    badhandle = Enum.YLeaf(8, "badhandle")

    notfound = Enum.YLeaf(9, "notfound")

    notsupported = Enum.YLeaf(10, "notsupported")

    alreadyinit = Enum.YLeaf(11, "alreadyinit")

    notinit = Enum.YLeaf(12, "notinit")

    smfailtocreate = Enum.YLeaf(13, "smfailtocreate")

    smfailtorun = Enum.YLeaf(14, "smfailtorun")

    smfailtoinit = Enum.YLeaf(15, "smfailtoinit")

    smfailtodestroy = Enum.YLeaf(16, "smfailtodestroy")

    msgparse = Enum.YLeaf(17, "msgparse")

    msgbuild = Enum.YLeaf(18, "msgbuild")

    notenabled = Enum.YLeaf(19, "notenabled")

    invalidrequest = Enum.YLeaf(20, "invalidrequest")

    init = Enum.YLeaf(21, "init")

    failtosetstate = Enum.YLeaf(22, "failtosetstate")

    unsupportedresponse = Enum.YLeaf(23, "unsupportedresponse")

    invalidresponse = Enum.YLeaf(24, "invalidresponse")

    storagefailtostore = Enum.YLeaf(25, "storagefailtostore")

    storagefailtoretrieve = Enum.YLeaf(26, "storagefailtoretrieve")

    nullccoidtoken = Enum.YLeaf(27, "nullccoidtoken")

    matchidentifier = Enum.YLeaf(28, "matchidentifier")

    matchvendor = Enum.YLeaf(29, "matchvendor")

    matchnonce = Enum.YLeaf(30, "matchnonce")

    commdisabled = Enum.YLeaf(31, "commdisabled")

    commsend = Enum.YLeaf(32, "commsend")

    commresponse = Enum.YLeaf(33, "commresponse")

    communkown = Enum.YLeaf(34, "communkown")

    smpostnotallow = Enum.YLeaf(35, "smpostnotallow")

    reqmsgmissingmandatoryfield = Enum.YLeaf(36, "reqmsgmissingmandatoryfield")

    responsefailed = Enum.YLeaf(37, "responsefailed")

    pinotinit = Enum.YLeaf(38, "pinotinit")

    alreadyenabled = Enum.YLeaf(39, "alreadyenabled")

    alreadyregistered = Enum.YLeaf(40, "alreadyregistered")

    certinvalid = Enum.YLeaf(41, "certinvalid")

    certexpired = Enum.YLeaf(42, "certexpired")

    notregistered = Enum.YLeaf(43, "notregistered")

    csrgenerationfailed = Enum.YLeaf(44, "csrgenerationfailed")

    verifysignaturefailed = Enum.YLeaf(45, "verifysignaturefailed")

    generatesignaturefailed = Enum.YLeaf(46, "generatesignaturefailed")

    signcertverificationfailed = Enum.YLeaf(47, "signcertverificationfailed")

    nodecertverificationfailed = Enum.YLeaf(48, "nodecertverificationfailed")

    parsecertificatefailed = Enum.YLeaf(49, "parsecertificatefailed")

    cryptorootcaimportfailed = Enum.YLeaf(50, "cryptorootcaimportfailed")

    taginvalid = Enum.YLeaf(51, "taginvalid")

    standby = Enum.YLeaf(52, "standby")

    registrationinprogress = Enum.YLeaf(53, "registrationinprogress")

    commretry = Enum.YLeaf(54, "commretry")

    authrenewinprogress = Enum.YLeaf(55, "authrenewinprogress")

    idcertrenewinprogress = Enum.YLeaf(56, "idcertrenewinprogress")

    noudichange = Enum.YLeaf(57, "noudichange")

    callhomeserviceoff = Enum.YLeaf(58, "callhomeserviceoff")

    msgexecinprogress = Enum.YLeaf(59, "msgexecinprogress")

    msgexecinproglocked = Enum.YLeaf(60, "msgexecinproglocked")

    certmatchessubsetudis = Enum.YLeaf(61, "certmatchessubsetudis")

    storagegroupchangeincomplete = Enum.YLeaf(62, "storagegroupchangeincomplete")

    storagemgmtnotinit = Enum.YLeaf(63, "storagemgmtnotinit")

    tspathnotchanged = Enum.YLeaf(64, "tspathnotchanged")

    cryptoinitnotcompleted = Enum.YLeaf(65, "cryptoinitnotcompleted")

    notinunidentified = Enum.YLeaf(66, "notinunidentified")

    platformpathinvalid = Enum.YLeaf(67, "platformpathinvalid")

    platformudiinvalid = Enum.YLeaf(68, "platformudiinvalid")

    storageobjfailtocreate = Enum.YLeaf(69, "storageobjfailtocreate")

    storageobjfailtoerase = Enum.YLeaf(70, "storageobjfailtoerase")

    storageobjdoesnotexist = Enum.YLeaf(71, "storageobjdoesnotexist")

    messageeventexceedspeer = Enum.YLeaf(72, "messageeventexceedspeer")

    codevalidationfailed = Enum.YLeaf(73, "codevalidationfailed")

    reserved = Enum.YLeaf(74, "reserved")

    noreservationinprogress = Enum.YLeaf(75, "noreservationinprogress")

    noauthorizationinstalled = Enum.YLeaf(76, "noauthorizationinstalled")

    reservationmismatch = Enum.YLeaf(77, "reservationmismatch")

    notreservationmode = Enum.YLeaf(78, "notreservationmode")

    reservationerror = Enum.YLeaf(79, "reservationerror")

    sysmgrinit = Enum.YLeaf(80, "sysmgrinit")

    alreadyexists = Enum.YLeaf(81, "alreadyexists")

    listinsertfailed = Enum.YLeaf(82, "listinsertfailed")

    sessionmgmtnotinit = Enum.YLeaf(83, "sessionmgmtnotinit")

    listinitfailed = Enum.YLeaf(84, "listinitfailed")

    listbusy = Enum.YLeaf(85, "listbusy")

    noclients = Enum.YLeaf(86, "noclients")

    ipc = Enum.YLeaf(87, "ipc")

    ipcopen = Enum.YLeaf(88, "ipcopen")

    ipcinit = Enum.YLeaf(89, "ipcinit")

    ipcconnect = Enum.YLeaf(90, "ipcconnect")

    ipcevents = Enum.YLeaf(91, "ipcevents")

    ipcmgmt = Enum.YLeaf(92, "ipcmgmt")

    ipcsend = Enum.YLeaf(93, "ipcsend")

    ipcreceive = Enum.YLeaf(94, "ipcreceive")

    ipctimeout = Enum.YLeaf(95, "ipctimeout")

    enqueuefailed = Enum.YLeaf(96, "enqueuefailed")

    dequeuefailed = Enum.YLeaf(97, "dequeuefailed")

    shuttingdown = Enum.YLeaf(98, "shuttingdown")

    couldnotvalidatetrustchain = Enum.YLeaf(99, "couldnotvalidatetrustchain")

    reservationalreadyinstalled = Enum.YLeaf(100, "reservationalreadyinstalled")

    reservationinstallparsefail = Enum.YLeaf(101, "reservationinstallparsefail")

    base64encoding = Enum.YLeaf(102, "base64encoding")

    base64decoding = Enum.YLeaf(103, "base64decoding")

    invalidsoftwareidtag = Enum.YLeaf(104, "invalidsoftwareidtag")

    certificatemismatch = Enum.YLeaf(105, "certificatemismatch")

    noreservation = Enum.YLeaf(106, "noreservation")

    agentunreachable = Enum.YLeaf(107, "agentunreachable")

    ignoreevent = Enum.YLeaf(108, "ignoreevent")

    b58overflow = Enum.YLeaf(109, "b58overflow")

    b58decode = Enum.YLeaf(110, "b58decode")

    b58badlen = Enum.YLeaf(111, "b58badlen")

    b58invdigit = Enum.YLeaf(112, "b58invdigit")

    b58decodeoverflow = Enum.YLeaf(113, "b58decodeoverflow")

    reservationversionoutofbound = Enum.YLeaf(114, "reservationversionoutofbound")

    base58encode = Enum.YLeaf(115, "base58encode")

    duplicatedentry = Enum.YLeaf(116, "duplicatedentry")

    missingentry = Enum.YLeaf(117, "missingentry")

    badpeerinfoformat = Enum.YLeaf(118, "badpeerinfoformat")

    badapplicationhaattributedataset = Enum.YLeaf(119, "badapplicationhaattributedataset")

    reservationinprogress = Enum.YLeaf(120, "reservationinprogress")

    xdmcreatehandle = Enum.YLeaf(121, "xdmcreatehandle")

    versionmismatchinentitlementrsp = Enum.YLeaf(122, "versionmismatchinentitlementrsp")

    harolenotsupported = Enum.YLeaf(123, "harolenotsupported")

    apphainvalidcharacter = Enum.YLeaf(124, "apphainvalidcharacter")

    apphaaddpeerfromsamedevice = Enum.YLeaf(125, "apphaaddpeerfromsamedevice")

    apphaappduplicatedinstance = Enum.YLeaf(126, "apphaappduplicatedinstance")

    versionmismatchinregresponse = Enum.YLeaf(127, "versionmismatchinregresponse")

    conversionnocb = Enum.YLeaf(128, "conversionnocb")

    conversionnotallowed = Enum.YLeaf(129, "conversionnotallowed")

    conversioninprogress = Enum.YLeaf(130, "conversioninprogress")

    conversionalreadystarted = Enum.YLeaf(131, "conversionalreadystarted")

    conversionnotenabled = Enum.YLeaf(132, "conversionnotenabled")

    versionconversionnotsupported = Enum.YLeaf(133, "versionconversionnotsupported")

    noconversioninprogress = Enum.YLeaf(134, "noconversioninprogress")

    cryptoversionmismatch = Enum.YLeaf(135, "cryptoversionmismatch")

    conversionstoppedpartially = Enum.YLeaf(136, "conversionstoppedpartially")

    utilityenabled = Enum.YLeaf(137, "utilityenabled")

    utilitynotenabled = Enum.YLeaf(138, "utilitynotenabled")

    transportnotavailable = Enum.YLeaf(139, "transportnotavailable")

    fqdn = Enum.YLeaf(140, "fqdn")

    thirdparty = Enum.YLeaf(141, "thirdparty")

    transporttype = Enum.YLeaf(142, "transporttype")

    max = Enum.YLeaf(143, "max")


class NotifRegisterFailureEnum(Enum):
    """
    NotifRegisterFailureEnum (Enum Class)

    Registration failure reasons. In all cases

    notif\-failure\-data\-group.message will contain a more 

    detailed failure message.

    .. data:: general_failure = 0

    	General failure.

    .. data:: already_registered_failure = 1

    	This smart licensing instance is already registered.

    .. data:: de_register_failure = 2

    	The de-register failed because this instance is not registered.

    """

    general_failure = Enum.YLeaf(0, "general-failure")

    already_registered_failure = Enum.YLeaf(1, "already-registered-failure")

    de_register_failure = Enum.YLeaf(2, "de-register-failure")


class RegistrationStateEnum(Enum):
    """
    RegistrationStateEnum (Enum Class)

    The smart licensing registration state.

    .. data:: reg_state_not_registered = 0

    	This smart licensing instance is not registered.

    .. data:: reg_state_complete = 1

    	Registration was successful and this smart licensing 

    	instance is registered.

    .. data:: reg_state_in_progress = 2

    	Registration is in progress.

    .. data:: reg_state_retry = 3

    	The initial registration attempt failed but

    	a retry is in progress.

    .. data:: reg_state_failed = 4

    	Registration failed.

    """

    reg_state_not_registered = Enum.YLeaf(0, "reg-state-not-registered")

    reg_state_complete = Enum.YLeaf(1, "reg-state-complete")

    reg_state_in_progress = Enum.YLeaf(2, "reg-state-in-progress")

    reg_state_retry = Enum.YLeaf(3, "reg-state-retry")

    reg_state_failed = Enum.YLeaf(4, "reg-state-failed")


class TransportTypeEnum(Enum):
    """
    TransportTypeEnum (Enum Class)

    The type of transport in use by smart licensing.

    .. data:: transport_type_callhome = 0

    	Smart Licensing is using callhome for communications.

    .. data:: transport_type_smart = 1

    	Smart licensing is using the smart transport for 

    	communications.

    """

    transport_type_callhome = Enum.YLeaf(0, "transport-type-callhome")

    transport_type_smart = Enum.YLeaf(1, "transport-type-smart")


class UtilityReportingTypeEnum(Enum):
    """
    UtilityReportingTypeEnum (Enum Class)

    What has triggered the system to start reporting utility usage.

    .. data:: utility_reporting_type_none = 0

    	The system is not reporting utility usage data.

    .. data:: utility_reporting_type_subscription = 1

    	The system is reporting utility usage data because it has 

    	received subscription information from either the SSM or 

    	satellite.

    .. data:: utility_reporting_type_certificate = 2

    	The system is reporting utility usage data because it has 

    	received a utility certificate from a Third Party 

    	Billing Platform.

    """

    utility_reporting_type_none = Enum.YLeaf(0, "utility-reporting-type-none")

    utility_reporting_type_subscription = Enum.YLeaf(1, "utility-reporting-type-subscription")

    utility_reporting_type_certificate = Enum.YLeaf(2, "utility-reporting-type-certificate")



class RegisterIdToken(Entity):
    """
    Register with an ID token.
    This will begin the registration process. Since the registration 
    process will take somewhere between seconds and hours you must get the  
    registration\-success or registration\-fail notifications 
    or check the registration status in smart\-license\:state
    to know the status of the registration.
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xe.cisco_smart_license.RegisterIdToken.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xe.cisco_smart_license.RegisterIdToken.Output>`
    
    

    """

    _prefix = 'cisco-smart-license'
    _revision = '2017-10-11'

    def __init__(self):
        super(RegisterIdToken, self).__init__()
        self._top_entity = None

        self.yang_name = "register-id-token"
        self.yang_parent_name = "cisco-smart-license"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = RegisterIdToken.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")

        self.output = RegisterIdToken.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._children_yang_names.add("output")
        self._segment_path = lambda: "cisco-smart-license:register-id-token"


    class Input(Entity):
        """
        
        
        .. attribute:: id_token
        
        	The ID token used to register
        	**type**\: str
        
        	**length:** 1..255
        
        .. attribute:: force
        
        	Force the registration if set
        	**type**\: bool
        
        	**default value**\: false
        
        

        """

        _prefix = 'cisco-smart-license'
        _revision = '2017-10-11'

        def __init__(self):
            super(RegisterIdToken.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "register-id-token"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('id_token', YLeaf(YType.str, 'id-token')),
                ('force', YLeaf(YType.boolean, 'force')),
            ])
            self.id_token = None
            self.force = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "cisco-smart-license:register-id-token/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RegisterIdToken.Input, ['id_token', 'force'], name, value)


    class Output(Entity):
        """
        
        
        .. attribute:: return_code
        
        	The return code.  If smart licensing is not enabled (status\:enabled) then the error will be error\-enum\:notenabled. On success the return code will be  error\-enum\:registrationinprogress
        	**type**\:  :py:class:`ErrorEnum <ydk.models.cisco_ios_xe.cisco_smart_license.ErrorEnum>`
        
        

        """

        _prefix = 'cisco-smart-license'
        _revision = '2017-10-11'

        def __init__(self):
            super(RegisterIdToken.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "register-id-token"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('return_code', YLeaf(YType.enumeration, 'return-code')),
            ])
            self.return_code = None
            self._segment_path = lambda: "output"
            self._absolute_path = lambda: "cisco-smart-license:register-id-token/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RegisterIdToken.Output, ['return_code'], name, value)

    def clone_ptr(self):
        self._top_entity = RegisterIdToken()
        return self._top_entity

class DeRegister(Entity):
    """
    De\-register. This will immediately de\-register the device.
    
    .. attribute:: output
    
    	
    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xe.cisco_smart_license.DeRegister.Output>`
    
    

    """

    _prefix = 'cisco-smart-license'
    _revision = '2017-10-11'

    def __init__(self):
        super(DeRegister, self).__init__()
        self._top_entity = None

        self.yang_name = "de-register"
        self.yang_parent_name = "cisco-smart-license"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.output = DeRegister.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._children_yang_names.add("output")
        self._segment_path = lambda: "cisco-smart-license:de-register"


    class Output(Entity):
        """
        
        
        .. attribute:: return_code
        
        	The return code for the de\-register process
        	**type**\:  :py:class:`ErrorEnum <ydk.models.cisco_ios_xe.cisco_smart_license.ErrorEnum>`
        
        

        """

        _prefix = 'cisco-smart-license'
        _revision = '2017-10-11'

        def __init__(self):
            super(DeRegister.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "de-register"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('return_code', YLeaf(YType.enumeration, 'return-code')),
            ])
            self.return_code = None
            self._segment_path = lambda: "output"
            self._absolute_path = lambda: "cisco-smart-license:de-register/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(DeRegister.Output, ['return_code'], name, value)

    def clone_ptr(self):
        self._top_entity = DeRegister()
        return self._top_entity

class RenewId(Entity):
    """
    Under normal operations smart licensing will automatically renew 
    the ID certificates used for regsitration. This command can 
    be used if he customer wants to initiate a manual 
    registration renewal.
    
    .. attribute:: output
    
    	
    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xe.cisco_smart_license.RenewId.Output>`
    
    

    """

    _prefix = 'cisco-smart-license'
    _revision = '2017-10-11'

    def __init__(self):
        super(RenewId, self).__init__()
        self._top_entity = None

        self.yang_name = "renew-id"
        self.yang_parent_name = "cisco-smart-license"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.output = RenewId.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._children_yang_names.add("output")
        self._segment_path = lambda: "cisco-smart-license:renew-id"


    class Output(Entity):
        """
        
        
        .. attribute:: return_code
        
        	The return code
        	**type**\:  :py:class:`ErrorEnum <ydk.models.cisco_ios_xe.cisco_smart_license.ErrorEnum>`
        
        

        """

        _prefix = 'cisco-smart-license'
        _revision = '2017-10-11'

        def __init__(self):
            super(RenewId.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "renew-id"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('return_code', YLeaf(YType.enumeration, 'return-code')),
            ])
            self.return_code = None
            self._segment_path = lambda: "output"
            self._absolute_path = lambda: "cisco-smart-license:renew-id/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RenewId.Output, ['return_code'], name, value)

    def clone_ptr(self):
        self._top_entity = RenewId()
        return self._top_entity

class RenewAuth(Entity):
    """
    Under normal operations smart licensing will automatically renew 
    the license authorization every 30 days. This command can 
    be used if he customer wants to iinitiate a manual 
    renewal.
    
    .. attribute:: output
    
    	
    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xe.cisco_smart_license.RenewAuth.Output>`
    
    

    """

    _prefix = 'cisco-smart-license'
    _revision = '2017-10-11'

    def __init__(self):
        super(RenewAuth, self).__init__()
        self._top_entity = None

        self.yang_name = "renew-auth"
        self.yang_parent_name = "cisco-smart-license"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.output = RenewAuth.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._children_yang_names.add("output")
        self._segment_path = lambda: "cisco-smart-license:renew-auth"


    class Output(Entity):
        """
        
        
        .. attribute:: return_code
        
        	The return code
        	**type**\:  :py:class:`ErrorEnum <ydk.models.cisco_ios_xe.cisco_smart_license.ErrorEnum>`
        
        

        """

        _prefix = 'cisco-smart-license'
        _revision = '2017-10-11'

        def __init__(self):
            super(RenewAuth.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "renew-auth"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('return_code', YLeaf(YType.enumeration, 'return-code')),
            ])
            self.return_code = None
            self._segment_path = lambda: "output"
            self._absolute_path = lambda: "cisco-smart-license:renew-auth/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RenewAuth.Output, ['return_code'], name, value)

    def clone_ptr(self):
        self._top_entity = RenewAuth()
        return self._top_entity

class Licensing(Entity):
    """
    Container to hold config and state.
    
    .. attribute:: config
    
    	Smart licensing configuration
    	**type**\:  :py:class:`Config <ydk.models.cisco_ios_xe.cisco_smart_license.Licensing.Config>`
    
    .. attribute:: state
    
    	Smart licensing state
    	**type**\:  :py:class:`State <ydk.models.cisco_ios_xe.cisco_smart_license.Licensing.State>`
    
    

    """

    _prefix = 'cisco-smart-license'
    _revision = '2017-10-11'

    def __init__(self):
        super(Licensing, self).__init__()
        self._top_entity = None

        self.yang_name = "licensing"
        self.yang_parent_name = "cisco-smart-license"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("config", ("config", Licensing.Config)), ("state", ("state", Licensing.State))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.config = Licensing.Config()
        self.config.parent = self
        self._children_name_map["config"] = "config"
        self._children_yang_names.add("config")

        self.state = Licensing.State()
        self.state.parent = self
        self._children_name_map["state"] = "state"
        self._children_yang_names.add("state")
        self._segment_path = lambda: "cisco-smart-license:licensing"


    class Config(Entity):
        """
        Smart licensing configuration.
        
        .. attribute:: enable
        
        	Enable/disable smart licensing. If state\:always\-enabled is true then Smart Licensing is always enabled and config\:enable will be  silently ignored
        	**type**\: bool
        
        .. attribute:: custom_id
        
        	A free form ID set by the customer which will be included in the utility usage (RUM) report and inthe message header
        	**type**\: str
        
        .. attribute:: privacy
        
        	Controls whether or not some information is sent in messages to the   CSSM or satellite
        	**type**\:  :py:class:`Privacy <ydk.models.cisco_ios_xe.cisco_smart_license.Licensing.Config.Privacy>`
        
        .. attribute:: utility
        
        	Utility settings
        	**type**\:  :py:class:`Utility <ydk.models.cisco_ios_xe.cisco_smart_license.Licensing.Config.Utility>`
        
        .. attribute:: transport
        
        	Transport layer settings
        	**type**\:  :py:class:`Transport <ydk.models.cisco_ios_xe.cisco_smart_license.Licensing.Config.Transport>`
        
        

        """

        _prefix = 'cisco-smart-license'
        _revision = '2017-10-11'

        def __init__(self):
            super(Licensing.Config, self).__init__()

            self.yang_name = "config"
            self.yang_parent_name = "licensing"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([("privacy", ("privacy", Licensing.Config.Privacy)), ("utility", ("utility", Licensing.Config.Utility)), ("transport", ("transport", Licensing.Config.Transport))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('enable', YLeaf(YType.boolean, 'enable')),
                ('custom_id', YLeaf(YType.str, 'custom-id')),
            ])
            self.enable = None
            self.custom_id = None

            self.privacy = Licensing.Config.Privacy()
            self.privacy.parent = self
            self._children_name_map["privacy"] = "privacy"
            self._children_yang_names.add("privacy")

            self.utility = Licensing.Config.Utility()
            self.utility.parent = self
            self._children_name_map["utility"] = "utility"
            self._children_yang_names.add("utility")

            self.transport = Licensing.Config.Transport()
            self.transport.parent = self
            self._children_name_map["transport"] = "transport"
            self._children_yang_names.add("transport")
            self._segment_path = lambda: "config"
            self._absolute_path = lambda: "cisco-smart-license:licensing/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Licensing.Config, ['enable', 'custom_id'], name, value)


        class Privacy(Entity):
            """
            Controls whether or not some information is sent in messages to the 
             CSSM or satellite.
            
            .. attribute:: hostname
            
            	If true then the hostname will not be sent in  any messages
            	**type**\: bool
            
            .. attribute:: version
            
            	If true then the smart licensing version will not be sent in  any messages
            	**type**\: bool
            
            

            """

            _prefix = 'cisco-smart-license'
            _revision = '2017-10-11'

            def __init__(self):
                super(Licensing.Config.Privacy, self).__init__()

                self.yang_name = "privacy"
                self.yang_parent_name = "config"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('hostname', YLeaf(YType.boolean, 'hostname')),
                    ('version', YLeaf(YType.boolean, 'version')),
                ])
                self.hostname = None
                self.version = None
                self._segment_path = lambda: "privacy"
                self._absolute_path = lambda: "cisco-smart-license:licensing/config/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Licensing.Config.Privacy, ['hostname', 'version'], name, value)


        class Utility(Entity):
            """
            Utility settings.
            
            .. attribute:: utility_enable
            
            	Indicates the customer's intent to start reporting  utility usage information. This alone does not enable  utility reporting. Either subscription information will be  automatically downloaded from the SSM or a utility certificate we be loaded if the system registers with a  Third Party Billing Platform
            	**type**\: bool
            
            .. attribute:: customer_info
            
            	Customer address information that will be included in  the utility usage reports
            	**type**\:  :py:class:`CustomerInfo <ydk.models.cisco_ios_xe.cisco_smart_license.Licensing.Config.Utility.CustomerInfo>`
            
            

            """

            _prefix = 'cisco-smart-license'
            _revision = '2017-10-11'

            def __init__(self):
                super(Licensing.Config.Utility, self).__init__()

                self.yang_name = "utility"
                self.yang_parent_name = "config"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([("customer-info", ("customer_info", Licensing.Config.Utility.CustomerInfo))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('utility_enable', YLeaf(YType.boolean, 'utility-enable')),
                ])
                self.utility_enable = None

                self.customer_info = Licensing.Config.Utility.CustomerInfo()
                self.customer_info.parent = self
                self._children_name_map["customer_info"] = "customer-info"
                self._children_yang_names.add("customer-info")
                self._segment_path = lambda: "utility"
                self._absolute_path = lambda: "cisco-smart-license:licensing/config/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Licensing.Config.Utility, ['utility_enable'], name, value)


            class CustomerInfo(Entity):
                """
                Customer address information that will be included in 
                the utility usage reports.
                
                .. attribute:: id
                
                	The cisco issued customer id which will be included in the utility usage (RUM) report
                	**type**\: str
                
                	**length:** 1..250
                
                .. attribute:: name
                
                	The customer company name which will be included in the utility usage (RUM) report
                	**type**\: str
                
                	**length:** 1..250
                
                .. attribute:: street
                
                	The customer company street address which will be included in the utility usage (RUM) report
                	**type**\: str
                
                	**length:** 1..250
                
                .. attribute:: city
                
                	The customer company city which will be included in the utility usage (RUM) report
                	**type**\: str
                
                	**length:** 1..250
                
                .. attribute:: state
                
                	The customer company state which will be included in the utility usage (RUM) report
                	**type**\: str
                
                	**length:** 1..250
                
                .. attribute:: country
                
                	The customer company country which will be included in the utility usage (RUM) report
                	**type**\: str
                
                	**length:** 1..250
                
                .. attribute:: postal_code
                
                	The customer location specific postal code which will be included in the utility usage (RUM) report
                	**type**\: str
                
                	**length:** 1..250
                
                

                """

                _prefix = 'cisco-smart-license'
                _revision = '2017-10-11'

                def __init__(self):
                    super(Licensing.Config.Utility.CustomerInfo, self).__init__()

                    self.yang_name = "customer-info"
                    self.yang_parent_name = "utility"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('id', YLeaf(YType.str, 'id')),
                        ('name', YLeaf(YType.str, 'name')),
                        ('street', YLeaf(YType.str, 'street')),
                        ('city', YLeaf(YType.str, 'city')),
                        ('state', YLeaf(YType.str, 'state')),
                        ('country', YLeaf(YType.str, 'country')),
                        ('postal_code', YLeaf(YType.str, 'postal-code')),
                    ])
                    self.id = None
                    self.name = None
                    self.street = None
                    self.city = None
                    self.state = None
                    self.country = None
                    self.postal_code = None
                    self._segment_path = lambda: "customer-info"
                    self._absolute_path = lambda: "cisco-smart-license:licensing/config/utility/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Licensing.Config.Utility.CustomerInfo, ['id', 'name', 'street', 'city', 'state', 'country', 'postal_code'], name, value)


        class Transport(Entity):
            """
            Transport layer settings.
            
            .. attribute:: transport_type
            
            	The transport type. If transport\-type is set to transport\-type\-callhome then any additional transport settings must be done from the callhome CLI. If the transport\-type is set to transport\-type\-smart additional settings are available below
            	**type**\:  :py:class:`TransportTypeEnum <ydk.models.cisco_ios_xe.cisco_smart_license.TransportTypeEnum>`
            
            .. attribute:: transport_smart
            
            	Settings for the smart transport
            	**type**\:  :py:class:`TransportSmart <ydk.models.cisco_ios_xe.cisco_smart_license.Licensing.Config.Transport.TransportSmart>`
            
            

            """

            _prefix = 'cisco-smart-license'
            _revision = '2017-10-11'

            def __init__(self):
                super(Licensing.Config.Transport, self).__init__()

                self.yang_name = "transport"
                self.yang_parent_name = "config"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([("transport-smart", ("transport_smart", Licensing.Config.Transport.TransportSmart))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('transport_type', YLeaf(YType.enumeration, 'transport-type')),
                ])
                self.transport_type = None

                self.transport_smart = Licensing.Config.Transport.TransportSmart()
                self.transport_smart.parent = self
                self._children_name_map["transport_smart"] = "transport-smart"
                self._children_yang_names.add("transport-smart")
                self._segment_path = lambda: "transport"
                self._absolute_path = lambda: "cisco-smart-license:licensing/config/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Licensing.Config.Transport, ['transport_type'], name, value)


            class TransportSmart(Entity):
                """
                Settings for the smart transport.
                
                .. attribute:: url_default
                
                	Tell smart licensing to set the default URLs for both url\-registration and url\-utility that point to  the Cisco SSM
                	**type**\: bool
                
                .. attribute:: urls
                
                	The URLS used for registration and utility reporting. These should be set if the product instance will communicate with a satellite or Third Party  Billing Platform
                	**type**\:  :py:class:`Urls <ydk.models.cisco_ios_xe.cisco_smart_license.Licensing.Config.Transport.TransportSmart.Urls>`
                
                

                """

                _prefix = 'cisco-smart-license'
                _revision = '2017-10-11'

                def __init__(self):
                    super(Licensing.Config.Transport.TransportSmart, self).__init__()

                    self.yang_name = "transport-smart"
                    self.yang_parent_name = "transport"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("urls", ("urls", Licensing.Config.Transport.TransportSmart.Urls))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('url_default', YLeaf(YType.boolean, 'url-default')),
                    ])
                    self.url_default = None

                    self.urls = Licensing.Config.Transport.TransportSmart.Urls()
                    self.urls.parent = self
                    self._children_name_map["urls"] = "urls"
                    self._children_yang_names.add("urls")
                    self._segment_path = lambda: "transport-smart"
                    self._absolute_path = lambda: "cisco-smart-license:licensing/config/transport/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Licensing.Config.Transport.TransportSmart, ['url_default'], name, value)


                class Urls(Entity):
                    """
                    The URLS used for registration and utility reporting.
                    These should be set if the product instance will
                    communicate with a satellite or Third Party 
                    Billing Platform.
                    
                    .. attribute:: url_registration
                    
                    	Set the URL used for registration, authorization and anything else not related to utility usage reporting
                    	**type**\: str
                    
                    .. attribute:: url_utility
                    
                    	Set the URL to be used for sending utility usage  reports. This should be the same as url\-registration  if you are using a satellite
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'cisco-smart-license'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Licensing.Config.Transport.TransportSmart.Urls, self).__init__()

                        self.yang_name = "urls"
                        self.yang_parent_name = "transport-smart"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('url_registration', YLeaf(YType.str, 'url-registration')),
                            ('url_utility', YLeaf(YType.str, 'url-utility')),
                        ])
                        self.url_registration = None
                        self.url_utility = None
                        self._segment_path = lambda: "urls"
                        self._absolute_path = lambda: "cisco-smart-license:licensing/config/transport/transport-smart/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Licensing.Config.Transport.TransportSmart.Urls, ['url_registration', 'url_utility'], name, value)


    class State(Entity):
        """
        Smart licensing state.
        
        .. attribute:: always_enabled
        
        	Smart Licensing is always enabled. the smart\-enabled leaf below  will always be true. The config\:enable setting above will be silently  ignored by Smart licensing
        	**type**\: bool
        
        .. attribute:: smart_enabled
        
        	Is smart licensing enabled. If always\-enabled above is true then  smart licensing is always enabled and can not be disabled
        	**type**\: bool
        
        .. attribute:: version
        
        	The smart licensing version in use
        	**type**\: str
        
        	**length:** 1..255
        
        .. attribute:: state_info
        
        	Smart licensing state information.     This is only valid if smart\-enabled = true
        	**type**\:  :py:class:`StateInfo <ydk.models.cisco_ios_xe.cisco_smart_license.Licensing.State.StateInfo>`
        
        

        """

        _prefix = 'cisco-smart-license'
        _revision = '2017-10-11'

        def __init__(self):
            super(Licensing.State, self).__init__()

            self.yang_name = "state"
            self.yang_parent_name = "licensing"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([("state-info", ("state_info", Licensing.State.StateInfo))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('always_enabled', YLeaf(YType.boolean, 'always-enabled')),
                ('smart_enabled', YLeaf(YType.boolean, 'smart-enabled')),
                ('version', YLeaf(YType.str, 'version')),
            ])
            self.always_enabled = None
            self.smart_enabled = None
            self.version = None

            self.state_info = Licensing.State.StateInfo()
            self.state_info.parent = self
            self._children_name_map["state_info"] = "state-info"
            self._children_yang_names.add("state-info")
            self._segment_path = lambda: "state"
            self._absolute_path = lambda: "cisco-smart-license:licensing/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Licensing.State, ['always_enabled', 'smart_enabled', 'version'], name, value)


        class StateInfo(Entity):
            """
            Smart licensing state information. 
               This is only valid if smart\-enabled = true.
            
            .. attribute:: registration
            
            	State of license registration
            	**type**\:  :py:class:`Registration <ydk.models.cisco_ios_xe.cisco_smart_license.Licensing.State.StateInfo.Registration>`
            
            .. attribute:: authorization
            
            	State of license authorization
            	**type**\:  :py:class:`Authorization <ydk.models.cisco_ios_xe.cisco_smart_license.Licensing.State.StateInfo.Authorization>`
            
            .. attribute:: utility
            
            	State of utility reporting
            	**type**\:  :py:class:`Utility <ydk.models.cisco_ios_xe.cisco_smart_license.Licensing.State.StateInfo.Utility>`
            
            .. attribute:: custom_id
            
            	The custom ID set by the customer that will be included in the utility usage (RUM) report and in th emessage header
            	**type**\: str
            
            .. attribute:: transport
            
            	State of the transport
            	**type**\:  :py:class:`Transport <ydk.models.cisco_ios_xe.cisco_smart_license.Licensing.State.StateInfo.Transport>`
            
            .. attribute:: privacy
            
            	State of the privacy settings
            	**type**\:  :py:class:`Privacy <ydk.models.cisco_ios_xe.cisco_smart_license.Licensing.State.StateInfo.Privacy>`
            
            .. attribute:: evaluation
            
            	State of the evaluation period
            	**type**\:  :py:class:`Evaluation <ydk.models.cisco_ios_xe.cisco_smart_license.Licensing.State.StateInfo.Evaluation>`
            
            .. attribute:: udi
            
            	UDI of the system
            	**type**\:  :py:class:`Udi <ydk.models.cisco_ios_xe.cisco_smart_license.Licensing.State.StateInfo.Udi>`
            
            .. attribute:: usage
            
            	List of license (entitlement tag) usage information.  This only contains the information for licenses that are in use
            	**type**\: list of  		 :py:class:`Usage <ydk.models.cisco_ios_xe.cisco_smart_license.Licensing.State.StateInfo.Usage>`
            
            

            """

            _prefix = 'cisco-smart-license'
            _revision = '2017-10-11'

            def __init__(self):
                super(Licensing.State.StateInfo, self).__init__()

                self.yang_name = "state-info"
                self.yang_parent_name = "state"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([("registration", ("registration", Licensing.State.StateInfo.Registration)), ("authorization", ("authorization", Licensing.State.StateInfo.Authorization)), ("utility", ("utility", Licensing.State.StateInfo.Utility)), ("transport", ("transport", Licensing.State.StateInfo.Transport)), ("privacy", ("privacy", Licensing.State.StateInfo.Privacy)), ("evaluation", ("evaluation", Licensing.State.StateInfo.Evaluation)), ("udi", ("udi", Licensing.State.StateInfo.Udi))])
                self._child_list_classes = OrderedDict([("usage", ("usage", Licensing.State.StateInfo.Usage))])
                self._leafs = OrderedDict([
                    ('custom_id', YLeaf(YType.str, 'custom-id')),
                ])
                self.custom_id = None

                self.registration = Licensing.State.StateInfo.Registration()
                self.registration.parent = self
                self._children_name_map["registration"] = "registration"
                self._children_yang_names.add("registration")

                self.authorization = Licensing.State.StateInfo.Authorization()
                self.authorization.parent = self
                self._children_name_map["authorization"] = "authorization"
                self._children_yang_names.add("authorization")

                self.utility = Licensing.State.StateInfo.Utility()
                self.utility.parent = self
                self._children_name_map["utility"] = "utility"
                self._children_yang_names.add("utility")

                self.transport = Licensing.State.StateInfo.Transport()
                self.transport.parent = self
                self._children_name_map["transport"] = "transport"
                self._children_yang_names.add("transport")

                self.privacy = Licensing.State.StateInfo.Privacy()
                self.privacy.parent = self
                self._children_name_map["privacy"] = "privacy"
                self._children_yang_names.add("privacy")

                self.evaluation = Licensing.State.StateInfo.Evaluation()
                self.evaluation.parent = self
                self._children_name_map["evaluation"] = "evaluation"
                self._children_yang_names.add("evaluation")

                self.udi = Licensing.State.StateInfo.Udi()
                self.udi.parent = self
                self._children_name_map["udi"] = "udi"
                self._children_yang_names.add("udi")

                self.usage = YList(self)
                self._segment_path = lambda: "state-info"
                self._absolute_path = lambda: "cisco-smart-license:licensing/state/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Licensing.State.StateInfo, ['custom_id'], name, value)


            class Registration(Entity):
                """
                State of license registration.
                
                .. attribute:: registration_state
                
                	The current registration state
                	**type**\:  :py:class:`RegistrationStateEnum <ydk.models.cisco_ios_xe.cisco_smart_license.RegistrationStateEnum>`
                
                .. attribute:: registration_in_progress
                
                	Registration is in progress
                	**type**\:  :py:class:`RegistrationInProgress <ydk.models.cisco_ios_xe.cisco_smart_license.Licensing.State.StateInfo.Registration.RegistrationInProgress>`
                
                .. attribute:: registration_failed
                
                	Registration failed
                	**type**\:  :py:class:`RegistrationFailed <ydk.models.cisco_ios_xe.cisco_smart_license.Licensing.State.StateInfo.Registration.RegistrationFailed>`
                
                .. attribute:: registration_retry
                
                	Registration failed and doing a retry
                	**type**\:  :py:class:`RegistrationRetry <ydk.models.cisco_ios_xe.cisco_smart_license.Licensing.State.StateInfo.Registration.RegistrationRetry>`
                
                .. attribute:: registration_complete
                
                	Registration success
                	**type**\:  :py:class:`RegistrationComplete <ydk.models.cisco_ios_xe.cisco_smart_license.Licensing.State.StateInfo.Registration.RegistrationComplete>`
                
                .. attribute:: export_control_allowed
                
                	Is the device allowed to enable export controlled features
                	**type**\: bool
                
                

                """

                _prefix = 'cisco-smart-license'
                _revision = '2017-10-11'

                def __init__(self):
                    super(Licensing.State.StateInfo.Registration, self).__init__()

                    self.yang_name = "registration"
                    self.yang_parent_name = "state-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("registration-in-progress", ("registration_in_progress", Licensing.State.StateInfo.Registration.RegistrationInProgress)), ("registration-failed", ("registration_failed", Licensing.State.StateInfo.Registration.RegistrationFailed)), ("registration-retry", ("registration_retry", Licensing.State.StateInfo.Registration.RegistrationRetry)), ("registration-complete", ("registration_complete", Licensing.State.StateInfo.Registration.RegistrationComplete))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('registration_state', YLeaf(YType.enumeration, 'registration-state')),
                        ('export_control_allowed', YLeaf(YType.boolean, 'export-control-allowed')),
                    ])
                    self.registration_state = None
                    self.export_control_allowed = None

                    self.registration_in_progress = Licensing.State.StateInfo.Registration.RegistrationInProgress()
                    self.registration_in_progress.parent = self
                    self._children_name_map["registration_in_progress"] = "registration-in-progress"
                    self._children_yang_names.add("registration-in-progress")

                    self.registration_failed = Licensing.State.StateInfo.Registration.RegistrationFailed()
                    self.registration_failed.parent = self
                    self._children_name_map["registration_failed"] = "registration-failed"
                    self._children_yang_names.add("registration-failed")

                    self.registration_retry = Licensing.State.StateInfo.Registration.RegistrationRetry()
                    self.registration_retry.parent = self
                    self._children_name_map["registration_retry"] = "registration-retry"
                    self._children_yang_names.add("registration-retry")

                    self.registration_complete = Licensing.State.StateInfo.Registration.RegistrationComplete()
                    self.registration_complete.parent = self
                    self._children_name_map["registration_complete"] = "registration-complete"
                    self._children_yang_names.add("registration-complete")
                    self._segment_path = lambda: "registration"
                    self._absolute_path = lambda: "cisco-smart-license:licensing/state/state-info/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Licensing.State.StateInfo.Registration, ['registration_state', 'export_control_allowed'], name, value)


                class RegistrationInProgress(Entity):
                    """
                    Registration is in progress.
                    
                    .. attribute:: start_time
                    
                    	Time the registration started
                    	**type**\: str
                    
                    	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                    
                    

                    """

                    _prefix = 'cisco-smart-license'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Licensing.State.StateInfo.Registration.RegistrationInProgress, self).__init__()

                        self.yang_name = "registration-in-progress"
                        self.yang_parent_name = "registration"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('start_time', YLeaf(YType.str, 'start-time')),
                        ])
                        self.start_time = None
                        self._segment_path = lambda: "registration-in-progress"
                        self._absolute_path = lambda: "cisco-smart-license:licensing/state/state-info/registration/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Licensing.State.StateInfo.Registration.RegistrationInProgress, ['start_time'], name, value)


                class RegistrationFailed(Entity):
                    """
                    Registration failed.
                    
                    .. attribute:: fail_time
                    
                    	Time the registration failed
                    	**type**\: str
                    
                    	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                    
                    .. attribute:: fail_message
                    
                    	Failure message that can be displayed for the user.  This is not a parsable message
                    	**type**\: str
                    
                    	**length:** 0..255
                    
                    

                    """

                    _prefix = 'cisco-smart-license'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Licensing.State.StateInfo.Registration.RegistrationFailed, self).__init__()

                        self.yang_name = "registration-failed"
                        self.yang_parent_name = "registration"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('fail_time', YLeaf(YType.str, 'fail-time')),
                            ('fail_message', YLeaf(YType.str, 'fail-message')),
                        ])
                        self.fail_time = None
                        self.fail_message = None
                        self._segment_path = lambda: "registration-failed"
                        self._absolute_path = lambda: "cisco-smart-license:licensing/state/state-info/registration/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Licensing.State.StateInfo.Registration.RegistrationFailed, ['fail_time', 'fail_message'], name, value)


                class RegistrationRetry(Entity):
                    """
                    Registration failed and doing a retry.
                    
                    .. attribute:: retry_next_time
                    
                    	Time the registration will be retried
                    	**type**\: str
                    
                    	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                    
                    .. attribute:: fail_time
                    
                    	Time the registration failed
                    	**type**\: str
                    
                    	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                    
                    .. attribute:: fail_message
                    
                    	Failure message that can be displayed for the user.  This is not a parsable message
                    	**type**\: str
                    
                    	**length:** 0..255
                    
                    

                    """

                    _prefix = 'cisco-smart-license'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Licensing.State.StateInfo.Registration.RegistrationRetry, self).__init__()

                        self.yang_name = "registration-retry"
                        self.yang_parent_name = "registration"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('retry_next_time', YLeaf(YType.str, 'retry-next-time')),
                            ('fail_time', YLeaf(YType.str, 'fail-time')),
                            ('fail_message', YLeaf(YType.str, 'fail-message')),
                        ])
                        self.retry_next_time = None
                        self.fail_time = None
                        self.fail_message = None
                        self._segment_path = lambda: "registration-retry"
                        self._absolute_path = lambda: "cisco-smart-license:licensing/state/state-info/registration/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Licensing.State.StateInfo.Registration.RegistrationRetry, ['retry_next_time', 'fail_time', 'fail_message'], name, value)


                class RegistrationComplete(Entity):
                    """
                    Registration success.
                    
                    .. attribute:: complete_time
                    
                    	Time the registration was successful
                    	**type**\: str
                    
                    	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                    
                    .. attribute:: last_renew_time
                    
                    	Time the last registration renewal occurred.  If empty then no renewal has occurred
                    	**type**\: str
                    
                    	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                    
                    .. attribute:: next_renew_time
                    
                    	Time the registration will be automatically renewed
                    	**type**\: str
                    
                    	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                    
                    .. attribute:: expire_time
                    
                    	Time the registration will expire if it is not renewed
                    	**type**\: str
                    
                    	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                    
                    .. attribute:: last_renew_success
                    
                    	Was the last renewal attempt successful
                    	**type**\: bool
                    
                    .. attribute:: fail_message
                    
                    	If the last renewal failed then this is a failure message that can be displayed for the user.  This is not a parsable string. Only present if the last renewal failed
                    	**type**\: str
                    
                    	**length:** 0..255
                    
                    .. attribute:: smart_account
                    
                    	The smart account name for this registration
                    	**type**\: str
                    
                    	**length:** 1..255
                    
                    .. attribute:: virtual_account
                    
                    	The virtual account name for this registration
                    	**type**\: str
                    
                    	**length:** 1..255
                    
                    

                    """

                    _prefix = 'cisco-smart-license'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Licensing.State.StateInfo.Registration.RegistrationComplete, self).__init__()

                        self.yang_name = "registration-complete"
                        self.yang_parent_name = "registration"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('complete_time', YLeaf(YType.str, 'complete-time')),
                            ('last_renew_time', YLeaf(YType.str, 'last-renew-time')),
                            ('next_renew_time', YLeaf(YType.str, 'next-renew-time')),
                            ('expire_time', YLeaf(YType.str, 'expire-time')),
                            ('last_renew_success', YLeaf(YType.boolean, 'last-renew-success')),
                            ('fail_message', YLeaf(YType.str, 'fail-message')),
                            ('smart_account', YLeaf(YType.str, 'smart-account')),
                            ('virtual_account', YLeaf(YType.str, 'virtual-account')),
                        ])
                        self.complete_time = None
                        self.last_renew_time = None
                        self.next_renew_time = None
                        self.expire_time = None
                        self.last_renew_success = None
                        self.fail_message = None
                        self.smart_account = None
                        self.virtual_account = None
                        self._segment_path = lambda: "registration-complete"
                        self._absolute_path = lambda: "cisco-smart-license:licensing/state/state-info/registration/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Licensing.State.StateInfo.Registration.RegistrationComplete, ['complete_time', 'last_renew_time', 'next_renew_time', 'expire_time', 'last_renew_success', 'fail_message', 'smart_account', 'virtual_account'], name, value)


            class Authorization(Entity):
                """
                State of license authorization.
                
                .. attribute:: authorization_state
                
                	The current authorization state
                	**type**\:  :py:class:`AuthorizationStateEnum <ydk.models.cisco_ios_xe.cisco_smart_license.AuthorizationStateEnum>`
                
                .. attribute:: authorization_none
                
                	No licenses in use. This empty container is not needed but is  a place holder to show there is no data for this state
                	**type**\:  :py:class:`AuthorizationNone <ydk.models.cisco_ios_xe.cisco_smart_license.Licensing.State.StateInfo.Authorization.AuthorizationNone>`
                
                .. attribute:: authorization_eval
                
                	Evaluation period is in use and counting down. The evaluation period only counts down when licenses are in use
                	**type**\:  :py:class:`AuthorizationEval <ydk.models.cisco_ios_xe.cisco_smart_license.Licensing.State.StateInfo.Authorization.AuthorizationEval>`
                
                .. attribute:: authorization_eval_expired
                
                	Evaluation period is in use but has expired
                	**type**\:  :py:class:`AuthorizationEvalExpired <ydk.models.cisco_ios_xe.cisco_smart_license.Licensing.State.StateInfo.Authorization.AuthorizationEvalExpired>`
                
                .. attribute:: authorization_authorized
                
                	All license usage is authorized and within terms of the contract
                	**type**\:  :py:class:`AuthorizationAuthorized <ydk.models.cisco_ios_xe.cisco_smart_license.Licensing.State.StateInfo.Authorization.AuthorizationAuthorized>`
                
                .. attribute:: authorization_authorized_reservation
                
                	All license usage is authorized because a   reservation authorization code is installed
                	**type**\:  :py:class:`AuthorizationAuthorizedReservation <ydk.models.cisco_ios_xe.cisco_smart_license.Licensing.State.StateInfo.Authorization.AuthorizationAuthorizedReservation>`
                
                .. attribute:: authorization_out_of_compliance
                
                	License usage is out of compliance with the terms of the  contract because more licenses are in use than were purchased
                	**type**\:  :py:class:`AuthorizationOutOfCompliance <ydk.models.cisco_ios_xe.cisco_smart_license.Licensing.State.StateInfo.Authorization.AuthorizationOutOfCompliance>`
                
                .. attribute:: authorization_authorization_expired
                
                	The authorization period has expired because the product  instance ahs not communicated with the SSM or satellite in  over 90 days
                	**type**\:  :py:class:`AuthorizationAuthorizationExpired <ydk.models.cisco_ios_xe.cisco_smart_license.Licensing.State.StateInfo.Authorization.AuthorizationAuthorizationExpired>`
                
                

                """

                _prefix = 'cisco-smart-license'
                _revision = '2017-10-11'

                def __init__(self):
                    super(Licensing.State.StateInfo.Authorization, self).__init__()

                    self.yang_name = "authorization"
                    self.yang_parent_name = "state-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("authorization-none", ("authorization_none", Licensing.State.StateInfo.Authorization.AuthorizationNone)), ("authorization-eval", ("authorization_eval", Licensing.State.StateInfo.Authorization.AuthorizationEval)), ("authorization-eval-expired", ("authorization_eval_expired", Licensing.State.StateInfo.Authorization.AuthorizationEvalExpired)), ("authorization-authorized", ("authorization_authorized", Licensing.State.StateInfo.Authorization.AuthorizationAuthorized)), ("authorization-authorized-reservation", ("authorization_authorized_reservation", Licensing.State.StateInfo.Authorization.AuthorizationAuthorizedReservation)), ("authorization-out-of-compliance", ("authorization_out_of_compliance", Licensing.State.StateInfo.Authorization.AuthorizationOutOfCompliance)), ("authorization-authorization-expired", ("authorization_authorization_expired", Licensing.State.StateInfo.Authorization.AuthorizationAuthorizationExpired))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('authorization_state', YLeaf(YType.enumeration, 'authorization-state')),
                    ])
                    self.authorization_state = None

                    self.authorization_none = Licensing.State.StateInfo.Authorization.AuthorizationNone()
                    self.authorization_none.parent = self
                    self._children_name_map["authorization_none"] = "authorization-none"
                    self._children_yang_names.add("authorization-none")

                    self.authorization_eval = Licensing.State.StateInfo.Authorization.AuthorizationEval()
                    self.authorization_eval.parent = self
                    self._children_name_map["authorization_eval"] = "authorization-eval"
                    self._children_yang_names.add("authorization-eval")

                    self.authorization_eval_expired = Licensing.State.StateInfo.Authorization.AuthorizationEvalExpired()
                    self.authorization_eval_expired.parent = self
                    self._children_name_map["authorization_eval_expired"] = "authorization-eval-expired"
                    self._children_yang_names.add("authorization-eval-expired")

                    self.authorization_authorized = Licensing.State.StateInfo.Authorization.AuthorizationAuthorized()
                    self.authorization_authorized.parent = self
                    self._children_name_map["authorization_authorized"] = "authorization-authorized"
                    self._children_yang_names.add("authorization-authorized")

                    self.authorization_authorized_reservation = Licensing.State.StateInfo.Authorization.AuthorizationAuthorizedReservation()
                    self.authorization_authorized_reservation.parent = self
                    self._children_name_map["authorization_authorized_reservation"] = "authorization-authorized-reservation"
                    self._children_yang_names.add("authorization-authorized-reservation")

                    self.authorization_out_of_compliance = Licensing.State.StateInfo.Authorization.AuthorizationOutOfCompliance()
                    self.authorization_out_of_compliance.parent = self
                    self._children_name_map["authorization_out_of_compliance"] = "authorization-out-of-compliance"
                    self._children_yang_names.add("authorization-out-of-compliance")

                    self.authorization_authorization_expired = Licensing.State.StateInfo.Authorization.AuthorizationAuthorizationExpired()
                    self.authorization_authorization_expired.parent = self
                    self._children_name_map["authorization_authorization_expired"] = "authorization-authorization-expired"
                    self._children_yang_names.add("authorization-authorization-expired")
                    self._segment_path = lambda: "authorization"
                    self._absolute_path = lambda: "cisco-smart-license:licensing/state/state-info/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Licensing.State.StateInfo.Authorization, ['authorization_state'], name, value)


                class AuthorizationNone(Entity):
                    """
                    No licenses in use. This empty container is not needed but is 
                    a place holder to show there is no data for this state.
                    
                    

                    """

                    _prefix = 'cisco-smart-license'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Licensing.State.StateInfo.Authorization.AuthorizationNone, self).__init__()

                        self.yang_name = "authorization-none"
                        self.yang_parent_name = "authorization"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict()
                        self._segment_path = lambda: "authorization-none"
                        self._absolute_path = lambda: "cisco-smart-license:licensing/state/state-info/authorization/%s" % self._segment_path()


                class AuthorizationEval(Entity):
                    """
                    Evaluation period is in use and counting down.
                    The evaluation period only counts down when licenses are
                    in use.
                    
                    .. attribute:: seconds_left
                    
                    	Number of seconds of license usage until the evaluation  period expires. Note that this not a hard date and time because if no licenses are in use the evaluation period stops  counting down
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'cisco-smart-license'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Licensing.State.StateInfo.Authorization.AuthorizationEval, self).__init__()

                        self.yang_name = "authorization-eval"
                        self.yang_parent_name = "authorization"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('seconds_left', YLeaf(YType.uint64, 'seconds-left')),
                        ])
                        self.seconds_left = None
                        self._segment_path = lambda: "authorization-eval"
                        self._absolute_path = lambda: "cisco-smart-license:licensing/state/state-info/authorization/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Licensing.State.StateInfo.Authorization.AuthorizationEval, ['seconds_left'], name, value)


                class AuthorizationEvalExpired(Entity):
                    """
                    Evaluation period is in use but has expired.
                    
                    .. attribute:: expire_time
                    
                    	Time the evaluation period expired
                    	**type**\: str
                    
                    	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                    
                    

                    """

                    _prefix = 'cisco-smart-license'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Licensing.State.StateInfo.Authorization.AuthorizationEvalExpired, self).__init__()

                        self.yang_name = "authorization-eval-expired"
                        self.yang_parent_name = "authorization"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('expire_time', YLeaf(YType.str, 'expire-time')),
                        ])
                        self.expire_time = None
                        self._segment_path = lambda: "authorization-eval-expired"
                        self._absolute_path = lambda: "cisco-smart-license:licensing/state/state-info/authorization/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Licensing.State.StateInfo.Authorization.AuthorizationEvalExpired, ['expire_time'], name, value)


                class AuthorizationAuthorized(Entity):
                    """
                    All license usage is authorized and within terms of the contract.
                    
                    .. attribute:: last_comm_status_success
                    
                    	Last communication was successful or failed
                    	**type**\: bool
                    
                    .. attribute:: fail_message
                    
                    	Failure message if the last communications attempt failed. This can be displayed for the user. It is not a parsable string
                    	**type**\: str
                    
                    	**length:** 0..255
                    
                    .. attribute:: last_comm_time
                    
                    	Time the last communication attempt happened
                    	**type**\: str
                    
                    	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                    
                    .. attribute:: next_comm_time
                    
                    	The next time communications will be attempted to the back end. This will be zero if the initial communication has not completed
                    	**type**\: str
                    
                    	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                    
                    .. attribute:: comm_deadline_time
                    
                    	If there are no communications between now and this time smart licensing will enter the authorization expired state.  This may be zero indicating there is no deadline
                    	**type**\: str
                    
                    	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                    
                    

                    """

                    _prefix = 'cisco-smart-license'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Licensing.State.StateInfo.Authorization.AuthorizationAuthorized, self).__init__()

                        self.yang_name = "authorization-authorized"
                        self.yang_parent_name = "authorization"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('last_comm_status_success', YLeaf(YType.boolean, 'last-comm-status-success')),
                            ('fail_message', YLeaf(YType.str, 'fail-message')),
                            ('last_comm_time', YLeaf(YType.str, 'last-comm-time')),
                            ('next_comm_time', YLeaf(YType.str, 'next-comm-time')),
                            ('comm_deadline_time', YLeaf(YType.str, 'comm-deadline-time')),
                        ])
                        self.last_comm_status_success = None
                        self.fail_message = None
                        self.last_comm_time = None
                        self.next_comm_time = None
                        self.comm_deadline_time = None
                        self._segment_path = lambda: "authorization-authorized"
                        self._absolute_path = lambda: "cisco-smart-license:licensing/state/state-info/authorization/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Licensing.State.StateInfo.Authorization.AuthorizationAuthorized, ['last_comm_status_success', 'fail_message', 'last_comm_time', 'next_comm_time', 'comm_deadline_time'], name, value)


                class AuthorizationAuthorizedReservation(Entity):
                    """
                    All license usage is authorized because a  
                    reservation authorization code is installed.
                    
                    .. attribute:: reservation_time
                    
                    	Time the reservation occurred
                    	**type**\: str
                    
                    	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                    
                    

                    """

                    _prefix = 'cisco-smart-license'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Licensing.State.StateInfo.Authorization.AuthorizationAuthorizedReservation, self).__init__()

                        self.yang_name = "authorization-authorized-reservation"
                        self.yang_parent_name = "authorization"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('reservation_time', YLeaf(YType.str, 'reservation-time')),
                        ])
                        self.reservation_time = None
                        self._segment_path = lambda: "authorization-authorized-reservation"
                        self._absolute_path = lambda: "cisco-smart-license:licensing/state/state-info/authorization/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Licensing.State.StateInfo.Authorization.AuthorizationAuthorizedReservation, ['reservation_time'], name, value)


                class AuthorizationOutOfCompliance(Entity):
                    """
                    License usage is out of compliance with the terms of the 
                    contract because more licenses are in use than were purchased.
                    
                    .. attribute:: last_comm_status_success
                    
                    	Last communication was successful or failed
                    	**type**\: bool
                    
                    .. attribute:: fail_message
                    
                    	Failure message if the last communications attempt failed. This can be displayed for the user. It is not a parsable string
                    	**type**\: str
                    
                    	**length:** 0..255
                    
                    .. attribute:: last_comm_time
                    
                    	Time the last communication attempt happened
                    	**type**\: str
                    
                    	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                    
                    .. attribute:: next_comm_time
                    
                    	The next time communications will be attempted to the back end. This will be zero if the initial communication has not completed
                    	**type**\: str
                    
                    	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                    
                    .. attribute:: comm_deadline_time
                    
                    	If there are no communications between now and this time smart licensing will enter the authorization expired state.  This may be zero indicating there is no deadline
                    	**type**\: str
                    
                    	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                    
                    .. attribute:: ooc_time
                    
                    	Time the product instance entered the out of compliance state
                    	**type**\: str
                    
                    	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                    
                    

                    """

                    _prefix = 'cisco-smart-license'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Licensing.State.StateInfo.Authorization.AuthorizationOutOfCompliance, self).__init__()

                        self.yang_name = "authorization-out-of-compliance"
                        self.yang_parent_name = "authorization"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('last_comm_status_success', YLeaf(YType.boolean, 'last-comm-status-success')),
                            ('fail_message', YLeaf(YType.str, 'fail-message')),
                            ('last_comm_time', YLeaf(YType.str, 'last-comm-time')),
                            ('next_comm_time', YLeaf(YType.str, 'next-comm-time')),
                            ('comm_deadline_time', YLeaf(YType.str, 'comm-deadline-time')),
                            ('ooc_time', YLeaf(YType.str, 'ooc-time')),
                        ])
                        self.last_comm_status_success = None
                        self.fail_message = None
                        self.last_comm_time = None
                        self.next_comm_time = None
                        self.comm_deadline_time = None
                        self.ooc_time = None
                        self._segment_path = lambda: "authorization-out-of-compliance"
                        self._absolute_path = lambda: "cisco-smart-license:licensing/state/state-info/authorization/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Licensing.State.StateInfo.Authorization.AuthorizationOutOfCompliance, ['last_comm_status_success', 'fail_message', 'last_comm_time', 'next_comm_time', 'comm_deadline_time', 'ooc_time'], name, value)


                class AuthorizationAuthorizationExpired(Entity):
                    """
                    The authorization period has expired because the product 
                    instance ahs not communicated with the SSM or satellite in 
                    over 90 days.
                    
                    .. attribute:: last_comm_status_success
                    
                    	Last communication was successful or failed
                    	**type**\: bool
                    
                    .. attribute:: fail_message
                    
                    	Failure message if the last communications attempt failed. This can be displayed for the user. It is not a parsable string
                    	**type**\: str
                    
                    	**length:** 0..255
                    
                    .. attribute:: last_comm_time
                    
                    	Time the last communication attempt happened
                    	**type**\: str
                    
                    	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                    
                    .. attribute:: next_comm_time
                    
                    	The next time communications will be attempted to the back end. This will be zero if the initial communication has not completed
                    	**type**\: str
                    
                    	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                    
                    .. attribute:: comm_deadline_time
                    
                    	If there are no communications between now and this time smart licensing will enter the authorization expired state.  This may be zero indicating there is no deadline
                    	**type**\: str
                    
                    	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                    
                    

                    """

                    _prefix = 'cisco-smart-license'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Licensing.State.StateInfo.Authorization.AuthorizationAuthorizationExpired, self).__init__()

                        self.yang_name = "authorization-authorization-expired"
                        self.yang_parent_name = "authorization"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('last_comm_status_success', YLeaf(YType.boolean, 'last-comm-status-success')),
                            ('fail_message', YLeaf(YType.str, 'fail-message')),
                            ('last_comm_time', YLeaf(YType.str, 'last-comm-time')),
                            ('next_comm_time', YLeaf(YType.str, 'next-comm-time')),
                            ('comm_deadline_time', YLeaf(YType.str, 'comm-deadline-time')),
                        ])
                        self.last_comm_status_success = None
                        self.fail_message = None
                        self.last_comm_time = None
                        self.next_comm_time = None
                        self.comm_deadline_time = None
                        self._segment_path = lambda: "authorization-authorization-expired"
                        self._absolute_path = lambda: "cisco-smart-license:licensing/state/state-info/authorization/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Licensing.State.StateInfo.Authorization.AuthorizationAuthorizationExpired, ['last_comm_status_success', 'fail_message', 'last_comm_time', 'next_comm_time', 'comm_deadline_time'], name, value)


            class Utility(Entity):
                """
                State of utility reporting.
                
                .. attribute:: enabled
                
                	Utility reporting is enabled. The system still  needs a utility certificate registration or a subscription  to begin reporting actual utility data
                	**type**\: bool
                
                .. attribute:: reporting
                
                	Is the system reporting utility data. If so then what triggered  it to start reporting. If this is utility\-reporting\-none then all of the times below will be zero
                	**type**\:  :py:class:`UtilityReportingTypeEnum <ydk.models.cisco_ios_xe.cisco_smart_license.UtilityReportingTypeEnum>`
                
                .. attribute:: reporting_times
                
                	If the product instance is reporting utility data this will contain various timing information about that reporting
                	**type**\:  :py:class:`ReportingTimes <ydk.models.cisco_ios_xe.cisco_smart_license.Licensing.State.StateInfo.Utility.ReportingTimes>`
                
                .. attribute:: customer_info
                
                	Customer address information that will be sent  in the utility usage reports
                	**type**\:  :py:class:`CustomerInfo <ydk.models.cisco_ios_xe.cisco_smart_license.Licensing.State.StateInfo.Utility.CustomerInfo>`
                
                

                """

                _prefix = 'cisco-smart-license'
                _revision = '2017-10-11'

                def __init__(self):
                    super(Licensing.State.StateInfo.Utility, self).__init__()

                    self.yang_name = "utility"
                    self.yang_parent_name = "state-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("reporting-times", ("reporting_times", Licensing.State.StateInfo.Utility.ReportingTimes)), ("customer-info", ("customer_info", Licensing.State.StateInfo.Utility.CustomerInfo))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('enabled', YLeaf(YType.boolean, 'enabled')),
                        ('reporting', YLeaf(YType.enumeration, 'reporting')),
                    ])
                    self.enabled = None
                    self.reporting = None

                    self.reporting_times = Licensing.State.StateInfo.Utility.ReportingTimes()
                    self.reporting_times.parent = self
                    self._children_name_map["reporting_times"] = "reporting-times"
                    self._children_yang_names.add("reporting-times")

                    self.customer_info = Licensing.State.StateInfo.Utility.CustomerInfo()
                    self.customer_info.parent = self
                    self._children_name_map["customer_info"] = "customer-info"
                    self._children_yang_names.add("customer-info")
                    self._segment_path = lambda: "utility"
                    self._absolute_path = lambda: "cisco-smart-license:licensing/state/state-info/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Licensing.State.StateInfo.Utility, ['enabled', 'reporting'], name, value)


                class ReportingTimes(Entity):
                    """
                    If the product instance is reporting utility data this will
                    contain various timing information about that reporting.
                    
                    .. attribute:: last_report_time
                    
                    	Time the last report was sent
                    	**type**\: str
                    
                    	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                    
                    .. attribute:: last_report_success
                    
                    	Was the last report successfully sent?
                    	**type**\: bool
                    
                    .. attribute:: fail_message
                    
                    	Failure message if the last report send failed
                    	**type**\: str
                    
                    	**length:** 0..255
                    
                    .. attribute:: next_report_time
                    
                    	Time the next report is scheduled to be sent
                    	**type**\: str
                    
                    	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                    
                    

                    """

                    _prefix = 'cisco-smart-license'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Licensing.State.StateInfo.Utility.ReportingTimes, self).__init__()

                        self.yang_name = "reporting-times"
                        self.yang_parent_name = "utility"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('last_report_time', YLeaf(YType.str, 'last-report-time')),
                            ('last_report_success', YLeaf(YType.boolean, 'last-report-success')),
                            ('fail_message', YLeaf(YType.str, 'fail-message')),
                            ('next_report_time', YLeaf(YType.str, 'next-report-time')),
                        ])
                        self.last_report_time = None
                        self.last_report_success = None
                        self.fail_message = None
                        self.next_report_time = None
                        self._segment_path = lambda: "reporting-times"
                        self._absolute_path = lambda: "cisco-smart-license:licensing/state/state-info/utility/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Licensing.State.StateInfo.Utility.ReportingTimes, ['last_report_time', 'last_report_success', 'fail_message', 'next_report_time'], name, value)


                class CustomerInfo(Entity):
                    """
                    Customer address information that will be sent 
                    in the utility usage reports.
                    
                    .. attribute:: id
                    
                    	The cisco issued customer id which will be included in the utility usage (RUM) report
                    	**type**\: str
                    
                    	**length:** 1..250
                    
                    .. attribute:: name
                    
                    	The customer company name which will be included in the utility usage (RUM) report
                    	**type**\: str
                    
                    	**length:** 1..250
                    
                    .. attribute:: street
                    
                    	The customer company street address which will be included in the utility usage (RUM) report
                    	**type**\: str
                    
                    	**length:** 1..250
                    
                    .. attribute:: city
                    
                    	The customer company city which will be included in the utility usage (RUM) report
                    	**type**\: str
                    
                    	**length:** 1..250
                    
                    .. attribute:: state
                    
                    	The customer company state which will be included in the utility usage (RUM) report
                    	**type**\: str
                    
                    	**length:** 1..250
                    
                    .. attribute:: country
                    
                    	The customer company country which will be included in the utility usage (RUM) report
                    	**type**\: str
                    
                    	**length:** 1..250
                    
                    .. attribute:: postal_code
                    
                    	The customer location specific postal code which will be included in the utility usage (RUM) report
                    	**type**\: str
                    
                    	**length:** 1..250
                    
                    

                    """

                    _prefix = 'cisco-smart-license'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Licensing.State.StateInfo.Utility.CustomerInfo, self).__init__()

                        self.yang_name = "customer-info"
                        self.yang_parent_name = "utility"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('id', YLeaf(YType.str, 'id')),
                            ('name', YLeaf(YType.str, 'name')),
                            ('street', YLeaf(YType.str, 'street')),
                            ('city', YLeaf(YType.str, 'city')),
                            ('state', YLeaf(YType.str, 'state')),
                            ('country', YLeaf(YType.str, 'country')),
                            ('postal_code', YLeaf(YType.str, 'postal-code')),
                        ])
                        self.id = None
                        self.name = None
                        self.street = None
                        self.city = None
                        self.state = None
                        self.country = None
                        self.postal_code = None
                        self._segment_path = lambda: "customer-info"
                        self._absolute_path = lambda: "cisco-smart-license:licensing/state/state-info/utility/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Licensing.State.StateInfo.Utility.CustomerInfo, ['id', 'name', 'street', 'city', 'state', 'country', 'postal_code'], name, value)


            class Transport(Entity):
                """
                State of the transport.
                
                .. attribute:: transport_type
                
                	Type of communications transport smart licensing is using
                	**type**\:  :py:class:`TransportTypeEnum <ydk.models.cisco_ios_xe.cisco_smart_license.TransportTypeEnum>`
                
                .. attribute:: url_settings
                
                	URLs in use if the transport type is smart
                	**type**\:  :py:class:`UrlSettings <ydk.models.cisco_ios_xe.cisco_smart_license.Licensing.State.StateInfo.Transport.UrlSettings>`
                
                

                """

                _prefix = 'cisco-smart-license'
                _revision = '2017-10-11'

                def __init__(self):
                    super(Licensing.State.StateInfo.Transport, self).__init__()

                    self.yang_name = "transport"
                    self.yang_parent_name = "state-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("url-settings", ("url_settings", Licensing.State.StateInfo.Transport.UrlSettings))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('transport_type', YLeaf(YType.enumeration, 'transport-type')),
                    ])
                    self.transport_type = None

                    self.url_settings = Licensing.State.StateInfo.Transport.UrlSettings()
                    self.url_settings.parent = self
                    self._children_name_map["url_settings"] = "url-settings"
                    self._children_yang_names.add("url-settings")
                    self._segment_path = lambda: "transport"
                    self._absolute_path = lambda: "cisco-smart-license:licensing/state/state-info/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Licensing.State.StateInfo.Transport, ['transport_type'], name, value)


                class UrlSettings(Entity):
                    """
                    URLs in use if the transport type is smart.
                    
                    .. attribute:: url_registration
                    
                    	The URL used for registration, authorization and any  other messages not related to utility
                    	**type**\: str
                    
                    .. attribute:: url_utility
                    
                    	The URL used for utility reporting. url\-utility and  url\-registration may be the same or different. If a satellite is in use then they will probably be the same
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'cisco-smart-license'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Licensing.State.StateInfo.Transport.UrlSettings, self).__init__()

                        self.yang_name = "url-settings"
                        self.yang_parent_name = "transport"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('url_registration', YLeaf(YType.str, 'url-registration')),
                            ('url_utility', YLeaf(YType.str, 'url-utility')),
                        ])
                        self.url_registration = None
                        self.url_utility = None
                        self._segment_path = lambda: "url-settings"
                        self._absolute_path = lambda: "cisco-smart-license:licensing/state/state-info/transport/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Licensing.State.StateInfo.Transport.UrlSettings, ['url_registration', 'url_utility'], name, value)


            class Privacy(Entity):
                """
                State of the privacy settings.
                
                .. attribute:: hostname
                
                	If true then the hostname will not be sent in  any messages
                	**type**\: bool
                
                .. attribute:: version
                
                	If true then the smart licensing version will not be sent in  any messages
                	**type**\: bool
                
                

                """

                _prefix = 'cisco-smart-license'
                _revision = '2017-10-11'

                def __init__(self):
                    super(Licensing.State.StateInfo.Privacy, self).__init__()

                    self.yang_name = "privacy"
                    self.yang_parent_name = "state-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('hostname', YLeaf(YType.boolean, 'hostname')),
                        ('version', YLeaf(YType.boolean, 'version')),
                    ])
                    self.hostname = None
                    self.version = None
                    self._segment_path = lambda: "privacy"
                    self._absolute_path = lambda: "cisco-smart-license:licensing/state/state-info/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Licensing.State.StateInfo.Privacy, ['hostname', 'version'], name, value)


            class Evaluation(Entity):
                """
                State of the evaluation period.
                
                .. attribute:: eval_in_use
                
                	Is the evaluation period currently in use and counting down
                	**type**\: bool
                
                .. attribute:: eval_expired
                
                	Has the evaluation period expired
                	**type**\: bool
                
                .. attribute:: eval_period_left
                
                	If the evaluation period is not expired this is the number  of seconds left in the period
                	**type**\:  :py:class:`EvalPeriodLeft <ydk.models.cisco_ios_xe.cisco_smart_license.Licensing.State.StateInfo.Evaluation.EvalPeriodLeft>`
                
                .. attribute:: eval_expire_time
                
                	If the evaluation period has expired then this is the  time of the expiration
                	**type**\:  :py:class:`EvalExpireTime <ydk.models.cisco_ios_xe.cisco_smart_license.Licensing.State.StateInfo.Evaluation.EvalExpireTime>`
                
                

                """

                _prefix = 'cisco-smart-license'
                _revision = '2017-10-11'

                def __init__(self):
                    super(Licensing.State.StateInfo.Evaluation, self).__init__()

                    self.yang_name = "evaluation"
                    self.yang_parent_name = "state-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("eval-period-left", ("eval_period_left", Licensing.State.StateInfo.Evaluation.EvalPeriodLeft)), ("eval-expire-time", ("eval_expire_time", Licensing.State.StateInfo.Evaluation.EvalExpireTime))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('eval_in_use', YLeaf(YType.boolean, 'eval-in-use')),
                        ('eval_expired', YLeaf(YType.boolean, 'eval-expired')),
                    ])
                    self.eval_in_use = None
                    self.eval_expired = None

                    self.eval_period_left = Licensing.State.StateInfo.Evaluation.EvalPeriodLeft()
                    self.eval_period_left.parent = self
                    self._children_name_map["eval_period_left"] = "eval-period-left"
                    self._children_yang_names.add("eval-period-left")

                    self.eval_expire_time = Licensing.State.StateInfo.Evaluation.EvalExpireTime()
                    self.eval_expire_time.parent = self
                    self._children_name_map["eval_expire_time"] = "eval-expire-time"
                    self._children_yang_names.add("eval-expire-time")
                    self._segment_path = lambda: "evaluation"
                    self._absolute_path = lambda: "cisco-smart-license:licensing/state/state-info/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Licensing.State.StateInfo.Evaluation, ['eval_in_use', 'eval_expired'], name, value)


                class EvalPeriodLeft(Entity):
                    """
                    If the evaluation period is not expired this is the number 
                    of seconds left in the period.
                    
                    .. attribute:: time_left
                    
                    	Number of seconds of license usage until the evaluation  period expires
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'cisco-smart-license'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Licensing.State.StateInfo.Evaluation.EvalPeriodLeft, self).__init__()

                        self.yang_name = "eval-period-left"
                        self.yang_parent_name = "evaluation"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('time_left', YLeaf(YType.uint32, 'time-left')),
                        ])
                        self.time_left = None
                        self._segment_path = lambda: "eval-period-left"
                        self._absolute_path = lambda: "cisco-smart-license:licensing/state/state-info/evaluation/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Licensing.State.StateInfo.Evaluation.EvalPeriodLeft, ['time_left'], name, value)


                class EvalExpireTime(Entity):
                    """
                    If the evaluation period has expired then this is the 
                    time of the expiration.
                    
                    .. attribute:: expire_time
                    
                    	Date and time the evaluation period expired
                    	**type**\: str
                    
                    	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                    
                    

                    """

                    _prefix = 'cisco-smart-license'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Licensing.State.StateInfo.Evaluation.EvalExpireTime, self).__init__()

                        self.yang_name = "eval-expire-time"
                        self.yang_parent_name = "evaluation"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('expire_time', YLeaf(YType.str, 'expire-time')),
                        ])
                        self.expire_time = None
                        self._segment_path = lambda: "eval-expire-time"
                        self._absolute_path = lambda: "cisco-smart-license:licensing/state/state-info/evaluation/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Licensing.State.StateInfo.Evaluation.EvalExpireTime, ['expire_time'], name, value)


            class Udi(Entity):
                """
                UDI of the system.
                
                .. attribute:: pid
                
                	The Product Identifier. Always combined with sn
                	**type**\: str
                
                	**length:** 1..255
                
                .. attribute:: sn
                
                	The system serial number. Always combined with pid
                	**type**\: str
                
                	**length:** 1..255
                
                .. attribute:: vid
                
                	The version identifier. Usually combined with pid & sn
                	**type**\: str
                
                	**length:** 1..255
                
                .. attribute:: uuid
                
                	A 32 byte hex value generated by the system.  This will be in proper UUID format 8\-4\-4\-4\-12. Often used by VMs or other systems that do not have a hardware identifier
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{8}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{4}\-[0\-9a\-fA\-F]{12}
                
                .. attribute:: suvi
                
                	Free form virtual identifier often used by software  only devices like software routers or VMs
                	**type**\: str
                
                	**length:** 1..255
                
                .. attribute:: host_identifier
                
                	Host identifier available on some systems.  Typically 8 hex digits
                	**type**\: str
                
                	**length:** 1..255
                
                .. attribute:: mac_address
                
                	The MAC address of the system. This is usually only used if there  is nothing else available to be used as an identifier
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                

                """

                _prefix = 'cisco-smart-license'
                _revision = '2017-10-11'

                def __init__(self):
                    super(Licensing.State.StateInfo.Udi, self).__init__()

                    self.yang_name = "udi"
                    self.yang_parent_name = "state-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('pid', YLeaf(YType.str, 'pid')),
                        ('sn', YLeaf(YType.str, 'sn')),
                        ('vid', YLeaf(YType.str, 'vid')),
                        ('uuid', YLeaf(YType.str, 'uuid')),
                        ('suvi', YLeaf(YType.str, 'suvi')),
                        ('host_identifier', YLeaf(YType.str, 'host-identifier')),
                        ('mac_address', YLeaf(YType.str, 'mac-address')),
                    ])
                    self.pid = None
                    self.sn = None
                    self.vid = None
                    self.uuid = None
                    self.suvi = None
                    self.host_identifier = None
                    self.mac_address = None
                    self._segment_path = lambda: "udi"
                    self._absolute_path = lambda: "cisco-smart-license:licensing/state/state-info/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Licensing.State.StateInfo.Udi, ['pid', 'sn', 'vid', 'uuid', 'suvi', 'host_identifier', 'mac_address'], name, value)


            class Usage(Entity):
                """
                List of license (entitlement tag) usage information. 
                This only contains the information for licenses that are in use.
                
                .. attribute:: entitlement_tag  (key)
                
                	The ISO 19770 entitlement tag used to define this license
                	**type**\: str
                
                .. attribute:: short_name
                
                	The human readable license name from the entitlement tag
                	**type**\: str
                
                .. attribute:: license_name
                
                	The license name that can be seen in the CSSM portal or on  the satellite.  This is only available after the product has registered
                	**type**\: str
                
                .. attribute:: description
                
                	The long description of this license. This is only available after the product has registered
                	**type**\: str
                
                .. attribute:: count
                
                	The in\-use count of this license. Note that licensing only reports  usage for licenses that are in use (count of 1 or greater)
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: enforcement_mode
                
                	The current enforcement mode of this license
                	**type**\:  :py:class:`EnforcementModeEnum <ydk.models.cisco_ios_xe.cisco_smart_license.EnforcementModeEnum>`
                
                .. attribute:: post_paid
                
                	If true then this entitlement is being reported in a post paid mode with utility usage reports. Otherwise it will be reported in  the regular prepaid mode
                	**type**\: bool
                
                .. attribute:: subscription_id
                
                	If this entitlement tag is being reported in the post paid utility usage mode and there is a subscription id in the customer's  virtual account this will be that subscription id
                	**type**\: str
                
                

                """

                _prefix = 'cisco-smart-license'
                _revision = '2017-10-11'

                def __init__(self):
                    super(Licensing.State.StateInfo.Usage, self).__init__()

                    self.yang_name = "usage"
                    self.yang_parent_name = "state-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['entitlement_tag']
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('entitlement_tag', YLeaf(YType.str, 'entitlement-tag')),
                        ('short_name', YLeaf(YType.str, 'short-name')),
                        ('license_name', YLeaf(YType.str, 'license-name')),
                        ('description', YLeaf(YType.str, 'description')),
                        ('count', YLeaf(YType.uint32, 'count')),
                        ('enforcement_mode', YLeaf(YType.enumeration, 'enforcement-mode')),
                        ('post_paid', YLeaf(YType.boolean, 'post-paid')),
                        ('subscription_id', YLeaf(YType.str, 'subscription-id')),
                    ])
                    self.entitlement_tag = None
                    self.short_name = None
                    self.license_name = None
                    self.description = None
                    self.count = None
                    self.enforcement_mode = None
                    self.post_paid = None
                    self.subscription_id = None
                    self._segment_path = lambda: "usage" + "[entitlement-tag='" + str(self.entitlement_tag) + "']"
                    self._absolute_path = lambda: "cisco-smart-license:licensing/state/state-info/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Licensing.State.StateInfo.Usage, ['entitlement_tag', 'short_name', 'license_name', 'description', 'count', 'enforcement_mode', 'post_paid', 'subscription_id'], name, value)

    def clone_ptr(self):
        self._top_entity = Licensing()
        return self._top_entity

