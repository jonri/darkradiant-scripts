__commandName__ = 'CountLoot'
__commandDisplayName__ = 'Count selected loot...'

def execute():
	import darkradiant as dr

	class LootCounter(dr.SelectionVisitor):
		loot_sum = 0
		def visit(self, node):
			entity = node.getEntity()
			if not entity.isNull():
				try:
					self.loot_sum += int(entity.getKeyValue("inv_loot_value"))
				except:
					pass

	counter = LootCounter()
	GlobalSelectionSystem.foreachSelected(counter)

	result = 'Total selected loot: ' + str(counter.loot_sum)
	GlobalDialogManager.createMessageBox('Count Selected Loot Results', result, dr.Dialog.CONFIRM).run()

if __executeCommand__:
	execute()
