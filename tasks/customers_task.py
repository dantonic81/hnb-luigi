import luigi
from customers_etl import main


class CustomersTask(luigi.Task):
    task_complete = False

    def run(self):
        main()
        self.task_complete = True

    def output(self):
        pass  # Define the output of the task if applicable

    def complete(self):
        # Override the complete method to always return True
        return self.task_complete


class PipelineTask(luigi.WrapperTask):
    def requires(self):
        return CustomersTask()


if __name__ == '__main__':
    luigi.run()
