def sort_by_occurrence(nums):
    """按照 list 物件 nums 裡的各元素出現次數，進行遞增排序"""
    # 把你的程式碼放在這裡
 
    new_lst = []
    new_dic = {}
 
    for element in input_list:
        if element not in new_dic:
            new_dic[element] = element
        else:
            new_dic[element] += 1
    new_lst = [(v,k) for k,v in new_dic.items()]
    new_lst.sort()
    finist = []
    for i in new_lst:
        finist.append(i[1])
    return  finist

if __name__ == '__main__':
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_list = [1, 1, 1, 2, 2, 3]
    output_list = sort_by_occurrence(input_list)
    print(output_list)


#留言板