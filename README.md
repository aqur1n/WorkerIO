# WorkerIO
![PyPI - Version](https://img.shields.io/pypi/v/workerio?style=for-the-badge&logo=pypi&logoColor=white)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/workerio?style=for-the-badge&logo=python&logoColor=white)

A tool that allows you to create your own workers and distribute work among them.

Each worker creates its own thread in which it will fetch jobs from the `queue.SimpleQueue` queue and execute them in its `execute` method.
The result of the job is returned using `asyncio.Future`.

> [!WARNING]
> Since everything will be executed in another thread, use thread-safe functions. Do not modify files unless you are sure they are not open in another worker.

### Installing
```console
# Linux/macOS
python3 -m pip install -U workerio

# Windows
py -3 -m pip install -U workerio
```

### Basic examples
```py
import workerio
from asyncio import new_event_loop
from requests import get


class MyUrlWorker(workerio.Worker):
    def execute(self, url: str):
        return get(url).text


manager = workerio.Manager()
manager.add_worker(MyUrlWorker())

async def main(): 
    manager.start_all()

    result = await manager.put_work(MyUrlWorker, "https://example.com")
    print(result)

    manager.stop_all_nowait()

if __name__ == "__main__":
    loop = new_event_loop()
    loop.run_until_complete(main())
```

```py
import workerio
from asyncio import Future


class MyManager(workerio.Manager):
    def put_work(self, worker_type, *args, **kwargs) -> Future:
        suitable_workers = self.get_suitable_workers(worker_type, *args, **kwargs)

        if len(suitable_workers) == 0:
            raise workerio.SuitableWorkerNotFound()

        selected_worker = suitable_workers[0]
        for worker in suitable_workers:
            if worker.qsize == 0 and worker.check(*args, **kwargs):
                selected_worker = worker
                break

        return selected_worker.put_job(*args, **kwargs)

manager = MyManager()

```
