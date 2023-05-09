# LFA_HW3-Minimal-DFA  
INPUT FORMAT:  
 -letters of the aphabet  
 -final states  
 -all states
 -every transition of form: qi a qj, where a is from the alphabet and qi and qj are states    
ex:  
a b ->the alphabet  
q6 ->final state(s)  
q0 q1 q2 q3 q4 q5 q6 ->states  
q0 a q1 ->a transition from q0 to q1 with 'a'  
q0 b q3  
q1 a q3  
q1 b q2  
q2 a q3  
q2 b q2  
q3 a q6  
q3 b q5  
q4 a q6  
q4 b q5  
q5 a q6  
q5 b q2  
q6 a q4  
q6 b q5  

