# SummerProject2018

Use the Espresso Performance Monitor to study tagging performance in bins 
of some variable.

This package enables the EPM to be run over bins of equal bin statistics.
The EPM is run twice, once to produce the calibration parameters for the 
individual taggers and combine the OS taggers using the even/odd events,
and a second time to calibrate the taggers and combine the OS and SS taggers
using the odd/even events. Directories labelled Calib_Bin_no_even/odd
and Comb_Bin_no_odd/even are created with the results from each EPM run.

histbins2.py defines a function called binboundaries which inputs a histogram
and a desired number of bins and return the bin boundaries for bins of equal
statistics.

EPMoptsTemplate.py is the template for the option file used in the EPM runs.
replacement.py contains two functions; dict which defines the replacements 
for the template, and process which applies the replacements and writes them
to an option file.

job.py combines the functions from above to run the EPM in the specified 
directories for the bins within the bin boundaries. Therefore, to run this
package only the job.py script must be modifed by:

1. Choosing the desired root file and histogram 
2. Define the changes to the template. It should be noted that the default
setting is chosen such that the EPM runs twice as stated above
3. Ensure the path to the EPM is correct in the lines where the EPM is run
4. Run job.py

To create the final graphs, FinalGraphs.py is run, which uses out2.py to extract
the tagging power values from the out.log files of each EPM run.
