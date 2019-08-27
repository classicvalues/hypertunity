from typing import List

from hypertunity.optimisation.base import Optimiser
from hypertunity.optimisation.domain import Domain, Sample


class RandomSearch(Optimiser):
    def __init__(self, domain, batch_size=1, seed=None):
        """Initialise the RandomSearch.

        If seed is provided the Domain is seeded.

        Args:
            domain: `Domain` of the objective to optimise. Will be sampled uniformly using the
                `sample()` method of the `Domain` object.
            batch_size: int, the number of samples to return at one step.
            seed: optional, int to seed the domain.
        """
        if seed is not None:
            domain = Domain(domain.as_dict(), seed=seed)
        super(RandomSearch, self).__init__(domain, batch_size)

    def run_step(self) -> List[Sample]:
        """Sample uniformly the domain `self.batch_size` number of times."""
        return [self.domain.sample() for _ in range(self.batch_size)]
