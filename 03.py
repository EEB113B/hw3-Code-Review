def sort_by_occurrence(nums):
    """按照 list 物件 nums 裡的各元素出現次數，進行遞增排序"""
    #創造一字典存放數字和其出現的次數
    dict0 = {}
    n = len(nums)
    for i in range(0,n) :
        if nums[i] not in dict0:
            dict0[nums[i]] = 1

        else:
            dict0[nums[i]] +=1
    
    #key跟value對調，讓數字出現的次數在前面以做排序    
    lst1 = [[x,y]for y,x in dict0.items()]
    #排序
    lst1.sort()
    lst2 = []
    m = len(lst1)
    for i in range(0,m):
        lst2.append(lst1[i][1])

    return lst2
           
if __name__ == '__main__':
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_list = [1, 1, 1, 2, 2, 3]
    output_list = sort_by_occurrence(input_list)
    print(output_list)


#留言板