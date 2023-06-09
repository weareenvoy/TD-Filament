import sys
sys.path.insert(0,project.folder + '/tdfil/thirdparty/natsort')

import natsort
# debug('needto get natsort implemented in v3...')

class scenemanagerext:
	"""
	sceneext description
	"""
	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp

		self.scene_objects_DAT = op('null_scene_objects_with_selected')


	def Refresh_All_Thumbnails(self):
		Scenecomp = parent.module.par.Scenecomp.eval()
		if Scenecomp == None:
			debug('Scenecomp is invalid, cannot refresh all thumbnails...')
			return
		
		materialCOMPs = Scenecomp.findChildren( parName='Objtype', parValue=op.TDFIL.Type_Group('MATERIAL')[0] )
		for each in materialCOMPs:
			each.Schedule_ThumbnailUpdate(0)
		
		meshCOMPs = Scenecomp.findChildren( parName='Objtype', parValue=op.TDFIL.Type_Group('MESH')[0] )
		for each in meshCOMPs:
			each.Schedule_ThumbnailUpdate(0)

	@property
	def Scene_Objects_DAT(self):
		return self.scene_objects_DAT


	def Outliner_Sort(self, path_strings):

		# return natsort.natsorted(path_strings)
		return natsort.os_sorted(path_strings)