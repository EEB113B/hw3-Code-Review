def sort_by_occurrence(nums):
    """按照 list 物件 nums 裡的各元素出現次數，進行遞增排序"""
    # 把你的程式碼放在這裡
    #建立一個字典 數字:次數
    num_dict = {}
    
    for i in nums:
        if i in num_dict:
            num_dict[i] += 1
        else:
            num_dict[i] = 1
    #將字典內的次數由小到大排列
    new_nums = sorted(num_dict.items(), key=lambda d : d[1])
    #將按照次數排列好列表中的數字叫出來後回傳
    new_nums_sort = [i[0] for i in new_nums]
    return new_nums_sort
         
    
if __name__ == '__main__':
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_list = [2,0,9,8,9,2,8,2,0,9,7,9,8,2,9]
    output_list = sort_by_occurrence(input_list)
    print(output_list)



#留言板