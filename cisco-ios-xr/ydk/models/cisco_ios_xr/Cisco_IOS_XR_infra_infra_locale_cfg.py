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

    .. data:: AD = 1

    	Andorra

    .. data:: AE = 2

    	United Arab Emirates

    .. data:: AF = 3

    	Afghanistan

    .. data:: AG = 4

    	Antigua and Barbuda

    .. data:: AI = 5

    	Anguilla

    .. data:: AL = 6

    	Albania

    .. data:: AM = 7

    	Armenia

    .. data:: AN = 8

    	Netherlands Antilles

    .. data:: AO = 9

    	Angola

    .. data:: AQ = 10

    	Antarctica

    .. data:: AR = 11

    	Argentina

    .. data:: AS = 12

    	American Samoa

    .. data:: AT = 13

    	Austria

    .. data:: AU = 14

    	Australia

    .. data:: AW = 15

    	Aruba

    .. data:: AZ = 16

    	Azerbaijan

    .. data:: BA = 17

    	Bosnia and Herzegovina

    .. data:: BB = 18

    	Barbados

    .. data:: BD = 19

    	Bangladesh

    .. data:: BE = 20

    	Belgium

    .. data:: BF = 21

    	Burkina Faso

    .. data:: BG = 22

    	Bulgaria

    .. data:: BH = 23

    	Bahrain

    .. data:: BI = 24

    	Burundi

    .. data:: BJ = 25

    	Benin

    .. data:: BM = 26

    	Bermuda

    .. data:: BN = 27

    	Brunei Darussalam

    .. data:: BO = 28

    	Bolivia

    .. data:: BR = 29

    	Brazil

    .. data:: BS = 30

    	Bahamas

    .. data:: BT = 31

    	Bhutan

    .. data:: BV = 32

    	Bouvet Island

    .. data:: BW = 33

    	Botswana

    .. data:: BY = 34

    	Belarus

    .. data:: BZ = 35

    	Belize

    .. data:: CA = 36

    	Canada

    .. data:: CC = 37

    	Cocos (Keeling) Islands

    .. data:: CD = 38

    	Congo, The Democratic Republic of the (Zaire)

    .. data:: CF = 39

    	Central African Republic

    .. data:: CG = 40

    	Congo

    .. data:: CH = 41

    	Switzerland

    .. data:: CI = 42

    	Cote D'Ivoire

    .. data:: CK = 43

    	Cook Islands

    .. data:: CL = 44

    	Chile

    .. data:: CM = 45

    	Cameroon

    .. data:: CN = 46

    	China

    .. data:: CO = 47

    	Colombia

    .. data:: CR = 48

    	Costa Rica

    .. data:: CU = 49

    	Cuba

    .. data:: CV = 50

    	Cape Verde

    .. data:: CX = 51

    	Christmas Island

    .. data:: CY = 52

    	Cyprus

    .. data:: CZ = 53

    	Czech Republic

    .. data:: DE = 54

    	Germany

    .. data:: DJ = 55

    	Djibouti

    .. data:: DK = 56

    	Denmark

    .. data:: DM = 57

    	Dominica

    .. data:: DO = 58

    	Dominican Republic

    .. data:: DZ = 59

    	Algeria

    .. data:: EC = 60

    	Ecuador

    .. data:: EE = 61

    	Estonia

    .. data:: EG = 62

    	Egypt

    .. data:: EH = 63

    	Western Sahara

    .. data:: ER = 64

    	Eritrea

    .. data:: ES = 65

    	Spain

    .. data:: ET = 66

    	Ethiopia

    .. data:: FI = 67

    	Finland

    .. data:: FJ = 68

    	Fiji

    .. data:: FK = 69

    	Falkland Islands (Malvinas)

    .. data:: FM = 70

    	Micronesia, Federated States of

    .. data:: FO = 71

    	Faroe Islands

    .. data:: FR = 72

    	France

    .. data:: GA = 73

    	Gabon

    .. data:: GB = 74

    	United Kingdom

    .. data:: GD = 75

    	Grenada

    .. data:: GE = 76

    	Georgia

    .. data:: GF = 77

    	French Guiana

    .. data:: GH = 78

    	Ghana

    .. data:: GI = 79

    	Gibraltar

    .. data:: GL = 80

    	Greenland

    .. data:: GM = 81

    	Gambia

    .. data:: GN = 82

    	Guinea

    .. data:: GP = 83

    	Guadeloupe

    .. data:: GQ = 84

    	Equatorial Guinea

    .. data:: GR = 85

    	Greece

    .. data:: GS = 86

    	South Georgia and the South Sandwich Islands

    .. data:: GT = 87

    	Guatemala

    .. data:: GU = 88

    	Guam

    .. data:: GW = 89

    	Guinea Bissau

    .. data:: GY = 90

    	Guyana

    .. data:: HK = 91

    	Hong Kong

    .. data:: HM = 92

    	Heard Island and McDonald Islands

    .. data:: HN = 93

    	Honduras

    .. data:: HR = 94

    	Croatia

    .. data:: HT = 95

    	Haiti

    .. data:: HU = 96

    	Hungary

    .. data:: ID = 97

    	Indonesia

    .. data:: IE = 98

    	Ireland

    .. data:: IL = 99

    	Israel

    .. data:: IN = 100

    	India

    .. data:: IO = 101

    	British Indian Ocean Territory

    .. data:: IQ = 102

    	Iraq

    .. data:: IR = 103

    	Iran, Islamic Republic of

    .. data:: IS = 104

    	Iceland

    .. data:: IT = 105

    	Italy

    .. data:: JM = 106

    	Jamaica

    .. data:: JO = 107

    	Jordan

    .. data:: JP = 108

    	Japan

    .. data:: KE = 109

    	Kenya

    .. data:: KG = 110

    	Kyrgyzstan

    .. data:: KH = 111

    	Cambodia

    .. data:: KI = 112

    	Kiribati

    .. data:: KM = 113

    	Comoros

    .. data:: KN = 114

    	Saint Kitts and Nevis

    .. data:: KP = 115

    	Korea, Democratic People's Republic of

    .. data:: KR = 116

    	Korea, Republic of

    .. data:: KW = 117

    	Kuwait

    .. data:: KY = 118

    	Cayman Islands

    .. data:: KZ = 119

    	Kazakstan

    .. data:: LA = 120

    	Lao People's Democratic Republic

    .. data:: LB = 121

    	Lebanon

    .. data:: LC = 122

    	Saint Lucia

    .. data:: LI = 123

    	Liechtenstein

    .. data:: LK = 124

    	Sri Lanka

    .. data:: LR = 125

    	Liberia

    .. data:: LS = 126

    	Lesotho

    .. data:: LT = 127

    	Lithuania

    .. data:: LU = 128

    	Luxembourg

    .. data:: LV = 129

    	Latvia

    .. data:: LY = 130

    	Libyan Arab Jamahiriya

    .. data:: MA = 131

    	Morocco

    .. data:: MC = 132

    	Monaco

    .. data:: MD = 133

    	Moldova, Republic of

    .. data:: MG = 134

    	Madagascar

    .. data:: MH = 135

    	Marshall Islands

    .. data:: MK = 136

    	Macedonia, The Former Yugoslav Republic of

    .. data:: ML = 137

    	Mali

    .. data:: MM = 138

    	Myanmar

    .. data:: MN = 139

    	Mongolia

    .. data:: MO = 140

    	Macau

    .. data:: MP = 141

    	Northern Mariana Islands

    .. data:: MQ = 142

    	Martinique

    .. data:: MR = 143

    	Mauritania

    .. data:: MS = 144

    	Montserrat

    .. data:: MT = 145

    	Malta

    .. data:: MU = 146

    	Mauritius

    .. data:: MV = 147

    	Maldives

    .. data:: MW = 148

    	Malawi

    .. data:: MX = 149

    	Mexico

    .. data:: MY = 150

    	Malaysia

    .. data:: MZ = 151

    	Mozambique

    .. data:: NA = 152

    	Namibia

    .. data:: NC = 153

    	New Caledonia

    .. data:: NE = 154

    	Niger

    .. data:: NF = 155

    	Norfolk Island

    .. data:: NG = 156

    	Nigeria

    .. data:: NI = 157

    	Nicaragua

    .. data:: NL = 158

    	Netherlands

    .. data:: NO = 159

    	Norway

    .. data:: NP = 160

    	Nepal

    .. data:: NR = 161

    	Nauru

    .. data:: NU = 162

    	Niue

    .. data:: NZ = 163

    	New Zealand

    .. data:: OM = 164

    	Oman

    .. data:: PA = 165

    	Panama

    .. data:: PE = 166

    	Peru

    .. data:: PF = 167

    	French Polynesia

    .. data:: PG = 168

    	Papua New Guinea

    .. data:: PH = 169

    	Philippines

    .. data:: PK = 170

    	Pakistan

    .. data:: PL = 171

    	Poland

    .. data:: PM = 172

    	Saint Pierre and Miquelon

    .. data:: PN = 173

    	Pitcairn

    .. data:: PR = 174

    	Puerto Rico

    .. data:: PT = 175

    	Portugal

    .. data:: PW = 176

    	Palau

    .. data:: PY = 177

    	Paraguay

    .. data:: QA = 178

    	Qatar

    .. data:: RE = 179

    	Reunion

    .. data:: RO = 180

    	Romania

    .. data:: RU = 181

    	Russian Federation

    .. data:: RW = 182

    	Rwanda

    .. data:: SA = 183

    	Saudi Arabia

    .. data:: SB = 184

    	Solomon Islands

    .. data:: SC = 185

    	Seychelles

    .. data:: SD = 186

    	Sudan

    .. data:: SE = 187

    	Sweden

    .. data:: SG = 188

    	Singapore

    .. data:: SH = 189

    	Saint Helena

    .. data:: SI = 190

    	Slovenia

    .. data:: SJ = 191

    	Svalbard and Jan Mayen

    .. data:: SK = 192

    	Slovakia

    .. data:: SL = 193

    	Sierra Leone

    .. data:: SM = 194

    	San Marino

    .. data:: SN = 195

    	Senegal

    .. data:: SO = 196

    	Somalia

    .. data:: SR = 197

    	Suriname

    .. data:: ST = 198

    	Sao Tome and Principe

    .. data:: SV = 199

    	El Salvador

    .. data:: SY = 200

    	Syrian Arab Republic

    .. data:: SZ = 201

    	Swaziland

    .. data:: TC = 202

    	Turks and Caicos Islands

    .. data:: TD = 203

    	Chad

    .. data:: TF = 204

    	French Southern Territories

    .. data:: TG = 205

    	Togo

    .. data:: TH = 206

    	Thailand

    .. data:: TJ = 207

    	Tajikistan

    .. data:: TK = 208

    	Tokelau

    .. data:: TM = 209

    	Turkmenistan

    .. data:: TN = 210

    	Tunisia

    .. data:: TO = 211

    	Tonga

    .. data:: TP = 212

    	East Timor

    .. data:: TR = 213

    	Turkey

    .. data:: TT = 214

    	Trinidad and Tobago

    .. data:: TV = 215

    	Tuvalu

    .. data:: TW = 216

    	Taiwan, Province of China

    .. data:: TZ = 217

    	Tanzania, United Republic of

    .. data:: UA = 218

    	Ukraine

    .. data:: UG = 219

    	Uganda

    .. data:: UM = 220

    	United States Minor Outlying Islands

    .. data:: US = 221

    	United States

    .. data:: UY = 222

    	Uruguay

    .. data:: UZ = 223

    	Uzbekistan

    .. data:: VA = 224

    	Holy See (Vatican City State)

    .. data:: VC = 225

    	Saint Vincent and The Grenadines

    .. data:: VE = 226

    	Venezuela

    .. data:: VG = 227

    	Virgin Islands, British

    .. data:: VI = 228

    	Virgin Islands, U.S.

    .. data:: VN = 229

    	Vietnam

    .. data:: VU = 230

    	Vanuatu

    .. data:: WF = 231

    	Wallis and Futuna

    .. data:: WS = 232

    	Samoa

    .. data:: YE = 233

    	Yemen

    .. data:: YT = 234

    	Mayotte

    .. data:: YU = 235

    	Yugoslavia

    .. data:: ZA = 236

    	South Africa

    .. data:: ZM = 237

    	Zambia

    .. data:: ZW = 238

    	Zimbabwe

    """

    AD = 1

    AE = 2

    AF = 3

    AG = 4

    AI = 5

    AL = 6

    AM = 7

    AN = 8

    AO = 9

    AQ = 10

    AR = 11

    AS = 12

    AT = 13

    AU = 14

    AW = 15

    AZ = 16

    BA = 17

    BB = 18

    BD = 19

    BE = 20

    BF = 21

    BG = 22

    BH = 23

    BI = 24

    BJ = 25

    BM = 26

    BN = 27

    BO = 28

    BR = 29

    BS = 30

    BT = 31

    BV = 32

    BW = 33

    BY = 34

    BZ = 35

    CA = 36

    CC = 37

    CD = 38

    CF = 39

    CG = 40

    CH = 41

    CI = 42

    CK = 43

    CL = 44

    CM = 45

    CN = 46

    CO = 47

    CR = 48

    CU = 49

    CV = 50

    CX = 51

    CY = 52

    CZ = 53

    DE = 54

    DJ = 55

    DK = 56

    DM = 57

    DO = 58

    DZ = 59

    EC = 60

    EE = 61

    EG = 62

    EH = 63

    ER = 64

    ES = 65

    ET = 66

    FI = 67

    FJ = 68

    FK = 69

    FM = 70

    FO = 71

    FR = 72

    GA = 73

    GB = 74

    GD = 75

    GE = 76

    GF = 77

    GH = 78

    GI = 79

    GL = 80

    GM = 81

    GN = 82

    GP = 83

    GQ = 84

    GR = 85

    GS = 86

    GT = 87

    GU = 88

    GW = 89

    GY = 90

    HK = 91

    HM = 92

    HN = 93

    HR = 94

    HT = 95

    HU = 96

    ID = 97

    IE = 98

    IL = 99

    IN = 100

    IO = 101

    IQ = 102

    IR = 103

    IS = 104

    IT = 105

    JM = 106

    JO = 107

    JP = 108

    KE = 109

    KG = 110

    KH = 111

    KI = 112

    KM = 113

    KN = 114

    KP = 115

    KR = 116

    KW = 117

    KY = 118

    KZ = 119

    LA = 120

    LB = 121

    LC = 122

    LI = 123

    LK = 124

    LR = 125

    LS = 126

    LT = 127

    LU = 128

    LV = 129

    LY = 130

    MA = 131

    MC = 132

    MD = 133

    MG = 134

    MH = 135

    MK = 136

    ML = 137

    MM = 138

    MN = 139

    MO = 140

    MP = 141

    MQ = 142

    MR = 143

    MS = 144

    MT = 145

    MU = 146

    MV = 147

    MW = 148

    MX = 149

    MY = 150

    MZ = 151

    NA = 152

    NC = 153

    NE = 154

    NF = 155

    NG = 156

    NI = 157

    NL = 158

    NO = 159

    NP = 160

    NR = 161

    NU = 162

    NZ = 163

    OM = 164

    PA = 165

    PE = 166

    PF = 167

    PG = 168

    PH = 169

    PK = 170

    PL = 171

    PM = 172

    PN = 173

    PR = 174

    PT = 175

    PW = 176

    PY = 177

    QA = 178

    RE = 179

    RO = 180

    RU = 181

    RW = 182

    SA = 183

    SB = 184

    SC = 185

    SD = 186

    SE = 187

    SG = 188

    SH = 189

    SI = 190

    SJ = 191

    SK = 192

    SL = 193

    SM = 194

    SN = 195

    SO = 196

    SR = 197

    ST = 198

    SV = 199

    SY = 200

    SZ = 201

    TC = 202

    TD = 203

    TF = 204

    TG = 205

    TH = 206

    TJ = 207

    TK = 208

    TM = 209

    TN = 210

    TO = 211

    TP = 212

    TR = 213

    TT = 214

    TV = 215

    TW = 216

    TZ = 217

    UA = 218

    UG = 219

    UM = 220

    US = 221

    UY = 222

    UZ = 223

    VA = 224

    VC = 225

    VE = 226

    VG = 227

    VI = 228

    VN = 229

    VU = 230

    WF = 231

    WS = 232

    YE = 233

    YT = 234

    YU = 235

    ZA = 236

    ZM = 237

    ZW = 238


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_infra_locale_cfg as meta
        return meta._meta_table['LocaleCountryEnum']


class LocaleLanguageEnum(Enum):
    """
    LocaleLanguageEnum

    Locale language

    .. data:: AA = 1

    	Afar

    .. data:: AB = 2

    	Abkhazian

    .. data:: AF = 3

    	Afrikaans

    .. data:: AM = 4

    	Amharic

    .. data:: AR = 5

    	Arabic

    .. data:: AS = 6

    	Assamese

    .. data:: AY = 7

    	Aymara

    .. data:: AZ = 8

    	Azerbaijani

    .. data:: BA = 9

    	Bashkir

    .. data:: BE = 10

    	Byelorussian

    .. data:: BG = 11

    	Bulgarian

    .. data:: BH = 12

    	Bihari

    .. data:: BI = 13

    	Bislama

    .. data:: BN = 14

    	Bengali

    .. data:: BO = 15

    	Tibetan

    .. data:: BR = 16

    	Breton

    .. data:: CA = 17

    	Catalan

    .. data:: CO = 18

    	Corsican

    .. data:: CS = 19

    	Czech

    .. data:: CY = 20

    	Welsh

    .. data:: DA = 21

    	Danish

    .. data:: DE = 22

    	German

    .. data:: DZ = 23

    	Bhutani

    .. data:: EL = 24

    	Greek

    .. data:: EN = 25

    	English

    .. data:: EO = 26

    	Esperanto

    .. data:: ES = 27

    	Spanish

    .. data:: ET = 28

    	Estonian

    .. data:: EU = 29

    	Basque

    .. data:: FA = 30

    	Persian

    .. data:: FI = 31

    	Finnish

    .. data:: FJ = 32

    	Fiji

    .. data:: FO = 33

    	Faroese

    .. data:: FR = 34

    	French

    .. data:: FY = 35

    	Frisian

    .. data:: GA = 36

    	Irish

    .. data:: GD = 37

    	Scots Gaelic

    .. data:: GL = 38

    	Galician

    .. data:: GN = 39

    	Guarani

    .. data:: GU = 40

    	Gujarati

    .. data:: HA = 41

    	Hausa

    .. data:: HE = 42

    	Hebrew

    .. data:: HI = 43

    	Hindi

    .. data:: HR = 44

    	Croatian

    .. data:: HU = 45

    	Hungarian

    .. data:: HY = 46

    	Armenian

    .. data:: IA = 47

    	Interlingua

    .. data:: ID = 48

    	Indonesian

    .. data:: IE = 49

    	Interlingue

    .. data:: IK = 50

    	Inupiak

    .. data:: IS = 51

    	Icelandic

    .. data:: IT = 52

    	Italian

    .. data:: IU = 53

    	Inuktitut

    .. data:: JA = 54

    	Japanese

    .. data:: JW = 55

    	Javanese

    .. data:: KA = 56

    	Georgian

    .. data:: KK = 57

    	Kazakh

    .. data:: KL = 58

    	Greenlandic

    .. data:: KM = 59

    	Cambodian

    .. data:: KN = 60

    	Kannada

    .. data:: KO = 61

    	Korean

    .. data:: KS = 62

    	Kashmiri

    .. data:: KU = 63

    	Kurdish

    .. data:: KY = 64

    	Kirghiz

    .. data:: LA = 65

    	Latin

    .. data:: LN = 66

    	Lingala

    .. data:: LO = 67

    	Laothian

    .. data:: LT = 68

    	Lithuanian

    .. data:: LV = 69

    	Latvian, Lettish

    .. data:: MG = 70

    	Malagasy

    .. data:: MI = 71

    	Maori

    .. data:: MK = 72

    	Macedonian

    .. data:: ML = 73

    	Malayalam

    .. data:: MN = 74

    	Mongolian

    .. data:: MO = 75

    	Moldavian

    .. data:: MR = 76

    	Marathi

    .. data:: MS = 77

    	Malay

    .. data:: MT = 78

    	Maltese

    .. data:: MY = 79

    	Burmese

    .. data:: NA = 80

    	Nauru

    .. data:: NE = 81

    	Nepali

    .. data:: NL = 82

    	Dutch

    .. data:: NO = 83

    	Norwegian

    .. data:: OC = 84

    	Occitan

    .. data:: OM = 85

    	(Afan) Oromo

    .. data:: OR = 86

    	Oriya

    .. data:: PA = 87

    	Punjabi

    .. data:: PL = 88

    	Polish

    .. data:: PS = 89

    	Pashto, Pushto

    .. data:: PT = 90

    	Portuguese

    .. data:: QU = 91

    	Quechua

    .. data:: RM = 92

    	Rhaeto Romance

    .. data:: RN = 93

    	Kirundi

    .. data:: RO = 94

    	Romanian

    .. data:: RU = 95

    	Russian

    .. data:: RW = 96

    	Kinyarwanda

    .. data:: SA = 97

    	Sanskrit

    .. data:: SD = 98

    	Sindhi

    .. data:: SG = 99

    	Sangho

    .. data:: SH = 100

    	Serbo Croatian

    .. data:: SI = 101

    	Sinhalese

    .. data:: SK = 102

    	Slovak

    .. data:: SL = 103

    	Slovenian

    .. data:: SM = 104

    	Samoan

    .. data:: SN = 105

    	Shona

    .. data:: SO = 106

    	Somali

    .. data:: SQ = 107

    	Albanian

    .. data:: SR = 108

    	Serbian

    .. data:: SS = 109

    	Siswati

    .. data:: ST = 110

    	Sesotho

    .. data:: SU = 111

    	Sundanese

    .. data:: SV = 112

    	Swedish

    .. data:: SW = 113

    	Swahili

    .. data:: TA = 114

    	Tamil

    .. data:: TE = 115

    	Telugu

    .. data:: TG = 116

    	Tajik

    .. data:: TH = 117

    	Thai

    .. data:: TI = 118

    	Tigrinya

    .. data:: TK = 119

    	Turkmen

    .. data:: TL = 120

    	Tagalog

    .. data:: TN = 121

    	Setswana

    .. data:: TO = 122

    	Tonga

    .. data:: TR = 123

    	Turkish

    .. data:: TS = 124

    	Tsonga

    .. data:: TT = 125

    	Tatar

    .. data:: TW = 126

    	Twi

    .. data:: UG = 127

    	Uighur

    .. data:: UK = 128

    	Ukrainian

    .. data:: UR = 129

    	Urdu

    .. data:: UZ = 130

    	Uzbek

    .. data:: VI = 131

    	Vietnamese

    .. data:: VO = 132

    	Volapuk

    .. data:: WO = 133

    	Wolof

    .. data:: XH = 134

    	Xhosa

    .. data:: YI = 135

    	Yiddish

    .. data:: YO = 136

    	Yoruba

    .. data:: ZA = 137

    	Zhuang

    .. data:: ZH = 138

    	Chinese

    .. data:: ZU = 139

    	Zulu

    """

    AA = 1

    AB = 2

    AF = 3

    AM = 4

    AR = 5

    AS = 6

    AY = 7

    AZ = 8

    BA = 9

    BE = 10

    BG = 11

    BH = 12

    BI = 13

    BN = 14

    BO = 15

    BR = 16

    CA = 17

    CO = 18

    CS = 19

    CY = 20

    DA = 21

    DE = 22

    DZ = 23

    EL = 24

    EN = 25

    EO = 26

    ES = 27

    ET = 28

    EU = 29

    FA = 30

    FI = 31

    FJ = 32

    FO = 33

    FR = 34

    FY = 35

    GA = 36

    GD = 37

    GL = 38

    GN = 39

    GU = 40

    HA = 41

    HE = 42

    HI = 43

    HR = 44

    HU = 45

    HY = 46

    IA = 47

    ID = 48

    IE = 49

    IK = 50

    IS = 51

    IT = 52

    IU = 53

    JA = 54

    JW = 55

    KA = 56

    KK = 57

    KL = 58

    KM = 59

    KN = 60

    KO = 61

    KS = 62

    KU = 63

    KY = 64

    LA = 65

    LN = 66

    LO = 67

    LT = 68

    LV = 69

    MG = 70

    MI = 71

    MK = 72

    ML = 73

    MN = 74

    MO = 75

    MR = 76

    MS = 77

    MT = 78

    MY = 79

    NA = 80

    NE = 81

    NL = 82

    NO = 83

    OC = 84

    OM = 85

    OR = 86

    PA = 87

    PL = 88

    PS = 89

    PT = 90

    QU = 91

    RM = 92

    RN = 93

    RO = 94

    RU = 95

    RW = 96

    SA = 97

    SD = 98

    SG = 99

    SH = 100

    SI = 101

    SK = 102

    SL = 103

    SM = 104

    SN = 105

    SO = 106

    SQ = 107

    SR = 108

    SS = 109

    ST = 110

    SU = 111

    SV = 112

    SW = 113

    TA = 114

    TE = 115

    TG = 116

    TH = 117

    TI = 118

    TK = 119

    TL = 120

    TN = 121

    TO = 122

    TR = 123

    TS = 124

    TT = 125

    TW = 126

    UG = 127

    UK = 128

    UR = 129

    UZ = 130

    VI = 131

    VO = 132

    WO = 133

    XH = 134

    YI = 135

    YO = 136

    ZA = 137

    ZH = 138

    ZU = 139


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_infra_locale_cfg as meta
        return meta._meta_table['LocaleLanguageEnum']



class Locale(object):
    """
    Define the geographical locale
    
    .. attribute:: country
    
    	Name of country locale
    	**type**\:  :py:class:`LocaleCountryEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_infra_locale_cfg.LocaleCountryEnum>`
    
    .. attribute:: language
    
    	Name of language locale
    	**type**\:  :py:class:`LocaleLanguageEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_infra_locale_cfg.LocaleLanguageEnum>`
    
    

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
        if not self.is_config():
            return False
        if self.country is not None:
            return True

        if self.language is not None:
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_infra_locale_cfg as meta
        return meta._meta_table['Locale']['meta_info']


