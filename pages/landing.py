try:
    import streamlit as st  # type: ignore[import]
except ImportError:  # pragma: no cover
    st = None


def show_landing_page():
    if st is None:
        raise RuntimeError("Streamlit is not installed. Install it with 'pip install streamlit' to use this page.")

    # =====================================================
    # HERO SECTION
    # =====================================================

    st.markdown(
        """
        <div class="hero-section">
            <div class="hero-title">
                🌱 GREENIFY
            </div>

            <div class="hero-subtitle">
                Smart Waste Management & Recycling Platform
                <br><br>
                Reduce Waste • Recycle Better • Earn Rewards
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # =====================================================
    # BANNER IMAGE
    # =====================================================

    try:

        st.image(
            "assets/landing_bg.jpg",
            use_container_width=True
        )

    except Exception:

        st.info(
            "Add landing_bg.jpg to assets folder."
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # =====================================================
    # IMPACT SECTION
    # =====================================================

    st.markdown(
        "<h2 style='color:#2E7D32'>Our Impact</h2>",
        unsafe_allow_html=True
    )