#------------------------------------------#
# Title: IO Classes
# Desc: A Module for IO Classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Extended functionality to add tracks
# joeprado, 2020-Mar-29, Completed ToDos
# joeprado, 2020-Mar-29, Conducted further troubleshooting of code. Made appropariate edits. 
# joeprado, 2020-Mar-29, Updated and added to docstrings.
#------------------------------------------#

if __name__ == '__main__':
    raise Exception('This file is not meant to run by itself')

import DataClasses as DC
import ProcessingClasses as PC

class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name (list), lst_Inventory): -> None
        load_inventory(file_name (list)): -> (a list of CD objects)

    """
    @staticmethod
    def save_inventory(list_Of_File_Names: list, lst_Inventory: list) -> None:
        """
        Args:
            file_name (list): list of file names [CD Inventory, Track Inventory] that hold the data.
            lst_Inventory (list): list of CD objects.

        Returns:
            None.
        """

        # Putting file names into a list. 
        file_name_CD = list_Of_File_Names[0]
        file_name_trk = list_Of_File_Names[1]
        try:
            with open(file_name_CD, 'w') as file:
                for disc in lst_Inventory:
                    file.write(disc.get_record())
            with open(file_name_trk, 'w') as file:
                for disc in lst_Inventory:
                    cd_tracks = disc.tracks
                    disc_id = disc.cd_id
                    for track in cd_tracks:
                        if track is not None:
                            file.write('{},{}'.format(disc_id, track.get_record()))
        except Exception as e: 
            print('There was a general error!', e, e.__doc__, type(e), sep='\n')


    @staticmethod
    def load_inventory(list_Of_File_Names: list) -> list:
        
        """Function to manage data ingestion from list of files to a list of CD objects and a list of track Objects.

        Args:
            file_name (list): list of file names [CD Inventory, Track Inventory] that hold the data.

        Returns:
            list: list of CD objects.

        """

        lst_Inventory = []  #clear list in runtime 
        file_name_CD = list_Of_File_Names[0]
        file_name_trk = list_Of_File_Names[1]
        try:
            with open(file_name_CD, 'r') as file:
                for line in file:
                    data = line.strip().split(',')
                    row = DC.CD(data[0], data[1], data[2])
                    lst_Inventory.append(row)
            with open(file_name_trk, 'r') as file:
                for line in file:
                    data = data = line.strip().split(',')
                    cd = PC.DataProcessor.select_cd(lst_Inventory, int(data[0]))
                    track = DC.Track(int(data[1]), data[2], data[3])
                    cd.add_track(track)
        except Exception as e:
            print('There was a general error!', e, e.__doc__, type(e), sep='\n')
        return lst_Inventory

class ScreenIO:
    """Handling Input / Output
    
    Methods:
        print_menu(): Displays a menu of choices to the user
        menu_choice(): Gets user input for menu selection
        print_CD_menu(): Displays a sub menu of choices for CD / Album to the user
        menu_CD_choice(): Gets user input for CD sub menu selection
        show_inventory(table): Displays current inventory table
        show_tracks(CD(object)): Displays the Tracks on a CD / Album
        get_CD_info(): function to request CD information from User to add CD to inventory
        get_track_info(): function to request Track information from User to add Track to CD / Album
    """
    
    

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Main Menu\n\n[l] load Inventory from file\n[a] Add CD / Album\n[d] Display Current Inventory')
        print('[c] Choose CD / Album\n[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, d, c, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'd', 'c', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, d, c, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def print_CD_menu():
        """Displays a sub menu of choices for CD / Album to the user

        Args:
            None.

        Returns:
            None.
        """

        print('CD Sub Menu\n\n[a] Add track\n[d] Display cd / Album details\n[r] Remove track\n[x] exit to Main Menu')

    @staticmethod
    def menu_CD_choice():
        """Gets user input for CD sub menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices a, d, r or x

        """
        choice = ' '
        while choice not in ['a', 'd', 'r', 'x']:
            choice = input('Which operation would you like to perform? [a, d, r or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table


        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print(row)
        print('======================================')

    @staticmethod
    def show_tracks(cd):
        """Displays the Tracks on a CD / Album

        Args:
            cd (CD): CD object.

        Returns:
            None.

        """
        print('====== Current CD / Album: ======')
        print(cd)
        print('=================================')
        print(cd.get_tracks())
        print('=================================')

    @staticmethod
    def get_CD_info():
        """function to request CD information from User to add CD to inventory
        
        Args:
            None.


        Returns:
            cdId (string): Holds the ID of the CD dataset.
            cdTitle (string): Holds the title of the CD.
            cdArtist (string): Holds the artist of the CD.

        """

        cdId = input('Enter ID: ').strip()
        cdTitle = input('What is the CD\'s title? ').strip()
        cdArtist = input('What is the Artist\'s name? ').strip()
        return cdId, cdTitle, cdArtist

    @staticmethod
    def get_track_info():
        """function to request Track information from User to add Track to CD / Album
        
        Args:
            None.

        Returns:
            trkId (string): Holds the ID of the Track dataset.
            trkTitle (string): Holds the title of the Track.
            trkLength (string): Holds the length (time) of the Track.

        """

        trkId = input('Enter Position on CD / Album: ').strip()
        trkTitle = input('What is the Track\'s title? ').strip()
        trkLength = input('What is the Track\'s length? ').strip()
        return trkId, trkTitle, trkLength

