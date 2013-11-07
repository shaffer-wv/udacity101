#only returns highest ranked url
def lucky_search(index, ranks, keyword):
    urls = lookup(index, keyword)
		if not urls:
			return None
		else:
			best_url = urls[0]
			for url in urls:
          if ranks[url] > ranks[best_url]:
              best_url = url
      return best_url
   
	 
def ordered_search(index, ranks, keyword):
    urls = lookup(index, keyword)
    return quick_sort(urls, ranks)


def quick_sort(urls, ranks):
    if not urls or len(urls) <= 1:
        return urls
    else:
        pivot = ranks[urls[0]]
        lesser = []
        greater = []
        for url in urls[1:]:
            if ranks[url] <= pivot:
                lesser.append(url)
            else:
                greater.append(url)
        return quick_sort(lesser, ranks) + [urls[0]] + quick_sort(greater, ranks)
		