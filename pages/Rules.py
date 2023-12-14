import streamlit as st
import base64

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

def get_base64_of_bin_file(png_file):
    with open(png_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


def build_markup_for_logo(
    png_file,
    background_position="50% 10%",
    margin_top="10%",
    image_width="30%",
    image_height="",
):
    binary_string = get_base64_of_bin_file(png_file)
    return """
            <style>
                [data-testid="stSidebarNav"] {
                    background-image: url("data:image/png;base64,%s");
                    background-repeat: no-repeat;
                    background-position: %s;
                    margin-top: %s;
                    background-size: %s %s;
                }
            </style>
            """ % (
        binary_string,
        background_position,
        margin_top,
        image_width,
        image_height,
    )


def add_logo(png_file):
    logo_markup = build_markup_for_logo(png_file)
    st.markdown(
        logo_markup,
        unsafe_allow_html=True,
    )

# def single_container_notes_horizontal():
#     st.markdown("# Single Container with Horizontal Notes")

#     # Create a session state to persist data between reruns
#     if 'notes' not in st.session_state:
#         st.session_state.notes = ["Hello"]

#     # Add a button to add a new note
#     if st.button("Add Note"):
#         st.session_state.notes.append("New Note")

#     # Add a button to delete the last note
#     if st.button("Delete Last Note") and st.session_state.notes:
#         st.session_state.notes.pop()

#     # Render notes horizontally using columns
#     col_count = len(st.session_state.notes)
#     col_width = int(12 / max(1, col_count))
#     cols = st.columns(col_count)

#     for i, (col, note) in enumerate(zip(cols, st.session_state.notes)):
#         with col:
#             st.markdown(f"## Note {i + 1}")
#             st.text_area(f"Edit Note {i + 1}", value=note, key=f'note_{i}', height=100)

# def single_container_notes_with_pagination():
#     st.markdown("# Single Container with Paginated Notes")

#     # Create a session state to persist data between reruns
#     if 'notes' not in st.session_state:
#         st.session_state.notes = ["Note"]
#     action_button_container = st.empty()

#     with action_button_container:
#         # Add a button to add a new note
#         if st.button("Add Note"):
#             st.session_state.notes.append("New Note")

#     # Set the number of notes per page
#     notes_per_page = 4

#     # Calculate the number of pages
#     num_pages = (len(st.session_state.notes) + notes_per_page - 1) // notes_per_page

#     # Get the current page from the user input
#     page = st.number_input("Page", min_value=1, max_value=num_pages, value=1)

#     # Calculate the start and end indices for the current page
#     start_idx = (page - 1) * notes_per_page
#     end_idx = min(start_idx + notes_per_page, len(st.session_state.notes))

#     # Render notes horizontally using columns for the current page
#     col_count = end_idx - start_idx
#     col_width = int(12 / max(1, col_count))
#     cols = st.columns(col_count)

#     for i, (col, note) in enumerate(zip(cols, st.session_state.notes[start_idx:end_idx])):
#         with col:
#             st.text_area(f"Edit Note {start_idx + i + 1}", value=note, key=f'note_{start_idx + i}', height=100)

def restricted_notes_layout():
    st.markdown("# Restricted Notes Layout")

    # Create a session state to persist data between reruns
    if 'notes' not in st.session_state:
        st.session_state.notes = []

    # Add a button to add a new note
    if st.button("Add Note") and len(st.session_state.notes) < 8:
        st.session_state.notes.append("New Note")

    # Render notes in rows with a maximum of 4 notes per row
    col_count = 4
    cols = st.columns(col_count)

    for i, note in enumerate(st.session_state.notes):
        col_index = i % col_count
        with cols[col_index]:
            st.text_area(f"Edit Note {i + 1}", value=note, key=f'note_{i}', height=100)

add_logo("Logo_Bayer.png")

st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"]::before {
                content: "Next Best Offer";
                margin-left: 20px;
                margin-top: 20px;
                font-size: 30px;
                position: relative;
                top: 170px;
                left: 50px;
                font-weight: 300;
            }
            [data-testid="stSidebarNav"] ul {
                margin-top: 100px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
st.markdown("# Rules page ")
st.sidebar.markdown("# Rules page ")

# single_container_notes_horizontal()

# single_container_notes_with_pagination()

restricted_notes_layout()