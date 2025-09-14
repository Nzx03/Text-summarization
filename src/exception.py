import sys 
from src.logging import logging

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    # this for execution info which will give 3 info  ( in which first 2 info is not of my use)
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
     file_name, exc_tb.tb_lineno,str(error))

    return error_message   #error message

class CustomException(Exception):
    def __init__(self, error_message,error_detail:sys):  #constructor
        super().__init__(error_message)  #for inheriting the __init__ function (from exception)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message #going to print excpetion
    