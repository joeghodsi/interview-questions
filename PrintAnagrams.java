/**
 * Given an array of words, print sets of anagrams on seperate lines.
 */

//Solution

/**
 * m = number of words
 * n = number of characters in a word
 * The first loop is m*nlogn as it iterates over all words and sorts each one in nlogn time.
 * The second loop, while a double for loop, actually only touches each word once and prints it.
 * Therefore the runtime for this algorithm is m*nlogn
 * 
 * @param words The list of words.
 */
public static void printAnagrams(String[] words) {
   HashMap<String, List<Integer>> anagramIndices = new HashMap<String, List<Integer>>();

   for(int i = 0; i < words.length; i++){
      char[] chars = words[i].toCharArray();
      Arrays.sort(chars);
      String sortedWord = new String(chars);

      if(!anagramIndices.containsKey(sortedWord))
         anagramIndices.put(sortedWord, new ArrayList<Integer>());
      anagramIndices.get(sortedWord).add(i);
   }

   for(List<Integer> anagramWords : anagramIndices.values()){
      for(Integer index : anagramWords)
         System.out.print(words[index] + " ");
      System.out.println();
   }
}