def sort_by_occurrence(inputlst):
    """按照 list 物件 nums 裡的各元素出現次數，進行遞增排序"""
    
    dict1 ={}  
    for i in range(0,len(inputlst)): #讀取inputlst全部內容
        if inputlst[i] not in dict1: #若inputlst的值不在dict1 創建一個new key value=1
            dict1[inputlst[i]] = 1
        else:
            dict1[inputlst[i]]+=1   #key已存在 value+1

    sortlst = [[v,k] for k,v in dict1.items()] #key value 位置順序互換 存到一個list of tuple 
    sortlst.sort()  #value由小到大排列
    outputlst=[]
    for i in range(0,len(sortlst)):  
        outputlst.append(sortlst[i][1]) #照順序把key寫入outputlst
        
    return outputlst




if __name__ == '__main__':
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_list = [2,0,9,8,9,2,8,2,0,9,7,9,8,2,9]
    output_list = sort_by_occurrence(input_list)
    print(output_list)


#留言板