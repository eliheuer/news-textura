# Builds a new designspace file
import os
from fontTools.designspaceLib import DesignSpaceDocument, AxisDescriptor, SourceDescriptor, InstanceDescriptor
root = os.getcwd()
doc = DesignSpaceDocument()
familyName = "NewsTextura"

#------
# axes
#------

axis = AxisDescriptor()
axis.maximum = 144
axis.minimum = 9
axis.default = 9
axis.name = "opsz"
axis.tag = "opsz"
doc.addAxis(axis)

#---------
# masters
#---------

s0 = SourceDescriptor()
s0.path = "MutatorSansLightCondensed.ufo"
s0.name = "master.MutatorMathTest.LightCondensed.0"
s0.familyName = familyName
s0.styleName = "LightCondensed"
s0.location = dict(weight=0, width=0)
s0.copyLib = True
s0.copyInfo = True
s0.copyGroups = True
s0.copyFeatures = True
doc.addSource(s0)

s1 = SourceDescriptor()
s1.path = "MutatorSansBoldCondensed.ufo"
s1.name = "master.MutatorMathTest.BoldCondensed.1"
s1.familyName = familyName
s1.styleName = "BoldCondensed"
s1.location = dict(weight=1000, width=0)
doc.addSource(s1)

s2 = SourceDescriptor()
s2.path = "MutatorSansLightWide.ufo"
s2.name = "master.MutatorMathTest.LightWide.2"
s2.familyName = familyName
s2.styleName = "LightWide"
s2.location = dict(weight=0, width=1000)
doc.addSource(s2)

s3 = SourceDescriptor()
s3.path = "MutatorSansBoldWide.ufo"
s3.name = "master.MutatorMathTest.BoldWide.3"
s3.familyName = familyName
s3.styleName = "BoldWide"
s3.location = dict(weight=1000, width=1000)
doc.addSource(s3)

#-----------
# instances
#-----------

i0 = InstanceDescriptor()
i0.name = 'instance_LightCondensed'
i0.familyName = familyName
i0.styleName = "Medium"
i0.path = os.path.join(root, "instances", "MutatorSansTest-Medium.ufo")
i0.location = dict(weight=500, width=327)
i0.kerning = True
i0.info = True
doc.addInstance(i0)

#-------
# rules
#-------

# TODO: add rules to match the contents of `MutatorSans.designspace`
# http://github.com/LettError/mutatorSans/blob/master/MutatorSans.designspace

#--------
# saving
#--------

path = os.path.join(root, "MutatorSans__test123__.designspace")
doc.write(path)
