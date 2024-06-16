# -*- coding: utf-8 -*-
import luigi


class TaskA(luigi.Task):
    def run(self):
        print("Running Task A")


class TaskB(luigi.Task):

    def requires(self):
        return TaskA()

    def run(self):
        print("Running Task B")


if __name__ == '__main__':
    luigi.run()
