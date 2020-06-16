// Exports functions from a binary to a set of C files.  Each function that
// ends with ___FILENAME will be exported to FILENAME.c
//@author GW_Ponder
//@category GW_Ponder
//@keybinding
//@menupath
//@toolbar
//

import java.io.BufferedWriter;
import java.io.FileWriter;

import ghidra.app.decompiler.flatapi.FlatDecompilerAPI;
import ghidra.app.script.GhidraScript;
import ghidra.program.model.listing.Function;
import ghidra.program.model.listing.FunctionIterator;
import ghidra.program.model.listing.Listing;

public class SplitExports extends GhidraScript {
    
  @Override
  protected void run() throws Exception {
      
    // Identify directory for files 
    // This example puts them in user's home directory in Windows.
    String path_name = System.getProperty("user.home") + "\\"; 
    
    // create a FlatDecompilerAPI to handle the decompilation
    FlatDecompilerAPI fda = new FlatDecompilerAPI(this);
    
    monitor.setMessage("Selecting functions to export...");
    Listing listing = state.getCurrentProgram().getListing();
    FunctionIterator iter = listing.getFunctions(true);
    
    // While there are more functions and the user hasn't cancelled
    while (iter.hasNext() && !monitor.isCancelled()) {
      // get the next function
      Function func = iter.next();
      
      // get the name of the function
      String func_name = func.getName();
      
      // only export functions that have names that end in ___FILENAME
      // where filename is the name of the file to append the function to
      if (func_name.contains("___") ) {
        println("Found function " + func_name);
        
        String file_name = path_name + func_name.split("___")[1] + ".c";
        println("  Writing to " + file_name);
       
        // Open FILENAME.c for append
        BufferedWriter c_file = new BufferedWriter(
                new FileWriter(file_name, true)); 
    
        // Write the decompiled version of the function
        c_file.write(fda.decompile(func));
        
        // close the function
        c_file.newLine();
        c_file.close();
      }
    }
  }
}