""" Cisco_IOS_XR_infra_infra_locale_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-infra\-locale package configuration.

This module contains definitions
for the following management objects\:
  locale\: Define the geographical locale

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class LocaleCountry(Enum):
    """
    LocaleCountry (Enum Class)

    Locale country

    .. data:: ad = 1

    	Andorra

    .. data:: ae = 2

    	United Arab Emirates

    .. data:: af = 3

    	Afghanistan

    .. data:: ag = 4

    	Antigua and Barbuda

    .. data:: ai = 5

    	Anguilla

    .. data:: al = 6

    	Albania

    .. data:: am = 7

    	Armenia

    .. data:: an = 8

    	Netherlands Antilles

    .. data:: ao = 9

    	Angola

    .. data:: aq = 10

    	Antarctica

    .. data:: ar = 11

    	Argentina

    .. data:: as_ = 12

    	American Samoa

    .. data:: at = 13

    	Austria

    .. data:: au = 14

    	Australia

    .. data:: aw = 15

    	Aruba

    .. data:: az = 16

    	Azerbaijan

    .. data:: ba = 17

    	Bosnia and Herzegovina

    .. data:: bb = 18

    	Barbados

    .. data:: bd = 19

    	Bangladesh

    .. data:: be = 20

    	Belgium

    .. data:: bf = 21

    	Burkina Faso

    .. data:: bg = 22

    	Bulgaria

    .. data:: bh = 23

    	Bahrain

    .. data:: bi = 24

    	Burundi

    .. data:: bj = 25

    	Benin

    .. data:: bm = 26

    	Bermuda

    .. data:: bn = 27

    	Brunei Darussalam

    .. data:: bo = 28

    	Bolivia

    .. data:: br = 29

    	Brazil

    .. data:: bs = 30

    	Bahamas

    .. data:: bt = 31

    	Bhutan

    .. data:: bv = 32

    	Bouvet Island

    .. data:: bw = 33

    	Botswana

    .. data:: by = 34

    	Belarus

    .. data:: bz = 35

    	Belize

    .. data:: ca = 36

    	Canada

    .. data:: cc = 37

    	Cocos (Keeling) Islands

    .. data:: cd = 38

    	Congo, The Democratic Republic of the (Zaire)

    .. data:: cf = 39

    	Central African Republic

    .. data:: cg = 40

    	Congo

    .. data:: ch = 41

    	Switzerland

    .. data:: ci = 42

    	Cote D'Ivoire

    .. data:: ck = 43

    	Cook Islands

    .. data:: cl = 44

    	Chile

    .. data:: cm = 45

    	Cameroon

    .. data:: cn = 46

    	China

    .. data:: co = 47

    	Colombia

    .. data:: cr = 48

    	Costa Rica

    .. data:: cu = 49

    	Cuba

    .. data:: cv = 50

    	Cape Verde

    .. data:: cx = 51

    	Christmas Island

    .. data:: cy = 52

    	Cyprus

    .. data:: cz = 53

    	Czech Republic

    .. data:: de = 54

    	Germany

    .. data:: dj = 55

    	Djibouti

    .. data:: dk = 56

    	Denmark

    .. data:: dm = 57

    	Dominica

    .. data:: do = 58

    	Dominican Republic

    .. data:: dz = 59

    	Algeria

    .. data:: ec = 60

    	Ecuador

    .. data:: ee = 61

    	Estonia

    .. data:: eg = 62

    	Egypt

    .. data:: eh = 63

    	Western Sahara

    .. data:: er = 64

    	Eritrea

    .. data:: es = 65

    	Spain

    .. data:: et = 66

    	Ethiopia

    .. data:: fi = 67

    	Finland

    .. data:: fj = 68

    	Fiji

    .. data:: fk = 69

    	Falkland Islands (Malvinas)

    .. data:: fm = 70

    	Micronesia, Federated States of

    .. data:: fo = 71

    	Faroe Islands

    .. data:: fr = 72

    	France

    .. data:: ga = 73

    	Gabon

    .. data:: gb = 74

    	United Kingdom

    .. data:: gd = 75

    	Grenada

    .. data:: ge = 76

    	Georgia

    .. data:: gf = 77

    	French Guiana

    .. data:: gh = 78

    	Ghana

    .. data:: gi = 79

    	Gibraltar

    .. data:: gl = 80

    	Greenland

    .. data:: gm = 81

    	Gambia

    .. data:: gn = 82

    	Guinea

    .. data:: gp = 83

    	Guadeloupe

    .. data:: gq = 84

    	Equatorial Guinea

    .. data:: gr = 85

    	Greece

    .. data:: gs = 86

    	South Georgia and the South Sandwich Islands

    .. data:: gt = 87

    	Guatemala

    .. data:: gu = 88

    	Guam

    .. data:: gw = 89

    	Guinea Bissau

    .. data:: gy = 90

    	Guyana

    .. data:: hk = 91

    	Hong Kong

    .. data:: hm = 92

    	Heard Island and McDonald Islands

    .. data:: hn = 93

    	Honduras

    .. data:: hr = 94

    	Croatia

    .. data:: ht = 95

    	Haiti

    .. data:: hu = 96

    	Hungary

    .. data:: id = 97

    	Indonesia

    .. data:: ie = 98

    	Ireland

    .. data:: il = 99

    	Israel

    .. data:: in_ = 100

    	India

    .. data:: io = 101

    	British Indian Ocean Territory

    .. data:: iq = 102

    	Iraq

    .. data:: ir = 103

    	Iran, Islamic Republic of

    .. data:: is_ = 104

    	Iceland

    .. data:: it = 105

    	Italy

    .. data:: jm = 106

    	Jamaica

    .. data:: jo = 107

    	Jordan

    .. data:: jp = 108

    	Japan

    .. data:: ke = 109

    	Kenya

    .. data:: kg = 110

    	Kyrgyzstan

    .. data:: kh = 111

    	Cambodia

    .. data:: ki = 112

    	Kiribati

    .. data:: km = 113

    	Comoros

    .. data:: kn = 114

    	Saint Kitts and Nevis

    .. data:: kp = 115

    	Korea, Democratic People's Republic of

    .. data:: kr = 116

    	Korea, Republic of

    .. data:: kw = 117

    	Kuwait

    .. data:: ky = 118

    	Cayman Islands

    .. data:: kz = 119

    	Kazakstan

    .. data:: la = 120

    	Lao People's Democratic Republic

    .. data:: lb = 121

    	Lebanon

    .. data:: lc = 122

    	Saint Lucia

    .. data:: li = 123

    	Liechtenstein

    .. data:: lk = 124

    	Sri Lanka

    .. data:: lr = 125

    	Liberia

    .. data:: ls = 126

    	Lesotho

    .. data:: lt = 127

    	Lithuania

    .. data:: lu = 128

    	Luxembourg

    .. data:: lv = 129

    	Latvia

    .. data:: ly = 130

    	Libyan Arab Jamahiriya

    .. data:: ma = 131

    	Morocco

    .. data:: mc = 132

    	Monaco

    .. data:: md = 133

    	Moldova, Republic of

    .. data:: mg = 134

    	Madagascar

    .. data:: mh = 135

    	Marshall Islands

    .. data:: mk = 136

    	Macedonia, The Former Yugoslav Republic of

    .. data:: ml = 137

    	Mali

    .. data:: mm = 138

    	Myanmar

    .. data:: mn = 139

    	Mongolia

    .. data:: mo = 140

    	Macau

    .. data:: mp = 141

    	Northern Mariana Islands

    .. data:: mq = 142

    	Martinique

    .. data:: mr = 143

    	Mauritania

    .. data:: ms = 144

    	Montserrat

    .. data:: mt = 145

    	Malta

    .. data:: mu = 146

    	Mauritius

    .. data:: mv = 147

    	Maldives

    .. data:: mw = 148

    	Malawi

    .. data:: mx = 149

    	Mexico

    .. data:: my = 150

    	Malaysia

    .. data:: mz = 151

    	Mozambique

    .. data:: na = 152

    	Namibia

    .. data:: nc = 153

    	New Caledonia

    .. data:: ne = 154

    	Niger

    .. data:: nf = 155

    	Norfolk Island

    .. data:: ng = 156

    	Nigeria

    .. data:: ni = 157

    	Nicaragua

    .. data:: nl = 158

    	Netherlands

    .. data:: no = 159

    	Norway

    .. data:: np = 160

    	Nepal

    .. data:: nr = 161

    	Nauru

    .. data:: nu = 162

    	Niue

    .. data:: nz = 163

    	New Zealand

    .. data:: om = 164

    	Oman

    .. data:: pa = 165

    	Panama

    .. data:: pe = 166

    	Peru

    .. data:: pf = 167

    	French Polynesia

    .. data:: pg = 168

    	Papua New Guinea

    .. data:: ph = 169

    	Philippines

    .. data:: pk = 170

    	Pakistan

    .. data:: pl = 171

    	Poland

    .. data:: pm = 172

    	Saint Pierre and Miquelon

    .. data:: pn = 173

    	Pitcairn

    .. data:: pr = 174

    	Puerto Rico

    .. data:: pt = 175

    	Portugal

    .. data:: pw = 176

    	Palau

    .. data:: py = 177

    	Paraguay

    .. data:: qa = 178

    	Qatar

    .. data:: re = 179

    	Reunion

    .. data:: ro = 180

    	Romania

    .. data:: ru = 181

    	Russian Federation

    .. data:: rw = 182

    	Rwanda

    .. data:: sa = 183

    	Saudi Arabia

    .. data:: sb = 184

    	Solomon Islands

    .. data:: sc = 185

    	Seychelles

    .. data:: sd = 186

    	Sudan

    .. data:: se = 187

    	Sweden

    .. data:: sg = 188

    	Singapore

    .. data:: sh = 189

    	Saint Helena

    .. data:: si = 190

    	Slovenia

    .. data:: sj = 191

    	Svalbard and Jan Mayen

    .. data:: sk = 192

    	Slovakia

    .. data:: sl = 193

    	Sierra Leone

    .. data:: sm = 194

    	San Marino

    .. data:: sn = 195

    	Senegal

    .. data:: so = 196

    	Somalia

    .. data:: sr = 197

    	Suriname

    .. data:: st = 198

    	Sao Tome and Principe

    .. data:: sv = 199

    	El Salvador

    .. data:: sy = 200

    	Syrian Arab Republic

    .. data:: sz = 201

    	Swaziland

    .. data:: tc = 202

    	Turks and Caicos Islands

    .. data:: td = 203

    	Chad

    .. data:: tf = 204

    	French Southern Territories

    .. data:: tg = 205

    	Togo

    .. data:: th = 206

    	Thailand

    .. data:: tj = 207

    	Tajikistan

    .. data:: tk = 208

    	Tokelau

    .. data:: tm = 209

    	Turkmenistan

    .. data:: tn = 210

    	Tunisia

    .. data:: to = 211

    	Tonga

    .. data:: tp = 212

    	East Timor

    .. data:: tr = 213

    	Turkey

    .. data:: tt = 214

    	Trinidad and Tobago

    .. data:: tv = 215

    	Tuvalu

    .. data:: tw = 216

    	Taiwan, Province of China

    .. data:: tz = 217

    	Tanzania, United Republic of

    .. data:: ua = 218

    	Ukraine

    .. data:: ug = 219

    	Uganda

    .. data:: um = 220

    	United States Minor Outlying Islands

    .. data:: us = 221

    	United States

    .. data:: uy = 222

    	Uruguay

    .. data:: uz = 223

    	Uzbekistan

    .. data:: va = 224

    	Holy See (Vatican City State)

    .. data:: vc = 225

    	Saint Vincent and The Grenadines

    .. data:: ve = 226

    	Venezuela

    .. data:: vg = 227

    	Virgin Islands, British

    .. data:: vi = 228

    	Virgin Islands, U.S.

    .. data:: vn = 229

    	Vietnam

    .. data:: vu = 230

    	Vanuatu

    .. data:: wf = 231

    	Wallis and Futuna

    .. data:: ws = 232

    	Samoa

    .. data:: ye = 233

    	Yemen

    .. data:: yt = 234

    	Mayotte

    .. data:: yu = 235

    	Yugoslavia

    .. data:: za = 236

    	South Africa

    .. data:: zm = 237

    	Zambia

    .. data:: zw = 238

    	Zimbabwe

    """

    ad = Enum.YLeaf(1, "ad")

    ae = Enum.YLeaf(2, "ae")

    af = Enum.YLeaf(3, "af")

    ag = Enum.YLeaf(4, "ag")

    ai = Enum.YLeaf(5, "ai")

    al = Enum.YLeaf(6, "al")

    am = Enum.YLeaf(7, "am")

    an = Enum.YLeaf(8, "an")

    ao = Enum.YLeaf(9, "ao")

    aq = Enum.YLeaf(10, "aq")

    ar = Enum.YLeaf(11, "ar")

    as_ = Enum.YLeaf(12, "as")

    at = Enum.YLeaf(13, "at")

    au = Enum.YLeaf(14, "au")

    aw = Enum.YLeaf(15, "aw")

    az = Enum.YLeaf(16, "az")

    ba = Enum.YLeaf(17, "ba")

    bb = Enum.YLeaf(18, "bb")

    bd = Enum.YLeaf(19, "bd")

    be = Enum.YLeaf(20, "be")

    bf = Enum.YLeaf(21, "bf")

    bg = Enum.YLeaf(22, "bg")

    bh = Enum.YLeaf(23, "bh")

    bi = Enum.YLeaf(24, "bi")

    bj = Enum.YLeaf(25, "bj")

    bm = Enum.YLeaf(26, "bm")

    bn = Enum.YLeaf(27, "bn")

    bo = Enum.YLeaf(28, "bo")

    br = Enum.YLeaf(29, "br")

    bs = Enum.YLeaf(30, "bs")

    bt = Enum.YLeaf(31, "bt")

    bv = Enum.YLeaf(32, "bv")

    bw = Enum.YLeaf(33, "bw")

    by = Enum.YLeaf(34, "by")

    bz = Enum.YLeaf(35, "bz")

    ca = Enum.YLeaf(36, "ca")

    cc = Enum.YLeaf(37, "cc")

    cd = Enum.YLeaf(38, "cd")

    cf = Enum.YLeaf(39, "cf")

    cg = Enum.YLeaf(40, "cg")

    ch = Enum.YLeaf(41, "ch")

    ci = Enum.YLeaf(42, "ci")

    ck = Enum.YLeaf(43, "ck")

    cl = Enum.YLeaf(44, "cl")

    cm = Enum.YLeaf(45, "cm")

    cn = Enum.YLeaf(46, "cn")

    co = Enum.YLeaf(47, "co")

    cr = Enum.YLeaf(48, "cr")

    cu = Enum.YLeaf(49, "cu")

    cv = Enum.YLeaf(50, "cv")

    cx = Enum.YLeaf(51, "cx")

    cy = Enum.YLeaf(52, "cy")

    cz = Enum.YLeaf(53, "cz")

    de = Enum.YLeaf(54, "de")

    dj = Enum.YLeaf(55, "dj")

    dk = Enum.YLeaf(56, "dk")

    dm = Enum.YLeaf(57, "dm")

    do = Enum.YLeaf(58, "do")

    dz = Enum.YLeaf(59, "dz")

    ec = Enum.YLeaf(60, "ec")

    ee = Enum.YLeaf(61, "ee")

    eg = Enum.YLeaf(62, "eg")

    eh = Enum.YLeaf(63, "eh")

    er = Enum.YLeaf(64, "er")

    es = Enum.YLeaf(65, "es")

    et = Enum.YLeaf(66, "et")

    fi = Enum.YLeaf(67, "fi")

    fj = Enum.YLeaf(68, "fj")

    fk = Enum.YLeaf(69, "fk")

    fm = Enum.YLeaf(70, "fm")

    fo = Enum.YLeaf(71, "fo")

    fr = Enum.YLeaf(72, "fr")

    ga = Enum.YLeaf(73, "ga")

    gb = Enum.YLeaf(74, "gb")

    gd = Enum.YLeaf(75, "gd")

    ge = Enum.YLeaf(76, "ge")

    gf = Enum.YLeaf(77, "gf")

    gh = Enum.YLeaf(78, "gh")

    gi = Enum.YLeaf(79, "gi")

    gl = Enum.YLeaf(80, "gl")

    gm = Enum.YLeaf(81, "gm")

    gn = Enum.YLeaf(82, "gn")

    gp = Enum.YLeaf(83, "gp")

    gq = Enum.YLeaf(84, "gq")

    gr = Enum.YLeaf(85, "gr")

    gs = Enum.YLeaf(86, "gs")

    gt = Enum.YLeaf(87, "gt")

    gu = Enum.YLeaf(88, "gu")

    gw = Enum.YLeaf(89, "gw")

    gy = Enum.YLeaf(90, "gy")

    hk = Enum.YLeaf(91, "hk")

    hm = Enum.YLeaf(92, "hm")

    hn = Enum.YLeaf(93, "hn")

    hr = Enum.YLeaf(94, "hr")

    ht = Enum.YLeaf(95, "ht")

    hu = Enum.YLeaf(96, "hu")

    id = Enum.YLeaf(97, "id")

    ie = Enum.YLeaf(98, "ie")

    il = Enum.YLeaf(99, "il")

    in_ = Enum.YLeaf(100, "in")

    io = Enum.YLeaf(101, "io")

    iq = Enum.YLeaf(102, "iq")

    ir = Enum.YLeaf(103, "ir")

    is_ = Enum.YLeaf(104, "is")

    it = Enum.YLeaf(105, "it")

    jm = Enum.YLeaf(106, "jm")

    jo = Enum.YLeaf(107, "jo")

    jp = Enum.YLeaf(108, "jp")

    ke = Enum.YLeaf(109, "ke")

    kg = Enum.YLeaf(110, "kg")

    kh = Enum.YLeaf(111, "kh")

    ki = Enum.YLeaf(112, "ki")

    km = Enum.YLeaf(113, "km")

    kn = Enum.YLeaf(114, "kn")

    kp = Enum.YLeaf(115, "kp")

    kr = Enum.YLeaf(116, "kr")

    kw = Enum.YLeaf(117, "kw")

    ky = Enum.YLeaf(118, "ky")

    kz = Enum.YLeaf(119, "kz")

    la = Enum.YLeaf(120, "la")

    lb = Enum.YLeaf(121, "lb")

    lc = Enum.YLeaf(122, "lc")

    li = Enum.YLeaf(123, "li")

    lk = Enum.YLeaf(124, "lk")

    lr = Enum.YLeaf(125, "lr")

    ls = Enum.YLeaf(126, "ls")

    lt = Enum.YLeaf(127, "lt")

    lu = Enum.YLeaf(128, "lu")

    lv = Enum.YLeaf(129, "lv")

    ly = Enum.YLeaf(130, "ly")

    ma = Enum.YLeaf(131, "ma")

    mc = Enum.YLeaf(132, "mc")

    md = Enum.YLeaf(133, "md")

    mg = Enum.YLeaf(134, "mg")

    mh = Enum.YLeaf(135, "mh")

    mk = Enum.YLeaf(136, "mk")

    ml = Enum.YLeaf(137, "ml")

    mm = Enum.YLeaf(138, "mm")

    mn = Enum.YLeaf(139, "mn")

    mo = Enum.YLeaf(140, "mo")

    mp = Enum.YLeaf(141, "mp")

    mq = Enum.YLeaf(142, "mq")

    mr = Enum.YLeaf(143, "mr")

    ms = Enum.YLeaf(144, "ms")

    mt = Enum.YLeaf(145, "mt")

    mu = Enum.YLeaf(146, "mu")

    mv = Enum.YLeaf(147, "mv")

    mw = Enum.YLeaf(148, "mw")

    mx = Enum.YLeaf(149, "mx")

    my = Enum.YLeaf(150, "my")

    mz = Enum.YLeaf(151, "mz")

    na = Enum.YLeaf(152, "na")

    nc = Enum.YLeaf(153, "nc")

    ne = Enum.YLeaf(154, "ne")

    nf = Enum.YLeaf(155, "nf")

    ng = Enum.YLeaf(156, "ng")

    ni = Enum.YLeaf(157, "ni")

    nl = Enum.YLeaf(158, "nl")

    no = Enum.YLeaf(159, "no")

    np = Enum.YLeaf(160, "np")

    nr = Enum.YLeaf(161, "nr")

    nu = Enum.YLeaf(162, "nu")

    nz = Enum.YLeaf(163, "nz")

    om = Enum.YLeaf(164, "om")

    pa = Enum.YLeaf(165, "pa")

    pe = Enum.YLeaf(166, "pe")

    pf = Enum.YLeaf(167, "pf")

    pg = Enum.YLeaf(168, "pg")

    ph = Enum.YLeaf(169, "ph")

    pk = Enum.YLeaf(170, "pk")

    pl = Enum.YLeaf(171, "pl")

    pm = Enum.YLeaf(172, "pm")

    pn = Enum.YLeaf(173, "pn")

    pr = Enum.YLeaf(174, "pr")

    pt = Enum.YLeaf(175, "pt")

    pw = Enum.YLeaf(176, "pw")

    py = Enum.YLeaf(177, "py")

    qa = Enum.YLeaf(178, "qa")

    re = Enum.YLeaf(179, "re")

    ro = Enum.YLeaf(180, "ro")

    ru = Enum.YLeaf(181, "ru")

    rw = Enum.YLeaf(182, "rw")

    sa = Enum.YLeaf(183, "sa")

    sb = Enum.YLeaf(184, "sb")

    sc = Enum.YLeaf(185, "sc")

    sd = Enum.YLeaf(186, "sd")

    se = Enum.YLeaf(187, "se")

    sg = Enum.YLeaf(188, "sg")

    sh = Enum.YLeaf(189, "sh")

    si = Enum.YLeaf(190, "si")

    sj = Enum.YLeaf(191, "sj")

    sk = Enum.YLeaf(192, "sk")

    sl = Enum.YLeaf(193, "sl")

    sm = Enum.YLeaf(194, "sm")

    sn = Enum.YLeaf(195, "sn")

    so = Enum.YLeaf(196, "so")

    sr = Enum.YLeaf(197, "sr")

    st = Enum.YLeaf(198, "st")

    sv = Enum.YLeaf(199, "sv")

    sy = Enum.YLeaf(200, "sy")

    sz = Enum.YLeaf(201, "sz")

    tc = Enum.YLeaf(202, "tc")

    td = Enum.YLeaf(203, "td")

    tf = Enum.YLeaf(204, "tf")

    tg = Enum.YLeaf(205, "tg")

    th = Enum.YLeaf(206, "th")

    tj = Enum.YLeaf(207, "tj")

    tk = Enum.YLeaf(208, "tk")

    tm = Enum.YLeaf(209, "tm")

    tn = Enum.YLeaf(210, "tn")

    to = Enum.YLeaf(211, "to")

    tp = Enum.YLeaf(212, "tp")

    tr = Enum.YLeaf(213, "tr")

    tt = Enum.YLeaf(214, "tt")

    tv = Enum.YLeaf(215, "tv")

    tw = Enum.YLeaf(216, "tw")

    tz = Enum.YLeaf(217, "tz")

    ua = Enum.YLeaf(218, "ua")

    ug = Enum.YLeaf(219, "ug")

    um = Enum.YLeaf(220, "um")

    us = Enum.YLeaf(221, "us")

    uy = Enum.YLeaf(222, "uy")

    uz = Enum.YLeaf(223, "uz")

    va = Enum.YLeaf(224, "va")

    vc = Enum.YLeaf(225, "vc")

    ve = Enum.YLeaf(226, "ve")

    vg = Enum.YLeaf(227, "vg")

    vi = Enum.YLeaf(228, "vi")

    vn = Enum.YLeaf(229, "vn")

    vu = Enum.YLeaf(230, "vu")

    wf = Enum.YLeaf(231, "wf")

    ws = Enum.YLeaf(232, "ws")

    ye = Enum.YLeaf(233, "ye")

    yt = Enum.YLeaf(234, "yt")

    yu = Enum.YLeaf(235, "yu")

    za = Enum.YLeaf(236, "za")

    zm = Enum.YLeaf(237, "zm")

    zw = Enum.YLeaf(238, "zw")


class LocaleLanguage(Enum):
    """
    LocaleLanguage (Enum Class)

    Locale language

    .. data:: aa = 1

    	Afar

    .. data:: ab = 2

    	Abkhazian

    .. data:: af = 3

    	Afrikaans

    .. data:: am = 4

    	Amharic

    .. data:: ar = 5

    	Arabic

    .. data:: as_ = 6

    	Assamese

    .. data:: ay = 7

    	Aymara

    .. data:: az = 8

    	Azerbaijani

    .. data:: ba = 9

    	Bashkir

    .. data:: be = 10

    	Byelorussian

    .. data:: bg = 11

    	Bulgarian

    .. data:: bh = 12

    	Bihari

    .. data:: bi = 13

    	Bislama

    .. data:: bn = 14

    	Bengali

    .. data:: bo = 15

    	Tibetan

    .. data:: br = 16

    	Breton

    .. data:: ca = 17

    	Catalan

    .. data:: co = 18

    	Corsican

    .. data:: cs = 19

    	Czech

    .. data:: cy = 20

    	Welsh

    .. data:: da = 21

    	Danish

    .. data:: de = 22

    	German

    .. data:: dz = 23

    	Bhutani

    .. data:: el = 24

    	Greek

    .. data:: en = 25

    	English

    .. data:: eo = 26

    	Esperanto

    .. data:: es = 27

    	Spanish

    .. data:: et = 28

    	Estonian

    .. data:: eu = 29

    	Basque

    .. data:: fa = 30

    	Persian

    .. data:: fi = 31

    	Finnish

    .. data:: fj = 32

    	Fiji

    .. data:: fo = 33

    	Faroese

    .. data:: fr = 34

    	French

    .. data:: fy = 35

    	Frisian

    .. data:: ga = 36

    	Irish

    .. data:: gd = 37

    	Scots Gaelic

    .. data:: gl = 38

    	Galician

    .. data:: gn = 39

    	Guarani

    .. data:: gu = 40

    	Gujarati

    .. data:: ha = 41

    	Hausa

    .. data:: he = 42

    	Hebrew

    .. data:: hi = 43

    	Hindi

    .. data:: hr = 44

    	Croatian

    .. data:: hu = 45

    	Hungarian

    .. data:: hy = 46

    	Armenian

    .. data:: ia = 47

    	Interlingua

    .. data:: id = 48

    	Indonesian

    .. data:: ie = 49

    	Interlingue

    .. data:: ik = 50

    	Inupiak

    .. data:: is_ = 51

    	Icelandic

    .. data:: it = 52

    	Italian

    .. data:: iu = 53

    	Inuktitut

    .. data:: ja = 54

    	Japanese

    .. data:: jw = 55

    	Javanese

    .. data:: ka = 56

    	Georgian

    .. data:: kk = 57

    	Kazakh

    .. data:: kl = 58

    	Greenlandic

    .. data:: km = 59

    	Cambodian

    .. data:: kn = 60

    	Kannada

    .. data:: ko = 61

    	Korean

    .. data:: ks = 62

    	Kashmiri

    .. data:: ku = 63

    	Kurdish

    .. data:: ky = 64

    	Kirghiz

    .. data:: la = 65

    	Latin

    .. data:: ln = 66

    	Lingala

    .. data:: lo = 67

    	Laothian

    .. data:: lt = 68

    	Lithuanian

    .. data:: lv = 69

    	Latvian, Lettish

    .. data:: mg = 70

    	Malagasy

    .. data:: mi = 71

    	Maori

    .. data:: mk = 72

    	Macedonian

    .. data:: ml = 73

    	Malayalam

    .. data:: mn = 74

    	Mongolian

    .. data:: mo = 75

    	Moldavian

    .. data:: mr = 76

    	Marathi

    .. data:: ms = 77

    	Malay

    .. data:: mt = 78

    	Maltese

    .. data:: my = 79

    	Burmese

    .. data:: na = 80

    	Nauru

    .. data:: ne = 81

    	Nepali

    .. data:: nl = 82

    	Dutch

    .. data:: no = 83

    	Norwegian

    .. data:: oc = 84

    	Occitan

    .. data:: om = 85

    	(Afan) Oromo

    .. data:: or_ = 86

    	Oriya

    .. data:: pa = 87

    	Punjabi

    .. data:: pl = 88

    	Polish

    .. data:: ps = 89

    	Pashto, Pushto

    .. data:: pt = 90

    	Portuguese

    .. data:: qu = 91

    	Quechua

    .. data:: rm = 92

    	Rhaeto Romance

    .. data:: rn = 93

    	Kirundi

    .. data:: ro = 94

    	Romanian

    .. data:: ru = 95

    	Russian

    .. data:: rw = 96

    	Kinyarwanda

    .. data:: sa = 97

    	Sanskrit

    .. data:: sd = 98

    	Sindhi

    .. data:: sg = 99

    	Sangho

    .. data:: sh = 100

    	Serbo Croatian

    .. data:: si = 101

    	Sinhalese

    .. data:: sk = 102

    	Slovak

    .. data:: sl = 103

    	Slovenian

    .. data:: sm = 104

    	Samoan

    .. data:: sn = 105

    	Shona

    .. data:: so = 106

    	Somali

    .. data:: sq = 107

    	Albanian

    .. data:: sr = 108

    	Serbian

    .. data:: ss = 109

    	Siswati

    .. data:: st = 110

    	Sesotho

    .. data:: su = 111

    	Sundanese

    .. data:: sv = 112

    	Swedish

    .. data:: sw = 113

    	Swahili

    .. data:: ta = 114

    	Tamil

    .. data:: te = 115

    	Telugu

    .. data:: tg = 116

    	Tajik

    .. data:: th = 117

    	Thai

    .. data:: ti = 118

    	Tigrinya

    .. data:: tk = 119

    	Turkmen

    .. data:: tl = 120

    	Tagalog

    .. data:: tn = 121

    	Setswana

    .. data:: to = 122

    	Tonga

    .. data:: tr = 123

    	Turkish

    .. data:: ts = 124

    	Tsonga

    .. data:: tt = 125

    	Tatar

    .. data:: tw = 126

    	Twi

    .. data:: ug = 127

    	Uighur

    .. data:: uk = 128

    	Ukrainian

    .. data:: ur = 129

    	Urdu

    .. data:: uz = 130

    	Uzbek

    .. data:: vi = 131

    	Vietnamese

    .. data:: vo = 132

    	Volapuk

    .. data:: wo = 133

    	Wolof

    .. data:: xh = 134

    	Xhosa

    .. data:: yi = 135

    	Yiddish

    .. data:: yo = 136

    	Yoruba

    .. data:: za = 137

    	Zhuang

    .. data:: zh = 138

    	Chinese

    .. data:: zu = 139

    	Zulu

    """

    aa = Enum.YLeaf(1, "aa")

    ab = Enum.YLeaf(2, "ab")

    af = Enum.YLeaf(3, "af")

    am = Enum.YLeaf(4, "am")

    ar = Enum.YLeaf(5, "ar")

    as_ = Enum.YLeaf(6, "as")

    ay = Enum.YLeaf(7, "ay")

    az = Enum.YLeaf(8, "az")

    ba = Enum.YLeaf(9, "ba")

    be = Enum.YLeaf(10, "be")

    bg = Enum.YLeaf(11, "bg")

    bh = Enum.YLeaf(12, "bh")

    bi = Enum.YLeaf(13, "bi")

    bn = Enum.YLeaf(14, "bn")

    bo = Enum.YLeaf(15, "bo")

    br = Enum.YLeaf(16, "br")

    ca = Enum.YLeaf(17, "ca")

    co = Enum.YLeaf(18, "co")

    cs = Enum.YLeaf(19, "cs")

    cy = Enum.YLeaf(20, "cy")

    da = Enum.YLeaf(21, "da")

    de = Enum.YLeaf(22, "de")

    dz = Enum.YLeaf(23, "dz")

    el = Enum.YLeaf(24, "el")

    en = Enum.YLeaf(25, "en")

    eo = Enum.YLeaf(26, "eo")

    es = Enum.YLeaf(27, "es")

    et = Enum.YLeaf(28, "et")

    eu = Enum.YLeaf(29, "eu")

    fa = Enum.YLeaf(30, "fa")

    fi = Enum.YLeaf(31, "fi")

    fj = Enum.YLeaf(32, "fj")

    fo = Enum.YLeaf(33, "fo")

    fr = Enum.YLeaf(34, "fr")

    fy = Enum.YLeaf(35, "fy")

    ga = Enum.YLeaf(36, "ga")

    gd = Enum.YLeaf(37, "gd")

    gl = Enum.YLeaf(38, "gl")

    gn = Enum.YLeaf(39, "gn")

    gu = Enum.YLeaf(40, "gu")

    ha = Enum.YLeaf(41, "ha")

    he = Enum.YLeaf(42, "he")

    hi = Enum.YLeaf(43, "hi")

    hr = Enum.YLeaf(44, "hr")

    hu = Enum.YLeaf(45, "hu")

    hy = Enum.YLeaf(46, "hy")

    ia = Enum.YLeaf(47, "ia")

    id = Enum.YLeaf(48, "id")

    ie = Enum.YLeaf(49, "ie")

    ik = Enum.YLeaf(50, "ik")

    is_ = Enum.YLeaf(51, "is")

    it = Enum.YLeaf(52, "it")

    iu = Enum.YLeaf(53, "iu")

    ja = Enum.YLeaf(54, "ja")

    jw = Enum.YLeaf(55, "jw")

    ka = Enum.YLeaf(56, "ka")

    kk = Enum.YLeaf(57, "kk")

    kl = Enum.YLeaf(58, "kl")

    km = Enum.YLeaf(59, "km")

    kn = Enum.YLeaf(60, "kn")

    ko = Enum.YLeaf(61, "ko")

    ks = Enum.YLeaf(62, "ks")

    ku = Enum.YLeaf(63, "ku")

    ky = Enum.YLeaf(64, "ky")

    la = Enum.YLeaf(65, "la")

    ln = Enum.YLeaf(66, "ln")

    lo = Enum.YLeaf(67, "lo")

    lt = Enum.YLeaf(68, "lt")

    lv = Enum.YLeaf(69, "lv")

    mg = Enum.YLeaf(70, "mg")

    mi = Enum.YLeaf(71, "mi")

    mk = Enum.YLeaf(72, "mk")

    ml = Enum.YLeaf(73, "ml")

    mn = Enum.YLeaf(74, "mn")

    mo = Enum.YLeaf(75, "mo")

    mr = Enum.YLeaf(76, "mr")

    ms = Enum.YLeaf(77, "ms")

    mt = Enum.YLeaf(78, "mt")

    my = Enum.YLeaf(79, "my")

    na = Enum.YLeaf(80, "na")

    ne = Enum.YLeaf(81, "ne")

    nl = Enum.YLeaf(82, "nl")

    no = Enum.YLeaf(83, "no")

    oc = Enum.YLeaf(84, "oc")

    om = Enum.YLeaf(85, "om")

    or_ = Enum.YLeaf(86, "or")

    pa = Enum.YLeaf(87, "pa")

    pl = Enum.YLeaf(88, "pl")

    ps = Enum.YLeaf(89, "ps")

    pt = Enum.YLeaf(90, "pt")

    qu = Enum.YLeaf(91, "qu")

    rm = Enum.YLeaf(92, "rm")

    rn = Enum.YLeaf(93, "rn")

    ro = Enum.YLeaf(94, "ro")

    ru = Enum.YLeaf(95, "ru")

    rw = Enum.YLeaf(96, "rw")

    sa = Enum.YLeaf(97, "sa")

    sd = Enum.YLeaf(98, "sd")

    sg = Enum.YLeaf(99, "sg")

    sh = Enum.YLeaf(100, "sh")

    si = Enum.YLeaf(101, "si")

    sk = Enum.YLeaf(102, "sk")

    sl = Enum.YLeaf(103, "sl")

    sm = Enum.YLeaf(104, "sm")

    sn = Enum.YLeaf(105, "sn")

    so = Enum.YLeaf(106, "so")

    sq = Enum.YLeaf(107, "sq")

    sr = Enum.YLeaf(108, "sr")

    ss = Enum.YLeaf(109, "ss")

    st = Enum.YLeaf(110, "st")

    su = Enum.YLeaf(111, "su")

    sv = Enum.YLeaf(112, "sv")

    sw = Enum.YLeaf(113, "sw")

    ta = Enum.YLeaf(114, "ta")

    te = Enum.YLeaf(115, "te")

    tg = Enum.YLeaf(116, "tg")

    th = Enum.YLeaf(117, "th")

    ti = Enum.YLeaf(118, "ti")

    tk = Enum.YLeaf(119, "tk")

    tl = Enum.YLeaf(120, "tl")

    tn = Enum.YLeaf(121, "tn")

    to = Enum.YLeaf(122, "to")

    tr = Enum.YLeaf(123, "tr")

    ts = Enum.YLeaf(124, "ts")

    tt = Enum.YLeaf(125, "tt")

    tw = Enum.YLeaf(126, "tw")

    ug = Enum.YLeaf(127, "ug")

    uk = Enum.YLeaf(128, "uk")

    ur = Enum.YLeaf(129, "ur")

    uz = Enum.YLeaf(130, "uz")

    vi = Enum.YLeaf(131, "vi")

    vo = Enum.YLeaf(132, "vo")

    wo = Enum.YLeaf(133, "wo")

    xh = Enum.YLeaf(134, "xh")

    yi = Enum.YLeaf(135, "yi")

    yo = Enum.YLeaf(136, "yo")

    za = Enum.YLeaf(137, "za")

    zh = Enum.YLeaf(138, "zh")

    zu = Enum.YLeaf(139, "zu")



class Locale(Entity):
    """
    Define the geographical locale
    
    .. attribute:: country
    
    	Name of country locale
    	**type**\:  :py:class:`LocaleCountry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_infra_locale_cfg.LocaleCountry>`
    
    .. attribute:: language
    
    	Name of language locale
    	**type**\:  :py:class:`LocaleLanguage <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_infra_locale_cfg.LocaleLanguage>`
    
    

    """

    _prefix = 'infra-infra-locale-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(Locale, self).__init__()
        self._top_entity = None

        self.yang_name = "locale"
        self.yang_parent_name = "Cisco-IOS-XR-infra-infra-locale-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict([
            ('country', (YLeaf(YType.enumeration, 'country'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_infra_locale_cfg', 'LocaleCountry', '')])),
            ('language', (YLeaf(YType.enumeration, 'language'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_infra_locale_cfg', 'LocaleLanguage', '')])),
        ])
        self.country = None
        self.language = None
        self._segment_path = lambda: "Cisco-IOS-XR-infra-infra-locale-cfg:locale"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Locale, ['country', 'language'], name, value)

    def clone_ptr(self):
        self._top_entity = Locale()
        return self._top_entity

