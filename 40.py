def sort_by_occurrence(nums):
    """按照 list 物件 nums 裡的各元素出現次數，進行遞增排序"""
    # 把你的程式碼放在這裡
    mylist=[]   #建一個list
    mydict={}   #建一個dictionary
    for i in nums:  #把nums一個一個取出來
        if i not in mydict:  #假如字典沒有key i
            mydict[i]=1  #新增一組key:value
        else:
            mydict[i]+=1  #字典有key，value加一
    mylist=[(v,k) for k,v in mydict.items()]  #轉成list of tuples才能排序
    mylist.sort()  #排序
    finlist=[]  #建一個list
    for m in mylist:   #把mylist一個一個取出來 
        finlist.append(m[1])  #把m裡的第二個元素取出並加到finlist
    return finlist




if __name__ == '__main__':
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_list = [1, 1, 1, 2, 2, 3]
    output_list = sort_by_occurrence(input_list)
    print(output_list)


#留言板