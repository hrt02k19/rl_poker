import itertools

from .handrank import HandRank

card=[]
for i in range(13):
    for j in range(4):
        card.append([14-i, j%4])

def hand(c1,c2,c3,c4,c5,c6,c7):
    #7枚のカードのidを投げると、ハンドの強さを返す

    #ロイヤルストレートフラッシュ: (10,)
    #ストレートフラッシュ: (9, "ストレートの最大値")
    #4カード: (8, "4枚ある数字", "残りの最大値")
    #フルハウス: (7, "3枚ある数字の最大値" ,"それ以外で2枚ある数字の最大値")
    #フラッシュ: (6, "同じスートの最大値","2番目",...,"5番目")
    #ストレート: (5, "ストレートの最大値")
    #3カード: (4, "3枚ある数字", "残りの最大値", "2番目")
    #2ペア: (3, "2枚ある数字の最大値","2番目","残りの最大値")
    #1ペア: (2, "2枚ある数字","残りの最大値","2番目","3番目")
    #ハイカード: (1, "最大値" ,"2番目",...,"5番目")

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

    if max(s_counter)>=5:  #フラッシュ成立
        straight=0
        flush_n=[]
        flush_s=s_counter.index(max(s_counter)) #フラッシュのスート
        for c in C:
            if card[c][1]==flush_s:
                flush_n.append(card[c][0])
                if card[c][0] == 14:
                    flush_n.append(1)
        for i in range(14, 0, -1):
            if i in flush_n:
                straight=straight+1
                
                if straight==5:  #ストレート成立
                    if i==10:     #ロイヤルストレートフラッシュ
                        return HandRank(10)
                    else:        #ストレートフラッシュ
                        return HandRank(9,i+4) 
            else:
                straight=0
        else:
            flush_n = sorted(flush_n, reverse=True)
            return HandRank(6,flush_n[0],flush_n[1],flush_n[2],flush_n[3],flush_n[4])
    
    if max(n_counter)==4:   #4カード
        id_4=n_counter.index(max(n_counter)) #4カードの数字
        for i in range(15):
            if 1 <= n_counter[i] <= 3:
                n_second_id=i
        return HandRank(8,id_4,n_second_id)
    
    straight=0
    for i in range(13):
        if n_counter[14-i]>=1:
            straight=straight+1
        if n_counter[14-i]==0:
            straight=0
        if straight==5: #ストレート
            return HandRank(5,14-i+4)
    if straight == 4 and n_counter[14] >= 1:
        return HandRank(5, 5)
            
            
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
            return HandRank(7,n_first_id,n_second_id)
        

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
            return HandRank(4,n_first_id,n_second_id,n_third_id)
        
    if max(n_counter)==2:
        n_counter_2=sorted(n_counter, reverse=True)
        n_first_id=0
        n_second_id=0
        n_third_id=0
        n_fourth_id=0

        if n_counter_2[1]>=2:   #2ペア成立
            for i in range(15):
                if n_counter[i]==2:
                    if n_first_id == 0:
                        n_first_id=i
                    elif n_second_id == 0:
                        n_second_id=n_first_id
                        n_first_id=i
                    else:
                        n_third_id = max(n_second_id, n_third_id)
                        n_second_id = n_first_id
                        n_first_id = i
                if n_counter[i]==1:
                    n_third_id=i
            return HandRank(3,n_first_id,n_second_id,n_third_id)
        else:   #1ペア
            for i in range(15):
                if n_counter[i]==2:
                    n_first_id=i
                if n_counter[i]==1:
                    n_fourth_id=n_third_id
                    n_third_id=n_second_id
                    n_second_id=i
            return HandRank(2,n_first_id,n_second_id,n_third_id,n_fourth_id)

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
        return HandRank(1,n_first_id,n_second_id,n_third_id,n_fourth_id,n_fifth_id)

def board_battle(board1,board2,board3,board4,board5,hero1,hero2,villain1,villain2):
    hero_hand=hand(board1,board2,board3,board4,board5,hero1,hero2)
    villain_hand=hand(board1,board2,board3,board4,board5,villain1,villain2)
    if hero_hand>villain_hand:
        return 1
    if hero_hand==villain_hand:
        return 0
    if hero_hand<villain_hand:
        return -1
    
def winning_rate(hero1,hero2,villain1,villain2):
    battle_count=0
    win_count=0
    other=[]
    for i in range(52):
        if i!=hero1 and i!=hero2 and i!=villain1 and i!=villain2:
            other.append(i)
    for board in itertools.combinations(other,5):
        if board_battle(board[0],board[1],board[2],board[3],board[4],hero1,hero2,villain1,villain2)==1:
            win_count+=1
        battle_count+=1
    return win_count / battle_count * 100
