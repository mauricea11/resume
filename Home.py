from pathlib import Path
import streamlit as sl
from PIL import Image
from streamlit import link_button

# Path Settings


DIR = Path(__file__).parent
CSS = DIR / "styles" / "main.css"
RESUME_PATH = DIR / "assets/Maurice August Resume sh.pdf"
PROFILE_PICTURE = DIR / "assets/Headshot.jpeg"

#Resume Details

TITLE = "Maurice August Resume"
ICON = "👋🏾"
NAME = "Maurice August"
DESCRIPTION = "Final year computer science student interested in using data science to make the world safer"
# SOCIAL = {
#     "Github": "https://github.com/mauricea11/mauricea11/blob/main/README.md",
#     "Twitch": "ilikerice9"
# }

sl.set_page_config(page_title=TITLE, page_icon=ICON)



sl.sidebar.markdown('''
# Sections

- [Home](#hello-world)
- [Qualifications](#qualifications)
- [Skills](#technical-skills)
- [Experience](#professional-experience)
''', unsafe_allow_html=True)

sl.title("Hello world!")
 


#Loading Files

with open(CSS) as c: 
    sl.markdown("<style>{}</style>".format(c.read()), unsafe_allow_html=True)

with open(RESUME_PATH, "rb") as resume:
    PDF_BYTE = resume.read()
    picture = Image.open(PROFILE_PICTURE)

#Hero

col1, col2 = sl.columns(2, gap="small")
with col1:
    sl.image(picture, width=230)

sl.write("#")

with col2:
    sl.title(NAME)
    sl.write(DESCRIPTION)
    # sl.download_button(label= "📄 Download resume", data=PDF_BYTE, file_name=RESUME_PATH.name, mime="application/octet-stream")
    # sl.write("📧 mauriceaugust@outlook.com")
    sl.link_button("Github", "https://github.com/mauricea11?tab=repositories")


#Social

# cols = sl.columns(len(SOCIAL))

# for i, (platform, link) in enumerate(SOCIAL.items()):
#     cols[i].write(f"[{platform}]({link})")

#General Experience
sl.write("#")
sl.subheader("📈 Qualifications")
sl.write("""
    - 5 years of Object Oriented programming experience
    - 3 years of experience with financial service software
    - 5 years of experience with Microsoft Office, in particular Excel
    - Passion for inventing and figuring out unique ways to do tasks
"""
)

#Technical skills
sl.write("#")
sl.subheader("🛠️ Technical Skills")
sl.write(""" 
    - Python (Pandas, Flask), Java, JavaScript, R, Swift
    - Git/Github
    - Tableau
    - Postgres, MySQL
    - Excel 
    - Unity
    - Heroku
""")

#Experience
sl.write("#")
sl.subheader("🧑🏽‍💼Professional Experience")
sl.write("---")

#Most recent job

sl.write("**IT Services LLC | Full-stack Developer**"
)
sl.write("""
    July 2022 - August 2022 
""")
sl.write("""
    - Designed login page for company website using JavaScript, HTML, and CSS, enabling users to have cookies saved and redirecting them to the student or instructor websites
    - Created router files in Node JS allowing for easy retrieval or modification of information using GET and POST requests
    - Attended standup meetings 3 times per week to discuss and resolve issues in code, and new features to implement
"""
)

#2ND
sl.write("**Code Path | SITE Intern – Full-stack Developer**"
)
sl.write("""
    May 2022 – June 2022 
""")
sl.write("""
    - Built weekly full stack projects (Thursday – Friday) spanning various technologies like HTML, CSS, React, Node, and SQL
    - Engaged in stand-up meetings where each intern would give an update on daily exercise completion and challenges faced
    - Participated in lectures that explained full stack concepts before joining a pod of 3-5 interns to complete a daily challenge
"""
)

sl.write("**CUNY Research Foundation & Office of Mayor Eric Adams | Data Analyst**"
)
sl.write("""
    December 2021 - March 2022 
""")
sl.write("""
    - Cleaned several thousand rows of governmental department data using the Excel data analysis feature and common String formulas in order to prevent inaccurate visualizations
    - Created visualizations with Tableau and Excel that showed the highest spending category within each governmental department to prepare mayors new financial budget
    - Used statistical principles such as correlation, regression analysis, and confidence intervals to assess which governmental department had the highest spending and why
"""
)

#3RD
sl.write("**Visa Inc. | Global Product Intern**"
)
sl.write("""
    May 2021 - July 2021 
""")
sl.write("""
    - Conducted a study of comparing VASs (Value Added Services) & similar competitor offerings with the Subscription Management team to determine which countries to offer the VASs & update the product roadmap
    - Presented the research study to 2 senior product managers & product head to effectively price & market VASs to improve sales
    - Coordinated 5 calls with global senior product managers in Europe & North America to assess sales efforts for Visa Token Service - VASs & review to client feedback to resolve any issues so we could better market the products
"""
)

#4TH
sl.write("**TD Bank | Product Management Summer Analyst**"
)
sl.write("""
    May 2020 - Aug. 2020 
""")
sl.write("""
    - Developed a walkthrough demo & chatbot using jQuery & Apex code within Salesforce nCino & WalkMe apps to assist users on how to create a contact object correctly to avoid discrepancies
    - Discovered & implemented a free database of U.S. ZIP codes to ensure accurate ZIP codes are used within client & deal contracts that saved 8 days of work & $1000+ of fees to utilize private databases
    - Created an app page in Salesforce in 3 days using custom objects & validation rules to showcase foundational knowledge of Salesforce within our Scrum training program
"""
)

#5TH
sl.write("**Federal Reserve Bank of New York | Junior Supervision Analyst**"
)
sl.write("""
    Feb. 2019 - Oct. 2019 
""")
sl.write("""
    - Analyzed a database of 700 keywords from a Natural Language Processing algorithm for duplicates to accurately automate bank examination document responses that reduced the rate of duplicates by 70% & decreased a week worth of manual work
    - Generated statistics on over 100 financial instrument training data in Excel that determined if employees found it beneficial & consolidated training offerings which saved the company ~$5000 per course
"""
)
