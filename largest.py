l = [-53, -60, 40, 30]           
# Ek list banayi gayi hai jisme kuch positive aur negative numbers hain.

largest = l[0]                   
# List ke pehle element ko 'largest' (sabse bada) maan liya gaya hai.

sec_largest = l[0]               
# List ke pehle element ko hi 'second largest' bhi maan liya gaya hai (initialization ke liye).

index1 = 0                       
# 'largest' element ka index 0 se start kiya gaya hai.

index2 = 0                       
# 'second largest' element ka index bhi 0 se start kiya gaya hai.

for i in l:                      
# List ke har element par loop chala rahe hain.

    if i > largest:              
        # Agar current element 'largest' se bada hai:
        sec_largest = largest    
        # Purane 'largest' ko 'second largest' bana diya.
        largest = i              
        # Naye element ko 'largest' bana diya.
        index2 = index1          
        # Purane 'largest' ka index ab 'second largest' ka index ho gaya.
        index1 = l.index(i)      
        # Naye 'largest' ka index nikal liya.

    elif i > sec_largest:        
        # Agar current element 'second largest' se bada hai (lekin 'largest' se chhota ya barabar hai):
        sec_largest = i          
        # Usko 'second largest' bana diya.
        index2 = l.index(i)      
        # Uska index nikal liya.

print(f"Largest: {largest} at index {index1}")           
# Sabse bada number aur uska index print kiya.

print(f"Second Largest: {sec_largest} at index {index2}") 
# Dusra sabse bada number aur uska index print kiya.