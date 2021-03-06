import sys
from services.spawn import DynamicSpawnGroup
from services.spawn import MobileTemplate
from java.util import Vector

def addDynamicGroup(core):
	dynamicGroup = DynamicSpawnGroup()	
	mobileTemplates = Vector()
	mobileTemplates.add('tusken_raider')
	dynamicGroup.setMobiles(mobileTemplates)
	dynamicGroup.setName('tatooine_tusken_wild')
	dynamicGroup.setMaxSpawns(5)
	dynamicGroup.setMinSpawnDistance(150)
	core.spawnService.addDynamicGroup('tatooine_tusken_wild', dynamicGroup)
	return