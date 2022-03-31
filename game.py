import random

Total_game_round = 1000 # 게임의 총 횟수를 지정합니다

class Main :
    @staticmethod
    def main( args) :
        Wallet = 100000 # 본인이 사용할 돈입니다.
        BetMoney = 100 # 베팅 금액입니다
        Time = 0
        Fail = 0
        while (Time < 1000) : #게임을 n번 실행합니다 n의 값이 커질수록 실행가능한 경우의수가 증가합니다
            
            randNum = random.randint(1,11) # 1부터 10 까지의 난수를 생성하여 생성된 난수에 따라 이기거나 집니다
            
            if (randNum < 5 and Wallet > 0) : # 50%의 확률로 이깁니다
                
                Wallet += BetMoney # 이겼을때 베팅한 금액의 두배를 가져갑니다
                
                BetMoney = 100 # 초기 베팅금액과 동일합니다
                
                Fail = 0 # 연속 베팅 손실의 수를 0으로 되돌립니다
            
            elif (randNum > 5 and Wallet > 0) : # 50%의 확률로 집니다
                    
                    Wallet -= BetMoney # 베팅한 금액만큼의 손실이 발생합니다
                    
                    BetMoney = BetMoney * 2 # 마틴게일 베팅법을 적용하였습니다 베팅손실시 베팅금액의 두배를 다시 베팅합니다
                    
                    Fail += 1 # 연속 베팅 손실의 횟수를 1 증가시킵니다.
            
            elif (Wallet < 0) : # 보유한 금액이 0이 될때 중지합니다.
                        
                        print("LOSE, ALL-IN")
                        print(f"게임은 총 {Time}회 실행되었습니다. 마지막 {Time - 1}라운드에서 보유금액보다 큰 금액을 {Time}라운드에 베팅하여 파산하였습니다.")
                        break


            elif (Time >= 1000):
                print(f"{Total_game_round}의 이상만큼 게임이 실행되었습니다. {Total_game_round} 이상의 수를 지정하십시오.")

            Time += 1 # 위 함수가 실행될때 마다 베팅횟수가 1 증가합니다.
            
            print("현재 보유금액:" + str(Wallet)+ " " + "총 베팅횟수:" + str(Time)+"회" + " " + "연속손실:" + str(Fail)+"회")
    

if __name__=="__main__":
    Main.main([])