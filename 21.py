def sort_by_occurrence(lst1):
    """按照 list 物件 nums 裡的各元素出現次數，進行遞增排序"""
    

    dict1 ={}
    for k in range(0,len(lst1)):
        if lst1[k] not in dict1:
            dict1[lst1[k]]=1
        else:
            dict1[lst1[k]]+=1

    lst2= [[v,i] for i,v in dict1.items()]
    lst2.sort()
    lst3=[]
    for k in range(0,len(lst2)):
        lst3.append(lst2[k][1])

    return lst3




if __name__ == '__main__':
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_list = [2,0,9,8,9,2,8,2,0,9,7,9,8,2,9]
    output_list = sort_by_occurrence(input_list)
    print(output_list)


#留言板