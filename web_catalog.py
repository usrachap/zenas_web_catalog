# Import python packages
import streamlit as st
import requests
#from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col

# Write directly to the app
st.title("Zena's Amazing Athleisure Catalog")
st.write(
    """Pick a Sweatsuit color or style:
    """)

cnx = st.connection("snowflake")
session = snx.session()
my_dataframe = session.table("ZENAS_ATHLEISURE_DB.PRODUCTS.catalog_for_website").select(col('color_or_style'))
