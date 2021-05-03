import threading
import time
import sys, re, os
from zipfile import ZipFile


try:
	from selenium import webdriver
	import selenium.common.exceptions
	from selenium.webdriver.common.keys import Keys
	from selenium.webdriver.support.ui import Select
	from selenium.webdriver.common.keys import Keys
	from selenium.webdriver.chrome.options import Options
	from selenium.webdriver.common.action_chains import ActionChains
	import wget
except:
	print("Install Dependencies using 'python3 -m pip install -r requirements.txt")


def download():
	arr = os.listdir()
	if "chromedriver.exe" not in arr:
		wget.download("https://chromedriver.storage.googleapis.com/90.0.4430.24/chromedriver_win32.zip")
		zip = ZipFile('chromedriver_win32.zip')
		zip.extractall()
	else:
		pass



def login(): # login using credentials, runs only first time.
		email = input("\nEnter Your Email:")
		password = input("\nEnter Your Password:")
		driver = webdriver.Chrome(options=options)
		web = driver.get("https://olympus.greatlearning.in/login")
		do = driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/div/form[1]/div[1]/input")
		time.sleep(1)
		do.send_keys(email)
		do = driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/div/form[1]/div[2]/input")
		do.send_keys(password)
		do = driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/div/form[1]/div[3]/div[2]/button").click()
		time.sleep(5)
		#driver.quit()

def main():
	options = Options()
	options.headless = True
	options.add_argument("--mute-audio")
	options.add_argument(r"user-data-dir=\\config")
	options.add_experimental_option("detach", True)
	driver = webdriver.Chrome(options=options)
	

	print("Initiating....")

	

	def getList(dict):
		return [*dict]

	def run(addr):
		driver.get(addr)
		time.sleep(20)
		do = driver.find_elements_by_xpath("/html/body/div[1]/main/div/div[2]/div[1]/main/div[2]/div[1]/div[2]/div[1]/div[2]/button")[0]
		do.click()


	
	driver.get("https://olympus.greatlearning.in/courses")
	time.sleep(4)

	#def get_links_from_page():
	



	course = []
	links = driver.find_elements_by_tag_name("a")
	for link in links:
		href = link.get_attribute("href")
		if "greatlearning.in/courses/" in href:
			course_id = href
			course.append(course_id)
	time.sleep(5)
	name = []
	elems = driver.find_elements_by_css_selector("h4")
	for elem in elems:
		course_name = elem.text
		if "Completed Courses" not in course_name:
			name.append(course_name)


	courses = dict(zip(name, course)) # form dictionary with course name and id
	all_courses = getList(courses)



	#driver.quit()


	print("Available Courses: ")
	for x in range(1,len(all_courses)+1):
		print(str(x)+".",all_courses[x-1])
	def choice():
		ch = input("Enter Your Choice :")
		
		if ch > len(all_courses):
			print("Choose correctly!")
			choice()
		else:
			do = all_courses[ch-1]
			address = str(courses[do])
			driver.get(address)
			time.sleep(5)
	all_vids = []
	links = driver.find_elements_by_tag_name("a")
	for link in links:
		href = link.get_attribute("href")
		#do = re.sub("\D","",address)
		if "pages" in href:
			all_vids.append(href)

	print(all_vids)

	for x in all_vids:
		driver.execute_script("window.open('');")
		driver.switch_to.window(driver.window_handles[len(driver.window_handles)-1])
		driver.get(x)
		time.sleep(6)
		do = driver.find_elements_by_xpath("/html/body/div[1]/main/div/div[2]/div[1]/main/div[2]/div[1]/div[2]/div[1]/div[2]/button")[0]
		do.click()

	driver.close()

try:
	first_time = False
	while first_time is not True:
		login()
		first_time = True
	main()
except:
	print("Error! Run Again \n close Chrome if running.")















	


'''
try:
	
	do = driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/div/form[1]/div[3]/div[2]/button").click()
	time.sleep(5)
	web = driver.get(x)
	time.sleep(15)
	try:
		do = driver.find_elements_by_xpath("/html/body/div[1]/main/div/div[2]/div[1]/main/div[2]/div[1]/div[2]/div[1]/div[2]/button")[0]
		do.click()
		print("opened a new tab")
	except Exception as e:
		time.sleep(1)
		print("Error Found, using other method")
		driver.get(x)
		time.sleep(20)
		do = driver.find_elements_by_xpath("/html/body/div[1]/main/div/div[2]/div[1]/main/div[2]/div[1]/div[2]/div[1]/div[2]/button")[0]
		do.click()
except:
	pass
'''
 































