class Solution {
    public int countKDifference(int[] nums, int k) {
        Map<Integer,Integer> countmap=new HashMap<>();
        int count=0;

        for(int num:nums){
            // for num+k
            if(countmap.containsKey(num+k)){
                count+=countmap.get(num+k);
            }

            // for num-k
            if(countmap.containsKey(num-k)){
                count+=countmap.get(num-k);
            }

            // add to map 
            countmap.put(num, countmap.getOrDefault(num,0)+1);
        }

        return count;
    }
}