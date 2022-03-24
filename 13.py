def sort_by_occurrence(nums):
    from collections import Counter
    counter = Counter(nums)                 #利用Counter來計算list內出現物件的次數，回傳為dict type
    a_list = []
    b_list = []
    for key, occur in counter.items():      #將dict type轉為list 
        a_list = a_list + [(occur, key)]    #occur為物件出現次數，key為物件，將其包裝成新物件
    a_list.sort()                           #依照出現次數由少到多排列
    for k in a_list:                        #將a_list內的新物件依照順序取出
        b_list = b_list + [k[1]]            #只取出key，也就是物件的部分，存為list_b
    return b_list                           #回傳b_list，內容為出現次數由少到多的物件


if __name__ == '__main__':
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_list = [1, 1, 1, 2, 2, 3]
    output_list = sort_by_occurrence(input_list)
    print(output_list)


#留言板