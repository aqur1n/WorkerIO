"""
MIT License

Copyright (c) 2025-present aqur1n

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


class WorkerioException(Exception): ...


class ManagerException(WorkerioException): ...

class WorkersNotFound(ManagerException):
    def __init__(self, worker_type) -> None:
        super().__init__(f"No active workers {worker_type} were found")

class SuitableWorkerNotFound(ManagerException):
    def __init__(self) -> None:
        super().__init__("Unable to find a suitable worker")

class WorkerAlreadyPresent(ManagerException):
    def __init__(self) -> None:
        super().__init__("This worker is already on the worker's list")


class WorkerException(WorkerioException): ...

class WorkerCouldNotAcceptJob(WorkerException): ...
