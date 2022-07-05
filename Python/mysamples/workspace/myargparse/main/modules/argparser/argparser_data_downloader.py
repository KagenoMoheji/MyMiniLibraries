from argparse import ArgumentParser

from modules.argparser.validator_datetime import valid_yyyymmdd_or_datediff
from modules.argparser.validator_filesystem import valid_fname

def get_parser(datetime_ref, dir_check_existence, description):
    parser = ArgumentParser(description = description)
    parser.add_argument(
        "-d", "--targetDate",
        help = "取得するデータ断面．`yyyyMMdd`または`<int>d`で指定すること．",
        required = True,
        type = valid_yyyymmdd_or_datediff(datetime_ref)
    )
    parser.add_argument(
        "-e", "--envFile",
        help = "環境変数ファイル(拡張子必要)",
        required = True,
        type = valid_fname(dir_check_existence = dir_check_existence)
    )
    return parser
