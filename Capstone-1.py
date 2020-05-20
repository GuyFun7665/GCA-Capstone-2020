#TODO write a description for this script
#@author Scott Matheson, Shayne Gradwell, Tyson Jamison
#@category _NEW_
#@keybinding 
#@menupath 
#@toolbar 


#TODO Add User Code Here

testString = "Hello World"
print(testString)

def getProgramInfo()
	program_name = currentProgram.getName()
	creation_date = currentProgram.getCreationDate()
	language_id = currentProgram.getLanguageID()
	compiler_spec_id = currentProgram.getCompilerSpec().getCompilerSpecID()
	print "%s: %s_%s (%s)\n" % (program_name, language_id, compiler_spec_id, creation_date)

def getMemoryLayout()
	print "Memory layout:"
	print "Imagebase: " + hex(currentProgram.getImageBase().getOffset())
	for block in getMemoryBlocks():
   		start = block.getStart().getOffset()
		end = block.getEnd().getOffset()
    		print "%s [start: 0x%x, end: 0x%x]" % (block.getName(), start, end)

def getNextFunction()
	function = getFirstFunction()
	while function is not None:
   		print function.getName()
		function = getFunctionAfter(function)

def getCurrentAddress()
	print "Current location: " + hex(currentLocation.getAddress().getOffset())

def getUserInput()
	val = askString("Please input something: ")
	print val

def popUp()
	popup("Something")

def addComment()
	minAddress = currentProgram.getMinAddress()
	listing = currentProgram.getListing()
	codeUnit = listing.getCodeUnitAt(minAddress)
	codeUnit.setComment(codeUnit.PLATE_COMMENT, "This is an added comment!")

def getDataType()
	from ghidra.app.util.datatype import DataTypeSelectionDialog
	from ghidra.util.data.DataTypeParser import AllowedDataTypes
	tool = state.getTool()
	dtm = currentProgram.getDataTypeManager()
	selectionDialog = DataTypeSelectionDialog(tool, dtm, -1, AllowedDataTypes.FIXED_LENGTH)
	tool.showDialog(selectionDialog)
	dataType = selectionDialog.getUserChosenDataType()
	if dataType != None: print "Chosen data type: " + str(dataType)

def reportProgress()
	import time
	monitor.initialize(10)
	for i in range(10):
		monitor.checkCanceled() # check to see if the user clicked cancel
		time.sleep(1) # pause a bit so we can see progress
		monitor.incrementProgress(1) # update the progress
		monitor.setMessage("Working on " + str(i)) # update the status message