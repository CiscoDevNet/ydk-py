""" Cisco_IOS_XE_utd 

Cisco XE Native Unified Threat Defense (UTD) Yang model.
Copyright (c) 2016 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class UtdCategoryType(Enum):
    """
    UtdCategoryType (Enum Class)

    .. data:: abortion = 0

    .. data:: abused_drugs = 1

    .. data:: adult_and_pornography = 2

    .. data:: alcohol_and_tobacco = 3

    .. data:: auctions = 4

    .. data:: bot_nets = 5

    .. data:: business_and_economy = 6

    .. data:: cdns = 7

    .. data:: cheating = 8

    .. data:: computer_and_internet_info = 9

    .. data:: computer_and_internet_security = 10

    .. data:: confirmed_spam_sources = 11

    .. data:: cult_and_occult = 12

    .. data:: dating = 13

    .. data:: dead_sites = 14

    .. data:: dynamic_content = 15

    .. data:: educational_institutions = 16

    .. data:: entertainment_and_arts = 17

    .. data:: fashion_and_beauty = 18

    .. data:: financial_services = 19

    .. data:: gambling = 20

    .. data:: games = 21

    .. data:: government = 22

    .. data:: gross = 23

    .. data:: hacking = 24

    .. data:: hate_and_racism = 25

    .. data:: health_and_medicine = 26

    .. data:: home = 27

    .. data:: hunting_and_fishing = 28

    .. data:: illegal = 29

    .. data:: image_and_video_search = 30

    .. data:: individual_stock_advice_and_tools = 31

    .. data:: internet_communications = 32

    .. data:: internet_portals = 33

    .. data:: job_search = 34

    .. data:: keyloggers_and_monitoring = 35

    .. data:: kids = 36

    .. data:: legal = 37

    .. data:: local_information = 38

    .. data:: malware_sites = 39

    .. data:: marijuana = 40

    .. data:: military = 41

    .. data:: motor_vehicles = 42

    .. data:: music = 43

    .. data:: news_and_media = 44

    .. data:: nudity = 45

    .. data:: online_greeting_cards = 46

    .. data:: online_personal_storage = 47

    .. data:: open_http_proxies = 48

    .. data:: p2p = 49

    .. data:: parked_sites = 50

    .. data:: pay_to_surf = 51

    .. data:: personal_sites_and_blogs = 52

    .. data:: philosophy_and_political_advocacy = 53

    .. data:: phishing_and_other_frauds = 54

    .. data:: private_ip_addresses = 55

    .. data:: proxy_avoid_and_anonymizers = 56

    .. data:: questionable = 57

    .. data:: real_estate = 58

    .. data:: recreation_and_hobbies = 59

    .. data:: reference_and_research = 60

    .. data:: religion = 61

    .. data:: search_engines = 62

    .. data:: sex_education = 63

    .. data:: shareware_and_freeware = 64

    .. data:: shopping = 65

    .. data:: social_network = 66

    .. data:: society = 67

    .. data:: spam_urls = 68

    .. data:: sports = 69

    .. data:: spyware_and_adware = 70

    .. data:: streaming_media = 71

    .. data:: swimsuits_and_intimate_apparel = 72

    .. data:: training_and_tools = 73

    .. data:: translation = 74

    .. data:: travel = 75

    .. data:: uncategorized = 76

    .. data:: unconfirmed_spam_sources = 77

    .. data:: violence = 78

    .. data:: weapons = 79

    .. data:: web_advertisements = 80

    .. data:: web_based_email = 81

    .. data:: web_hosting = 82

    """

    abortion = Enum.YLeaf(0, "abortion")

    abused_drugs = Enum.YLeaf(1, "abused-drugs")

    adult_and_pornography = Enum.YLeaf(2, "adult-and-pornography")

    alcohol_and_tobacco = Enum.YLeaf(3, "alcohol-and-tobacco")

    auctions = Enum.YLeaf(4, "auctions")

    bot_nets = Enum.YLeaf(5, "bot-nets")

    business_and_economy = Enum.YLeaf(6, "business-and-economy")

    cdns = Enum.YLeaf(7, "cdns")

    cheating = Enum.YLeaf(8, "cheating")

    computer_and_internet_info = Enum.YLeaf(9, "computer-and-internet-info")

    computer_and_internet_security = Enum.YLeaf(10, "computer-and-internet-security")

    confirmed_spam_sources = Enum.YLeaf(11, "confirmed-spam-sources")

    cult_and_occult = Enum.YLeaf(12, "cult-and-occult")

    dating = Enum.YLeaf(13, "dating")

    dead_sites = Enum.YLeaf(14, "dead-sites")

    dynamic_content = Enum.YLeaf(15, "dynamic-content")

    educational_institutions = Enum.YLeaf(16, "educational-institutions")

    entertainment_and_arts = Enum.YLeaf(17, "entertainment-and-arts")

    fashion_and_beauty = Enum.YLeaf(18, "fashion-and-beauty")

    financial_services = Enum.YLeaf(19, "financial-services")

    gambling = Enum.YLeaf(20, "gambling")

    games = Enum.YLeaf(21, "games")

    government = Enum.YLeaf(22, "government")

    gross = Enum.YLeaf(23, "gross")

    hacking = Enum.YLeaf(24, "hacking")

    hate_and_racism = Enum.YLeaf(25, "hate-and-racism")

    health_and_medicine = Enum.YLeaf(26, "health-and-medicine")

    home = Enum.YLeaf(27, "home")

    hunting_and_fishing = Enum.YLeaf(28, "hunting-and-fishing")

    illegal = Enum.YLeaf(29, "illegal")

    image_and_video_search = Enum.YLeaf(30, "image-and-video-search")

    individual_stock_advice_and_tools = Enum.YLeaf(31, "individual-stock-advice-and-tools")

    internet_communications = Enum.YLeaf(32, "internet-communications")

    internet_portals = Enum.YLeaf(33, "internet-portals")

    job_search = Enum.YLeaf(34, "job-search")

    keyloggers_and_monitoring = Enum.YLeaf(35, "keyloggers-and-monitoring")

    kids = Enum.YLeaf(36, "kids")

    legal = Enum.YLeaf(37, "legal")

    local_information = Enum.YLeaf(38, "local-information")

    malware_sites = Enum.YLeaf(39, "malware-sites")

    marijuana = Enum.YLeaf(40, "marijuana")

    military = Enum.YLeaf(41, "military")

    motor_vehicles = Enum.YLeaf(42, "motor-vehicles")

    music = Enum.YLeaf(43, "music")

    news_and_media = Enum.YLeaf(44, "news-and-media")

    nudity = Enum.YLeaf(45, "nudity")

    online_greeting_cards = Enum.YLeaf(46, "online-greeting-cards")

    online_personal_storage = Enum.YLeaf(47, "online-personal-storage")

    open_http_proxies = Enum.YLeaf(48, "open-http-proxies")

    p2p = Enum.YLeaf(49, "p2p")

    parked_sites = Enum.YLeaf(50, "parked-sites")

    pay_to_surf = Enum.YLeaf(51, "pay-to-surf")

    personal_sites_and_blogs = Enum.YLeaf(52, "personal-sites-and-blogs")

    philosophy_and_political_advocacy = Enum.YLeaf(53, "philosophy-and-political-advocacy")

    phishing_and_other_frauds = Enum.YLeaf(54, "phishing-and-other-frauds")

    private_ip_addresses = Enum.YLeaf(55, "private-ip-addresses")

    proxy_avoid_and_anonymizers = Enum.YLeaf(56, "proxy-avoid-and-anonymizers")

    questionable = Enum.YLeaf(57, "questionable")

    real_estate = Enum.YLeaf(58, "real-estate")

    recreation_and_hobbies = Enum.YLeaf(59, "recreation-and-hobbies")

    reference_and_research = Enum.YLeaf(60, "reference-and-research")

    religion = Enum.YLeaf(61, "religion")

    search_engines = Enum.YLeaf(62, "search-engines")

    sex_education = Enum.YLeaf(63, "sex-education")

    shareware_and_freeware = Enum.YLeaf(64, "shareware-and-freeware")

    shopping = Enum.YLeaf(65, "shopping")

    social_network = Enum.YLeaf(66, "social-network")

    society = Enum.YLeaf(67, "society")

    spam_urls = Enum.YLeaf(68, "spam-urls")

    sports = Enum.YLeaf(69, "sports")

    spyware_and_adware = Enum.YLeaf(70, "spyware-and-adware")

    streaming_media = Enum.YLeaf(71, "streaming-media")

    swimsuits_and_intimate_apparel = Enum.YLeaf(72, "swimsuits-and-intimate-apparel")

    training_and_tools = Enum.YLeaf(73, "training-and-tools")

    translation = Enum.YLeaf(74, "translation")

    travel = Enum.YLeaf(75, "travel")

    uncategorized = Enum.YLeaf(76, "uncategorized")

    unconfirmed_spam_sources = Enum.YLeaf(77, "unconfirmed-spam-sources")

    violence = Enum.YLeaf(78, "violence")

    weapons = Enum.YLeaf(79, "weapons")

    web_advertisements = Enum.YLeaf(80, "web-advertisements")

    web_based_email = Enum.YLeaf(81, "web-based-email")

    web_hosting = Enum.YLeaf(82, "web-hosting")



