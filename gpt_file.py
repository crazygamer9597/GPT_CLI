import asyncio
import time
import re
from playwright.async_api import async_playwright

async def process_input(page, existing_output):
    textarea_selector = '#prompt-textarea'
    output_selector = 'div.w-full.text-token-text-primary'
    user_input = input("Enter your input (type 'leave' to exit): ")
    if user_input.lower() == 'leave':
        return False
    try:
        await page.wait_for_selector(textarea_selector, timeout=10000)
        await page.fill(textarea_selector, user_input)
        await page.press(textarea_selector, 'Enter')
        print("Request sent successfully.")
        
        start_time = time.time()
        while True:
            output_elements = await page.query_selector_all(output_selector)
            new_output = []
            for element in output_elements:
                output_text = await element.inner_text()
                if output_text not in existing_output:
                    new_output.append(output_text)
                    existing_output.append(output_text)
            
            if new_output:
                print("Reply:")
                for text in new_output:
                    text_without_gpt = re.sub(r'\b(chatgpt)\b', '', text, flags=re.IGNORECASE)
                    print(text_without_gpt.strip())
            else:
                # if time.time() - start_time <= 1:  # Print this message if it's the first check
                #     print("No new output found.")
                await page.wait_for_timeout(3000)
            if time.time() - start_time > 20:
                print("Timeout reached. Exiting.")
                break
            if not new_output and time.time() - start_time > 8:
                # print("No new output found after waiting. Exiting.")
                break
    except Exception as e:
        print(f"Failed to perform the operation: {e}")
    return True

async def main():
    async with async_playwright() as p:
        browser = await p.firefox.launch(headless=True)
        page = await browser.new_page()
        await page.goto('https://chatgpt.com/', wait_until='networkidle')
        existing_output = []
        while True:
            if not await process_input(page, existing_output):
                break
        await browser.close()
asyncio.run(main())