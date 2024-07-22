This is my 3rd miniproject! Honestly, this was a tough one due to having to relate multiple classes together, inheriting and anticipating and fixing related issues. But, it's in a good spot right now at the end of it.

Changes:  
1. Fixed menu selection bugs when choosing out of bounds options
2. Changed error codes in search_dict and askMenu functions to allow for better error handling  
3. Added quit to menu option in search_dict
4. Search_dict now also allows for retries if an error is run into until the user succeeds or decides to return to menu

You can:  
1. Add books, users, authors and genres  
2. Check and return books for different users  
3. Display info on books, users, authors and generes as well as what books a user has checked out  
4. Save your data for later automatic importing  

Program behavior notes:  
1. It will start the program by checking if there is a library folder or not. If there is it'll import from that folder, else it'll switch to the default data provided.  
2. You can navigate by entering the requested information within the CLI, such as numbers to navigate.  
3. There is a quit to menu option in every menu except the top menu, which instead allows for save and quit or just quitting.
4. Make sure to save after each use! It will create the backup folders automatically.
5. If you want to use an older backup of a file, just copy and replace the current file with the old one.  

Future updates:  
1. Checks are needed to ensure that not only the library folder is being checked, but also the individual files within so that it does not import nothing.  
2. Late fees.  
3. Reservation system.  
4. Automatic backups. 
5. Backup restoration from the CLI.  
6. Fixing the way borrowed ISBNs are stored so that the graceful_set is not needed.