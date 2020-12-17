# darkradiant-scripts

A collection of scripts I created for my own mapping workflow.


### batch_export.py
Exports each layer as its own model.  This is helpful if you have a dedicated .map file for creating modules or any other group of related assets.  Simply create one asset on each layer, and name the layer with your desired filename (without the extension).  The batch export will save each layer according to its name, and you can iterate on your assets by making edits, batch exporting, and calling reloadModels.
