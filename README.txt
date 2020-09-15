To begin the program, I define the main module.

Next, I set the variable "iFile" to open the .txt file and set it to read.

Then I set the variable "oFile" to create a new .txt file and set it to write (will use later in the program).

I then created the "msg" variable,setting "iFile" to read the text indside of the .txt file I'm opening.

Create a for loop to find numbers in msg.
Create an if loop inside the for loopto see if the numbers 0 or 1 are found in msg.
Replace the found numbers (0 and 1) with "" (nothing)

(end of if and for loop)

Write the msg variable into that new file we created ("oFile").

Close that newly written file.

Run main.


*TROUBLESHOOTING:
When I ran, 0's and 1's were gone, but newlines (\n) were being printed out instead of executed into the text file.
Had to change "readlines()" to "read()" in the variable msg so it would read the file correctly.