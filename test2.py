class Test:
    def __init__(self, questions):
        self.questions = questions
    def add_more(self, more):
        self.questions += more
    def __str__(self):
        return f'I have {self.questions} questions to answer.'
class Quiz(Test):
    def __str__(self):
        return 'All my questions are multiple choice.'
            
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
