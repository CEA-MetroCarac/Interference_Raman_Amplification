"""
module description
"""
import pytest
from pytest import approx

from amplification_ex.ex_impact_of_layer_of_interest_thickness import loi_amplification as loi
from amplification_ex.ex_impact_of_another_layer_thickness import otherlayer_amplification as nloi


def test_amplification_loi():
    _, intensity = loi(make_plots=False)
    assert intensity[0, 19, 39, 59, 79, 99] == approx([0.038585478078246985,
                                                        0.9913354942927443,
                                                        0.6912498221086218,
                                                        0.42901560306970166,
                                                        0.2754875155236099,
                                                        0.1886722523282841])

def test_amplification_noloi():
    _, intensity = nloi(make_plots=False)
    assert intensity[0, 19, 39, 59, 79, 99] == approx([0.008641562443703265,
                                                        0.40647587286047404,
                                                        0.6744926363012996,
                                                        0.014596913019395011,
                                                        0.24217258819059825,
                                                        0.7605079075998302])