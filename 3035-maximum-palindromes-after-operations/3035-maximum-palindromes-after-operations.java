class Solution {
    public int maxPalindromesAfterOperations(String[] words) {
        int[] freq=new int[26];

        // count freq of each letter in the words array
        for(String word : words){
            for(char ch : word.toCharArray()){
                freq[ch-'a']++;
            }
        }

        // Count total pairs from freq
        int totalPairs=0;
        for(int f : freq){
            totalPairs+=f/2;
        }

        // sort words by length 
        Arrays.sort(words, Comparator.comparingInt(String::length));

        // check with total pairs and required pairs and count no. of palindrome
        int count=0;

        for (String word:words){
            int requiredPairs=word.length()/2;
            if (totalPairs>=requiredPairs){
                totalPairs-=requiredPairs;
                count++;
            }
            else{
                break;
            }
        }

        return count;

    }
}