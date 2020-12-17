__commandName__ = 'batchExport'
__commandDisplayName__ = 'Export layers as models...'

if __executeCommand__:
    import darkradiant as dr

    class LayerExporter(dr.LayerVisitor):
        basePath = None
        modelFormat = None
        skipDefault = False
        centerObjects = 0
        skipCaulk = 0
        
        def __init__(self, path, modelFormat, skipDefault, centerObjects, skipCaulk):
            super().__init__()
            self.basePath = path
            self.modelFormat = modelFormat
            self.skipDefault = skipDefault == 1
            self.centerObjects = centerObjects
            self.skipCaulk = skipCaulk

        def visit(self, layerID, layerName):
            if self.skipDefault and layerID == 0:
               return
            
            layerVisibility = GlobalLayerManager.layerIsVisible(layerID)
            GlobalLayerManager.setLayerVisibility(layerID, True)
            GlobalSelectionSystem.setSelectedAll(False)
            GlobalLayerManager.setSelected(layerID, True)
            path = '{}/{}.{}'.format(self.basePath, layerName, self.modelFormat)
            #Usage: ExportSelectedAsModel <Path> <ExportFormat> [<CenterObjects>] [<SkipCaulk>] [<ReplaceSelectionWithModel>] [<UseEntityOrigin>] [<ExportLightsAsObjects>]
            exportCommand = 'ExportSelectedAsModel {} {} {} {} 0 0 0'.format(path, self.modelFormat, self.centerObjects, self.skipCaulk)
            print(exportCommand)
            GlobalCommandSystem.execute(exportCommand)
            GlobalLayerManager.setLayerVisibility(layerID, layerVisibility)
            
    dialog = GlobalDialogManager.createDialog(__commandName__)
    pathHandle = dialog.addPathEntry('Save path:', True)
    dialog.setElementValue(pathHandle, GlobalRegistry.get('user/scripts/batchExport/recentPath'))

    #NOTE: the file extension is extracted from the following strings, so they
    #      must be present at the end of the string, in the form "(.ext)".
    modelFormats = dr.StringVector()
    modelFormats.append('ASCII Scene Export (.ase)')
    modelFormats.append('Lightwave Object File (.lwo)')
    modelFormats.append('Wavefront OBJ (.obj)')
    modelFormatHandle = dialog.addComboBox('Output format:', modelFormats)
    dialog.setElementValue(modelFormatHandle, GlobalRegistry.get('user/scripts/batchExport/modelFormat'))
    
    skipDefaultHandle = dialog.addCheckbox('Skip default layer')
    dialog.setElementValue(skipDefaultHandle, GlobalRegistry.get('user/scripts/batchExport/skipDefault'))
    
    centerObjectsHandle = dialog.addCheckbox('Center objects at origin')
    dialog.setElementValue(centerObjectsHandle, GlobalRegistry.get('user/scripts/batchExport/centerObjects'))

    skipCaulkHandle = dialog.addCheckbox('Skip caulked faces')
    dialog.setElementValue(skipCaulkHandle, GlobalRegistry.get('user/scripts/batchExport/skipCaulk'))
    
    if dialog.run() == dr.Dialog.OK:
        path = dialog.getElementValue(pathHandle)
        GlobalRegistry.set('user/scripts/batchExport/recentPath', path)
        
        modelFormat = dialog.getElementValue(modelFormatHandle)
        GlobalRegistry.set('user/scripts/batchExport/modelFormat', modelFormat)
        
        skipDefault = dialog.getElementValue(skipDefaultHandle)
        GlobalRegistry.set('user/scripts/batchExport/skipDefault', skipDefault)
        
        centerObjects = dialog.getElementValue(centerObjectsHandle)
        GlobalRegistry.set('user/scripts/batchExport/centerObjects', centerObjects)

        skipCaulk = dialog.getElementValue(skipCaulkHandle)
        GlobalRegistry.set('user/scripts/batchExport/skipCaulk', skipCaulk)
        
        GlobalLayerManager.foreachLayer(LayerExporter(path, modelFormat[-4:-1], skipDefault, centerObjects, skipCaulk))
