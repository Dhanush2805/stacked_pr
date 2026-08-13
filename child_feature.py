# child_feature.py

from parent_feature import parent_feature


def child_feature():
    return f"Child uses: {parent_feature()}"