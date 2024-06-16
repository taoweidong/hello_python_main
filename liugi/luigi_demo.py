# -*- coding: utf-8 -*-
import luigi


class PrintMsg(luigi.Task):
    message = luigi.Parameter(default="Hello guigi.....")

    def run(self):
        print("*" * 50)
        print(self.message)


if __name__ == '__main__':
    luigi.run()
