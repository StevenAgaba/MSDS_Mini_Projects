"""
Risk assessment model.
"""

import numpy as np


class RiskAssessment:
    """
    Revenue-risk classification.
    """

    def classify(self, cv):

        if cv < 0.15:
            return "Low Risk"

        elif cv < 0.30:
            return "Moderate Risk"

        else:
            return "High Risk"

    def value_at_risk(
        self,
        revenues,
        level=5
    ):

        return np.percentile(
            revenues,
            level
        )