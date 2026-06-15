import streamlit as st
from utils.database import (
    load_data,
    SCAN_HISTORY_FILE,
    PICKUPS_FILE,
    USERS_FILE
)

# ==========================================================
# GET USER DATA
# ==========================================================

def get_user_stats():

    user_id = st.session_state.get(
        "user_id",
        ""
    )

    scans = load_data(
        SCAN_HISTORY_FILE
    )

    pickups = load_data(
        PICKUPS_FILE
    )

    users = load_data(
        USERS_FILE
    )

    user_scans = [
        scan
        for scan in scans
        if scan.get("user_id") == user_id
    ]

    user_pickups = [
        pickup
        for pickup in pickups
        if pickup.get("user_id") == user_id
    ]

    user = next(
        (
            u
            for u in users
            if u.get("user_id") == user_id
        ),
        {}
    )

    return {
        "points": user.get(
            "green_points",
            0
        ),
        "badges": user.get(
            "badges",
            []
        ),
        "scans": len(user_scans),
        "pickups": len(user_pickups)
    }

# ==========================================================
# CITIZEN HOME PAGE
# ==========================================================

def show_citizen_home():

    user_name = st.session_state.get(
        "user_name",
        "Citizen"
    )

    stats = get_user_stats()

    st.title(
        f"🌱 Welcome, {user_name}"
    )

    st.markdown(
        """
        Manage your waste responsibly,
        earn rewards, and contribute
        to a greener future.
        """
    )

    st.markdown("---")

    # ======================================================
    # METRICS
    # ======================================================

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "🎁 Green Points",
            stats["points"]
        )

    with col2:
        st.metric(
            "📸 Waste Scans",
            stats["scans"]
        )

    with col3:
        st.metric(
            "🚛 Pickups",
            stats["pickups"]
        )

    with col4:
        st.metric(
            "🌍 CO₂ Saved",
            f"{stats['scans'] * 0.2:.1f} kg"
        )

    st.markdown("---")

    # ======================================================
    # QUICK ACTIONS
    # ======================================================

    st.subheader(
        "⚡ Quick Actions"
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(
            """
            <div class="dashboard-card">
                <h3>📸 AI Scanner</h3>
                <p>
                Identify waste instantly
                using AI.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            """
            <div class="dashboard-card">
                <h3>🚛 Pickup Request</h3>
                <p>
                Schedule waste pickup
                from your location.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:

        st.markdown(
            """
            <div class="dashboard-card">
                <h3>🎁 Rewards</h3>
                <p>
                View points and unlock
                sustainability badges.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # ======================================================
    # BADGES
    # ======================================================

    st.subheader(
        "🏆 Your Badges"
    )

    badges = stats["badges"]

    if badges:

        for badge in badges:
            st.success(badge)

    else:

        st.info(
            "No badges earned yet. "
            "Start scanning and recycling!"
        )

    st.markdown("---")

    # ======================================================
    # RECENT ACTIVITY
    # ======================================================

    st.subheader(
        "📋 Recent Activity"
    )

    scans = load_data(
        SCAN_HISTORY_FILE
    )

    user_scans = [

        scan

        for scan in scans

        if scan.get("user_id")
        == st.session_state.get(
            "user_id"
        )

    ]

    if user_scans:

        recent_scans = user_scans[-5:]

        for scan in reversed(
            recent_scans
        ):

            st.write(
                f"📸 {scan.get('waste_type')} "
                f"({scan.get('timestamp')})"
            )

    else:

        st.info(
            "No activity yet."
        )

    st.markdown("---")

    # ======================================================
    # ENVIRONMENTAL IMPACT
    # ======================================================

    st.subheader(
        "🌍 Your Environmental Impact"
    )

    impact_col1, impact_col2 = st.columns(2)

    with impact_col1:

        st.markdown(
            """
            <div class="impact-card">
                <h2>♻ Waste Recycled</h2>
                <h1>
                """
            + str(stats["scans"])
            + """
                </h1>
            </div>
            """,
            unsafe_allow_html=True
        )

    with impact_col2:

        co2_saved = round(
            stats["scans"] * 0.2,
            2
        )

        st.markdown(
            f"""
            <div class="impact-card">
                <h2>🌱 CO₂ Saved</h2>
                <h1>{co2_saved} kg</h1>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<br><br>", unsafe_allow_html=True)

    st.success(
        "Every waste item you recycle "
        "helps create a cleaner and "
        "more sustainable future."
    )