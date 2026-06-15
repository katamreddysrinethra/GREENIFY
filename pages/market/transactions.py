import streamlit as st
import pandas as pd
from datetime import datetime

from utils.database import (
    load_data,
    save_data
)

# ==========================================================
# TRANSACTION FILE
# ==========================================================

TRANSACTIONS_FILE = "data/transactions.json"


# ==========================================================
# GENERATE TRANSACTION ID
# ==========================================================

def generate_transaction_id():

    transactions = load_data(
        TRANSACTIONS_FILE
    )

    return f"TXN{len(transactions)+1:05d}"


# ==========================================================
# SAVE TRANSACTION
# ==========================================================

def save_transaction(record):

    transactions = load_data(
        TRANSACTIONS_FILE
    )

    transactions.append(record)

    save_data(
        TRANSACTIONS_FILE,
        transactions
    )


# ==========================================================
# TRANSACTIONS PAGE
# ==========================================================

def show_transactions():

    st.title("💰 Marketplace Transactions")

    st.markdown(
        """
        View and manage marketplace
        transaction records.
        """
    )

    st.markdown("---")

    # ======================================================
    # DEMO TRANSACTION CREATOR
    # ======================================================

    st.subheader(
        "➕ Add Transaction"
    )

    with st.expander(
        "Create Transaction Record"
    ):

        buyer = st.text_input(
            "Buyer Name"
        )

        seller = st.text_input(
            "Seller Name"
        )

        waste_type = st.selectbox(
            "Waste Type",
            [
                "Plastic",
                "Paper",
                "Glass",
                "Metal",
                "Organic Waste",
                "E-Waste",
                "Mixed Waste"
            ]
        )

        quantity = st.number_input(
            "Quantity (KG)",
            min_value=1.0,
            step=1.0
        )

        price_per_kg = st.number_input(
            "Price Per KG (₹)",
            min_value=1.0,
            step=1.0
        )

        if st.button(
            "Save Transaction"
        ):

            total_amount = (
                quantity
                * price_per_kg
            )

            transaction = {

                "transaction_id":
                generate_transaction_id(),

                "buyer":
                buyer,

                "seller":
                seller,

                "waste_type":
                waste_type,

                "quantity":
                quantity,

                "price_per_kg":
                price_per_kg,

                "total_amount":
                total_amount,

                "created_at":
                datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
            }

            save_transaction(
                transaction
            )

            st.success(
                "Transaction recorded successfully."
            )

            st.rerun()

    st.markdown("---")

    # ======================================================
    # LOAD TRANSACTIONS
    # ======================================================

    transactions = load_data(
        TRANSACTIONS_FILE
    )

    if not transactions:

        st.info(
            "No transactions found."
        )

        return

    # ======================================================
    # METRICS
    # ======================================================

    total_transactions = len(
        transactions
    )

    total_volume = sum(

        float(
            transaction.get(
                "quantity",
                0
            )
        )

        for transaction in transactions

    )

    total_value = sum(

        float(
            transaction.get(
                "total_amount",
                0
            )
        )

        for transaction in transactions

    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "📋 Transactions",
            total_transactions
        )

    with col2:

        st.metric(
            "⚖ Volume (KG)",
            round(
                total_volume,
                2
            )
        )

    with col3:

        st.metric(
            "💰 Total Value",
            f"₹{round(total_value,2)}"
        )

    st.markdown("---")

    # ======================================================
    # TABLE
    # ======================================================

    df = pd.DataFrame(
        transactions
    )

    st.dataframe(
        df,
        use_container_width=True
    )

    st.markdown("---")

    # ======================================================
    # DETAILED VIEW
    # ======================================================

    st.subheader(
        "📄 Transaction Details"
    )

    for transaction in reversed(
        transactions
    ):

        with st.expander(

            f"{transaction['transaction_id']} "
            f"- "
            f"{transaction['waste_type']}"

        ):

            st.write(
                f"🛒 Buyer: "
                f"{transaction['buyer']}"
            )

            st.write(
                f"🏪 Seller: "
                f"{transaction['seller']}"
            )

            st.write(
                f"♻ Waste Type: "
                f"{transaction['waste_type']}"
            )

            st.write(
                f"⚖ Quantity: "
                f"{transaction['quantity']} KG"
            )

            st.write(
                f"💰 Price/KG: ₹"
                f"{transaction['price_per_kg']}"
            )

            st.write(
                f"💵 Total Amount: ₹"
                f"{transaction['total_amount']}"
            )

            st.write(
                f"🕒 Date: "
                f"{transaction['created_at']}"
            )

    st.markdown("---")

    st.success(
        "🌍 Marketplace transactions promote sustainable recycling and resource recovery."
    )