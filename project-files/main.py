import json
import doctorsPage as dps
import doctorPage as dp
import mysqlDatabase as md
import pandas as pd
import mongodb_Database as mgdb

doctor_name = list()
doctor_titles = list()
doctor_gender = list()
doctor_expertise = list()
doctor_research = list()
doctor_phone = list()
doctor_location = list()
doctor_education = list()
        
def main():
    first_page = 1
    last_page = 1
    for pgNo in range(first_page, last_page+1):
        page = dps.doctorsPage("https://www.hopkinsmedicine.org/profiles/search?query=&page=" + str(pgNo))
        
        # getting the names and title that are displayed in the page
        names, title = page.get_doctorName_title()
        doctor_name.extend(names)
        doctor_titles.extend(title)
        profileLinks = page.getProfileLinks()
        for profileLink in profileLinks:

            # getting the profile links
            detailed_doctor = dp.doctorPage(profileLink)
            doctor_gender.append(detailed_doctor.getGender())

            # getting expertise and research interests
            exp, res = detailed_doctor.getExpertiseResearchInterests()
            doctor_expertise.extend(exp)
            doctor_research.extend(res)

            # getting the contact details
            cnct = detailed_doctor.getContactNo()
            doctor_phone.append(cnct)

            # getting the address or location
            loc = detailed_doctor.getLocation()
            doctor_location.append(loc)

            # getting the education details
            edu = detailed_doctor.getEducation()
            doctor_education.append(edu)

            # resetting the detailed page driver
            detailed_doctor.reset()
        
        # resetting the display page driver
        page.reset()

    d = {
		'Name' : doctor_name,
		'Title' : doctor_titles,
		'Gender' : doctor_gender,
		'Expertise' : doctor_expertise,
		'Research_Interests' : doctor_research,
		'Phone' : doctor_phone,
		'Location' : doctor_location,
		'Education' : doctor_education
	}

    df = pd.DataFrame(d)
    print(df)

    df.to_json('data.json', orient='records')

    with open('data.json') as file:
        data = json.load(file)

    with open('prettified_data.json', 'w') as file:
        json.dump(data, file, indent=4, sort_keys=True)
    
    sql_data = md.SQLdata(df)
    sql_data.createDatabase()
    sql_data.createTable()
    sql_data.insertRecordsDf()

    mongo_data = mgdb.mongoDatabase()
    mongo_data.connect()
    
if __name__ == "__main__":
    main()
