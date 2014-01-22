/**
 * Implement the binary search algorithm.
 */
 
//Solution

/**
 * This implementation of binary search is recursive and returns null if the value is not found.
 * @param value The value being searched for
 * @param array The array being searched
 * @param low The lower index in the search range
 * @param high The higher index in the search range
 * @return The index of value or null if value is not found
 */
public static Integer binarySearch(int value, ArrayList<Integer> array, int low, int high) {
   int mid = low + (high - low)/2;

   if(low > high) return null;
   if(value < array.get(mid))
      return binarySearch(value, array, low, mid - 1);
   else if(value > array.get(mid))
      return binarySearch(value, array, mid + 1, high);
   else return mid;
}