import re
import json

class MyDict(dict):
    def exist_nested_keys(self, *keys):
        '''
        https://stackoverflow.com/a/43491315
        '''
        d = self
        for key in keys:
            try:
                # ここでネストしつつキーの存在確認。キーがなかったら例外投げる。
                d = d[key]
            except KeyError:
                return False
        return True
    
    def validate_required_keyexist_type(self, defdict_required):
        '''
        "{key1: {key2_1: {key3: type, key2_2: type}"構造で必須キーが記載された引数keys_requiredを基に，関数呼び出しした辞書型データの必須キーの存在・型判定を行う．
        ※"type=str|int|float|...|[str|int|float|...]"であり，辞書型以外の場合はそれがキーに対するデータ型とする．
        ※keyにおいて，"#.+#"のようにカギカッコで囲まれて渡される「繰り返し構造型」の場合，それ以外のkeyの存在は認めず，またそのkeyに対応するデータは，共通の構造の型定義でなければならない．
        
        - Args
            - defdict_required:dict: "{key1: {key2_1: {key3: type, key2_2: type}"構造の必須キーの辞書型定義．
        - Returns
            - res:boolean: 必須キーがすべて存在し，型違反が無い場合True．
            - err:Exception: res=Falseの際に渡されるエラーオブジェクト．
        '''
        for key in defdict_required:
            regresult_desc_key = re.fullmatch(r"^\[.+\]$", key) # description of key
            if regresult_desc_key:
                if len(defdict_required.keys()) > 1:
                    # 繰り返し構造型の定義の位置において，2つ以上のキーが存在している場合，繰り返し構造型のみにするようにエラーを投げる．
                    return False, KeyError("Found other keys in the same layer of key '{}'.".format(key))
                # 繰り返し構造型
                defdict_loop = defdict_required[key]
                for data_key in self.keys():
                    res, err = MyDict(self[data_key]).validate_required_keyexist_type(defdict_loop)
                    if not res:
                        return False, err
            else:
                # ここで定義に反している部分を見つける
                if key not in self.keys():
                    # 必須のキーが存在しなかった場合はFalseを返す
                    return False, KeyError("Not found key '{}'.".format(key))

                if type(defdict_required[key]) == type:
                    if defdict_required[key] != type(self[key]):
                        # keyに対応する値値の型が一致しなかった場合はFalseを返す
                        # プリミティブ的な型(str含む)の判定はここで対応できる
                        return False, TypeError("Invalid type in key '{}'.".format(key))
                else:
                    # 定義において[]や{}の場合はtype型ではないので分岐が必要になる
                    if type(defdict_required[key]) != type(self[key]):
                        # keyに対応する値値の型が一致しなかった場合はFalseを返す
                        return False, TypeError("Invalid type in key '{}'.".format(key))

                    if type(defdict_required[key]) == dict: # type(self[key]) == dict
                        # 値が辞書の場合，子の辞書をvalidate_required_keyexist_typeに渡して再帰させる
                        res, err = MyDict(self[key]).validate_required_keyexist_type(defdict_required[key])
                        if res == False:
                            return res, err
                    elif type(defdict_required[key]) == list: # type(self[key]) == list
                        # 値がリストの場合，リストに格納された値すべてが定義の型か調べる
                        if not all([type(v) == defdict_required[key][0] for v in self[key]]):
                            return False, TypeError("Invalid type in list of key '{}'.".format(key))
            
        return True, None
    
    def format_json(self, indent = 4, ensure_ascii = False):
        '''
        https://qiita.com/Hyperion13fleet/items/7129623ab32bdcc6e203#json%E3%82%92%E7%B6%BA%E9%BA%97%E3%81%AB%E8%A1%A8%E7%A4%BA%E3%81%A7%E3%81%8D%E3%82%8B%E3%82%88%E3%81%86%E3%81%ABdump%E3%81%99%E3%82%8B
        '''
        return json.dumps(self, indent = indent, ensure_ascii = ensure_ascii)
    
    def output_json(self, fname, mode = "w", indent = 4, ensure_ascii = False, encoding = "utf8"):
        with open(fname, mode = mode, encoding = encoding) as f:
            f.write(self.format_json(indent = indent, ensure_ascii = ensure_ascii))
