class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        int n=nums.length;
        int[] output=new int[n-k+1];
        // make the deque 
        Deque<Integer> q= new ArrayDeque<>();

        int ri=0;

        for(int i=0;i<n;i++){
            // first check deque only has k window elements
            while(!q.isEmpty() && q.peekFirst()==i-k){
                q.pollFirst();
            }

            // append to the q - pop the elements less than curr
            while(!q.isEmpty() && nums[q.peekLast()]<nums[i]){
                q.pollLast();
            }
            q.offerLast(i);
            
            // append to output
            if(i>=k-1){
                output[ri++]=nums[q.peekFirst()];
            }

        }
        return output;


    }
}