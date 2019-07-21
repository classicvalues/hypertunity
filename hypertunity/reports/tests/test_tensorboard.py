# -*- coding: utf-8 -*-
import os
import tempfile
import pytest

from hypertunity.optimisation import base
from hypertunity.optimisation.domain import Domain
from ..tensorboard import TensorboardReporter


@pytest.mark.slow
def test_from_history():
    domain = Domain({"x": [-5., 6.], "y": ("sin", "sqr"), "z": tuple(range(4))})
    n_samples = 10
    with tempfile.TemporaryDirectory() as tmp_dir:
        rep = TensorboardReporter(domain, metrics=["metric_1", "metric_2"], logdir=tmp_dir)
        history = [base.HistoryPoint(sample=domain.sample(),
                                     metrics={"metric_1": base.EvaluationScore(float(i)),
                                              "metric_2": base.EvaluationScore(i*2.)})
                   for i in range(n_samples)]
        rep.from_history(history)
        assert len(os.listdir(tmp_dir)) == n_samples
        for root, dirs, files in os.walk(tmp_dir):
            assert all(map(lambda x: x.startswith("events.out.tfevents"), files))