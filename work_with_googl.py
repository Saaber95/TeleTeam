import string
from pprint import pprint

import gspread
from gspread import Cell, Client, Spreadsheet, Worksheet
from gspread.utils import rowcol_to_a1
import requests

SPREADSHEET_URL = "https://docs.google.com/spreadsheets/d/.../"


def show_available_worksheets(sh: Spreadsheet):
    worksheets = sh.worksheets()

    for ws in worksheets:
        print("Worksheet with title", repr(ws.title), "and id", ws.id)


def show_main_ws(sh: Spreadsheet):
    main_ws = sh.sheet1
    print("Main ws:", main_ws)


def create_ws_fill_and_del(sh: Spreadsheet):
    another_worksheet = sh.add_worksheet("another", rows=15, cols=10)
    print(another_worksheet)
    # input("enter to fill ws")
    another_worksheet.insert_row(["hello", "world"])
    # input("enter to fill ws again")
    another_worksheet.insert_row(list(range(1, 16)))
    # input("enter to delete ws")
    sh.del_worksheet(another_worksheet)


def insert_some_data(ws: Worksheet):
    ws.insert_rows([
        list(range(1, 40)),
        list(string.ascii_lowercase),
        list(string.ascii_uppercase),
        list(string.punctuation),
        list("hello world and OTUS!"),
    ])


def append_rows(ws: Worksheet):
    ws.append_rows([
        list(reversed(string.ascii_uppercase)),
        list(reversed(string.ascii_lowercase)),
        list(range(50, 1, -3)),
    ])


def update_table_by_cells(ws: Worksheet):
    ws.update_cell(2, 3, "Hello OTUS!!!")
    rows = 3
    cols = 2
    row = 4
    col = 1
    range_start = rowcol_to_a1(row, col)
    range_end = rowcol_to_a1(row + rows - 1, col + cols - 1)
    cells_range = f"{range_start}:{range_end}"
    print("update range", cells_range)
    values = [[""] * cols] * rows
    print("values", values)
    ws.update(cells_range, values)


def show_all_values_in_ws(ws: Worksheet):
    list_of_lists = ws.get_all_values()
    print(list_of_lists)
    print("===" * 20)
    for row in list_of_lists:
        print(row)


def create_and_fill_comments_ws(sh: Spreadsheet):
    comments_data = requests.get("https://jsonplaceholder.typicode.com/comments").json()
    header_row = ["id", "postId", "email", "name", "body"]
    rows = [header_row]
    for comment in comments_data:  # type: dict
        rows.append([
            comment.get(key, "")
            for key in header_row
        ])

    comments_ws = sh.add_worksheet("comments", rows=1, cols=len(header_row))
    comments_ws.insert_rows(rows)


def show_worksheet(ws: Worksheet):
    list_of_dicts = ws.get_all_records()
    pprint(list_of_dicts)


def find_comment_by_author(ws: Worksheet):
    cell: Cell = ws.find("Hayden@althea.biz")
    print("Found something at row %s and col %s" % (cell.row, cell.col))

    row = ws.row_values(cell.row)
    print(row)


def do_batch_update(ws: Worksheet):
    batches = []
    for i in range(1, 20, 2):
        items_count = i + 1
        addr_from = rowcol_to_a1(i, 1)
        addr_to = rowcol_to_a1(i, items_count)
        data_range = f"{addr_from}:{addr_to}"
        print("add range", data_range)
        batch = {
            "range": data_range,
            "values": [[i] * items_count],
        }
        batches.append(batch)

    ws.batch_update(batches)


def apply_formatting(ws: Worksheet):
    cell_format = {
        "horizontalAlignment": "CENTER",
        "backgroundColor": {
            "red": 0.5,
            "green": 1.0,
            "blue": 0.3,
        },
        "textFormat": {
            "foregroundColor": {
                "red": 0.2,
                "green": 0.7,
                "blue": 1,
            },
            "fontSize": 12,
            "bold": True,
        },
    }
    ws.format("B11:C13", cell_format)


