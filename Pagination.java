/**
 * Write a function that, for a given product search, when given the total # of items, # of items
 * per page, # of page links to show, and current page, will return a string pagination like this
 * example:
 *
 * pagination( total # of items, # of items per page, # of page links to show, current page)
 *
 * [1] 2 3 4 5 ...
 * 1 2 [3] 4 5 ...
 * ... 2 3 [4] 5 6 ...
 * ... 7 8 9 10 [11]
 *
 * Clarification: The above results are a set of results for a set of calls. Each line represents
 * one return value for one call.
 */
 
//Solution

/**
 * @param itemCount the total number of items in the search result
 * @param itemsPerPage the number of items to be displayed per search result page
 * @param pageLinkCount the number of page links to display
 * @param currPage the current page of the search results
 * @return a string pagination identifying the current and surrounding pages for search results
 */
public static String pagination(int itemCount, int itemsPerPage, int pageLinkCount, int currPage){
   int pageCount = itemCount / itemsPerPage, startPage, endPage;
   String result = new String();

   if(currPage <= pageLinkCount/2 + 1){ //near start
      startPage = 1;
      endPage = pageLinkCount;
   }else if(currPage >= pageCount - pageLinkCount/2){ //at end
      startPage = pageCount - pageLinkCount + 1;
      endPage = pageCount;
   }else{ //in middle
      startPage = currPage - pageLinkCount/2;
      endPage = currPage + pageLinkCount/2;
   }

   if(startPage != 1)
      result += "... ";

   for(int i = startPage; i <= endPage; i++)
      result += (i == currPage) ? "["+i+"] " : i+" ";

   if(endPage != pageCount)
      result += "... ";

   return result.substring(0, result.length() - 1);
}