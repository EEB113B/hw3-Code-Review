def sort_by_occurrence(nums):
    """按照 list 物件 nums 裡的各元素出現次數，進行遞增排序"""
    # 把你的程式碼放在這裡
    ans =[]
    i=0
    while i<=9:  #數字從0~9
        count=0
        if  input_list.count(i)==0: #計算input_list裡，所出現數字的次數，如果是0次，便跳過這個數。
           i+=1                     #將其+1，再做下一次的判斷
           continue
        else:
            nums =[]
            count = input_list.count(i)
            nums.append(i)
            nums.append(count)
            ans.append(nums) #將所計算的數字與算出的出現次數放入同一個list裡，順序是[i,count]
            i+=1
    size = sorted(ans,key=lambda x:x[1]) #集合ans裡，由[i,count]index為1(這裡是counter)的大小排序各個[i,count]
    size_len = len(size) #計算每個輸入的list長度
    size_final = []
    for j in range(size_len): #計算每個輸入的list，看需要跑多少次
        size_final.append(size[j][0]) #抓取所要的項目，加到ize_final這個空集合裡

    return size_final






        



  
    
    

if __name__ == '__main__':
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_list = [2,0,9,8,9,2,8,2,0,9,7,9,8,2,9]
    output_list = sort_by_occurrence(input_list)
    print(output_list)


#留言板