class Solution {
    public String countAndSay(int n) {
        String res="1";

        for(int step=1; step<n;step++){
            StringBuilder next = new StringBuilder();
            int count=1;

            for(int i=1;i<res.length();i++){
                if(res.charAt(i)==res.charAt(i-1)){
                    count++;
                }
                else{
                    next.append(count).append(res.charAt(i-1));
                    count=1;
                }
            }

            next.append(count).append(res.charAt(res.length()-1));
            res=next.toString();
        }
        
        return res;
    }
}