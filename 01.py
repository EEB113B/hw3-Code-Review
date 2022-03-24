def sort_by_occurrence(nums):
    """按照 list 物件 nums 裡的各元素出現次數，進行遞增排序"""
    # 把你的程式碼放在這裡
    nums_dic = {}#將輸入的list轉成dictionary
    ans = []#設定一個空list，用來放答案
    for i in nums:
        nums_dic[i] = nums.count(i)#利用count求出list中每個數字出現的次數，並加進dictionary裡，key是數字，value是次數
    nums_dic = sorted(nums_dic.items(),key=lambda x:x[1])#利用value(次數)由小到大排序
    for j in range(len(nums_dic)):
        num = nums_dic[j][0] #抓出由小到大排序後的key(數字)
        ans.append(num)#將數字加入空list中
    return(ans)#回傳答案
    

if __name__ == '__main__':
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_list = [1,1,1,2,2,3]
    output_list = sort_by_occurrence(input_list)
    print(output_list)


#留言板