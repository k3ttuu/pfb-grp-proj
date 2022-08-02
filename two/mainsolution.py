import api, cash_on_hand, profit_loss, overheads

def main ():
    forex = api.apifunction()
    overheads.overheads.function(forex)
    cash_on_hand.cash_on_hand.function(forex)
    profit_loss.profit.loss.function(forex)
    
main ()