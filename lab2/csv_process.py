#!/usr/bin/env python
# -*-coding:utf-8 -*-
import csv


def main():
    read_target = "score.csv"
    write_target = "calculated.csv"
    with open(read_target, newline="") as read_file:
        csv_reader = csv.DictReader(read_file)
        with open(write_target, "w", newline="") as write_file:
            csv_writer = csv.DictWriter(
                write_file, fieldnames=csv_reader.fieldnames)
            csv_writer.writeheader()

            work1_sum = 0
            work2_sum = 0
            exam_sum = 0
            count = 0

            for record in csv_reader:
                if record["姓名"] != "平均":
                    record["作业1"] = int(record["作业1"])
                    record["作业2"] = int(record["作业2"])
                    record["期末考试"] = int(record["期末考试"])
                    work1_sum += record["作业1"]
                    work2_sum += record["作业2"]
                    exam_sum += record["期末考试"]
                    count += 1
                else:
                    record["作业1"] = work1_sum/count
                    record["作业2"] = work2_sum/count
                    record["期末考试"] = exam_sum/count

                record["总成绩"] = record["作业1"] + record["作业2"] + record["期末考试"]
                record["平均"] = record["总成绩"]/3

                csv_writer.writerow(record)


if __name__ == "__main__":
    main()
