from enum import Enum
from typing import (
    Iterable,
    Optional,
    Sequence,
    overload,
    Union,
    ClassVar,
    Tuple,
    Any,
    List,
)
from numpy import ndarray

class Device:
    class DeviceType(Enum):
        CPU = ...
        CUDA = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, device_type: Union[str, DeviceType], device_id: int) -> None: ...
    @overload
    def __init__(self, type_colon_id: str) -> None: ...
    def get_id(self) -> int: ...
    def get_type(self) -> DeviceType: ...

class DtypeCode(Enum):
    Bool = ...
    Float = ...
    Int = ...
    Object = ...
    UInt = ...
    Undefined = ...

class Dtype:
    Bool: ClassVar[Dtype]
    Float32: ClassVar[Dtype]
    Float64: ClassVar[Dtype]
    Int16: ClassVar[Dtype]
    Int32: ClassVar[Dtype]
    Int64: ClassVar[Dtype]
    Int8: ClassVar[Dtype]
    UInt16: ClassVar[Dtype]
    UInt32: ClassVar[Dtype]
    UInt64: ClassVar[Dtype]
    UInt8: ClassVar[Dtype]
    Undefined: ClassVar[Dtype]
    def __init__(self, dtype_code: DtypeCode, byte_size: int, name: str) -> None: ...
    def byte_code(self) -> DtypeCode: ...
    def byte_size(self) -> int: ...

class DynamicSizeVector:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, other: DynamicSizeVector) -> None: ...
    @overload
    def __init__(self, dim_sizes: Iterable) -> None: ...
    def append(self, x: Optional[int]) -> None: ...
    def clear(self) -> None: ...
    def count(self, x: Optional[int]) -> int: ...
    def extend(self, L: Union[DynamicSizeVector, Iterable]) -> None: ...
    def insert(self, i: int, x: Optional[int]) -> None: ...
    def pop(self, i: Optional[int] = None) -> Optional[int]: ...
    def remove(self, x: Optional[int]) -> None: ...

class SizeVector:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, other: SizeVector) -> None: ...
    @overload
    def __init__(self, dim_sizes: Iterable) -> None: ...
    def append(self, x: int) -> None: ...
    def clear(self) -> None: ...
    def count(self, x: int) -> int: ...
    def extend(self, L: Union[SizeVector, Iterable]) -> None: ...
    def insert(self, i: int, x: int) -> None: ...
    def pop(self, i: Optional[int] = None) -> int: ...
    def remove(self, x: int) -> None: ...

class HashMap:
    def __init__(
        self,
        init_capacity: int,
        dtype_key: Dtype,
        dtype_value: Dtype,
        element_shape_key: SizeVector,
        element_shape_value: SizeVector,
        device: Device = Device("CPU:0"),
    ) -> None: ...
    def activate(self, keys: Tensor) -> Tuple[Tensor, Tensor]: ...
    def capacity(self) -> int: ...
    def clone(self) -> HashMap: ...
    def cpu(self) -> HashMap: ...
    def cuda(self, device_id: int = 0) -> HashMap: ...
    def erase(self, keys: Tensor) -> Tensor: ...
    def find(self, keys: Tensor) -> Tuple[Tensor, Tensor]: ...
    def get_active_addrs(self) -> Tensor: ...
    def get_key_buffer(self) -> Tensor: ...
    def get_key_tensor(self) -> Tensor: ...
    def get_value_buffer(self) -> Tensor: ...
    def get_value_tensor(self) -> Tensor: ...
    def insert(self, keys: Tensor, values: Tensor) -> Tuple[Tensor, Tensor]: ...
    def rehash(self, buckets: int) -> None: ...
    def size(self) -> int: ...
    def to(self, device: Device, copy: bool = False) -> HashMap: ...

class Scalar:
    def __init__(self, v: Union[float, int, bool]) -> None: ...

class Tensor:
    @overload
    def __init__(
        self,
        np_array: ndarray,
        dtype: Optional[Dtype] = None,
        device: Optional[Device] = None,
    ) -> None: ...
    @overload
    def __init__(
        self,
        scalar_value: Union[bool, int, float],
        dtype: Optional[Dtype] = None,
        device: Optional[Device] = None,
    ) -> None: ...
    @overload
    def __init__(
        self,
        shape: Sequence[int],
        dtype: Optional[Dtype] = None,
        device: Optional[Device] = None,
    ) -> None: ...
    def abs(self) -> Tensor: ...
    def abs_(self) -> Tensor: ...
    def add(self, value: Union[Scalar, Tensor]) -> Tensor: ...
    def add_(self, value: Union[Scalar, Tensor]) -> Tensor: ...
    def all(self) -> bool: ...
    def allclose(
        self, other: Tensor, rtol: float = 1e-05, atol: float = 1e-08
    ) -> bool: ...
    def any(self) -> bool: ...
    @overload
    @classmethod
    def arange(
        cls,
        stop: Union[int, float],
        dtype: Optional[Dtype] = None,
        device: Optional[Device] = None,
    ) -> Tensor: ...
    @overload
    @classmethod
    def arange(
        cls,
        start: Union[int, float, None],
        stop: Union[int, float, None],
        dtype: Optional[Dtype] = None,
        device: Optional[Device] = None,
    ) -> Tensor: ...
    def argmax(self, dim: Optional[SizeVector] = None) -> Tensor: ...
    def argmin(self, dim: Optional[SizeVector] = None) -> Tensor: ...
    def ceil(self) -> Tensor: ...
    def clip(self, min_val: Scalar, max_val: Scalar) -> Tensor: ...
    def clip_(self, min_val: Scalar, max_val: Scalar) -> Tensor: ...
    def clone(self) -> Tensor: ...
    def contiguous(self) -> Tensor: ...
    def cos(self) -> Tensor: ...
    def cos_(self) -> Tensor: ...
    def cpu(self) -> Tensor: ...
    def cuda(self, device_id: int = 0) -> Tensor: ...
    def det(self) -> float: ...
    @classmethod
    def diag(cls, input: Tensor) -> Tensor: ...
    def div(self, value: Union[Scalar, Tensor]) -> Tensor: ...
    def div_(self, value: Union[Scalar, Tensor]) -> Tensor: ...
