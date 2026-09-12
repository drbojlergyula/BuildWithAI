"""copay.py — deterministic computation for story S3. Pure functions, no I/O."""

import math

CAP_NOTE = (
    "The co-payment counts toward the annual maximum of CHF 700 (adults) / CHF 350 (children) "
    "— of a 40 % co-payment only 25 points count toward that maximum; the remaining 15 points are uncapped."
)


def round2(x: float) -> float:
    return round(x + 1e-9, 2)


def per_pack_difference(own_price: float, own_share: int, alt_price: float, alt_share: int = 10) -> float:
    """Difference in co-payment per pack once the deductible is used up."""
    return round2(own_share / 100 * own_price - alt_share / 100 * alt_price)


def packs_per_year(units_per_day: float, units_per_pack: int) -> int:
    return math.ceil(365 * units_per_day / units_per_pack)


def yearly_difference(own_price: float, own_share: int, alt_price: float, units_per_day: float, units_per_pack: int) -> float:
    return round2(packs_per_year(units_per_day, units_per_pack) * per_pack_difference(own_price, own_share, alt_price))
