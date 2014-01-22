/**
 * Write a method that checks the endianness of the underlying OS.
 */
 
//Solutions

/**
 * @return True if the underlying OS is big endian
 */
public static boolean isBigEndian() {
   if(ByteOrder.nativeOrder().equals(ByteOrder.BIG_ENDIAN))
      return true;
   return false;
}

/**
 * @return True if the underlying OS is little endian
 */
public static boolean isLittleEndian() {
   if(ByteOrder.nativeOrder().equals(ByteOrder.LITTLE_ENDIAN))
      return true;
   return false;
}