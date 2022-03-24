from collections import Counter
def sort_by_occurrence(nums):
    """按照 list 物件 nums 裡的各元素出現次數，進行遞增排序"""
    # 把你的程式碼放在這裡
    count_list=Counter(input_list)#用Counter統計每個元素出現的次數，依照從高到低的順序排序，存入字典中
    sort_count_list=sorted(count_list.items(), key = lambda item:item[1])#對count_list字典中各項的value(各元素的出現次數)進行由小到大排列，並去除數值重複項，回傳排列後的新list
    output_list=[]#為output設一個新的空list
    for i in sort_count_list:#依序取出sort_count_list中各項
        output_list.append(i[0])#將各項的key(元素)存入output_list
    return output_list#回傳從小到大排序各元素出現次數的list 

if __name__ == '__main__':
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_list = [1, 1, 1, 2, 2, 3]
    output_list = sort_by_occurrence(input_list)
    print(output_list)

#留言板