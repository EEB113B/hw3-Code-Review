def sort_by_occurrence(input_list):
    """按照 list 物件 nums 裡的各元素出現次數，進行遞增排序"""
    # 把你的程式碼放在這裡
    
    length = len(input_list)
    dict1 = {}
    for i in range(0, length):   
        if input_list[i] not in dict1:    #新的東西加進dict1
            dict1[input_list[i]] = 1
        if input_list[i] in dict1:   #累計
            dict1[input_list[i]] += 1
    list_v_k = [[v, k]for k, v in dict1.items()] #key value 對調放入list中
    list_v_k.sort()
    lst = []
    for i in range(0, len(list_v_k)):   
        lst.append(list_v_k[i][1])
    return lst



if __name__ == '__main__':
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_list = [1, 1, 1, 2, 2, 3]
    output_list = sort_by_occurrence(input_list)
    print(output_list)


#留言板