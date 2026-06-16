import streamlit as st
import pandas as pd
from utils.database import (
    load_data,
    save_data,
    PURCHASES_FILE,
    COLLECTED_WASTE_FILE
)

def show_direct_purchase():

    st.title("🛒 Direct Waste Purchase")

    st.markdown(
        """
        Purchase recyclable waste
        directly from registered
        waste collectors.
        """
    )

    waste_inventory = load_data(
        COLLECTED_WASTE_FILE
    )

    if not waste_inventory:

        st.info(
            "No waste inventory available."
        )

        return

    df = pd.DataFrame(
        waste_inventory
    )

    st.subheader(
        "♻ Available Waste"
    )

    st.dataframe(
        df,
        use_container_width=True
    )

    st.markdown("---")

    st.subheader(
        "💰 Purchase Request"
    )

    waste_id = st.selectbox(
        "Select Waste",
        df["inventory_id"]
    )

    quantity = st.number_input(
        "Quantity (KG)",
        min_value=1
    )

    offered_price = st.number_input(
        "Offer Price per KG",
        min_value=1.0
    )

    if st.button(
        "Send Purchase Request"
    ):

        purchases = load_data(
            PURCHASES_FILE
        )

        purchases.append({

            "purchase_id":
            len(purchases)+1,

            "market_partner":
            st.session_state.get(
                "user_name"
            ),

            "inventory_id":
            waste_id,

            "quantity":
            quantity,

            "price":
            offered_price,

            "status":
            "Pending"

        })

        save_data(
            PURCHASES_FILE,
            purchases
        )

        st.success(
            "Purchase request sent."
        )