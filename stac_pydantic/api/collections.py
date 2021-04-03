from typing import List

from pydantic import BaseModel

from ..collection import Collection
from ..shared import Link
from ..version import STAC_VERSION


class Collections(BaseModel):
    """
    http://docs.opengeospatial.org/is/17-069r3/17-069r3.html#_feature_collections_rootcollections
    """

    links: List[Link]
    collections: List[Collection]