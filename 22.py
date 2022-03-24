def sort_by_occurrence(nums):
    """按照 list 物件 nums 裡的各元素出現次數，進行遞增排序"""
    # 把你的程式碼放在這裡
    count_list=[]
    count_dict={}
    for i in input_list:
        if i in count_dict:
            count_dict[i]+=1
        else :
            count_dict=1    
    count_list=[(v,k)for(k,v) in count_dict.items()]
    count_list.sort()
    result_list=[]
    for j in count_list:
        result_list.append(j[1])
        return result_list


if __name__ == '__main__':
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_list = [1, 1, 1, 2, 2, 3]
    output_list = sort_by_occurrence(input_list)
    print(output_list)


#留言板