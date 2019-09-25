#
# PySNMP MIB module NPB-SYSTEM (http://snmplabs.com/pysmi)
# ASN.1 source file://./NPB-SYSTEM.mib
# Produced by pysmi-0.3.4 at Wed Sep 25 12:44:10 2019
# On host MacBook-Pro-anthony.local platform Darwin version 18.7.0 by user anthony
# Using Python version 2.7.10 (default, Feb 22 2019, 21:55:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
Ipv6Address, = mibBuilder.importSymbols("IPV6-TC", "Ipv6Address")
npb_2, = mibBuilder.importSymbols("NPB-NPB-2", "npb-2")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, Bits, TimeTicks, Counter64, Unsigned32, ModuleIdentity, Gauge32, iso, ObjectIdentity, IpAddress, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "Bits", "TimeTicks", "Counter64", "Unsigned32", "ModuleIdentity", "Gauge32", "iso", "ObjectIdentity", "IpAddress", "Counter32")
TruthValue, DisplayString, RowStatus, TextualConvention, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "RowStatus", "TextualConvention", "DateAndTime")
systemMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1))
systemMib.setRevisions(('2015-12-29 00:00',))
if mibBuilder.loadTexts: systemMib.setLastUpdated('201512290000Z')
if mibBuilder.loadTexts: systemMib.setOrganization('@ORGANIZATION')
class UnsignedByte(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class UnsignedShort(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class ConfdString(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class InetAddressIP(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(16, 16), )
class String(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class HexList(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1x:'

class SwUpgradeStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    namedValues = NamedValues(("not-started", 0), ("downloading", 1), ("downloading-failed", 2), ("verifying", 3), ("verify-failed", 4), ("burn-in-progress", 5), ("burn-failed", 6), ("canceling", 7), ("stopped", 8), ("succeed", 9))

class ConsolePortBaudrate(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class TimeAndDateSource(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + SingleValueConstraint(1, 2)
    namedValues = NamedValues(("local-config", 1), ("ntp-server", 2))

class AlarmManagerStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + SingleValueConstraint(0, 1, 2)
    namedValues = NamedValues(("open", 0), ("close", 1), ("event", 2))

class AuthAccess(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + SingleValueConstraint(1, 2)
    namedValues = NamedValues(("read-only", 1), ("read-write", 2))

class SwActionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + SingleValueConstraint(0, 1)
    namedValues = NamedValues(("start", 0), ("stop", 1))

class SwSwImageFile(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 1024)

class AlarmModule(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + SingleValueConstraint(0, 1, 2, 3, 4, 5, 6)
    namedValues = NamedValues(("port", 0), ("filter", 1), ("hw", 2), ("recovery", 3), ("powerup", 4), ("system", 5), ("lb", 6))

class SwBootBank(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + SingleValueConstraint(0, 1)
    namedValues = NamedValues(("bank-a", 0), ("bank-b", 1))

class SyslogComparison(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + SingleValueConstraint(0, 1)
    namedValues = NamedValues(("sameOrHigher", 0), ("same", 1))

class SwUpgradeProgress(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 100)

class AaaName(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class AclName(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class AuthProtocol(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + SingleValueConstraint(0, 1, 2)
    namedValues = NamedValues(("none", 0), ("md5", 1), ("sha", 2))

class PrivProtocol(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + SingleValueConstraint(0, 1, 2)
    namedValues = NamedValues(("none", 0), ("des", 1), ("aes-128", 2))

class AuthprivPass(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class PortDuplexConfig(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 8)

class Direction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + SingleValueConstraint(0, 1, 2)
    namedValues = NamedValues(("bToF", 0), ("fToB", 1), ("none", 2))

class KeyDigest(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + SingleValueConstraint(0, 1, 2, 3)
    namedValues = NamedValues(("md5", 0), ("sha", 1), ("sha1", 2), ("none", 3))

class ConfigLocalFile(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class SwSwVersion(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 256)

class TrapVer(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + SingleValueConstraint(1, 4)
    namedValues = NamedValues(("v2c-trap", 1), ("v3-trap", 4))

class SyslogFacility(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21)
    namedValues = NamedValues(("auth", 0), ("authpriv", 1), ("cron", 2), ("daemon", 3), ("ftp", 4), ("kern", 5), ("lpr", 6), ("mail", 7), ("news", 8), ("security", 9), ("syslog", 10), ("user", 11), ("uucp", 12), ("local0", 13), ("local1", 14), ("local2", 15), ("local3", 16), ("local4", 17), ("local5", 18), ("local6", 19), ("local7", 20), ("all", 21))

class Authentication(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + SingleValueConstraint(0, 1)
    namedValues = NamedValues(("none", 0), ("symmetric-keys", 1))

class MgmtPortSpeedConfig(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + SingleValueConstraint(10, 100, 1000, 9999)
    namedValues = NamedValues(("speed10M", 10), ("speed100M", 100), ("speed1000M", 1000), ("auto", 9999))

class AlarmContext(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + SingleValueConstraint(0, 1, 2, 3)
    namedValues = NamedValues(("cli", 0), ("webui", 1), ("snmp", 2), ("netconf", 3))

class AlarmSeverity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + SingleValueConstraint(0, 1, 2, 3)
    namedValues = NamedValues(("info", 0), ("minor", 1), ("major", 2), ("critical", 3))

class SyslogTransport(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + SingleValueConstraint(0, 1, 2)
    namedValues = NamedValues(("udp", 0), ("tcp", 1), ("relp", 2))

class LocalFile(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class PortDuplex(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + SingleValueConstraint(0, 1, 2)
    namedValues = NamedValues(("unknown", 0), ("half", 1), ("full", 2))

class RemoteAuthentication(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + SingleValueConstraint(0, 1)
    namedValues = NamedValues(("radius", 0), ("tacacs", 1))

class Group(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + SingleValueConstraint(1, 2, 3)
    namedValues = NamedValues(("admin", 1), ("oper", 2), ("read-only", 3))

class LedControlOper(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + SingleValueConstraint(0, 1)
    namedValues = NamedValues(("off", 0), ("on", 1))

class MgmtPortSpeed(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + SingleValueConstraint(0, 10, 100, 1000, 10000)
    namedValues = NamedValues(("na", 0), ("speed10M", 10), ("speed100M", 100), ("speed1G", 1000), ("speed10G", 10000))

class SyslogPriority(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    namedValues = NamedValues(("emerg", 0), ("alert", 1), ("crit", 2), ("err", 3), ("warning", 4), ("notice", 5), ("info", 6), ("debug", 7), ("none", 8), ("all", 9))

class RemoteUrl(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 1024)

class PsuOverType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + SingleValueConstraint(-1, 0, 1)
    namedValues = NamedValues(("notExist", -1), ("normal", 0), ("overHeat", 1))

class StatusType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + SingleValueConstraint(-1, 0, 1)
    namedValues = NamedValues(("na", -1), ("fail", 0), ("good", 1))

class SyslogActionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + SingleValueConstraint(0, 1, 2)
    namedValues = NamedValues(("local-file", 0), ("local-user", 1), ("remote-machine", 2))

class AaaPassword(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class Password(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class Timezone(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254), SingleValueConstraint(255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509), SingleValueConstraint(510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596))
    namedValues = NamedValues(("africa-abidjan", 0), ("africa-accra", 1), ("africa-addisAbaba", 2), ("africa-algiers", 3), ("africa-asmara", 4), ("africa-asmera", 5), ("africa-bamako", 6), ("africa-bangui", 7), ("africa-banjul", 8), ("africa-bissau", 9), ("africa-blantyre", 10), ("africa-brazzaville", 11), ("africa-bujumbura", 12), ("africa-cairo", 13), ("africa-casablanca", 14), ("africa-ceuta", 15), ("africa-conakry", 16), ("africa-dakar", 17), ("africa-darEsSalaam", 18), ("africa-djibouti", 19), ("africa-douala", 20), ("africa-elAaiun", 21), ("africa-freetown", 22), ("africa-gaborone", 23), ("africa-harare", 24), ("africa-johannesburg", 25), ("africa-juba", 26), ("africa-kampala", 27), ("africa-khartoum", 28), ("africa-kigali", 29), ("africa-kinshasa", 30), ("africa-lagos", 31), ("africa-libreville", 32), ("africa-lome", 33), ("africa-luanda", 34), ("africa-lubumbashi", 35), ("africa-lusaka", 36), ("africa-malabo", 37), ("africa-maputo", 38), ("africa-maseru", 39), ("africa-mbabane", 40), ("africa-mogadishu", 41), ("africa-monrovia", 42), ("africa-nairobi", 43), ("africa-ndjamena", 44), ("africa-niamey", 45), ("africa-nouakchott", 46), ("africa-ouagadougou", 47), ("africa-Porto-novo", 48), ("africa-saoTome", 49), ("africa-timbuktu", 50), ("africa-tripoli", 51), ("africa-tunis", 52), ("africa-windhoek", 53), ("america-adak", 54), ("america-anchorage", 55), ("america-anguilla", 56), ("america-antigua", 57), ("america-araguaina", 58), ("america-Argentina-buenosAires", 59), ("america-Argentina-catamarca", 60), ("america-Argentina-comodRivadavia", 61), ("america-Argentina-cordoba", 62), ("america-Argentina-jujuy", 63), ("america-Argentina-laRioja", 64), ("america-Argentina-mendoza", 65), ("america-Argentina-rioGallegos", 66), ("america-Argentina-salta", 67), ("america-Argentina-sanJuan", 68), ("america-Argentina-sanLuis", 69), ("america-Argentina-tucuman", 70), ("america-Argentina-ushuaia", 71), ("america-aruba", 72), ("america-asuncion", 73), ("america-atikokan", 74), ("america-atka", 75), ("america-bahia", 76), ("america-bahiaBanderas", 77), ("america-barbados", 78), ("america-belem", 79), ("america-belize", 80), ("america-Blanc-sablon", 81), ("america-boaVista", 82), ("america-bogota", 83), ("america-boise", 84), ("america-buenosAires", 85), ("america-cambridgeBay", 86), ("america-campoGrande", 87), ("america-cancun", 88), ("america-caracas", 89), ("america-catamarca", 90), ("america-cayenne", 91), ("america-cayman", 92), ("america-chicago", 93), ("america-chihuahua", 94), ("america-coralHarbour", 95), ("america-cordoba", 96), ("america-costaRica", 97), ("america-creston", 98), ("america-cuiaba", 99), ("america-curacao", 100), ("america-danmarkshavn", 101), ("america-dawson", 102), ("america-dawsonCreek", 103), ("america-denver", 104), ("america-detroit", 105), ("america-dominica", 106), ("america-edmonton", 107), ("america-eirunepe", 108), ("america-elSalvador", 109), ("america-ensenada", 110), ("america-fortNelson", 111), ("america-fortWayne", 112), ("america-fortaleza", 113), ("america-glaceBay", 114), ("america-godthab", 115), ("america-gooseBay", 116), ("america-grandTurk", 117), ("america-grenada", 118), ("america-guadeloupe", 119), ("america-guatemala", 120), ("america-guayaquil", 121), ("america-guyana", 122), ("america-halifax", 123), ("america-havana", 124), ("america-hermosillo", 125), ("america-Indiana-indianapolis", 126), ("america-Indiana-knox", 127), ("america-Indiana-marengo", 128), ("america-Indiana-petersburg", 129), ("america-Indiana-tellCity", 130), ("america-Indiana-vevay", 131), ("america-Indiana-vincennes", 132), ("america-Indiana-winamac", 133), ("america-indianapolis", 134), ("america-inuvik", 135), ("america-iqaluit", 136), ("america-jamaica", 137), ("america-jujuy", 138), ("america-juneau", 139), ("america-Kentucky-louisville", 140), ("america-Kentucky-monticello", 141), ("america-knoxIN", 142), ("america-kralendijk", 143), ("america-laPaz", 144), ("america-lima", 145), ("america-losAngeles", 146), ("america-louisville", 147), ("america-lowerPrinces", 148), ("america-maceio", 149), ("america-managua", 150), ("america-manaus", 151), ("america-marigot", 152), ("america-martinique", 153), ("america-matamoros", 154), ("america-mazatlan", 155), ("america-mendoza", 156), ("america-menominee", 157), ("america-merida", 158), ("america-metlakatla", 159), ("america-mexicoCity", 160), ("america-miquelon", 161), ("america-moncton", 162), ("america-monterrey", 163), ("america-montevideo", 164), ("america-montreal", 165), ("america-montserrat", 166), ("america-nassau", 167), ("america-newYork", 168), ("america-nipigon", 169), ("america-nome", 170), ("america-noronha", 171), ("america-NorthDakota-beulah", 172), ("america-NorthDakota-center", 173), ("america-NorthDakota-newSalem", 174), ("america-ojinaga", 175), ("america-panama", 176), ("america-pangnirtung", 177), ("america-paramaribo", 178), ("america-phoenix", 179), ("america-Port-au-prince", 180), ("america-portofSpain", 181), ("america-portoAcre", 182), ("america-portoVelho", 183), ("america-puertoRico", 184), ("america-rainyRiver", 185), ("america-rankinInlet", 186), ("america-recife", 187), ("america-regina", 188), ("america-resolute", 189), ("america-rioBranco", 190), ("america-rosario", 191), ("america-santaIsabel", 192), ("america-santarem", 193), ("america-santiago", 194), ("america-santoDomingo", 195), ("america-saoPaulo", 196), ("america-scoresbysund", 197), ("america-shiprock", 198), ("america-sitka", 199), ("america-stBarthelemy", 200), ("america-stJohns", 201), ("america-stKitts", 202), ("america-stLucia", 203), ("america-stThomas", 204), ("america-stVincent", 205), ("america-swiftCurrent", 206), ("america-tegucigalpa", 207), ("america-thule", 208), ("america-thunderBay", 209), ("america-tijuana", 210), ("america-toronto", 211), ("america-tortola", 212), ("america-vancouver", 213), ("america-virgin", 214), ("america-whitehorse", 215), ("america-winnipeg", 216), ("america-yakutat", 217), ("america-yellowknife", 218), ("antarctica-casey", 219), ("antarctica-davis", 220), ("antarctica-dumontDUrville", 221), ("antarctica-macquarie", 222), ("antarctica-mawson", 223), ("antarctica-mcMurdo", 224), ("antarctica-palmer", 225), ("antarctica-rothera", 226), ("antarctica-southPole", 227), ("antarctica-syowa", 228), ("antarctica-troll", 229), ("antarctica-vostok", 230), ("arctic-longyearbyen", 231), ("asia-aden", 232), ("asia-almaty", 233), ("asia-amman", 234), ("asia-anadyr", 235), ("asia-aqtau", 236), ("asia-aqtobe", 237), ("asia-ashgabat", 238), ("asia-ashkhabad", 239), ("asia-baghdad", 240), ("asia-bahrain", 241), ("asia-baku", 242), ("asia-bangkok", 243), ("asia-beirut", 244), ("asia-bishkek", 245), ("asia-brunei", 246), ("asia-calcutta", 247), ("asia-chita", 248), ("asia-choibalsan", 249), ("asia-chongqing", 250), ("asia-chungking", 251), ("asia-colombo", 252), ("asia-dacca", 253), ("asia-damascus", 254)) + NamedValues(("asia-dhaka", 255), ("asia-dili", 256), ("asia-dubai", 257), ("asia-dushanbe", 258), ("asia-gaza", 259), ("asia-harbin", 260), ("asia-hebron", 261), ("asia-hoChiMinh", 262), ("asia-hongKong", 263), ("asia-hovd", 264), ("asia-irkutsk", 265), ("asia-istanbul", 266), ("asia-jakarta", 267), ("asia-jayapura", 268), ("asia-jerusalem", 269), ("asia-kabul", 270), ("asia-kamchatka", 271), ("asia-karachi", 272), ("asia-kashgar", 273), ("asia-kathmandu", 274), ("asia-katmandu", 275), ("asia-khandyga", 276), ("asia-kolkata", 277), ("asia-krasnoyarsk", 278), ("asia-kualaLumpur", 279), ("asia-kuching", 280), ("asia-kuwait", 281), ("asia-macao", 282), ("asia-macau", 283), ("asia-magadan", 284), ("asia-makassar", 285), ("asia-manila", 286), ("asia-muscat", 287), ("asia-nicosia", 288), ("asia-novokuznetsk", 289), ("asia-novosibirsk", 290), ("asia-omsk", 291), ("asia-oral", 292), ("asia-phnomPenh", 293), ("asia-pontianak", 294), ("asia-pyongyang", 295), ("asia-qatar", 296), ("asia-qyzylorda", 297), ("asia-rangoon", 298), ("asia-riyadh", 299), ("asia-saigon", 300), ("asia-sakhalin", 301), ("asia-samarkand", 302), ("asia-seoul", 303), ("asia-shanghai", 304), ("asia-singapore", 305), ("asia-srednekolymsk", 306), ("asia-taipei", 307), ("asia-tashkent", 308), ("asia-tbilisi", 309), ("asia-tehran", 310), ("asia-telAviv", 311), ("asia-thimbu", 312), ("asia-thimphu", 313), ("asia-tokyo", 314), ("asia-ujungPandang", 315), ("asia-ulaanbaatar", 316), ("asia-ulanBator", 317), ("asia-urumqi", 318), ("asia-Ust-nera", 319), ("asia-vientiane", 320), ("asia-vladivostok", 321), ("asia-yakutsk", 322), ("asia-yekaterinburg", 323), ("asia-yerevan", 324), ("atlantic-azores", 325), ("atlantic-bermuda", 326), ("atlantic-canary", 327), ("atlantic-capeVerde", 328), ("atlantic-faeroe", 329), ("atlantic-faroe", 330), ("atlantic-janMayen", 331), ("atlantic-madeira", 332), ("atlantic-reykjavik", 333), ("atlantic-southGeorgia", 334), ("atlantic-stHelena", 335), ("atlantic-stanley", 336), ("australia-aCT", 337), ("australia-adelaide", 338), ("australia-brisbane", 339), ("australia-brokenHill", 340), ("australia-canberra", 341), ("australia-currie", 342), ("australia-darwin", 343), ("australia-eucla", 344), ("australia-hobart", 345), ("australia-lHI", 346), ("australia-lindeman", 347), ("australia-lordHowe", 348), ("australia-melbourne", 349), ("australia-nSW", 350), ("australia-north", 351), ("australia-perth", 352), ("australia-queensland", 353), ("australia-south", 354), ("australia-sydney", 355), ("australia-tasmania", 356), ("australia-victoria", 357), ("australia-west", 358), ("australia-yancowinna", 359), ("brazil-acre", 360), ("brazil-deNoronha", 361), ("brazil-east", 362), ("brazil-west", 363), ("cET", 364), ("cST6CDT", 365), ("canada-atlantic", 366), ("canada-central", 367), ("canada-East-saskatchewan", 368), ("canada-eastern", 369), ("canada-mountain", 370), ("canada-newfoundland", 371), ("canada-pacific", 372), ("canada-saskatchewan", 373), ("canada-yukon", 374), ("chile-continental", 375), ("chile-easterIsland", 376), ("cuba", 377), ("eet", 378), ("est", 379), ("est5edt", 380), ("egypt", 381), ("eire", 382), ("etc-GMT", 383), ("etc-GMT-plus0", 384), ("etc-GMT-plus1", 385), ("etc-GMT-plus10", 386), ("etc-GMT-plus11", 387), ("etc-GMT-plus12", 388), ("etc-GMT-plus2", 389), ("etc-GMT-plus3", 390), ("etc-GMT-plus4", 391), ("etc-GMT-plus5", 392), ("etc-GMT-plus6", 393), ("etc-GMT-plus7", 394), ("etc-GMT-plus8", 395), ("etc-GMT-plus9", 396), ("etc-GMT-minus0", 397), ("etc-GMT-minus1", 398), ("etc-GMT-minus10", 399), ("etc-GMT-minus11", 400), ("etc-GMT-minus12", 401), ("etc-GMT-minus13", 402), ("etc-GMT-minus14", 403), ("etc-GMT-minus2", 404), ("etc-GMT-minus3", 405), ("etc-GMT-minus4", 406), ("etc-GMT-minus5", 407), ("etc-GMT-minus6", 408), ("etc-GMT-minus7", 409), ("etc-GMT-minus8", 410), ("etc-GMT-minus9", 411), ("etc-GMT0", 412), ("etc-greenwich", 413), ("etc-uct", 414), ("etc-utc", 415), ("etc-universal", 416), ("etc-zulu", 417), ("europe-amsterdam", 418), ("europe-andorra", 419), ("europe-athens", 420), ("europe-belfast", 421), ("europe-belgrade", 422), ("europe-berlin", 423), ("europe-bratislava", 424), ("europe-brussels", 425), ("europe-bucharest", 426), ("europe-budapest", 427), ("europe-busingen", 428), ("europe-chisinau", 429), ("europe-copenhagen", 430), ("europe-dublin", 431), ("europe-gibraltar", 432), ("europe-guernsey", 433), ("europe-helsinki", 434), ("europe-isleOfMan", 435), ("europe-istanbul", 436), ("europe-jersey", 437), ("europe-kaliningrad", 438), ("europe-kiev", 439), ("europe-lisbon", 440), ("europe-ljubljana", 441), ("europe-london", 442), ("europe-luxembourg", 443), ("europe-madrid", 444), ("europe-malta", 445), ("europe-mariehamn", 446), ("europe-minsk", 447), ("europe-monaco", 448), ("europe-moscow", 449), ("europe-nicosia", 450), ("europe-oslo", 451), ("europe-paris", 452), ("europe-podgorica", 453), ("europe-prague", 454), ("europe-riga", 455), ("europe-rome", 456), ("europe-samara", 457), ("europe-sanMarino", 458), ("europe-sarajevo", 459), ("europe-simferopol", 460), ("europe-skopje", 461), ("europe-sofia", 462), ("europe-stockholm", 463), ("europe-tallinn", 464), ("europe-tirane", 465), ("europe-tiraspol", 466), ("europe-uzhgorod", 467), ("europe-vaduz", 468), ("europe-vatican", 469), ("europe-vienna", 470), ("europe-vilnius", 471), ("europe-volgograd", 472), ("europe-warsaw", 473), ("europe-zagreb", 474), ("europe-zaporozhye", 475), ("europe-zurich", 476), ("factory", 477), ("gb", 478), ("gb-eire", 479), ("gmt", 480), ("gmt-plus0", 481), ("gmt-minus0", 482), ("gmt0", 483), ("greenwich", 484), ("hst", 485), ("hongkong", 486), ("iceland", 487), ("indian-antananarivo", 488), ("indian-chagos", 489), ("indian-christmas", 490), ("indian-cocos", 491), ("indian-comoro", 492), ("indian-kerguelen", 493), ("indian-mahe", 494), ("indian-maldives", 495), ("indian-mauritius", 496), ("indian-mayotte", 497), ("indian-reunion", 498), ("iran", 499), ("israel", 500), ("jamaica", 501), ("japan", 502), ("kwajalein", 503), ("libya", 504), ("met", 505), ("mst", 506), ("mst7mdt", 507), ("mexico-bajaNorte", 508), ("mexico-bajaSur", 509)) + NamedValues(("mexico-general", 510), ("nz", 511), ("nz-chat", 512), ("navajo", 513), ("prc", 514), ("pst8pdt", 515), ("pacific-apia", 516), ("pacific-auckland", 517), ("pacific-bougainville", 518), ("pacific-chatham", 519), ("pacific-chuuk", 520), ("pacific-easter", 521), ("pacific-efate", 522), ("pacific-enderbury", 523), ("pacific-fakaofo", 524), ("pacific-fiji", 525), ("pacific-funafuti", 526), ("pacific-galapagos", 527), ("pacific-gambier", 528), ("pacific-guadalcanal", 529), ("pacific-guam", 530), ("pacific-honolulu", 531), ("pacific-johnston", 532), ("pacific-kiritimati", 533), ("pacific-kosrae", 534), ("pacific-kwajalein", 535), ("pacific-majuro", 536), ("pacific-marquesas", 537), ("pacific-midway", 538), ("pacific-nauru", 539), ("pacific-niue", 540), ("pacific-norfolk", 541), ("pacific-noumea", 542), ("pacific-pagoPago", 543), ("pacific-palau", 544), ("pacific-pitcairn", 545), ("pacific-pohnpei", 546), ("pacific-ponape", 547), ("pacific-portMoresby", 548), ("pacific-rarotonga", 549), ("pacific-saipan", 550), ("pacific-samoa", 551), ("pacific-tahiti", 552), ("pacific-tarawa", 553), ("pacific-tongatapu", 554), ("pacific-truk", 555), ("pacific-wake", 556), ("pacific-wallis", 557), ("pacific-yap", 558), ("poland", 559), ("portugal", 560), ("roc", 561), ("rok", 562), ("singapore", 563), ("systemV-aST4", 564), ("systemV-aST4ADT", 565), ("systemV-cST6", 566), ("systemV-cST6CDT", 567), ("systemV-eST5", 568), ("systemV-eST5EDT", 569), ("systemV-hST10", 570), ("systemV-mST7", 571), ("systemV-mST7MDT", 572), ("systemV-pST8", 573), ("systemV-pST8PDT", 574), ("systemV-yST9", 575), ("systemV-yST9YDT", 576), ("turkey", 577), ("uct", 578), ("uS-alaska", 579), ("uS-aleutian", 580), ("uS-arizona", 581), ("uS-central", 582), ("uS-East-indiana", 583), ("uS-eastern", 584), ("uS-hawaii", 585), ("uS-Indiana-starke", 586), ("uS-michigan", 587), ("uS-mountain", 588), ("uS-pacific", 589), ("uS-Pacific-new", 590), ("uS-samoa", 591), ("utc", 592), ("universal", 593), ("w-su", 594), ("wet", 595), ("zulu", 596))

class Username(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class UserAuthPriority(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + SingleValueConstraint(0, 1)
    namedValues = NamedValues(("high", 0), ("low", 1))

system = MibIdentifier((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1))
systemHw = MibIdentifier((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 1))
systemHwLocationLed = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 1, 1), LedControlOper()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemHwLocationLed.setStatus('current')
systemConfigFiles = MibIdentifier((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 2))
systemLog = MibIdentifier((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 3))
systemLogLevel = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 3, 1), Integer32().subtype(subtypeSpec=SingleValueConstraint(0, 1)).clone(namedValues=NamedValues(("normal", 0), ("debug", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemLogLevel.setStatus('current')
systemAaa = MibIdentifier((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 4))
systemNpb2 = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 5), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemNpb2.setStatus('current')
systemAlarms = MibIdentifier((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 6))
systemAlarmsSyslog = MibIdentifier((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 6, 1))
systemAlarmsSyslogEnabled = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 6, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemAlarmsSyslogEnabled.setStatus('current')
systemAlarmsTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 6, 2))
systemAlarmsTrapEnabled = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 6, 2, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemAlarmsTrapEnabled.setStatus('current')
systemSecurity = MibIdentifier((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 7))
systemSyslog = MibIdentifier((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 8))
systemTimeAndDate = MibIdentifier((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 9))
systemTimeAndDateCurrentTimeAndDate = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 9, 1), String()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemTimeAndDateCurrentTimeAndDate.setStatus('current')
systemTimeAndDateShowTime = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 9, 2), String().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemTimeAndDateShowTime.setStatus('current')
systemTimeAndDateShowDate = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 9, 3), String().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemTimeAndDateShowDate.setStatus('current')
systemTimeAndDateTimeZone = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 9, 4), Timezone()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemTimeAndDateTimeZone.setStatus('current')
systemTimeAndDateNtp = MibIdentifier((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 9, 5))
systemTimeAndDateNtpAdmin = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 9, 5, 1), Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2)).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemTimeAndDateNtpAdmin.setStatus('current')
systemTimeAndDateNtpNtpStatusAsString = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 9, 5, 2), String().subtype(subtypeSpec=ValueSizeConstraint(0, 512))).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemTimeAndDateNtpNtpStatusAsString.setStatus('current')
systemTimeAndDatePtp = MibIdentifier((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 9, 6))
systemTimeAndDatePtpAdmin = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 9, 6, 1), Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2)).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemTimeAndDatePtpAdmin.setStatus('current')
systemMgmtPort = MibIdentifier((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 10))
systemMgmtPortIpv4Address = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 10, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemMgmtPortIpv4Address.setStatus('current')
systemMgmtPortIpv4Mask = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 10, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemMgmtPortIpv4Mask.setStatus('current')
systemMgmtPortIpv4Gateway = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 10, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemMgmtPortIpv4Gateway.setStatus('current')
systemMgmtPortIpv6Address = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 10, 4), Ipv6Address()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemMgmtPortIpv6Address.setStatus('current')
systemMgmtPortIpv6PrefixLen = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 10, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemMgmtPortIpv6PrefixLen.setStatus('current')
systemMgmtPortIpv6Gateway = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 10, 6), Ipv6Address()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemMgmtPortIpv6Gateway.setStatus('current')
systemMgmtPortDhcp = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 10, 7), Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2)).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemMgmtPortDhcp.setStatus('current')
systemMgmtPortSpeed = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 10, 8), MgmtPortSpeedConfig()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemMgmtPortSpeed.setStatus('current')
systemMgmtPortDuplex = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 10, 9), PortDuplexConfig()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemMgmtPortDuplex.setStatus('current')
systemMgmtPortActMgmtPort = MibIdentifier((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 10, 10))
systemMgmtPortActMgmtPortActMac = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 10, 10, 1), String().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemMgmtPortActMgmtPortActMac.setStatus('current')
systemMgmtPortActMgmtPortActLink = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 10, 10, 2), String().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemMgmtPortActMgmtPortActLink.setStatus('current')
systemMgmtPortActMgmtPortActSpeed = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 10, 10, 3), MgmtPortSpeed()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemMgmtPortActMgmtPortActSpeed.setStatus('current')
systemMgmtPortActMgmtPortActDuplex = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 10, 10, 4), String().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemMgmtPortActMgmtPortActDuplex.setStatus('current')
systemMgmtPortActMgmtPortActIpv4Address = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 10, 10, 5), String().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemMgmtPortActMgmtPortActIpv4Address.setStatus('current')
systemMgmtPortActMgmtPortActIpv4Mask = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 10, 10, 6), String().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemMgmtPortActMgmtPortActIpv4Mask.setStatus('current')
systemMgmtPortActMgmtPortActIpv4Gateway = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 10, 10, 7), String().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemMgmtPortActMgmtPortActIpv4Gateway.setStatus('current')
systemMgmtPortActMgmtPortActIpv6Address = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 10, 10, 8), String()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemMgmtPortActMgmtPortActIpv6Address.setStatus('current')
systemMgmtPortActMgmtPortActIpv6PrefixLen = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 10, 10, 9), String().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemMgmtPortActMgmtPortActIpv6PrefixLen.setStatus('current')
systemMgmtPortActMgmtPortActIpv6Gateway = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 10, 10, 10), String()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemMgmtPortActMgmtPortActIpv6Gateway.setStatus('current')
systemConsolePort = MibIdentifier((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 11))
systemConsolePortCurrentBaudrate = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 11, 1), ConsolePortBaudrate()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemConsolePortCurrentBaudrate.setStatus('current')
systemUserMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 12))
systemUserMgmtLocalAuth = MibIdentifier((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 12, 1))
systemUserMgmtLocalAuthOrder = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 12, 1, 1), UserAuthPriority()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemUserMgmtLocalAuthOrder.setStatus('current')
systemUserMgmtRemoteAuth = MibIdentifier((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 12, 2))
systemUserMgmtRemoteAuthOrder = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 12, 2, 1), UserAuthPriority()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemUserMgmtRemoteAuthOrder.setStatus('current')
systemDetails = MibIdentifier((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 13))
systemDetailsModelName = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 13, 1), String().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemDetailsModelName.setStatus('current')
systemDetailsSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 13, 2), String().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemDetailsSerialNumber.setStatus('current')
systemDetailsSwVersion = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 13, 3), String().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemDetailsSwVersion.setStatus('current')
systemDetailsHwVersion = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 13, 4), String().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemDetailsHwVersion.setStatus('current')
systemDetailsSwitchName = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 13, 5), String().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemDetailsSwitchName.setStatus('current')
systemDetailsSwitchVersion = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 13, 6), String().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemDetailsSwitchVersion.setStatus('current')
systemDetailsCpuType = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 13, 7), String().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemDetailsCpuType.setStatus('current')
systemDetailsHostname = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 13, 8), String().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemDetailsHostname.setStatus('current')
systemHwStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 14))
systemSwUpgrade = MibIdentifier((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 15))
systemSwUpgradeStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 15, 1))
systemSwUpgradeStatusBootBankCur = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 15, 1, 1), SwBootBank()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemSwUpgradeStatusBootBankCur.setStatus('current')
systemSwUpgradeStatusActiveBootBank = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 15, 1, 2), SwBootBank()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemSwUpgradeStatusActiveBootBank.setStatus('current')
systemSwUpgradeStatusActiveSwVersion = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 15, 1, 3), SwSwVersion()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemSwUpgradeStatusActiveSwVersion.setStatus('current')
systemSwUpgradeStatusActiveSwImageFile = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 15, 1, 4), SwSwImageFile()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemSwUpgradeStatusActiveSwImageFile.setStatus('current')
systemSwUpgradeStatusUpgradeStatus = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 15, 1, 5), SwUpgradeStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemSwUpgradeStatusUpgradeStatus.setStatus('current')
systemSwUpgradeStatusDownloadProgess = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 15, 1, 6), SwUpgradeProgress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemSwUpgradeStatusDownloadProgess.setStatus('current')
systemSwUpgradeStatusErrorMessage = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 15, 1, 7), String()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemSwUpgradeStatusErrorMessage.setStatus('current')
systemSwUpgradeStatusSwBankA = MibIdentifier((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 15, 1, 8))
systemSwUpgradeStatusSwBankABank = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 15, 1, 8, 1), SwBootBank()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemSwUpgradeStatusSwBankABank.setStatus('current')
systemSwUpgradeStatusSwBankASwVersion = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 15, 1, 8, 2), SwSwVersion()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemSwUpgradeStatusSwBankASwVersion.setStatus('current')
systemSwUpgradeStatusSwBankASwImageFile = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 15, 1, 8, 3), SwSwImageFile()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemSwUpgradeStatusSwBankASwImageFile.setStatus('current')
systemSwUpgradeStatusSwBankAStatus = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 15, 1, 8, 4), Integer32().subtype(subtypeSpec=SingleValueConstraint(0, 1, 2)).clone(namedValues=NamedValues(("valid", 0), ("corrupt", 1), ("empty", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemSwUpgradeStatusSwBankAStatus.setStatus('current')
systemSwUpgradeStatusSwBankB = MibIdentifier((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 15, 1, 9))
systemSwUpgradeStatusSwBankBBank = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 15, 1, 9, 1), SwBootBank()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemSwUpgradeStatusSwBankBBank.setStatus('current')
systemSwUpgradeStatusSwBankBSwVersion = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 15, 1, 9, 2), SwSwVersion()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemSwUpgradeStatusSwBankBSwVersion.setStatus('current')
systemSwUpgradeStatusSwBankBSwImageFile = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 15, 1, 9, 3), SwSwImageFile()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemSwUpgradeStatusSwBankBSwImageFile.setStatus('current')
systemSwUpgradeStatusSwBankBStatus = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 15, 1, 9, 4), Integer32().subtype(subtypeSpec=SingleValueConstraint(0, 1, 2)).clone(namedValues=NamedValues(("valid", 0), ("corrupt", 1), ("empty", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemSwUpgradeStatusSwBankBStatus.setStatus('current')
systemSwUpgradeFileName = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 15, 2), SwSwImageFile()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemSwUpgradeFileName.setStatus('current')
systemSwUpgradeUsername = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 15, 3), String()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemSwUpgradeUsername.setStatus('current')
systemSwUpgradePassword = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 15, 4), ConfdString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemSwUpgradePassword.setStatus('current')
systemSwUpgradeAction = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 15, 5), SwActionType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemSwUpgradeAction.setStatus('current')
systemConfigFilesStatusTable = MibTable((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 2, 1), )
if mibBuilder.loadTexts: systemConfigFilesStatusTable.setStatus('current')
systemConfigFilesStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 2, 1, 1), ).setIndexNames((1, "NPB-SYSTEM", "systemConfigFilesStatusShowLeafFilename"))
if mibBuilder.loadTexts: systemConfigFilesStatusEntry.setStatus('current')
systemConfigFilesStatusShowLeafFilename = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 2, 1, 1, 1), ConfigLocalFile())
if mibBuilder.loadTexts: systemConfigFilesStatusShowLeafFilename.setStatus('current')
systemConfigFilesStatusShowLeafDate = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 2, 1, 1, 2), String()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemConfigFilesStatusShowLeafDate.setStatus('current')
systemConfigFilesStatusShowLeafSize = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 2, 1, 1, 3), String().subtype(subtypeSpec=ValueSizeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemConfigFilesStatusShowLeafSize.setStatus('current')
systemAaaUsernameTable = MibTable((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 4, 1), )
if mibBuilder.loadTexts: systemAaaUsernameTable.setStatus('current')
systemAaaUsernameEntry = MibTableRow((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 4, 1, 1), ).setIndexNames((1, "NPB-SYSTEM", "systemAaaUsernameName"))
if mibBuilder.loadTexts: systemAaaUsernameEntry.setStatus('current')
systemAaaUsernameName = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 4, 1, 1, 1), AaaName())
if mibBuilder.loadTexts: systemAaaUsernameName.setStatus('current')
systemAaaUsernamePassword = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 4, 1, 1, 2), AaaPassword()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: systemAaaUsernamePassword.setStatus('current')
systemAaaUsernameGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 4, 1, 1, 3), Group()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: systemAaaUsernameGroup.setStatus('current')
systemAaaUsernameRowstatus = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 4, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: systemAaaUsernameRowstatus.setStatus('current')
systemAlarmsAlarmTable = MibTable((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 6, 3), )
if mibBuilder.loadTexts: systemAlarmsAlarmTable.setStatus('current')
systemAlarmsAlarmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 6, 3, 1), ).setIndexNames((0, "NPB-SYSTEM", "systemAlarmsAlarmKey"))
if mibBuilder.loadTexts: systemAlarmsAlarmEntry.setStatus('current')
systemAlarmsAlarmKey = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 6, 3, 1, 1), Unsigned32())
if mibBuilder.loadTexts: systemAlarmsAlarmKey.setStatus('current')
systemAlarmsAlarmLastUpdated = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 6, 3, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemAlarmsAlarmLastUpdated.setStatus('current')
systemAlarmsAlarmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 6, 3, 1, 3), AlarmManagerStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemAlarmsAlarmStatus.setStatus('current')
systemAlarmsAlarmCreation = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 6, 3, 1, 4), String()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemAlarmsAlarmCreation.setStatus('current')
systemAlarmsAlarmClearance = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 6, 3, 1, 5), String()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemAlarmsAlarmClearance.setStatus('current')
systemAlarmsAlarmId = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 6, 3, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemAlarmsAlarmId.setStatus('current')
systemAlarmsAlarmModule = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 6, 3, 1, 7), AlarmModule()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemAlarmsAlarmModule.setStatus('current')
systemAlarmsAlarmSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 6, 3, 1, 8), AlarmSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemAlarmsAlarmSeverity.setStatus('current')
systemAlarmsAlarmMessage = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 6, 3, 1, 9), String().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemAlarmsAlarmMessage.setStatus('current')
systemSecurityAclTable = MibTable((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 7, 1), )
if mibBuilder.loadTexts: systemSecurityAclTable.setStatus('current')
systemSecurityAclEntry = MibTableRow((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 7, 1, 1), ).setIndexNames((1, "NPB-SYSTEM", "systemSecurityAclName"))
if mibBuilder.loadTexts: systemSecurityAclEntry.setStatus('current')
systemSecurityAclName = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 7, 1, 1, 1), AclName())
if mibBuilder.loadTexts: systemSecurityAclName.setStatus('current')
systemSecurityAclIp = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 7, 1, 1, 2), ConfdString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: systemSecurityAclIp.setStatus('current')
systemSecurityAclRowstatus = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 7, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: systemSecurityAclRowstatus.setStatus('current')
systemSyslogRuleTable = MibTable((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 8, 1), )
if mibBuilder.loadTexts: systemSyslogRuleTable.setStatus('current')
systemSyslogRuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 8, 1, 1), ).setIndexNames((1, "NPB-SYSTEM", "systemSyslogRuleName"))
if mibBuilder.loadTexts: systemSyslogRuleEntry.setStatus('current')
systemSyslogRuleName = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 8, 1, 1, 1), String())
if mibBuilder.loadTexts: systemSyslogRuleName.setStatus('current')
systemSyslogRuleDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 8, 1, 1, 2), String()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: systemSyslogRuleDescription.setStatus('current')
systemSyslogRuleEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 8, 1, 1, 3), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: systemSyslogRuleEnabled.setStatus('current')
systemSyslogRuleActionType = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 8, 1, 1, 4), SyslogActionType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: systemSyslogRuleActionType.setStatus('current')
systemSyslogRuleActionLocalFileSettingsImmediateSync = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 8, 1, 1, 5), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: systemSyslogRuleActionLocalFileSettingsImmediateSync.setStatus('current')
systemSyslogRuleActionLocalUserSettingsUsers = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 8, 1, 1, 6), ConfdString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: systemSyslogRuleActionLocalUserSettingsUsers.setStatus('current')
systemSyslogRuleActionRemoteMachineSettingsName = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 8, 1, 1, 7), ConfdString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: systemSyslogRuleActionRemoteMachineSettingsName.setStatus('current')
systemSyslogRuleActionRemoteMachineSettingsTransport = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 8, 1, 1, 8), SyslogTransport().clone('udp')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: systemSyslogRuleActionRemoteMachineSettingsTransport.setStatus('current')
systemSyslogRuleActionRemoteMachineSettingsPort = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 8, 1, 1, 9), UnsignedShort()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: systemSyslogRuleActionRemoteMachineSettingsPort.setStatus('current')
systemSyslogRuleRowstatus = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 8, 1, 1, 10), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: systemSyslogRuleRowstatus.setStatus('current')
systemSyslogRuleSelectorsTable = MibTable((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 2), )
if mibBuilder.loadTexts: systemSyslogRuleSelectorsTable.setStatus('current')
systemSyslogRuleSelectorsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 2, 1), ).setIndexNames((0, "NPB-SYSTEM", "systemSyslogRuleName"), (0, "NPB-SYSTEM", "systemSyslogRuleSelectorsSelectorId"))
if mibBuilder.loadTexts: systemSyslogRuleSelectorsEntry.setStatus('current')
systemSyslogRuleSelectorsSelectorId = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: systemSyslogRuleSelectorsSelectorId.setStatus('current')
systemSyslogRuleSelectorsFacilityList = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 2, 1, 2), ConfdString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: systemSyslogRuleSelectorsFacilityList.setStatus('current')
systemSyslogRuleSelectorsIgnore = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 2, 1, 3), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: systemSyslogRuleSelectorsIgnore.setStatus('current')
systemSyslogRuleSelectorsComparison = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 2, 1, 4), SyslogComparison().clone('sameOrHigher')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: systemSyslogRuleSelectorsComparison.setStatus('current')
systemSyslogRuleSelectorsPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 2, 1, 5), SyslogPriority()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: systemSyslogRuleSelectorsPriority.setStatus('current')
systemSyslogRuleSelectorsRowstatus = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 2, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: systemSyslogRuleSelectorsRowstatus.setStatus('current')
systemTimeAndDateNtpServerTable = MibTable((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 9, 5, 3), )
if mibBuilder.loadTexts: systemTimeAndDateNtpServerTable.setStatus('current')
systemTimeAndDateNtpServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 9, 5, 3, 1), ).setIndexNames((0, "NPB-SYSTEM", "systemTimeAndDateNtpServerId"))
if mibBuilder.loadTexts: systemTimeAndDateNtpServerEntry.setStatus('current')
systemTimeAndDateNtpServerId = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 9, 5, 3, 1, 1), UnsignedShort().subtype(subtypeSpec=ValueRangeConstraint(1, 4)))
if mibBuilder.loadTexts: systemTimeAndDateNtpServerId.setStatus('current')
systemTimeAndDateNtpServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 9, 5, 3, 1, 2), InetAddressIP()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: systemTimeAndDateNtpServerAddress.setStatus('current')
systemTimeAndDateNtpServerPolling = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 9, 5, 3, 1, 3), Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2)).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: systemTimeAndDateNtpServerPolling.setStatus('current')
systemTimeAndDateNtpServerPollMaxInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 9, 5, 3, 1, 4), UnsignedShort().subtype(subtypeSpec=ValueRangeConstraint(10, 17)).clone(10)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: systemTimeAndDateNtpServerPollMaxInterval.setStatus('current')
systemTimeAndDateNtpServerPollMinInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 9, 5, 3, 1, 5), UnsignedShort().subtype(subtypeSpec=ValueRangeConstraint(3, 10)).clone(6)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: systemTimeAndDateNtpServerPollMinInterval.setStatus('current')
systemTimeAndDateNtpServerAuthenticationType = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 9, 5, 3, 1, 6), KeyDigest().clone('none')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: systemTimeAndDateNtpServerAuthenticationType.setStatus('current')
systemTimeAndDateNtpServerKeyid = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 9, 5, 3, 1, 7), UnsignedShort().subtype(subtypeSpec=ValueRangeConstraint(1, 65534))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: systemTimeAndDateNtpServerKeyid.setStatus('current')
systemTimeAndDateNtpServerKeyValue = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 9, 5, 3, 1, 8), ConfdString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: systemTimeAndDateNtpServerKeyValue.setStatus('current')
systemTimeAndDateNtpServerRowstatus = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 9, 5, 3, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: systemTimeAndDateNtpServerRowstatus.setStatus('current')
systemUserMgmtRemoteServerTable = MibTable((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 12, 3), )
if mibBuilder.loadTexts: systemUserMgmtRemoteServerTable.setStatus('current')
systemUserMgmtRemoteServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 12, 3, 1), ).setIndexNames((0, "NPB-SYSTEM", "systemUserMgmtRemoteServerAuthPriority"))
if mibBuilder.loadTexts: systemUserMgmtRemoteServerEntry.setStatus('current')
systemUserMgmtRemoteServerAuthPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 12, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 5)))
if mibBuilder.loadTexts: systemUserMgmtRemoteServerAuthPriority.setStatus('current')
systemUserMgmtRemoteServerAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 12, 3, 1, 2), Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2)).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: systemUserMgmtRemoteServerAdmin.setStatus('current')
systemUserMgmtRemoteServerAuthMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 12, 3, 1, 3), RemoteAuthentication()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: systemUserMgmtRemoteServerAuthMethod.setStatus('current')
systemUserMgmtRemoteServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 12, 3, 1, 4), String()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: systemUserMgmtRemoteServerAddress.setStatus('current')
systemUserMgmtRemoteServerPort = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 12, 3, 1, 5), UnsignedShort()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: systemUserMgmtRemoteServerPort.setStatus('current')
systemUserMgmtRemoteServerKey = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 12, 3, 1, 6), ConfdString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: systemUserMgmtRemoteServerKey.setStatus('current')
systemUserMgmtRemoteServerRowstatus = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 12, 3, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: systemUserMgmtRemoteServerRowstatus.setStatus('current')
systemHwStatusFanTable = MibTable((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 14, 1), )
if mibBuilder.loadTexts: systemHwStatusFanTable.setStatus('current')
systemHwStatusFanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 14, 1, 1), ).setIndexNames((0, "NPB-SYSTEM", "systemHwStatusFanNumber"))
if mibBuilder.loadTexts: systemHwStatusFanEntry.setStatus('current')
systemHwStatusFanNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 14, 1, 1, 1), UnsignedShort())
if mibBuilder.loadTexts: systemHwStatusFanNumber.setStatus('current')
systemHwStatusFanAvailable = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 14, 1, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemHwStatusFanAvailable.setStatus('current')
systemHwStatusFanDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 14, 1, 1, 3), Direction()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemHwStatusFanDirection.setStatus('current')
systemHwStatusFanFrontSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 14, 1, 1, 4), String()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemHwStatusFanFrontSpeed.setStatus('current')
systemHwStatusFanRearSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 14, 1, 1, 5), String()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemHwStatusFanRearSpeed.setStatus('current')
systemHwStatusFanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 14, 1, 1, 6), Integer32().subtype(subtypeSpec=SingleValueConstraint(0, 1, 2)).clone(namedValues=NamedValues(("ok", 0), ("alarm", 1), ("unknown", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemHwStatusFanStatus.setStatus('current')
systemHwStatusFanLastFailureTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 14, 1, 1, 7), String()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemHwStatusFanLastFailureTimestamp.setStatus('current')
systemHwStatusPsuTable = MibTable((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 14, 2), )
if mibBuilder.loadTexts: systemHwStatusPsuTable.setStatus('current')
systemHwStatusPsuEntry = MibTableRow((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 14, 2, 1), ).setIndexNames((0, "NPB-SYSTEM", "systemHwStatusPsuNumber"))
if mibBuilder.loadTexts: systemHwStatusPsuEntry.setStatus('current')
systemHwStatusPsuNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 14, 2, 1, 1), UnsignedShort())
if mibBuilder.loadTexts: systemHwStatusPsuNumber.setStatus('current')
systemHwStatusPsuAvailable = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 14, 2, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemHwStatusPsuAvailable.setStatus('current')
systemHwStatusPsuPsuDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 14, 2, 1, 3), String()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemHwStatusPsuPsuDescr.setStatus('current')
systemHwStatusPsuPowerGood = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 14, 2, 1, 4), StatusType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemHwStatusPsuPowerGood.setStatus('current')
systemHwStatusPsuVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 14, 2, 1, 5), ConfdString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemHwStatusPsuVoltage.setStatus('current')
systemHwStatusPsuCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 14, 2, 1, 6), ConfdString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemHwStatusPsuCurrent.setStatus('current')
systemHwStatusPsuPower = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 14, 2, 1, 7), ConfdString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemHwStatusPsuPower.setStatus('current')
systemHwStatusPsuPsuTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 14, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemHwStatusPsuPsuTemp.setStatus('current')
systemHwStatusPsuPsuOverTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 14, 2, 1, 9), PsuOverType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemHwStatusPsuPsuOverTemp.setStatus('current')
systemHwStatusPsuLastFailureTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 14, 2, 1, 10), String()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemHwStatusPsuLastFailureTimestamp.setStatus('current')
systemHwStatusPsuLowThresholdInVolts = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 14, 2, 1, 11), ConfdString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemHwStatusPsuLowThresholdInVolts.setStatus('current')
systemHwStatusPsuHighThresholdInVolts = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 14, 2, 1, 12), ConfdString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemHwStatusPsuHighThresholdInVolts.setStatus('current')
systemHwStatusTemperatureSensorsTable = MibTable((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 14, 3), )
if mibBuilder.loadTexts: systemHwStatusTemperatureSensorsTable.setStatus('current')
systemHwStatusTemperatureSensorsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 14, 3, 1), ).setIndexNames((0, "NPB-SYSTEM", "systemHwStatusTemperatureSensorsNumber"))
if mibBuilder.loadTexts: systemHwStatusTemperatureSensorsEntry.setStatus('current')
systemHwStatusTemperatureSensorsNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 14, 3, 1, 1), UnsignedShort())
if mibBuilder.loadTexts: systemHwStatusTemperatureSensorsNumber.setStatus('current')
systemHwStatusTemperatureSensorsDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 14, 3, 1, 2), String()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemHwStatusTemperatureSensorsDescr.setStatus('current')
systemHwStatusTemperatureSensorsStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 14, 3, 1, 3), Integer32().subtype(subtypeSpec=SingleValueConstraint(0, 1, 2)).clone(namedValues=NamedValues(("ok", 0), ("alarm", 1), ("unknown", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemHwStatusTemperatureSensorsStatus.setStatus('current')
systemHwStatusTemperatureSensorsTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 14, 3, 1, 4), ConfdString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemHwStatusTemperatureSensorsTemp.setStatus('current')
systemHwStatusTemperatureSensorsHighThresholdInCelsius = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 14, 3, 1, 5), ConfdString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemHwStatusTemperatureSensorsHighThresholdInCelsius.setStatus('current')
systemHwStatusTemperatureSensorsLowThresholdInCelsius = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 14, 3, 1, 6), ConfdString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemHwStatusTemperatureSensorsLowThresholdInCelsius.setStatus('current')
systemHwStatusTemperatureSensorsLastFailureTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 1, 1, 14, 3, 1, 7), String()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemHwStatusTemperatureSensorsLastFailureTimestamp.setStatus('current')
mibBuilder.exportSymbols("NPB-SYSTEM", systemAaaUsernamePassword=systemAaaUsernamePassword, systemSwUpgrade=systemSwUpgrade, RemoteAuthentication=RemoteAuthentication, systemHwStatusPsuPsuDescr=systemHwStatusPsuPsuDescr, systemMgmtPortActMgmtPortActIpv6Address=systemMgmtPortActMgmtPortActIpv6Address, AlarmContext=AlarmContext, HexList=HexList, Direction=Direction, systemTimeAndDateNtpServerAddress=systemTimeAndDateNtpServerAddress, systemSecurityAclTable=systemSecurityAclTable, systemSyslogRuleTable=systemSyslogRuleTable, systemMgmtPortIpv4Address=systemMgmtPortIpv4Address, Timezone=Timezone, SwSwImageFile=SwSwImageFile, StatusType=StatusType, systemConfigFilesStatusShowLeafFilename=systemConfigFilesStatusShowLeafFilename, systemMgmtPortActMgmtPortActIpv4Address=systemMgmtPortActMgmtPortActIpv4Address, systemTimeAndDate=systemTimeAndDate, systemSwUpgradeFileName=systemSwUpgradeFileName, systemMgmtPortActMgmtPortActIpv6Gateway=systemMgmtPortActMgmtPortActIpv6Gateway, systemMgmtPortIpv6Gateway=systemMgmtPortIpv6Gateway, systemDetailsSwVersion=systemDetailsSwVersion, systemTimeAndDateNtpNtpStatusAsString=systemTimeAndDateNtpNtpStatusAsString, systemSyslogRuleSelectorsComparison=systemSyslogRuleSelectorsComparison, systemTimeAndDateNtpServerEntry=systemTimeAndDateNtpServerEntry, systemSyslogRuleDescription=systemSyslogRuleDescription, systemUserMgmtRemoteServerAuthPriority=systemUserMgmtRemoteServerAuthPriority, systemSwUpgradeStatusSwBankA=systemSwUpgradeStatusSwBankA, systemUserMgmtRemoteServerAuthMethod=systemUserMgmtRemoteServerAuthMethod, systemTimeAndDateNtp=systemTimeAndDateNtp, systemHw=systemHw, systemSyslogRuleSelectorsRowstatus=systemSyslogRuleSelectorsRowstatus, systemSyslogRuleActionType=systemSyslogRuleActionType, systemHwStatusPsuPsuTemp=systemHwStatusPsuPsuTemp, systemUserMgmtRemoteServerTable=systemUserMgmtRemoteServerTable, SyslogPriority=SyslogPriority, systemHwStatusTemperatureSensorsNumber=systemHwStatusTemperatureSensorsNumber, systemSyslogRuleEntry=systemSyslogRuleEntry, ConfdString=ConfdString, systemAlarmsAlarmSeverity=systemAlarmsAlarmSeverity, systemConfigFilesStatusShowLeafSize=systemConfigFilesStatusShowLeafSize, AaaPassword=AaaPassword, MgmtPortSpeed=MgmtPortSpeed, systemTimeAndDateNtpServerId=systemTimeAndDateNtpServerId, systemHwStatusPsuEntry=systemHwStatusPsuEntry, systemAlarmsAlarmId=systemAlarmsAlarmId, systemAaaUsernameName=systemAaaUsernameName, systemSyslogRuleSelectorsPriority=systemSyslogRuleSelectorsPriority, SyslogComparison=SyslogComparison, systemSyslog=systemSyslog, systemHwStatusPsuHighThresholdInVolts=systemHwStatusPsuHighThresholdInVolts, AuthprivPass=AuthprivPass, systemHwStatusPsuPsuOverTemp=systemHwStatusPsuPsuOverTemp, systemUserMgmtRemoteServerAdmin=systemUserMgmtRemoteServerAdmin, SyslogTransport=SyslogTransport, systemSwUpgradeStatusSwBankB=systemSwUpgradeStatusSwBankB, systemAlarmsTrap=systemAlarmsTrap, systemAaaUsernameEntry=systemAaaUsernameEntry, AuthProtocol=AuthProtocol, systemAlarmsSyslogEnabled=systemAlarmsSyslogEnabled, systemTimeAndDateNtpServerRowstatus=systemTimeAndDateNtpServerRowstatus, ConfigLocalFile=ConfigLocalFile, systemSwUpgradeStatusActiveSwVersion=systemSwUpgradeStatusActiveSwVersion, systemMgmtPortDhcp=systemMgmtPortDhcp, systemHwStatusFanLastFailureTimestamp=systemHwStatusFanLastFailureTimestamp, SyslogActionType=SyslogActionType, Username=Username, systemMgmtPortIpv6Address=systemMgmtPortIpv6Address, SwActionType=SwActionType, systemMgmtPortActMgmtPortActMac=systemMgmtPortActMgmtPortActMac, KeyDigest=KeyDigest, systemDetailsSwitchVersion=systemDetailsSwitchVersion, systemAlarmsAlarmCreation=systemAlarmsAlarmCreation, systemSyslogRuleActionRemoteMachineSettingsTransport=systemSyslogRuleActionRemoteMachineSettingsTransport, systemTimeAndDateNtpServerKeyValue=systemTimeAndDateNtpServerKeyValue, TrapVer=TrapVer, TimeAndDateSource=TimeAndDateSource, systemConfigFilesStatusTable=systemConfigFilesStatusTable, systemHwStatusPsuPower=systemHwStatusPsuPower, systemAlarmsAlarmModule=systemAlarmsAlarmModule, systemAlarmsAlarmEntry=systemAlarmsAlarmEntry, systemSwUpgradeStatus=systemSwUpgradeStatus, systemSecurityAclName=systemSecurityAclName, systemSwUpgradeStatusSwBankASwVersion=systemSwUpgradeStatusSwBankASwVersion, systemTimeAndDateNtpServerAuthenticationType=systemTimeAndDateNtpServerAuthenticationType, UnsignedByte=UnsignedByte, systemSwUpgradeStatusSwBankAStatus=systemSwUpgradeStatusSwBankAStatus, systemSecurityAclRowstatus=systemSecurityAclRowstatus, systemSwUpgradeAction=systemSwUpgradeAction, systemAlarmsSyslog=systemAlarmsSyslog, systemSyslogRuleActionLocalFileSettingsImmediateSync=systemSyslogRuleActionLocalFileSettingsImmediateSync, systemDetailsModelName=systemDetailsModelName, systemHwStatusPsuLowThresholdInVolts=systemHwStatusPsuLowThresholdInVolts, systemHwStatusTemperatureSensorsTemp=systemHwStatusTemperatureSensorsTemp, AuthAccess=AuthAccess, systemHwStatusFanDirection=systemHwStatusFanDirection, systemHwStatusFanTable=systemHwStatusFanTable, SwUpgradeProgress=SwUpgradeProgress, systemHwStatusPsuNumber=systemHwStatusPsuNumber, system=system, systemUserMgmtRemoteAuthOrder=systemUserMgmtRemoteAuthOrder, systemMib=systemMib, systemLog=systemLog, systemMgmtPortActMgmtPortActLink=systemMgmtPortActMgmtPortActLink, systemHwStatusFanStatus=systemHwStatusFanStatus, systemUserMgmtRemoteServerRowstatus=systemUserMgmtRemoteServerRowstatus, systemLogLevel=systemLogLevel, systemHwStatusTemperatureSensorsEntry=systemHwStatusTemperatureSensorsEntry, systemSecurity=systemSecurity, LedControlOper=LedControlOper, systemConfigFiles=systemConfigFiles, systemHwStatusPsuVoltage=systemHwStatusPsuVoltage, systemHwStatusTemperatureSensorsDescr=systemHwStatusTemperatureSensorsDescr, ConsolePortBaudrate=ConsolePortBaudrate, systemSyslogRuleName=systemSyslogRuleName, systemSyslogRuleActionRemoteMachineSettingsName=systemSyslogRuleActionRemoteMachineSettingsName, systemTimeAndDateNtpAdmin=systemTimeAndDateNtpAdmin, MgmtPortSpeedConfig=MgmtPortSpeedConfig, AclName=AclName, systemHwStatusFanFrontSpeed=systemHwStatusFanFrontSpeed, systemHwStatus=systemHwStatus, systemSwUpgradeStatusActiveSwImageFile=systemSwUpgradeStatusActiveSwImageFile, systemSyslogRuleSelectorsSelectorId=systemSyslogRuleSelectorsSelectorId, systemSyslogRuleSelectorsTable=systemSyslogRuleSelectorsTable, systemSwUpgradeStatusActiveBootBank=systemSwUpgradeStatusActiveBootBank, SyslogFacility=SyslogFacility, systemHwStatusTemperatureSensorsLastFailureTimestamp=systemHwStatusTemperatureSensorsLastFailureTimestamp, SwSwVersion=SwSwVersion, PortDuplex=PortDuplex, systemSyslogRuleSelectorsFacilityList=systemSyslogRuleSelectorsFacilityList, systemTimeAndDateNtpServerPollMaxInterval=systemTimeAndDateNtpServerPollMaxInterval, systemHwStatusTemperatureSensorsHighThresholdInCelsius=systemHwStatusTemperatureSensorsHighThresholdInCelsius, LocalFile=LocalFile, systemDetailsHostname=systemDetailsHostname, systemHwStatusTemperatureSensorsStatus=systemHwStatusTemperatureSensorsStatus, systemAlarmsAlarmMessage=systemAlarmsAlarmMessage, systemSwUpgradeUsername=systemSwUpgradeUsername, systemHwStatusFanNumber=systemHwStatusFanNumber, Authentication=Authentication, systemMgmtPortActMgmtPort=systemMgmtPortActMgmtPort, systemSyslogRuleActionLocalUserSettingsUsers=systemSyslogRuleActionLocalUserSettingsUsers, systemUserMgmtLocalAuthOrder=systemUserMgmtLocalAuthOrder, systemAlarms=systemAlarms, systemSyslogRuleSelectorsEntry=systemSyslogRuleSelectorsEntry, systemConfigFilesStatusEntry=systemConfigFilesStatusEntry, systemMgmtPortActMgmtPortActIpv4Mask=systemMgmtPortActMgmtPortActIpv4Mask, systemHwLocationLed=systemHwLocationLed, systemSwUpgradeStatusSwBankBBank=systemSwUpgradeStatusSwBankBBank, systemDetailsSerialNumber=systemDetailsSerialNumber, systemSyslogRuleEnabled=systemSyslogRuleEnabled, systemAlarmsAlarmStatus=systemAlarmsAlarmStatus, systemNpb2=systemNpb2, InetAddressIP=InetAddressIP, systemTimeAndDatePtp=systemTimeAndDatePtp, systemUserMgmtRemoteServerEntry=systemUserMgmtRemoteServerEntry, systemHwStatusTemperatureSensorsLowThresholdInCelsius=systemHwStatusTemperatureSensorsLowThresholdInCelsius, systemHwStatusPsuCurrent=systemHwStatusPsuCurrent, systemMgmtPortSpeed=systemMgmtPortSpeed, systemConfigFilesStatusShowLeafDate=systemConfigFilesStatusShowLeafDate, systemTimeAndDateNtpServerTable=systemTimeAndDateNtpServerTable, systemUserMgmtRemoteServerAddress=systemUserMgmtRemoteServerAddress, systemAlarmsTrapEnabled=systemAlarmsTrapEnabled, systemTimeAndDateNtpServerPollMinInterval=systemTimeAndDateNtpServerPollMinInterval, systemAaaUsernameTable=systemAaaUsernameTable, PrivProtocol=PrivProtocol, systemDetailsSwitchName=systemDetailsSwitchName, systemAaaUsernameRowstatus=systemAaaUsernameRowstatus, systemUserMgmtRemoteServerKey=systemUserMgmtRemoteServerKey, systemSwUpgradeStatusErrorMessage=systemSwUpgradeStatusErrorMessage, systemSwUpgradeStatusDownloadProgess=systemSwUpgradeStatusDownloadProgess, systemSyslogRuleSelectorsIgnore=systemSyslogRuleSelectorsIgnore, RemoteUrl=RemoteUrl, systemTimeAndDateShowTime=systemTimeAndDateShowTime, systemMgmtPort=systemMgmtPort, systemTimeAndDateCurrentTimeAndDate=systemTimeAndDateCurrentTimeAndDate, systemHwStatusPsuTable=systemHwStatusPsuTable, UnsignedShort=UnsignedShort, systemMgmtPortDuplex=systemMgmtPortDuplex, PYSNMP_MODULE_ID=systemMib, systemMgmtPortActMgmtPortActSpeed=systemMgmtPortActMgmtPortActSpeed, systemSyslogRuleRowstatus=systemSyslogRuleRowstatus, systemSwUpgradeStatusSwBankBSwVersion=systemSwUpgradeStatusSwBankBSwVersion, systemSwUpgradeStatusBootBankCur=systemSwUpgradeStatusBootBankCur, systemMgmtPortActMgmtPortActIpv4Gateway=systemMgmtPortActMgmtPortActIpv4Gateway, PsuOverType=PsuOverType, systemSecurityAclIp=systemSecurityAclIp, systemTimeAndDateNtpServerKeyid=systemTimeAndDateNtpServerKeyid, systemAlarmsAlarmKey=systemAlarmsAlarmKey, AaaName=AaaName, SwBootBank=SwBootBank, systemMgmtPortActMgmtPortActDuplex=systemMgmtPortActMgmtPortActDuplex, systemAaa=systemAaa, systemSwUpgradePassword=systemSwUpgradePassword, systemSwUpgradeStatusSwBankBSwImageFile=systemSwUpgradeStatusSwBankBSwImageFile, systemConsolePort=systemConsolePort, systemMgmtPortIpv4Gateway=systemMgmtPortIpv4Gateway, systemAaaUsernameGroup=systemAaaUsernameGroup, systemUserMgmt=systemUserMgmt, systemHwStatusFanRearSpeed=systemHwStatusFanRearSpeed, systemTimeAndDateShowDate=systemTimeAndDateShowDate, systemHwStatusPsuLastFailureTimestamp=systemHwStatusPsuLastFailureTimestamp, systemHwStatusTemperatureSensorsTable=systemHwStatusTemperatureSensorsTable, UserAuthPriority=UserAuthPriority, AlarmModule=AlarmModule, PortDuplexConfig=PortDuplexConfig, AlarmSeverity=AlarmSeverity, Password=Password, AlarmManagerStatus=AlarmManagerStatus, systemConsolePortCurrentBaudrate=systemConsolePortCurrentBaudrate, systemSecurityAclEntry=systemSecurityAclEntry, systemMgmtPortActMgmtPortActIpv6PrefixLen=systemMgmtPortActMgmtPortActIpv6PrefixLen, systemDetailsCpuType=systemDetailsCpuType, systemHwStatusFanEntry=systemHwStatusFanEntry, systemUserMgmtRemoteServerPort=systemUserMgmtRemoteServerPort, systemDetails=systemDetails, systemSwUpgradeStatusSwBankBStatus=systemSwUpgradeStatusSwBankBStatus, systemTimeAndDatePtpAdmin=systemTimeAndDatePtpAdmin, systemSwUpgradeStatusSwBankABank=systemSwUpgradeStatusSwBankABank, systemUserMgmtRemoteAuth=systemUserMgmtRemoteAuth, systemTimeAndDateNtpServerPolling=systemTimeAndDateNtpServerPolling, SwUpgradeStatus=SwUpgradeStatus, systemAlarmsAlarmLastUpdated=systemAlarmsAlarmLastUpdated, systemTimeAndDateTimeZone=systemTimeAndDateTimeZone, systemMgmtPortIpv4Mask=systemMgmtPortIpv4Mask, systemHwStatusFanAvailable=systemHwStatusFanAvailable, systemAlarmsAlarmTable=systemAlarmsAlarmTable, systemDetailsHwVersion=systemDetailsHwVersion, systemUserMgmtLocalAuth=systemUserMgmtLocalAuth, systemAlarmsAlarmClearance=systemAlarmsAlarmClearance, systemMgmtPortIpv6PrefixLen=systemMgmtPortIpv6PrefixLen, systemHwStatusPsuPowerGood=systemHwStatusPsuPowerGood, systemSwUpgradeStatusUpgradeStatus=systemSwUpgradeStatusUpgradeStatus, systemHwStatusPsuAvailable=systemHwStatusPsuAvailable, Group=Group, systemSyslogRuleActionRemoteMachineSettingsPort=systemSyslogRuleActionRemoteMachineSettingsPort, String=String, systemSwUpgradeStatusSwBankASwImageFile=systemSwUpgradeStatusSwBankASwImageFile)
