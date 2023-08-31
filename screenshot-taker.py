from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from PIL import Image
import urllib.parse

print("""
Please Enter the followings
***** Press 1 for a single domain *****
***** Press 2 for multiple domains *****
""")
option = int(input("[+] Enter the option: "))

if option == 1:
    subdomain = input("[+] Enter the subdomain: ")
    
    options = Options()
    options.add_argument('-headless')  # Run Firefox in headless mode
    driver = webdriver.Firefox(options=options)
    
    try:
        driver.get(subdomain)
        
        screenshot = driver.get_screenshot_as_png()
        domain_name = subdomain.replace('http://', '').replace('https://', '').replace('.', '_')
        screenshot_filename = f"{domain_name}.png"
        
        with open(screenshot_filename, "wb") as f:
            f.write(screenshot)
            
        print(f"Screenshot saved for {subdomain}")
    except Exception as e:
        print(f"Error capturing screenshot for {subdomain}: {e}")
    
    # Close the browser
    driver.quit()

elif option == 2:
    subdomain_list_path = input("[+] Enter the file path: ")
    subdomains = open(subdomain_list_path, "r").read().splitlines()

    options = Options()
    options.add_argument('-headless')  # Run Firefox in headless mode
    driver = webdriver.Firefox(options=options)

    for sub in subdomains:
        sub = sub.strip()  # Remove leading/trailing spaces if any
        
        try:
            driver.get(sub)
            
            screenshot = driver.get_screenshot_as_png()
            domain_name = sub.replace('http://', '').replace('https://', '').replace('.', '_')
            screenshot_filename = f"{domain_name}.png"
            
            with open(screenshot_filename, "wb") as f:
                f.write(screenshot)
                
            print(f"Screenshot saved for {sub}")
        except Exception as e:
            print(f"Error capturing screenshot for {sub}: {e}")
        
    # Close the browser
    driver.quit()

else:
    print("Wrong Input")

print("Thank you for using it")
