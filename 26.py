def sort_by_occurrence(nums):
    """按照 list 物件 nums 裡的各元素出現次數，進行遞增排序"""
    # 把你的程式碼放在這裡

    data_list = []                                      #建立一個空list
    data_dict = {}                                      #建立一個空dict
    for i in nums:                                      #逐一抓出 input_list 的數字
        if i not in data_dict:                          #判斷 key 有沒有在字典裡
            data_dict[i] = 1                            #如果沒有，新增一組 key/value
        else:                                           #否則
            data_dict[i] = data_dict[i] + 1             #將原本 key 裡面的 value 加 1

    data_list = [(v,k)for k,v in data_dict.items()]     #建立一組 名叫 data_list 的 list of tuple 方便排序
    data_list.sort()                                    #將 data_list 排序

    result_list =[]                                     #創建一駔新的 list 來放最後排序好的數字
    for j in data_list:                                 #逐一取出 data_list 裡的數字
        result_list.append(j[1])                        #然後將取出的數字放進 result_list 裡

    return result_list                                  #最後回傳 result_list 
  


if __name__ == '__main__':
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_list = [1, 1, 1, 2, 2, 3]
    output_list = sort_by_occurrence(input_list)
    print(output_list)
    


#留言板