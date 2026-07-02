from playwright.sync_api import sync_playwright
import os

def run_cuj(page):
    page.goto(f"file://{os.path.abspath('test_frontend.html')}")
    page.wait_for_timeout(1000)

    # Click the new Phase 8 checkbox
    page.get_by_role("checkbox", name="Phase 8: Generate Custom Shell (Experimental)").check()
    page.wait_for_timeout(500)

    # Click the new Phase 9 checkbox
    page.get_by_role("checkbox", name="Phase 9: Plugin Architecture (Experimental)").check()
    page.wait_for_timeout(500)

    # Click the new Phase 10 checkbox
    page.get_by_role("checkbox", name="Phase 10: AST Graph Visualization (Debugging)").check()
    page.wait_for_timeout(500)

    # Click the new Phase 11 checkbox
    page.get_by_role("checkbox", name="Phase 11: Automated Vulnerability Scanning (Experimental)").check()
    page.wait_for_timeout(500)

    # Click the new Phase 12 checkbox
    page.get_by_role("checkbox", name="Phase 12: AI Code Summarization (Experimental)").check()
    page.wait_for_timeout(500)

    # Click the execute button to trigger the new mock pipeline statuses and log console
    page.get_by_role("button", name="Execute Pipeline").click()
    page.wait_for_timeout(1000)

    # Wait for the status update to scroll the console
    page.wait_for_timeout(4500)

    # Wait for completion states of all 12 phases
    page.wait_for_timeout(17000)

    # Take a screenshot at the final completed state containing the custom shell output
    page.screenshot(path="./verification/screenshots/verification.png", full_page=True)

    # Wait a bit longer to hold the final state in the video
    page.wait_for_timeout(1500)

if __name__ == "__main__":
    os.makedirs("./verification/videos", exist_ok=True)
    os.makedirs("./verification/screenshots", exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            record_video_dir="./verification/videos",
            viewport={'width': 1000, 'height': 850}
        )
        page = context.new_page()

        # Override file chooser behavior for the input field so alert doesn't trigger
        page.on("dialog", lambda dialog: dialog.accept())

        # Mock file selection for the required file input
        with open("mock.exe", "w") as f:
            f.write("mock")

        page.goto(f"file://{os.path.abspath('test_frontend.html')}")
        page.locator("#binaryFile").set_input_files("mock.exe")

        try:
            run_cuj(page)
        finally:
            context.close()
            browser.close()
            if os.path.exists("mock.exe"):
                os.remove("mock.exe")
