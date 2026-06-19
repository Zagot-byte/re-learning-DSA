class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if ( len(s) != len(t) ):
            return False
        else:
             s_dict=self.freq(s)
             t_dict=self.freq(t)
             return s_dict == t_dict 
                
            
    def freq(self,text):
        freq={}
        for i in text:
            if i in freq:
                freq[i]=freq[i]+1
            else:
                freq[i]=1
        return freq
    
