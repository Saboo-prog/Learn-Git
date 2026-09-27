from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=False,
        args=["--start-maximized"]
    )

    context = browser.new_context()
    page = context.new_page()

    page.goto(
        "https://sauce-demo.myshopify.com/",
        wait_until="domcontentloaded"
    )

    page.get_by_role("link", name="Sign up").click()

    # First Name
    page.locator('input[name="customer[first_name]"]').fill("Sahil")

    # Last Name
    page.locator('input[name="customer[last_name]"]').fill("Kapil")

    # Email
    page.locator('input[name="customer[email]"]').fill("sahil+g9@yopmail.com")

    # Password
    page.locator('input[name="customer[password]"]').fill("Sahhhh")

    # Create account
    page.locator('input[type="submit"][value="Create"]').click()


    print(page.url

    page.wait_for_timeout(5000)


    print("ahhahfshsfisahifsahiashifsa")

    browser.close()