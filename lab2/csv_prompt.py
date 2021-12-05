#!/usr/bin/env python
# -*-coding:utf-8 -*-
import csv
import prettytable as pt


def is_continue():
    """ask if continue

    Returns:
        bool: whether continue
    """
    text = input("是否继续([y]/n)?")
    if text == '':
        text = 'y'
    if text.strip().lower() == 'y':
        return True
    else:
        return False


def print_score(record: dict):
    table = pt.PrettyTable()
    table.field_names = record.keys()
    table.add_row(record.values())
    print(table)


def main():
    read_target = "calculated.csv"
    table = pt.PrettyTable()
    records = {}

    print(f"[*]正在从 {read_target} 加载数据...")
    with open(read_target, 'r', newline='') as f:
        csv_reader = csv.DictReader(f)

        table.field_names = csv_reader.fieldnames
        for record in csv_reader:
            table.add_row(record.values())
            name = record["姓名"]
            records[name] = record

    print("[+]加载成功！")
    print(table)

    while True:
        name = input("请输入你想查询成绩的人的姓名：").strip()
        print("[*]正在查询...")
        if name in records:
            print("[+]查询成功！")
            print_score(records[name])
        else:
            print("[-]查无此人！")
        if not is_continue():
            break


if __name__ == "__main__":
    main()
