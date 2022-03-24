def sort_by_occurrence(nums):
    from collections import Counter
    c = Counter(nums)  #利用Counter來計算list內出現物件的次數，回傳為dict type
    a = []
    b = []
    for key, occur in c.items():  #將dict type轉為list 
        a = a + [(occur, key)]    #occur為物件出現次數，key為物件，將其包裝成新物件
    a.sort()                      #依據出現次數排列，由少到多
    for k in a:                   #將a內的新物件依序取出
        b = b + [k[1]]            #只取出key，也就是物件的部分，存為list b
    return b                      #回傳b，內容為出現次數由少到多的物件

        
    


if __name__ == '__main__':
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_list = [2,0,9,8,9,2,8,2,0,9,7,9,8,2,9]
    output_list = sort_by_occurrence(input_list)
    print(output_list)


#留言板