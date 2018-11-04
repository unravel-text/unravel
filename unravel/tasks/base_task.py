from celery import Task


class BaseTask(Task):

    def __init__(self):
        """
        A task is not instantiated for every request, but is registered in the task registry as a global instance.
        This means that the __init__ constructor will only be called once per process,
        and that the task class is semantically closer to an Actor.
        """

    def run(self, *args, **kwargs):
        return 0

    def after_return(self, status, retval, task_id, *args, **kwargs) -> None:
        """
        Handler called after the task returns.
        The return value of this handler is ignored.
        :param status: Current task state.
        :param retval: Task return value/exception.
        :param task_id: Unique id of the task.
        :param args: Original arguments for the task that returned.
        :param kwargs: Original keyword arguments for the task that returned.
        :param einfo: ExceptionInfo instance, containing the traceback (if any).
        :return:
        """

        einfo = kwargs.get('einfo')

    def on_failure(self, exc, task_id, *args, **kwargs) -> None:
        """
         This is run by the worker when the task fails.
          The return value of this handler is ignored.
        :param exc: The exception raised by the task.
        :param task_id: Unique id of the failed task.
        :param args: Original arguments for the task that failed.
        :param kwargs: Original keyword arguments for the task that failed.
        :param einfo:
        :return:
        """

        einfo = kwargs.get('einfo')

    def on_retry(self, exc, task_id, *args, **kwargs) -> None:
        """
        This is run by the worker when the task is to be retried.
        The return value of this handler is ignored.
        :param exc: The exception sent to retry().
        :param task_id: Unique id of the retried task.
        :param args: Original arguments for the retried task.
        :param kwargs: Original keyword arguments for the retried task.
        :param einfo: ExceptionInfo instance, containing the traceback.
        :return:
        """

        einfo = kwargs.get('einfo')

    def on_success(self, retval, task_id, *args, **kwargs) -> None:
        """
        Run by the worker if the task executes successfully.
        The return value of this handler is ignored.
        :param retval: The return value of the task.
        :param task_id: Unique id of the executed task.
        :param args: Original arguments for the executed task.
        :param kwargs: Original keyword arguments for the executed task.
        :return:
        """

        pass
