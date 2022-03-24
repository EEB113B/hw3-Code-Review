def sort_by_occurrence(nums):
    """按照 list 物件 nums 裡的各元素出現次數，進行遞增排序"""
    
    # 創一個dict來記錄每個數字出現的次數(key是出現的次數、value是數字本身)
    count_dict = {}
    for i in nums:
        count = nums.count(i)      
        if count not in count_dict:
            count_dict[count] = i
    
    # 轉成lst來排序
    count_lst = sorted(count_dict)

    # 再創一個lst來輸入value
    new_lst = []
    for i in count_lst:
        new_lst.append(count_dict[i]) 
    return(new_lst)


    
if __name__ == '__main__':
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_list = [2,0,9,8,9,2,8,2,0,9,7,9,8,2,9]
    output_list = sort_by_occurrence(input_list)
    print(output_list)


#留言板