import streamlit as st
from PIL import Image

# Set page config
st.set_page_config(
    page_title="Beast Entertainment - Survival Challenge",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Hide Streamlit branding in footer
st.markdown("""
    <style>
        footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Colors and styling
st.markdown("""
    <style>
    .main {
        background-color: #002b36;
        color: white;
    }
    h1, h2 {
        color: #DAA520;
    }
    .button {
        background-color: #32CD32;
        color: white;
        border: none;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 8px;
    }
    .center {
        text-align: center;
    }
    .sponsor-img {
        margin: 0 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Navbar for page selection
st.sidebar.title("Navigation")
page = st.sidebar.radio("Select Page", ["Home", "Event Gallery", "Services"])

if page == "Home":
    # Header section
    st.image("APP/logo.jpeg", width=150)  # Replace with your logo if available
    st.title("Beast Entertainment - Survival Challenge")
    st.subheader("Are You Ready to Win $1 Million?")

    # Description section
    st.markdown("""
    ### About the Challenge
    Beast Entertainment brings you the **Survival Challenge**! Compete in exciting games set in an abandoned city for a chance to win **$1 million**. This season, we're pushing boundaries and testing limits—physically and mentally. It's your time to shine!

    **Join from anywhere in the world**—we will fly you to the required location once selected!

    **What to Expect:**
    - Thrilling games inspired by challenges like Squid Game and Spartan tasks.
    - A unique location: an eerie abandoned city designed for maximum excitement.
    - Your chance to prove you're the ultimate survivor!

    ---
    """)

    # Flyer section
    st.header("Event Flyer")
    flyer = Image.open("APP/flyer.jpg")  # Replace with your flyer image file
    st.image(flyer, caption="Scan the QR Code to Apply!", use_container_width=True)

    # Apply Now and Activities Section
    st.markdown("""
    <div class="column-border">
        <div style="display: flex; flex-direction: row; justify-content: space-between; padding: 10px;">
            <div style="flex: 1; margin-right: 10px;">
                <h2>Apply Now</h2>
                <p>Complete the application form to get started:</p>
                <a href="https://docs.google.com/forms/d/e/1FAIpQLSeTLZsrT3wzH40-hv-RbGdpjn_gpVBQMDwVBBoJHigMSnFk2g/viewform?usp=sharing" target="_blank" class="button">Click Here to Apply</a>
            </div>
            <div style="flex: 1;">
                <h2>Activities</h2>
                <ul>
                    <li>Navigate through obstacle courses in the abandoned city.</li>
                    <li>Participate in physically and mentally challenging games.</li>
                    <li>Collaborate with teammates and strategize to win.</li>
                </ul>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Footer with sponsor logos and contact information
    st.markdown("---")

    # Contact Information Section
    st.markdown("""
    <div style="text-align: center;">
        <h4>Contact Us</h4>
        <p>For inquiries, email us at <b>mrbeastbussiness6@gmail.com</b></p>
        <p>Follow us on Instagram: <a href="https://www.instagram.com/game.zuri" target="_blank">@game.zuri</a></p>
    </div>
    """, unsafe_allow_html=True)

    # Sponsors Section
    st.markdown("<h4 style='text-align: center;'>Our Collaborators</h4>", unsafe_allow_html=True)

    # Display sponsor/collaborators logos in a horizontal row
    collaborator_images = [
        "APP/instagram.png",
        "APP/tiktok.png",
        "APP/snapchat.png",
        "APP/youtube.png"
    ]

    # Render images in columns
    cols = st.columns(len(collaborator_images))  # Create one column per image
    for col, image_path in zip(cols, collaborator_images):
        with col:
            st.image(image_path, use_container_width=True)  # Ensure images adjust to the column width

elif page == "Event Gallery":
    # Gallery Section
    st.header("Event Gallery")
    st.markdown("### Sneak Peek Into the Event")

    # List of image files to display in the gallery
    image_files = ["APP/image1.jpg", "APP/image2.jpg", "APP/image3.jpg", "APP/image4.jpg"]  # Replace with your image filenames

    # Loop through the images and display them in separate rows with natural size
    for image_file in image_files:
        img = Image.open(image_file)
        st.image(img, use_container_width=False)  # use_container_width=False to show the image in its natural size

elif page == "Services":
    # Services Section
    st.header("Our Services")
    st.markdown("### What We Offer")

    # E-Games Hosting Section
    with st.expander("**E-Games Hosting**"):
        st.markdown("""
        High-energy online gaming tournaments for competitive gamers. Join our e-games hosting events and showcase your gaming skills to a global audience. Prizes await the best players!
        """)
        e_games_image = Image.open("APP/e_games_sample.jpg")  # Replace with your e-games image
        st.image(e_games_image, caption="E-Games Tournament", use_container_width=True)

    # Summer Camps Section
    with st.expander("**Summer Camps**"):
        st.markdown("""
        Unforgettable summer camps with exciting activities and adventures. From outdoor challenges to team-building exercises, our summer camps are perfect for making lifelong memories.
        """)
        summer_camp_image = Image.open("APP/summer_camp_sample.jpg")  # Replace with your summer camp image
        st.image(summer_camp_image, caption="Summer Camp Adventure", use_container_width=True)

    # Survival Challenges Section
    with st.expander("**Survival Challenges**"):
        st.markdown("""
        Thrilling real-world challenges to test your limits and win big prizes. Experience the ultimate survival test in our abandoned city scenarios. Will you be the last one standing?
        """)
        survival_challenges_image = Image.open("APP/survival_challenge_sample.jpg")  # Replace with your survival challenges image
        st.image(survival_challenges_image, caption="Survival Challenge", use_container_width=True)

# Footer with sponsor logos and contact information
    st.markdown("---")

    # Contact Information Section
    st.markdown("""
    <div style="text-align: center;">
        <h4>Contact Us</h4>
        <p>For inquiries, email us at <b>mrbeastbussiness6@gmail.com</b></p>
        <p>Follow us on Instagram: <a href="https://www.instagram.com/game.zuri" target="_blank">@game.zuri</a></p>
    </div>
    """, unsafe_allow_html=True)

    # Sponsors Section
    st.markdown("<h4 style='text-align: center;'>Our Collaborators</h4>", unsafe_allow_html=True)

    # Display sponsor/collaborators logos in a horizontal row
    collaborator_images = [
        "APP/instagram.png",
        "APP/tiktok.png",
        "APP/snapchat.png",
        "APP/youtube.png"
    ]

    # Render images in columns
    cols = st.columns(len(collaborator_images))  # Create one column per image
    for col, image_path in zip(cols, collaborator_images):
        with col:
            st.image(image_path, use_container_width=True)  # Ensure images adjust to the column width
