from pathlib import Path
from utills import File

class ProductPathData:
    NAME_FILE_PRODUCTS = "products.json"
    def __init__(
        self,
        path_base: str | Path
    ):

        self.path_base = (
            self._validate_path(path_base)
        )

        self.path_file_products = (
            self.path_base
            / self.NAME_FILE_PRODUCTS
        )

    def _validate_path(
        self,
        path_base: str | Path
    ) -> Path:

        if not isinstance(
            path_base,
            (str, Path)
        ):
            raise TypeError(
                "path_base must be str or Path"
            )

        return Path(path_base)

# # test tạo thành công
# product = ProductPathData(
#     id="product_1",
#     path_base="data/products"
# )
# print(product.id)
# print(product.path_base)
# print(product.folder_id)
