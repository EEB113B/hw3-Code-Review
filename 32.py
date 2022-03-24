def sort_by_occurrence(nums):
    """按照 list 物件 nums 裡的各元素出現次數，進行遞增排序"""
    #建立一計算個數字典
    counting_dict = {}
    #將物件及其個數加入字典
    for element in nums:
        if element not in counting_dict:
            counting_dict[element] = 1
        else:
            counting_dict[element] += 1
    #將字典數值列為陣列
    for objects, counts in counting_dict.items():
    #將次數與物件顛倒，並依照次數遞減遞加排列
        unsorted_list = [(counts, objects) for objects,counts in counting_dict.items()]
        sorted_list = sorted(unsorted_list, reverse = False)
    #建立一陣列
    key_list = []
    #依照次數將key加入陣列中
    for key in sorted_list:
        key_list.append(key[1])

    return key_list
        


if __name__ == '__main__':
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_list = [2,0,9,8,9,2,8,2,0,9,7,9,8,2,9]
    output_list = sort_by_occurrence(input_list)
    print(output_list)


#留言板