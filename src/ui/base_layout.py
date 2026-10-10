import streamlit as st

def style_background_home():

    st.markdown("""
         <style>
            
             .stApp{
               background: #5865F2 !important;
            }

             .stApp div[data-testid="stColumn"]{
                    background-color:#E0E3FF !important;
                    padding:2.5rem !important;
                    border-radius: 5rem !important;
                    }


         </style>

            """, unsafe_allow_html =True)


def style_background_dashboard():

    st.markdown("""
         <style>
            
             .stApp{
               background:  #E0E3FF !important;

            }

         </style>

            """, unsafe_allow_html =True)


def style_base_layout():

    st.markdown("""
         <style>
            @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');
            @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');

            /* Hide Top bar of streamlit */

            #MainMenu , footer , header {
              visibility: hidden;
            }

            .block-container {
                padding-top:1.5rem !important;    
            }

            h1 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 3.5rem !important;
                line-height:1.1 !important;
                margin-bottom:0rem !important;
                color: black !important;
            }
                

            h2 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 2rem !important;
                line-height:0.9 !important;
                margin-bottom:0rem !important;
                color: black !important;
            }
                
            h3, h4, p {
                font-family: 'Outfit', sans-serif;    
            }

            /* ---------- Light-blue background ke upar ka saara text BLACK ---------- */
            [data-testid="stMain"] h3,
            [data-testid="stMain"] h4,
            [data-testid="stMain"] [data-testid="stWidgetLabel"] p,
            [data-testid="stMain"] [data-testid="stWidgetLabel"] label,
            [data-testid="stMain"] [data-testid="stCaptionContainer"],
            [data-testid="stMain"] [data-testid="stMarkdownContainer"]:not(button *) p,
            [data-testid="stMain"] [data-testid="stMarkdownContainer"]:not(button *) li,
            [data-testid="stMain"] [data-testid="stExpander"] summary,
            [data-testid="stMain"] [data-testid="stExpander"] summary p,
            [data-testid="stMain"] [data-testid="stExpander"] summary span {
                color: #000000 !important;
                opacity: 1 !important;
            }

            /* Expander ka arrow aur border saaf dikhe */
            [data-testid="stMain"] [data-testid="stExpander"] summary svg {
                color: #000000 !important;
                fill: #000000 !important;
            }
            [data-testid="stMain"] [data-testid="stExpander"] {
                border: 1px solid rgba(0, 0, 0, 0.25) !important;
                border-radius: 12px !important;
            }

            /* ---------- Buttons ---------- */
            button{
                border-radius: 1.5rem !important;
                background-color: #5865F2 !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button[kind="secondary"]{
                border-radius: 1.5rem !important;
                background-color: #EB459E !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button[kind="tertiary"]{
                border-radius: 1.5rem !important;
                background-color: black !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            /* Button ke andar ka text hamesha white rahe */
            button p, button span {
                color: white !important;
            }

            button:hover{
                transform :scale(1.05)}

         </style>

            """, unsafe_allow_html =True)