import streamlit as st

# Set page configuration
st.set_page_config(page_title="Educational Research Web App", layout="wide")


# Create a placeholder to inject the popover button using components
c1,c2,c3,c4,c5=st.columns([1,1,2,1,1])
with c3:
    with st.popover("Acknowledgements", help="Click here to view our acknowledgements."):
        st.markdown("""
        ## Acknowledgements

        We'd like to express our gratitude to the creators and maintainers of the resources and tools that helped make this application possible.

        While the majority of content, code, and visuals are custom-built or curated in-house, the following have played a valuable role in supporting this project:

        - **Fonts**:  
          This app uses the *Bahnschrift Condensed* font (by Microsoft) and web fonts from Google Fonts, including **Montserrat** and **Open Sans**. Please note that some fonts may have specific terms for commercial use.

        - **External Resources**:  
            - [**STRING Database**](https://string-db.org): For protein-protein interaction data.  
            - [**Primer3**](https://www.primer3plus.com/index.html): Used for primer design in molecular biology workflows.  
            - [**ICRISAT CicerSeq**](https://cegresources.icrisat.org/cicerseq/?page_id=3605): For curated chickpea sequence data.

        We appreciate the openness and availability of these resources, which help the scientific community grow and innovate together.
        """)
