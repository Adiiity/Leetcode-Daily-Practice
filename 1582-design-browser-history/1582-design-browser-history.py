class BrowserHistory:

    def __init__(self, homepage: str):
        self.history=[homepage]
        self.curr=0
        self.leng=1

    def visit(self, url: str) -> None:
        self.curr+=1
        if len(self.history)==self.curr:
            self.history.append(url)
            self.leng+=1
        else:
            self.history[self.curr]=url
            self.leng=self.curr+1

    def back(self, steps: int) -> str:
        self.curr=max(self.curr-steps,0)
        return self.history[self.curr]

    def forward(self, steps: int) -> str:
        self.curr=min(self.curr+steps,self.leng-1)
        return self.history[self.curr]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)