/**
 * Implement the merge sort algorithm.
 */
 
//Solution

/**
 * A recursive merge sort implementation
 * @param array The array or subarray to be sorted
 * @return The sorted array or subarray
 */
public static ArrayList<Integer> mergeSort(ArrayList<Integer> array) {
   if(array.size() <= 1) return array;
   int mid = array.size()/2;
   ArrayList<Integer> left = mergeSort(new ArrayList<Integer>(array.subList(0, mid)));
   ArrayList<Integer> right = mergeSort(new ArrayList<Integer>(array.subList(mid, array.size())));
   return merge(left, right);
}

/**
 * A merge sort helper function for merging two sorted subarrays
 * @param left A sorted subarray
 * @param right A sorted subarray
 * @return The sorted list of the two subarrays
 */
private static ArrayList<Integer> merge(ArrayList<Integer> left, ArrayList<Integer> right) {
   ArrayList<Integer> result = new ArrayList<Integer>();

   while(!left.isEmpty() && !right.isEmpty()) {
      if(left.get(0) <= right.get(0))
         result.add(left.remove(0));
      else result.add(right.remove(0));
   }

   if(!left.isEmpty()) result.addAll(left);
   else if(!right.isEmpty()) result.addAll(right);

   return result;
}