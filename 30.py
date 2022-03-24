def sort_by_occurrence(nums):
    """按照 list 物件 nums 裡的各元素出現次數，進行遞增排序"""
    # 把你的程式碼放在這裡
    length = len(nums)
    #建造初始list
    count_num = [0]*length
    sort_num = [0]*length
    n = 0

    #計算每項個數並排序$
    for i in range(0,length):
        count_num[i] = nums.count(i) #算每個字元的數量
    #將字元衣數量排序
    for i in range(1,length):
        for j in range(0,length):
            if count_num[j] == i:
                sort_num[n] = j
                n += 1
    
    #將零項刪除
    if 0 in nums:
        location = sort_num.index(0) #找出原字串的零
        sort_num[location] += 1 #將他先轉成1
        sort_num = list(filter((0).__ne__, sort_num)) #將其他零項刪除
        sort_num[location] -= 1#將1轉為零
    else:
        sort_num = list(filter((0).__ne__, sort_num))
    return sort_num


if __name__ == '__main__':
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_list = [1, 1, 1, 2, 2, 3]
    output_list = sort_by_occurrence(input_list)
    print(output_list)


#留言板