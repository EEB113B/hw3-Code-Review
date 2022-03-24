def sort_by_occurrence(nums):
    """按照 list 物件 nums 裡的各元素出現次數，進行遞增排序"""
    # 把你的程式碼放在這裡
    from collections import Counter

    count = Counter(nums)
    tn = []    
    n = []
    for (key, value) in count.items():    #key = numeber, value = times
        re = 0 
        for k in tn:    #「去除掉數值重複」
            if value == k[1]:
                tn.remove(k)
                re = 1    
                break 
        if re:
            continue
        else:  
            tn = tn + [(key, value)]   #[(number, times)]

    tn = sorted(tn, key=lambda t:t[1])  #「從小到大排序各元素的出現次數」
    for l in tn:
        n = n + [l[0]]   #[number]

    return n
    

if __name__ == '__main__':
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_list = [1,1,1,2,2,3]
    output_list = sort_by_occurrence(input_list)
    print(output_list)


#留言板