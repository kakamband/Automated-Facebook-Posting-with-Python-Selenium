from selenium import webdriver
import facebook

# VARIABLES
browser = webdriver.Chrome('PATH TO CHROME DRIVER')
youtube_url = 'YOUTUBE CHANNEL URL'

# OPENS YOUTUBE URL AND OPENS FIRST VIDEO
browser.get(youtube_url)
browser.find_element_by_id('thumbnail').click()

# SAVES URL OF FIRST VIDEO TO firstVideoURL
firstVideoURL = browser.current_url

# FACEBOOK ACCESS
token = 'YOUR FACEBOOK ACCESS TOKEN'
fb = facebook.GraphAPI(access_token=token)

# POST TO FACEBOOK
fb.put_object(parent_object='me', connection_name='feed', link=firstVideoURL, message='')
