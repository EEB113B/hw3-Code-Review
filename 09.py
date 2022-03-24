#def sort_by_occurrence(nums):
    #"""按照 list 物件 nums 裡的各元素出現次數，進行遞增排序"""
    # 把你的程式碼放在這裡


#if __name__ == '__main__':
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    #input_list = [1, 1, 1, 2, 2, 3]
    #output_list = sort_by_occurrence(input_list)
    #print(output_list)

def sort_by_occurrence(objects):
    from test_list import Counter
    number = Counter(objects)                     #利用Counter來計算list內出現物件的次數，回傳為dict type
    lst_1 = []
    lst_2 = []
    for key, apper in c.items():            #將dict type轉為list 
        lst_1 = lst_1 + [(apper, key)]      #apper為物件出現次數，key為物件，將其包裝成新物件
    lst_1.sort()                            #依據出現次數排列，由少到多
    for k in lst_1:                         #將lst_1內的新物件依序取出
        lst_2 = lst_2 + [k[1]]                      #只取出key，也就是物件的部分，存為list_2
    return lst_2                                #回傳lst_2，次數由少到多的物件

#留言板