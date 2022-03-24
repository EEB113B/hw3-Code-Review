def sort_by_occurrence(nums):
    """按照 list 物件 nums 裡的各元素出次數，進行遞增排序"""
    # 把你的程式碼放在這裡
    new = set(nums)            #list轉set，將重複的字元刪除
    in_list = sorted(nums)     #list排序
    re_list = list(new)        #轉回list
    second_list = [0]*len(re_list)      #新的list，一開始次數為0

    for j in range(len(re_list)):       
        second_list[j] =nums.count(re_list[j])      #計算list相同字元次數
    
    output = []                #新增output的空陣列
    for k in range(len(re_list)):
        max_list = max(second_list)      #新的list最大值
        x = second_list.index(max_list)  #x為新的list最大值index對轉回list的值

        y = re_list[x]   
        output.append(y)       #將最多次的字元加到output中
        second_list[x] = 0 #最大值歸0，可以找list的第二大值
    
    output.reverse()       #由小排到大
    return output

if __name__ == '__main__':
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_list = [1, 1, 1, 2, 2, 3]
    output_list = sort_by_occurrence(input_list)
    print(output_list)


#留言板