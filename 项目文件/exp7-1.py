class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
    # Your code here
    def is_worth_it(self):
        if self.draft-self.crew*1.5>20 :
            return True
        else:
            return False
        


EmptyShip =Ship(51,20)

print(EmptyShip.is_worth_it())