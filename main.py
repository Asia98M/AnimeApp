import streamlit as st
import pandas as pd
import os

CSV_FILE = 'series_database.csv'
COLUMNS = ['title', 'genre', 'theme', 'studio']

# Load or create Series Database CSV file
if os.path.exists(CSV_FILE):
    series_df = pd.read_csv(CSV_FILE)
    for col in COLUMNS:
        if col not in series_df.columns:
            series_df[col] = pd.to_numeric(series_df[col], errors='coerce')
else:
    series_data = [
        {'title': 'My Hero Academia', 'genre': 'action', 'theme': 'school, super power', 'studio': 'Bones', 'demographic': 'shounen'},
        {'title': 'Bleach', 'genre': 'action, adventure, supernatural', 'theme': 'none', 'studio': 'Pierrot', 'demographic': 'shounen'},
        {'title': 'Jujutsu Kaisen', 'genre': 'action, supernatural', 'theme': 'school', 'studio': 'Mappa', 'demographic': 'shounen'},
        {'title': 'Demon Slayer', 'genre': 'action, supernatural', 'theme': 'historical', 'studio': 'Ufotable', 'demographic': 'shounen'},
        {'title': 'Kamonohashi Ron', 'genre': 'comedy, mystery', 'theme': 'adult cast, detective', 'studio': 'Diomedéa', 'demographic': 'shounen'},
        {'title': 'Undead Girl Murder Farce', 'genre': 'fantasy, mystery', 'theme': 'adult cast, detective, historical, urban fantasy', 'studio': 'Lapin Track', 'demographic': 'none'},
        {'title': 'The Apothecary Diary', 'genre': 'drama, mystery', 'theme': 'historical, medical', 'studio': 'Toho Animation', 'demographic': 'none'},
        {'title': 'Skip to Loafer', 'genre': 'romance', 'theme': 'school', 'studio': 'P.A. Works', 'demographic': 'seinen'},
        {'title': 'A Sign of Affection', 'genre': 'romance', 'theme': 'adult cast', 'studio': 'Ajia-do', 'demographic': 'shoujo'}
    ]
    series_df = pd.DataFrame(series_data)
    series_df.to_csv(CSV_FILE, index=False)

# Save to CSV
def save_to_csv():
    series_df.to_csv(CSV_FILE, index=False)

# Update initial database in the code
def update_initial_database():
    with open(__file__, 'r') as file:
        lines = file.readlines()
    start_index = lines.index("    series_data = [\n")
    end_index = start_index
    while not lines[end_index].strip() == "]":
        end_index += 1
    new_series_data = series_df.to_dict(orient='records')
    formatted_data = "[\n" + ",\n".join([f"        {repr(entry)}" for entry in new_series_data]) + "\n    ]"
    lines[start_index:end_index + 1] = [formatted_data + "\n"]
    with open(__file__, 'w') as file:
        file.writelines(lines)

# Streamlit UI
st.title('Anime Recommendation Database')

# Search bar
search_query = st.text_input("Search for a Series by Keyword")
if search_query:
    search_results = series_df[series_df.apply(lambda row: search_query.lower() in str(row.values).lower(), axis=1)]
    st.write("Search Results:")
    st.dataframe(search_results)

# Dropdown filters
genres = ["None"] + sorted(set(", ".join(series_df['genre'].dropna()).split(", ")))
themes = ["None"] + sorted(set(", ".join(series_df['theme'].dropna()).split(", ")))
studios = ["None"] + sorted(set(series_df['studio'].dropna()))
demographic = ["None"] + sorted(set(series_df['demographic'].dropna()))

selected_genre = st.selectbox('Select Genre', genres)
selected_theme = st.selectbox('Select Theme', themes)
selected_studio = st.selectbox('Select Studio', studios)
selected_demographic = st.selectbox('Select Demographic', demographic)

# Filter series based on selection
filtered_df = series_df.copy()
if selected_genre != "None":
    filtered_df = filtered_df[filtered_df['genre'].str.contains(selected_genre, case=False, na=False)]
if selected_theme != "None":
    filtered_df = filtered_df[filtered_df['theme'].str.contains(selected_theme, case=False, na=False)]
if selected_studio != "None":
    filtered_df = filtered_df[filtered_df['studio'].str.contains(selected_studio, case=False, na=False)]

# Display filtered results
st.write("Filtered Series:")
st.dataframe(filtered_df)

# Add new entry
st.write("Add a New Series Entry:")
new_title = st.text_input("Title")
new_genre = st.text_input("Genre (comma-separated)")
new_theme = st.text_input("Theme (comma-separated)")
new_studio = st.text_input("Studio")
new_demographic = st.text_input("Demographic")

if st.button("Add Series"):
    if new_title and new_genre and new_theme and new_studio:
        if not series_df['title'].str.lower().eq(new_title.lower()).any():
            new_entry = {
                'title': new_title,
                'genre': new_genre,
                'theme': new_theme,
                'studio': new_studio
            }
            series_df = pd.concat([series_df, pd.DataFrame([new_entry])], ignore_index=True)
            save_to_csv()
            st.success("Series added successfully!")
        else:
            st.error("Series already exists!")
    else:
        st.error("Please fill out all fields.")
