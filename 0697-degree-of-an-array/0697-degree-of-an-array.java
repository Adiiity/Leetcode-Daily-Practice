class Solution {
    public int findShortestSubArray(int[] nums) {
        HashMap<Integer,Integer> count=new HashMap<>();
        HashMap<Integer,Integer> lastInd=new HashMap<>();
        HashMap<Integer,Integer> firstInd=new HashMap<>();

        int degree=0;

        for(int i=0;i<nums.length;i++){
            int num=nums[i];

            if(!firstInd.containsKey(num)){
                firstInd.put(num,i);
            }

            count.put(num,count.getOrDefault(num,0)+1);

            lastInd.put(num,i);

            degree=Math.max(degree,count.get(num));
        }

        int min_len=nums.length;

        for(int num:nums){
            if(count.get(num)==degree){
                min_len=Math.min(min_len,lastInd.get(num)-firstInd.get(num)+1);
            }
        }

        return min_len;
    }
}