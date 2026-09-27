from playwright.sync_api import sync_playwright 
with sync_playwright() as p:

    browser = p.chromium.launch(headless=False,args=["--start-maximized"])
    context = browser.new_context()

    page = context.new_page()

    page.goto("https://www.makemytrip.com/flights/")
    page.wait_for_timeout(5000) # class="commonModal__close"
    page.locator(".commonModal__close").click()
    page.locator("#fromCity").click()
    page.get_by_placeholder("From").fill("Chandigarh")
    page.get_by_role("option").filter(has_text="Chandigarh, India").click()
    page.locator("#toCity").click()
    page.get_by_placeholder("To").fill("Bang")
    page.get_by_role("option").filter(has_text="Bengaluru, India").click()
    
    page.get_by_role("gridcell", name="Wed Aug 19 2026").click()
    page.get_by_text("Tap to add a return date for bigger discounts").click()
    page.get_by_role("gridcell", name="Sat Sep 19 2026").click()

    page.locator(".primaryBtn font24 latoBold widgetSearchBtn ").click()
    page.wait_for_timeout(3000)
    page.screenshot(
        path= "/Users/sky/Desktop/Screenshots/Search.png",
        full_page=True
    )
    browser.close()



