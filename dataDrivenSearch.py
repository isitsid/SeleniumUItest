from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# This returns xpath of search textbox of the page
def home_search_textbox_name():
    return str("search")


# This returns xpath of search button of the page
def home_search_button_xpath():
    return "//*[@id='mw-content-text']/div/ol[1]"


# Test Data where we have search texts and their expected results
search_items = {
    "apple": "A common, round fruit produced by the tree Malus domestica, cultivated in temperate climates.",
    "pear": "An edible fruit produced by the pear tree, similar to an apple but elongated towards the stem."
}


# This is a function which takes 2 arguments
# search_text   -->  string to be searched
# expected_text -->  string result which is expected
def search_test(search_text, expected_text):
    browser = webdriver.Chrome()

    browser.get('https://en.wiktionary.org')

    # Verify if the title displayed has the valid text
    assert 'Wiktionary, the free dictionary' in browser.title

    # Find the search textbox
    elem = browser.find_element_by_name(home_search_textbox_name())

    # Send the search text to be searched
    elem.send_keys(search_text+ Keys.RETURN)

    # Find the search button to start searching for text
    elem = browser.find_element_by_xpath("//*[@id='mw-content-text']/div/ol[1]")

    # Assert for the expected result with the current result
    assert expected_text in elem.text

    browser.quit()


# main function to run
if __name__ == "__main__":
    for search_item in search_items:
        # Call Search_test function with search text and expected result as arguments
        search_test(search_item, search_items[search_item])
