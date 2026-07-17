import asyncio
import random
from dataclasses import dataclass
from typing import List

@dataclass
class TaskResult:
    name: str
    duration: float
    success: bool

class AsyncTaskManager:
    def __init__(self):
        self.results: List[TaskResult] = []

    async def worker(self, name: str):
        duration = random.uniform(1, 5)
        print(f"{name} started...")
        await asyncio.sleep(duration)

        success = random.choice([True, True, True, False])

        result = TaskResult(
            name=name,
            duration=duration,
            success=success
        )

        self.results.append(result)
        print(f"{name} finished in {duration:.2f}s")

    async def run(self):
        tasks = [
            asyncio.create_task(self.worker(f"Task-{i}"))
            for i in range(1, 6)
        ]

        await asyncio.gather(*tasks)

        print("\nSummary")
        print("-" * 30)

        for r in self.results:
            print(
                f"{r.name:<10} "
                f"{r.duration:.2f}s "
                f"{'Success' if r.success else 'Failed'}"
            )

        avg = sum(r.duration for r in self.results) / len(self.results)
        print(f"\nAverage Time: {avg:.2f}s")

if __name__ == "__main__":
    manager = AsyncTaskManager()
    asyncio.run(manager.run())