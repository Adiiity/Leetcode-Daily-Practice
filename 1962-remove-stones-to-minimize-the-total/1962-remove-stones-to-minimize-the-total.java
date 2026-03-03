
class Solution {
    public int minStoneSum(int[] piles, int k) {
        PriorityQueue<Integer> maxHeap= new PriorityQueue<>(Collections.reverseOrder());

        int sum=0;
        for(int pile:piles){
            maxHeap.add(pile);
            sum+=pile;
        }

        while(k-- >0){
            int max=maxHeap.poll();
            int remove=max/2;

            sum-=remove;
            maxHeap.add(max-remove);
        }

        return sum;
    }
}