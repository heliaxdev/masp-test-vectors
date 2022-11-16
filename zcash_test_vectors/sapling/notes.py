#!/usr/bin/env python3
import sys; assert sys.version_info[0] >= 3, "Python 3 required."

from hashlib import blake2s

from .pedersen import (
    mixing_pedersen_hash,
    windowed_pedersen_commitment,
)
from ..utils import i2lebsp, leos2bsp


def note_commit(rcm, g_d, pk_d, v, asset_type):
    digest = blake2s(asset_type, person=b'MASP__v_')
    from .jubjub import Point
    asset_generator = leos2bsp(bytes(Point.from_bytes(digest.digest())))
    return windowed_pedersen_commitment(rcm, [1] * 6 + asset_generator + i2lebsp(64, v) + g_d + pk_d)

def prf_nf_sapling(nk_star, rho_star):
    digest = blake2s(person=b'MASP__nf')
    digest.update(nk_star)
    digest.update(rho_star)
    return digest.digest()

def note_nullifier(nk, cm, pos):
    rho = mixing_pedersen_hash(cm, pos)
    return prf_nf_sapling(bytes(nk), bytes(rho))
