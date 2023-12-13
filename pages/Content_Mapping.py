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
    
st.markdown('''# **Content Mapping**
This screen helps the marketing team to map the content factory content with the different channels for each Core message in a Stotyline Plan.
''')

st.sidebar.markdown("# Content Factory Content Mapping ")