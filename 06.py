def sort_by_occurrence(nums):
    from collections import Counter
    """按照 list 物件 nums 裡的各元素出現次數，進行遞增排序"""
    # 把你的程式碼放在這裡 
    
    a = Counter(nums) #使用counter建立字典{數字:次數}
    sort_z=[] #建立一個空白list擺放排序好的數字
    sort_x = sorted(a.items(), key=lambda x: x[1]) #針對次數進行排序
    
    #讓排序好的數字利用append加入新的list
    for i in range(len(sort_x)):
        sort_y = sort_x[i][0]
        sort_z.append(sort_y)
    return sort_z 

     
           

    

if __name__ == '__main__':
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_list = [1,1,1,2,2,3]
    output_list = sort_by_occurrence(input_list)
    print(output_list)


#留言板