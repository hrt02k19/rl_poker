card=[]
for i in range(13):
    for j in range(4):
        card.append([14-i, j%4])

def hand(c1,c2,c3,c4,c5,c6,c7):
    #7枚のカードのidを投げると、ハンドの強さを返す

    #ロイヤルストレートフラッシュ: (1,)
    #ストレートフラッシュ: (2, "ストレートの最大値")
    #4カード: (3, "4枚ある数字", "残りの最大値")
    #フルハウス: (4, "3枚ある数字の最大値" ,"それ以外で2枚ある数字の最大値")
    #フラッシュ: (5, "同じスートの最大値","2番目",...,"5番目")
    #ストレート: (6, "ストレートの最大値")
    #3カード: (7, "3枚ある数字", "残りの最大値", "2番目")
    #2ペア: (8, "2枚ある数字の最大値","2番目","残りの最大値")
    #1ペア: (9, "2枚ある数字","残りの最大値","2番目","3番目")
    #ハイカード: (10, "最大値" ,"2番目",...,"5番目")

    C=[c1,c2,c3,c4,c5,c6,c7]
    N=[]
    S=[]
    for c in C:
        N.append(card[c][0])
        S.append(card[c][1])

    #各数字の枚数カウンター
    n_counter=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for n in N:
        for i in range(14):
            if n==i+1:
                n_counter[n]=n_counter[n]+1
    
    #各スートの枚数カウンター
    s_counter=[0,0,0,0]
    for s in S:
        for i in range(4):
            if s==i:
                s_counter[s]=s_counter[s]+1

    print(n_counter, s_counter)

    if max(s_counter)>=5:  #フラッシュ成立
        straight=0
        for i in range(13):
            if n_counter[14-i]>=1:
                straight=straight+1
                
                if straight==5:  #ストレート成立
                    if i==4:     #ロイヤルストレートフラッシュ
                        return (10,)
                    else:        #ストレートフラッシュ
                        return (9,14-i+4)
            
            if n_counter[14-i]==0:
                straight=0

            if i==12:
                flash_s=s_counter.index(max(s_counter)) #フラッシュのスート
                flash_n=[]
                for c in C:
                    if card[c][1]==flash_s:
                        flash_n.append(card[c][0])
                flash_n= sorted(flash_n, reverse=True)

                return (6,flash_n[0],flash_n[1],flash_n[2],flash_n[3],flash_n[4])
    
    if max(n_counter)==4:   #4カード
        id_4=n_counter.index(max(n_counter)) #4カードの数字
        n_counter_4=sorted(n_counter, reverse=True)
        n_second=n_counter_4[1]
        n_second_id=0
        for i in range(15):
            if n_counter[i]==n_second:
                n_second_id=i
        return (3,id_4,n_second_id)
    
    straight=0
    for i in range(13):
        if n_counter[14-i]>=1:
            straight=straight+1
        if n_counter[14-i]==0:
            straight=0
        if straight==5: #ストレート
            return (6,14-i+4)
            
            
    if max(n_counter)==3:   #3カード成立
        n_counter_3=sorted(n_counter, reverse=True)
        
        if n_counter_3[1]>=2:  #フルハウス成立
            n_first_id=0
            n_second_id=0 
            for i in range(15):
                if n_counter[i]==3:
                    if n_first_id==0:
                        n_first_id=i
                    else:
                        n_second_id=n_first_id
                        n_first_id=i
                if n_counter[i]==2:
                    n_second_id=i
            return (4,n_first_id,n_second_id)
        

        else:   #3カード
            n_first_id=0
            n_second_id=0
            n_third_id=0
            for i in range(15):
                if n_counter[i]==3:
                    n_first_id=i
                if n_counter[i]==1:
                    if n_second_id==0:
                        n_second_id=i
                    else:
                        n_third_id=n_second_id
                        n_second_id=i
            return (7,n_first_id,n_second_id,n_third_id)
        
    if max(n_counter)==2:
        n_counter_2=sorted(n_counter, reverse=True)
        n_first_id=0
        n_second_id=0
        n_third_id=0
        n_fourth_id=0

        if n_counter_2[1]>=2:   #2ペア成立
            for i in range(15):
                if n_counter[i]==2:
                    if n_first_id==0:
                        n_first_id=i
                    else:
                        n_second_id=n_first_id
                        n_first_id=i
                if n_counter[i]==1:
                    n_third_id=i
            return (8,n_first_id,n_second_id,n_third_id)
        else:   #1ペア
            for i in range(15):
                if n_counter[i]==2:
                    n_first_id=i
                if n_counter[i]==1:
                    n_fourth_id=n_third_id
                    n_third_id=n_second_id
                    n_second_id=i
            return (9,n_first_id,n_second_id,n_third_id,n_fourth_id)

    else:
        n_first_id=0
        n_second_id=0
        n_third_id=0
        n_fourth_id=0
        n_fifth_id=0
        for i in range(15):
            if n_counter[i]==1:
                    n_fifth_id=n_fourth_id
                    n_fourth_id=n_third_id
                    n_third_id=n_second_id
                    n_second_id=n_first_id
                    n_first_id=i
        return (10,n_first_id,n_second_id,n_third_id,n_fourth_id,n_fifth_id)

print(hand(0,5,10,15,20,25,30))