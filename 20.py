def sort_by_occurrence(nums):
    """按照 list 物件 nums 裡的各元素出現次數，進行遞增排序"""
    # 把你的程式碼放在這裡
    d ={}
    #產生一個空的字典
    for i in range(0,len(input_list)):
        if input_list[i] in d:
            d[input_list[i]] +=1
        if input_list[i] not in d:
            d[input_list[i]] = 1
    #把沒出現過的元素加入字典，出現過的把Value加1
    
    list = [(v, k) for k, v in d.items()]
    #將d字典內的Key和Value互換包成tuple之後，形成list。
    list.sort()
    #將list依照V大小排序。
    new_list = [k for v, k in list]
    #將list中的tuple中(v, k)的k依序抓出來，放入new_list。
    return new_list
    #回傳 new_list
if __name__ == '__main__':
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_list = [1,1,1,2,2,3]
    output_list = sort_by_occurrence(input_list)
    print(output_list)


#留言板