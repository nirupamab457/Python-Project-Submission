2.	Code Explanation Step by step:
Importing Required Libraries and Modules
 
•	customtkinter: Custom libraries for creating GUIs in Python.
•	subprocess: Used here to open files using system commands.
•	selenium: Required for automating web interactions, used here to scrape IMDb.
•	pandas: Essential for data manipulation, specifically handling data frames.
•	tkinter and ttk: Standard libraries for creating GUIs in Python.

display_details(df, file_name) Function
 
•	Function Purpose: Displays a GUI window (display_root) showing the top 10 movies with their ratings in a table format.
•	Components:
o	Treeview (table): Displays the data in a tabular format with columns for serial number (slno), movie name (name), and movie rating (rating).
o	Buttons:
 
	Close Button: Destroys the current window (display_root).
	New Extraction Button: Closes the current window and opens the genre and language selection window (select_genre_language()).
	View More Button: Opens the saved Excel file using the default system application.

select_genre_language() Function

	Function Purpose: Displays a GUI window (root) for selecting a movie genre and language.
	Components:
 
o	Frames (genre_frame and language_frame): Organize widgets for genre selection and language selection.
 
o	Labels (genre_lebel and language_lebel): Display text labels for indicating the purpose of dropdowns.
o	Combo Boxes (genre_option and language_option): Dropdown menus for selecting genre and language.
o	Buttons:
	Enter Genre Button (enter_genre_btn) and Enter Language Button (enter_language_btn): Allow users to enter custom genres and languages.
 
	Extract Button (ext_button): Initiates data extraction based on selected genre and language.
	Close Button (close_button): Closes the current window (root).

scrape_movies(genre, language) Function
	 
	Selenium Setup: Initializes Selenium WebDriver with Chrome options.
 
	Language Tags: Dictionary to map languages to their respective IMDb URL tags.
	URL Construction: Constructs the URL based on selected genre and language.
 
	Web Scraping:
o	Opens the constructed URL.
o	Extracts movie titles, years, ratings, and descriptions using XPath.
o	Handles missing data with try-except blocks.
	Data Handling:
 
	Stores extracted data in a Pandas DataFrame.
	Saves the DataFrame to an Excel file.
	Calls display_details() to show the top 10 movies.
 
3.	Output

Initial dialog box pops up after running the code

 


Select the genre and language from the dropdowns. You can enter them manually by clicking on the “enter a genre” and “enter a language” buttons respectively.

 

Genre selection is mandatory as proceeding without it will show error

 

The first out put contains a tabular view of the top 10 movies from the selected genre.

 

The “New Extraction” button will close the output table and open the extraction popup to select genre and language.

The “View more” button will open the excel sheet in which the data is stored.

Excel Output:
 
