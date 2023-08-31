from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from PIL import Image

# Print the GeckoDriver executable path (for verification)
print("GeckoDriver Executable Path:")
print(webdriver.Firefox(executable_path="geckodriver").capabilities['moz:webdriverClick'])

print("""
Please Enter the followings
***** Press 1 for a single domain *****
***** Press 2 for multiple domains *****
""")
option = int(input("[+] Enter the option: "))

if option == 1:
    subdomain = input("[+] Enter the subdomain: ")
    
    options = Options()
    options.headless = True  # Run Firefox in headless mode
    driver = webdriver.Firefox(options=options, executable_path="geckodriver")  # Path to geckodriver executable
    driver.get(subdomain)  # Using sub as the URL directly
    
    screenshot = driver.get_screenshot_as_png()
    screenshot_path = f"{subdomain}.png"
    
    with open(screenshot_path, "wb") as f:
        f.write(screenshot)
    
    # Close the browser
    driver.quit()

elif option == 2:
    subdomain_list_path = input("[+] Enter the file path: ")
    subdomains = open(subdomain_list_path, "r").read().splitlines()

    options = Options()
    options.headless = True  # Run Firefox in headless mode
    driver = webdriver.Firefox(options=options, executable_path="geckodriver")  # Path to geckodriver executable

    for sub in subdomains:
        driver.get(sub)  # Using sub as the URL directly
        
        screenshot = driver.get_screenshot_as_png()
        screenshot_path = f"{sub}.png"
        
        with open(screenshot_path, "wb") as f:
            f.write(screenshot)
        
    # Close the browser
    driver.quit()

else:
    print("Wrong Input")
