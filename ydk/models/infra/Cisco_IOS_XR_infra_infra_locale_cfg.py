""" Cisco_IOS_XR_infra_infra_locale_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-infra\-locale package configuration.

This module contains definitions
for the following management objects\:
  locale\: Define the geographical locale

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class LocaleCountry_Enum(Enum):
    """
    LocaleCountry_Enum

    Locale country

    """

    """

    Andorra

    """
    AD = 1

    """

    United Arab Emirates

    """
    AE = 2

    """

    Afghanistan

    """
    AF = 3

    """

    Antigua and Barbuda

    """
    AG = 4

    """

    Anguilla

    """
    AI = 5

    """

    Albania

    """
    AL = 6

    """

    Armenia

    """
    AM = 7

    """

    Netherlands Antilles

    """
    AN = 8

    """

    Angola

    """
    AO = 9

    """

    Antarctica

    """
    AQ = 10

    """

    Argentina

    """
    AR = 11

    """

    American Samoa

    """
    AS = 12

    """

    Austria

    """
    AT = 13

    """

    Australia

    """
    AU = 14

    """

    Aruba

    """
    AW = 15

    """

    Azerbaijan

    """
    AZ = 16

    """

    Bosnia and Herzegovina

    """
    BA = 17

    """

    Barbados

    """
    BB = 18

    """

    Bangladesh

    """
    BD = 19

    """

    Belgium

    """
    BE = 20

    """

    Burkina Faso

    """
    BF = 21

    """

    Bulgaria

    """
    BG = 22

    """

    Bahrain

    """
    BH = 23

    """

    Burundi

    """
    BI = 24

    """

    Benin

    """
    BJ = 25

    """

    Bermuda

    """
    BM = 26

    """

    Brunei Darussalam

    """
    BN = 27

    """

    Bolivia

    """
    BO = 28

    """

    Brazil

    """
    BR = 29

    """

    Bahamas

    """
    BS = 30

    """

    Bhutan

    """
    BT = 31

    """

    Bouvet Island

    """
    BV = 32

    """

    Botswana

    """
    BW = 33

    """

    Belarus

    """
    BY = 34

    """

    Belize

    """
    BZ = 35

    """

    Canada

    """
    CA = 36

    """

    Cocos (Keeling) Islands

    """
    CC = 37

    """

    Congo, The Democratic Republic of the (Zaire)

    """
    CD = 38

    """

    Central African Republic

    """
    CF = 39

    """

    Congo

    """
    CG = 40

    """

    Switzerland

    """
    CH = 41

    """

    Cote D'Ivoire

    """
    CI = 42

    """

    Cook Islands

    """
    CK = 43

    """

    Chile

    """
    CL = 44

    """

    Cameroon

    """
    CM = 45

    """

    China

    """
    CN = 46

    """

    Colombia

    """
    CO = 47

    """

    Costa Rica

    """
    CR = 48

    """

    Cuba

    """
    CU = 49

    """

    Cape Verde

    """
    CV = 50

    """

    Christmas Island

    """
    CX = 51

    """

    Cyprus

    """
    CY = 52

    """

    Czech Republic

    """
    CZ = 53

    """

    Germany

    """
    DE = 54

    """

    Djibouti

    """
    DJ = 55

    """

    Denmark

    """
    DK = 56

    """

    Dominica

    """
    DM = 57

    """

    Dominican Republic

    """
    DO = 58

    """

    Algeria

    """
    DZ = 59

    """

    Ecuador

    """
    EC = 60

    """

    Estonia

    """
    EE = 61

    """

    Egypt

    """
    EG = 62

    """

    Western Sahara

    """
    EH = 63

    """

    Eritrea

    """
    ER = 64

    """

    Spain

    """
    ES = 65

    """

    Ethiopia

    """
    ET = 66

    """

    Finland

    """
    FI = 67

    """

    Fiji

    """
    FJ = 68

    """

    Falkland Islands (Malvinas)

    """
    FK = 69

    """

    Micronesia, Federated States of

    """
    FM = 70

    """

    Faroe Islands

    """
    FO = 71

    """

    France

    """
    FR = 72

    """

    Gabon

    """
    GA = 73

    """

    United Kingdom

    """
    GB = 74

    """

    Grenada

    """
    GD = 75

    """

    Georgia

    """
    GE = 76

    """

    French Guiana

    """
    GF = 77

    """

    Ghana

    """
    GH = 78

    """

    Gibraltar

    """
    GI = 79

    """

    Greenland

    """
    GL = 80

    """

    Gambia

    """
    GM = 81

    """

    Guinea

    """
    GN = 82

    """

    Guadeloupe

    """
    GP = 83

    """

    Equatorial Guinea

    """
    GQ = 84

    """

    Greece

    """
    GR = 85

    """

    South Georgia and the South Sandwich Islands

    """
    GS = 86

    """

    Guatemala

    """
    GT = 87

    """

    Guam

    """
    GU = 88

    """

    Guinea Bissau

    """
    GW = 89

    """

    Guyana

    """
    GY = 90

    """

    Hong Kong

    """
    HK = 91

    """

    Heard Island and McDonald Islands

    """
    HM = 92

    """

    Honduras

    """
    HN = 93

    """

    Croatia

    """
    HR = 94

    """

    Haiti

    """
    HT = 95

    """

    Hungary

    """
    HU = 96

    """

    Indonesia

    """
    ID = 97

    """

    Ireland

    """
    IE = 98

    """

    Israel

    """
    IL = 99

    """

    India

    """
    IN = 100

    """

    British Indian Ocean Territory

    """
    IO = 101

    """

    Iraq

    """
    IQ = 102

    """

    Iran, Islamic Republic of

    """
    IR = 103

    """

    Iceland

    """
    IS = 104

    """

    Italy

    """
    IT = 105

    """

    Jamaica

    """
    JM = 106

    """

    Jordan

    """
    JO = 107

    """

    Japan

    """
    JP = 108

    """

    Kenya

    """
    KE = 109

    """

    Kyrgyzstan

    """
    KG = 110

    """

    Cambodia

    """
    KH = 111

    """

    Kiribati

    """
    KI = 112

    """

    Comoros

    """
    KM = 113

    """

    Saint Kitts and Nevis

    """
    KN = 114

    """

    Korea, Democratic People's Republic of

    """
    KP = 115

    """

    Korea, Republic of

    """
    KR = 116

    """

    Kuwait

    """
    KW = 117

    """

    Cayman Islands

    """
    KY = 118

    """

    Kazakstan

    """
    KZ = 119

    """

    Lao People's Democratic Republic

    """
    LA = 120

    """

    Lebanon

    """
    LB = 121

    """

    Saint Lucia

    """
    LC = 122

    """

    Liechtenstein

    """
    LI = 123

    """

    Sri Lanka

    """
    LK = 124

    """

    Liberia

    """
    LR = 125

    """

    Lesotho

    """
    LS = 126

    """

    Lithuania

    """
    LT = 127

    """

    Luxembourg

    """
    LU = 128

    """

    Latvia

    """
    LV = 129

    """

    Libyan Arab Jamahiriya

    """
    LY = 130

    """

    Morocco

    """
    MA = 131

    """

    Monaco

    """
    MC = 132

    """

    Moldova, Republic of

    """
    MD = 133

    """

    Madagascar

    """
    MG = 134

    """

    Marshall Islands

    """
    MH = 135

    """

    Macedonia, The Former Yugoslav Republic of

    """
    MK = 136

    """

    Mali

    """
    ML = 137

    """

    Myanmar

    """
    MM = 138

    """

    Mongolia

    """
    MN = 139

    """

    Macau

    """
    MO = 140

    """

    Northern Mariana Islands

    """
    MP = 141

    """

    Martinique

    """
    MQ = 142

    """

    Mauritania

    """
    MR = 143

    """

    Montserrat

    """
    MS = 144

    """

    Malta

    """
    MT = 145

    """

    Mauritius

    """
    MU = 146

    """

    Maldives

    """
    MV = 147

    """

    Malawi

    """
    MW = 148

    """

    Mexico

    """
    MX = 149

    """

    Malaysia

    """
    MY = 150

    """

    Mozambique

    """
    MZ = 151

    """

    Namibia

    """
    NA = 152

    """

    New Caledonia

    """
    NC = 153

    """

    Niger

    """
    NE = 154

    """

    Norfolk Island

    """
    NF = 155

    """

    Nigeria

    """
    NG = 156

    """

    Nicaragua

    """
    NI = 157

    """

    Netherlands

    """
    NL = 158

    """

    Norway

    """
    NO = 159

    """

    Nepal

    """
    NP = 160

    """

    Nauru

    """
    NR = 161

    """

    Niue

    """
    NU = 162

    """

    New Zealand

    """
    NZ = 163

    """

    Oman

    """
    OM = 164

    """

    Panama

    """
    PA = 165

    """

    Peru

    """
    PE = 166

    """

    French Polynesia

    """
    PF = 167

    """

    Papua New Guinea

    """
    PG = 168

    """

    Philippines

    """
    PH = 169

    """

    Pakistan

    """
    PK = 170

    """

    Poland

    """
    PL = 171

    """

    Saint Pierre and Miquelon

    """
    PM = 172

    """

    Pitcairn

    """
    PN = 173

    """

    Puerto Rico

    """
    PR = 174

    """

    Portugal

    """
    PT = 175

    """

    Palau

    """
    PW = 176

    """

    Paraguay

    """
    PY = 177

    """

    Qatar

    """
    QA = 178

    """

    Reunion

    """
    RE = 179

    """

    Romania

    """
    RO = 180

    """

    Russian Federation

    """
    RU = 181

    """

    Rwanda

    """
    RW = 182

    """

    Saudi Arabia

    """
    SA = 183

    """

    Solomon Islands

    """
    SB = 184

    """

    Seychelles

    """
    SC = 185

    """

    Sudan

    """
    SD = 186

    """

    Sweden

    """
    SE = 187

    """

    Singapore

    """
    SG = 188

    """

    Saint Helena

    """
    SH = 189

    """

    Slovenia

    """
    SI = 190

    """

    Svalbard and Jan Mayen

    """
    SJ = 191

    """

    Slovakia

    """
    SK = 192

    """

    Sierra Leone

    """
    SL = 193

    """

    San Marino

    """
    SM = 194

    """

    Senegal

    """
    SN = 195

    """

    Somalia

    """
    SO = 196

    """

    Suriname

    """
    SR = 197

    """

    Sao Tome and Principe

    """
    ST = 198

    """

    El Salvador

    """
    SV = 199

    """

    Syrian Arab Republic

    """
    SY = 200

    """

    Swaziland

    """
    SZ = 201

    """

    Turks and Caicos Islands

    """
    TC = 202

    """

    Chad

    """
    TD = 203

    """

    French Southern Territories

    """
    TF = 204

    """

    Togo

    """
    TG = 205

    """

    Thailand

    """
    TH = 206

    """

    Tajikistan

    """
    TJ = 207

    """

    Tokelau

    """
    TK = 208

    """

    Turkmenistan

    """
    TM = 209

    """

    Tunisia

    """
    TN = 210

    """

    Tonga

    """
    TO = 211

    """

    East Timor

    """
    TP = 212

    """

    Turkey

    """
    TR = 213

    """

    Trinidad and Tobago

    """
    TT = 214

    """

    Tuvalu

    """
    TV = 215

    """

    Taiwan, Province of China

    """
    TW = 216

    """

    Tanzania, United Republic of

    """
    TZ = 217

    """

    Ukraine

    """
    UA = 218

    """

    Uganda

    """
    UG = 219

    """

    United States Minor Outlying Islands

    """
    UM = 220

    """

    United States

    """
    US = 221

    """

    Uruguay

    """
    UY = 222

    """

    Uzbekistan

    """
    UZ = 223

    """

    Holy See (Vatican City State)

    """
    VA = 224

    """

    Saint Vincent and The Grenadines

    """
    VC = 225

    """

    Venezuela

    """
    VE = 226

    """

    Virgin Islands, British

    """
    VG = 227

    """

    Virgin Islands, U.S.

    """
    VI = 228

    """

    Vietnam

    """
    VN = 229

    """

    Vanuatu

    """
    VU = 230

    """

    Wallis and Futuna

    """
    WF = 231

    """

    Samoa

    """
    WS = 232

    """

    Yemen

    """
    YE = 233

    """

    Mayotte

    """
    YT = 234

    """

    Yugoslavia

    """
    YU = 235

    """

    South Africa

    """
    ZA = 236

    """

    Zambia

    """
    ZM = 237

    """

    Zimbabwe

    """
    ZW = 238


    @staticmethod
    def _meta_info():
        from ydk.models.infra._meta import _Cisco_IOS_XR_infra_infra_locale_cfg as meta
        return meta._meta_table['LocaleCountry_Enum']


class LocaleLanguage_Enum(Enum):
    """
    LocaleLanguage_Enum

    Locale language

    """

    """

    Afar

    """
    AA = 1

    """

    Abkhazian

    """
    AB = 2

    """

    Afrikaans

    """
    AF = 3

    """

    Amharic

    """
    AM = 4

    """

    Arabic

    """
    AR = 5

    """

    Assamese

    """
    AS = 6

    """

    Aymara

    """
    AY = 7

    """

    Azerbaijani

    """
    AZ = 8

    """

    Bashkir

    """
    BA = 9

    """

    Byelorussian

    """
    BE = 10

    """

    Bulgarian

    """
    BG = 11

    """

    Bihari

    """
    BH = 12

    """

    Bislama

    """
    BI = 13

    """

    Bengali

    """
    BN = 14

    """

    Tibetan

    """
    BO = 15

    """

    Breton

    """
    BR = 16

    """

    Catalan

    """
    CA = 17

    """

    Corsican

    """
    CO = 18

    """

    Czech

    """
    CS = 19

    """

    Welsh

    """
    CY = 20

    """

    Danish

    """
    DA = 21

    """

    German

    """
    DE = 22

    """

    Bhutani

    """
    DZ = 23

    """

    Greek

    """
    EL = 24

    """

    English

    """
    EN = 25

    """

    Esperanto

    """
    EO = 26

    """

    Spanish

    """
    ES = 27

    """

    Estonian

    """
    ET = 28

    """

    Basque

    """
    EU = 29

    """

    Persian

    """
    FA = 30

    """

    Finnish

    """
    FI = 31

    """

    Fiji

    """
    FJ = 32

    """

    Faroese

    """
    FO = 33

    """

    French

    """
    FR = 34

    """

    Frisian

    """
    FY = 35

    """

    Irish

    """
    GA = 36

    """

    Scots Gaelic

    """
    GD = 37

    """

    Galician

    """
    GL = 38

    """

    Guarani

    """
    GN = 39

    """

    Gujarati

    """
    GU = 40

    """

    Hausa

    """
    HA = 41

    """

    Hebrew

    """
    HE = 42

    """

    Hindi

    """
    HI = 43

    """

    Croatian

    """
    HR = 44

    """

    Hungarian

    """
    HU = 45

    """

    Armenian

    """
    HY = 46

    """

    Interlingua

    """
    IA = 47

    """

    Indonesian

    """
    ID = 48

    """

    Interlingue

    """
    IE = 49

    """

    Inupiak

    """
    IK = 50

    """

    Icelandic

    """
    IS = 51

    """

    Italian

    """
    IT = 52

    """

    Inuktitut

    """
    IU = 53

    """

    Japanese

    """
    JA = 54

    """

    Javanese

    """
    JW = 55

    """

    Georgian

    """
    KA = 56

    """

    Kazakh

    """
    KK = 57

    """

    Greenlandic

    """
    KL = 58

    """

    Cambodian

    """
    KM = 59

    """

    Kannada

    """
    KN = 60

    """

    Korean

    """
    KO = 61

    """

    Kashmiri

    """
    KS = 62

    """

    Kurdish

    """
    KU = 63

    """

    Kirghiz

    """
    KY = 64

    """

    Latin

    """
    LA = 65

    """

    Lingala

    """
    LN = 66

    """

    Laothian

    """
    LO = 67

    """

    Lithuanian

    """
    LT = 68

    """

    Latvian, Lettish

    """
    LV = 69

    """

    Malagasy

    """
    MG = 70

    """

    Maori

    """
    MI = 71

    """

    Macedonian

    """
    MK = 72

    """

    Malayalam

    """
    ML = 73

    """

    Mongolian

    """
    MN = 74

    """

    Moldavian

    """
    MO = 75

    """

    Marathi

    """
    MR = 76

    """

    Malay

    """
    MS = 77

    """

    Maltese

    """
    MT = 78

    """

    Burmese

    """
    MY = 79

    """

    Nauru

    """
    NA = 80

    """

    Nepali

    """
    NE = 81

    """

    Dutch

    """
    NL = 82

    """

    Norwegian

    """
    NO = 83

    """

    Occitan

    """
    OC = 84

    """

    (Afan) Oromo

    """
    OM = 85

    """

    Oriya

    """
    OR = 86

    """

    Punjabi

    """
    PA = 87

    """

    Polish

    """
    PL = 88

    """

    Pashto, Pushto

    """
    PS = 89

    """

    Portuguese

    """
    PT = 90

    """

    Quechua

    """
    QU = 91

    """

    Rhaeto Romance

    """
    RM = 92

    """

    Kirundi

    """
    RN = 93

    """

    Romanian

    """
    RO = 94

    """

    Russian

    """
    RU = 95

    """

    Kinyarwanda

    """
    RW = 96

    """

    Sanskrit

    """
    SA = 97

    """

    Sindhi

    """
    SD = 98

    """

    Sangho

    """
    SG = 99

    """

    Serbo Croatian

    """
    SH = 100

    """

    Sinhalese

    """
    SI = 101

    """

    Slovak

    """
    SK = 102

    """

    Slovenian

    """
    SL = 103

    """

    Samoan

    """
    SM = 104

    """

    Shona

    """
    SN = 105

    """

    Somali

    """
    SO = 106

    """

    Albanian

    """
    SQ = 107

    """

    Serbian

    """
    SR = 108

    """

    Siswati

    """
    SS = 109

    """

    Sesotho

    """
    ST = 110

    """

    Sundanese

    """
    SU = 111

    """

    Swedish

    """
    SV = 112

    """

    Swahili

    """
    SW = 113

    """

    Tamil

    """
    TA = 114

    """

    Telugu

    """
    TE = 115

    """

    Tajik

    """
    TG = 116

    """

    Thai

    """
    TH = 117

    """

    Tigrinya

    """
    TI = 118

    """

    Turkmen

    """
    TK = 119

    """

    Tagalog

    """
    TL = 120

    """

    Setswana

    """
    TN = 121

    """

    Tonga

    """
    TO = 122

    """

    Turkish

    """
    TR = 123

    """

    Tsonga

    """
    TS = 124

    """

    Tatar

    """
    TT = 125

    """

    Twi

    """
    TW = 126

    """

    Uighur

    """
    UG = 127

    """

    Ukrainian

    """
    UK = 128

    """

    Urdu

    """
    UR = 129

    """

    Uzbek

    """
    UZ = 130

    """

    Vietnamese

    """
    VI = 131

    """

    Volapuk

    """
    VO = 132

    """

    Wolof

    """
    WO = 133

    """

    Xhosa

    """
    XH = 134

    """

    Yiddish

    """
    YI = 135

    """

    Yoruba

    """
    YO = 136

    """

    Zhuang

    """
    ZA = 137

    """

    Chinese

    """
    ZH = 138

    """

    Zulu

    """
    ZU = 139


    @staticmethod
    def _meta_info():
        from ydk.models.infra._meta import _Cisco_IOS_XR_infra_infra_locale_cfg as meta
        return meta._meta_table['LocaleLanguage_Enum']



class Locale(object):
    """
    Define the geographical locale
    
    .. attribute:: country
    
    	Name of country locale
    	**type**\: :py:class:`LocaleCountry_Enum <ydk.models.infra.Cisco_IOS_XR_infra_infra_locale_cfg.LocaleCountry_Enum>`
    
    .. attribute:: language
    
    	Name of language locale
    	**type**\: :py:class:`LocaleLanguage_Enum <ydk.models.infra.Cisco_IOS_XR_infra_infra_locale_cfg.LocaleLanguage_Enum>`
    
    

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
        if self.is_presence():
            return True
        if self.country is not None:
            return True

        if self.language is not None:
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.infra._meta import _Cisco_IOS_XR_infra_infra_locale_cfg as meta
        return meta._meta_table['Locale']['meta_info']


