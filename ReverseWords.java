/**
 * Given an input string, return a string with the words in place but reversed.
 */
 
//Solution

/**
 * @param str the input string
 * @return A string containing the words in str, in place, but the characters of the words reversed
 */
public static String reverseWords(String str){
   String result = new String();
   StringTokenizer strTokens = new StringTokenizer(str, " ");

   while(strTokens.hasMoreTokens())
      result += new StringBuilder(strTokens.nextToken()).reverse() + " ";

   return result.substring(0, result.length() - 1);
}