def sort_by_occurrence(nums):
    d_dic = {}  #d_dic用來存放nums中各整數出現次數
    dic2 = {}   #dic2將d_dic中的key與value反轉
    c_lst = []  # 存放出現次數的list
    f_lst = []  # 最終結果
    for i in nums:  # 計算nums中各整數出現次數，放入d_dic中
        if i not in d_dic:
            d_dic[i] = 1
        else:
            d_dic[i] += 1
    for j in set(nums):  #把d_dic中的value提出來放進c_lst
        case = d_dic[j]
        c_lst.append(case)
        dic2[case] = j  #dic2的key是出現次數，value是nums中的整數
    c_lst = sorted(c_lst) #將出現次數由小到大排列
    for k in c_lst:  #  將排序過的出現次數按照大小教出對應的整數，並放進f_lst中
        key = dic2[k]
        f_lst.append(key)
    return f_lst

if __name__ == '__main__':
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_list = [1, 1, 1, 2, 2, 3]
    output_list = sort_by_occurrence(input_list)
    print(output_list)

#留言板