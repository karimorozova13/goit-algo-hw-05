import timeit

from kmp_search import kmp_search
from boyer_moore import boyer_moore_search
from rabin_karp import rabin_karp_search



        
        
        
if __name__ == '__main__':
    with open('article1.txt', encoding='utf-8') as fh:
        text = fh.read()
    
        time_taken_kmp_article1 = timeit.timeit(lambda: kmp_search(text, 'у теорії алгоритмів жадібні алгоритми'), number=3)
        time_taken_boyer_article1 = timeit.timeit(lambda: boyer_moore_search(text, 'у теорії алгоритмів жадібні алгоритми'), number=3)
        time_taken_rabin_article1 = timeit.timeit(lambda: rabin_karp_search(text, 'у теорії алгоритмів жадібні алгоритми'), number=3)
        
        time_taken_kmp_article1_not_found = timeit.timeit(lambda: kmp_search(text, 'Рекомендаційні системи є важливою складовою соціальних мереж'), number=3)
        time_taken_boyer_article1_not_found = timeit.timeit(lambda: boyer_moore_search(text, 'Рекомендаційні системи є важливою складовою соціальних мереж'), number=3)
        time_taken_rabin_article1_not_found = timeit.timeit(lambda: rabin_karp_search(text, 'Рекомендаційні системи є важливою складовою соціальних мереж'), number=3)
        
    with open('article2.txt', encoding='utf-8') as fh:
        text = fh.read()
    
        time_taken_kmp_article2 = timeit.timeit(lambda: kmp_search(text, 'Рекомендаційні системи є важливою складовою соціальних мереж'), number=3)
        time_taken_boyer_article2 = timeit.timeit(lambda: boyer_moore_search(text, 'Рекомендаційні системи є важливою складовою соціальних мереж'), number=3)
        time_taken_rabin_article2 = timeit.timeit(lambda: rabin_karp_search(text, 'Рекомендаційні системи є важливою складовою соціальних мереж'), number=3)
        
        time_taken_kmp_article2_not_found = timeit.timeit(lambda: kmp_search(text, 'у теорії алгоритмів жадібні алгоритми'), number=3)
        time_taken_boyer_article2_not_found = timeit.timeit(lambda: boyer_moore_search(text, 'у теорії алгоритмів жадібні алгоритми'), number=3)
        time_taken_rabin_article2_not_found = timeit.timeit(lambda: rabin_karp_search(text, 'у теорії алгоритмів жадібні алгоритми'), number=3)
        
        
    print(f"| {'Algorithm':<30} | {'Article 1':<20} | {'Article 2':<20} | {'Article 1 not found':<20} | {'Article 2 not found':<20} |")
    print(f"| {'-'*30} | {'-'*20} | {'-'*20} | {'-'*20} | {'-'*20} |")
    print(f"| {'Knuth Morris Pratt search':<30} | {time_taken_kmp_article1:20.5f} | {time_taken_kmp_article2:20.5f} | {time_taken_kmp_article1_not_found:20.5f} | {time_taken_kmp_article2_not_found:20.5f} |")
    print(f"| {'Boyer Moore search':<30} | {time_taken_boyer_article1:20.5f} | {time_taken_boyer_article2:20.5f} | {time_taken_boyer_article1_not_found:20.5f} | {time_taken_boyer_article2_not_found:20.5f} |")
    print(f"| {'Rabin Karp Search':<30} | {time_taken_rabin_article1:20.5f} | {time_taken_rabin_article2:20.5f} | {time_taken_rabin_article1_not_found:20.5f} | {time_taken_rabin_article2_not_found:20.5f} |")

