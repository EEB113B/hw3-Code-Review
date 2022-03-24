from calendar import c
from pickle import NONE
from re import I, X

def sort_by_occurrence(nums):
    """按照 list 物件 nums 裡的各元素出現次數，進行遞增排序"""
    # 把你的程式碼放在這裡
    #print("input:",nums)
    numset=set(nums) #轉set(把重複的去掉)
    numlist=list(numset)#轉回list
    #print("number:",numlist)
    #print("lenth:",len(numlist))
    num_count=[0]*len(numlist)#預設一開始出現次數都是0
    for i in range(len(numlist)):#count每個數字各出現幾次
        num_count[i] =nums.count(numlist[i])
    #print("count:",num_count)
    output=[]
    for i in range(max(num_count)+1):#$從次數等於0到最大次數
        for j in range(len(num_count)):#次數由小到大放進output
            if(num_count[j]== i):
                output.append(numlist[j])
    return output

if __name__ == '__main__':
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_list = [1,1,1,2,2,3]
    output_list = sort_by_occurrence(input_list)
    print(output_list)


#留言板