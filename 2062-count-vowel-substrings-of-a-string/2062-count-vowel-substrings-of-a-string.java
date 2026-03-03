class Solution {
    public int countVowelSubstrings(String word) {
      
        int n=word.length();
        int count=0;

        for(int i=0;i<n;i++){
            HashSet<Character> vowelMap=new HashSet<>();
            for(int j=i;j<n;j++){
                char ch= word.charAt(j);

                if(!isVowel(ch)) break;

                vowelMap.add(ch);

                if(vowelMap.size()==5){
                    count++;
                }
            }
        }
        return count;
    }

    private boolean isVowel(char ch){
        if(ch=='a' || ch=='i' || ch=='e' || ch=='o' || ch=='u'){
            return true;
        }
        return false;
    }
}