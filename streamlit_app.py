import streamlit as st
import pandas as pd
import base64
import streamlit.components.v1 as components
from pandas.api.types import (
    is_categorical_dtype,
    is_datetime64_any_dtype,
    is_numeric_dtype,
    is_object_dtype,
)

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

def render_page(df, placeholder, render_type=None):
    placeholder.empty()

  
    # with placeholder.container():
    #     #if render_type is None:
    #         add_logo("Logo_Bayer.png")
    #         st.markdown(
    #                 """
    #                 <style>
    #                     [data-testid="stSidebarNav"]::before {
    #                         content: "Next Best Offer";
    #                         margin-left: 20px;
    #                         margin-top: 20px;
    #                         font-size: 30px;
    #                         position: relative;
    #                         top: 170px;
    #                         left: 50px;
    #                         font-weight: 300;
    #                     }
    #                     [data-testid="stSidebarNav"] ul {
    #                         margin-top: 100px;
    #                     }
    #                 </style>
    #                 """,
    #                 unsafe_allow_html=True,
    #             )
    #         st.markdown('''# **Storylines**''')
    #         first_level_container = st.empty()
    #         #first_level_container.empty()
    #         with first_level_container:
    #             col1, col2, col3, col4 = st.columns([2,2,2,1])
    #             countryItemsFromTable = ("Select Country",) + tuple(set(df_campaigns['Country']))
    #             #TAOptionFromTable = ("Select TA",) + tuple(set(df['TA']))
    #             brandFromTable = ("Select Brand",) + tuple(set(df_campaigns['Brand']))
    #             countrySelection = col1.selectbox("Country", countryItemsFromTable, on_change=select_box_filter_changes, key='Country')
    #             TASelection = col2.selectbox("Therapeutic area", ("Select TA",) + tuple(set(df[df['Country']==countrySelection]['TA'])), on_change=select_box_filter_changes, key='TA')
    #             brandOptions = ("Select Brand",) + tuple(set(df[(df['Country']==countrySelection) & (df['TA']==TASelection)]['Brand']))
    #             brandSelection = col3.selectbox("Brand", brandOptions, on_change=select_box_filter_changes, key='Brand')

    #         if render_type == "df_update":
    #             second_container = st.empty()
    #             with placeholder.container():
    #                 placeholder.dataframe(df)
    #                 placeholder.dataframe(df.style.hide(axis="index"))
                    #st.markdown(df.style.hide(axis="index").to_html(), unsafe_allow_html=True)
        # if render_type is not None:
        #     placeholder.empty()
    with placeholder.container():
           # st.markdown('''# **Storylines**''')
            #first_level_container = st.empty()
            #first_level_container.empty()
            #with first_level_container:
            col1, col2, col3, col4 = st.columns([2,2,2,1])
            countryItemsFromTable = ("Select Country",) + tuple(set(df_campaigns['Country']))
            #TAOptionFromTable = ("Select TA",) + tuple(set(df['TA']))
            brandFromTable = ("Select Brand",) + tuple(set(df_campaigns['Brand']))
            countrySelection = col1.selectbox("Country", countryItemsFromTable, on_change=select_box_filter_changes, key='Country')
            TASelection = col2.selectbox("Therapeutic area", ("Select TA",) + tuple(set(df[df['Country']==countrySelection]['TA'])), on_change=select_box_filter_changes, key='TA')
            brandOptions = ("Select Brand",) + tuple(set(df[(df['Country']==countrySelection) & (df['TA']==TASelection)]['Brand']))
            brandSelection = col3.selectbox("Brand", brandOptions, on_change=select_box_filter_changes, key='Brand')
            columns = ['Storyline Status', 'CEC Name', 'Segment', 'Start Date', 'End Date', 'Owner']
            df = df[columns]
            #df['delete'] = st.button()'❌'
            st.dataframe(df)
            #st.dataframe(df.style.hide(axis="index"))
# Click the delete icon (delete) or press the delete key on your keyboard.
def select_box_filter_changes():
    df = filter_dataframe(df_campaigns)
    placeholder = st.empty()
    placeholder.empty()
    render_page(df, placeholder, "df_update")

def filter_dataframe(df):
    for column in st.session_state:
        if 'select' not in st.session_state[column].casefold():
            df = df[df[column] == st.session_state[column]]
    return df


st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

# Load campaigns data
df_campaigns = pd.read_excel('campaign_data.xlsx')
placeholder = st.empty()
render_page(df_campaigns, placeholder)

data_url = "https://raw.githubusercontent.com/mcnakhaee/palmerpenguins/master/palmerpenguins/data/penguins.csv"

#st.dataframe(df)

st.markdown("""
<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
""", unsafe_allow_html=True)