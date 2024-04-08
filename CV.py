# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 09:48:40 2021

@author: Alex
"""

### 

# Import Libraries
from fpdf import FPDF

# PDF variables
WIDTH = 210
HEIGHT = 297
Applicant = 'Alex Rathke'
Email = 'rathkealex@gmail.com'
Phone= '+353 85 848 3531'
Profession = 'Data Analyst'
Nationality = 'German - South African'
Profile_header = 'Profile'
Education = 'Education'
Career = 'Career'
Location = 'Dublin, Ireland'

# Create Title function
def create_title_page(pdf):
    pdf.set_font('Arial', '', 30)
    
    ### Name of applicant
    # Line break
    pdf.ln(5)
    # Position Applicant variable on page
    pdf.cell(1)
    pdf.write(5, f"{Applicant}")
    
    ### Profession of applicant
    # Line break
    pdf.ln(10)
    pdf.set_font('Arial', '', 12)
    # Position Profession variable on page
    pdf.cell(1)
    pdf.write(5, f"{Profession} / {Email} / {Phone} / {Nationality}")
    
    ### Profile Header
    # Line break
    pdf.ln(10)
    pdf.set_font('Arial', 'B', 12)
    # Position Profile variable on page
    pdf.cell(10)
    pdf.write(5, f'{Profile_header}')
    
    ### Write Profile
    # Line break
    pdf.ln(10)
    pdf.set_font('Arial', '', 12)
    pdf.cell(1)
    pdf.write(4, 'A self-motivated, entrepreneurial business professional with experience of collection, extraction')
    # Line break
    pdf.ln(7)
    pdf.cell(1)
    pdf.write(4, 'storage & data visualisation expertise. Time-managed and organised individual who strives for')
    # Line break
    pdf.ln(7)
    pdf.cell(1)
    pdf.write(4, 'concise communication & punctual attendance.')

    ### Skills
    # Line break
    pdf.ln(10)
    pdf.set_font('Arial', 'B', 12)
    pdf.write(4, 'Skills:')    
    pdf.set_font('Arial', '', 12)
    # Add Skill
    pdf.cell(1)
    pdf.write(4, 'Tableau,' + ' ' + 'Alteryx,' + ' ' + 'Trifacta,' + ' ' + 'Python,' + ' ' + 'SQL,' + ' ' + 'Excel,' + ' ' + 'Hudl,' + ' ' + 'InStat,' + ' ' + 'Wyscout,'+ ' ' + 'Opta,')
    # Line break
    pdf.ln(7)
    
    ### Education - most previous first then backwards
    # Line break
    pdf.ln(4)
    pdf.set_font('Arial', 'B', 12)
    # Position Education variable on page
    pdf.cell(10)
    pdf.write(4, f'{Education}')
    
    ### MSc - Limerick
    pdf.set_font('Arial', '', 12)
    # Line break
    pdf.ln(10)
    pdf.cell(1)
    pdf.write(4, '2015 - 2016' + ' ' + ' ' + 'University of Limerick, Ireland')
    # Line break
    pdf.ln(7)
    pdf.set_font('Arial', 'I', 12)
    pdf.cell(1)
    pdf.write(4, "MSc. (Hons) Sports Performance ->")
    
    # Add in link to MSc
    pdf.set_font('Arial', '', 12)
    # Line break
    #pdf.ln(7)
    pdf.cell(1)
    pdf.write(4, 'Visit ')
    # Then put a blue underlined link
    pdf.set_text_color(0, 0, 255)
    pdf.set_font('', 'U')
    pdf.write(4, 'Journal article', 'https://rua.ua.es/dspace/bitstream/10045/68771/1/jhse_Vol_12_N_proc2_S514-S529.pdf')

    ### BSc - Dublin
    pdf.set_text_color(0, 0, 0)
    pdf.set_font('Arial', '', 12)
    # Line break
    pdf.ln(10)
    pdf.cell(1)
    pdf.write(4, '2011 - 2011' + ' -> ' + 'University of College Dublin, Ireland')
    # Line break
    pdf.ln(7)
    pdf.set_font('Arial', 'I', 12)
    pdf.cell(1)
    pdf.write(4, "BSc. (Hons) Sports & Exercise Management")
    
    ### Career
    # Line break
    pdf.ln(12)
    pdf.set_font('Arial', 'B', 12)
    # Position Career variable on page
    pdf.cell(10)
    pdf.write(4, f'{Career}')
    
    ### Job 1
    # Line break
    pdf.ln(10)
    pdf.set_font('Arial', 'B', 12)
    pdf.set_text_color(0, 0, 255)
    # Add Job Title, Company & Location
    pdf.cell(1)
    pdf.write(4, 'Data Analyst' + ' @ ' + 'Aon ACIA' + ' ' + '(Dublin, Ireland)')
    # Line break
    pdf.ln(7)
    pdf.set_font('Arial', '', 12)
    pdf.set_text_color(0, 0, 0)
    # Add Start & End dates of job
    pdf.cell(1)
    pdf.write(4, 'June 2018 - current')
    # Line break
    pdf.ln(7)
    # Add Job roles & responsibilities
    pdf.cell(1)
    pdf.write(4, '-	Work in a team where we build data processes in Alteryx, Python and Trifacta. We also design')
    # Line break
    pdf.ln(7)
    # Add Job roles & responsibilities
    pdf.cell(1)
    pdf.write(4, 'maintain various Tableau dashboards for customers & colleagues. Other work involves the training')
    # Line break
    pdf.ln(7)
    # Add Job roles & responsibilities
    pdf.cell(1)
    pdf.write(4, 'of colleagues in technologies mentioned as well as general ad-hoc reporting & insight tasks.')
    
    ### Job 2
    # Line break
    pdf.ln(10)
    pdf.set_text_color(0, 0, 255)
    pdf.set_font('Arial', 'B', 12)
    # Add Job Title, Company & Location
    pdf.cell(1)
    pdf.write(4, 'Data Journalist' + ' @ ' + 'BET CENTRAL' + ' ' + '(Part-Time)')
    # Line break
    pdf.ln(7)
    pdf.set_font('Arial', '', 12)
    pdf.set_text_color(0, 0, 0)
    # Add Start & End dates of job
    pdf.cell(1)
    pdf.write(4, 'July 2019 - current')
    # Line break
    pdf.ln(7)
    # Add Job roles & responsibilities
    pdf.cell(1)
    pdf.write(4, '-	Use statistical data on football players and teams to provide contextual insights as a data')
    # Line break
    pdf.ln(7)
    # Add Job roles & responsibilities
    pdf.cell(1)
    pdf.write(4, 'journalist. Examine trends and analyse topics which allows fans to understand the use of numbers')
    # Line break
    pdf.ln(7)
    # Add Job roles & responsibilities
    pdf.cell(1)
    pdf.write(4, 'in football. Majority of coverage focuses on the South African soccer premiership.')
    
    
    ### Job 3
    # Line break
    pdf.ln(10)
    pdf.set_text_color(0, 0, 255)
    pdf.set_font('Arial', 'B', 12)
    # Add Job Title, Company & Location
    pdf.cell(1)
    pdf.write(4, 'Co-Founder' + ' @ ' + 'Laduma Analytics' + ' ' + '(Part-Time)')
    # Line break
    pdf.ln(7)
    pdf.set_font('Arial', '', 12)
    pdf.set_text_color(0, 0, 0)
    # Add Start & End dates of job
    pdf.cell(1)
    pdf.write(4, 'July 2019 - current')
    # Line break
    pdf.ln(7)
    # Add Job roles & responsibilities
    pdf.cell(1)
    pdf.write(4, '-	Formed this company with a colleague where we examine football in South Africa using data')
    # Line break
    pdf.ln(7)
    # Add Job roles & responsibilities
    pdf.cell(1)
    pdf.write(4, 'We provide statistical analysis & analytics to help bring teams a competitive edge')
   
Contents = ''
    
def create_content_table (pdf):
    ### Job 4
    # Line break
    pdf.ln(10)
    pdf.set_text_color(0, 0, 255)
    pdf.set_font('Arial', 'B', 12)
    # Add Job Title, Company & Location
    pdf.cell(1)
    pdf.write(4, 'Data Analyst' + ' @ ' + 'Dundalk FC' + ' ' + '(Part-Time)')
    # Line break
    pdf.ln(7)
    pdf.set_font('Arial', '', 12)
    pdf.set_text_color(0, 0, 0)
    # Add Start & End dates of job
    pdf.cell(1)
    pdf.write(4, 'June 2019 - October 2019')
    # Line break
    pdf.ln(7)
    # Add Job roles & responsibilities
    pdf.cell(1)
    pdf.write(4, '-	Analyse and scout football players for recruitment purposes. Conduct SWOT analysis of the club')
    # Line break
    pdf.ln(7)
    # Add Job roles & responsibilities
    pdf.cell(1)
    pdf.write(4, 'in comparison to previous campaign and vs peers in the league. Provide statistical scouting')
    # Line break
    pdf.ln(7)
    # Add Job roles & responsibilities
    pdf.cell(1)
    pdf.write(4, "analysis for the club's Champions & Europa League qualification periods.")
    
    ### Job 5
    # Line break
    pdf.ln(10)
    pdf.set_text_color(0, 0, 255)
    pdf.set_font('Arial', 'B', 12)
    # Add Job Title, Company & Location
    pdf.cell(1)
    pdf.write(4, 'Data Analyst' + ' @ ' + 'Brand Athlete Agency' + ' ' + '(Part-Time)')
    # Line break
    pdf.ln(7)
    pdf.set_font('Arial', '', 12)
    pdf.set_text_color(0, 0, 0)
    # Add Start & End dates of job
    pdf.cell(1)
    pdf.write(4, 'January 2019 - August 2019')
    # Line break
    pdf.ln(7)
    # Add Job roles & responsibilities
    pdf.cell(1)
    pdf.write(4, '-	Help set-up a scouting and analysis pathway to identify talent for scouts to analyse via video.')
    # Line break
    pdf.ln(7)
    # Add Job roles & responsibilities
    pdf.cell(1)
    pdf.write(4, 'Build player comparison models across leagues and/or positions in Alteryx and used Tableau to')
    # Line break
    pdf.ln(7)
    # Add Job roles & responsibilities
    pdf.cell(1)
    pdf.write(4, 'provide customer clubs with a range of back-up player options for the upcoming transfer markets.')
    
    ### Job 6
    # Line break
    pdf.ln(10)
    pdf.set_text_color(0, 0, 255)
    pdf.set_font('Arial', 'B', 12)
    # Add Job Title, Company & Location
    pdf.cell(1)
    pdf.write(4, 'Performance & Data Analyst' + ' @ ' + 'Tipperary GAA' + ' ' + '(Part-Time)')
    # Line break
    pdf.ln(7)
    pdf.set_font('Arial', '', 12)
    pdf.set_text_color(0, 0, 0)
    # Add Start & End dates of job
    pdf.cell(1)
    pdf.write(4, 'September 2017 - June 2019')
    # Line break
    pdf.ln(7)
    # Add Job roles & responsibilities
    pdf.cell(1)
    pdf.write(4, '-	Part of a team of analysts where collection of data on match days and video footage was used')
    # Line break
    pdf.ln(7)
    # Add Job roles & responsibilities
    pdf.cell(1)
    pdf.write(4, 'to enhance & provide feedback to management at half-time on tactics and strategies. Designed')
    # Line break
    pdf.ln(7)
    # Add Job roles & responsibilities
    pdf.cell(1)
    pdf.write(4, 'post-match player reports as well as Opposition analysis & database management.')
    
    ### Job 7
    # Line break
    pdf.ln(10)
    pdf.set_text_color(0, 0, 255)
    pdf.set_font('Arial', 'B', 12)
    # Add Job Title, Company & Location
    pdf.cell(1)
    pdf.write(4, 'Performance & Data Analyst' + ' @ ' + 'Doha, Qatar' + ' ' + '(Part-Time)')
    # Line break
    pdf.ln(7)
    pdf.set_font('Arial', '', 12)
    pdf.set_text_color(0, 0, 0)
    # Add Start & End dates of job
    pdf.cell(1)
    pdf.write(4, 'September 2017 - May 2018')
    # Line break
    pdf.ln(7)
    # Add Job roles & responsibilities
    pdf.cell(1)
    pdf.write(4, '-	Remote-working analysis opportunity to help out with Opposition scouting & set-piece analysis.')
    # Line break
    pdf.ln(7)
    # Add Job roles & responsibilities
    pdf.cell(1)
    pdf.write(4, '-	Player profiling reports were written and designed in Tableau.')
     
    ### Job 8
    # Line break
    pdf.ln(10)
    pdf.set_text_color(0, 0, 255)
    pdf.set_font('Arial', 'B', 12)
    # Add Job Title, Company & Location
    pdf.cell(1)
    pdf.write(4, 'Guest TV Analyst' + ' @ ' + 'Bundesliga Show' + ' ' + '(Part-Time)')
    # Line break
    pdf.ln(7)
    pdf.set_font('Arial', '', 12)
    pdf.set_text_color(0, 0, 0)
    # Add Start & End dates of job
    pdf.cell(1)
    pdf.write(4, 'March 2016 - June 2017')
    # Line break
    pdf.ln(7)
    # Add Job roles & responsibilities
    pdf.cell(1)
    pdf.write(4, '-	TV show analysis which examined the performances of African football players in the German.')
    # Line break
    pdf.ln(7)
    # Add Job roles & responsibilities
    pdf.cell(1)
    pdf.write(4, 'Bundesliga. With the producer and host, the script was written as well as the video analysis')
    # Line break
    pdf.ln(7)
    # Add Job roles & responsibilities
    pdf.cell(1)
    pdf.write(4, 'was edited. Presented the use case for statistical metrics to measure performance.')


# Create function
def create_report(filename=r"C:\Users\Alex\Desktop\CV\CV.pdf"):
    # Portrait, page size in millimetres and Letter format
    pdf = FPDF('P', 'mm', 'Letter')
    
    ''' First Page '''
    # Add extra page
    pdf.add_page()
    
    # Title Page
    create_title_page(pdf)
    # Add Letter head image
    #pdf.image(r"C:\Users\Alex\Desktop\CV\CV background 1.png", 
    #          0, 0, 75, HEIGHT)
    # Add rectangular border
    #pdf.rect(0, 0, 75, HEIGHT, style = 'D')
    
    # Add profile icon
    pdf.image(r"C:\Users\Alex\Desktop\CV\Profile_icon.png",
              5, 32, 15, 10)
    
    # Add Education image
    pdf.image(r"C:\Users\Alex\Desktop\CV\Education.png",
              5, 77, 12, 8)
    
    # Add Career image
    pdf.image(r"C:\Users\Alex\Desktop\CV\Career.png",
              5, 122, 15, 10)
   
    ''' Second Page - CV continued '''
    # Add extra page
    pdf.add_page()
    
    create_content_table(pdf)
    # Add Letter head image
    #pdf.image(r"C:\Users\Alex\Desktop\CV\CV background 2.png", 
    #          0, 0, 75, HEIGHT)
    # Add rectangular border
    #pdf.rect(0, 0, 75, HEIGHT, style = 'D')
    
    ### Languages
    # Line break
    pdf.ln(15)
    pdf.set_font('Arial', 'B', 12)
    pdf.write(4, 'Languages:')    
    pdf.set_font('Arial', '', 12)
    # Add Skill
    pdf.cell(1)
    pdf.write(4, '   English (fluent);' + ' ' + ' ' + 'German (fluent);' + ' ' + ' ' + 'French (beginner)')
    
    ### Hobbies
    # Line break
    pdf.ln(10)
    pdf.set_font('Arial', 'B', 12)
    pdf.write(4, 'Hobbies:')    
    pdf.set_font('Arial', '', 12)
    # Add Skill
    pdf.cell(10)
    pdf.write(4, 'Swimming,' + ' ' + 'Cycling,' + ' ' + 'Adventure sports,' + ' ' + 'Travelling,' + ' ' + 'Camping,' + ' ' + 'Coding')
    
    # Line break
    pdf.ln(10)
    # Tableau CV
    pdf.set_font('Arial', 'B', 12)
    pdf.write(4, 'Tableau CV:')
    pdf.set_font('Arial', '', 12)
    pdf.cell(4)
    pdf.write(4, 'Please click')
    pdf.cell(1)
    # Then put a blue underlined link
    pdf.set_text_color(0, 0, 255)
    pdf.set_font('', 'U')
    pdf.write(4, 'here', 'https://tabsoft.co/3fyHNIv')
    
    ### Fun Fact
    # Line break
    pdf.ln(10)
    # Set the colour to black font again
    pdf.set_text_color(0, 0, 0)
    pdf.set_font('Arial', 'B', 12)
    pdf.write(4, 'Fun fact:')    
    pdf.set_font('Arial', '', 12)
    # Add Skill
    pdf.cell(10)
    pdf.write(4, 'I cycled around Ireland unsupported over 7 days in 2020.')

    ### Python design
    # Line break
    pdf.ln(10)
    pdf.set_font('Arial', '', 12)
    pdf.write(4, '*This CV was written & designed in Python code.*')
    pdf.output(filename)
if __name__ == '__main__':
    create_report()