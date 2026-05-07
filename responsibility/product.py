
from models import Product
from utills import File
from path_structure import ProductPathData


class ProductRepository:

    def __init__(self, product_base : ProductPathData):
        self.product_base =  product_base

    @property
    def file_path(self):
        """
        đường dẫn file products.json
        """
        return self.product_base.path_file_products

    def load(self) -> dict[str, Product]:
        """
        đọc json -> dict Product
        """

        data = File.read_json(
            self.file_path,
            default={}
        )
        dict_products: dict[str, Product] = {}

        for product_id, product_data in data.items():

            product = Product.from_dict(
                product_data
            )

            dict_products[product_id] = product
        return dict_products


    def save(
        self,
        dict_products: dict[str, Product]
    ):
        """
        lưu dict Product xuống json
        """

        data = {
            product_id: product.to_dict()
            for product_id, product
            in dict_products.items()
        }

        File.save_json(
            self.file_path,
            data
        )

    def exists(self, product_id: str) -> bool:
        """
        kiểm tra product tồn tại
        """

        dict_products = self.load()

        return product_id in dict_products

    def get_by_id(
        self,
        product_id: str
    ) -> Product | None:
        """
        lấy product theo id
        """

        dict_products = self.load()

        return dict_products.get(product_id)

    def get_all(self) -> list[Product]:
        """
        lấy toàn bộ product
        """

        dict_products = self.load()

        return list(dict_products.values())