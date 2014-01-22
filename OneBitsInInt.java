/**
 * Write a method that takes an int and returns the number of bits that are set to 1
 */
 
//Solution

/**
 * Note that this algorithm doesn't care if the input is positive or negative. It simply counts
 * the number of 1s in the binary representation of the input.
 * @param n
 * @return The number of 1s in the binary representation of n
 */
public static int oneBitsInInt(int n) {
   int count = 0;

   while(n != 0) {
      if((n & 1) != 0) count++;
      n >>>= 1;
   }

   return count;
}