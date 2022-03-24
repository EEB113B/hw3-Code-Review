def sort_by_occurrence(nums):
    def sort_by_occurrence(nums):
    from collections import Counter
    m = Counter(nums)  #藉由Counter計算list內出現物件的次數，回傳為dict type
    p = []
    q = []
    for i, j in m.items():  #將dict type轉為list 
        p = p + [(j, i)]    #將j定為物件出現次數，i定為物件，並將其包裝成新物件
    p.sort()                      #依據出現次數進行排列，由少至多
    for k in p:                   #將p內的新物件一一取出
        q = q + [k[1]]            #只取出i，也就是物件的部分，存為list q
    return q                      #回傳q，內容為出現次數由少到多的物件
    


if __name__ == '__main__':
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_list = [1, 1, 1, 2, 2, 3]
    output_list = sort_by_occurrence(input_list)
    print(output_list)

#留言板