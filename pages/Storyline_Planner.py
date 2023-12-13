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
            .stButton{ padding-top: 28px; }
        </style>
        """,
        unsafe_allow_html=True,
    )

st.markdown('''# **Storyline Planner**
This screen helps the marketing team to prepare the storyline for any customer engagement plan.
Also it helps in tagging message topics to the Core messages
''')

st.sidebar.markdown("# Storyline Preparation ")

filters_placeholder = st.empty()

with filters_placeholder.container():

        # create three columns
        sel1, sel2, sel3, sel4 = st.columns(4)
        
        with sel1:
            option = st.selectbox(
                'Country:',
                ('Select Country', 'Germany', 'Switzerland', 'France', 'Netherlands' ))

            #st.write('*You selected:*', option)
            
        with sel2:
            option = st.selectbox(
                'Therapeutic area:',
                ('Select TA', 'TA1', 'TA2', 'TA3'))

            #st.write('*You selected:*', option)

        with sel3:
            option = st.selectbox(
                'Brand:',
                ('Select Brand', 'Brand1', 'Brand2', 'Brand3'))

            #st.write('*You selected:*', option)

        with sel4:
            option = st.selectbox(
                'CEC Name:',
                ('Select CEC', 'CEC1', 'CEC2', 'CEC3'))

            #st.write('*You selected:*', option)
            
st.divider()

FIELDS_Attn = []
DELETES_Attn = []
FIELDS_Rtnl = []
DELETES_Rtnl = []
FIELDS_Etnl = []
DELETES_Etnl = []
FIELDS_Next = []
DELETES_Next = []

def initialize_session_state(fields_size, fields, deletes):
    if fields_size not in st.session_state:
        st.session_state[fields_size] = 0
        st.session_state[fields] = []
        st.session_state[deletes] = []

def set_session_state(fields, deletes, fieldsArray, deletesArray):
    st.session_state[fields] = fieldsArray
    st.session_state[deletes] = deletesArray

def add_field(fields_size):
    st.session_state[fields_size] += 1


def delete_field_Attn(index):
    if "fields_size_Attn" in st.session_state:
        st.session_state["fields_size_Attn"] -= 1
        del st.session_state.fields_Attn[index]
        del st.session_state.deletes_Attn[index]

def delete_field(index, fields_size, fields, deletes):
    if fields_size in st.session_state:
        st.session_state[fields_size] -= 1
        del st.session_state[fields][index]
        del st.session_state[deletes][index]


def update_view(fields_size, fieldsArray, deletesArray, suffix):
    cmlist = st.columns(st.session_state[fields_size]+2)
    for i, cm in enumerate(cmlist):
        if i == len(cmlist) - 1:
            with cm:
                st.button("➕", key=f"add{suffix}{i}", on_click=add_field, args={"fields_size_Attn"})
        else:
            with cm:
                fieldsArray.append(
                    st.text_area(label = f"Core message {suffix}", value=f"Core Message {i + 1}", label_visibility='hidden'))


st.markdown("""<div style="font-size:18px; font-weight: bold; color: #00bdff;">GET ATTENTION</div>""", unsafe_allow_html=True)

initialize_session_state("fields_size_Attn", "fields_Attn", "deletes_Attn")    

update_view("fields_size_Attn", FIELDS_Attn, DELETES_Attn, "Attn")

#st.button("➕", key=f"addAttn", on_click=add_field, args={"fields_size_Attn"})

set_session_state("fields_Attn", "deletes_Attn", FIELDS_Attn, DELETES_Attn)

st.divider()



st.markdown("""<div style="font-size:18px; font-weight: bold; color: #00bdff;">REASONS TO BELIEVE (RATIONAL)</div>""", unsafe_allow_html=True)

initialize_session_state("fields_size_Rtnl", "fields_Rtnl", "deletes_Rtnl")    

update_view("fields_size_Rtnl", FIELDS_Rtnl, DELETES_Rtnl, "Rtnl")

#st.button("➕ Add new core message", key=f"addRtnl", on_click=add_field, args={"fields_size_Rtnl"})

set_session_state("fields_Rtnl", "deletes_Rtnl", FIELDS_Rtnl, DELETES_Rtnl)

st.divider()



st.markdown("""<div style="font-size:18px; font-weight: bold; color: #00bdff;">REASONS TO BELIEVE (EMOTIONAL)</div>""", unsafe_allow_html=True)

initialize_session_state("fields_size_Etnl", "fields_Etnl", "deletes_Etnl")    

update_view("fields_size_Etnl", FIELDS_Etnl, DELETES_Etnl, "Etnl")

#st.button("➕ Add new core message", key=f"addEtnl", on_click=add_field, args={"fields_size_Etnl"})

set_session_state("fields_Etnl", "deletes_Etnl", FIELDS_Etnl, DELETES_Etnl)

st.divider()



st.markdown("""<div style="font-size:18px; font-weight: bold; color: #00bdff;">NEXT STEPS</div>""", unsafe_allow_html=True)

initialize_session_state("fields_size_Next", "fields_Next", "deletes_Next")    

update_view("fields_size_Next", FIELDS_Next, DELETES_Next, "Next")

#st.button("➕ Add new core message", key=f"addNext", on_click=add_field, args={"fields_size_Next"})

set_session_state("fields_Next", "deletes_Next", FIELDS_Next, DELETES_Next)

st.divider()
