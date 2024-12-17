import streamlit as st
import base64
import webbrowser

image_path = "photo.jpg"

#canvas settings
st.set_page_config(
    page_title="Protfolio",  # App name shown in the browser tab
    page_icon=image_path ,# Emoji as an icon
    layout="wide"
)
#canvas styling
st.markdown("""
    <style>
    .stApp {
        background-color: #123950;
    }
    </style>
    """, unsafe_allow_html=True)

# Page Title
st.markdown("""
<h1 style="text-align:center;color:#008B8B;" >Presonal Protfolio</h1>
""",unsafe_allow_html=True)

# Img Section
image_path2 = "photo.jpg"

import os

# Function to convert the image to Base64
def get_base64_image(image_path2):
    with open(image_path2, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Path to your image
image_path2 = "photo.jpg"  # Make sure this image exists at the given path

try:
    # Get Base64 encoded image
    base64_img = get_base64_image(image_path2)

    # Add an image with rounded corners using Base64 and CSS
    st.markdown(
        f"""
        <style>
        .rounded-img {{
            border-radius: 50%; /* Makes the image circular */
            width: 200px; /* Adjust width */
            height: 200px; /* Adjust height */
            object-fit: cover; /* Ensures the image fits properly */
        }}
        </style>
        <img src="data:image/jpg;base64,{base64_img}" class="rounded-img">
        """,
        unsafe_allow_html=True
    )

except FileNotFoundError as e:
    st.error(f"Image not found: {str(e)}")
except Exception as e:
    st.error(f"An error occurred: {str(e)}")



#Small intro
# Columns for layout
col1, col2 = st.columns(2)

with col1:
    # st.image(image_path, width=200, caption="Muzaffar")
    st.header("Hello! I am Muzaffar.")

with col2:
    st.subheader("Experienced Data Analyst with 1+ years of industry expertise.")


col1, col2,col3,col4 = st.columns(4)
with col1:
    btn1 = st.button("Let's Connect")
    if btn1:
        webbrowser.open_new_tab("https://www.linkedin.com/in/mdmuzaffaransari-5a2ab6209")
        st.balloons()
with col2:
    btn2 = st.button("Email ")
    if btn2:
        webbrowser.open_new_tab("mailto:mdmuzaffaransari307@gmail.com")
        st.balloons()

# profile Summary
st.markdown("""
    <h3 style="color:aqua;">Summary</h3>
""",unsafe_allow_html=True)
st.write("""
Experienced Data Analyst with 1+ years of industry expertise. Proficient in Python, SQL, and Excel for data cleaning, modeling, and visualization. Detail-oriented and analytical thinker with strong problem-solving skills.Excellent team player with effective communication and project management abilities.
""")
st.progress(100)

# Technical Skills section
col1,col2=st.columns(2)
with col1:
    st.markdown(
        """
        <h3 style="color:aqua;">Technical Skills</h3>
         <h5 >Programming Language </h3>
         
         <li> Python</li>
         <li> SQL</li>
          <h5 ">Analytical Tools</h3>
         <li> Advance Excel</li>
         <li> Power BI</li>
           <li> Tableau</li>
         <li> Power Query</li>
         <li> DAX</li>
          <h5 ">Technology / Framwork</h3>
         <li> Flask</li>
         <li> Git And GitHub</li>
         <li> Streamlit</li>
         <li> Pandas</li>
         <li> Seaborn</li>
         <li> Matploitlib</li>
        
        """,
        unsafe_allow_html=True
    )
    #relevent course work section
with col2:
    st.markdown(
        """
        <h3 style="color:aqua;">Relevent Coursework</h3>
         <h5 ">Data Integrity</h3>
        
          <h5 ">Data Visulazation</h5>
         
        <h5>Data Governance</h5>
               <h5 >Data Manipulation</h5>
           <h5 >Generative AI</h3>
            <h5 >Data Mining </h3>
                <h5>Requirement Gathering</h3>
              <h5>Bussiness Impact Analysis </h3>
                <h5>Problem Solving</h3>
              <h5>Effective Communication </h3>
  

        """,
        unsafe_allow_html=True
    )
    #Extra circular
st.progress(100)
st.markdown("""
 <h3 style="color:aqua;">Extra Curricular & Certification</h3>
 <h3 style="color:#5F9EA0;font-size:25px">Extra Curricular</h3> 
  <h4 > Accenture North America Data Analytics and Visualization Job Simulation on Forage</h3>
  <p> <b>** </b> Completed a simulation focused on advising a hypothetical social media client as a Data Analyst at Accenture</p>
  <p> <b>** </b> Cleaned, modelled and analyzed 7 datasets to uncover insights into content trends to inform strategic decisions</p>
  <p> <b>** </b> Prepared a PowerPoint deck and video presentation to communicate key insights for the client and internal stakeholders</p>
  
 
  <h4 > Quantium Data Analytics Job Simulation on Forage</h3>
  <p> <b>** </b> Completed a job simulation focused on Data Analytics and Commercial Insights for the data science team.</p>
  <p> <b>** </b> Developed expertise in data preparation and customer analytics, utilizing transaction datasets to extract valuable insights and deliver data-driven commercial recommendations.</p>
  
 <p> <b>** </b> Leveraged acquired data analytics and insights from previous tasks to create comprehensive reports for the Category Manager, facilitating informed strategic decisions and enhancing commercial applications.</p>
  
  
 <!-- Certification -->
<h3 style="color:#5F9EA0;font-size:25px">Certification</h3> 
 <h4 > Google Data Analytics</h3>
 
  <p> <b>** </b>  Comprehensive Data Analysis Skills: Gained proficiency in data cleaning, visualization, and
analysis using tools like Excel, SQL, R, and Tableau</p>

  <p> <b>** </b> Data-Driven Decision Making: Developed the ability to apply statistical techniques and insights to
solve real-world business problems.
</p>
  
 <p> <b>** </b> Capstone Project: Completed a hands-on case study, showcasing end-to-end data
analysis and reporting.
</p>

 <h4 > LinkedIn Data Analytics</h3>
  <p> <b>** </b>  Created interactive dashboards using tools like Tableau or Power BI to present LinkedIn analytics insights to stakeholders</p>
  <p> <b>** </b> Used LinkedIn analytics to measure ROI and recommend data-driven strategies for improved marketing effectiveness.
</p> 
 <p> <b>** </b> Developed weekly and monthly LinkedIn performance reports for senior management, highlighting actionable insights and areas of improvement.
</p>

""",
unsafe_allow_html=True)

st.progress(100)
#Projects
st.markdown("""
<h3 style="color:aqua;">Projects</h3>
""",unsafe_allow_html=True)
col1,col2=st.columns(2)
with col1:
    st.markdown("""
     <h4 > API Building </h3>
  <p> <b>** </b>  Developed an IPL Dataset API using Python and flask to provide structured access to cricket data,
including team statistics, player performance, and match details. Implemented endpoints for querying
data, enabling seamless integration with analytical tools and applications.
</p>
<p><b>Technology Used</b></p>
<p>Python, Pandas, Flask,JSON</p>

    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
     <h4 > Indian Startups Funds Analysis </h3>
  <p> <b>** </b>  Built an interactive dashboard using Python and Streamlit to analyze funding trends in Indian startups.
Visualized key insights like funding amounts, sectors, and investor patterns for data-driven decisionmaking..
</p>
<p><b>Technology Used</b></p>
<p>Python, Pandas, Streamlit</p>

    """, unsafe_allow_html=True)
col1,col2=st.columns(2)
with col1:
    st.markdown("""
     <h4 > IPL Dashboard</h3>
  <p> <b>** </b>Created an interactive IPL Dashboard using Tableau, Excel, and Power Query to analyze team and player
performance , match statistics , and season trends . Automated data cleaning and transformation for
seamless updates and dynamic visualizations</p>
<p><b>Technology Used</b></p>
<p>Python, Pandas,Tableau, Calculation</p>
<a href="https://public.tableau.com/app/profile/md.muzaffar.ansari/viz/Ipl_17338515473090/Ipl"> Live Dashboard</a>
""", unsafe_allow_html=True)

with col2:
    st.markdown("""
     <h4 > Pharma Sales Analysis Dashboard</h3>
  <p> <b>** </b>This dashboard empowers stakeholders to identify growth opportunities, 
  optimize sales strategies, and make data-driven 
  decisions to enhance market performance</p>
<p><b>Technology Used</b></p>
<p>Python, Pandas,POwer BI, Power Query,DAX</p>

    """, unsafe_allow_html=True)


# Define the progress percentage
progress = 70

# Create the progress bar using Streamlit Markdown



