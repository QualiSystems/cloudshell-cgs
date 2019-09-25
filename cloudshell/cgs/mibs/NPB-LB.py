#
# PySNMP MIB module NPB-LB (http://snmplabs.com/pysmi)
# ASN.1 source file://./NPB-LB.mib
# Produced by pysmi-0.3.4 at Wed Sep 25 12:44:10 2019
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
lbMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 47477, 100, 2, 4))
lbMib.setRevisions(('2015-12-28 00:00',))
if mibBuilder.loadTexts: lbMib.setLastUpdated('201512280000Z')
if mibBuilder.loadTexts: lbMib.setOrganization('@ORGANIZATION')
class ConfdString(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class String(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class LbFailover(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + SingleValueConstraint(1, 2)
    namedValues = NamedValues(("active", 1), ("standby", 2))

class LbOverload(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + SingleValueConstraint(1, 2)
    namedValues = NamedValues(("drop", 1), ("re-hash", 2))

class LbHashParam(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17)
    namedValues = NamedValues(("lb-5-tuple", 1), ("smac", 2), ("dmac", 3), ("vlan", 4), ("ethertype", 5), ("ip-addr", 6), ("ip-dst-addr", 7), ("ip-protocol-number", 8), ("l4-port", 9), ("l4-dport", 10), ("l2-all", 11), ("mpls", 12), ("gtp-teid", 13), ("ip-src-addr", 14), ("l4-sport", 15), ("in-port", 16), ("lb-4-tuple", 17))

class LbAlgo(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + SingleValueConstraint(1, 2, 3, 4, 5)
    namedValues = NamedValues(("hash", 1), ("round-robin", 2), ("ip-src-addr", 3), ("ip-dst-addr", 4), ("hash-gtp-ip", 5))

lb = MibIdentifier((1, 3, 6, 1, 4, 1, 47477, 100, 2, 4, 1))
lbInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 47477, 100, 2, 4, 1, 1))
lbHash = MibIdentifier((1, 3, 6, 1, 4, 1, 47477, 100, 2, 4, 1, 2))
lbHashHash = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 4, 1, 2, 1), ConfdString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lbHashHash.setStatus('current')
lbHashSymmetric = MibScalar((1, 3, 6, 1, 4, 1, 47477, 100, 2, 4, 1, 2, 2), Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2)).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lbHashSymmetric.setStatus('current')
lbGroupTable = MibTable((1, 3, 6, 1, 4, 1, 47477, 100, 2, 4, 1, 3), )
if mibBuilder.loadTexts: lbGroupTable.setStatus('current')
lbGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 47477, 100, 2, 4, 1, 3, 1), ).setIndexNames((0, "NPB-LB", "lbGroupLbId"))
if mibBuilder.loadTexts: lbGroupEntry.setStatus('current')
lbGroupLbId = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 4, 1, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 99)))
if mibBuilder.loadTexts: lbGroupLbId.setStatus('current')
lbGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 4, 1, 3, 1, 2), String().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lbGroupName.setStatus('current')
lbGroupDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 4, 1, 3, 1, 3), String().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lbGroupDescription.setStatus('current')
lbGroupAlgo = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 4, 1, 3, 1, 4), LbAlgo().clone('hash')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lbGroupAlgo.setStatus('current')
lbGroupOutputs = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 4, 1, 3, 1, 5), String()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lbGroupOutputs.setStatus('current')
lbGroupOverload = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 4, 1, 3, 1, 6), LbOverload().clone('re-hash')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lbGroupOverload.setStatus('current')
lbGroupFailoverHoldtime = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 4, 1, 3, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 10000))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lbGroupFailoverHoldtime.setStatus('current')
lbGroupStandby = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 4, 1, 3, 1, 8), String()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lbGroupStandby.setStatus('current')
lbGroupStandbyFailover = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 4, 1, 3, 1, 9), LbFailover().clone('standby')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lbGroupStandbyFailover.setStatus('current')
lbGroupShowActivePorts = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 4, 1, 3, 1, 10), String()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lbGroupShowActivePorts.setStatus('current')
lbGroupTouch = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 4, 1, 3, 1, 11), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lbGroupTouch.setStatus('current')
lbGroupRowstatus = MibTableColumn((1, 3, 6, 1, 4, 1, 47477, 100, 2, 4, 1, 3, 1, 13), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lbGroupRowstatus.setStatus('current')
mibBuilder.exportSymbols("NPB-LB", LbOverload=LbOverload, lbGroupOutputs=lbGroupOutputs, lbMib=lbMib, lbGroupShowActivePorts=lbGroupShowActivePorts, lbHash=lbHash, lbGroupStandbyFailover=lbGroupStandbyFailover, lbGroupStandby=lbGroupStandby, lbHashSymmetric=lbHashSymmetric, lbHashHash=lbHashHash, lbGroupName=lbGroupName, lbInfo=lbInfo, lbGroupEntry=lbGroupEntry, lbGroupTouch=lbGroupTouch, lbGroupTable=lbGroupTable, LbAlgo=LbAlgo, lbGroupAlgo=lbGroupAlgo, lbGroupFailoverHoldtime=lbGroupFailoverHoldtime, ConfdString=ConfdString, lbGroupRowstatus=lbGroupRowstatus, PYSNMP_MODULE_ID=lbMib, lb=lb, String=String, lbGroupLbId=lbGroupLbId, LbHashParam=LbHashParam, LbFailover=LbFailover, lbGroupDescription=lbGroupDescription, lbGroupOverload=lbGroupOverload)
