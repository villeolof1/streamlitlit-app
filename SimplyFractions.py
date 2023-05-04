# ----------------------------
# IMPORTS
# ----------------------------

import streamlit as st
import numpy as np
from streamlit_option_menu import option_menu
from PIL import Image

st.set_page_config(page_title="SimplyFractions", page_icon="😮‍💨", layout="wide")

fracsimpim = Image.open("FractionSimplifiedImage.png")
pizzasimp = Image.open("PizzaSimplifyImage.png")

st.markdown(
    """<style>
        .thick-divider {
            border-top: 3px solid #999;
            margin-top: 20px;
            margin-bottom: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<hr class="thick-divider">', unsafe_allow_html=True)



#Use local CSS
def local_css(file_name):

    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.py")


# ----------------------------
# DEFINE FUNCION FOR SIMPLIFY FRACTIONS
# ----------------------------



def simplify(num, den) -> tuple:

    for divider in range(np.minimum(num,den),1,-1):
        if (num/divider).is_integer() and (den/divider).is_integer():
            st.write("÷ " + str(divider) + " (Highest Common Factor)")
            num = num/divider
            den = den/divider
            break
    return num, den

# ----------------------------
# SIDEBAR MENU
# ----------------------------

with st.sidebar:
    selected = option_menu(
    menu_title = "Main Menu", #requieed 
    options = ["Home", "Simplify Fractions", "Help!"]
    )

if selected == "Home":
    col1, col2 = st.columns(2)
    with col1:
        st.title("Simply Simplifying Fractions")
        st.write("""
        Welcome to our website! 
        
        Here you can easily and quickly simplify fractions!
        Are you struggling with reducing fractions to their 
        simplest form? Do you find yourself spending too 
        much time trying to simplify fractions by hand? 
        Our website is here to help!
        
        With our user-friendly interface, you can input 
        any fraction and simplify it within seconds. Our 
        tool can simplify fractions with both whole 
        numbers and decimals, and it can handle any size 
        of fraction, no matter how large or small.
        Our simplification process follows standard 
        mathematical rules and ensures the most simplified 
        form of the fraction. This makes it a valuable 
        tool for students, teachers, and anyone who needs 
        to simplify fractions on a regular basis.
        
        Best of all, our website is completely free to use, 
        and there is no need to download any software. 
        Simply visit our website and simply start simplifying 
        fractions right away!
        """)
    with col2:
        st.image(fracsimpim)
        st.image(pizzasimp)

# ----------------------------
# STREAMLIT PAGE BELOW
# ----------------------------
if selected == "Simplify Fractions":
    num = st.text_input("Numerator:")
    st.markdown('<hr class="thick-divider">', unsafe_allow_html=True)
    den = st.text_input("Denominator:")

    if st.button("Simplify!"):
        den = int(den)
        num = int(num)
        num_simple, den_simple = simplify(num, den)
        num_simple = int(num_simple)
        den_simple = int(den_simple)
        st.latex(r'\frac{%s}{%s}' % (num_simple, den_simple))

        st.write("")
        st.write("")
        st.write("")

        st.text("The simplified form of " + str(num) + " / " + str(den) + " equals to " + str(num_simple) + " / " + str(den_simple) + "!")

    st.markdown("")
    st.markdown("")
    st.markdown("")




if selected == "Help!":
    with st.container():
        st.header("FAQ")
        st.write("""
        1. What is the purpose of this website?
        Our goal is to make simplifying fractions free and availiable 
        to everyone! We want every single person to have a chance 
        to simplify fractions and improve their fraction skills!
        
        2. Is it free? 
        Of course it is free! Since out goal is to make simplifying 
        fractions free and availible to everyone, it would be quite
        ironic if this website wasn't free.
        
        3. What topics are covered in this website?
        Simply Simplifying fractions, LOL! I might add some tutorials
        to learn simplifying fractions as well!

        """)

    #Contact form
    st.header("Contact Us")
    st.write("Do you find any bugs? Have any questions? Other?")
    contact_form = """
    <form action="https://formsubmit.co/galileo.streamlit@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="False">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html = True)

st.markdown("<p style='text-align: center;'>© SimplyFractions</p>", unsafe_allow_html=True)
