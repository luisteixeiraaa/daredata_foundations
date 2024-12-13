from enum import Enum, unique


@unique
class Region(Enum):
    """Enumerator class for countries available in the dataset."""

    AT = "AT"
    BE = "BE"
    BG = "BG"
    CH = "CH"
    CY = "CY"
    CZ = "CZ"
    DK = "DK"
    EE = "EE"
    EL = "EL"
    ES = "ES"
    EU27_2020 = "EU27_2020"
    EU = "EU"
    FI = "FI"
    FR = "FR"
    HR = "HR"
    HU = "HU"
    IS = "IS"
    IT = "IT"
    LI = "LI"
    LT = "LT"
    LU = "LU"
    LV = "LV"
    MT = "MT"
    NL = "NL"
    NO = "NO"
    PL = "PL"
    PT = "PT"
    RO = "RO"
    SE = "SE"
    SI = "SI"
    SK = "SK"
    DE = "DE"
    DE_TOT = "DE_TOT"
    AL = "AL"
    EA18 = "EA18"
    EA19 = "EA19"
    EFTA = "EFTA"
    IE = "IE"
    ME = "ME"
    MK = "MK"
    RS = "RS"
    AM = "AM"
    AZ = "AZ"
    GE = "GE"
    TR = "TR"
    UA = "UA"
    BY = "BY"
    EEA30_2007 = "EEA30_2007"

    @classmethod
    def valid_countries(cls) -> list:
        """method to return only valid countries in the enum class Region.
        Consider that a country is valid if it is in their shortform.

        :return list[Region]: List of valid regions.
        """
        return [region for region in cls if len(region.value) == 2]
