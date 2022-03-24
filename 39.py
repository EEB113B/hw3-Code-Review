def sort_by_occurrence(nums):
    """按照 list 物件 nums 裡的各元素出現次數，進行遞增排序"""
    # 把你的程式碼放在這裡
    mydict1 = {}
    lst2 = []
    for i in input_list:
    #逐個掃描list中的數字
        if i not in mydict1:
            mydict1[i] = 1
            #dict裡的key沒有該項就加入
        else:
            mydict1[i]+=1
            #如果有就將他的數值(count)加一
    lst1 = [(v,k) for k,v in mydict1.items()]
    #將(key,value)轉換成tuple放入list

    lst1.sort()
    for j in lst1:
    #將每個tuple抓出來
        for k in j:
            lst2.append(k)   
            #將每個tuple中的每一項抓出來放入list
    return (lst2[1::2])
    #回傳每一個key



if __name__ == '__main__':
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_list = [1, 1, 1, 2, 2, 3]
    output_list = sort_by_occurrence(input_list)
    print(output_list)


#留言板