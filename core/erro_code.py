from enum import Enum
class ErrorCode(Enum):
    # Product
    PRODUCT_ALREADY_EXISTED = 1000
    PRODUCT_DOSE_NOT_EXIST = 1001


ERROR_MESSAGE = {
    ErrorCode.PRODUCT_ALREADY_EXISTED: "[Thất bại] thêm sản phẩm đã tồn tại. Hãy tạo lại mã sản phẩm khác với mã hiện tại.",
    ErrorCode.PRODUCT_DOSE_NOT_EXIST:"[Thất bại] Xóa sản phẩm không thành công vì sản phẩm không tồn tại"
}