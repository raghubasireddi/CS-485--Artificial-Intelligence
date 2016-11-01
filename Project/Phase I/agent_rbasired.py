from agents import Agent
class Agent_rbasired(Agent):
    def will_buy(self, value, price, prob):
	if (prob > 0.7):
		return True
	elif (prob > 0.5 and price/value < 0.3):
		return True
	elif(price/value < 0.4):
		return True
