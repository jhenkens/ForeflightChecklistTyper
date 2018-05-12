# ForeflightChecklistTyper
This project uses an iOS App called AirType in order to enter ForeFlight checklists from a CSV into the app.

Unless I am currently mistaken (May 10th, 2018) Foreflight does not let one edit checklists on a computer, to reimport back into the app.

With this, you install AirType, Edit the python script to have your iPad's IP address then make a new CheckList List (the "+ New List" buton, which then takes you to the list with "+ New Detail Item" and "+ New Check Item").

Once you are there, run the python script, tap New Check Item, and then it will fill out the first field. Tap the response, then the notes, waiting for the "AirType" icon to appear on the keyboard each time indicating a connection.

You should see fields populating. Sometimes the python script will propt you to switch to new detail item, press return, then back to new check item, and press return.


The way the code automatically fills out each field is that the iOS keyboard closes the connection each time you change fields.

Thus, the python code monitors the health of its connection, and when the connection is closed, it knows that soon a new connection will be available, on a new field.

Obviously super hacky, but it helped me. Maybe it can help or inspire you too.
