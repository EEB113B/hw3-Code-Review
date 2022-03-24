def sort_by_occurrence(nums):
    """按照 list 物件 nums 裡的各元素出現次數，進行遞增排序"""
    # 把你的程式碼放在這裡

    #用dictionary計算次數
    dict_nums = {}
    for i in nums:
        if i in dict_nums:
            dict_nums[i] += 1
        else:
            dict_nums[i] = 1
    #由小到大排序出現次數
    dict_nums = dict(sorted(dict_nums.items(), key=lambda item: item[1]))

    #建立回傳用的list
    list_nums=[]

    #list的值為排序過的key值
    for i in dict_nums:
        list_nums.append(i)
    return list_nums

if __name__ == '__main__':
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_list = [1, 1, 1, 2, 2, 3]
    output_list = sort_by_occurrence(input_list)
    print(output_list)

    input_list2 = [5,5,6,6,6,6,0,1,1,1]
    output_list2 = sort_by_occurrence(input_list2)
    print(output_list2)

    input_list3 = [2,0,9,8,9,2,8,2,0,9,7,9,8,2,9]
    output_list3 = sort_by_occurrence(input_list3)
    print(output_list3)
    


#留言板