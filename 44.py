def sort_by_occurrence(nums):
    """按照 list 物件 nums 裡的各元素出現次數，進行遞增排序"""
    # 把你的程式碼放在這裡
    count_d = {}    #建立兩個空字典
    count_d_reverse = {} 
    count_lst = []  #建立兩個空字串
    final_lst = []
    for i in nums:
        count_d[i] = nums.count(i) #計算出現次數，並把次數加進字典
    lst_set = set(nums)  #利用set來把重複的數字刪除
    for j in lst_set:
        count = count_d[j]
        count_lst.append(count)
        count_lst.sort()  #排列出現次數
        count_d_reverse[count] = j #key 和 value對調，之後才可以將數字改回list
    for k in count_lst:
        number = count_d_reverse[k]
        final_lst.append(number)  #利用append把數字加回list裡，並return
    return final_lst
        


if __name__ == '__main__':
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_list = [1, 1, 1, 2, 2, 3]
    output_list = sort_by_occurrence(input_list)
    print(output_list)


#留言板