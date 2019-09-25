#
# PySNMP MIB module NPB-FILTERS (http://snmplabs.com/pysmi)
# ASN.1 source file://./NPB-FILTERS.mib
# Produced by pysmi-0.3.4 at Wed Sep 25 12:44:11 2019
# On host MacBook-Pro-anthony.local platform Darwin version 18.7.0 by user anthony
# Using Python version 2.7.10 (default, Feb 22 2019, 21:55:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
npb_2, = mibBuilder.importSymbols("NPB-NPB-2", "npb-2")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, Bits, TimeTicks, Counter64, Unsigned32, ModuleIdentity, Gauge32, iso, ObjectIdentity, IpAddress, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "Bits", "TimeTicks", "Counter64", "Unsigned32", "ModuleIdentity", "Gauge32", "iso", "ObjectIdentity", "IpAddress", "Counter32")
TruthValue, DisplayString, RowStatus, TextualConvention, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "RowStatus", "TextualConvention", "DateAndTime")
filtersMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3))
filtersMib.setRevisions(('2015-12-28 00:00',))
if mibBuilder.loadTexts: filtersMib.setLastUpdated('201512280000Z')
if mibBuilder.loadTexts: filtersMib.setOrganization('@ORGANIZATION')
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

class String(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class HexList(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1x:'

class FilterModes(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + SingleValueConstraint(1, 2, 3, 4, 6)
    namedValues = NamedValues(("l2-l4-ipv4", 1), ("l3-l4-ipv4-udf", 2), ("l3-l4-ipv4-ipv6-mpls", 3), ("l3-l4-ipv4-udf-vlb", 4), ("l2-l4-ipv6", 6))

class PacketStartPoint(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + SingleValueConstraint(1, 2, 3)
    namedValues = NamedValues(("l2", 1), ("l3", 2), ("l4", 3))

class L3Ipv4SessionType(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class L4PortType(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class PktLenRange(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class IpFrag(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + SingleValueConstraint(0, 1, 2, 3)
    namedValues = NamedValues(("any", 0), ("first", 1), ("not-first", 2), ("none", 3))

class FilterOperation(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + SingleValueConstraint(0, 1)
    namedValues = NamedValues(("or", 0), ("and", 1))

class L2InnerVlanType(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class L2MplsType(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class L3Ipv4Type(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class L3Ipv6Type(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class UdfTunnel(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + SingleValueConstraint(0, 1, 2, 3, 4, 5, 6)
    namedValues = NamedValues(("gtp-l2tp", 0), ("l2tp", 1), ("none", 2), ("gre", 3), ("gtp-l2tp-ipv4-ipv6", 4), ("gre-ipv6", 5), ("mpls", 6))

class LbListAsString(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class VlanRangeString(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class Capabilities(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + SingleValueConstraint(1023)
    namedValues = NamedValues(("max-num-of-filters", 1023))

class L2VlanType(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class L4PortListRangeType(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class FilterAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + SingleValueConstraint(1, 2, 3)
    namedValues = NamedValues(("redirect", 1), ("drop", 2), ("copy", 3))

class L4PortListMaskType(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class GreInterface(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class TunnelL4PortType(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class VlbSource(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + SingleValueConstraint(0, 1)
    namedValues = NamedValues(("primary", 0), ("secondary", 1))

class UdfPattern(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class VlanAsString(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class PacketOffset(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class L3Ipv6SessionType(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class FilterId(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 1023)

class L3ProtType(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class L4PortListRangeMaskType(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class UdfLeafref(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

filters = MibIdentifier((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1))
filtersMode = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 1), FilterModes()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: filtersMode.setStatus('current')
filtersModes = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: filtersModes.setStatus('current')
filtersUdfWindow = MibIdentifier((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 3))
filtersUdfWindowTunnel = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 3, 1), UdfTunnel()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: filtersUdfWindowTunnel.setStatus('current')
filtersClear = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: filtersClear.setStatus('current')
filterMemory = MibIdentifier((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 2))
filterMemoryAvailableRanges = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 2, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: filterMemoryAvailableRanges.setStatus('current')
filterMemoryUsedRanges = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 2, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: filterMemoryUsedRanges.setStatus('current')
filterMemoryTotalRanges = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 2, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: filterMemoryTotalRanges.setStatus('current')
filterMemoryTotalRangesPerc = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 2, 4), ConfdString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: filterMemoryTotalRangesPerc.setStatus('current')
filterMemoryAvailableFilters = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 2, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: filterMemoryAvailableFilters.setStatus('current')
filterMemoryUsedFilters = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 2, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: filterMemoryUsedFilters.setStatus('current')
filterMemoryTotalFilters = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 2, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: filterMemoryTotalFilters.setStatus('current')
filterMemoryTotalFiltersPerc = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 2, 8), ConfdString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: filterMemoryTotalFiltersPerc.setStatus('current')
filterMemoryAvailableIntFilters = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 2, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: filterMemoryAvailableIntFilters.setStatus('current')
filterMemoryUsedIntFilters = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 2, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: filterMemoryUsedIntFilters.setStatus('current')
filterMemoryTotalIntFilters = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 2, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: filterMemoryTotalIntFilters.setStatus('current')
filterMemoryTotalIntFiltersPerc = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 2, 12), ConfdString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: filterMemoryTotalIntFiltersPerc.setStatus('current')
filterMemoryHwUpdate = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 2, 13), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: filterMemoryHwUpdate.setStatus('current')
filtersFilterTable = MibTable((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5), )
if mibBuilder.loadTexts: filtersFilterTable.setStatus('current')
filtersFilterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1), ).setIndexNames((0, "NPB-FILTERS", "filtersFilterFilterId"))
if mibBuilder.loadTexts: filtersFilterEntry.setStatus('current')
filtersFilterFilterId = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 1), FilterId())
if mibBuilder.loadTexts: filtersFilterFilterId.setStatus('current')
filtersFilterStatsHitsPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: filtersFilterStatsHitsPackets.setStatus('current')
filtersFilterStatsHitsBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: filtersFilterStatsHitsBytes.setStatus('current')
filtersFilterStatsHitsPps = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: filtersFilterStatsHitsPps.setStatus('current')
filtersFilterStatsHitsBps = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: filtersFilterStatsHitsBps.setStatus('current')
filtersFilterUsedHwFilters = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: filtersFilterUsedHwFilters.setStatus('current')
filtersFilterAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 7), Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2)).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterAdmin.setStatus('current')
filtersFilterName = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 8), String().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterName.setStatus('current')
filtersFilterDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 9), String().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterDescription.setStatus('current')
filtersFilterAction = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 10), FilterAction()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterAction.setStatus('current')
filtersFilterOperator = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 11), FilterOperation()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterOperator.setStatus('current')
filtersFilterL2InnerVlanMask = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 12), String()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterL2InnerVlanMask.setStatus('current')
filtersFilterL2MplsLabel1 = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 13), L2MplsType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterL2MplsLabel1.setStatus('current')
filtersFilterL2MplsLabel1Mask = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 14), String()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterL2MplsLabel1Mask.setStatus('current')
filtersFilterL2MplsLabel2 = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 15), L2MplsType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterL2MplsLabel2.setStatus('current')
filtersFilterL2MplsLabel2Mask = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 16), String()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterL2MplsLabel2Mask.setStatus('current')
filtersFilterL2MplsLabel3 = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 17), L2MplsType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterL2MplsLabel3.setStatus('current')
filtersFilterL2MplsLabel3Mask = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 18), String()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterL2MplsLabel3Mask.setStatus('current')
filtersFilterL2MplsLabel4 = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 19), L2MplsType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterL2MplsLabel4.setStatus('current')
filtersFilterL2MplsLabel4Mask = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 20), String()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterL2MplsLabel4Mask.setStatus('current')
filtersFilterL3Dscp = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 21), UnsignedByte().subtype(subtypeSpec=ValueRangeConstraint(1, 63))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterL3Dscp.setStatus('current')
filtersFilterL3PktLen = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 22), PktLenRange()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterL3PktLen.setStatus('current')
filtersFilterL3Ipv4SrcNetmask = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 23), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterL3Ipv4SrcNetmask.setStatus('current')
filtersFilterL3Ipv4DstNetmask = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 24), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterL3Ipv4DstNetmask.setStatus('current')
filtersFilterL3Ipv6SrcPrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 25), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterL3Ipv6SrcPrefix.setStatus('current')
filtersFilterL3Ipv6DstPrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 26), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterL3Ipv6DstPrefix.setStatus('current')
filtersFilterTunnelL2tp = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 27), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterTunnelL2tp.setStatus('current')
filtersFilterTunnelGre = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 28), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterTunnelGre.setStatus('current')
filtersFilterTunnelMpls = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 29), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterTunnelMpls.setStatus('current')
filtersFilterGtpMsgType = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 30), UnsignedByte().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterGtpMsgType.setStatus('current')
filtersFilterGtpTeid = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 31), String()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterGtpTeid.setStatus('current')
filtersFilterGtpTeidMask = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 32), String()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterGtpTeidMask.setStatus('current')
filtersFilterTunnelIpv4SrcNetmask = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 33), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterTunnelIpv4SrcNetmask.setStatus('current')
filtersFilterTunnelIpv4DstNetmask = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 34), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterTunnelIpv4DstNetmask.setStatus('current')
filtersFilterTunnelIpv6SrcPrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 35), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterTunnelIpv6SrcPrefix.setStatus('current')
filtersFilterTunnelIpv6DstPrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 36), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterTunnelIpv6DstPrefix.setStatus('current')
filtersFilterTunnelL4SportMask = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 37), String()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterTunnelL4SportMask.setStatus('current')
filtersFilterTunnelL4DportMask = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 38), String()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterTunnelL4DportMask.setStatus('current')
filtersFilterNot = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 39), ConfdString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterNot.setStatus('current')
filtersFilterL2Ethertype = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 40), String()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterL2Ethertype.setStatus('current')
filtersFilterL2Smac = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 41), HexList().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterL2Smac.setStatus('current')
filtersFilterL2SmacMask = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 42), HexList().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterL2SmacMask.setStatus('current')
filtersFilterL2Dmac = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 43), HexList().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterL2Dmac.setStatus('current')
filtersFilterL2DmacMask = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 44), HexList().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterL2DmacMask.setStatus('current')
filtersFilterL2Vlan = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 45), L2VlanType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterL2Vlan.setStatus('current')
filtersFilterL2InnerVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 46), L2InnerVlanType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterL2InnerVlan.setStatus('current')
filtersFilterL3Frag = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 47), IpFrag()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterL3Frag.setStatus('current')
filtersFilterL3ProtocolNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 48), L3ProtType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterL3ProtocolNumber.setStatus('current')
filtersFilterL3Ipv4Addr = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 49), L3Ipv4Type()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterL3Ipv4Addr.setStatus('current')
filtersFilterL3IpList = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 50), String().subtype(subtypeSpec=ValueSizeConstraint(1, 16))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterL3IpList.setStatus('current')
filtersFilterL3IpSrcList = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 51), String().subtype(subtypeSpec=ValueSizeConstraint(1, 16))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterL3IpSrcList.setStatus('current')
filtersFilterL3IpDstList = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 52), String().subtype(subtypeSpec=ValueSizeConstraint(1, 16))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterL3IpDstList.setStatus('current')
filtersFilterL3Ipv4SrcAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 53), L3Ipv4Type()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterL3Ipv4SrcAddr.setStatus('current')
filtersFilterL3Ipv4DstAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 54), L3Ipv4Type()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterL3Ipv4DstAddr.setStatus('current')
filtersFilterL3Ipv6Addr = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 55), L3Ipv6Type()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterL3Ipv6Addr.setStatus('current')
filtersFilterL3Ipv6SrcAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 56), L3Ipv6Type()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterL3Ipv6SrcAddr.setStatus('current')
filtersFilterL3Ipv6DstAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 57), L3Ipv6Type()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterL3Ipv6DstAddr.setStatus('current')
filtersFilterL4Port = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 58), L4PortType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterL4Port.setStatus('current')
filtersFilterL4Sport = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 59), L4PortType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterL4Sport.setStatus('current')
filtersFilterL4Dport = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 60), L4PortType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterL4Dport.setStatus('current')
filtersFilterL3Ipv4Session = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 61), L3Ipv4SessionType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterL3Ipv4Session.setStatus('current')
filtersFilterL3Ipv4SrcSession = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 62), L3Ipv4SessionType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterL3Ipv4SrcSession.setStatus('current')
filtersFilterL3Ipv4DstSession = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 63), L3Ipv4SessionType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterL3Ipv4DstSession.setStatus('current')
filtersFilterL3Ipv6Session = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 64), L3Ipv6SessionType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterL3Ipv6Session.setStatus('current')
filtersFilterL3Ipv6SrcSession = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 65), L3Ipv6SessionType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterL3Ipv6SrcSession.setStatus('current')
filtersFilterL3Ipv6DstSession = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 66), L3Ipv6SessionType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterL3Ipv6DstSession.setStatus('current')
filtersFilterL4TcpflagUrg = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 67), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterL4TcpflagUrg.setStatus('current')
filtersFilterL4TcpflagAck = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 68), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterL4TcpflagAck.setStatus('current')
filtersFilterL4TcpflagPsh = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 69), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterL4TcpflagPsh.setStatus('current')
filtersFilterL4TcpflagRst = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 70), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterL4TcpflagRst.setStatus('current')
filtersFilterL4TcpflagSyn = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 71), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterL4TcpflagSyn.setStatus('current')
filtersFilterL4TcpflagFin = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 72), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterL4TcpflagFin.setStatus('current')
filtersFilterTunnelGtp = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 73), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterTunnelGtp.setStatus('current')
filtersFilterTunnelProtocolNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 74), L3ProtType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterTunnelProtocolNumber.setStatus('current')
filtersFilterTunnelIpv4Addr = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 75), L3Ipv4Type()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterTunnelIpv4Addr.setStatus('current')
filtersFilterTunnelIpv4SrcAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 76), L3Ipv4Type()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterTunnelIpv4SrcAddr.setStatus('current')
filtersFilterTunnelIpv4DstAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 77), L3Ipv4Type()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterTunnelIpv4DstAddr.setStatus('current')
filtersFilterTunnelIpv6Addr = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 78), L3Ipv6Type()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterTunnelIpv6Addr.setStatus('current')
filtersFilterTunnelIpv6SrcAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 79), L3Ipv6Type()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterTunnelIpv6SrcAddr.setStatus('current')
filtersFilterTunnelIpv6DstAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 80), L3Ipv6Type()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterTunnelIpv6DstAddr.setStatus('current')
filtersFilterTunnelL4Port = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 81), TunnelL4PortType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterTunnelL4Port.setStatus('current')
filtersFilterTunnelL4Sport = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 82), TunnelL4PortType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterTunnelL4Sport.setStatus('current')
filtersFilterTunnelL4Dport = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 83), TunnelL4PortType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterTunnelL4Dport.setStatus('current')
filtersFilterVlanSetOuter = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 84), UnsignedShort().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterVlanSetOuter.setStatus('current')
filtersFilterSetVirtualLb = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 85), VlanRangeString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterSetVirtualLb.setStatus('current')
filtersFilterSetVirtualLbSource = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 86), VlbSource()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterSetVirtualLbSource.setStatus('current')
filtersFilterSmacReplace = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 87), HexList().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterSmacReplace.setStatus('current')
filtersFilterDmacReplace = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 88), HexList().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterDmacReplace.setStatus('current')
filtersFilterInputPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 89), String()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterInputPorts.setStatus('current')
filtersFilterInputInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 90), GreInterface()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterInputInterface.setStatus('current')
filtersFilterOutputPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 91), String()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterOutputPorts.setStatus('current')
filtersFilterOutputLbGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 92), LbListAsString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterOutputLbGroup.setStatus('current')
filtersFilterOutputInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 93), GreInterface()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterOutputInterface.setStatus('current')
filtersFilterRowstatus = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 5, 1, 96), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterRowstatus.setStatus('current')
filtersFilterUdfTable = MibTable((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 3), )
if mibBuilder.loadTexts: filtersFilterUdfTable.setStatus('current')
filtersFilterUdfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 3, 1), ).setIndexNames((0, "NPB-FILTERS", "filtersFilterFilterId"), (1, "NPB-FILTERS", "filtersFilterUdfName"))
if mibBuilder.loadTexts: filtersFilterUdfEntry.setStatus('current')
filtersFilterUdfName = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 3, 1, 1), String().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: filtersFilterUdfName.setStatus('current')
filtersFilterUdfPattern = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 3, 1, 2), UdfPattern()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterUdfPattern.setStatus('current')
filtersFilterUdfMask = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 3, 1, 3), String()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterUdfMask.setStatus('current')
filtersFilterUdfRowstatus = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 3, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersFilterUdfRowstatus.setStatus('current')
filtersIpListTable = MibTable((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 6), )
if mibBuilder.loadTexts: filtersIpListTable.setStatus('current')
filtersIpListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 6, 1), ).setIndexNames((1, "NPB-FILTERS", "filtersIpListListName"))
if mibBuilder.loadTexts: filtersIpListEntry.setStatus('current')
filtersIpListListName = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 6, 1, 1), String().subtype(subtypeSpec=ValueSizeConstraint(1, 16)))
if mibBuilder.loadTexts: filtersIpListListName.setStatus('current')
filtersIpListDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 6, 1, 2), String().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersIpListDescription.setStatus('current')
filtersIpListRowstatus = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 6, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersIpListRowstatus.setStatus('current')
filtersIpListRulesNum = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 6, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: filtersIpListRulesNum.setStatus('current')
filtersUdfWindowUdfTable = MibTable((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 3, 2), )
if mibBuilder.loadTexts: filtersUdfWindowUdfTable.setStatus('current')
filtersUdfWindowUdfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 3, 2, 1), ).setIndexNames((1, "NPB-FILTERS", "filtersUdfWindowUdfName"))
if mibBuilder.loadTexts: filtersUdfWindowUdfEntry.setStatus('current')
filtersUdfWindowUdfName = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 3, 2, 1, 1), String().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: filtersUdfWindowUdfName.setStatus('current')
filtersUdfWindowUdfDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 3, 2, 1, 2), String().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersUdfWindowUdfDescription.setStatus('current')
filtersUdfWindowUdfStartPoint = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 3, 2, 1, 3), PacketStartPoint().clone('l2')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersUdfWindowUdfStartPoint.setStatus('current')
filtersUdfWindowUdfOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 3, 2, 1, 4), PacketOffset().clone('0')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersUdfWindowUdfOffset.setStatus('current')
filtersUdfWindowUdfUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 3, 2, 1, 5), String()).setMaxAccess("readonly")
if mibBuilder.loadTexts: filtersUdfWindowUdfUsed.setStatus('current')
filtersUdfWindowUdfRowstatus = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 3, 1, 3, 2, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filtersUdfWindowUdfRowstatus.setStatus('current')
mibBuilder.exportSymbols("NPB-FILTERS", filtersFilterL2Smac=filtersFilterL2Smac, filtersFilterTunnelIpv6Addr=filtersFilterTunnelIpv6Addr, filters=filters, filtersMode=filtersMode, L3Ipv4SessionType=L3Ipv4SessionType, IpFrag=IpFrag, filtersFilterUsedHwFilters=filtersFilterUsedHwFilters, filtersFilterUdfTable=filtersFilterUdfTable, filtersFilterTunnelMpls=filtersFilterTunnelMpls, filtersFilterL4TcpflagFin=filtersFilterL4TcpflagFin, UdfLeafref=UdfLeafref, GreInterface=GreInterface, filterMemoryTotalRangesPerc=filterMemoryTotalRangesPerc, filtersFilterL2MplsLabel2=filtersFilterL2MplsLabel2, PacketOffset=PacketOffset, filtersFilterL3ProtocolNumber=filtersFilterL3ProtocolNumber, filtersFilterSmacReplace=filtersFilterSmacReplace, filtersIpListListName=filtersIpListListName, VlanRangeString=VlanRangeString, filtersFilterL3PktLen=filtersFilterL3PktLen, PacketStartPoint=PacketStartPoint, filtersFilterL2MplsLabel1Mask=filtersFilterL2MplsLabel1Mask, filtersFilterTunnelL2tp=filtersFilterTunnelL2tp, filterMemoryUsedIntFilters=filterMemoryUsedIntFilters, filtersFilterRowstatus=filtersFilterRowstatus, filtersFilterL3Dscp=filtersFilterL3Dscp, filtersFilterL4Sport=filtersFilterL4Sport, filtersUdfWindowUdfStartPoint=filtersUdfWindowUdfStartPoint, filtersMib=filtersMib, ConfdString=ConfdString, filtersFilterTunnelIpv6SrcAddr=filtersFilterTunnelIpv6SrcAddr, filtersFilterOutputInterface=filtersFilterOutputInterface, filtersFilterL2Dmac=filtersFilterL2Dmac, filtersFilterTunnelGre=filtersFilterTunnelGre, FilterId=FilterId, filtersFilterL3Ipv4SrcAddr=filtersFilterL3Ipv4SrcAddr, L4PortListRangeType=L4PortListRangeType, filtersFilterL3Ipv6DstSession=filtersFilterL3Ipv6DstSession, filtersFilterTunnelIpv6SrcPrefix=filtersFilterTunnelIpv6SrcPrefix, filtersFilterTunnelIpv4DstAddr=filtersFilterTunnelIpv4DstAddr, filtersFilterL3IpDstList=filtersFilterL3IpDstList, filtersFilterL2MplsLabel2Mask=filtersFilterL2MplsLabel2Mask, filtersFilterL3Ipv4Session=filtersFilterL3Ipv4Session, FilterModes=FilterModes, filtersFilterTunnelGtp=filtersFilterTunnelGtp, filtersUdfWindowUdfDescription=filtersUdfWindowUdfDescription, filtersFilterTunnelL4Port=filtersFilterTunnelL4Port, L2InnerVlanType=L2InnerVlanType, filtersClear=filtersClear, filtersFilterL3Ipv6SrcSession=filtersFilterL3Ipv6SrcSession, filtersFilterTunnelIpv6DstAddr=filtersFilterTunnelIpv6DstAddr, PktLenRange=PktLenRange, LbListAsString=LbListAsString, L3Ipv6Type=L3Ipv6Type, filtersFilterL3Ipv4DstAddr=filtersFilterL3Ipv4DstAddr, filtersFilterAction=filtersFilterAction, filtersFilterSetVirtualLb=filtersFilterSetVirtualLb, L4PortListMaskType=L4PortListMaskType, filtersFilterTunnelL4Sport=filtersFilterTunnelL4Sport, filtersFilterGtpTeidMask=filtersFilterGtpTeidMask, filtersUdfWindowUdfEntry=filtersUdfWindowUdfEntry, filterMemoryHwUpdate=filterMemoryHwUpdate, filterMemoryTotalIntFiltersPerc=filterMemoryTotalIntFiltersPerc, PYSNMP_MODULE_ID=filtersMib, filtersFilterL3Ipv4SrcNetmask=filtersFilterL3Ipv4SrcNetmask, filtersFilterTunnelIpv4Addr=filtersFilterTunnelIpv4Addr, UnsignedByte=UnsignedByte, filtersIpListDescription=filtersIpListDescription, filtersFilterL3IpList=filtersFilterL3IpList, filtersFilterTunnelL4DportMask=filtersFilterTunnelL4DportMask, filtersFilterL3Ipv4DstSession=filtersFilterL3Ipv4DstSession, filtersFilterL2MplsLabel1=filtersFilterL2MplsLabel1, filtersFilterTunnelIpv4SrcAddr=filtersFilterTunnelIpv4SrcAddr, filtersUdfWindowTunnel=filtersUdfWindowTunnel, filtersFilterEntry=filtersFilterEntry, L3ProtType=L3ProtType, L4PortListRangeMaskType=L4PortListRangeMaskType, UdfPattern=UdfPattern, filterMemoryUsedRanges=filterMemoryUsedRanges, filtersFilterDescription=filtersFilterDescription, filtersUdfWindowUdfUsed=filtersUdfWindowUdfUsed, filtersFilterNot=filtersFilterNot, filterMemoryTotalRanges=filterMemoryTotalRanges, filtersFilterL2MplsLabel4Mask=filtersFilterL2MplsLabel4Mask, filtersIpListEntry=filtersIpListEntry, filtersFilterTunnelProtocolNumber=filtersFilterTunnelProtocolNumber, filtersFilterL3IpSrcList=filtersFilterL3IpSrcList, filtersFilterL2InnerVlan=filtersFilterL2InnerVlan, filtersFilterUdfPattern=filtersFilterUdfPattern, L3Ipv6SessionType=L3Ipv6SessionType, filtersFilterUdfName=filtersFilterUdfName, filterMemoryAvailableIntFilters=filterMemoryAvailableIntFilters, filtersFilterL3Ipv6SrcAddr=filtersFilterL3Ipv6SrcAddr, filtersIpListRulesNum=filtersIpListRulesNum, filtersFilterUdfEntry=filtersFilterUdfEntry, filterMemoryTotalIntFilters=filterMemoryTotalIntFilters, TunnelL4PortType=TunnelL4PortType, filtersFilterL2InnerVlanMask=filtersFilterL2InnerVlanMask, filtersFilterL4TcpflagAck=filtersFilterL4TcpflagAck, L3Ipv4Type=L3Ipv4Type, filtersUdfWindowUdfRowstatus=filtersUdfWindowUdfRowstatus, filtersFilterL3Ipv4Addr=filtersFilterL3Ipv4Addr, filtersIpListRowstatus=filtersIpListRowstatus, L2VlanType=L2VlanType, filtersFilterL2Ethertype=filtersFilterL2Ethertype, Capabilities=Capabilities, L2MplsType=L2MplsType, UdfTunnel=UdfTunnel, filtersFilterUdfMask=filtersFilterUdfMask, filtersFilterL4TcpflagSyn=filtersFilterL4TcpflagSyn, filtersFilterTunnelIpv6DstPrefix=filtersFilterTunnelIpv6DstPrefix, filtersModes=filtersModes, filtersFilterL3Frag=filtersFilterL3Frag, filtersFilterL3Ipv4SrcSession=filtersFilterL3Ipv4SrcSession, filtersFilterStatsHitsBps=filtersFilterStatsHitsBps, filtersFilterInputPorts=filtersFilterInputPorts, filtersFilterVlanSetOuter=filtersFilterVlanSetOuter, L4PortType=L4PortType, filtersFilterL2MplsLabel4=filtersFilterL2MplsLabel4, HexList=HexList, filtersUdfWindowUdfName=filtersUdfWindowUdfName, filtersFilterStatsHitsPackets=filtersFilterStatsHitsPackets, filterMemoryAvailableRanges=filterMemoryAvailableRanges, filtersFilterL2MplsLabel3Mask=filtersFilterL2MplsLabel3Mask, filterMemory=filterMemory, filterMemoryTotalFilters=filterMemoryTotalFilters, filtersFilterL3Ipv6DstAddr=filtersFilterL3Ipv6DstAddr, VlbSource=VlbSource, filtersFilterTunnelL4SportMask=filtersFilterTunnelL4SportMask, filtersFilterL3Ipv6Session=filtersFilterL3Ipv6Session, filtersFilterStatsHitsPps=filtersFilterStatsHitsPps, filtersFilterOutputPorts=filtersFilterOutputPorts, filterMemoryTotalFiltersPerc=filterMemoryTotalFiltersPerc, filtersFilterL3Ipv4DstNetmask=filtersFilterL3Ipv4DstNetmask, filtersFilterL4Port=filtersFilterL4Port, UnsignedShort=UnsignedShort, filtersFilterL2MplsLabel3=filtersFilterL2MplsLabel3, filtersFilterTunnelIpv4SrcNetmask=filtersFilterTunnelIpv4SrcNetmask, filtersFilterL3Ipv6Addr=filtersFilterL3Ipv6Addr, filtersFilterL4TcpflagRst=filtersFilterL4TcpflagRst, filtersFilterTable=filtersFilterTable, filtersFilterDmacReplace=filtersFilterDmacReplace, filtersFilterOperator=filtersFilterOperator, filtersUdfWindow=filtersUdfWindow, filtersFilterTunnelL4Dport=filtersFilterTunnelL4Dport, filtersFilterL2SmacMask=filtersFilterL2SmacMask, filtersFilterName=filtersFilterName, filtersFilterInputInterface=filtersFilterInputInterface, filtersIpListTable=filtersIpListTable, filtersFilterL4Dport=filtersFilterL4Dport, filtersFilterL3Ipv6DstPrefix=filtersFilterL3Ipv6DstPrefix, filtersFilterL2Vlan=filtersFilterL2Vlan, filtersFilterGtpTeid=filtersFilterGtpTeid, filterMemoryAvailableFilters=filterMemoryAvailableFilters, filterMemoryUsedFilters=filterMemoryUsedFilters, filtersFilterOutputLbGroup=filtersFilterOutputLbGroup, filtersFilterL4TcpflagPsh=filtersFilterL4TcpflagPsh, filtersFilterL3Ipv6SrcPrefix=filtersFilterL3Ipv6SrcPrefix, filtersFilterFilterId=filtersFilterFilterId, filtersFilterAdmin=filtersFilterAdmin, FilterAction=FilterAction, FilterOperation=FilterOperation, filtersUdfWindowUdfOffset=filtersUdfWindowUdfOffset, filtersFilterL4TcpflagUrg=filtersFilterL4TcpflagUrg, filtersFilterStatsHitsBytes=filtersFilterStatsHitsBytes, filtersFilterUdfRowstatus=filtersFilterUdfRowstatus, filtersFilterTunnelIpv4DstNetmask=filtersFilterTunnelIpv4DstNetmask, filtersUdfWindowUdfTable=filtersUdfWindowUdfTable, VlanAsString=VlanAsString, String=String, filtersFilterSetVirtualLbSource=filtersFilterSetVirtualLbSource, filtersFilterL2DmacMask=filtersFilterL2DmacMask, filtersFilterGtpMsgType=filtersFilterGtpMsgType)
