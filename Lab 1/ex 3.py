
def count_substring(sub_string, string):
    l=len(sub_string)
    count=0
    for i in range(len(string)-len(sub_string)+1):
        if(string[i:i+len(sub_string)] == sub_string ):      
            count+=1
    return count

sub_string = input()
string = input()
print(count_substring(sub_string, string))   