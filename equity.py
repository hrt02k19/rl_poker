card=[]
for i in range(13):
    for j in range(4):
        card.append([14-i, j%4])

def hand(c1,c2,c3,c4,c5,c6,c7):
    C=[c1,c2,c3,c4,c5,c6,c7]
    N=[]
    S=[]
    for c in C:
        N.append(card[c][0])
        S.append(card[c][1])

    #各数字の枚数カウンター
    n_counter=[None,None,0,0,0,0,0,0,0,0,0,0,0,0,0]
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

    if max(s_counter)>=5:  #フラッシュ成立
        straight=0
        for i in range(13):
            if n_counter[14-i]>=1:
                straight=straight+1
                
                if straight==5:  #ストレート成立
                    straight=0
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
    
    return 0

print(hand(0,4,8,12,16,7,5))
print(hand(1,9,13,21,25,29,2))
