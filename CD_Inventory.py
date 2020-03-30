#------------------------------------------#
# Title: CD_Inventory.py
# Desc: The CD Inventory App main Module
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Extended functionality to add tracks
# joeprado, 2020-Mar-29, Completed ToDos
# joeprado, 2020-Mar-29, Futher script troubleshooting
#------------------------------------------#

import ProcessingClasses as PC
import IOClasses as IO

lstFileNames = ['AlbumInventory.txt', 'TrackInventory.txt']
lstOfCDObjects = IO.FileIO.load_inventory(lstFileNames) # When program starts, calls function that reads in the currently saved Inventory from a list of two text files 

while True:
    IO.ScreenIO.print_menu() #Display Menu to user and get choice
    strChoice = IO.ScreenIO.menu_choice() # Process menu selection

    if strChoice == 'x': #user selection to exit program
        break
    if strChoice == 'l':  ##Process user input
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled.  ')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            lstOfCDObjects = IO.FileIO.load_inventory(lstFileNames) #Calls function that reads in currently saved inventory from from a list of two text files.
            IO.ScreenIO.show_inventory(lstOfCDObjects) #Calls function that displays inventory to user
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.ScreenIO.show_inventory(lstOfCDObjects) #Calls function that displays inventory to user
        continue  # start loop back at top.
    elif strChoice == 'a': #Process user input
        tplCdInfo = IO.ScreenIO.get_CD_info() # Gets user input for CD info
        PC.DataProcessor.add_CD(tplCdInfo, lstOfCDObjects) # Creates CD object and appends to table of CD objects
        IO.ScreenIO.show_inventory(lstOfCDObjects) #Calls function that displays inventory to user
        continue  # start loop back at top.
    elif strChoice == 'd': #Process user input
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 'c': #Process user input
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        cd_idx = input('Select the CD / Album index: ')
        cd = PC.DataProcessor.select_cd(lstOfCDObjects, cd_idx)
        while True: 
            IO.ScreenIO.print_CD_menu()
            strChoice = IO.ScreenIO.menu_CD_choice()
            if strChoice == 'x': #Process user input
                break  
            elif strChoice == 'a': #Process user input, user selection to exit program
                track_info_tupl = IO.ScreenIO.get_track_info() #Get user input for track info
                PC.DataProcessor.add_track(track_info_tupl, cd) #Creates track object and appends to list of track objects within CD objects. 
            elif strChoice == 'd': #Process user input 
                IO.ScreenIO.show_tracks(cd) #displays tracks for a given CD
            elif strChoice == 'r': #Process user input
                IO.ScreenIO.show_tracks(cd) #displays tracks for a given CD
                chosen_track = int(input("Select the track to delete."))
                cd.rmv_track(chosen_track) # Removes selelcted track from CD  
            else: 
                print('Invalid selection. Back to main menu')
            continue  # start loop back at top.
    elif strChoice == 's': #Process user input
        IO.ScreenIO.show_inventory(lstOfCDObjects) #Calls function that displays inventory to user
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower() #Confirms that user wants to save inventories. 
        if strYesNo == 'y':
            IO.FileIO.save_inventory(lstFileNames, lstOfCDObjects) #Calls function that saves CD and track inventories to two text files. 
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    else:
        print('General Error')  # catch-all should not be possible, as user choice gets vetted in IO, but to be safe: