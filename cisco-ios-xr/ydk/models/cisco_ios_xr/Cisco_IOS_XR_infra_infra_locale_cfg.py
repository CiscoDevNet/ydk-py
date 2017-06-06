""" Cisco_IOS_XR_infra_infra_locale_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-infra\-locale package configuration.

This module contains definitions
for the following management objects\:
  locale\: Define the geographical locale

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class LocaleCountryEnum(Enum):
    """
    LocaleCountryEnum

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

    ad = 1

    ae = 2

    af = 3

    ag = 4

    ai = 5

    al = 6

    am = 7

    an = 8

    ao = 9

    aq = 10

    ar = 11

    as_ = 12

    at = 13

    au = 14

    aw = 15

    az = 16

    ba = 17

    bb = 18

    bd = 19

    be = 20

    bf = 21

    bg = 22

    bh = 23

    bi = 24

    bj = 25

    bm = 26

    bn = 27

    bo = 28

    br = 29

    bs = 30

    bt = 31

    bv = 32

    bw = 33

    by = 34

    bz = 35

    ca = 36

    cc = 37

    cd = 38

    cf = 39

    cg = 40

    ch = 41

    ci = 42

    ck = 43

    cl = 44

    cm = 45

    cn = 46

    co = 47

    cr = 48

    cu = 49

    cv = 50

    cx = 51

    cy = 52

    cz = 53

    de = 54

    dj = 55

    dk = 56

    dm = 57

    do = 58

    dz = 59

    ec = 60

    ee = 61

    eg = 62

    eh = 63

    er = 64

    es = 65

    et = 66

    fi = 67

    fj = 68

    fk = 69

    fm = 70

    fo = 71

    fr = 72

    ga = 73

    gb = 74

    gd = 75

    ge = 76

    gf = 77

    gh = 78

    gi = 79

    gl = 80

    gm = 81

    gn = 82

    gp = 83

    gq = 84

    gr = 85

    gs = 86

    gt = 87

    gu = 88

    gw = 89

    gy = 90

    hk = 91

    hm = 92

    hn = 93

    hr = 94

    ht = 95

    hu = 96

    id = 97

    ie = 98

    il = 99

    in_ = 100

    io = 101

    iq = 102

    ir = 103

    is_ = 104

    it = 105

    jm = 106

    jo = 107

    jp = 108

    ke = 109

    kg = 110

    kh = 111

    ki = 112

    km = 113

    kn = 114

    kp = 115

    kr = 116

    kw = 117

    ky = 118

    kz = 119

    la = 120

    lb = 121

    lc = 122

    li = 123

    lk = 124

    lr = 125

    ls = 126

    lt = 127

    lu = 128

    lv = 129

    ly = 130

    ma = 131

    mc = 132

    md = 133

    mg = 134

    mh = 135

    mk = 136

    ml = 137

    mm = 138

    mn = 139

    mo = 140

    mp = 141

    mq = 142

    mr = 143

    ms = 144

    mt = 145

    mu = 146

    mv = 147

    mw = 148

    mx = 149

    my = 150

    mz = 151

    na = 152

    nc = 153

    ne = 154

    nf = 155

    ng = 156

    ni = 157

    nl = 158

    no = 159

    np = 160

    nr = 161

    nu = 162

    nz = 163

    om = 164

    pa = 165

    pe = 166

    pf = 167

    pg = 168

    ph = 169

    pk = 170

    pl = 171

    pm = 172

    pn = 173

    pr = 174

    pt = 175

    pw = 176

    py = 177

    qa = 178

    re = 179

    ro = 180

    ru = 181

    rw = 182

    sa = 183

    sb = 184

    sc = 185

    sd = 186

    se = 187

    sg = 188

    sh = 189

    si = 190

    sj = 191

    sk = 192

    sl = 193

    sm = 194

    sn = 195

    so = 196

    sr = 197

    st = 198

    sv = 199

    sy = 200

    sz = 201

    tc = 202

    td = 203

    tf = 204

    tg = 205

    th = 206

    tj = 207

    tk = 208

    tm = 209

    tn = 210

    to = 211

    tp = 212

    tr = 213

    tt = 214

    tv = 215

    tw = 216

    tz = 217

    ua = 218

    ug = 219

    um = 220

    us = 221

    uy = 222

    uz = 223

    va = 224

    vc = 225

    ve = 226

    vg = 227

    vi = 228

    vn = 229

    vu = 230

    wf = 231

    ws = 232

    ye = 233

    yt = 234

    yu = 235

    za = 236

    zm = 237

    zw = 238


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_infra_locale_cfg as meta
        return meta._meta_table['LocaleCountryEnum']


class LocaleLanguageEnum(Enum):
    """
    LocaleLanguageEnum

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

    aa = 1

    ab = 2

    af = 3

    am = 4

    ar = 5

    as_ = 6

    ay = 7

    az = 8

    ba = 9

    be = 10

    bg = 11

    bh = 12

    bi = 13

    bn = 14

    bo = 15

    br = 16

    ca = 17

    co = 18

    cs = 19

    cy = 20

    da = 21

    de = 22

    dz = 23

    el = 24

    en = 25

    eo = 26

    es = 27

    et = 28

    eu = 29

    fa = 30

    fi = 31

    fj = 32

    fo = 33

    fr = 34

    fy = 35

    ga = 36

    gd = 37

    gl = 38

    gn = 39

    gu = 40

    ha = 41

    he = 42

    hi = 43

    hr = 44

    hu = 45

    hy = 46

    ia = 47

    id = 48

    ie = 49

    ik = 50

    is_ = 51

    it = 52

    iu = 53

    ja = 54

    jw = 55

    ka = 56

    kk = 57

    kl = 58

    km = 59

    kn = 60

    ko = 61

    ks = 62

    ku = 63

    ky = 64

    la = 65

    ln = 66

    lo = 67

    lt = 68

    lv = 69

    mg = 70

    mi = 71

    mk = 72

    ml = 73

    mn = 74

    mo = 75

    mr = 76

    ms = 77

    mt = 78

    my = 79

    na = 80

    ne = 81

    nl = 82

    no = 83

    oc = 84

    om = 85

    or_ = 86

    pa = 87

    pl = 88

    ps = 89

    pt = 90

    qu = 91

    rm = 92

    rn = 93

    ro = 94

    ru = 95

    rw = 96

    sa = 97

    sd = 98

    sg = 99

    sh = 100

    si = 101

    sk = 102

    sl = 103

    sm = 104

    sn = 105

    so = 106

    sq = 107

    sr = 108

    ss = 109

    st = 110

    su = 111

    sv = 112

    sw = 113

    ta = 114

    te = 115

    tg = 116

    th = 117

    ti = 118

    tk = 119

    tl = 120

    tn = 121

    to = 122

    tr = 123

    ts = 124

    tt = 125

    tw = 126

    ug = 127

    uk = 128

    ur = 129

    uz = 130

    vi = 131

    vo = 132

    wo = 133

    xh = 134

    yi = 135

    yo = 136

    za = 137

    zh = 138

    zu = 139


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_infra_locale_cfg as meta
        return meta._meta_table['LocaleLanguageEnum']



class Locale(object):
    """
    Define the geographical locale
    
    .. attribute:: country
    
    	Name of country locale
    	**type**\:   :py:class:`LocaleCountryEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_infra_locale_cfg.LocaleCountryEnum>`
    
    .. attribute:: language
    
    	Name of language locale
    	**type**\:   :py:class:`LocaleLanguageEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_infra_locale_cfg.LocaleLanguageEnum>`
    
    

    """

    _prefix = 'infra-infra-locale-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.country = None
        self.language = None

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-infra-infra-locale-cfg:locale'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.country is not None:
            return True

        if self.language is not None:
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_infra_locale_cfg as meta
        return meta._meta_table['Locale']['meta_info']


