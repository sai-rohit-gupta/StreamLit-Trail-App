import streamlit as st
import base64
import datetime
import pandas as pd


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
st.markdown('''# **CEB Planner**
This screen helps the marketing team to define a plan or blueprint to bring customer from one adoption status to another.
''')


st.markdown(
    """
<style>
button {
    height: auto;
    padding-top: 10px !important;
    padding-bottom: 10px !important;
    padding-left: 20px !important;
    padding-right: 20px !important;
}
</style>
""",
    unsafe_allow_html=True,
)

st.divider()

def ceb_planner_form():
    
    today = datetime.datetime.now()
    next_year = today.year + 1
    jan_1 = datetime.date(next_year, 1, 1)
    dec_31 = datetime.date(next_year, 12, 31)

    first_level_container = st.empty()
    with first_level_container:
        col1, col2, col3, col4 = st.columns(4)
        col1.selectbox("Segment", ("Select Segment", "test1", "test2"))
        col3.date_input("CEB Start date", format="DD/MM/YYYY")
        col4.date_input("CEB End date", format="DD/MM/YYYY")
    
    second_level_container = st.empty()
    with second_level_container:
        col1, col2, col3, col4 = st.columns(4)
        col1.text_area("CEB Name", height = 25)
        col2.text_area("Segment Size")
        col3.text_area("Segment Value")
        col4.text_area("Potential")

    third_level_container = st.empty()
    with third_level_container:
        col1, col2, col3 = st.columns([1,1,2])

        with col1:
            st.selectbox("Country", ("Select Country", "C1", "C2"))
            st.selectbox("Brand", ("Select Brand", "C1", "C2"))
            st.selectbox("Speciality", ("Select Speciality"))
        with col2:
            st.selectbox("Threapeutic area", ("Select Threapeutic area", "T1", "T2"))
            st.selectbox("Indication", ("Select Indication", "T1", "T2"))
        #col3.selectbox("Priority Opportunity", ('Select priority opportunity', 'This is a lengthy text for priority opportunity, this text is added for testing of streamlit selectbox dimension changes', 'p2'))
        col3.text_area("Priority Opportunity", height = 400)

    fourth_level_container = st.empty()
    with fourth_level_container:
        col1, col3 = st.columns([2,2])
        with col1:
            st.selectbox("Adoption Ladder (FROM)", ('Select priority opportunity', 'p1', 'p2'))
            st.selectbox("Communication Objective", ('Select Communication Objective', 'c1', 'c2'))
        with col3:
            st.selectbox("Adoption Ladder (TO)", ('Select adoption ladder to', 'p1', 'p2'))
            st.selectbox("PGMI", ('Select PGMI', 'p1', 'p2'))
    st.selectbox("Customer Insight", ["Select customer insight", "t1"])
    col1, col2, col3 = st.columns(3)
    col1.selectbox("Barrier/Driver", ('Select Barrier / Driver 1', 'p1', 'p2'))
    col2.selectbox("Barrier/Driver", ('Select Barrier / Driver 2', 'p1', 'p2'))
    col3.selectbox("Barrier/Driver", ('Select Barrier / Driver 3', 'p1', 'p2'))
    button_container = st.empty()
    with button_container:
        col1, col2, col3, col4 = st.columns(4)
        submit_button = col3.button("Submit")
        next_button = col4.button("next")

    
	
custom_css = '''
    <style>
        div.css-1om1ktf.e1y61itm0 {
          width: 800px;
        }
        textarea.st-cl {
          height: 25px;
        }
    </style>
    '''
st.markdown(custom_css, unsafe_allow_html=True)

ceb_planner_form()