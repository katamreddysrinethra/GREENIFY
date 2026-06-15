import streamlit as st


def show_landing_page():

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

    st.markdown("<br><br>", unsafe_allow_html=True)

    # =====================================================
    # BANNER IMAGE
    # =====================================================

    try:
        st.image(
            "assets/landing_bg.jpg",
            use_container_width=True
        )
    except:
        pass

    st.markdown("<br>", unsafe_allow_html=True)

    # =====================================================
    # STATISTICS SECTION
    # =====================================================

    st.markdown(
        """
        <h2 style='text-align:center;color:#2E7D32'>
        🌍 Making An Environmental Impact
        </h2>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(
            """
            <div class="metric-box">
                <div class="metric-number">
                12,500+
                </div>
                <div class="metric-label">
                KG Waste Recycled
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class="metric-box">
                <div class="metric-number">
                4,850+
                </div>
                <div class="metric-label">
                Pickups Completed
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            """
            <div class="metric-box">
                <div class="metric-number">
                7.2 Tons
                </div>
                <div class="metric-label">
                CO₂ Saved
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col4:
        st.markdown(
            """
            <div class="metric-box">
                <div class="metric-number">
                3,000+
                </div>
                <div class="metric-label">
                Active Users
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<br><br>", unsafe_allow_html=True)

    # =====================================================
    # FEATURES SECTION
    # =====================================================

    st.markdown(
        """
        <h2 style='text-align:center;color:#2E7D32'>
        🚀 Platform Features
        </h2>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(
            """
            <div class="feature-card">

                <div class="feature-icon">
                📸
                </div>

                <div class="feature-title">
                AI Waste Scanner
                </div>

                <div class="feature-text">
                Upload a waste image and let AI identify
                the waste type and provide segregation guidance.
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            """
            <div class="feature-card">

                <div class="feature-icon">
                🚛
                </div>

                <div class="feature-title">
                Smart Pickup System
                </div>

                <div class="feature-text">
                Request pickups, track collectors,
                and manage waste disposal efficiently.
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:

        st.markdown(
            """
            <div class="feature-card">

                <div class="feature-icon">
                🎁
                </div>

                <div class="feature-title">
                Rewards & Badges
                </div>

                <div class="feature-text">
                Earn Green Points and unlock badges
                for responsible waste management.
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<br>", unsafe_allow_html=True)

    col4, col5, col6 = st.columns(3)

    with col4:

        st.markdown(
            """
            <div class="feature-card">

                <div class="feature-icon">
                🌍
                </div>

                <div class="feature-title">
                Environmental Impact
                </div>

                <div class="feature-text">
                Track CO₂ savings, landfill reduction,
                and sustainability contributions.
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with col5:

        st.markdown(
            """
            <div class="feature-card">

                <div class="feature-icon">
                📚
                </div>

                <div class="feature-title">
                Education Hub
                </div>

                <div class="feature-text">
                Learn proper segregation methods,
                recycling tips, and sustainability practices.
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with col6:

        st.markdown(
            """
            <div class="feature-card">

                <div class="feature-icon">
                🏪
                </div>

                <div class="feature-title">
                Recycling Marketplace
                </div>

                <div class="feature-text">
                Connect with buyers and sellers
                in the circular economy ecosystem.
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<br><br>", unsafe_allow_html=True)

    # =====================================================
    # HOW IT WORKS
    # =====================================================

    st.markdown(
        """
        <h2 style='text-align:center;color:#2E7D32'>
        ♻ How GREENIFY Works
        </h2>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        1️⃣ Scan Waste Using AI

        2️⃣ Identify Waste Category

        3️⃣ Request Pickup

        4️⃣ Earn Green Points

        5️⃣ Create Environmental Impact
        """
    )

    st.markdown("<br><br>", unsafe_allow_html=True)

    # =====================================================
    # CONTINUE BUTTON
    # =====================================================

    c1, c2, c3 = st.columns([2, 2, 2])

    with c2:

        if st.button(
            "🚀 CLICK TO CONTINUE",
            use_container_width=True
        ):

            st.session_state.page = "login"

            st.rerun()

    st.markdown("<br><br>", unsafe_allow_html=True)

    # =====================================================
    # FOOTER MESSAGE
    # =====================================================

    st.markdown(
        """
        <div style='text-align:center;color:gray'>

        🌱 Together We Can Build A Cleaner And Greener Future 🌱

        </div>
        """,
        unsafe_allow_html=True
    )