def sort_by_occurrence(nums):
    """按照 list 物件 nums 裡的各元素出現次數，進行遞增排序"""
    # 把你的程式碼放在這裡
    new_list = []                        
    for i in nums:                      #去除list中重複值
        if i not in new_list:
            new_list.append(i)
    count_times = []
    for j in new_list:                       #計算每個元素出現次數
        times = nums.count(j)
        count_times.append(times)
    num_times=[]
    for x,y in zip(new_list,count_times):    #將new和count_times的元素和出現次數組成新的list
        num_times.append([x,y])
    def sort_key(str):                  #定義一個key作為排序依據
        return str[1]
    num_times.sort(key=sort_key )             #依出現次數遞增排序(reverse = True)
    result = []
    for k in range(len(num_times)):           #將排序後的元素取出，成為新的list
        result.append(num_times[k][0])
    return result



if __name__ == '__main__':
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_list = [1,1,1,2,2,3]
    output_list = sort_by_occurrence(input_list)
    print(output_list)

#留言板