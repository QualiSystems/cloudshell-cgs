#
# PySNMP MIB module NPB-NPB (http://snmplabs.com/pysmi)
# ASN.1 source file://./NPB-NPB.mib
# Produced by pysmi-0.3.4 at Wed Sep 25 12:44:10 2019
# On host MacBook-Pro-anthony.local platform Darwin version 18.7.0 by user anthony
# Using Python version 2.7.10 (default, Feb 22 2019, 21:55:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
cgs, = mibBuilder.importSymbols("CGS", "cgs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, Bits, TimeTicks, Counter64, Unsigned32, ModuleIdentity, Gauge32, iso, ObjectIdentity, IpAddress, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "Bits", "TimeTicks", "Counter64", "Unsigned32", "ModuleIdentity", "Gauge32", "iso", "ObjectIdentity", "IpAddress", "Counter32")
TruthValue, DisplayString, RowStatus, TextualConvention, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "RowStatus", "TextualConvention", "DateAndTime")
npb = ModuleIdentity((1, 3, 6, 1, 4, 1, 47477, 100))
npb.setRevisions(('2016-07-10 00:00',))
if mibBuilder.loadTexts: npb.setLastUpdated('201607100000Z')
if mibBuilder.loadTexts: npb.setOrganization('@ORGANIZATION')
mibBuilder.exportSymbols("NPB-NPB", npb=npb, PYSNMP_MODULE_ID=npb)
