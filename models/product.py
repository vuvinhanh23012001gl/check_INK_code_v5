class Product:
    def __init__(self, id: int, name: str, description: str = "", path_img_product: str = ""):
        self._id = id
        self._name = name
        self._description = description
        self.path_img_product = path_img_product
        # metadata
        self.created_at = ""
        self.updated_at = ""

    # -------- id --------
    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, value: int) -> bool:
        if isinstance(value, int) and value > 0:
            self._id = value
            return True
        return False

    # -------- name --------
    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value.strip() if value else ""

    # -------- description --------
    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, value: str):
        self._description = value or ""

    # -------- helper --------
    def __repr__(self):
        return (
            f"Product("
            f"id={self._id}, "
            f"name='{self._name}', "
            f"created='{self.created_at}'"
            f")"
        )

    def to_dict(self) -> dict:
        return {
            "id": self._id,
            "name": self._name,
            "description": self._description,

            # Metadata
            "created_at": str(self.created_at) if self.created_at else "",
            "updated_at": str(self.updated_at) if self.updated_at else "",
            "path_img_product":self.path_img_product
        }
    
    @classmethod
    def from_dict(
        cls,
        data: dict
    ):

        if not isinstance(data, dict):
            raise TypeError(
                "data must be dict"
            )

        product = cls(

            id=str(
                data.get("id", "")
            ),

            name=str(
                data.get("name", "")
            ),

            description=str(
                data.get(
                    "description",
                    ""
                )
            ),

            path_img_product=str(
                data.get(
                    "path_img_product",
                    ""
                )
            )
        )

        product.created_at = str(
            data.get(
                "created_at",
                ""
            )
        )

        product.updated_at = str(
            data.get(
                "updated_at",
                ""
            )
        )

        return product