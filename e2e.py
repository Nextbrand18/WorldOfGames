#!/usr/bin/env python3
"""
End-to-end Selenium test for the WoG Scores service.
Exit codes:
  0  → success
 -1 → failure
"""
import sys
import time
import argparse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException, NoSuchElementException

LOWER, UPPER = 1, 1000  # valid score range

def test_scores_service(url: str) -> bool:
    opts = Options()
    opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")

    try:
        driver = webdriver.Chrome(options=opts)
        driver.set_page_load_timeout(10)
        driver.get(url)
        time.sleep(1)                     # small wait for render
        elem = driver.find_element("id", "score")
        score_text = elem.text.strip()
        print(f"[e2e] Retrieved score text: '{score_text}'")
        score = int(score_text)           # will raise ValueError if not numeric
        passed = LOWER <= score <= UPPER
        print(f"[e2e] Score {score} within range {LOWER}-{UPPER}: {passed}")
        return passed
    except (WebDriverException, NoSuchElementException, ValueError) as err:
        print(f"[e2e] ERROR: {err}")
        return False
    finally:
        try:
            driver.quit()
        except Exception:
            pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default="http://localhost:8777", help="Scores service URL")
    args = parser.parse_args()

    ok = test_scores_service(args.url)
    sys.exit(0 if ok else -1)


if __name__ == "__main__":
    main()
