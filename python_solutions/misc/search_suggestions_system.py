from typing import List


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:

        """
            * sort products
            * incrementally increase prefix
            * find at most 3 matches, add them to list
            * repeat until prefix == searchword
        """


        MAX_RESULTS_PER_ENTRY = 3
        products.sort()

        prefix = ''


        filtered_products = products
        search_results = []

        while searchWord:
            prefix += searchWord[0]
            searchWord = searchWord[1:]

            prefix_filter = filter(lambda x: x.startswith(prefix), filtered_products)
            filtered_products = list(prefix_filter)

            max_results = min(len(filtered_products), MAX_RESULTS_PER_ENTRY)
            search_results.append(filtered_products[:max_results])

        return search_results



if __name__ == '__main__':
    products = ["mobile","mouse","moneypot","monitor","mousepad"]
    search_word = "mouse"
    output = Solution().suggestedProducts(products, search_word)
    print("Input:%s|%s\nOutput:%s" % (products, search_word, output))

    products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
    search_word = "mouse"
    output = Solution().suggestedProducts(products, search_word)
    print("Input:%s|%s\nOutput:%s" % (products, search_word, output))

    products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
    search_word = "mouse"
    output = Solution().suggestedProducts(products, search_word)
    print("Input:%s|%s\nOutput:%s" % (products, search_word, output))


