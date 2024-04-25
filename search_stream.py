import streamlit as st
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('chroma_embeddings.db')

# Define function to search for subtitle files based on movie name
def search_subtitle(movie_name):
    query = f"SELECT name, file_content FROM subtitles WHERE name LIKE '%{movie_name}%'"
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchone()
    return result

st.title('Subtitle Search Engine')

search_query = st.text_input('Enter movie name:')
if st.button('Search'):
    if search_query:
        movie_name, file_content = search_subtitle(search_query)
        if movie_name and file_content:
            st.write(f'Download subtitle file for {movie_name}:')
            st.download_button(label='Download', data=file_content, file_name=f'{movie_name}_subtitle.csv', mime='text/plain')
        else:
            st.write('No results found.')

# Close database connection
conn.close()
