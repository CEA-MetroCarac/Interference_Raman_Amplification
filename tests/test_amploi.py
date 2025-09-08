"""
module description
"""
from pytest import approx

from examples.ex_impact_of_layer_of_interest_thickness import loi_amplification as loi
from examples.ex_impact_of_another_layer_thickness import otherlayer_amplification as nloi

SLICE = [0, 19, 39, 59, 79, 99]


def test_amplification_loi():
    _, intensity = loi(make_plots=False)
    # print(intensity[SLICE])

    assert intensity[SLICE] == approx([0.02565086,
                                       0.95216651,
                                       0.95215546,
                                       0.77618384,
                                       0.60513513,
                                       0.47097518])


def test_amplification_noloi():
    _, intensity = nloi(make_plots=False)
    # print(intensity[SLICE])

    assert intensity[SLICE] == approx([0.008641562443703265,
                                       0.40647587286047404,
                                       0.6744926363012996,
                                       0.014596913019395011,
                                       0.24217258819059825,
                                       0.7605079075998302])
