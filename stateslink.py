from selenium import webdriver	
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
a=input()
if a =='Tamil Nadu':
    browser=webdriver.Firefox()
    browser.get('https://elections.tn.gov.in/rollpdf/DraftRoll_09112022.aspx')
    dname='சென்னை'
    Dist=Select(browser.find_element("xpath",'//*[@id="ddl_District"]'))
    Dist.select_by_visible_text(dname)  
    ACname='பெரம்பூர்'
    AC=Select(browser.find_element("xpath",'//*[@id="ddl_Assembly"]'))
    AC.select_by_visible_text(ACname) 
    browser.execute_script("window.scrollTo(0, 200)")
    browser.find_element("xpath",'/html/body/form/div[3]/div/div[3]/div/div/div/div[3]/div/div[2]/div[3]/div/input').click()
elif a =='Andaman & Nicobar Islands':
    browser=webdriver.Firefox()
    browser.get('https://ceodaman.nic.in/ElectoralRoll/DraftER2022/polling_station_wise_roll_in_eng.htm')
elif a == 'Andhra Pradesh':
    browser=webdriver.Firefox()
    browser.get('https://ceoaperolls.ap.gov.in/AP_Eroll_2022/Rolls')
    dname='2-Vizianagaram'
    Dist=Select(browser.find_element("xpath",'//*[@id="ddlDist"]'))
    Dist.select_by_visible_text(dname)
    ACname='12-Parvathipuram (SC)'
    AC=Select(browser.find_element("xpath",'//*[@id="ddlAC"]'))
    AC.select_by_visible_text(ACname)
    browser.find_element("xpath",'/html/body/div[3]/div/div/div[2]/div/form/div[6]/div/input').click()
elif a == 'Arunachal Pradesh':
    browser=webdriver.Firefox()
    browser.get('https://ceoarunachal.nic.in/droll2023.html')
elif a == 'Assam':
    browser=webdriver.Firefox()
    browser.get('http://103.8.249.227:8080/voterlist/')
elif a == 'Bihar':
    browser=webdriver.Firefox()
    browser.get('http://ele.bihar.gov.in/pdfsearch/')
elif a =='Chandigarh':
    browser=webdriver.Firefox()
    browser.get('https://ceochandigarh.gov.in/en/list-of-polling-stations')
elif a =='Chhattisgarh':
    browser=webdriver.Firefox()
    browser.get('https://election.cg.nic.in/voterlist/Default.aspx')
elif a =='Dadra and Nager Haveli and Daman & Diu':
    browser=webdriver.Firefox()
    browser.get('https://ceo.dnh.gov.in/')
elif a =='Goa':
    browser=webdriver.Firefox()
    browser.get('https://ceogoa.nic.in/appln/UIL/ElectoralRoll.aspx')
elif a =='Gujarat':
    browser=webdriver.Firefox()
    browser.get('https://erms.gujarat.gov.in/ceo-gujarat/master/frmEPDFRoll.aspx')
elif a =='Haryana':
    browser=webdriver.Firefox()
    browser.get('https://ceoharyana.gov.in/WebCMS/Start/1791')
elif a =='Himachal Pradesh':
    browser=webdriver.Firefox()
    browser.get('https://electionhp.gov.in/pscd/')
elif a =='Jharkhand':
    browser=webdriver.Firefox()
    browser.get('http://164.100.150.3/mrollpdf1/aceng.aspx')
elif a =='Karnataka':
    browser=webdriver.Firefox()
    browser.get('https://ceo.karnataka.gov.in/')
elif a =='Kerala':
    browser=webdriver.Firefox()
    browser.get('http://www.ceo.kerala.gov.in/electoralrolls.html')
elif a =='Lakshadweep':
    browser=webdriver.Firefox()
    browser.get('https://ceolakshadweep.gov.in/electoral-rolls')
elif a =='Madhya Pradesh':
    browser=webdriver.Firefox()
    browser.get('https://ceomadhyapradesh.nic.in/VL.aspx')
elif a =='Maharashtra':
    browser=webdriver.Firefox()
    browser.get('https://ceoelection.maharashtra.gov.in/searchlist/')
elif a =='Manipur':
    browser=webdriver.Firefox()
    browser.get('https://ceomanipur.nic.in/eroll')
elif a =='Meghalaya':
    browser=webdriver.Firefox()
    browser.get('https://ceomeghalaya.nic.in/erolls/erolls-general-electors.html')
elif a =='Mizoram':
    browser=webdriver.Firefox()
    browser.get('https://ceo.mizoram.gov.in/view_erolls')
elif a =='NCT OF Delhi':
    browser=webdriver.Firefox()
    browser.get('https://ceodelhi.gov.in/AcListEng.aspx')
elif a =='Odisha':
    browser=webdriver.Firefox()
    browser.get('http://ceoorissa.nic.in/main.html')
elif a =='Puducherry':
    browser=webdriver.Firefox()
    browser.get('https://ceopuducherry.py.gov.in/rolls/rolls.html')
elif a =='Punjab':
    browser=webdriver.Firefox()
    browser.get('https://ceopunjab.gov.in/electoralphoto')
elif a =='Rajasthan':
    browser=webdriver.Firefox()
    browser.get('http://ems.raj.nic.in/electoralroll/rln')
elif a =='Sikkim':
    browser=webdriver.Firefox()
    browser.get('https://ceosikkim.nic.in/ElectoralRolls/PollingStationName?ERollID=18')
elif a =='Telangana':
    browser=webdriver.Firefox()
    browser.get('https://ceotserms2.telangana.gov.in/ts_erolls/rolls.aspx')
elif a =='Tripura':
    browser=webdriver.Firefox()
    browser.get('')
elif a =='Uttar Pradesh':
    browser=webdriver.Firefox()
    browser.get('https://ceouttarpradesh.nic.in/rollpdf/rollpdf.aspx')
elif a =='Uttarakhand':
    browser=webdriver.Firefox()
    browser.get('https://election.uk.gov.in/')
elif a =='West Bengal':
    browser=webdriver.Firefox()
    browser.get('https://ceowestbengal.nic.in/DistrictList') 
    
