def sort_by_occurrence(nums):
    """按照 list 物件 nums 裡的各元素出現次數，進行遞增排序"""
    # 把你的程式碼放在這裡
    staging=[]                              ##先製作暫存區
    for i in set(nums):                     ##將nums變成集合形式然後一個一個讀取(集合是為了不讓nums裡面重複的字母一直被讀取)
        staging.append((nums.count(i),i))   ##將上個步驟中集合讀出來的值一個個帶入nums中算個數，然後再與集合讀出來的值做tuple，並加入暫存區
                                            ##(做tuple是為了不讓裡面的數被改動)
    staging.sort()                          ##將暫存區內的數由小到大排序(排序依據抓的是tuple中第一個數)
    nums=[]                                 ##將nums清空
    for j in staging:                       ##讀暫存區內的一個個tuple(已排序)
        nums.append(j[1])                   ##將每個tuple中第一個數(從零開始算)加到nums

    return nums                             ##回傳答案


if __name__ == '__main__':
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_list = [2,0,9,8,9,2,8,2,0,9,7,9,8,2,9]
    output_list = sort_by_occurrence(input_list)
    print(output_list)


#留言板