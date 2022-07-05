from argparse import ArgumentTypeError
import os

def valid_fname(dir_check_existence):
    '''
    - Args
        - dir_check_existence:str: ファイルの存在チェックするディレクトリ
    - Returns
        - validate:func: 引数バリデータを返す．
    '''
    def validate(input):
        '''
        - Args
            - input:str: argparse.ArgumentParserが受け取った入力
        - Returns
            - :str: 引数でもらったファイル名そのまま
        '''
        filepath = "{}/{}".format(dir_check_existence, input)
        if os.path.isfile(filepath):
            return input
        else:
            raise ArgumentTypeError(
                "[filepath: {}]File not found.".format(filepath)
            )
    return validate

