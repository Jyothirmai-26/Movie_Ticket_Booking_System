import streamlit as st
from datetime import datetime
import random

# ---------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------

st.set_page_config(
    page_title="Movie Ticket Booking",
    page_icon="🎬",
    layout="centered"
)

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------

st.markdown("""
<style>
    .main {
        background-color: #f5f7fb;
    }

    .title {
        text-align: center;
        color: #6c2bd9;
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #666;
        font-size: 18px;
        margin-bottom: 30px;
    }

    .movie-card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #e5e5e5;
        margin-bottom: 20px;
    }

    .summary-card {
        background-color: #ffffff;
        padding: 25px;
        border-radius: 15px;
        border: 1px solid #ddd;
        box-shadow: 0 3px 10px rgba(0,0,0,0.06);
    }

    .total {
        font-size: 28px;
        font-weight: bold;
        color: #6c2bd9;
    }

    .success-box {
        background-color: #e9f8ef;
        padding: 18px;
        border-radius: 12px;
        border-left: 5px solid #28a745;
        margin-top: 15px;
    }

    div.stButton > button {
        width: 100%;
        border-radius: 10px;
        height: 45px;
        font-size: 16px;
        font-weight: 600;
    }

    @media (max-width: 600px) {
        .title {
            font-size: 30px;
        }

        .subtitle {
            font-size: 15px;
        }
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# MOVIE DATA
# ---------------------------------------------------

movies = {
    "Avengers: Endgame": {
        "genre": "Action • Adventure • Sci-Fi",
        "duration": "3h 02m",
        "rating": "8.4/10",
        "description": "Earth's mightiest heroes come together for one final battle."
    },
    "Interstellar": {
        "genre": "Sci-Fi • Drama • Adventure",
        "duration": "2h 49m",
        "rating": "8.7/10",
        "description": "A team of explorers travels through a wormhole in search of a new home."
    },
    "Spider-Man: No Way Home": {
        "genre": "Action • Adventure • Fantasy",
        "duration": "2h 28m",
        "rating": "8.2/10",
        "description": "Spider-Man faces villains from different universes."
    },
    "Avatar: The Way of Water": {
        "genre": "Action • Adventure • Fantasy",
        "duration": "3h 12m",
        "rating": "7.6/10",
        "description": "Jake Sully and his family explore the oceans of Pandora."
    }
}

# ---------------------------------------------------
# TICKET PRICES
# ---------------------------------------------------

ticket_prices = {
    "Standard": 150,
    "Premium": 250,
    "VIP": 350
}

# ---------------------------------------------------
# SESSION STATE
# ---------------------------------------------------

if "booking_confirmed" not in st.session_state:
    st.session_state.booking_confirmed = False

if "booking_id" not in st.session_state:
    st.session_state.booking_id = ""

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------

st.markdown(
    '<div class="title">🎬 Movie Ticket Booking</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Book your movie tickets quickly and easily 🍿</div>',
    unsafe_allow_html=True
)

# ---------------------------------------------------
# MOVIE SELECTION
# ---------------------------------------------------

st.markdown("### 🎞️ Select Your Movie")

selected_movie = st.selectbox(
    "Choose a movie",
    list(movies.keys())
)

movie_info = movies[selected_movie]

st.markdown(
    f"""
    <div class="movie-card">
        <h2>🎬 {selected_movie}</h2>
        <p><b>Genre:</b> {movie_info["genre"]}</p>
        <p><b>Duration:</b> {movie_info["duration"]}</p>
        <p><b>Rating:</b> ⭐ {movie_info["rating"]}</p>
        <p>{movie_info["description"]}</p>
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------------------------------------------
# BOOKING DETAILS
# ---------------------------------------------------

st.markdown("### 🎟️ Booking Details")

col1, col2 = st.columns(2)

with col1:
    ticket_type = st.selectbox(
        "Ticket Category",
        list(ticket_prices.keys())
    )

with col2:
    number_of_tickets = st.number_input(
        "Number of Tickets",
        min_value=1,
        max_value=10,
        value=1,
        step=1
    )

# ---------------------------------------------------
# PRICE CALCULATION
# ---------------------------------------------------

price_per_ticket = ticket_prices[ticket_type]

total_price = price_per_ticket * number_of_tickets

# ---------------------------------------------------
# LIVE PRICE DISPLAY
# ---------------------------------------------------

st.markdown("### 💰 Price Details")

price_col1, price_col2, price_col3 = st.columns(3)

with price_col1:
    st.metric(
        "Ticket Price",
        f"₹{price_per_ticket}"
    )

with price_col2:
    st.metric(
        "Tickets",
        number_of_tickets
    )

with price_col3:
    st.metric(
        "Total",
        f"₹{total_price}"
    )

st.divider()

# ---------------------------------------------------
# BOOKING BUTTON
# ---------------------------------------------------

if st.button("🎫 Confirm Booking", type="primary"):

    if number_of_tickets < 1:
        st.error("Please select at least one ticket.")

    else:
        # Generate a simple booking ID
        st.session_state.booking_id = (
            "MOV" + str(random.randint(10000, 99999))
        )

        st.session_state.booking_confirmed = True

        st.success("🎉 Booking confirmed successfully!")

# ---------------------------------------------------
# BOOKING SUMMARY
# ---------------------------------------------------

if st.session_state.booking_confirmed:

    st.markdown("## 🧾 Booking Summary")

    st.markdown(
        f"""
        <div class="summary-card">

        <h3>🎟️ Your Movie Booking</h3>

        <p><b>Booking ID:</b> {st.session_state.booking_id}</p>

        <p><b>🎬 Movie:</b> {selected_movie}</p>

        <p><b>🎟️ Ticket Type:</b> {ticket_type}</p>

        <p><b>🔢 Number of Tickets:</b> {number_of_tickets}</p>

        <p><b>💵 Price per Ticket:</b> ₹{price_per_ticket}</p>

        <hr>

        <p class="total">💰 Total Amount: ₹{total_price}</p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="success-box">
            ✅ <b>Booking Confirmed!</b><br>
            Enjoy <b>{selected_movie}</b> 🍿<br>
            Your booking ID is
            <b>{st.session_state.booking_id}</b>.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    # ---------------------------------------------------
    # RESET BUTTON
    # ---------------------------------------------------

    if st.button("🔄 Make Another Booking"):

        st.session_state.booking_confirmed = False
        st.session_state.booking_id = ""

        st.rerun()

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.divider()

st.markdown(
    """
    <div style="text-align:center; color:#777;">
        🎬 Movie Ticket Booking System <br>
        Built with Python + Streamlit 🐍
    </div>
    """,
    unsafe_allow_html=True
)
