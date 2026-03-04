class Solution {
    public int minSwaps(String s) {

        int balance=0;
        int unmatched=0;

        for(char c:s.toCharArray()){
            if(c=='['){
                balance++;
            }
            else{
                if(balance>0){
                    balance--;
                }else{
                    unmatched++;
                }
            }
        }
        return ((unmatched+1)/2);
    }
}