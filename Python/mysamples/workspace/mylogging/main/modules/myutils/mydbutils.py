import re

def dbutils_exists(path):
    '''
    "dbfs:/"で始まるPathを使い，ファイルまたはディレクトリの存在確認する．
    '''
    try:
        dbutils.fs.ls(path)
        return True
    except Exception as e:
        return False


def dbfs_path_nonspark2spark(path):
    return re.sub(r"^/dbfs", "dbfs:", path)

def dbfs_path_spark2nonspark(path):
    return re.sub(r"^dbfs:", "/dbfs", path)


def hdfs_dir2objects(hdfs_path):
    '''
    DatabricksのノートブックからDBFSのファイルへのアクセスはHDFSフォーマットのファイルパス("/dbfs/"開始ではなく"dbfs:/"開始または"/dbfs/"直下のPath開始で，実体のファイルが有るディレクトリ名までのパス．Spark標準のファイル入出力関数を使うとこのフォーマットになってる．)になっているので，実体のファイルまでのパスに変換してlist型で返す．
    つまり，hdfs_pathのディレクトリ下にある"part-*"のファイル名(をhdfs_pathに文字列結合したファイルパス)のリストを返す．
    list型で返す理由は，hdfs_pathのディレクトリ下に複数パーティション存在する場合に対応するため．
    - https://stackoverflow.com/questions/41990086/specifying-the-filename-when-saving-a-dataframe-as-a-csv

    - Args
        - hdfs_path:str: HDFSフォーマット，つまりディレクトリ名になっているファイルパス．"/dbfs/"開始と"dbfs:/"開始のどちらでも可．
    - Returns
        - hdfs_objects:list: 実体のファイルまでのパスのリスト．
    '''
    # dbutilsを使うので，"/dbfs/"開始なら"dbfs:/"開始にしておく．
    path = dbfs_path_nonspark2spark(hdfs_path) # re.sub(r"^/dbfs", "dbfs:", path)
    hdfs_objects = [hdfs_path + "/" + l.name for l in dbutils.fs.ls(path) if l.name[0:5] == "part-"]
    return hdfs_objects
