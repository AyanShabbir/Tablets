import streamlit as st

# URL for the logo
logo_url = "https://raw.githubusercontent.com/AyanShabbir/Tablets/main/LOGObg.png"  # Use raw URL for direct image access
st.set_page_config(page_title="Tablets Clinic", layout="wide")

# Sidebar for navigation
st.sidebar.title("Navigation")
options = ["Home", "Departments", "Contact Us"]
selection = st.sidebar.radio("Go to", options)

# Header with logo (displayed on every page)
st.markdown("""
    <style>
        .header {
            display: flex;
            align-items: center;
            justify-content: center; /* Center content */
            padding: 10px 0;
            position: relative; /* Positioning for absolute logo */
        }
        .logo {
            position: absolute; /* Position logo absolutely */
            left: 20px; /* Adjust space from left */
            width: 100px; /* Adjust size here */
        }
        .main-title {
            text-align: center; /* Center the title */
            color: #2d572c; /* Dark green for the title */
            font-size: 24px; /* Adjust font size if needed */
            margin-left: 120px; /* Space for the logo */
            margin-top: 0; /* Remove top margin */
        }
    </style>
""", unsafe_allow_html=True)

# Display the logo
st.markdown(f"""
    <div class="header">
        <img src="{logo_url}" class="logo" />
        <h1 style="display: {'block' if selection == 'Home' else 'none'};">Welcome to Tablets Clinic</h1>
    </div>
""", unsafe_allow_html=True)

# Additional styles for the rest of the page
st.markdown("""
    <style>
        .card {
            background-color: white;
            border-radius: 10px;
            padding: 20px;
            margin: 10px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }
        .card p {
            color: #000000; /* Set paragraph text color to black */
        }
        h3 {
            color: #2d572c; /* Dark green for headings */
        }
        p {
            color: #dedede; /* Light gray for text */
        }
        .contact {
            background-color: #2d572c; /* Dark green for contact section */
            border-radius: 10px;
            padding: 20px;
            margin: 10px 0;
            color: #ffffff; /* White for contact text */
        }
        body {
            background-color: #dedede; /* Light gray background for the main body */
        }
    </style>
""", unsafe_allow_html=True)

# Home Section
if selection == "Home":
    st.markdown("<h3 style='text-align: center;'>Your Health, Our Priority</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>At Tablets Clinic, we offer a variety of services to cater to your health needs.</p>", unsafe_allow_html=True)
    
    # Adding additional spacing
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Adding additional information
    st.markdown("""
    <h3 style='text-align: center; color: #2d572c;'>Why Tablets?</h3>
    <ul style='text-align: center; list-style-type: none; padding: 0;'>
        <li style='margin: 10px 0; font-size: 18px;'>Experienced, Highly Qualified and PMC Registered Doctors</li>
        <li style='margin: 10px 0; font-size: 18px;'>State-of-the-Art Laboratory</li>
        <li style='margin: 10px 0; font-size: 18px;'>Associated Authentic Pharmacy</li>
    </ul>
""", unsafe_allow_html=True)
    
    # Adding images to the Home page
    st.image("https://scontent.fpew2-1.fna.fbcdn.net/v/t39.30808-6/277790565_108630745157561_6472859447440928934_n.jpg?_nc_cat=101&ccb=1-7&_nc_sid=833d8c&_nc_ohc=SrnIlVCDOiEQ7kNvgF9X4pt&_nc_ht=scontent.fpew2-1.fna&oh=00_AYDj5BF4fvrhzwZhh9S_6bAwCkUJQzCiPLDWQhl0MQIuoA&oe=66F51173", caption="Tablets Clinic", use_column_width=True)
    st.image("https://scontent.fpew2-1.fna.fbcdn.net/v/t39.30808-6/278571671_110159415004694_5008292888592397998_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=833d8c&_nc_ohc=XZ2cQcagCT4Q7kNvgFtma2r&_nc_ht=scontent.fpew2-1.fna&_nc_gid=AgEuXal5kKES_fDFyxhjbdn&oh=00_AYBuNzP8ZeuDnSCOzN5RSFNySlKH5kRk0lBIHH8CCjkoqw&oe=66F50A29", caption="First Aid Room", use_column_width=True)
    st.image("https://scontent.fpew2-1.fna.fbcdn.net/v/t39.30808-6/278494893_108779405142695_775308775597318433_n.jpg?_nc_cat=101&ccb=1-7&_nc_sid=833d8c&_nc_ohc=-m4Q5HkajE8Q7kNvgHrIPZl&_nc_ht=scontent.fpew2-1.fna&_nc_gid=A6DOG4Y-gMgOl7WDTE4gi_q&oh=00_AYCJbvP3JZSX3TOZ4iRtW1FfZDHgAXTz1Vl_IbjTXl_25g&oe=66F4F95D", caption="Reception", use_column_width=True)

# Departments Section
elif selection == "Departments":
    st.markdown("### Our Departments")
    cols = st.columns(3)
    department_info = {
        "Cardiology": "Heart health and wellness.",
        "Pediatrics": "Care for children and adolescents.",
        "Orthopedics": "Bone and joint treatment.",
        "Dermatology": "Skin care and treatment.",
        "Psychology": "Mental health and wellness.",
        "General Medicine": "Comprehensive healthcare services."
    }

    for i, (department, description) in enumerate(department_info.items()):
        with cols[i % 3]:
            st.markdown(f"<div class='card'><h3>{department}</h3><p>{description}</p></div>", unsafe_allow_html=True)

# Contact Us Section
elif selection == "Contact Us":
    st.markdown("""
        <div class='contact'>
            <p>For inquiries, please reach out via:</p>
            <p>Phone: 0331-8789184</p>
            <p>Telephone: (0544) 631119</p>
            <p><a href='https://www.facebook.com/p/Tablets-Clinics-100083301034236/' target='_blank'>Visit us on Facebook</a></p>
        </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("© 2024 Tablets Clinic. All rights reserved.")
