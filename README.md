**Code Explanation Step by step**:
Importing Required Libraries and Modules
 ![image](https://github.com/nirupamab457/Python-Project-Submission/assets/95667423/8f596126-e15b-4007-b2b8-265a7b9a4192)

•	customtkinter: Custom libraries for creating GUIs in Python.
•	subprocess: Used here to open files using system commands.
•	selenium: Required for automating web interactions, used here to scrape IMDb.
•	pandas: Essential for data manipulation, specifically handling data frames.
•	tkinter and ttk: Standard libraries for creating GUIs in Python.

display_details(df, file_name) Function
 ![image](https://github.com/nirupamab457/Python-Project-Submission/assets/95667423/7cfd598e-5462-4872-84a7-d2a14215e4e0)

•	Function Purpose: Displays a GUI window (display_root) showing the top 10 movies with their ratings in a table format.
•	Components:
o	Treeview (table): Displays the data in a tabular format with columns for serial number (slno), movie name (name), and movie rating (rating).
o	Buttons:
![image](https://github.com/nirupamab457/Python-Project-Submission/assets/95667423/d3d12c4f-81ac-4864-8a2e-bc916057e400)

 
	Close Button: Destroys the current window (display_root).
	New Extraction Button: Closes the current window and opens the genre and language selection window (select_genre_language()).
	View More Button: Opens the saved Excel file using the default system application.

select_genre_language() Function

	Function Purpose: Displays a GUI window (root) for selecting a movie genre and language.
	Components:
 ![image](https://github.com/nirupamab457/Python-Project-Submission/assets/95667423/52ac3084-9681-43f8-bb7a-a02551a4db32)

o	Frames (genre_frame and language_frame): Organize widgets for genre selection and language selection.
 ![image](https://github.com/nirupamab457/Python-Project-Submission/assets/95667423/1acc7e79-d50c-44f4-8b4f-9fe9e7e17729)

o	Labels (genre_lebel and language_lebel): Display text labels for indicating the purpose of dropdowns.
o	Combo Boxes (genre_option and language_option): Dropdown menus for selecting genre and language.
o	Buttons:
	Enter Genre Button (enter_genre_btn) and Enter Language Button (enter_language_btn): Allow users to enter custom genres and languages.
 ![image](https://github.com/nirupamab457/Python-Project-Submission/assets/95667423/adb8a37e-1727-41d0-a4d2-6962f43a759f)

	Extract Button (ext_button): Initiates data extraction based on selected genre and language.
	Close Button (close_button): Closes the current window (root).

scrape_movies(genre, language) Function
	 ![image](https://github.com/nirupamab457/Python-Project-Submission/assets/95667423/00ab3636-53c6-467c-84f1-aaf59d6a5ea1)

	Selenium Setup: Initializes Selenium WebDriver with Chrome options.
 ![image](https://github.com/nirupamab457/Python-Project-Submission/assets/95667423/06417d05-4bc1-4b50-b2ea-ea2844ce38a0)

	Language Tags: Dictionary to map languages to their respective IMDb URL tags.
	URL Construction: Constructs the URL based on selected genre and language.
![image](https://github.com/nirupamab457/Python-Project-Submission/assets/95667423/c10af61f-51d8-46ff-a50a-60a53d51d2d1)


	Web Scraping:
o	Opens the constructed URL.
o	Extracts movie titles, years, ratings, and descriptions using XPath.
o	Handles missing data with try-except blocks.
	Data Handling:
 ![image](https://github.com/nirupamab457/Python-Project-Submission/assets/95667423/656b91df-a71a-4862-b7ab-9fb7affa45a4)

	Stores extracted data in a Pandas DataFrame.
	Saves the DataFrame to an Excel file.
	Calls display_details() to show the top 10 movies.
 
**Output**

Initial dialog box pops up after running the code
![image](https://github.com/nirupamab457/Python-Project-Submission/assets/95667423/bb295576-b581-4ed0-9507-7d40440d20cb)

 


Select the genre and language from the dropdowns. You can enter them manually by clicking on the “enter a genre” and “enter a language” buttons respectively.

 ![image](https://github.com/nirupamab457/Python-Project-Submission/assets/95667423/fddb7086-5e6b-47bc-9f01-a8f6d3602ecd)


Genre selection is mandatory as proceeding without it will show error
![image](https://github.com/nirupamab457/Python-Project-Submission/assets/95667423/fd34ae76-1777-479a-9fc9-1476c151357a)

 

The first out put contains a tabular view of the top 10 movies from the selected genre.
![image](https://github.com/nirupamab457/Python-Project-Submission/assets/95667423/81c8a1a7-074f-415e-9fce-04ca2ff4a316)

 

The “New Extraction” button will close the output table and open the extraction popup to select genre and language.

The “View more” button will open the excel sheet in which the data is stored.

Excel Output:
 ![image](https://github.com/nirupamab457/Python-Project-Submission/assets/95667423/b08d3281-a995-4a1e-80cc-6d72f42a2a54)

