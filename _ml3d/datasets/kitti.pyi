"""
This type stub file was generated by pyright.
"""

from .base_dataset import BaseDataset
from .utils import BEVBox3D

log = ...
class KITTI(BaseDataset):
    """This class is used to create a dataset based on the KITTI dataset, and
    used in object detection, visualizer, training, or testing.
    """
    def __init__(self, dataset_path, name=..., cache_dir=..., use_cache=..., val_split=..., test_result_folder=..., **kwargs) -> None:
        """Initialize the function by passing the dataset and other details.

        Args:
            dataset_path: The path to the dataset to use.
            name: The name of the dataset (KITTI in this case).
            cache_dir: The directory where the cache is stored.
            use_cache: Indicates if the dataset should be cached.
            val_split: The split value to get a set of images for training,
            validation, for testing.
            test_result_folder: Path to store test output.

        Returns:
            class: The corresponding class.
        """
        ...
    
    @staticmethod
    def get_label_to_names(): # -> dict[int, str]:
        """Returns a label to names dictonary object.

        Returns:
            A dict where keys are label numbers and values are the corresponding
            names.
        """
        ...
    
    @staticmethod
    def read_lidar(path):
        """Reads lidar data from the path provided.

        Returns:
            A data object with lidar information.
        """
        ...
    
    @staticmethod
    def read_label(path, calib): # -> list[Unknown]:
        """Reads labels of bound boxes.

        Returns:
            The data objects with bound boxes information.
        """
        ...
    
    @staticmethod
    def read_calib(path): # -> dict[str, ndarray[Unknown, Unknown]]:
        """Reads calibiration for the dataset. You can use them to compare
        modeled results to observed results.

        Returns:
            The camera and the camera image used in calibration.
        """
        ...
    
    def get_split(self, split): # -> KITTISplit:
        """Returns a dataset split.

        Args:
            split: A string identifying the dataset split that is usually one of
            'training', 'test', 'validation', or 'all'.

        Returns:
            A dataset split object providing the requested subset of the data.
        """
        ...
    
    def get_split_list(self, split): # -> List[str] | List[Unknown]:
        """Returns the list of data splits available.

        Args:
            split: A string identifying the dataset split that is usually one of
            'training', 'test', 'validation', or 'all'.

        Returns:
            A dataset split object providing the requested subset of the data.

        Raises:
            ValueError: Indicates that the split name passed is incorrect. The
            split name should be one of 'training', 'test', 'validation', or
            'all'.
        """
        ...
    
    def is_tested(self): # -> None:
        """Checks if a datum in the dataset has been tested.

        Args:
            dataset: The current dataset to which the datum belongs to.
            attr: The attribute that needs to be checked.

        Returns:
            If the dataum attribute is tested, then resturn the path where the
            attribute is stored; else, returns false.
        """
        ...
    
    def save_test_result(self, results, attrs): # -> None:
        """Saves the output of a model.

        Args:
            results: The output of a model for the datum associated with the
            attribute passed.
            attrs: The attributes that correspond to the outputs passed in
            results.
        """
        ...
    


class KITTISplit:
    def __init__(self, dataset, split=...) -> None:
        ...
    
    def __len__(self): # -> int:
        ...
    
    def get_data(self, idx): # -> dict[str, Unknown]:
        ...
    
    def get_attr(self, idx): # -> dict[str, Unknown]:
        ...
    


class Object3d(BEVBox3D):
    """The class stores details that are object-specific, such as bounding box
    coordinates, occulusion and so on.
    """
    def __init__(self, center, size, label, calib=...) -> None:
        ...
    
    def get_difficulty(self): # -> Literal[0, 1, 2, -1]:
        """The method determines difficulty level of the object, such as Easy,
        Moderate, or Hard.
        """
        ...
    
    def to_str(self): # -> str:
        ...
    


