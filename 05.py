def sort_by_occurrence(nums):
    """按照 list 物件 nums 裡的各元素出現次數，進行遞增排序"""
    # 把你的程式碼放在這裡
    #print("input:",nums)
    newset = set(nums)                   #list轉set可刪去重複字元
    arrange_list = sorted(nums)          #將input的list排序
    #print(arrange_list)
    #print(newset)
    relist = list(newset)                #將set轉回list以便做編輯
    new_list = [0]*len(relist)           #創造新的list
    
    for i in range(len(relist)):         #for迴圈運算input list相同字元出現的次數
        new_list[i] =nums.count(relist[i])
    #print("hh",new_list)
    x = []                              #創造新的空陣列
    for j in range(len(relist)):
        a = max(new_list)               #找出new_list的最大值
        b = relist[new_list.index(a)]   #new_list最大值的index對應到relist的值，剛好可以找到input list出現最多次的值
        x.append(b)                     #把出現最多次的字元加到新的空字串中
        new_list[new_list.index(a)] = 0 #把new_list中最大數字設為0，以便下次進行for迴圈運算時可以找到list中的第二大值
    x.reverse()                         #題目要求由出現次數小排到大，所以做反轉換
    return x


if __name__ == '__main__':
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_list = [1,1,1,2,2,3]
    output_list = sort_by_occurrence(input_list)
    print(output_list)


#留言板