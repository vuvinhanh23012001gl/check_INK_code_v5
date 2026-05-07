from models import Product,Result
from responsibility import ProductRepository
from utills import File
from core.erro_code import  ErrorCode
import cv2
import shutil
from datetime import datetime

class ProductService:
    def __init__(
        self,
        repository: ProductRepository
    ):
        if not isinstance(
            repository,
            ProductRepository
        ):
            raise TypeError(
                "repository must be ProductRepository"
            )
        self.repository = repository
        self.dict_products_obj = (
            self.repository.load()
        )




    def now_str(self):
        return datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
    
    def create_product_folder(
        self,
        product: Product
    ):
        path_product = (
            self.repository.product_base
            / str(product.id)
        )  
        File.create_folder(path_product)
        product.path_img_product = str(
            path_product
        )


    def add_product(
        self,
        product: Product,
        image=None
    ):

        product_id = str(product.id)

        if product_id in self.dict_products_obj:

            return Result.Fail(
                ErrorCode.PRODUCT_ALREADY_EXISTED
            )

        # time create
        product.created_at = self.now_str()

        product.updated_at = self.now_str()

        # tạo folder
        self.create_product_folder(
            product
        )

        # save image
        if image is not None:

            self.save_image_product(
                product,
                image
            )

        # add dict
        self.dict_products_obj[
            product_id
        ] = product

        # save json
        self.repository.save(
            self.dict_products_obj
        )

        return Result.Ok()


    def update_product(
        self,
        product: Product
    ):
        if not isinstance(
            product,
            Product
        ):
            raise TypeError(
                "product must be Product"
            )

        product_id = str(product.id)

        if product_id not in self.dict_products_obj:

            return Result.Fail(
                ErrorCode.PRODUCT_DOSE_NOT_EXIST
            )
        # giữ nguyên created_at
        old_product = (
            self.dict_products_obj[
                product_id
            ]
        )

        product.created_at = (
            old_product.created_at
        )
        # update time
        product.updated_at = self.now_str()

        self.dict_products_obj[
            product_id
        ] = product

        self.repository.save(
            self.dict_products_obj
        )
        return Result.Ok()


    def remove_product(
        self,
        product_id: str
    ):
        """
        xóa product
        """
        if product_id not in self.dict_products_obj:

            return Result.Fail(
                ErrorCode.PRODUCT_DOSE_NOT_EXIST
            )

        # path folder product
        path_product = (
            self.repository.product_base
            / str(product_id)
        )

        # xóa folder nếu tồn tại
        if path_product.exists():
            shutil.rmtree(path_product)
        # xóa dict
        del self.dict_products_obj[
            product_id
        ]
        # save json
        self.repository.save(
            self.dict_products_obj
        )
        return Result.Ok()

    def get_product(
        self,
        product_id: str
    ) -> Product | None:
        """
        lấy product theo id
        """
        return self.dict_products_obj.get(
            product_id
        )

    def get_all_products(
        self
    ) -> list[Product]:
        """
        lấy toàn bộ product
        """
        return list(
            self.dict_products_obj.values()
        )

    def exists_product(
        self,
        product_id: str
    ) -> bool:
        """
        kiểm tra tồn tại
        """

        return (
            product_id
            in self.dict_products_obj
        )


    def count_products(self) -> int:
        """
        đếm số lượng product
        """
        return len(
            self.dict_products_obj
        )
    

    def save_image_product(self, product: Product, image):
        folder_product = (
            self.repository.product_base
            / str(product.id)
        )
        File.create_folder(folder_product)
        path_image = folder_product / f"{product.id}.jpg"
        cv2.imwrite(str(path_image), image)
        product.path_img_product = str(
            path_image.relative_to(self.repository.product_base)
        )
        self.dict_products_obj[str(product.id)] = product
        return path_image


# from models import Product
# from responsibility import ProductRepository
# import numpy as np
# from config.product_config import ProductConfig

# def test_product_service():

#     repository = ProductRepository(
#         ProductConfig.path,"vuvinhanh.json"
#     )

#     service = ProductService(
#         repository
#     )

#     # create product
#     product = Product(
#         id="P05",
#         name="kẹo dâu",
#         description="kẹo vị dâu"
#     )

#     # create image
#     image = np.zeros(
#         (300, 300, 3),
#         dtype=np.uint8
#     )

#     image[:] = (0, 255, 0)

#     # add
#     result = service.add_product(
#         product,
#         image
#     )

#     print(
#         "ADD:",
#         result.message()
#     )

    # # get
    # product_get = service.get_product(
    #     "P05"
    # )

    # print(
    #     "GET:",
    #     product_get
    # )

    # # update
    # product_update = Product(
    #     id="P05",
    #     name="kẹo cam",
    #     description="kẹo vị cam"
    # )

    # result = service.update_product(
    #     product_update
    # )

    # print(
    #     "UPDATE:",
    #     result.message()
    # )

    # # exists
    # print(
    #     "EXISTS:",
    #     service.exists_product("P05")
    # )

    # # count
    # print(
    #     "COUNT:",
    #     service.count_products()
    # )

    # # all products
    # print(
    #     "ALL:",
    #     service.get_all_products()
    # )

    # # remove
    # result = service.remove_product(
    #     "P05"
    # )

    # print(
    #     "REMOVE:",
    #     result.message()
    # )

    # print(
    #     "EXISTS AFTER REMOVE:",
    #     service.exists_product("P05")
    # )


# if __name__ == "__main__":

#     test_product_service()