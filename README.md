# darkradiant-scripts

A collection of scripts I created for my own mapping workflow.


### batch_export.py
Exports each layer as its own model.  This is helpful if you have a dedicated .map file for creating modules or any other group of related assets.  Simply create one asset on each layer, and name the layer with your desired filename (without the extension).  The batch export will save each layer according to its name, and you can iterate on your assets by making edits, batch exporting, and calling reloadModels.

### find_duplicate_entities.py
If you accidentally copy an entity and move it back on top of the original, it can be hard to find it after the fact.  In-game the model will not z-fight but appear to get lit twice.  Duplicated lights will be twice as bright, duplicated sounds twice as loud, etc.

This script will detect these duplicated entities and select the duplicates for you.  You can delete them straightaway, or use Hide Deselected (ctrl-shift-h) to isolate the duplicates for further inspection.

To be considered a duplicate, two entities must have the same origin, model, classname, and rotation.  The comparison can be extended in the script to include additional spawnargs if there are any cases where this causes false positives.
