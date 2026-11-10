"""Legacy replenishment helper (mirror copy)."""


def suggested_order(on_hand, reorder_point):
    # legacy rule: order enough to reach the reorder point once
    return max(0, int(reorder_point) - int(on_hand))
