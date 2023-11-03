import streamlit as st
import random

# Title
st.title("Ticket Booking System")

# Sidebar
st.sidebar.title("Options")

# Select number of tickets
num_tickets = st.sidebar.number_input("Select Number of Tickets", min_value=1, max_value=10, value=1)

# Select movie
movies = ["Movie 1", "Movie 2", "Movie 3", "Movie 4"]
movie = st.sidebar.selectbox("Select Movie", movies)

# Select showtime
showtimes = ["10:00 AM", "2:00 PM", "6:00 PM", "10:00 PM"]
showtime = st.sidebar.selectbox("Select Showtime", showtimes)

# Display selected options
st.sidebar.write(f"Selected Movie: {movie}")
st.sidebar.write(f"Selected Showtime: {showtime}")
st.sidebar.write(f"Total Tickets: {num_tickets}")

# Seat selection
st.sidebar.subheader("Select Seats")
seat_rows = 6
seat_cols = 10

selected_seats = st.sidebar.multiselect("Select Seats", [f"Row {i}, Seat {j}" for i in range(1, seat_rows + 1) for j in range(1, seat_cols + 1)], [], num_tickets)

# Book button
if st.sidebar.button("Book Tickets"):
    if len(selected_seats) == num_tickets:
        # Simulate payment processing
        payment_successful = random.choice([True, False])
        if payment_successful:
            st.success(f"Successfully booked {num_tickets} tickets for {movie} at {showtime}. Enjoy the show!")
            st.write(f"Selected Seats: {', '.join(selected_seats)}")
        else:
            st.error("Payment failed. Please try again.")
    else:
        st.warning("Please select the correct number of seats.")

# Availability
st.subheader("Seat Availability")
available_seats = [f"Row {i}, Seat {j}" for i in range(1, seat_rows + 1) for j in range(1, seat_cols + 1)]
for seat in selected_seats:
    available_seats.remove(seat)
st.write(f"{len(available_seats)} seats available out of {seat_rows * seat_cols}")

# Footer
st.markdown("---")
st.markdown("Developed by Your Name")
