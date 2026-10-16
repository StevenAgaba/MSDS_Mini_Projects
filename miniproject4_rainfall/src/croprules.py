"""
Crop suitability rules.
"""


class CropRule:

    def __init__(self):

        self.crops = {
            "Maize": (70, 200),
            "Beans": (50, 150),
            "Coffee": (100, 250)
        }

    def classify(
        self,
        rainfall
    ):

        suitable = []

        for crop, limits in self.crops.items():

            low, high = limits

            if low <= rainfall <= high:

                suitable.append(
                    crop
                )

        if rainfall < 50:
            return ["Drought Risk"]

        if rainfall > 250:
            return ["Waterlogging Risk"]

        if suitable:
            return suitable

        return ["Marginal"]