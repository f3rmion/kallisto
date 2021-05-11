# tests/test_eeq.py

import numpy as np

from tests.store import ch_radical, pyridine


def test_eeq():
    charge = 0
    mol = ch_radical()
    eeq = mol.get_eeq(charge)
    assert np.isclose(eeq[0], -0.17166856)
    assert np.isclose(eeq[1], 0.17166856)


def test_eeq_cation():
    charge = 1
    mol = ch_radical()
    eeq = mol.get_eeq(charge)
    assert np.isclose(eeq[0], 0.59769359)
    assert np.isclose(eeq[1], 0.40230641)


def test_eeq_anion():
    charge = -1
    mol = ch_radical()
    eeq = mol.get_eeq(charge)
    assert np.isclose(eeq[0], -0.94103071)
    assert np.isclose(eeq[1], -0.05896929)


def test_eeq_ies():
    charge = 0
    mol = pyridine()
    ies = True
    eeq = mol.get_eeq(charge, ies)
    assert np.isclose(eeq, -0.05657355)


def test_eeq_ies_cation():
    charge = 1
    mol = pyridine()
    ies = True
    eeq = mol.get_eeq(charge, ies)
    assert np.isclose(eeq, 1.34730585)
