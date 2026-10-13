from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    try:
        print("GitHub Actions server-e browser launch kora hocche...")
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        print("Meta AI site-e access kora hocche...")
        page.goto("https://www.meta.ai", timeout=60000)
        
        # Screenshot nibe verify korar jonno
        page.screenshot(path="meta_screenshot.png")
        print("Success! Screenshot capture hoyeche.")
        
        time.sleep(3)
        browser.close()
    except Exception as e:
        print(f"Error asheche: {e}")
