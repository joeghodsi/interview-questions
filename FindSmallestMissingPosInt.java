/**
 * Find the smallest positive integer *not* in the unsorted array.
 */
 
//Solution

/**
 * This algorithm has a runtime of O(n) and uses O(1) space.
 * The algorithm moves each integer, x, in 1 to n to its respective index, x - 1 (since arrays are
 * zero indexed), and sets all other integers to zero. This will ultimately produce a sorted array
 * with 0s in indices that don't have their respective value (ie arr[8] = 0 if arr doesn't contain
 * 9 ...remember, zero-indexed). Finally, it simply loops through the sorted array and returns the
 * index + 1 of the first zero or it returns the array length + 1.
 * @param arr The unsorted array
 * @return The smallest positive integer not in the array
 */
public static int findSmallestMissingPosInt(int[] arr) {
   for(int i = 0, numSwapsAndZeros = 0; (i < arr.length) && (numSwapsAndZeros < arr.length); i++) {
      while((arr[i] >= 1) && (arr[i] <= arr.length) && (i + 1 != arr[i])) {
         swap(arr, arr[i] - 1, i);
         numSwapsAndZeros++;
      }
      if((arr[i] < 1) || (arr[i] > arr.length)) {
         arr[i] = 0;
         numSwapsAndZeros++;
      }
   }

   for(int i = 0; i < arr.length; i++)
      if(arr[i] == 0) return i + 1;

   return arr.length + 1;
}

private static void swap(int[] arr, int i, int j){
   int temp = arr[i];
   arr[i] = arr[j];
   arr[j] = temp;
}