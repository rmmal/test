import sys
import unittest

sys.path.append("../")
from Tests.BaseTest import BaseTest


class Searching(BaseTest):

    def setUp(self):
        super().setUp()
        self.item_name = 'Blouse'

    def test001_search_method1(self):
        """
            TC001: Verify that the searching on the {} in the home page is working correctly
            1- Search in the home page table for {}
        """.format(self.item_name,self.item_name)

        self.LOGGER.info("Searching for a {} in the home page table ".format(self.item_name))
        result = self.home_page.search_in_home_page_table(self.item_name)
        self.assertEqual(self.item_name + " Found", result)

    def test002_search_method2(self):
        """
           TC002: Verify that the searching on the blouse in the Women page is working correctly
           1- Click on the tab women from the menu
           2- Search for a {} in the women page table
        """.format(self.item_name)

        self.LOGGER.info("Clicking on the women tab from the menu ".format(self.item_name))
        self.home_page.go_to_tab_women()

        self.LOGGER.info("Searching for a {} in the women page table ".format(self.item_name))
        result = self.women_page.search_in_women_page_table(self.item_name)
        self.assertEqual(self.item_name + " Found", result)

    def test003_search_method3(self):
        """
           TC003: Verify that the searching on the blouse from the search box is working correctly
           1- Write {} in the search box and click search
           2- Search for a {} in the search result page table
        """.format(self.item_name,self.item_name)

        self.LOGGER.info("Writing {} in the search box and click search".format(self.item_name))
        self.home_page.search_in_searchbox(self.item_name)

        self.LOGGER.info("Searching for a {} in the search page table ".format(self.item_name))
        result = self.searchresult_page.search_in_search_page_table(self.item_name)
        self.assertEqual(self.item_name + " Found", result)


