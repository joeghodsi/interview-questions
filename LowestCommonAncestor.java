/**
 * Implement the Lowest Common Ancestor algorithm assuming a data structure similar to a binary tree
 * in which each node doesn't point to its left and right child, but rather it points to its parent.
 * 
 */
 
//Solutions

/**
 * This algorithm finds the lowest common ancestor between two nodes in the tree, node1 and
 * node2.
 * @param node1 An arbitrary node in the tree structure
 * @param node2 An arbitrary node in the tree structure
 * @return The lowest common ancestor between the two nodes in the tree
 */
public static Integer LCA(LinkedList<Integer> node1, LinkedList<Integer> node2) {
   HashMap<Integer, Integer> list = new HashMap<>();

   for(Integer i : node1)
      list.put(i, i);
   for(Integer i : node2)
      if(list.containsKey(i))
         return i;

   return null;
}

/**
 * This is the optimal LCA solution. It shares the same runtime as the above method - O(n) -
 * but it uses constant space (the above solution uses an O(n) space HashMap).
 * @param node1 An arbitrary node in the tree structure
 * @param node2 An arbitrary node in the tree structure
 * @return The lowest common ancestor between the two nodes in the tree
 */
public static Integer LCA_optimal(LinkedList<Integer> node1, LinkedList<Integer> node2) {
   Iterator<Integer> it1, it2;
   boolean list1End = false, list2End = false;
   int i = 0, i1, i2;

   //Find the length of the shortest list
   for(it1 = node1.iterator(), it2 = node2.iterator(); it1.hasNext() && it2.hasNext(); i++) {
      it1.next();
      it2.next();
   }

   if(!it1.hasNext()) list1End = true;
   if(!it2.hasNext()) list2End = true;

   //Move through the lists so they are both the same length (the length of the shortest list)
   if(list1End) it2 = node2.listIterator(node2.size() - i);
   else it2 = node2.iterator();
   if(list2End) it1 = node1.listIterator(node1.size() - i);
   else it1 = node1.iterator();

   //Now that the lists are the same "depth," move up the "tree" comparing at each new "depth"
   while(it1.hasNext() && it2.hasNext()) {
      i1 = it1.next();
      i2 = it2.next();
      if(i1 == i2)
         return i1;
   }

   return null;
}