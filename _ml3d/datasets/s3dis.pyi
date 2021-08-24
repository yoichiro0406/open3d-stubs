"""
This type stub file was generated by pyright.
"""

from .utils import BEVBox3D
from .base_dataset import BaseDataset, BaseDatasetSplit

log = ...
class S3DIS(BaseDataset):
    """This class is used to create a dataset based on the S3DIS (Stanford
    Large-Scale 3D Indoor Spaces) dataset, and used in visualizer, training, or
    testing.

    The S3DIS dataset is best used to train models for building indoors.
    """
    def __init__(self, dataset_path, name=..., task=..., cache_dir=..., use_cache=..., class_weights=..., num_points=..., test_area_idx=..., ignored_label_inds=..., ignored_objects=..., test_result_folder=..., **kwargs) -> None:
        """Initialize the function by passing the dataset and other details.

        Args:
            dataset_path: The path to the dataset to use.
            name: The name of the dataset (S3DIS in this case).
            task: One of {segmentation, detection} for semantic segmentation and object detection.
            cache_dir: The directory where the cache is stored.
            use_cache: Indicates if the dataset should be cached.
            class_weights: The class weights to use in the dataset.
            num_points: The maximum number of points to use when splitting the dataset.
            test_area_idx: The area to use for testing. The valid values are 1 through 6.
            ignored_label_inds: A list of labels that should be ignored in the dataset.
            ignored_objects: Ignored objects
            test_result_folder: The folder where the test results should be stored.
        """
        ...
    
    @staticmethod
    def get_label_to_names(): # -> dict[int, str]:
        """Returns a label to names dictonary object.

        Returns:
            A dict where keys are label numbers and
            values are the corresponding names.
        """
        ...
    
    def get_split(self, split): # -> S3DISSplit:
        """Returns a dataset split.

        Args:
            split: A string identifying the dataset split that is usually one of
            'training', 'test', 'validation', or 'all'.

        Returns:
            A dataset split object providing the requested subset of the data.
        """
        ...
    
    def get_split_list(self, split): # -> list[str]:
        ...
    
    def is_tested(self, attr): # -> bool:
        ...
    
    def save_test_result(self, results, attr): # -> None:
        ...
    
    @staticmethod
    def create_ply_files(dataset_path, class_names): # -> None:
        ...
    
    @staticmethod
    def read_bboxes(bboxes, ignored_objects): # -> list[Unknown]:
        ...
    


class S3DISSplit(BaseDatasetSplit):
    """This class is used to create a split for S3DIS dataset.

    Initialize the class.

    Args:
        dataset: The dataset to split.
        split: A string identifying the dataset split that is usually one of
            'training', 'test', 'validation', or 'all'.
        **kwargs: The configuration of the model as keyword arguments.

    Returns:
        A dataset split object providing the requested subset of the data.
    """
    def __init__(self, dataset, split=...) -> None:
        ...
    
    def __len__(self): # -> int:
        ...
    
    def get_data(self, idx): # -> dict[str, Unknown]:
        ...
    
    def get_attr(self, idx): # -> dict[str, Unknown]:
        ...
    


class Object3d(BEVBox3D):
    """Stores object specific details like bbox coordinates."""
    def __init__(self, name, center, size, yaw) -> None:
        ...
    


