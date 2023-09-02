from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from PIL import Image
import os

def capture_screenshot(subdomain, output_dir):
    options = Options()
    options.add_argument('-headless')
    driver = webdriver.Firefox(options=options)
    
    try:
        driver.get(subdomain)
        
        screenshot = driver.get_screenshot_as_png()
        domain_name = urllib.parse.urlparse(subdomain).hostname.replace('.', '_')
        screenshot_filename = os.path.join(output_dir, f"{domain_name}.png")
        
        with open(screenshot_filename, "wb") as f:
            f.write(screenshot)
            
        print(f"Screenshot saved for {subdomain} in {screenshot_filename}")
    except Exception as e:
        print(f"Error capturing screenshot for {subdomain}: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    print("""
    Please Enter the followings
    ***** Press 1 for a single domain *****
    ***** Press 2 for multiple domains *****
    """)
    
    option = int(input("[+] Enter the option: "))
    
    if option == 1:
        subdomain = input("[+] Enter the subdomain: ")
        output_dir = input("[+] Enter the path where you want to save the screenshot: ")
        capture_screenshot(subdomain, output_dir)
    elif option == 2:
        subdomain_list_path = input("[+] Enter the file path: ")
        subdomains = open(subdomain_list_path, "r").read().splitlines()
        output_dir = input("[+] Enter the path where you want to save the screenshots: ").strip()
        
        for sub in subdomains:
            capture_screenshot(sub, output_dir)
    else:
        print("Wrong Input")
    
    print("Thank you for using it")
