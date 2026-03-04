class Solution {
    public int minimumChairs(String s) {
        int chairs=0;
        int min_chairs=0;
        
        for(int ch:s.toCharArray()){
            if(ch=='L'){
                chairs--;
            }
            else{
                chairs++;
            }
            min_chairs=Math.max(min_chairs,chairs);
        }
        return min_chairs;
    }
}