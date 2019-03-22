# WebInteractionTutorial

https://github.com/BurntSushi/nfldb/wiki/Python-&-pip-Windows-installation

Step 1: Requirements + Purpose
	
	Python 3.6-3.7
	Selenium
	ChromeDriver
	
  Whats the legality of this stuff?

Step 2: Use requests to Post to a simple form

    import requests
    sesh = requests.session()

    url = "https://www.ssense.com/en-ca/newsletters/subscribers"

    email = input("Whats your email: ")

    gender = input("What is your clothing gender? men/women: ")

    payload = {"email": email, "gender": "women", "source": "SSENSE_EN_FOOTER"}

    headers = {}

    x= sesh.post(url, payload, headers)

    if(x.status_code == 200):
    print("success")


Step 3: Use BeautifulSoup to pull basic data from a website, in our case LCBO.com.

    import requests
    import pandas
    from bs4 import BeautifulSoup as bs

    csv = pandas.read_csv('https://raw.githubusercontent.com/jlumbard/WebInteractionTutorial/master/LCBOProductList.csv')

    csv['BottleSize'] = ""
    csv['Proof'] = ""
    csv['MadeIn'] = ""
    csv['Cost'] = ""

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    session = requests.Session()


    for index, row in csv.iterrows():
      print(index)
      try:

        rawFile = session.get(row['ns1:loc'], headers = headers)
        soup = bs(rawFile.text)

        details = soup.find("div", {"class": "product-details-list"})
        detailChildren = details.findChildren("dd", recursive=True)

        csv.set_value(index, 'BottleSize', detailChildren[0].text.replace(u'\xa0', '').replace(u'\n','').replace(u'\t',''))
        csv.set_value(index, 'Proof', detailChildren[1].text.replace(u'\xa0', '').replace(u'\n','').replace(u'\t','').replace('%',''))
        csv.set_value(index, 'MadeIn',detailChildren[2].text.replace(u'\xa0', '').replace(u'\n','').replace(u'\t',''))
        csv.set_value(index, 'Cost',soup.find("span", {"class": "price"}).text.replace(u'\xa0', '').replace(u'\n','').replace(u'\t','').replace('$','').replace(',','.'))
	
      except Exception as e:
        pass

      if(index == 70):
        break
	
	
  Then maybe try this:
  
    	for index, row in csv.iterrows():
	  print(row)
	  if(index ==70):
	    break

Step 4: Use Selenium, a web-driving tool, to put in your info on SupremeNewYork.com

    Why do you use selenium instead?
    
    	browser = webdriver.Chrome(path)
	browser.get('https://www.supremenewyork.com/shop/t-shirts/uubxrkwyn/i6yxfj3sp')
	import time

	time.sleep(5)

	for x in browser.find_elements_by_class_name('button'):
		print(x.text)

	browser.find_elements_by_class_name('button')[2].click()


	time.sleep(5)
	browser.find_elements_by_class_name('button')[1].click()

	browser.find_element_by_xpath('//*[@id="order_billing_name"]').send_keys("Brock Lumbard")

	browser.find_element_by_xpath('//*[@id="order_email"]').send_keys("blumbard.hba2020@ivey.ca")

	browser.find_element_by_xpath('//*[@id="order_tel"]').send_keys("306-540-3084")

	browser.find_element_by_xpath('//*[@id="bo"]').send_keys("217 Western Road")

	browser.find_element_by_xpath('//*[@id="oba3"]').send_keys("3586")

	browser.find_element_by_xpath('//*[@id="order_billing_zip"]').send_keys("N4V1E9")#postalCode

	browser.find_element_by_xpath('//*[@id="order_billing_city"]').send_keys("London")#City

	browser.find_element_by_xpath('//*[@id="order_billing_country"]').send_keys("Canada")#Country

	browser.find_element_by_xpath('//*[@id="order_billing_state"]').send_keys("ON")#Province

	browser.find_element_by_xpath('//*[@id="nnaerb"]').send_keys("1111111111111111")#CCnumber

	browser.find_element_by_xpath('//*[@id="credit_card_month"]').send_keys("09")#ExpiryMonth

	browser.find_element_by_xpath('//*[@id="credit_card_year"]').send_keys("2020")#ExpiryYear

	browser.find_element_by_xpath('//*[@id="orcer"]').send_keys("111")#CVV

	browser.find_element_by_xpath('//*[@id="order_terms"]').click() #TermsAndConditions

	browser.find_element_by_xpath('//*[@id="pay"]/input').click()
    
  Done. Did it fail for you?
  
  Discussion. What do Websites do to make this harder for you?
