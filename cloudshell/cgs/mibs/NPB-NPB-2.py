#
# PySNMP MIB module NPB-NPB-2 (http://snmplabs.com/pysmi)
# ASN.1 source file://./NPB-NPB-2.mib
# Produced by pysmi-0.3.4 at Wed Sep 25 12:44:11 2019
# On host MacBook-Pro-anthony.local platform Darwin version 18.7.0 by user anthony
# Using Python version 2.7.10 (default, Feb 22 2019, 21:55:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
npb, = mibBuilder.importSymbols("NPB-NPB", "npb")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, Bits, TimeTicks, Counter64, Unsigned32, ModuleIdentity, Gauge32, iso, ObjectIdentity, IpAddress, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "Bits", "TimeTicks", "Counter64", "Unsigned32", "ModuleIdentity", "Gauge32", "iso", "ObjectIdentity", "IpAddress", "Counter32")
TruthValue, DisplayString, RowStatus, TextualConvention, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "RowStatus", "TextualConvention", "DateAndTime")
npb_2 = ModuleIdentity((1, 3, 6, 1, 4, 1, 47477, 100, 2)).setLabel("npb-2")
npb_2.setRevisions(('2016-07-10 00:00',))
if mibBuilder.loadTexts: npb_2.setLastUpdated('201607100000Z')
if mibBuilder.loadTexts: npb_2.setOrganization('@ORGANIZATION')
mibBuilder.exportSymbols("NPB-NPB-2", npb_2=npb_2, PYSNMP_MODULE_ID=npb_2)
