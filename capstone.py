import customtkinter, subprocess
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
from tkinter import ttk
from tkinter import messagebox


# GUI to display top 10 movies with their ratings n a table formaat
def display_details(df, file_name):
    def close():
        display_root.destroy()

    def extract_more():
        display_root.destroy()
        select_genre_language()

    def open_file():
        subprocess.run(['start', file_name], shell=True) 

    display_root = customtkinter.CTk()
    display_root.title("Movie suggestor")

    table = ttk.Treeview(display_root, columns = ('slno', 'name', 'rating'), show = 'headings') 
    table.heading('slno', text = 'Sl. No.')
    table.heading('name', text = 'Movie Name')
    table.heading('rating', text = 'Movie Rating')

    table.grid(row = 0, columnspan = 3, sticky="nsew", pady=10, padx=10)

    for i, row in df.iterrows(): # itterate through the data frame to get the values aand insert them in table format
        table.insert(parent='', index=i, values=(i+1, row['Title'], row['Rating']))

    close_button = customtkinter.CTkButton(display_root, text="Close", command=close)
    close_button.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

    extract_more_button = customtkinter.CTkButton(display_root, text="New Extraction", command=extract_more)
    extract_more_button.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

    view_more_button = customtkinter.CTkButton(display_root, text="View More", command=open_file)
    view_more_button.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")

    display_root.mainloop()

# GUI to select genre and language
def select_genre_language():
    root = customtkinter.CTk()
    root.title("Movie suggestor")
    root.attributes('-topmost', True)

    def close():
        root.destroy()

    def validity(genre_option, language_option): # varify if no genre is selected and give a error message
        if genre_option == '':
            messagebox.showinfo('Genre Validation', 'Please select a genre and try again.')
        else:
            root.destroy()
            scrape_movies(genre_option, language_option)

    genre_frame = customtkinter.CTkFrame(root)
    genre_frame.grid(row = 0, column = 0, sticky="nsew", pady=10, padx=10)

    language_frame = customtkinter.CTkFrame(root)
    language_frame.grid(row = 0, column = 1, sticky="nsew", pady=10, padx=10)

    def open_input_genre():
        genre_dialog = customtkinter.CTkInputDialog(text="Type a Genre:", title="Enter Genre")
        genre_option.set(genre_dialog.get_input())

    def open_input_language():
        language_dialog = customtkinter.CTkInputDialog(text="Type a Language:", title="Enter Language")
        language_option.set(language_dialog.get_input())

    genre_lebel = customtkinter.CTkLabel(genre_frame, text="Select Genre:")
    genre_lebel.grid(row=0, column=0, pady=10, padx=10, sticky="nsew")

    genre_option = customtkinter.CTkComboBox(genre_frame, values=["action", "comedy", "adventure", "thriller", "horror", "animation", "sci-fi", "drama", "mystery"])
    genre_option.set("")

    genre_option.grid(row=1, column=0, pady=10, padx=10, sticky="nsew")

    enter_genre_btn = customtkinter.CTkButton(genre_frame, text="Enter a genre", command=open_input_genre)
    enter_genre_btn.grid(row=2, column=0, pady=10, padx=10, sticky="nsew")

    language_lebel = customtkinter.CTkLabel(language_frame, text="Select Language:")
    language_lebel.grid(row=0, column=0, pady=10, padx=10, sticky="nsew")

    language_option = customtkinter.CTkComboBox(language_frame, values=["English", "Hindi", "Telegu", "Malayalam", "Oriya", "Tamil", "Kannada"])
    language_option.set("")

    language_option.grid(row=1, column=0, pady=10, padx=10, sticky="nsew")

    enter_language_btn = customtkinter.CTkButton(language_frame, text="Enter a language", command=open_input_language)
    enter_language_btn.grid(row=2, column=0, pady=10, padx=10, sticky="nsew")

    ext_button = customtkinter.CTkButton(root, text="Extract", command=lambda:validity(genre_option.get(), language_option.get()))
    ext_button.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

    close_button = customtkinter.CTkButton(root, text="Close", command=close)
    close_button.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

    root.mainloop()

# Scraping data from IMDB using selenium
def scrape_movies(genre, language):
    options = Options()
    options = webdriver.ChromeOptions()

    driver = webdriver.Chrome(options=options)

    # dict to get the language tag for url
    language_tags = {
        'Hindi': 'hi',
        'English': 'en',
        "Telegu":'te',
        "Malayalam":'ml',
        "Oriya":'or',
        "Tamil":'ta',
        "Kannada":'kn',
    }

    if language == '':
        url = f'https://www.imdb.com/search/title/?genres={genre}'
    else:
        lang_tag = language_tags [language]
        url = f'https://www.imdb.com/search/title/?genres={genre}&languages={lang_tag}'

    titles = []
    years = []
    ratings = []
    description = []
    
    driver.get(url)    

    try:
        movies_list = driver.find_elements(By.XPATH, '/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[2]/ul')[0]
        movies_number = movies_list.find_elements(By.TAG_NAME, 'li')

        for i in range ((len(movies_number))):
            try:
                title_xpath = f'/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[2]/ul/li[{i+1}]/div/div/div/div[1]/div[2]/div[1]/a/h3'
                movie_title = driver.find_element(By.XPATH, title_xpath).text
                titles.append(movie_title.split('. ')[1])
            except:
                titles.append("Cannot find title")

            try:
                year_of_rel_xpath = f'/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[2]/ul/li[{i+1}]/div/div/div/div[1]/div[2]/div[2]/span[1]'
                yr_of_rel = driver.find_element(By.XPATH, year_of_rel_xpath).text.split('–')[0]
                years.append(yr_of_rel)
            except:
                years.append("Cannot find year of release")

            try:
                rating_xpath = f'/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[2]/ul/li[{i+1}]/div/div/div/div[1]/div[2]/span/div/span'
                rating = driver.find_element(By.XPATH, rating_xpath).text
                ratings.append(rating.split()[0] + " ★ " + rating.split()[1])
            except:
                ratings.append("Cannot find rating")

            try:
                movie_description_xpath = f'/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[2]/ul/li[{i+1}]/div/div/div/div[2]/div/div'
                movie_description = driver.find_element(By.XPATH, movie_description_xpath).text
                description.append(movie_description)
            except:
                description.append("Cannot find description")

    except Exception as e:
        print(f"An error occurred while scraping: {e}")
    finally:
        driver.quit()

    data = {'Title': titles, 'Year': years, 'Rating': ratings, 'Description': description}
    df = pd.DataFrame(data) # converting extracted data into daata frame

    if language == '':
        file_name = f'movies_{genre}.xlsx'
    else:
        file_name = f'movies_{genre}_{language}.xlsx'

    df.to_excel(file_name, index=False) # saaving output as excel using pd
    display_details(df.loc[:9, ['Title', 'Rating']], file_name)
    print(f"Scraped {len(titles)} movies for genre {genre}")

if __name__ == "__main__":
    customtkinter.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
    customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

    select_genre_language()
