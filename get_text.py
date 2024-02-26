from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def extract_content(driver):
    # Get the current page HTML source
    html_source = driver.page_source
    
    # Define the start and end markers for the content extraction
    start_marker = '<h2>'
    end_marker = '<div id="favoriteshow_3" style="display:none" align="center"></div>'
    
    # Find the start and end positions of the content to be extracted
    start_pos = html_source.find(start_marker)
    end_pos = html_source.find(end_marker, start_pos)
    
    # Extract the content between the start and end markers
    if start_pos != -1 and end_pos != -1:
        content = html_source[start_pos:end_pos]
        # Optionally, clean or process the content as needed here
        # Replace all <br> and </div> tags with newline characters
        content = content.replace('<br>', '\n') 
        # Remove </div>, <h2>, and </h2> tags
        content = content.replace('</div>', '').replace('<h2>', '').replace('</h2>', '')
        # Remove <div style="clear:both;"> if it exists
        content = content.replace('<div style="clear:both;">', '')
        # Write the extracted content to a file
        with open('extracted_content.txt', 'a', encoding='utf-8') as file:
            file.write(content + "\n\n")
    


def main(total_chapters):
    # Setup the WebDriver (ensure you have the WebDriver for your browser installed)
    driver = webdriver.Chrome()  # or use `webdriver.Firefox()`, etc., depending on your browser
    
    # Replace this URL with the URL of the page you want to scrape
    url = 'https://www.jjwxc.net/onebook.php?novelid=7972788&chapterid=1'
    driver.get(url)
    
    for _ in range(total_chapters):
        extract_content(driver)
        # Simulate pressing the right arrow key to navigate
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.RIGHT)
        time.sleep(10)  # Sleep to avoid being detected as a robot and allow the page to load

    driver.quit()

if __name__ == "__main__":
    total_chapters = 51  # Example: Replace 100 with the actual total chapter count
    main(total_chapters)